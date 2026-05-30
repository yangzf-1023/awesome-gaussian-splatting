#!/usr/bin/env python3
"""Daily arXiv crawler for Gaussian Splatting papers.

Pipeline:
  1. Query arXiv with phrase-quoted full-text search (title + abstract + comments).
  2. Apply local strong/negative keyword guard to reduce false positives.
  3. Dedup against data/seen.json.
  4. Classify each new paper into a topic bucket.
  5. (Optional) Generate Chinese TL;DR via OpenAI-compatible endpoint.
  6. Append each new paper to its per-topic file under topics/<slug>.md.
  7. Rewrite README's TOPIC-INDEX and LATEST blocks (only the most recent day
     is shown inline; full per-topic history lives in topics/).
  8. Archive day blocks older than RETAIN_DAYS into papers/YYYY-MM.md
     (kept for backwards-compatible chronological browsing).
  9. (Optional) Push a digest card to Feishu via webhook.
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
from topics_writer import append_papers, regenerate_index, topic_counts

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
INDEX_START = "<!-- TOPIC-INDEX-START -->"
INDEX_END = "<!-- TOPIC-INDEX-END -->"
LATEST_START = "<!-- LATEST-START -->"
LATEST_END = "<!-- LATEST-END -->"

NAME_TO_SLUG = {name: slug for name, slug in topic_order()}


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


def _sanitize_for_details(text: str) -> str:
    """Make abstract safe inside <details>: collapse whitespace, escape closing tag."""
    t = re.sub(r"\s+", " ", text).strip()
    return t.replace("</details>", "<\\/details>")


def render_entry(p: dict) -> str:
    tldr = p.get("tldr_zh", "")
    summary = p.get("summary", "")
    lines = [
        f"- **[{p['title']}]({p['link']})**  ",
        f"  *{p['authors']}*  ",
        f"  `{p['published']}` · `{p['primary_category']}` · [abs]({p['link']}) · [pdf]({p['pdf']})",
    ]
    if tldr:
        lines.append(f"  > 💡 {tldr}")
    if summary:
        clean = _sanitize_for_details(summary)
        lines.append("")
        lines.append("  <details><summary>Abstract</summary>")
        lines.append("")
        lines.append(f"  {clean}")
        lines.append("")
        lines.append("  </details>")
    return "\n".join(lines) + "\n"


def group_by_topic(papers: list[dict]) -> "dict[str, list[dict]]":
    grouped: dict[str, list[dict]] = {}
    for name, _ in topic_order():
        grouped[name] = []
    for p in papers:
        grouped.setdefault(p["topic"], []).append(p)
    return {k: v for k, v in grouped.items() if v}


def _slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "topic"


def _replace_block(text: str, start: str, end: str, new_inner: str) -> str:
    """Replace text between markers; create block if missing."""
    if start in text and end in text:
        pre, rest = text.split(start, 1)
        _, post = rest.split(end, 1)
        return pre + start + "\n" + new_inner.rstrip() + "\n" + end + post
    # If markers missing, no-op (defensive)
    return text


def render_topic_index(counts: dict, latest_grouped: dict) -> str:
    lines = [
        "",
        "| # | Topic | Total Papers | Latest-day Δ | Browse |",
        "|---|---|---|---|---|",
    ]
    for i, (name, _slug) in enumerate(topic_order(), 1):
        slug = NAME_TO_SLUG.get(name, _slugify(name))
        total = counts.get(name, 0)
        delta = len(latest_grouped.get(name, []))
        delta_cell = f"**+{delta}**" if delta else "—"
        lines.append(
            f"| {i} | **{name}** | {total} | {delta_cell} | "
            f"[topics/{slug}.md](topics/{slug}.md) |"
        )
    lines.append("")
    return "\n".join(lines)


def render_latest_block(date_str: str, grouped: dict, total: int) -> str:
    lines = ["", f"### {date_str} (UTC) — {total} new paper(s)", ""]
    if not grouped:
        lines.append("_No new papers today._")
        lines.append("")
        return "\n".join(lines)
    for name, papers in grouped.items():
        slug = NAME_TO_SLUG.get(name, _slugify(name))
        lines.append(
            f"<details><summary><b>{name}</b> ({len(papers)}) · "
            f"<a href=\"topics/{slug}.md\">full list →</a></summary>"
        )
        lines.append("")
        for p in papers:
            lines.append(render_entry(p))
            lines.append("")
        lines.append("</details>")
        lines.append("")
    return "\n".join(lines)


def update_readme(date_str: str, papers: list[dict]) -> None:
    """Rewrite the AUTO-GENERATED area: topic index + latest day only."""
    content = README.read_text(encoding="utf-8")
    if START_MARKER not in content or END_MARKER not in content:
        raise RuntimeError("README markers missing")

    grouped = group_by_topic(papers) if papers else {}
    counts = topic_counts()  # already includes today's after append_papers ran

    topic_index = render_topic_index(counts, grouped)
    latest_block = render_latest_block(date_str, grouped, len(papers))

    # If sub-markers exist, do targeted replacements; otherwise rebuild full body.
    if INDEX_START in content and LATEST_START in content:
        content = _replace_block(content, INDEX_START, INDEX_END, topic_index)
        content = _replace_block(content, LATEST_START, LATEST_END, latest_block)
        README.write_text(content, encoding="utf-8")
        return

    pre, rest = content.split(START_MARKER, 1)
    _, post = rest.split(END_MARKER, 1)
    body = (
        "\n\n"
        "## Browse by topic\n\n"
        "Each topic file accumulates every paper this repo has ever ingested in that bucket, newest first.\n\n"
        f"{INDEX_START}\n{topic_index.rstrip()}\n{INDEX_END}\n\n"
        "## Latest update\n\n"
        f"Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into "
        f"[`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).\n\n"
        f"{LATEST_START}\n{latest_block.rstrip()}\n{LATEST_END}\n\n"
    )
    README.write_text(pre.rstrip() + "\n\n" + START_MARKER + body + END_MARKER + post, encoding="utf-8")


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

        # 1) Append to per-topic files FIRST so topic_counts() reflects today.
        grouped = group_by_topic(new_papers)
        try:
            append_papers(today, grouped, render_entry)
            regenerate_index()
        except Exception as e:
            print(f"[warn] topic writer raised: {e}", file=sys.stderr)

        # 2) Rewrite README index + latest block
        update_readme(today, new_papers)

        for p in new_papers:
            seen[p["id"]] = p["published"]
        save_json(SEEN_FILE, seen)

        try:
            feishu_notify(today, len(new_papers), grouped, REPO_URL)
        except Exception as e:
            print(f"[warn] feishu notify raised: {e}", file=sys.stderr)
    else:
        # Still refresh the README's "latest" block so the date marker is current.
        try:
            update_readme(today, [])
        except Exception as e:
            print(f"[warn] update_readme (no papers) raised: {e}", file=sys.stderr)

    # Monthly archive keeps backwards-compatible chronological view.
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
