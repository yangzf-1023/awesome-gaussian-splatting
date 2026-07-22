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
| 1 | **Survey & Benchmark** | 84 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 288 | — | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 48 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 74 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 38 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 47 | **+2** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 62 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 18 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 8 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 24 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 28 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 10 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-22 (UTC) — 4 new paper(s)

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[FlexiAvatar: Unified 3D Gaussian Human Avatars Under Arbitrary Body Visibility](https://arxiv.org/abs/2607.19100)**  
  *Yihalem Yimolal Tiruneh, Muhammad Salman Ali, Uyoung Jeong, Muneeb A. Khan, MD Khalequzzaman Chowdhury Sayem, Allanur Bayramgeldiyev, Binod Bhattarai, Seungryul Baek*  
  `2026-07-21` · `cs.CV` · [abs](https://arxiv.org/abs/2607.19100) · [pdf](https://arxiv.org/pdf/2607.19100.pdf)
  > 💡 针对单目视频人体重建中可见区域质量下降问题，提出FlexiAvatar，显式优化可见区域并利用扩散补全不可见区域，提升重建质量。

  <details><summary>Abstract</summary>

  Reconstructing animatable 3D human avatars from monocular video is a fundamental problem in computer vision with broad applications in AR/VR and digital content creation. Existing approaches typically couple parametric body models with neural rendering or 3D Gaussian splatting and optimize all body regions jointly from short videos, which often degrades fidelity in the visible areas. To overcome this limitation, we introduce FlexiAvatar, a unified framework that explicitly optimizes only the visible body regions, effectively eliminating artifacts arising from unobserved limbs. Our method integrates occlusion-robust SMPL-X tracking with part-specific residual refinement to capture high-frequency geometric and appearance details. To complete entirely unseen regions (e.g., back views), we leverage a diffusion-based approach to generate texture consistent with the observed appearance. Experiments on full-body (NeuMan, ZJU-MoCap, WildAvatar), upper/half-body (talk-show clips), and head-only (INSTA) inputs show that FlexiAvatar delivers consistently higher reconstruction quality, outperforming state-of-the-art methods by an average PSNR improvement of approximately 3% across datasets. Finally, by restricting optimization to observed regions, our method reduces the effective number of Gaussians that must be optimized and rendered, leading to reduced runtime and memory overhead in partial-visibility scenarios.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539)**  
  *Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.18539) · [pdf](https://arxiv.org/pdf/2607.18539.pdf)
  > 💡 利用时间条件变形场和视频扩散先验实现大尺度场景的细微动态动画，同时保持刚性结构，提升沉浸感。

  <details><summary>Abstract</summary>

  Novel view rendering of large and complex reconstructed scenes is becoming increasingly photorealistic. However, most reconstructions remain static and lack the ambient motion that makes environments immersive. We present AniGS, a method for scene-level animation of 3D Gaussian Splatting (3DGS) reconstructions that adds subtle, distributed dynamics, e.g., vegetation motion, while preserving rigid structures. Unlike existing 3D animation techniques which are limited to object-centric subjects or small regions, AniGS is designed for large, cluttered, navigable scenes. AniGS represents the scene with a canonical 3DGS and models motion using a time-conditioned deformation field. To animate the entire scene, we leverage a pretrained video diffusion model and introduce an iterative dataset--model update strategy that progressively expands viewpoint coverage and repeatedly updates camera-fixed training videos using a render-and-refine scheme. To prevent artifacts from unintended motion in static areas, we further introduce a composed video-to-video refinement scheme that restricts motion to desired regions. Experiments on five real-world, large-scale outdoor scenes demonstrate that AniGS produces natural ambient dynamics and high-quality novel view videos, enabling more immersive viewing experiences of reconstructed environments.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (2) · <a href="topics/compression.md">full list →</a></summary>

- **[ZeroSplat: Generalized Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2607.18801)**  
  *Jiayu Ding, Meilu Song, Xiaoyi Zhang, Hongbo Jin, Yichen Jin, Xiangtian Si*  
  `2026-07-21` · `cs.CV` · [abs](https://arxiv.org/abs/2607.18801) · [pdf](https://arxiv.org/pdf/2607.18801.pdf)
  > 💡 现有3DGS分割仅支持单目标且需大量计算，ZeroSplat利用多视图几何约束将2D VLM先验提升至3D，实现训练-free的任意目标分割。

  <details><summary>Abstract</summary>

  Recent advancements in 3D Gaussian Splatting (3DGS) have enabled language-guided scene understanding. However, existing Referring 3D Gaussian Splatting (R3DGS) methods are fundamentally restricted to single-target queries. To reflect the ambiguity of real-world instructions, we introduce the Generalized Referring 3D Gaussian Splatting Segmentation (GR3DGS) task, which requires dynamically segmenting an arbitrary number of targets (0, 1, or $N$). To facilitate comprehensive evaluation of this new task, we construct two new benchmarks: GR-LERF and GR-ScanNet. Crucially, existing R3DGS paradigms exhibit fundamental technical bottlenecks that severely limit their performance on the GR3DGS task: they lack intrinsic 3D point-level understanding by operating merely on 2D rendered pixels, and they incur prohibitive computational overhead by requiring per-scene optimization to embed heavy semantic features. To dismantle these bottlenecks, we propose ZeroSplat, a novel training-free and zero-feature framework. ZeroSplat lifts 2D Vision-Language Model (VLM) priors into 3D space through robust multi-view geometric constraints. This strategy enables intrinsic point-level understanding without incurring any additional feature storage. Extensive experiments demonstrate that ZeroSplat significantly outperforms state-of-the-art methods across generalized and single-target scenarios while maintaining exceptional efficiency. Project Page: https://inkmind-ai.github.io/ZeroSplat

  </details>


- **[ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466)**  
  *Kaiyuan Tang, Chaoli Wang*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.18466) · [pdf](https://arxiv.org/pdf/2607.18466.pdf)
  > 💡 针对体积可视化中高斯溅射表示冗余问题，提出轻量神经网络预测隐式高斯与联合学习、熵编码压缩，提升重建质量并减小模型。

  <details><summary>Abstract</summary>

  Recent advances in differentiable Gaussian splatting have highlighted the potential of primitive-based approaches as alternative scene representations for interactive, high-quality, volume visualization (VolVis) of large datasets. However, the explicit nature of current primitive-based methods, combined with isolated optimization for each VolVis scene, results in redundant, non-compact representations. We present ECoNGS, an efficient compressive neural Gaussian splatting framework for VolVis scene representation. ECoNGS employs lightweight neural networks to dynamically predict implicit, editable Gaussian splats from explicit anchor points, effectively combining model compactness and parameter efficiency of implicit representations with high-performance rendering of explicit primitives. We explore a joint learning strategy that clusters geometrically similar scenes and shares parameters across them, significantly reducing overall training time and model size while maintaining reconstruction fidelity. To achieve a more compact scene representation, we further compress the explicit anchor attributes using a neural entropy model that estimates their probability distributions, enabling compact storage via entropy coding. We systematically investigate Gaussian initialization strategies and propose a simple yet effective scheme tailored for VolVis scenes, improving reconstruction accuracy and accelerating convergence. We evaluate ECoNGS qualitatively and quantitatively across various univariate and multivariate VolVis scenes, highlighting its superior performance over prior methods in training time, reconstruction quality, and model size. In particular, compared with the prior method iVR-GS, ECoNGS improves reconstruction quality by up to 2.2 dB in PSNR while reducing the model size by up to 6.1x and the training time by up to 5.9x. The code is available at https://github.com/TouKaienn/ECoNGS.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
