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
| 1 | **Survey & Benchmark** | 57 | **+1** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 229 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 29 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 43 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 20 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 31 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 34 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 10 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 12 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 2 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 13 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 21 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-08 (UTC) — 3 new paper(s)

<details><summary><b>Survey & Benchmark</b> (1) · <a href="topics/survey.md">full list →</a></summary>

- **[RPC-GS: Gaussian Splatting with native RPC Rendering for Satellite Imagery](https://arxiv.org/abs/2606.06690)**  
  *Valentin Wagner, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens*  
  `2026-06-04` · `cs.CV` · [abs](https://arxiv.org/abs/2606.06690) · [pdf](https://arxiv.org/pdf/2606.06690.pdf)
  > 💡 针对卫星影像高斯泼溅中相机模型近似导致几何误差的问题，提出原生RPC渲染框架，通过直接投影与雅可比协方差变换，显著降低重建误差。

  <details><summary>Abstract</summary>

  We present RPC-GS, the first Gaussian Splatting framework for satellite imagery that operates natively with Rational Polynomial Camera (RPC) models. The RPC model is the de facto standard for representing the complex imaging geometry of modern pushbroom satellite sensors. To simplify rendering, prior satellite Gaussian Splatting methods replace the RPC model with perspective or affine camera approximations, leading to geometric errors during reconstruction. RPC-GS avoids these approximations by projecting Gaussian means and covariances directly through the RPC model during the splatting process. We embed the RPC model in a chain of carefully selected geo-coordinate transformations representing a mapping from splatting-suitable scene coordinates to image coordinates. To map the Gaussian covariance matrices, we derive a numerically robust Jacobian-based covariance projection for the (partially nonlinear) coordinate transformations. Since RPCs lack an explicit notion of camera depth, we integrate a metric ray-based depth formulation. We benchmark RPC, perspective, and affine camera models in a unified framework, with our native RPC renderer consistently achieving the lowest reconstruction error on leading satellite benchmark datasets, improving mean altitude error over perspective and affine approximations by 29.6% and 63.8% on DFC2019, and by 9.9% and 37.9% on IARPA2016. We release our code to support future research of Gaussian Splatting in the satellite imaging domain.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[EvoGS: Constructing Continuous-Layered Gaussian Splatting with Evolution Tree for Scalable 3D Streaming](https://arxiv.org/abs/2606.07179)**  
  *Yuang Shi, Simone Gasparini, Géraldine Morin, Wei Tsang Ooi*  
  `2026-06-05` · `cs.CV` · [abs](https://arxiv.org/abs/2606.07179) · [pdf](https://arxiv.org/pdf/2606.07179.pdf)
  > 💡 现有离散分层3DGS流式传输存在冗余和误差累积，提出连续分层进化树表示，消除冗余并大幅降低传输和显存占用。

  <details><summary>Abstract</summary>

  Streaming 3D Gaussian Splatting requires highly scalable, progressive representations. Existing progressive methods rely on \textit{discrete layering}, accumulating separate splat sets for each level of detail. This structural independence between layers inherently leads to error accumulation, severe splat redundancy, and uncontrolled quality transitions. We propose EvoGS, the first \textit{continuous-layering} representation. Organized as an Evolution Tree, EvoGS generates finer details via an explicit, wavelet-inspired parent-child refinement. This empowers child nodes to structurally correct ancestral errors, yield inherently sparse and highly compressible inter-layer signals. Extensive experiments show EvoGS eliminates splat redundancy from over 65\% to under 25\%. Compared to state-of-the-art baselines, it reduces transmission payload and GPU VRAM footprint by up to 2.4$\times$ and 5.5$\times$, respectively, and achieves smooth quality transitions optimal for real-time adaptive streaming. Project page: https://yuang-ian.github.io/evogs/

  </details>


- **[QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation](https://arxiv.org/abs/2606.07118)**  
  *Yuxiang Chen, Yuanhao Wang, Ziheng Zhang, Meng Zhang, Yu Liu, Yufei Jia, Tiancai Wang, Erjin Zhou, Jin Xie*  
  `2026-06-05` · `cs.RO` · [abs](https://arxiv.org/abs/2606.07118) · [pdf](https://arxiv.org/pdf/2606.07118.pdf)
  > 💡 利用重建场景校准视觉、接触和动力学，通过3DGS与残差补偿缩小仿真到现实差距，实现零样本地形导航。

  <details><summary>Abstract</summary>

  Simulation is central to robot learning, yet the sim-to-real gap remains a major bottleneck.Existing approaches often tackle visual or dynamic gaps separately, overlooking how these individual mismatches accumulate and propagate throughout the robot's state evolution.In this paper, we introduce QuadVerse, an integrated framework that uses reconstructed scenes as a calibration substrate for aligning visual perception, physical interaction, and actuator dynamics.From captured RGB videos, we reconstruct geometry-constrained 3D Gaussian Splatting (3DGS) scenes that support batched photorealistic ego-view rendering and collision-ready semantic mesh extraction. The meshes further enable contact calibration by initializing spatially varying friction priors and refining them through trajectory-based posterior search.To address remaining actuator discrepancies, QuadVerse trains a residual dynamics compensator by replaying real-world trajectories on the contact-calibrated terrain, reducing the entanglement between terrain-induced contact errors and actuator non-idealities.Experiments show that QuadVerse improves reconstruction quality and locomotion tracking over relevant baselines.Leveraging this foundation, we demonstrate robust zero-shot visual-navigation policy deployment without task-specific real-world rollouts.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
