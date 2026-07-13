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
| 1 | **Survey & Benchmark** | 80 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 277 | **+1** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 42 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 68 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 37 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 37 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 56 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 17 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 7 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 20 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 26 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-13 (UTC) — 3 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (1) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control](https://arxiv.org/abs/2607.08948)**  
  *Siddarth Jain, Ho Jin Choi*  
  `2026-07-09` · `cs.RO` · [abs](https://arxiv.org/abs/2607.08948) · [pdf](https://arxiv.org/pdf/2607.08948.pdf)
  > 💡 提出基于3D高斯泼溅的混合滤波与连续距离场方法，实现动态环境下的实时场景重建与无碰撞机器人反应控制。

  <details><summary>Abstract</summary>

  Robotic manipulators excel in structured environments but face substantial challenges in unstructured and dynamic settings. This paper presents SplatCtrl, a unified framework for real-time scene reconstruction and reactive robot motion generation to enable collision-free robotic arm control in previously unseen and continuously changing environments. Building on 3D Gaussian Splatting (3D-GS), we introduce a hybrid voxel-based filtering and dynamic Gaussian relocation strategy that supports efficient scene reconstruction from RGB-D streams while accommodating environmental changes. For safe and reactive control, we further propose a method for deriving continuous signed distance functions from isotropic Gaussians, providing stable and differentiable collision probability estimates that bridge classical distance fields with the modern implicit representation. These continuous distance metrics are incorporated into control barrier functions, resulting in a unified perception-action coupling framework that supports smooth and reliable real-time motion generation in response to scene changes. Experimental validation in simulation, on physical robot, and within shared human-robot workspace demonstrates the framework's effectiveness, achieving integrated scene reconstruction and reactive control in uncertain, and dynamic environments.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[StereoSplat+: Feed-Forward Stereo Gaussian Splatting with Diffusion-Assisted Progressive Inference](https://arxiv.org/abs/2607.08808)**  
  *Zihua Liu, Masatoshi Okutomi*  
  `2026-07-09` · `cs.CV` · [abs](https://arxiv.org/abs/2607.08808) · [pdf](https://arxiv.org/pdf/2607.08808.pdf)
  > 💡 单个立体对重建3DGS困难，提出StereoSplat前馈估计器融合成本体积与三平面，结合扩散增强渐进推理提升遮挡区渲染质量与几何精度。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled high-quality, render-ready scene representations for novel-view synthesis. However, most existing 3DGS pipelines rely on multi-view observations (or non-causal access to future frames) to achieve sufficient coverage, which is often unavailable in on-device robotics and AR settings where sensing is restricted to a single stereo rig. Recovering a high-quality 3DGS scene from one stereo observation, therefore, remains challenging due to occlusions, limited field of view, and missing geometry. We present StereoSplat+, a diffusion-enhanced feed-forward framework that enables causal reconstruction from a single stereo pair. Our method builds on two key components. First, we propose StereoSplat, an input-invariant feed-forward 3D Gaussian estimator that takes a variable number of posed stereo pairs as input and predicts high-quality 3D Gaussians. StereoSplat fuses complementary geometry cues via a cost-volume branch and a triplane-based 3D volume branch and leverages continuous pose encoding to generalize across view counts and camera configurations. Second, since multiple posed stereo pairs are typically unavailable at inference time, we introduce a diffusion-enhanced one-shot progressive inference scheme called StereoSplat+: starting from one stereo pair, we render novel stereo views from the predicted 3DGS, refine them with a one-step diffusion enhancer, and feed them back as additional inputs to update the 3DGS. Experiments on the KITTI-360 dataset show that StereoSplat+ improves novel-view rendering quality and geometry accuracy, especially in occluded regions and under strong view extrapolation, outperforming recent feed-forward 3DGS baselines.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[AnythingReality: Robust Online Gaussian Splatting SLAM for Open-Vocabulary VR Scene Exploration](https://arxiv.org/abs/2607.09260)**  
  *Timofei Kozlov, Dmitrii Maliukov, Andrey Marchenko, Miguel Altamirano Cabrera, Dzmitry Tsetserukou*  
  `2026-07-10` · `cs.CV` · [abs](https://arxiv.org/abs/2607.09260) · [pdf](https://arxiv.org/pdf/2607.09260.pdf)

  <details><summary>Abstract</summary>

  We present a novel integrated architecture for robust online 3D Gaussian splatting, real-time VR exploration, and speech-driven Vision-Language-Model interaction. Unlike methods assuming clean depth or external poses, our system combines ORB-SLAM3-based pose estimation with online Gaussian reconstruction for noisy real-world data. A VR pipeline enables immersive exploration of incremental reconstructions; a semantic module transcribes voice commands, generates scene descriptions, and records points of interest. Against state-of-the-art online Gaussian splatting methods, we improve image quality on our dataset (+14.5% PSNR, +8.6% SSIM, -14.3% LPIPS) and TUM-RGBD (+11.7% PSNR, +7.8% SSIM, -21.6% LPIPS), with comparable or superior frame rates via quality-speed configurations. We achieve an 88% VLM object-recognition rate.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
