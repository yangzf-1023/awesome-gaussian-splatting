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
| 1 | **Survey & Benchmark** | 50 | **+1** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 217 | **+3** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 25 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 40 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 19 | **+1** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 30 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 30 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 8 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 11 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 2 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 11 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 20 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-01 (UTC) — 7 new paper(s)

<details><summary><b>Survey & Benchmark</b> (1) · <a href="topics/survey.md">full list →</a></summary>

- **[Smaller and Faster 3DGS via Post-Training Dictionary Learning](https://arxiv.org/abs/2605.30396)**  
  *Jiarong Gong, Jonas Unger, Ehsan Miandji*  
  `2026-05-28` · `cs.GR` · [abs](https://arxiv.org/abs/2605.30396) · [pdf](https://arxiv.org/pdf/2605.30396.pdf)
  > 💡 提出基于字典学习的后训练压缩框架，无需重训练，实现3.95倍压缩同时提升渲染速度约24%并保持图像质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a promising neural scene representation for real-time rendering, but trained models often suffer from large memory footprints, limiting deployment on less powerful devices. Existing compression techniques often lead to architectures with several additional trainable parameters. While achieving outstanding compression ratios, they introduce noticeable drops in image quality. In this work, we introduce the first dictionary-learning-based compression framework for 3DGS. The proposed post-training compression pipeline can be deployed in virtually any 3DGS model without the need for re-training or modifications to existing 3DGS models. Our compression framework is straightforward to implement, yet provides significant compression capabilities, preserves image quality, and improves real-time rendering performance. Across 13 benchmark scenes, our approach achieves an average compression ratio of 3.95x, 3.10x, and 4.55x when applied to 3DGS, 3DGS-MCMC, and PixelGS, respectively. This yields consistent rendering speedups of 23.3%, 24.3%, and 25.3%, while maintaining image quality.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (3) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.30863)**  
  *Youngtae Han, Sung-hwan Han, Youngmin Yi*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30863) · [pdf](https://arxiv.org/pdf/2605.30863.pdf)
  > 💡 提出静态-动态分解的高斯泼溅框架，结合前馈编码器和光流模型，实现高效高保真动态场景重建，无需COLMAP预处理。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction and novel view synthesis are fundamental to next-generation visual intelligence applications such as virtual reality, robotics, and digital twins. However, high-fidelity reconstruction of complex, time-varying scenes from arbitrary viewpoints remains a significant challenge. Existing dynamic 3DGS methods suffer from computational inefficiency, since they model all Gaussians as dynamic components. While recent decomposition-based approaches address this issue, they still struggle with degraded reconstruction quality and prolonged training time. To mitigate these limitations, we propose a novel dynamic reconstruction framework built upon an efficient static-dynamic decomposition strategy using a Feed-Forward Gaussian Splatting encoder and an optical flow model. By eliminating redundant computations on static regions, our method achieves state-of-the-art performance, outperforming existing baselines across rendering quality, training and rendering speed, and storage efficiency. Notably, on the Neural 3D dataset, our framework requires only 10 minutes for training and achieves a rendering speed of over 700 FPS on a single NVIDIA RTX 5090 GPU at resolution of 1352x1014. Furthermore, our decomposition strategy eliminates the need for COLMAP preprocessing and enables deterministic initialization, thereby enhancing both efficiency and reproducibility.

  </details>


- **[Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation](https://arxiv.org/abs/2605.30855)**  
  *Hanlin Chen, Jiaxin Wei, Xibin Song, Yifu Wang, Steve Wang, Hongdong Li, Pan Ji, Gim Hee Lee*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30855) · [pdf](https://arxiv.org/pdf/2605.30855.pdf)
  > 💡 针对长序列AR视频生成中的累积漂移问题，提出潜在高斯记忆与偏差学习框架，实现稳健的状态保持与SOTA性能。

  <details><summary>Abstract</summary>

  Frame-wise action-controlled image-to-video generation is a promising paradigm for interactive world simulation, where each control signal should elicit an immediate visual response. However, maintaining visual fidelity and 3D consistency over long autoregressive rollouts remains challenging. Existing 3D-aware methods often suffer from catastrophic drift due to two impediments: information loss from \textit{Latent--RGB Cycling}, where generated latents are repeatedly decoded to RGB and re-encoded for future conditioning, and the training--inference gap induced by the \textit{error-free hypothesis}, where clean training memory fails to match prediction-corrupted inference memory. To address these challenges, we present \textbf{Robust Dreamer}, a memory-augmented framework built around how to design 3D memory and how to use it robustly. First, we introduce \textbf{Latent Gaussian Memory}, which anchors diffusion latents inherited from the generation process to Gaussian primitives and recalls them via latent-space Gaussian splatting. This provides dense, geometry-aware, view-aligned conditioning while avoiding accumulated degradation from repeated VAE conversion. Second, we propose \textbf{Deviation Learning with Dynamic Deviation Archive}, which synthesizes rollout-induced latent deviations through a one-step approximation, stores them by autoregressive stage and denoising timestamp, and injects them into historical memory during training. This exposes the generator to realistic corrupted memory states and teaches internal correction before inference. Experiments on ScanNet, DL3DV, and OmniWorldGame demonstrate state-of-the-art long-horizon performance.

  </details>


- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595)**  
  *Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.31595) · [pdf](https://arxiv.org/pdf/2605.31595.pdf)
  > 💡 用紧凑高斯查询令牌聚合时序特征，实现前馈4D

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction from monocular video remains a fundamental challenge in computer vision. Existing feed-forward methods predict 3D Gaussians pixel-wise for each frame, suffering from duplicated Gaussians and view-dependent biases that hinder effective learning of scene motion. We present C4G, a feed-forward 4D reconstruction framework built upon a compact set of timestamp-conditioned learnable Gaussian query tokens. Each token aggregates corresponding features across the full temporal context and decodes a 3D Gaussian whose position is modulated by the target timestamp, enabling globally coherent motion modeling without per-scene optimization. To capture fine-grained details, we further introduce a video diffusion model-based rendering enhancement module. Since our framework effectively aggregates features into Gaussians, we extend this capability to feature lifting, producing a 4D feature field that supports point tracking and dynamic scene understanding. C4G achieves strong novel-view synthesis performance using significantly fewer Gaussians and without requiring camera poses, while exhibiting stronger motion modeling and robustness to large temporal gaps.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[Benchmarking Single-Step Inpainting Methods for Multi-Object 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2605.30987)**  
  *Finn Dröge, Cecilia Curreli, Abhishek Saroha, Daniel Cremers*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30987) · [pdf](https://arxiv.org/pdf/2605.30987.pdf)
  > 💡 对比2D修复器用于3DGS场景移除，重建型优于扩散，从头初始化胜于微调，并引入多对象真实数据集。

  <details><summary>Abstract</summary>

  The tasks of object removal and inpainting 3D Gaussian Splatting (3DGS) scenes face challenges such as 3D consistency across camera views. In comparing 2D inpainters and their suitability for the 3D domain, we find that reconstruction-based inpainters outperform generative diffusion models in 3D consistency. Integrating these 2D inpainters into different single-step methods for creating and finetuning 3DGS scenes, our results indicate that initializing the scene from scratch produces higher quality results than finetuning the existing scene. Using a state-of-the-art generative 2D inpainter, we create a straightforward baseline to underline the importance of object removal before inpainting in the 3D setting. Since 360° datasets rarely include real-world ground truths, and challenging occlusion scenarios are equally sparse, we introduce a novel multi-object scene with recorded ground truth data and many views with object occlusions.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (1) · <a href="topics/editing.md">full list →</a></summary>

- **[Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419)**  
  *Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.31419) · [pdf](https://arxiv.org/pdf/2605.31419.pdf)
  > 💡 提出基于可微三角形splatting的密集RGB-D SLAM，实现跟踪与建图，支持在线网格编辑，几何性能优于基线。

  <details><summary>Abstract</summary>

  We present a dense RGB-D SLAM system using differentiable triangles as the 3D map representation. While 3D Gaussian Splatting has emerged as the leading method for novel-view synthesis, triangles remain the standard primitive for traditional rendering hardware, game engines, and downstream tasks requiring explicit geometry such as simulation, collision, and editing. Recent offline methods have demonstrated that an unstructured 'triangle soup' can be optimised into a photorealistic mesh via Delaunay triangulation across a set of posed images. Building upon this insight, we present the first dense SLAM system to employ Triangle Splatting to perform both tracking and mapping through online differentiable rendering of a triangle soup. The map can be converted into a connected mesh on-the-fly via restricted Delaunay triangulation, enabling new online capabilities such as mesh deformation and collision checking. On Replica and TUM-RGBD, our system outperforms baselines on 3D geometry, matches the camera-tracking accuracy, and enables online mesh-based scene editing.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting](https://arxiv.org/abs/2605.31376)**  
  *Hannah Schieber, Dominik Frischmann, Victor Schaack, Angela P. Schoellig, Daniel Roth*  
  `2026-05-29` · `cs.RO` · [abs](https://arxiv.org/abs/2605.31376) · [pdf](https://arxiv.org/pdf/2605.31376.pdf)
  > 💡 针对未知室内环境语义导航难题，提出TSDF引导高斯泼溅的混合框架，结合YOLO检测

  <details><summary>Abstract</summary>

  Autonomous robots in unknown indoor environments require both reliable collision avoidance and object-level understanding. Classical representations such as TSDF support safe planning but lack semantics, while photorealistic methods like Gaussian Splatting (GS) provide rich appearance yet suffer from soft geometry, limiting precise obstacle avoidance. We present LiftNav, a hybrid navigation framework built on GSFusion's TSDF+GS dual map, augmented with a real-time pipeline of YOLO-based detection, TSDF-based 3D lifting, and B-spline trajectory optimization. This design enables flexible semantic navigation without dense 3D embeddings. We further introduce a hinge-loss-based collision penalty that improves trajectory smoothness and safety. We evaluate our approach in a simulation using the Replica dataset. Compared against a state-of-the-art radiance field baseline we show a 100% feasibility rate and shorter trajectories.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
