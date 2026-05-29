#!/usr/bin/env python3
"""Daily arXiv crawler for Gaussian Splatting papers.

Pipeline:
  1. Query arXiv with phrase-quoted full-text search (title + abstract + comments).
  2. Apply local strong/negative keyword guard to reduce false positives.
  3. Dedup against data/seen.json.
  4. Classify each new paper into a topic bucket.
  5. (Optional) Generate Chinese TL;DR via OpenAI-compatible endpoint.
  6. Rewrite the AUTO-GENERATED block in README.md, grouped by topic.
  7. Archive day blocks older than RETAIN_DAYS into papers/YYYY-MM.md.
  8. (Optional) Push a digest card to Feishu via webhook.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

import feedparser
import requests

from classify import classify, topic_order
from feishu_notify import notify as feishu_notify
from tldr import enrich as tldr_enrich
from archive import archive_old_blocks

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SEEN_FILE = ROOT / "data" / "seen.json"
META_FILE = ROOT / "data" / "meta.json"

ARXIV_API = "http://export.arxiv.org/api/query"

PHRASE_QUERIES = [
    '"gaussian splatting"',
    '"gaussian splat"',
    '"3d gaussian"',
    '"4d gaussian"',
    '"3dgs"',
    '"4dgs"',
]

STRONG_POSITIVES = [
    re.compile(r"\bgaussian splatting\b", re.I),
    re.compile(r"\bgaussian splat\b", re.I),
    re.compile(r"\b3d ?gs\b", re.I),
    re.compile(r"\b4d ?gs\b", re.I),
    re.compile(r"\b3d gaussians?\b", re.I),
    re.compile(r"\b4d gaussians?\b", re.I),
]

NEGATIVE_PATTERNS = [
    re.compile(r"\bgaussian process(es)?\b", re.I),
    re.compile(r"\bgaussian mixture\b", re.I),
    re.compile(r"\bgaussian noise\b", re.I),
    re.compile(r"\bgaussian beam\b", re.I),
    re.compile(r"\bgaussian kernel\b", re.I),
    re.compile(r"\bgaussian distribution\b", re.I),
    re.compile(r"\bgaussian random\b", re.I),
]

MAX_RESULTS = 200
REQUEST_TIMEOUT = 60
SLEEP_BETWEEN = 3

REPO_URL = "https://github.com/yangzf-1023/awesome-gaussian-splatting"

START_MARKER = "<!-- AUTO-GENERATED-START -->"
END_MARKER = "<!-- AUTO-GENERATED-END -->"


def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def is_relevant(title: str, summary: str) -> bool:
    blob = f"{title}\n{summary}"
    if not any(p.search(blob) for p in STRONG_POSITIVES):
        return False
    unambiguous = re.search(
        r"\bgaussian splatt(ing|er)?\b|\b3d ?gs\b|\b4d ?gs\b", blob, re.I
    )
    if unambiguous:
        return True
    if any(n.search(blob) for n in NEGATIVE_PATTERNS):
        return False
    return True


def fetch_query(query: str) -> list[dict]:
    params = {
        "search_query": f"all:{query}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "start": 0,
        "max_results": MAX_RESULTS,
    }
    url = f"{ARXIV_API}?{urlencode(params)}"
    print(f"[fetch] {url}")
    resp = requests.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    feed = feedparser.parse(resp.text)

    kept = []
    for entry in feed.entries:
        title = re.sub(r"\s+", " ", (entry.get("title") or "").strip())
        summary = re.sub(r"\s+", " ", (entry.get("summary") or "").strip())
        if not is_relevant(title, summary):
            continue

        raw_id = entry.get("id", "")
        m = re.search(r"abs/([^v\s]+)", raw_id)
        if not m:
            continue
        arxiv_id = m.group(1)

        authors = ", ".join(a.get("name", "") for a in entry.get("authors", []))
        primary = ""
        if entry.get("tags"):
            primary = entry["tags"][0].get("term", "")

        topic_name, topic_slug = classify(f"{title}\n{summary}")

        kept.append({
            "id": arxiv_id,
            "title": title,
            "authors": authors,
            "summary": summary,
            "link": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            "published": entry.get("published", "")[:10],
            "primary_category": primary,
            "topic": topic_name,
            "topic_slug": topic_slug,
        })
    print(f"[fetch] query={query!r}: kept {len(kept)} / scanned {len(feed.entries)}")
    return kept


def render_entry(p: dict) -> str:
    tldr = p.get("tldr_zh", "")
    lines = [
        f"- **[{p['title']}]({p['link']})**  ",
        f"  *{p['authors']}*  ",
        f"  `{p['published']}` · `{p['primary_category']}` · [abs]({p['link']}) · [pdf]({p['pdf']})",
    ]
    if tldr:
        lines.append(f"  > 💡 {tldr}")
    return "\n".join(lines) + "\n"


def group_by_topic(papers: list[dict]) -> "dict[str, list[dict]]":
    grouped: dict[str, list[dict]] = {}
    for name, _ in topic_order():
        grouped[name] = []
    for p in papers:
        grouped.setdefault(p["topic"], []).append(p)
    return {k: v for k, v in grouped.items() if v}


def render_day_block(date_str: str, papers: list[dict]) -> str:
    grouped = group_by_topic(papers)
    lines = [f"### {date_str} (UTC) — {len(papers)} new paper(s)\n"]
    for topic, items in grouped.items():
        lines.append(f"#### {topic} ({len(items)})\n")
        for p in items:
            lines.append(render_entry(p))
        lines.append("")
    return "\n".join(lines)


def update_readme(date_str: str, papers: list[dict]) -> None:
    content = README.read_text(encoding="utf-8")
    if START_MARKER not in content or END_MARKER not in content:
        raise RuntimeError("README markers missing")

    pre, rest = content.split(START_MARKER, 1)
    old_block, post = rest.split(END_MARKER, 1)

    parts = [START_MARKER, ""]
    if papers:
        parts.append(render_day_block(date_str, papers))

    prev = old_block.strip()
    if prev and not prev.startswith("_No papers fetched yet"):
        parts.append(prev)
        parts.append("")

    parts.append(END_MARKER)
    README.write_text(pre + "\n".join(parts) + post, encoding="utf-8")


def main() -> int:
    seen: dict[str, str] = load_json(SEEN_FILE, {})
    collected: dict[str, dict] = {}

    for q in PHRASE_QUERIES:
        try:
            for p in fetch_query(q):
                if p["id"] in seen or p["id"] in collected:
                    continue
                collected[p["id"]] = p
        except Exception as e:
            print(f"[warn] query failed {q!r}: {e}", file=sys.stderr)
        time.sleep(SLEEP_BETWEEN)

    new_papers = sorted(collected.values(), key=lambda x: x["published"], reverse=True)
    print(f"[result] {len(new_papers)} new paper(s) after dedup + filter")

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    moved = 0

    if new_papers:
        # LLM enrichment (silent no-op if env vars unset)
        try:
            tldr_enrich(new_papers)
        except Exception as e:
            print(f"[warn] tldr enrich raised: {e}", file=sys.stderr)

        update_readme(today, new_papers)
        for p in new_papers:
            seen[p["id"]] = p["published"]
        save_json(SEEN_FILE, seen)

        grouped = group_by_topic(new_papers)
        try:
            feishu_notify(today, len(new_papers), grouped, REPO_URL)
        except Exception as e:
            print(f"[warn] feishu notify raised: {e}", file=sys.stderr)

    # Run monthly archival regardless (handles late catch-up too).
    try:
        moved = archive_old_blocks()
        if moved:
            print(f"[archive] moved {moved} day block(s) to papers/")
    except Exception as e:
        print(f"[warn] archive raised: {e}", file=sys.stderr)

    save_json(META_FILE, {
        "last_updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_seen": len(seen),
        "added_this_run": len(new_papers),
        "archived_this_run": moved,
    })
    return 0


if __name__ == "__main__":
    sys.exit(main())
