# Awesome Gaussian Splatting

[![Daily arXiv Update](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml/badge.svg)](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml)
![Last Updated](https://img.shields.io/badge/dynamic/json?label=Last%20Updated&query=%24.last_updated&url=https%3A%2F%2Fraw.githubusercontent.com%2Fyangzf-1023%2Fawesome-gaussian-splatting%2Fmain%2Fdata%2Fmeta.json)

A curated, **auto-updated** list of papers related to **Gaussian Splatting (3DGS / 4DGS / Dynamic GS / Streaming GS / GS Compression / ...)** on [arXiv](https://arxiv.org/).

> The crawler runs **every day at 01:30 UTC** via GitHub Actions, fetches the latest submissions from arXiv, filters by Gaussian-Splatting-related keywords, and appends new entries to this README.

---

## How it works

- **Source**: arXiv API (`http://export.arxiv.org/api/query`)
- **Scope**: categories `cs.CV`, `cs.GR`, `cs.LG`, `cs.AI`, `eess.IV`
- **Filter keywords**: `gaussian splatting`, `3dgs`, `4dgs`, `3d gaussian`, `4d gaussian`, `gaussian splat`
- **Dedup**: by arXiv ID, persisted in `data/seen.json`
- **Schedule**: daily at `01:30 UTC` (≈ 09:30 Beijing)
- You can also trigger it manually from the **Actions** tab.

## Repository structure

```
.
├── .github/workflows/daily-update.yml   # GitHub Actions schedule
├── scripts/fetch_arxiv.py               # arXiv crawler & README updater
├── data/seen.json                       # dedup cache
├── data/meta.json                       # last-updated timestamp
└── README.md                            # this file (auto-edited below the marker)
```

## Manual run (locally)

```bash
pip install -r requirements.txt
python scripts/fetch_arxiv.py
```

## Contributing

Found a missing paper? Open an issue or PR — manual entries above the auto-generated marker are preserved.

## License

[MIT](LICENSE)

---

<!-- AUTO-GENERATED-START -->
_No papers fetched yet. The first batch will appear after the next scheduled run._
<!-- AUTO-GENERATED-END -->
