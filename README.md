# Awesome Gaussian Splatting

[![Daily arXiv Update](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml/badge.svg)](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml)
![Last Updated](https://img.shields.io/badge/dynamic/json?label=Last%20Updated&query=%24.last_updated&url=https%3A%2F%2Fraw.githubusercontent.com%2Fyangzf-1023%2Fawesome-gaussian-splatting%2Fmain%2Fdata%2Fmeta.json)

A curated, **auto-updated** list of papers related to **Gaussian Splatting (3DGS / 4DGS / Dynamic GS / Streaming GS / GS Compression / ...)** on [arXiv](https://arxiv.org/).

> The crawler runs **every day at 01:30 UTC** via GitHub Actions. It (1) queries arXiv full-text search with quoted phrases, (2) applies a strong/negative keyword guard, (3) classifies each new paper into a sub-topic bucket, (4) optionally calls an LLM for a one-line Chinese TL;DR, (5) updates this README, (6) archives day blocks older than 30 days into [`papers/YYYY-MM.md`](papers/), and (7) optionally pushes a digest card to a Feishu group.

---

## How it works

- **Source**: arXiv API (`http://export.arxiv.org/api/query`) with `all:` full-text search.
- **Phrase queries**: `"gaussian splatting"`, `"gaussian splat"`, `"3d gaussian"`, `"4d gaussian"`, `"3dgs"`, `"4dgs"`.
- **Strong positive guard**: title/abstract must contain `gaussian splatting / splat / 3DGS / 4DGS / 3D gaussian(s) / 4D gaussian(s)`.
- **Negative guard**: drop if only ambiguous `3D gaussian` co-occurs with `gaussian process/mixture/noise/beam/kernel/distribution/random`.
- **Dedup**: by arXiv ID in `data/seen.json`.
- **Topic classifier**: rule-based, first match wins (`scripts/classify.py`).
- **LLM TL;DR**: optional Chinese one-liner via any OpenAI-compatible Chat Completions endpoint, cached in `data/tldr.json`.
- **Monthly archive**: day blocks older than 30 days are moved into `papers/YYYY-MM.md`.
- **Feishu notify**: posts an interactive card with TL;DR previews to your group.

## Sub-topics

Papers fall into the **first** matching bucket; unmatched go to **Others**.

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

## LLM TL;DR configuration (optional)

The script is **backend-agnostic**: it calls any OpenAI-compatible `/chat/completions` endpoint based on three environment variables. Set them as repo secrets:

| Secret | Example value |
|---|---|
| `OPENAI_BASE_URL` | `https://api.deepseek.com/v1` · `https://api.openai.com/v1` · `https://api.moonshot.cn/v1` · etc. |
| `OPENAI_API_KEY`  | your key |
| `OPENAI_MODEL`    | `deepseek-chat` · `gpt-4o-mini` · `moonshot-v1-8k` · etc. |

If any of these is unset, TL;DR is silently skipped — the pipeline still works.

Results are cached in `data/tldr.json` keyed by arXiv ID, so re-runs do not re-spend tokens.

## Feishu notifications (optional)

1. Target Feishu group → **Settings → Group Bots → Add Bot → Custom Bot**, copy the Webhook URL. Optionally enable a signing secret.
2. Repo → **Settings → Secrets and variables → Actions**:
   - `FEISHU_WEBHOOK` (required to enable)
   - `FEISHU_SECRET`  (only if you enabled signing)

## Monthly archive

Day blocks older than 30 days are moved out of this README into `papers/YYYY-MM.md`. Index lives at [`papers/README.md`](papers/README.md). This keeps the main README small and renderable on GitHub.

## Repository structure

```
.
├── .github/workflows/daily-update.yml   # GitHub Actions schedule
├── scripts/
│   ├── fetch_arxiv.py                   # main orchestrator
│   ├── classify.py                      # rule-based topic classifier
│   ├── tldr.py                          # OpenAI-compatible Chinese TL;DR
│   ├── archive.py                       # monthly archival
│   └── feishu_notify.py                 # Feishu webhook notifier
├── data/
│   ├── seen.json                        # dedup cache (arXiv id -> date)
│   ├── tldr.json                        # LLM TL;DR cache
│   └── meta.json                        # last-updated timestamp
├── papers/
│   ├── README.md                        # index of monthly archives
│   └── YYYY-MM.md                       # archived day blocks
└── README.md                            # this file (auto-edited between markers)
```

## Manual run (locally)

```bash
pip install -r requirements.txt

# Optional enrichment
export OPENAI_BASE_URL="https://api.deepseek.com/v1"
export OPENAI_API_KEY="sk-..."
export OPENAI_MODEL="deepseek-chat"
export FEISHU_WEBHOOK="https://open.feishu.cn/open-apis/bot/v2/hook/xxxx"

python scripts/fetch_arxiv.py
```

## Contributing

Found a missing paper, wrong classification, or bad TL;DR? Open an issue or PR — manual content above the auto-generated marker is preserved.

## License

[MIT](LICENSE)

---

<!-- AUTO-GENERATED-START -->
















## Browse by topic

Each topic file accumulates every paper this repo has ever ingested in that bucket, newest first.

<!-- TOPIC-INDEX-START -->

| # | Topic | Total Papers | Latest-day Δ | Browse |
|---|---|---|---|---|
| 1 | **Survey & Benchmark** | 59 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 236 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 30 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 46 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 23 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 32 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 35 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 10 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 13 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 3 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 13 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 22 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-12 (UTC) — 2 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction](https://arxiv.org/abs/2606.13655)**  
  *Jen-Hao Cheng, Yipeng Wang, Hao Zhang, Gengshan Yang, Jenq-Neng Hwang*  
  `2026-06-11` · `cs.CV` · [abs](https://arxiv.org/abs/2606.13655) · [pdf](https://arxiv.org/pdf/2606.13655.pdf)
  > 💡 提出Flex4DHuman，用相对相机姿态编码的多视角视频扩散模型，无需几何先验，从单目视频生成动态4D高斯

  <details><summary>Abstract</summary>

  We present Flex4DHuman, a multi-view video diffusion model that transforms a monocular or sparse multi-view video of a dynamic subject into synchronized dense multi-view videos using only relative camera-pose conditioning. Unlike prior human-centric methods that rely on skeletons, depth maps, normals, or rendered target-view geometry, Flex4DHuman requires no explicit geometry priors and instead conditions generation through relative camera-pose positional encoding. The generated videos can be directly ingested by downstream reconstruction pipelines to create dynamic 4D Gaussian splats. Built on the Wan 2.1 1.3B text-to-video model, Flex4DHuman preserves the backbone architecture and encodes camera and view information through a five-axis positional encoding that extends spatio-temporal RoPE with view indices and continuous SE(3) relative camera geometry. A three-stage curriculum progressively trains the model for pose following, flexible reference-to-target view generation, and temporal rollout. To support temporal rollout, we train with clean historical target-view tokens. We also add multi-view captions to enable test-time text control. Combined with an off-the-shelf 4D Gaussian Splatting stage, our framework lifts monocular static-camera videos into dynamic 4D Gaussian splats. Experiments on DNA-Rendering and ActorsHQ show that Flex4DHuman surpasses prior state-of-the-art methods, while the same formulation generalizes to animal categories after mixed human-animal training. These capabilities make Flex4DHuman a practical step toward scalable 4D content creation from casual monocular videos for simulation, gaming, AR/VR, and video re-shooting.

  </details>


- **[MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376)**  
  *Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu, Jun Liang, Shengfeng He, Jing Li*  
  `2026-06-11` · `cs.CV` · [abs](https://arxiv.org/abs/2606.13376) · [pdf](https://arxiv.org/pdf/2606.13376.pdf)
  > 💡 用单张窄视场图像，通过全景扩散和3D高斯支架构建，再经条件视频生成器实时渲染，支持8FPS交互漫游。

  <details><summary>Abstract</summary>

  We present MoVerse, a real-time video world model that creates an interactively navigable scene from a single narrow-field-of-view image. This setting is challenging because the input observes only a small fraction of the environment, while interactive roaming requires a complete surrounding world, persistent geometry, controllable camera motion, and temporally coherent high-fidelity observations. MoVerse addresses this problem by separating world construction from observation rendering. It first expands the input into a gravity-aligned 360$^\circ$ panorama with topology-aware diffusion, closing the missing field of view before 3D reasoning. It then lifts the panorama into a persistent 3D Gaussian scaffold using panoramic geometry-aware residual prediction, yielding a dense and directly renderable spatial memory. Finally, a Gaussian-conditioned video renderer translates scaffold renderings along user-specified camera trajectories into photorealistic video. To make this renderer practical for interaction, we train a bidirectional diffusion teacher for high-quality conditional rendering and distill it into a causal autoregressive student for bounded-latency streaming. This design combines the controllability and long-range consistency of explicit 3D representations with the perceptual quality of generative video models. MoVerse supports real-time scene roaming at 8~FPS on a single NVIDIA RTX~4090 GPU, demonstrating a practical path toward single-image world creation with interactive video output.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
