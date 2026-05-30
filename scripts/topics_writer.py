"""Per-topic Markdown file maintenance.

Each topic has its own file at `topics/<slug>.md` accumulating ALL papers ever
ingested in that bucket, grouped by date (newest first). New papers are
inserted at the top of the file under a `## YYYY-MM-DD` heading.

The main README only keeps the topic index table + the latest day, so this
module is what makes per-topic browsing scale.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
TOPICS_DIR = ROOT / "topics"

DATE_HEADING_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})\s*$", re.M)


def _topic_file(slug: str) -> Path:
    return TOPICS_DIR / f"{slug}.md"


def _ensure_header(path: Path, topic_name: str) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        f"# {topic_name}\n\n"
        f"All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.\n\n"
        f"[← Back to main index](../README.md)\n\n"
        f"---\n"
    )
    path.write_text(header, encoding="utf-8")


def append_papers(date_str: str, grouped: dict, render_entry) -> None:
    """Append today's papers to each per-topic file.

    Args:
      date_str: "YYYY-MM-DD"
      grouped: {topic_display_name: [paper_dict, ...]}
      render_entry: callable(paper_dict) -> markdown string (with trailing \n)
    """
    # Local import to avoid circular dep at module import time
    from classify import topic_order
    slug_by_name = {name: slug for name, slug in topic_order()}

    for topic_name, papers in grouped.items():
        if not papers:
            continue
        slug = slug_by_name.get(topic_name, _slugify(topic_name))
        path = _topic_file(slug)
        _ensure_header(path, topic_name)

        existing = path.read_text(encoding="utf-8")
        day_heading = f"## {date_str}"

        new_entries = [render_entry(p).rstrip() + "\n" for p in papers]
        new_block = "\n".join(new_entries)

        if day_heading in existing:
            # Idempotent: insert under the existing heading (right after it).
            pattern = re.compile(rf"^{re.escape(day_heading)}\s*$", re.M)
            m = pattern.search(existing)
            insert_at = m.end()
            updated = existing[:insert_at] + "\n\n" + new_block + existing[insert_at:]
        else:
            # Find first existing "## " date heading to insert before it,
            # otherwise append at end-of-file.
            m = DATE_HEADING_RE.search(existing)
            block = f"\n{day_heading}\n\n{new_block}\n"
            if m:
                insert_at = m.start()
                updated = existing[:insert_at] + block + existing[insert_at:]
            else:
                updated = existing.rstrip() + "\n" + block
        path.write_text(updated, encoding="utf-8")


def regenerate_index() -> None:
    """Rewrite topics/README.md with a chronological topic table."""
    if not TOPICS_DIR.exists():
        return
    from classify import topic_order
    rows = []
    canonical = list(topic_order())
    slugs = [(n, s) for n, s in canonical]
    # Append any extra files not in canonical (defensive)
    known_slugs = {s for _, s in canonical}
    for path in sorted(TOPICS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        slug = path.stem
        if slug not in known_slugs:
            slugs.append((slug.replace("-", " ").title(), slug))

    for idx, (name, slug) in enumerate(slugs, 1):
        path = _topic_file(slug)
        if not path.exists():
            continue
        # Count entries by counting bullet headers '- **['
        text = path.read_text(encoding="utf-8")
        count = len(re.findall(r"^- \*\*\[", text, re.M))
        rows.append(f"| {idx} | {name} | {count} | [{slug}.md]({slug}.md) |")

    lines = [
        "# Topics Index",
        "",
        "Every Gaussian-Splatting paper this repo has ever ingested, grouped by sub-topic. "
        "Each file is auto-appended as new papers come in.",
        "",
        "[← Back to main README](../README.md)",
        "",
        "| # | Topic | Papers | File |",
        "|---|---|---|---|",
        *rows,
        "",
    ]
    (TOPICS_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def topic_counts() -> dict:
    """Return {topic_display_name: total_paper_count} for the README index table."""
    from classify import topic_order
    out = {}
    for name, slug in topic_order():
        path = _topic_file(slug)
        if not path.exists():
            out[name] = 0
            continue
        text = path.read_text(encoding="utf-8")
        out[name] = len(re.findall(r"^- \*\*\[", text, re.M))
    return out


def _slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "topic"
