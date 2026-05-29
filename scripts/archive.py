"""Monthly archive helper.

Moves day blocks older than RETAIN_DAYS out of README.md's AUTO-GENERATED
section and appends them to `papers/YYYY-MM.md`. Also (re)generates
`papers/README.md` as a chronological index of all archive files.

A day block is recognised by the heading pattern:

    ### YYYY-MM-DD (UTC) — N new paper(s)

The block spans from one such heading until the next, or until END_MARKER.
"""
from __future__ import annotations

import re
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
ARCHIVE_DIR = ROOT / "papers"

START_MARKER = "<!-- AUTO-GENERATED-START -->"
END_MARKER = "<!-- AUTO-GENERATED-END -->"

DAY_HEADING_RE = re.compile(
    r"^### (\d{4}-\d{2}-\d{2}) \(UTC\) — (\d+) new paper\(s\)\s*$", re.M
)

RETAIN_DAYS = 30  # keep this many most-recent day blocks inline in README


def _split_blocks(body: str) -> list[tuple[date, str]]:
    """Split the AUTO-GENERATED body into (date, full_block_text) pairs.

    `full_block_text` includes its `### ...` heading and everything until the
    next day heading (exclusive) or end of body.
    """
    headings = list(DAY_HEADING_RE.finditer(body))
    blocks: list[tuple[date, str]] = []
    for i, m in enumerate(headings):
        start = m.start()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(body)
        d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        text = body[start:end].rstrip() + "\n"
        blocks.append((d, text))
    return blocks


def _append_to_month(d: date, block: str) -> Path:
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    fname = ARCHIVE_DIR / f"{d.strftime('%Y-%m')}.md"
    if not fname.exists():
        fname.write_text(
            f"# Awesome Gaussian Splatting — Archive {d.strftime('%Y-%m')}\n\n"
            f"Auto-archived day blocks for **{d.strftime('%Y-%m')}**. "
            f"Newest first.\n\n",
            encoding="utf-8",
        )

    existing = fname.read_text(encoding="utf-8")
    # Idempotency: if the exact day heading already present, skip.
    head_line = f"### {d.isoformat()} (UTC)"
    if head_line in existing:
        return fname

    # Insert newest-first: place the new block right after the file header.
    # Header is the first two lines (title + blank) plus the intro paragraph.
    # We simply find the first "### " or end-of-file and insert before it.
    insert_at = existing.find("### ")
    if insert_at == -1:
        new_content = existing.rstrip() + "\n\n" + block.rstrip() + "\n"
    else:
        new_content = existing[:insert_at] + block.rstrip() + "\n\n" + existing[insert_at:]
    fname.write_text(new_content, encoding="utf-8")
    return fname


def _regenerate_index() -> None:
    if not ARCHIVE_DIR.exists():
        return
    files = sorted(
        [p for p in ARCHIVE_DIR.glob("*.md") if p.name != "README.md"],
        reverse=True,
    )
    lines = [
        "# Monthly Archives\n",
        "Each file collects the day blocks for that month, auto-rotated out of "
        "the main README to keep it lean.\n",
    ]
    if not files:
        lines.append("_No archives yet._\n")
    else:
        for f in files:
            lines.append(f"- [{f.stem}]({f.name})")
    (ARCHIVE_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def archive_old_blocks(today: date | None = None) -> int:
    """Run archival. Returns number of day blocks moved.

    A block is moved if today - block_date >= RETAIN_DAYS.
    """
    today = today or datetime.now(timezone.utc).date()
    content = README.read_text(encoding="utf-8")
    if START_MARKER not in content or END_MARKER not in content:
        return 0

    pre, rest = content.split(START_MARKER, 1)
    body, post = rest.split(END_MARKER, 1)

    blocks = _split_blocks(body)
    if not blocks:
        return 0

    keep_parts: list[str] = []
    moved = 0
    # Preserve any prose between START_MARKER and the first day heading
    first_heading_idx = body.find("### ")
    leading_prose = body[:first_heading_idx] if first_heading_idx != -1 else body
    keep_parts.append(leading_prose)

    for d, block in blocks:
        age = (today - d).days
        if age >= RETAIN_DAYS:
            _append_to_month(d, block)
            moved += 1
        else:
            keep_parts.append(block)

    new_body = "".join(keep_parts).rstrip() + "\n"
    new_content = pre + START_MARKER + "\n" + new_body + END_MARKER + post
    README.write_text(new_content, encoding="utf-8")

    if moved:
        _regenerate_index()
    return moved


if __name__ == "__main__":
    n = archive_old_blocks()
    print(f"[archive] moved {n} day block(s) to papers/")
