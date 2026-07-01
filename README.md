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
| 1 | **Survey & Benchmark** | 73 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 262 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 38 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 58 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 32 | **+2** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 34 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 53 | **+3** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 16 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 17 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 6 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 17 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 12 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 24 | **+1** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-01 (UTC) — 10 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036)**  
  *Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.32036) · [pdf](https://arxiv.org/pdf/2606.32036.pdf)
  > 💡 通过3D空间预测和点-图像变换器，从输入点集直接推断高斯原语，减少冗余并提升人体重建效率与质量。

  <details><summary>Abstract</summary>

  Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our key insight is to perform predictions directly in 3D space, enabling the network to learn and produce a highly compact representation. To this end, we propose PointSplat, a novel human-centric approach that directly infers Gaussian primitives from an input point set. The proposed method first estimates a coarse geometric proxy and performs ray casting to prune redundant points and establish explicit 2D--3D correspondences. Subsequently, it employs a Point-Image Transformer to fuse appearance and geometry features, predicting Gaussian attributes in a single forward pass. This design restricts predictions to foreground regions of interest, substantially reducing the total number of Gaussians while improving novel-view rendering quality. Extensive experiments demonstrate that PointSplat achieves higher efficiency and quality while exhibiting strong robustness to variations in view count and image resolution across multiple datasets.

  </details>


- **[LUNA: Learning Universal 3D Human Animation Beyond Skinning](https://arxiv.org/abs/2606.31981)**  
  *Peng Li, Rawal Khirodkar, Junxuan Li, Yuan Dong, Chen Cao, Yuan Liu, Wenhan Luo, Yike Guo, Shunsuke Saito*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.31981) · [pdf](https://arxiv.org/pdf/2606.31981.pdf)
  > 💡 提出无线性混合蒙皮的通用神经动画模型LUNA，用transformer运动回归器和混合监督实现零样本跨身份3D人体动画。

  <details><summary>Abstract</summary>

  Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often introduce artifacts due to imperfect fitting. We propose LUNA, an LBS-free universal neural animation model that directly maps multiple 2D controls like images, keypoints, sketches, and unseen characters into 3D Gaussian deformations, bypassing explicit body fitting. At its core, a transformer-based motion regressor disentangles global rigid motion from fine-grained local dynamics to capture both coherent movement and subtle non-rigid effects. To resolve the inherent ambiguity of 2D-to-3D lifting while scaling beyond fitted datasets, we introduce hybrid supervision that distills soft structural priors from an LBS teacher and a loss that supports training on both limited fitted data and large in-the-wild unlabeled videos. Extensive experiments show LUNA achieves competitive visual fidelity compared to LBS-based approaches, while delivering realistic human motion and zero-shot cross-identity generalization across diverse driving modalities. To the best of our knowledge, LUNA is the first end-to-end 3D animatable model that supports implicit 2D driving.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera](https://arxiv.org/abs/2606.31679)**  
  *Kristof Overdulve, Lode Jorissen, Nick Michiels*  
  `2026-06-30` · `cs.GR` · [abs](https://arxiv.org/abs/2606.31679) · [pdf](https://arxiv.org/pdf/2606.31679.pdf)
  > 💡 针对蝴蝶标本微距景深小和腹面不可见难题，结合焦点堆叠、非接触镜面和镜面感知3DGS实现全方位高保真新视角合成。

  <details><summary>Abstract</summary>

  Mounted butterflies are among the most striking objects in natural history collections. However, their beauty is notoriously hard to digitize in 3D: they are small and fragile, with microscopic hairs and vein structures. Capturing them in sufficient detail, therefore, requires a macro lens, which has a very limited Depth of Field (DoF). Moreover, a camera body cannot be maneuvered beneath a pinned specimen to photograph its ventral surface (the underside of the wings). We introduce an end-to-end pipeline that resolves these challenges to turn such specimens into photo-realistic 3D models viewable from every direction. It combines three ingredients: handheld focus stacking for all-in-focus macro capture without a tripod, a non-contact first-surface mirror system that exposes the ventral surface without touching the specimen, and a segmentation-free, mirror-aware 3D Gaussian Splatting extension. We validate the reconstructions on four diverse specimens.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)**  
  *Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.31918) · [pdf](https://arxiv.org/pdf/2606.31918.pdf)
  > 💡 提出基于点云条件视频修复的DriveWeaver，解决车辆插入光照不一致与3D资产依赖问题，实现高质量、可泛化的实时渲染。

  <details><summary>Abstract</summary>

  A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes. This process enhances scene diversity and facilitates the creation of various corner cases for testing and improving autonomous driving models. However, existing methods often rely on pre-reconstructed 3D assets, which frequently lead to lighting inconsistencies between the inserted foreground and the background. Moreover, the reliance on limited, manually-curated 3D assets hinders large-scale deployment. To address these challenges, we propose DriveWeaver, a novel framework for controllable vehicle insertion in autonomous driving simulation. Specifically, for a masked target insertion area, DriveWeaver performs video inpainting conditioned on vehicle point clouds to generate high-quality, temporally consistent vehicles. This video-inpainting-based approach ensures seamless blending between the foreground and background, while the readily available point cloud conditions enable superior generalization. To support long-term generation, we further design a global-to-local hierarchical inpainting strategy, ensuring the consistent identity and appearance of the inserted vehicles. Meanwhile, we extract explicit 3D Gaussian representations of the inserted vehicles through an urban reconstruction pipeline to enable real-time rendering for autonomous driving simulation. Extensive experiments across diverse datasets demonstrate that our method outperforms existing baselines in visual realism and geometric consistency, providing a robust tool for scalable autonomous driving scene augmentation.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (2) · <a href="topics/editing.md">full list →</a></summary>

- **[Intrinsic decomposition and editing of 3D Gaussian splats](https://arxiv.org/abs/2606.31637)**  
  *Alexandre Lanvin, Jeffrey Hu, Simon Lucas, Adrien Bousseau, George Drettakis*  
  `2026-06-30` · `cs.GR` · [abs](https://arxiv.org/abs/2606.31637) · [pdf](https://arxiv.org/pdf/2606.31637.pdf)
  > 💡 将3D高斯泼溅辐射场分解为漫反射反照率、阴影和视角残差，通过独立原语集和优化实现纹理编辑。

  <details><summary>Abstract</summary>

  Intrinsic decomposition which expresses image colors as the product of diffuse albedo and shading, possibly augmented with view-dependent residuals has a long history in image editing as it enables the modification of object colors and textures without altering lighting. We extend intrinsic decomposition to radiance fields represented with Gaussian splatting by proposing solutions to three key aspects of such decomposition. First, we describe how to model the intrinsic decomposition as independent sets of Gaussian primitives, which allows each set to adapt to the characteristics of the layer it represents. Second, we present an optimization procedure guided by data-driven predictions to disentangle multi-view photographs of a scene into the aforementioned intrinsic sets. Finally, we provide an editing workflow where users modify the texture of planar surfaces simply by modifying the albedo of that surface in one image. Capturing this edit within the intrinsic radiance field allows re-rendering of the edited scene with plausible lighting under arbitrary viewpoints.

  </details>


- **[Editable Physically-based Reflections in Raytraced Gaussian Radiance Fields](https://arxiv.org/abs/2606.30861)**  
  *Yohan Poirier-Ginter, Jeffrey Hu, Jean-François Lalonde, George Drettakis*  
  `2026-06-29` · `cs.GR` · [abs](https://arxiv.org/abs/2606.30861) · [pdf](https://arxiv.org/pdf/2606.30861.pdf)
  > 💡 针对3DGS中镜面反射不可编辑问题，提出利用漫反射与镜面缓冲区、路径追踪和光线

  <details><summary>Abstract</summary>

  Radiance fields such as 3D Gaussian Splatting allow real-time rendering of scenes captured from photos. They also reconstruct most specular reflections with high visual quality, but typically model them with "fake" reflected geometry, using primitives behind the reflector. Our goal is to correctly reconstruct the reflector and the reflected objects such as to make specular reflections editable. We present a proof of concept which exploits promising learning-based methods to extract diffuse and specular buffers from photos, as well as geometry and BRDF buffers. Our method builds on three key components. First, by using diffuse and specular buffers of input training views, we optimize a diffuse version of the scene and use path tracing to efficiently generate physically based specular reflections. Second, we present a specialized training method that allows this process to converge. Finally, we present a fast ray tracing algorithm for 3D Gaussian primitives that enables efficient multi-bounce reflections. Our method reconstructs reflectors and reflected objects, including those not seen in the input images, in a unique scene representation. Our solution allows real-time, consistent editing of captured scenes with specular reflections, including multi-bounce effects, changing roughness, and more. We mainly show results using ground truth buffers from synthetic scenes, and also preliminary results in real scenes with currently imperfect learning-based buffers. Code and data are available at: https://repo-sam.inria.fr/nerphys/editable-gaussian-reflections/

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (3) · <a href="topics/rendering.md">full list →</a></summary>

- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556)**  
  *Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.31556) · [pdf](https://arxiv.org/pdf/2606.31556.pdf)
  > 💡 利用辐射场合成新视图辅助高斯溅射优化，解决稀疏视图下初始几何敏感问题，提升重建质量并保持实时渲染。

  <details><summary>Abstract</summary>

  Generating high-quality novel views at real-time frame rates remains a central challenge in 3D vision, particularly in sparse-view scenarios. Neural radiance fields have demonstrated robust reconstruction from limited observations, but their reliance on volumetric rendering leads to high computational cost and slow inference. In contrast, Gaussian Splatting methods achieve real-time rendering through rasterization, but their optimization is highly sensitive to the quality of the initial geometry. This sensitivity becomes especially problematic in sparse-view settings, where limited observations often lead to incomplete or noisy point-cloud reconstructions. In this work, we present AugSplat, a simple framework for improving Gaussian Splatting in sparse-view regimes using radiance-field-based view augmentation. We first train a radiance field on the sparse input views and use it to synthesize additional images from nearby novel viewpoints, increasing the effective view-space coverage available for supervision. These synthetic views are then used as auxiliary supervision during Gaussian Splatting optimization. We study two variants: Staged AugSplat, which uses synthetic views for an initial optimization phase before switching to real images, and Dual AugSplat, which jointly trains on real and synthetic views with a decaying synthetic loss weight. Experiments on sparse-view mip-NeRF 360 scenes show that AugSplat improves reconstruction quality over standard Gaussian Splatting. Staged AugSplat achieves the strongest average performance, while Dual AugSplat provides a closely performing formulation that keeps real-image supervision active throughout training, and both variants preserve real-time rendering at inference.

  </details>


- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869)**  
  *Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis*  
  `2026-06-29` · `cs.GR` · [abs](https://arxiv.org/abs/2606.30869) · [pdf](https://arxiv.org/pdf/2606.30869.pdf)
  > 💡 利用射线追踪仅相交评估的对数缩放特性，通过密集初始化加速，实现接近光栅化速度的3D高斯射线追踪。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a popular representation for radiance field reconstruction, distinguished by the rendering speed of its rasterization-based renderer. While 3D Gaussians can also be ray traced, this approach has so far been slower, with 3D Gaussian Ray Tracing (3DGRT) taking nearly one order of magnitude longer to optimize. To address this, we present GRay, a fast ray tracer for 3D Gaussians designed to close this performance gap and match 3DGS's speed. Our method leverages the algorithmic difference between both approaches: unlike rasterization, ray tracing evaluates only Gaussians that are actually intersected by a ray, leading to potentially logarithmic--rather than linear--scaling in the number of primitives. This property allows ray tracing to better exploit dense scenes composed of numerous tiny Gaussians, a configuration which has largely been overlooked. Notably, we show that dense initialization--which creates many small Gaussians--slows down rasterization, but instead speeds up ray tracing. Designed to leverage this effect, GRay renders nearly 4x faster and optimizes nearly 10x faster than 3DGRT while maintaining similar quality, and has competitive speed with 3DGS albeit at somewhat lower quality. Code is available at https://repo-sam.inria.fr/nerphys/gray.

  </details>


- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809)**  
  *Annika Thomas, Mason Peterson, Jonathan P. How*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30809) · [pdf](https://arxiv.org/pdf/2606.30809.pdf)
  > 💡 现有3DGS均匀分配容量浪费资源，GaussLite提出任务驱动的稀疏化映射，通过LLM解析和开放词汇检测按需分配密度，在资源受限硬件上实时重建，ROI PSNR提升超2.7dB。

  <details><summary>Abstract</summary>

  Existing 3D Gaussian Splatting (3DGS) systems distribute representation capacity uniformly across a scene, ignoring the fact that many downstream robotic tasks engage only a fraction of the reconstructed geometry. This causes valuable onboard compute to be allocated towards optimizing irrelevant parts of the scene, either limiting online capacity or under-optimizing the most relevant parts of the scene. We introduce GaussLite, a task-driven 3DGS mapping system that conditions its representation density on a natural-language task specification. Given a posed RGB-D stream and a task such as "prepare to pick up the object on the desk," GaussLite uses a one-shot LLM parser to extract target and anchor objects, which are grounded per-frame by an open-vocabulary detector and segmented to produce per-pixel relevance masks in real time. The mapper allocates seeding density, gradient flow and scaling by task relevance. At matched Gaussian budget and real-time mapping at 4 Hz on resource-constrained hardware, GaussLite outperforms baselines on ROI PSNR on the Replica Dataset by an average +2.72 dB and on a real-hardware demonstration in indoor and outdoor settings by +2.23 dB. We further show that two task-specialized agents' maps can be fused into a single shared map via per-voxel voting on active-optimization counts in real time, outperforming concatenation by +3.42 dB while only sharing an average 7.08% of the map.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (1) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050)**  
  *Yujin Tang, Tian Zhou, Xin Lin, Cheng Tan, Yifan Hu, Rong Jin, SouYoung Jin, Liang Sun*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.31050) · [pdf](https://arxiv.org/pdf/2606.31050.pdf)
  > 💡 针对视频预测中像素级MSE导致模糊的问题，提出基于可微渲染的PDR方法，利用2D高斯表示与可微渲染器，实现高保真预测。

  <details><summary>Abstract</summary>

  How to accurately predict a high-fidelity future world? While the visual world is inherently continuous, existing deterministic video prediction models operate in discrete pixel space and are mainly optimized with pixel-wise mean squared error (MSE), which often leads to over-smoothed predictions and a lack of fine-grained visual details. To address these limitations, we propose Predictive Differentiable Rendering (PDR), a novel end-to-end video prediction paradigm that bridges the gap between discrete and continuous representations. Inspired by recent progress in 3D reconstruction with 3D Gaussian Splatting, we introduce PredGS, a lightweight and plug-and-play adapter based on 2D Gaussian representation, which could be seamlessly integrated with existing pixel space predictors, significantly improving spatial detail preservation with negligible computational overhead. Furthermore, we develop predgsplat, a CUDA-accelerated differentiable 2D Gaussian renderer supporting arbitrary channels. Each Gaussian is defined by 5 + C learnable parameters (position, scale, rotation, and C channel amplitudes) and achieves up to 10x faster rendering than the baseline. Optimized by a combined L1 and SSIM loss, PDR overcomes the inherent blurring tendencies of MSE Loss, significantly enhancing the prediction performance. Extensive experiments on diverse real-world benchmarks, including TaxiBJ, WeatherBench, KTH, and Human3.6M, demonstrate that PDR consistently surpasses existing methods, delivering superior detail preservation, visual fidelity, and predictive accuracy.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
