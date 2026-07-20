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
| 1 | **Survey & Benchmark** | 81 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 286 | **+3** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 47 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 72 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 37 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 41 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 60 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 17 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 8 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 23 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 28 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 10 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-20 (UTC) — 4 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (3) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806)**  
  *Weitao Xiong, Tianyu Liu, Peng Li, Kok Chung Chua, Toa Chean Khim, Pu Wang, Hongfei Xue*  
  `2026-07-17` · `cs.CV` · [abs](https://arxiv.org/abs/2607.15806) · [pdf](https://arxiv.org/pdf/2607.15806.pdf)
  > 💡 采用物理-学习混合方法

  <details><summary>Abstract</summary>

  High-fidelity simulation of mmWave radar signals for dynamic human motion is valuable for developing radar-based human sensing models; yet collecting accurately labeled measurements for a specific deployment site remains expensive. We present HybridSim, a physics-learning hybrid simulator that synthesizes mmWave radar signals from dynamic human meshes under a fixed indoor room configuration, explicitly decoupling propagation into two components. To parameterize the human subject, we use a tri-plane representation to extract human features and a Graph Convolutional Network to stabilize optimization and mitigate gradient instability. The direct signal path is modeled via an inverse-rendering formulation with a microfacet BRDF to capture primary surface reflections. In parallel, the indirect path is approximated by combining 3D Gaussian Splatting with a virtual-receiver geometry to fit and reproduce site-specific multipath interference patterns, achieving substantially lower computational cost than explicit full ray tracing. Experiments in a fixed-room setting show improved agreement with a physically based reference and consistent gains on downstream radar-based human sensing tasks when using HybridSim for site-specific data augmentation.

  </details>


- **[ImprovedVBGS: Real-time Continual Variational Bayes Gaussian Splatting](https://arxiv.org/abs/2607.15542)**  
  *Damani Mguni-Coker*  
  `2026-07-17` · `cs.CV` · [abs](https://arxiv.org/abs/2607.15542) · [pdf](https://arxiv.org/pdf/2607.15542.pdf)
  > 💡 空间截断变分推理和高效重分配实现1680倍加速，在NeRF合成数据集上保持重建质量的同时达到实时连续学习。

  <details><summary>Abstract</summary>

  On-the-fly reconstruction is a key requirement for many applications in robotics and autonomous navigation. Variational Bayes Gaussian Splatting (VBGS) enables continual learning without replay buffers using Coordinate Ascent Variational Inference (CAVI), but its per-frame iterations over all observed points make it too slow for real-time use with strict memory and latency requirements. We present ImprovedVBGS, an accelerated framework for on-the-fly continual reconstruction. This is achieved primarily through (i) spatially truncated variational inference, and (ii) improved reassignment that uses forwarding, truncation and eliminates wasteful dynamic recompilation. On the NeRF synthetic dataset, we reduce mean per-frame latency from ~84.0 s to ~0.050 s on an RTX 3070 Ti, a 1680x speed-up while maintaining reconstruction quality.

  </details>


- **[Rendering 3D Gaussians on a Graph Processor](https://arxiv.org/abs/2607.15951)**  
  *Nicholas Fry, Ignacio Alzugaray, Mark Pupilli, Paul H. J. Kelly, Andrew J. Davison*  
  `2026-07-17` · `cs.GR` · [abs](https://arxiv.org/abs/2607.15951) · [pdf](https://arxiv.org/pdf/2607.15951.pdf)
  > 💡 在仅含片上SRAM的IPU上首次实现3D高斯渲染，利用网格通信和BSP模型，分析带宽与负载平衡瓶颈。

  <details><summary>Abstract</summary>

  We present the first implementation of a 3D Gaussian renderer on an Intelligence Processing Unit (IPU), comprising 1,472 independent tiles with only on-chip SRAM; constraints that approximate properties of efficient sensor-processor architectures. Our input scenes are 3D Gaussian maps from real-world sequences. Each tile 'owns' a screen-space region of the framebuffer; Gaussian primitives are routed to destination tiles via Manhattan-distance hops on a north-east-west-south (NEWS) grid, then distributed to overlapping neighbours in an expanding tree pattern. Computation follows the IPU's Bulk Synchronous Parallel (BSP) model, with inter-tile communication defined at compile time. We show this hardware allows us to exploit spatial and temporal locality by enabling local data transfer between cores. We evaluate the bottlenecks in this SRAM-only implementation: inter-tile bandwidth, per-tile SRAM capacity, and workload imbalance from non-uniform Gaussian density. We analyse how these constraints affect performance and render quality. This exploration raises broader questions for conventional GPUs and 3D representations, suggesting that direct inter-SM (streaming multiprocessor) communication might offer ways to reduce DRAM access in GPU kernels. We discuss these implications for the future of on-sensor and DRAM-free architectures. Project page: https://nmjfry.github.io/ipu-3dgs/

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[E3DGS: Unified Geometric-Photometric Equivariance for 3D Gaussian Splatting via Color-as-Geometry Embedding](https://arxiv.org/abs/2607.15536)**  
  *Chankyo Kim, Maani Ghaffari*  
  `2026-07-17` · `cs.CV` · [abs](https://arxiv.org/abs/2607.15536) · [pdf](https://arxiv.org/pdf/2607.15536.pdf)
  > 💡 利用颜色-几何嵌入统一表示，提出E3DGS等变架构，无需Clebsch-Gordan张量积，提升相机变换鲁棒性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) captures scenes by coupling explicit geometry (position, covariance) with view-dependent photometry (Spherical Harmonics). However, building $\mathrm{SE}(3)$-equivariant architectures on these primitives presents a fundamental representation bottleneck. Color has been treated as a signal rather than a geometric entity, making it nontrivial to unify symmetry across geometry and appearance as the camera frame changes. While translations are handled by relative coordinates, rotations act heterogeneously across attributes: $μ\mapsto Rμ$, $Σ\mapsto RΣR^\top$, and $f_\ell\mapsto D^\ell(R)f_\ell$. This mismatch complicates strict equivariance, leading existing methods to either discard or flatten SH coefficients, thereby breaking symmetry. We propose a unified solution rooted in representation theory: for SH degrees $\ell\le2$, photometry is algebraically isomorphic to a rank-2 geometric tensor. We prove that the Wigner-$D$ action on these SH coefficients can be exactly reformulated as the conjugation action on $3\times3$ matrices. Leveraging this, we introduce the Unified Matrix Embedding, a lifting that maps all Gaussian attributes into a unified carrier space, $\mathfrak{gl}(3)$. Building on the "Color-as-Geometry" formulation, we present E3DGS, a rigid-body ($\mathrm{SE}(3)$) equivariant architecture that processes 3D Gaussians without Clebsch-Gordan tensor products. Evaluations on object vision and action-conditioned Gaussian world modeling demonstrate that our unified approach yields strong robustness under camera-frame changes and improved data efficiency.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
