#!/usr/bin/env python3
"""Daily arXiv crawler for Gaussian Splatting papers.

Fetches the latest submissions across a set of CV/GR categories, filters by
Gaussian-Splatting-related keywords, dedups against data/seen.json, and
prepends new entries into README.md between the AUTO-GENERATED markers.
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

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SEEN_FILE = ROOT / "data" / "seen.json"
META_FILE = ROOT / "data" / "meta.json"

ARXIV_API = "http://export.arxiv.org/api/query"
CATEGORIES = ["cs.CV", "cs.GR", "cs.LG", "cs.AI", "eess.IV"]
KEYWORDS = [
    "gaussian splatting",
    "gaussian splat",
    "3d gaussian",
    "4d gaussian",
    "3dgs",
    "4dgs",
]
MAX_RESULTS = 200          # per category per run
REQUEST_TIMEOUT = 60       # seconds
SLEEP_BETWEEN = 3          # be nice to arXiv

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


def matches_keyword(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in KEYWORDS)


def fetch_category(cat: str) -> list[dict]:
    params = {
        "search_query": f"cat:{cat}",
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

    papers = []
    for entry in feed.entries:
        title = (entry.get("title") or "").strip().replace("\n", " ")
        title = re.sub(r"\s+", " ", title)
        summary = (entry.get("summary") or "").strip().replace("\n", " ")
        if not (matches_keyword(title) or matches_keyword(summary)):
            continue

        # arXiv id, e.g. http://arxiv.org/abs/2501.12345v1
        raw_id = entry.get("id", "")
        m = re.search(r"abs/([^v\s]+)", raw_id)
        if not m:
            continue
        arxiv_id = m.group(1)

        authors = ", ".join(a.get("name", "") for a in entry.get("authors", []))
        link = f"https://arxiv.org/abs/{arxiv_id}"
        pdf = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        published = entry.get("published", "")[:10]

        papers.append({
            "id": arxiv_id,
            "title": title,
            "authors": authors,
            "link": link,
            "pdf": pdf,
            "published": published,
            "primary_category": cat,
        })
    print(f"[fetch] {cat}: kept {len(papers)} matched / scanned {len(feed.entries)}")
    return papers


def render_entry(p: dict) -> str:
    return (
        f"- **[{p['title']}]({p['link']})**  \n"
        f"  *{p['authors']}*  \n"
        f"  `{p['published']}` · `{p['primary_category']}` · [abs]({p['link']}) · [pdf]({p['pdf']})\n"
    )


def update_readme(new_papers: list[dict]) -> None:
    content = README.read_text(encoding="utf-8")
    if START_MARKER not in content or END_MARKER not in content:
        raise RuntimeError("README markers missing")

    pre, rest = content.split(START_MARKER, 1)
    _old, post = rest.split(END_MARKER, 1)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    new_block = [START_MARKER, ""]

    if new_papers:
        new_block.append(f"### {today} (UTC) — {len(new_papers)} new paper(s)\n")
        for p in new_papers:
            new_block.append(render_entry(p))
        new_block.append("")

    # Preserve previous auto-generated history
    # The previous block sits between markers; keep everything except the leading marker line.
    prev_block = _old.strip()
    if prev_block and not prev_block.startswith("_No papers fetched yet"):
        new_block.append(prev_block)
        new_block.append("")

    new_block.append(END_MARKER)
    README.write_text(pre + "\n".join(new_block) + post, encoding="utf-8")


def main() -> int:
    seen: dict[str, str] = load_json(SEEN_FILE, {})
    collected: dict[str, dict] = {}

    for cat in CATEGORIES:
        try:
            for p in fetch_category(cat):
                if p["id"] in seen or p["id"] in collected:
                    continue
                collected[p["id"]] = p
        except Exception as e:
            print(f"[warn] failed on {cat}: {e}", file=sys.stderr)
        time.sleep(SLEEP_BETWEEN)

    new_papers = sorted(
        collected.values(),
        key=lambda x: x["published"],
        reverse=True,
    )
    print(f"[result] {len(new_papers)} new paper(s) after dedup")

    if new_papers:
        update_readme(new_papers)
        for p in new_papers:
            seen[p["id"]] = p["published"]
        save_json(SEEN_FILE, seen)

    save_json(META_FILE, {
        "last_updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_seen": len(seen),
        "added_this_run": len(new_papers),
    })
    return 0


if __name__ == "__main__":
    sys.exit(main())
