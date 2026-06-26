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
| 1 | **Survey & Benchmark** | 69 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 248 | — | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 35 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 55 | **+2** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 28 | **+1** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 33 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 46 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 13 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 16 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | **+1** | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 5 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 15 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 23 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-26 (UTC) — 5 new paper(s)

<details><summary><b>Generation / Diffusion</b> (2) · <a href="topics/generation.md">full list →</a></summary>

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223)**  
  *Jiyong Kim, Shuang Song, Ronjgun Qin*  
  `2026-06-25` · `cs.CV` · [abs](https://arxiv.org/abs/2606.27223) · [pdf](https://arxiv.org/pdf/2606.27223.pdf)
  > 💡 卫星高斯泼溅因视角受限导致立面空洞和保真度低，提出单目深度监督与阴影引导生成细化，几何误差降18%，视觉保真度提28-45%。

  <details><summary>Abstract</summary>

  Gaussian Splatting has been recently explored for satellite 3D reconstruction, demonstrating flexibility and efficiency in representing radiometrically diverse satellite scenes. However, the limited top viewpoint of satellite imagery results in insufficient supervision on building facades, leaving surface holes and degraded visual fidelity. Generative refinement, which leverages pretrained generative priors to iteratively refine and update the rendered images used as supervision targets, has recently been investigated to improve the visual fidelity of Gaussian-rendered images. However, since these models refine each view independently, the resulting images can generate hallucinations and break photo-consistency, leading to geometric degradation. To address these limitations, we propose SatSplatDiff, which aims to minimize geometric degradation prevalent in generative refinement. Building on photogrammetric DSM initialization and 2DGS-based shadow casting established in our prior work SatSplat, we first introduce monocular depth supervision and multi-scale geometric refinement to establish a geometrically accurate and well-regularized surface representation. We then apply shadow-guided generative refinement, where geometrically calculated shadow maps guide the Gaussians to maintain consistency with the underlying geometry, improving visual fidelity while reducing geometric degradation. Extensive evaluations on the IARPA2016 and DFC2019 datasets demonstrate state-of-the-art performance, reducing geometric MAE by up to 18% and improving visual fidelity (FID-CLIP) by 28-45% over existing baselines. Our method delivers up to 5x resolution enhancement with minimal hallucination and sensor-consistent appearance, demonstrating seamless cross-tile consistency and strong scalability for large-scale reconstruction. Source code is available at https://github.com/GDAOSU/SatSplatDiff

  </details>


- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071)**  
  *Zhisong Xu, Takeshi Oishi*  
  `2026-06-25` · `cs.CV` · [abs](https://arxiv.org/abs/2606.27071) · [pdf](https://arxiv.org/pdf/2606.27071.pdf)
  > 💡 针对旋转主导弱视差下稀疏全景图重建难题，提出无SfM框架，结合几何引导扩散补全与3DGS优化，提升稳定性。

  <details><summary>Abstract</summary>

  Panoramic sensing offers wide field-of-view coverage, yet 3D reconstruction from sparse panoramas remains challenging under rotation-dominant, weak-parallax motion. In such regimes, SfM/SLAM initialization is often ill-conditioned and unreliable. We present PanoImager, an SfM-free framework that combines feed-forward pose/depth priors, geometry-conditioned diffusion view completion, and depth-guided 3DGS optimization. Given only a few panoramic images, PanoImager decomposes them into local perspective views, synthesizes auxiliary observations to enrich sparse evidence, and stabilizes Gaussian optimization for improved cross-view consistency. Experiments on multiple benchmarks show improved stability under extreme sparsity, suggesting PanoImager as an offline/background component for map refinement when SfM/SLAM fails to initialize.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (1) · <a href="topics/editing.md">full list →</a></summary>

- **[Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting](https://arxiv.org/abs/2606.26754)**  
  *Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang*  
  `2026-06-25` · `cs.CV` · [abs](https://arxiv.org/abs/2606.26754) · [pdf](https://arxiv.org/pdf/2606.26754.pdf)
  > 💡 提出容量控制的最优传输框架，通过半平衡运输与列容量约束，解决多视角风格化中特征重用和一致性不足。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) provides an efficient and explicit representation for novel view synthesis, enforcing stylistic coherence across viewpoints remains challenging. Existing 3D stylization methods typically apply 2D feature-matching losses independently per rendered view, which leads to unstable style allocation, many-to-one feature reuse, and limited cross-view consistency. We propose a capacity-controlled framework for multi-view stylization of 3DGS, grounded in optimal transport. Specifically, we reformulate local style matching as a semi-balanced optimal transport problem. By introducing explicit column-capacity constraints with tunable strength, our formulation mitigates many-to-one matching and enables controllable allocation of style features. This transport-based objective provides a principled mechanism for balancing feature coverage and stylistic diversity while maintaining stable correspondences across viewpoints. To further enhance cross-view coherence, we incorporate a novel cross-view matching guidance to constrain correspondences between scene content and style patterns. In addition, we introduce several geometric regularizations to enhance the vanilla 3DGS, thereby enabling optimized Gaussian primitives to represent finer-grained textures during stylization. Extensive experiments demonstrate that our approach significantly improves multi-view stylistic consistency and produces stable, expressive 3D stylizations while preserving the core semantic structure of the scene.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985)**  
  *Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung*  
  `2026-06-25` · `cs.GR` · [abs](https://arxiv.org/abs/2606.26985) · [pdf](https://arxiv.org/pdf/2606.26985.pdf)
  > 💡 提出Vis4GS多视图可视分析工具，连接3DGS伪影与高斯属性及优化历史，实现原始级诊断。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) supports fast training and real-time rendering, but its optimization process remains difficult to interpret. Existing viewers mainly expose the final reconstructed scene and offer limited support for explaining how Gaussian properties contribute to visible artifacts or evolve during training. We present Vis4GS, a multi-view visual analytics tool for primitive-level diagnosis of 3DGS reconstruction artifacts. Built on the original 3DGS viewer and training framework, Vis4GS links rendered artifacts to Gaussian properties, View Coverage, training progress, and Gaussian genealogy through four linked views: an interactive Gaussian analysis view, a property timeline view, a Gaussian densification tree view, and a log and control panel. The system supports Gaussian selection, blur and needle-like artifact scoring, View Coverage analysis, and multiscale genealogy exploration of clone, split, prune, and clone-split events. By connecting scene-level artifacts with primitive-level evidence and optimization history, Vis4GS enables a structured workflow for diagnosing reconstruction failures beyond final-image inspection and global metrics. A user study also shows that Vis4GS provides stronger support for usability and artifact understanding than the original 3DGS viewer.

  </details>


</details>

<details><summary><b>Medical / Surgical</b> (1) · <a href="topics/medical.md">full list →</a></summary>

- **[Rendering Novel Views of MRI Using 3D Gaussian Splatting](https://arxiv.org/abs/2606.26236)**  
  *Robin Y. Park, Mark C. Eid, Rhydian Windsor, Amir Jamaludin, Ana I. L. Namburete, João F. Henriques, Andrew Zisserman*  
  `2026-06-24` · `eess.IV` · [abs](https://arxiv.org/abs/2606.26236) · [pdf](https://arxiv.org/pdf/2606.26236.pdf)
  > 💡 通过3D高斯泼溅对稀疏各向异性MRI进行体积重建并渲染新视角，提升脊柱狭窄分级的准确性。

  <details><summary>Abstract</summary>

  The objective of this paper is to improve radiological gradings measured on MRIs of spines, by resampling scans so that the new view planes are better aligned with the target anatomy than the original sparse images. To this end, we adapt 3D Gaussian Splatting to form a volumetric reconstruction starting from sparse anisotropic MRIs, and imaging planes aligned with the anatomy relevant for clinical evaluation are then sampled and rendered. The novel view plane is optimal for diagnostic radiological grading of the target anatomy, whereas the original MRI is not. The resampled scans are then used to predict ordinal severity grades of localised stenosis conditions in spinal MRIs. We compare our method against Voxel Interpolation resampling, which takes the average of inverse-distance weighted nearest neighbour intensities for each target coordinate. Experiments show that across all stenosis conditions, resampled scans using Gaussian Splatting produce more accurate stenosis gradings compared to the raw scans which do not include the complete anatomy in-plane, as well as images resampled using Voxel Interpolation.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
