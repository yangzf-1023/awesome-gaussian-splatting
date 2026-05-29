# Awesome Gaussian Splatting

[![Daily arXiv Update](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml/badge.svg)](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml)
![Last Updated](https://img.shields.io/badge/dynamic/json?label=Last%20Updated&query=%24.last_updated&url=https%3A%2F%2Fraw.githubusercontent.com%2Fyangzf-1023%2Fawesome-gaussian-splatting%2Fmain%2Fdata%2Fmeta.json)

A curated, **auto-updated** list of papers related to **Gaussian Splatting (3DGS / 4DGS / Dynamic GS / Streaming GS / GS Compression / ...)** on [arXiv](https://arxiv.org/).

> The crawler runs **every day at 01:30 UTC** via GitHub Actions. It queries arXiv full-text search with quoted phrases, applies a strong/negative keyword guard, classifies each new paper into a sub-topic bucket, updates this README, and (optionally) pushes a digest to a Feishu group.

---

## How it works

- **Source**: arXiv API (`http://export.arxiv.org/api/query`) using `all:` full-text search (title + abstract + comments).
- **Phrase queries** (each quoted to avoid partial matches):
  `"gaussian splatting"`, `"gaussian splat"`, `"3d gaussian"`, `"4d gaussian"`, `"3dgs"`, `"4dgs"`.
- **Strong positive guard**: title or abstract must contain one of `gaussian splatting / gaussian splat / 3DGS / 4DGS / 3D gaussian(s) / 4D gaussian(s)`.
- **Negative guard**: drop if only ambiguous match (`3D gaussian`) co-occurs with `gaussian process / mixture / noise / beam / kernel / distribution / random`.
- **Dedup**: by arXiv ID in `data/seen.json`.
- **Topic classifier**: rule-based, first match wins (see `scripts/classify.py`).
- **Notifier**: posts an interactive card to a Feishu group webhook when `FEISHU_WEBHOOK` secret is set.
- **Schedule**: daily at `01:30 UTC` (≈ 09:30 Beijing). Also runnable from the **Actions** tab.

## Sub-topics

Papers are bucketed into the following sub-topics (in priority order). A paper falls into the **first** bucket whose keywords it matches; unmatched papers go to **Others**.

| # | Sub-topic | Example keywords |
|---|---|---|
| 1 | Survey & Benchmark | survey, review, benchmark |
| 2 | Dynamic / 4D / Streaming | 4D, dynamic, temporal, deformable, streaming |
| 3 | Avatar / Human / Face | avatar, human, body, face, head |
| 4 | Generation / Diffusion | text-to-3D, generation, diffusion, SDS |
| 5 | Editing / Stylization / Watermark | editing, stylization, inpainting, watermark |
| 6 | Compression / Compact / Efficient Storage | compression, quantization, pruning, codec |
| 7 | Rendering / Acceleration / Mobile | real-time, mobile, LOD, rasterization |
| 8 | SLAM / Localization / Mapping | SLAM, localization, mapping, odometry |
| 9 | Autonomous Driving / Outdoor | driving, street, urban, LiDAR, city-scale |
| 10 | Medical / Surgical | medical, surgery, endoscopy, CT/MRI |
| 11 | Relighting / Material / BRDF | relighting, BRDF, material, inverse rendering |
| 12 | Sparse-View / Few-shot / Generalizable | sparse-view, few-shot, single-image, feed-forward |
| 13 | Semantic / Scene Understanding | semantic, segmentation, scene graph, grounding |
| 14 | Reconstruction / Geometry | reconstruction, mesh, depth, photogrammetry |
| 15 | Others | (fallback) |

## Feishu (Lark) notifications

To receive a daily digest card in a Feishu group:

1. In the target group: **Settings → Group Bots → Add Bot → Custom Bot**, copy the **Webhook URL**. Optionally enable a signing secret.
2. In this repo: **Settings → Secrets and variables → Actions → New repository secret**.
   - `FEISHU_WEBHOOK` = your webhook URL (required)
   - `FEISHU_SECRET` = your signing secret (optional)

The notifier is a no-op when `FEISHU_WEBHOOK` is unset, so forks without secrets still work.

## Repository structure

```
.
├── .github/workflows/daily-update.yml   # GitHub Actions schedule
├── scripts/
│   ├── fetch_arxiv.py                   # arXiv crawler & README updater
│   ├── classify.py                      # rule-based topic classifier
│   └── feishu_notify.py                 # Feishu webhook notifier
├── data/
│   ├── seen.json                        # dedup cache (arXiv id -> date)
│   └── meta.json                        # last-updated timestamp
└── README.md                            # auto-edited between markers
```

## Manual run (locally)

```bash
pip install -r requirements.txt
export FEISHU_WEBHOOK="https://open.feishu.cn/open-apis/bot/v2/hook/xxxx"  # optional
python scripts/fetch_arxiv.py
```

## Contributing

Found a missing paper or wrong classification? Open an issue or PR — manual entries above the auto-generated marker are preserved.

## License

[MIT](LICENSE)

---

<!-- AUTO-GENERATED-START -->
_No papers fetched yet under the new classifier. The next scheduled run will repopulate this section, grouped by sub-topic._
<!-- AUTO-GENERATED-END -->
