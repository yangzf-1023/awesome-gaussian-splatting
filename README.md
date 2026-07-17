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
| 2 | **Dynamic / 4D / Streaming** | 283 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 46 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 72 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 37 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 41 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 60 | **+3** | [topics/rendering.md](topics/rendering.md) |
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

### 2026-07-17 (UTC) — 7 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight](https://arxiv.org/abs/2607.14997)**  
  *Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang*  
  `2026-07-16` · `cs.RO` · [abs](https://arxiv.org/abs/2607.14997) · [pdf](https://arxiv.org/pdf/2607.14997.pdf)
  > 💡 针对语言条件四旋翼飞行，提出首个真实飞行的动作中心世界动作模型，用视频扩散Transformer预测动作块，提升跟踪与搜索性能。

  <details><summary>Abstract</summary>

  Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level waypoints, or instantaneous velocity commands, which provide limited supervision about how flight actions change future observations. We present AeroAct, an action-centered world-action model (WAM) for quadrotor navigation. To the best of our knowledge, AeroAct is the first WAM instantiated and demonstrated for real-world aerial flight. The model adapts a pretrained video diffusion Transformer to predict local trajectory-action chunks from egocentric visual history, proprioception, and language. Future first-person frames are used during training as dense consequence supervision, while deployment directly decodes actions without generating future video. To obtain aligned visual, state, language, and dynamically feasible action data, we build a DiffAero-based pipeline with complementary Isaac Lab and 3D Gaussian splatting renderers. We further introduce a low-cost handheld collection device that couples camera observations with motion estimates to recreate flight-like egocentric trajectories, and a self-guidance procedure that improves temporal consistency across overlapping trajectory chunks. Closed-loop simulation and real-world experiments show that temporal visual context improves target tracking and object-search performance, and that WAM-based policies can be executed on a physical quadrotor.

  </details>


- **[Instant NuRec: Feed-Forward 3D Gaussian Reconstruction for Driving Scene Simulation](https://arxiv.org/abs/2607.14203)**  
  *NVIDIA, :, Jiahui Huang, Jiawei Ren, Michal Tyszkiewicz, Bjoern Haefner, Michael Shelley, Xin Kang, Seung Wook Kim, Ning Xu, Qi Wu, Janick Martinez Esturo, Shengyu Huang, Nick Schneider, Laura Leal-Taixe, Zan Gojcic, Sanja Fidler*  
  `2026-07-15` · `cs.GR` · [abs](https://arxiv.org/abs/2607.14203) · [pdf](https://arxiv.org/pdf/2607.14203.pdf)
  > 💡 提出前

  <details><summary>Abstract</summary>

  3D simulation platforms are critical for autonomous driving because they enable end-to-end policy evaluation, thereby reducing development costs and improving safety. In recent years, neural simulation has become predominant, with methods such as NuRec playing a central role; however, these methods remain relatively slow and typically require per-scene tuning. In this work, we present Instant NuRec, a feed-forward neural reconstruction model that turns a short multi-view driving log into a fully simulatable 3D Gaussian Splatting (3DGS) world in a single forward pass. The model accepts multi-view input from a calibrated camera rig and emits a layered output consisting of static and dynamic 3DGS layers, a sky cubemap, and per-camera ISP corrections, while providing native support for non-pinhole camera models via 3DGUT. It reconstructs a 10-20-second multi-camera scene in roughly 1.5 seconds and achieves a PSNR on the Waymo Open Dataset that is 2.01 dB above the strongest evaluated baseline. Instant NuRec is deeply integrated into NuRec and is compatible with AlpaSim for closed-loop simulation.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048)**  
  *Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang*  
  `2026-07-16` · `cs.CV` · [abs](https://arxiv.org/abs/2607.15048) · [pdf](https://arxiv.org/pdf/2607.15048.pdf)
  > 💡 使用自适应网格高斯表示实现大规模道路表面高效鲁棒映射

  <details><summary>Abstract</summary>

  Road surface mapping plays a crucial role in autonomous driving, supporting high-definition map generation, lane-level perception, and automatic road annotation. Recent mesh-based road surface reconstruction methods have shown promising results, but they still suffer from limited reconstruction quality and high optimization cost, especially in large-scale driving scenarios. To address these limitations, we propose ROADGS-T, a robust and efficient large-scale road surface mapping framework based on adaptive meshgrid Gaussian representation. Specifically, we model the road surface by placing 2D Gaussian surfels on a meshgrid, where each surfel explicitly stores color, semantic, and geometric information. Compared with conventional mesh-based representations and 3D Gaussian primitives, the proposed meshgrid Gaussian representation better matches the thin-surface property of roads while significantly reducing redundant primitives and overlap during optimization. To further improve representation efficiency and structural fidelity, we introduce a road-structure-aware adaptive meshgrid strategy, which allocates denser Gaussian surfels to geometrically or semantically complex regions, such as lane markings, road boundaries, and height discontinuities, while maintaining a compact representation in flat road areas. Moreover, instead of relying on a single nearest vehicle pose, we design a trajectory-consistency-guided pose-robust refinement strategy, which estimates local surface priors from multiple neighboring poses and adaptively weights pose-guided height regularization according to their geometric consistency.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513)**  
  *Amir Said, Randall Rauwendaal*  
  `2026-07-16` · `cs.CV` · [abs](https://arxiv.org/abs/2607.14513) · [pdf](https://arxiv.org/pdf/2607.14513.pdf)
  > 💡 针对3DGS球谐系数数据量大问题，采用GPU并行纹理压缩编码，实现高效压缩与低视觉损失。

  <details><summary>Abstract</summary>

  Techniques for modeling 3D scenes from image collections, such as 3D Gaussian Splatting (3DGS), are capable of generating high-quality novel views by leveraging graphics primitives with view-dependent appearance. In 3DGS, spherical harmonic (SH) are employed to model view-dependent color, resulting in a large number of SH coefficients per primitive and large memory requirements. While compression approaches have been proposed to mitigate this problem, they do not exploit the capabilities of modern Graphics Processing Units (GPUs) for parallel decoding and rendering. In this paper, we propose a method for compressing SH color coefficients using texture compression schemes specifically designed for efficient parallel GPU decoding and supported by dedicated hardware acceleration. It is shown that those methods can compress color coefficients more effectively than 2D textures by exploiting the fact that primitives can be locally grouped and reordered according to color. Furthermore, we introduce a bit-rate control strategy that preserves random access, enabling large-scale parallelization without compromising rendering performance. Experimental results using BC1 and BC7 texture compression formats show that GPU-based decompression can be achieved with negligible or imperceptible degradation in the visual quality of rendered 3DGS scenes.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (3) · <a href="topics/rendering.md">full list →</a></summary>

- **[JADE-GS: Joint Alternating Deblurring Guided by Events in 3D Gaussian Splatting](https://arxiv.org/abs/2607.14990)**  
  *Haoyu Fu, Jiafeng Huang, Yuchen Wang, Shengjie Zhao*  
  `2026-07-16` · `cs.CV` · [abs](https://arxiv.org/abs/2607.14990) · [pdf](https://arxiv.org/pdf/2607.14990.pdf)
  > 💡 融合事件与图像先验的像素自适应门控及双向循环3DGS，实现高质量去模糊实时渲染，感知指标领先。

  <details><summary>Abstract</summary>

  When a camera moves fast during exposure, blur destroys the intra-exposure motion a 3D model needs to recover the sharp scene, while event cameras capture exactly this signal at microsecond resolution. Turning them into reliable 3D supervision faces two obstacles. First, the two restoration priors fail in opposite ways: physics-based event-integration priors preserve edges but accumulate drift; learned networks recover texture but distort boundaries. Second, existing pipelines run in one direction only, so raw event noise or the biases of fixed 2D pseudo-labels pass uncorrected into the geometry. JADE-GS addresses both: a pixel-adaptive routing gate fuses the complementary priors, and the resulting 2D restorer is coupled to a 3D Gaussian Splatting student in a bidirectional loop, where detached, multi-view-consistent renders and a physics-based reblurring constraint regularize the restorer, turning a fixed preprocessor into a geometry-aware predictor. Across synthetic and real benchmarks, JADE-GS attains the best perceptual quality, leading LPIPS and CLIP-IQA on both benchmarks with competitive PSNR and SSIM, and trainsin about one hour under 5 GB on a single consumer GPU while preserving real-time rendering.

  </details>


- **[Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481)**  
  *Andreas Meuleman, Linus Franke, Boris Zhestiankin, Camille Montemagni, George Drettakis*  
  `2026-07-16` · `cs.CV` · [abs](https://arxiv.org/abs/2607.14481) · [pdf](https://arxiv.org/pdf/2607.14481.pdf)
  > 💡 针对无序输入图像，利用共视图和聚类实现即时全局一致的三维高斯溅射重建。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become the method of choice for reconstructing and real-time rendering of captured scenes. To capture a scene with good visual quality, continuous image sequences are usually combined with out-of-order shots for better scene coverage. Structure from motion can reconstruct such captures, but only after they are all available and often with high computational cost. Incremental reconstruction methods -- often derived from SLAM solutions -- provide immediate feedback, but cannot handle the out-of-order capture we require. We provide the first immediate feedback solution for such radiance field capture that provides global consistency. We first introduce a method for fast matching in out-of-order sequences, by repurposing visual place recognition models and a covisibility graph, and provide an efficient way to find highly connected keyframes, improving quality even for ordered sequences. We show how these steps -- together with GPU optimization and careful Gaussian primitive placement -- provide fast local reconstruction, in our challenging radiance field reconstruction case. We then introduce a novel cluster-based method, again using the covisibility graph, to provide efficient loop closure that does not require sequential input. Finally, to handle large scenes in our context, we introduce a progressive hierarchy that allows our method to scale to large environments, without compromising efficiency. Our results show we provide immediate feedback 3DGS reconstruction with good visual quality in several datasets, with up to thousands of input images.

  </details>


- **[G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470)**  
  *Dasong Gao, Vivienne Sze, Sertac Karaman*  
  `2026-07-16` · `cs.CV` · [abs](https://arxiv.org/abs/2607.14470) · [pdf](https://arxiv.org/pdf/2607.14470.pdf)
  > 💡 利用检测跟踪2D高斯斑块并三角化为3D斑块，实现快速内存高效少视图表面重建。

  <details><summary>Abstract</summary>

  Few-view surface reconstruction recovers the visible surfaces of a scene from a few posed RGB images, providing the 3D models that robots need to explore and interact online. On mobile platforms, the reconstruction must be fast and geometrically accurate while keeping a small memory footprint to ensure safe and efficient operation. 3D Gaussian Splatting (3DGS) offers a high-fidelity scene representation, but building it from a few views is ill-posed, as many distinct surfaces reproduce the same images, making traditional photometric methods prone to "floater" artifacts. End-to-end methods resolve the ambiguity by regressing splats with large, usually Transformer-based, networks that require heavy compute and memory while generalizing poorly to new scenes. We propose G2SR, which exploits a well-posed core of the task: given cross-view 2D splat correspondences, 3D splats follow analytically from multi-view geometry. G2SR employs a lightweight neural frontend to detect and track 2D Gaussian splats on the image plane and an analytic backend to triangulate each into a metric-scale 3D splat. On ScanNet, Replica, and DTU, G2SR matches or exceeds the geometric accuracy of state-of-the-art end-to-end methods while running at 69-89 reconstructions per second within 203 MB of GPU memory (5-107x less) for 2- and 3-view inputs at 384 x 512 resolution, offering a practical path to online Gaussian-based surface reconstruction.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
