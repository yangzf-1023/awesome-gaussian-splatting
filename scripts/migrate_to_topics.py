#!/usr/bin/env python3
"""One-shot migration: split README's AUTO-GENERATED block into per-topic files.

Reads:  README.md
Writes: topics/<slug>.md  (one file per topic, papers grouped by day inside)
        topics/README.md  (index)
        README.md         (rewritten with topic index + latest day only)

Idempotent: re-running on an already-migrated README is a no-op for the topic
files (they keep their content) but the README index is regenerated from the
current topics/ contents.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
TOPICS_DIR = ROOT / "topics"

START_MARKER = "<!-- AUTO-GENERATED-START -->"
END_MARKER = "<!-- AUTO-GENERATED-END -->"
INDEX_START = "<!-- TOPIC-INDEX-START -->"
INDEX_END = "<!-- TOPIC-INDEX-END -->"
LATEST_START = "<!-- LATEST-START -->"
LATEST_END = "<!-- LATEST-END -->"

DAY_RE = re.compile(r"^### (\d{4}-\d{2}-\d{2}) \(UTC\) — (\d+) new paper\(s\)\s*$")
TOPIC_RE = re.compile(r"^#### (.+?) \((\d+)\)\s*$")
ENTRY_HEAD_RE = re.compile(r"^- \*\*\[.+?\]\(.+?\)\*\*\s*$")

# Mirror of scripts/classify.py
TOPIC_META = [
    ("Survey & Benchmark", "survey"),
    ("Dynamic / 4D / Streaming", "dynamic-4d"),
    ("Avatar / Human / Face", "avatar-human"),
    ("Generation / Diffusion", "generation"),
    ("Editing / Stylization / Watermark", "editing"),
    ("Compression / Compact / Efficient Storage", "compression"),
    ("Rendering / Acceleration / Mobile", "rendering"),
    ("SLAM / Localization / Mapping", "slam"),
    ("Autonomous Driving / Outdoor", "driving"),
    ("Medical / Surgical", "medical"),
    ("Relighting / Material / BRDF", "relighting"),
    ("Sparse-View / Few-shot / Generalizable", "sparse-view"),
    ("Semantic / Scene Understanding", "semantic"),
    ("Reconstruction / Geometry", "reconstruction"),
    ("Others", "others"),
]
NAME_TO_SLUG = {n: s for n, s in TOPIC_META}


def split_entries(lines):
    entries, cur = [], []
    for line in lines:
        if ENTRY_HEAD_RE.match(line):
            if cur:
                entries.append(_strip(cur))
                cur = []
            cur.append(line)
        else:
            if cur:
                cur.append(line)
    if cur:
        entries.append(_strip(cur))
    return ["\n".join(e) for e in entries]


def _strip(lines):
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def parse_readme(text):
    if START_MARKER not in text or END_MARKER not in text:
        raise SystemExit("AUTO-GENERATED markers missing in README")
    pre, rest = text.split(START_MARKER, 1)
    body, post = rest.split(END_MARKER, 1)
    lines = body.splitlines()
    day_starts = [(i, m.group(1)) for i, line in enumerate(lines)
                  for m in [DAY_RE.match(line)] if m]
    if not day_starts:
        return pre, None, 0, OrderedDict(), OrderedDict(), post

    latest_idx, latest_date = day_starts[0]
    m = DAY_RE.match(lines[latest_idx])
    latest_total = int(m.group(2)) if m else 0

    all_topics = OrderedDict()
    latest_per_topic = OrderedDict()
    for idx, (start, date_str) in enumerate(day_starts):
        end = day_starts[idx + 1][0] if idx + 1 < len(day_starts) else len(lines)
        day_lines = lines[start + 1:end]
        topic_starts = [(j, m2.group(1)) for j, line in enumerate(day_lines)
                        for m2 in [TOPIC_RE.match(line)] if m2]
        for k, (tstart, tname) in enumerate(topic_starts):
            tend = topic_starts[k + 1][0] if k + 1 < len(topic_starts) else len(day_lines)
            entries = split_entries(day_lines[tstart + 1:tend])
            all_topics.setdefault(tname, []).extend((date_str, e) for e in entries)
            if start == latest_idx:
                latest_per_topic.setdefault(tname, []).extend(entries)
    return pre, latest_date, latest_total, latest_per_topic, all_topics, post


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "topic"


def write_topic_files(all_topics):
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)
    written = OrderedDict()
    ordered = [n for n, _ in TOPIC_META if n in all_topics] + \
              [n for n in all_topics if n not in NAME_TO_SLUG]
    for name in ordered:
        slug = NAME_TO_SLUG.get(name, slugify(name))
        by_date = {}
        for d, e in all_topics[name]:
            by_date.setdefault(d, []).append(e)
        out = [f"# {name}\n",
               "All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.\n",
               "[← Back to main index](../README.md)\n",
               "---\n"]
        for d in sorted(by_date.keys(), reverse=True):
            out.append(f"## {d}\n")
            for e in by_date[d]:
                out.append(e)
                out.append("")
        (TOPICS_DIR / f"{slug}.md").write_text(
            "\n".join(out).rstrip() + "\n", encoding="utf-8")
        written[name] = len(all_topics[name])
    return written


def write_topics_index(written):
    lines = ["# Topics Index", "",
             "Every Gaussian-Splatting paper this repo has ever ingested, grouped by sub-topic. "
             "Each file is auto-appended as new papers come in.", "",
             "[← Back to main README](../README.md)", "",
             "| # | Topic | Papers | File |",
             "|---|---|---|---|"]
    for i, (name, count) in enumerate(written.items(), 1):
        slug = NAME_TO_SLUG.get(name, slugify(name))
        lines.append(f"| {i} | {name} | {count} | [{slug}.md]({slug}.md) |")
    (TOPICS_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_topic_index_block(written, latest_per_topic):
    lines = ["", "| # | Topic | Total Papers | Latest-day Δ | Browse |",
             "|---|---|---|---|---|"]
    for i, (name, count) in enumerate(written.items(), 1):
        slug = NAME_TO_SLUG.get(name, slugify(name))
        delta = len(latest_per_topic.get(name, []))
        delta_cell = f"**+{delta}**" if delta else "—"
        lines.append(f"| {i} | **{name}** | {count} | {delta_cell} | "
                     f"[topics/{slug}.md](topics/{slug}.md) |")
    lines.append("")
    return "\n".join(lines)


def render_latest_block(latest_date, latest_total, latest_per_topic):
    lines = [""]
    if latest_date:
        lines.append(f"### {latest_date} (UTC) — {latest_total} new paper(s)")
        lines.append("")
        if latest_per_topic:
            for name, entries in latest_per_topic.items():
                slug = NAME_TO_SLUG.get(name, slugify(name))
                lines.append(
                    f"<details><summary><b>{name}</b> ({len(entries)}) · "
                    f"<a href=\"topics/{slug}.md\">full list →</a></summary>")
                lines.append("")
                for e in entries:
                    lines.append(e)
                    lines.append("")
                lines.append("</details>")
                lines.append("")
        else:
            lines.append("_No new papers today._")
    else:
        lines.append("_No papers ingested yet._")
    lines.append("")
    return "\n".join(lines)


def build_new_readme(pre, latest_date, latest_total, latest_per_topic, written, post):
    idx = render_topic_index_block(written, latest_per_topic)
    latest = render_latest_block(latest_date, latest_total, latest_per_topic)
    body = (
        "\n\n"
        "## Browse by topic\n\n"
        "Each topic file accumulates every paper this repo has ever ingested in that bucket, newest first.\n\n"
        f"{INDEX_START}\n{idx.rstrip()}\n{INDEX_END}\n\n"
        "## Latest update\n\n"
        "Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into "
        "[`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).\n\n"
        f"{LATEST_START}\n{latest.rstrip()}\n{LATEST_END}\n\n"
    )
    return pre.rstrip() + "\n\n" + START_MARKER + body + END_MARKER + post


def main():
    text = README.read_text(encoding="utf-8")
    pre, latest_date, latest_total, latest_per_topic, all_topics, post = parse_readme(text)
    if not all_topics:
        print("[migrate] No day blocks found in README; nothing to split.")
        return 0
    print(f"[migrate] latest={latest_date} total={latest_total}, topics={len(all_topics)}")
    for name, items in all_topics.items():
        print(f"  - {name}: {len(items)} (latest +{len(latest_per_topic.get(name, []))})")
    written = write_topic_files(all_topics)
    write_topics_index(written)
    new_readme = build_new_readme(pre, latest_date, latest_total,
                                  latest_per_topic, written, post)
    README.write_text(new_readme, encoding="utf-8")
    print(f"[migrate] wrote {len(written)} topic files + new README "
          f"({len(new_readme)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
