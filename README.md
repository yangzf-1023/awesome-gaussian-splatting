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
| 1 | **Survey & Benchmark** | 66 | **+4** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 246 | **+4** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 33 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 50 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 24 | **+1** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 32 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 44 | **+4** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 13 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 16 | **+1** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 3 | **+1** | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 5 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 15 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 23 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-23 (UTC) — 17 new paper(s)

<details><summary><b>Survey & Benchmark</b> (4) · <a href="topics/survey.md">full list →</a></summary>

- **[Temporally Aware Densification for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.23212)**  
  *Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23212) · [pdf](https://arxiv.org/pdf/2606.23212.pdf)
  > 💡 提出可见性感知致密化，用时域自适应阈值和偏移扭曲改进动态高斯致密化，提升动态场景重建质量。

  <details><summary>Abstract</summary>

  Despite modeling temporal motion, dynamic 3D Gaussian Splatting (3DGS) methods still inherit a static densification strategy that is ill-suited for dynamic scenes. This neglect of temporal behavior leads to under-reconstructed and blurry dynamic regions, as short-lived Gaussians receive sparse supervision and fail to densify effectively. We propose a Visibility-Aware Densification (VAD) framework that integrates temporal visibility into the densification process, ensuring that Gaussians are refined based on their actual temporal presence. A Temporally-Adaptive Thresholding (TAT) mechanism further adjusts each Gaussian's densification threshold according to its temporal lifespan, promoting balanced refinement of both static and dynamic regions. Finally, a Temporal Offset Warping (TOW) design enhances deformation capacity around temporal centers, extending the lifespan of highly dynamic Gaussians and facilitating more effective densification. Our approach achieves substantial improvements in the visual quality of dynamic regions, outperforming existing methods across three dynamic multi-view benchmark datasets. Moreover, the proposed VAD module generalizes across diverse dynamic 3DGS methods, consistently improving dynamic reconstruction as a plug-and-play component.

  </details>


- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031)**  
  *Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23031) · [pdf](https://arxiv.org/pdf/2606.23031.pdf)
  > 💡 提出组合稀疏体素光栅化框架，用多八叉树表示动态与静态场景，通过LiDAR先验加速训练，高效重建动态驾驶场景。

  <details><summary>Abstract</summary>

  Reconstructing dynamic urban scenes remains challenging due to the unbounded nature of driving environments and the presence of multiple dynamic objects. Currently, potentially faster sparse voxel methods are mainly designed for static scenarios. On the other hand, dynamic approaches based on 3D Gaussian Splatting, despite their high-fidelity, are often time-consuming for driving scenarios and exhibit uncontrollable memory growth in large scenes. To address these limitations, we present DrivingVoxels, a compositional sparse voxel rendering framework for dynamic driving scenes. Our method jointly rasterizes sparse voxels from multiple independent octrees within a single rendering pass. Each rigid dynamic object is represented by an octree defined in its local coordinate frame, while a separate static octree models the stationary background. DrivingVoxels adopts a fully explicit, neural-free representation together with a LiDAR-guided structural initialization that efficiently captures scene geometry. We evaluate our framework on the PandaSet benchmark, demonstrating that DrivingVoxels performs on par on perceptual metrics and better on structural metrics for NVS and reconstruction while requiring shorter training times than previous 3DGS-base methods to an efficient optimization workflow anchored by a strong LiDAR prior.

  </details>


- **[LOGOS: LiDAR-Only Gaussian Elevation Splatting for Unified Tiny Obstacle Segmentation](https://arxiv.org/abs/2606.21527)**  
  *Nan Ming, Yeqiang Qian, Chunxiang Wang, Ming Yang*  
  `2026-06-19` · `cs.RO` · [abs](https://arxiv.org/abs/2606.21527) · [pdf](https://arxiv.org/pdf/2606.21527.pdf)
  > 💡 提出基于2D高斯原语的无反向传播LiDAR高程溅射方法，实现微小障碍物鲁棒分割，在退化点云中性能显著优于现有方法。

  <details><summary>Abstract</summary>

  Robust obstacle segmentation is essential for the safety of intelligent robots, where LiDAR-based perception systems play a fundamental role in the robot-environment interaction. While extensive LiDAR-based approaches have demonstrated high performance on common obstacles in urban scenarios, their results on tiny obstacles such as curbs, gravel, and potholes remain unsatisfactory due to the significant similarity between tiny obstacles and inherent road undulations. Moreover, their segmentation accuracy even deteriorates sharply when the LiDAR scans suffer from degradation in challenging off-road scenes. To overcome these bottlenecks, we propose LOGOS, a LiDAR-only unified tiny obstacle segmentation system, which models the road surface as a continuous mixture of 2D Gaussian primitives and distinguishes tiny obstacles via high-presicion elevation estimation. Unlike existing Gaussian splatting methods that rely on iterative RGB training, LOGOS is a backpropagation-free LiDAR-only approach. It directly estimates Gaussian parameters via a freespace-aware initialization by incrementally pruning non-road primitives using smoothness constraints. Subsequently, pointwise signed distances are computed via a novel normal-aware elevation splatting function, ensuring robustness to both flat and sloped terrains. We evaluate LOGOS on a highly heterogeneous benchmark of point cloud frames collected from urban mobility scenarios and mining haulage off-road environments. These data are practically acquired using different LiDAR sensors and exhibit large variations in point density, terrain roughness, and obstacle types. Experiments on the road and off-road scenes demonstrate that LOGOS significantly outperforms other state-of-the-art methods, particularly in degraded point cloud regions and challenging off-road scenarios, while maintaining real-time efficiency.

  </details>


- **[ACE-GS: Acing the Trade-off with Accurate, Compact and Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2606.21244)**  
  *Jijian Zhao*  
  `2026-06-19` · `cs.CV` · [abs](https://arxiv.org/abs/2606.21244) · [pdf](https://arxiv.org/pdf/2606.21244.pdf)
  > 💡 ACE-GS通过动量一致稠密化、统计剪枝和跨维频率补偿，在3-5分钟收敛，加速3.7倍并提升PSNR 0.89dB。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting achieves exceptional real-time rendering, but its substantial computational and storage demands hinder widespread deployment. Existing accelerated paradigms often aggressively prune primitives for rapid convergence, causing severe loss of high-frequency details. To address this, we tackle the fundamental problem of achieving both exceptional rendering quality and ultra-fast reconstruction speed. In this paper, we propose ACE-GS, a progressive optimization framework tailored for accurate, compressed, and efficient scene representation. We realize that precise primitive management is the key to breaking this trade-off. Therefore, we first design a momentum consistency-guided densification strategy, strictly constraining primitive growth onto authentic geometric manifolds to avoid computational waste while significantly accelerating convergence. Building upon this efficient initialization, we deploy a statistical sensitivity-driven sparsification mechanism to precisely prune redundant primitives, yielding a further compressed footprint. Finally, to thoroughly compensate for the risk of micro-structure loss caused by the aforementioned strict primitive control, we introduce a cross-dimensional residual frequency compensation scheme that explicitly back-injects high-frequency error energy into primitive attributes, perfectly restoring sharp geometric details. Extensive experiments validate our superiority. While maintaining a highly compact scene representation, our system achieves up to 3.7 times training acceleration against the rapid framework Speedy-Splat. Requiring only 3 to 5 minutes to converge, ACE-GS secures the highest structural similarity and achieves a peak PSNR improvement of up to 0.89 dB over the original 3DGS, establishing a new benchmark for ultra-fast and high-fidelity novel view synthesis.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (4) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688)**  
  *Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23688) · [pdf](https://arxiv.org/pdf/2606.23688.pdf)
  > 💡 通过因果潜在条件适应单视图3D重建生成时序一致初始预测，再经遮挡感知优化和扩散先验细化，显著提升大变形和遮挡下的4D重建质量。

  <details><summary>Abstract</summary>

  Reconstructing dynamic non-rigid objects from monocular video requires integrating visual cues from direct observations with data-driven priors over geometry and appearance. Prior approaches either learn to directly predict 4D representations from visual input or initialize a 3D representation that is subsequently deformed and refined based on video evidence. However, the former are constrained by the scarcity of 4D training data, while the latter leverage priors only for the initial reconstruction and rely solely on video supervision thereafter; neither handles complex in-the-wild scenarios with large deformations and occlusions well. We present Lift4D, a test-time optimization framework that addresses both limitations. First, we adapt an existing single-view 3D reconstruction model to yield temporally consistent per-frame predictions via causal latent conditioning, providing a coherent initialization for a deformable 3D Gaussian Splatting representation. We then ``sculpt'' this representation to match the input video through an occlusion-aware optimization that faithfully recovers visible surface details while completing unobserved regions using a view-conditioned diffusion prior. We demonstrate that Lift4D clearly improves over prior 4D reconstruction methods, particularly on challenging in-the-wild sequences with severe occlusions and non-rigid motion.

  </details>


- **[MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455)**  
  *Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23455) · [pdf](https://arxiv.org/pdf/2606.23455.pdf)
  > 💡 针对现有物理仿真忽略温度场的问题，提出MeGAS将热力学相变融入3DGS，实现物理一致的热力学场景编辑与高保真渲染。

  <details><summary>Abstract</summary>

  Recent advances integrate physically grounded Newtonian dynamics with neural rendering frameworks, narrowing the gap between photorealistic scene reconstruction and physics-based animation. However, existing approaches focus on mechanically driven dynamics while neglecting temperature, a fundamental yet invisible physical factor underlying phenomena such as melting, solidification, and other thermomechanical processes. In this paper, we propose MeGAS, a novel framework that incorporates thermomechanical phase-change dynamics into 3D Gaussian Splatting (3DGS). Specifically, we propose a new thermomechanical dynamic Gaussian Splatting representation that augments 3DGS with temperature attributes and employs a heat advection-diffusion solver with MPM dynamics incorporating phase transitions, enabling physically plausible and visually realistic synthesis of thermophysical phenomena. Furthermore, a new topology-adaptive Gaussian rendering strategy is proposed to mitigate cracking and floaters under extreme deformation. Extensive experiments demonstrate that MeGAS produces physically consistent thermomechanical behavior while maintaining high-fidelity photorealistic rendering, advancing toward physics-integrated world models.

  </details>


- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197)**  
  *Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt*  
  `2026-06-20` · `cs.CV` · [abs](https://arxiv.org/abs/2606.22197) · [pdf](https://arxiv.org/pdf/2606.22197.pdf)
  > 💡 针对动态高斯喷溅中运动一致性与视觉保真度的矛盾，提出多级竞争分配框架，显著提升渲染质量并保持实时性。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian splatting faces a fundamental tension between motion consistency and visual fidelity. Deformation-based approaches preserve temporal correspondence but suffer from motion over-factorization, oversmoothing high-frequency dynamics. In contrast, 4D-primitive methods capture fine visual details yet incur temporal overparameterization, breaking object identity and leading to severe storage overhead. To resolve this, we introduce Multi4D, a framework for high-fidelity dynamic Gaussian Splatting based on multi-level competitive allocation. Instead of a monolithic representation, we distribute modeling capacity across three structured levels: static structure, persistent dynamic geometry, and transient appearance primitives. Through shared rasterization and residual-driven optimization, these levels dynamically compete to explain photometric error, enabling adaptive specialization without pre-assigned decomposition. This allocation preserves long-term motion consistency while capturing fine dynamic detail, achieving state-of-the-art rendering quality and real-time performance with significantly fewer dynamic primitives. Furthermore, because our representation explicitly tracks compact persistent Gaussians over time, semantic features can be embedded afterward, enabling Multi4D to achieve state-of-the-art 4D segmentation accuracy with an order-of-magnitude speedup. Project page: https://batfacewayne.github.io/Multi4D.io/

  </details>


- **[Scene-Level Heterogeneous Physics Simulation with 3D Gaussian Splats](https://arxiv.org/abs/2606.21753)**  
  *Xiaoyang Liu, Shangzhe Wu, Kai Han*  
  `2026-06-19` · `cs.GR` · [abs](https://arxiv.org/abs/2606.21753) · [pdf](https://arxiv.org/pdf/2606.21753.pdf)
  > 💡 将3DGS等异构资产统一为物理粒子集，首次实现场景级多求解器物理模拟与非刚性变形。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has achieved state-of-the-art photorealistic rendering, but the representation gap prevents these assets from being physically interactive. Production-grade physics engines do not understand the 3DGS representation, while prior physics-for-3DGS methods are monolithic silos. These prior works are fundamentally limited, demonstrating only object-centric physics in isolated environments, such as on an ideal plane. They are incapable of interacting with complex static collision geometry or heterogeneous assets. We propose a novel framework that, for the first time, bridges this gap by enabling 3DGS assets to participate in scene-level, heterogeneous, multi-solver physical simulations. Our core contribution is a Representation Abstraction Framework that translates all diverse assets, including 3DGS, virtual meshes, and fluids, into a unified physical particle set. This abstraction is key to enabling complex behaviors, such as the non-rigid deformation of 3DGS assets, within a unified physics pipeline. This particle set, along with the static scene collision boundaries derived from scene capture, is processed within a solver-agnostic physics kernel. The physical results are then mapped back to drive each asset's specific visual reconstruction. This architecture unlocks capabilities impossible with prior art. We demonstrate complex, two-way interactions between deformable 3DGS assets, standard CG assets such as fluids and meshes, and large-scale captured static environments, showcasing realistic coupled phenomena that were previously unattainable.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091)**  
  *Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao*  
  `2026-06-20` · `cs.RO` · [abs](https://arxiv.org/abs/2606.22091) · [pdf](https://arxiv.org/pdf/2606.22091.pdf)
  > 💡 提出ACEsplat，通过自监督场景坐标回归构建内部几何先验，实现仅由RGB和位姿快速重建3DGS，无需外部初始化，15-25分钟完成。

  <details><summary>Abstract</summary>

  Per-scene 3D Gaussian Splatting (3DGS) enables high-fidelity rendering, but practical robotic and AR scene capture pipelines often depend on external geometric initialization (e.g., SfM point clouds or depth estimates), which can be slow and brittle in on-site deployment. We present ACEsplat, a fast per-scene optimization framework that reconstructs 3D Gaussian representations from RGB images and camera poses only, without requiring external 3D priors (e.g., precomputed SfM models or supervised depth maps). ACEsplat uses a two-stage pipeline: (1) a self-supervised scene coordinate regression (SCR) module builds an internal geometry prior within 4--5 minutes; (2) SCR features and coordinate priors are fused by a lightweight Gaussian initialization head, followed by per-scene 3DGS optimization. On static-view rendering, ACEsplat achieves 29.11 dB PSNR on Wayspots with real-time SLAM poses and 33.20 dB on Cambridge Landmarks with SfM-refined poses. On RealEstate10K sparse-view novel view synthesis, it achieves competitive image fidelity under a challenging 2-view setting. ACEsplat completes scene-specific SCR mapping and 3DGS reconstruction within 15--25 minutes on a single GPU, making it a practical RGB+pose-only solution for rapid scene setup in robotics and mixed-reality applications.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[Lighting-Consistent Object Transfer Across Radiance Fields](https://arxiv.org/abs/2606.22481)**  
  *Nicolás Violante, George Kopanas, Linus Franke, Julien Philip, George Drettakis*  
  `2026-06-21` · `cs.GR` · [abs](https://arxiv.org/abs/2606.22481) · [pdf](https://arxiv.org/pdf/2606.22481.pdf)
  > 💡 扩散模型协调不同3DGS场景间光照不一致的对象转移，利用异质数据集训练并通过后优化提升合成质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is widely used to capture and render real scenes. Compositing objects from one capture into another has applications in many domains, such as VFX, architecture and interior design, or marketing. However, extracting an object from a source scene and naively pasting it into a target scene will fail to produce realistic results due to the different lighting conditions between the two scenes. To address this problem, we introduce a diffusion model that harmonizes naively composited images with inconsistent lighting. The model is trained with a heterogeneous dataset of image pairs (inconsistent composite input, consistent output), combining synthetic, generated, and real data. Our complete 3D solution allows a user to extract an object from the source scene and composite it into the target scene. From this, the (inconsistent) views of the target scene with the composite object are rendered. Our diffusion model harmonizes each one of these views, which are finally consolidated in a 3DGS representation with a post-optimization step. Our method provides visually compelling results, making object transfer between 3DGS easy to use and significantly improving quality compared to previous methods.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (1) · <a href="topics/editing.md">full list →</a></summary>

- **[From Uncertainty to Stability and Fidelity: Guiding Sparse-View 3D Gaussian Splatting with Fisher Information](https://arxiv.org/abs/2606.20842)**  
  *Junbao Zhou, Qingshan Xu, Yuan Zhou, Xiaolong Shen, Beier Zhu, Kesen Zhao, Yiming Zeng, Chen Bai, Cheng Lu, Hanwang Zhang*  
  `2026-06-18` · `cs.CV` · [abs](https://arxiv.org/abs/2606.20842) · [pdf](https://arxiv.org/pdf/2606.20842.pdf)
  > 💡 利用Fisher信息指导立体增强与不确定性正则化，减少随机性，提升稀疏视图3DGS的稳定性和渲染保真度。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a promising technique for novel view synthesis. However, 3DGS requires dense input views to achieve high-quality rendering. In sparse-view scenarios, 3DGS often prones to overfitting, resulting in noticeable artifacts and degraded rendering quality. Previous methods explore to address this issue by introducing additional priors (e.g. depth priors) or integrating regularization techniques (e.g. Dropout). However, these methods are often applied without principled guidance. In particular, prior-based augmentation typically samples novel viewpoints randomly, while Dropout-based regularization randomly removes Gaussians. The compounded randomness introduces uncertainty and instability, limiting the fidelity of novel view synthesis. In this paper, we propose a novel method for sparse-view 3DGS that incorporates Fisher Information to quantitatively guide the utilization of geometric priors and regularization. Specifically, our method comprises two key components: (1) Stereo augmentation with Fisher Information. By leveraging Fisher Information, we actively select most informative supporting views and use depth priors to curate reliable pseudo ground truths, which reduces randomness in augmentation and improves stability and rendering fidelity; (2) Uncertainty-aware regularization. We reduce the instability of Dropout-based regularization by using Fisher Information to quantitatively measure the uncertainty of each 3D Gaussian, and adaptively adjust the removal probability, leading to more stable and effective regularization. With these two components, our method effectively mitigates overfitting and improves the stability of optimization in sparse-view 3DGS, resulting in superior rendering fidelity. Extensive experiments show that our method achieves state-of-the-art performance in sparse-view novel view synthesis benchmarks.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (4) · <a href="topics/rendering.md">full list →</a></summary>

- **[Learning Stable Canonical Worlds for Novel View Synthesis and Beyond](https://arxiv.org/abs/2606.23027)**  
  *Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23027) · [pdf](https://arxiv.org/pdf/2606.23027.pdf)
  > 💡 前馈高斯泼溅在视图增多时易积累噪声，通过不确定性感知融合构建规范潜在世界，新视图合成PSNR提升2.5dB，语义分割准确率提升11%。

  <details><summary>Abstract</summary>

  Feed-forward Gaussian splatting (FFGS) facilitates real-time novel view synthesis, yet current methods often remain tied to view-dependent predictions. As more input views are added, they may accumulate noisy or redundant evidence instead of converging to a stable scene representation. In this paper, we introduce CanonicalGS, a feed-forward pipeline that maps cluttered multi-view observations into a stable, scene-centric representation. CanonicalGS first extracts view-centric evidence from depth, semantic features, and uncertainty estimates, and then aggregates this evidence in a canonical latent world using uncertainty-aware fusion. By emphasizing reliable observations while suppressing uncertain or redundant ones, CanonicalGS produces representations that scale more effectively for novel view synthesis and transfer to downstream visual perception tasks. Experiments show up to a $2.5$ dB improvement in peak signal-to-noise ratio for synthesizing novel views and an $11\%$ gain in semantic segmentation accuracy.

  </details>


- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898)**  
  *Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu*  
  `2026-06-20` · `cs.GR` · [abs](https://arxiv.org/abs/2606.21898) · [pdf](https://arxiv.org/pdf/2606.21898.pdf)
  > 💡 针对网格转3DGS问题，提出基于全光采样理论的白盒框架，通过最小采样率推导和反照率-着色分解更新实现奈奎斯特级全局光照渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a promising method for high-quality, real-time 3D reconstruction. To associate 3DGS with mesh representations, existing methods primarily focus on 3DGS-to-mesh reconstruction from multi-view images. In contrast, the problem of converting a mesh into 3DGS has received comparatively less attention. Instead of relying on heuristic strategies that bind 3D Gaussians to the mesh, we propose a novel white-box 3DGS construction framework, termed Mesh2GS, which generates 3DGS directly from mesh geometry based on plenoptic sampling theory, achieving Nyquist-level performance for high-quality global illumination rendering. Firstly, we propose a plenoptic sampling guided 3DGS construction strategy that theoretically derives the minimum sampling rate of the sampled views and the distribution of 3D Gaussians. Second, we propose a novel 3DGS update procedure with albedo--shading decomposition for efficient global-illumination capture. Finally, we introduce a neural illumination enhancement module to handle non-Lambertian effects. Experimental results demonstrate that our method surpasses state-of-the-art baselines and is practically effective for both real-time shared rendering and non-Lambertian effects capturing specular highlights. The project code will be released upon acceptance.

  </details>


- **[Single-Event Upsets in 3D Gaussian Splatting Rendering: Bit-Level Criticality, Spatial Extent, and a Parallel Support Guard](https://arxiv.org/abs/2606.21791)**  
  *Faruk Alpay, Baris Basaran*  
  `2026-06-19` · `cs.GR` · [abs](https://arxiv.org/abs/2606.21791) · [pdf](https://arxiv.org/pdf/2606.21791.pdf)
  > 💡 分析3DGS渲染中单比特翻转的位

  <details><summary>Abstract</summary>

  Three-dimensional Gaussian splatting is a standard real-time scene representation increasingly deployed on hardware exposed to transient faults, such as spaceborne processors and robotic edge devices where silent data corruption occurs. A trained model is a large array of floating-point parameters in GPU memory, where a single-event upset corresponds to a single flipped bit. This paper measures these effects and constructs a defense. A GPU-resident parallel fault-injection engine applies over 3.8 million controlled single-bit upsets across four scenes, six fields, all bit positions, and three numeric formats (fp32, fp16, bf16), using 5.3 GPU-hours. The effect is highly concentrated: most upsets leave the image perceptually unchanged due to high redundancy, but a small set of high-order bits principally the logarithmic scale's sign bit enlarge a single primitive to cover up to 75.7% of the frame. A closed-form perturbation bound derived from the IEEE-754 layout and pipeline activations predicts this per-bit ordering. This concentration motivates a support guard: a per-primitive clamp of each parameter to the coordinate box observed during training, costing 76 us per frame. Over 768,000 guarded upsets, the worst corruption footprint is restricted to 11.68% of the frame. We prove the guard leaves clean models unchanged and prevents frame-covering corruption. Under an accumulated dose of 20,000 simultaneous upsets, the unguarded renderer degrades to 10.6 dB, whereas the guarded renderer remains at 21.8 dB. The corruption footprint also dictates the number of tile/compositing nodes contaminated in distributed renderers, where the per-node guard contains it.

  </details>


- **[Spectral GS-SLAM: Observability-Aware, Degeneracy-Robust Tracking for Real-Time 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2606.21258)**  
  *Edward Beng Wai Tan, Siew-Kei Lam, Dongshuo Zhang*  
  `2026-06-19` · `cs.RO` · [abs](https://arxiv.org/abs/2606.21258) · [pdf](https://arxiv.org/pdf/2606.21258.pdf)
  > 💡 针对纹理缺失或几何退化场景中跟踪易失效问题，提出结合ICP与特征约束并引入高斯感知平面性加权的实时鲁棒SLAM方法。

  <details><summary>Abstract</summary>

  Recent 3DGS-SLAM systems enable real-time operation by leveraging conventional feature matching or ICP-based tracking, thereby avoiding the heavy dense photometric optimization used in earlier approaches. However, feature matching remains prone to failure in textureless environments, while ICP-based tracking struggles in structureless or geometrically degenerate scenes due to ill-conditioned optimization. To address this issue, we propose Spectral GS-SLAM, an efficient yet robust tracking framework that integrates ICP with complementary feature-based constraints. Our method mitigates numerical instability by adaptively compensating under-constrained directions in degenerate scenarios, without interfering with the shared Gaussian representation used for mapping. We further introduce a Gaussian-aware planarity weighting mechanism that exploits the intrinsic covariance structure of 3D Gaussians to characterize scene geometry and guide information fusion. Extensive evaluations on challenging TUM RGB-D sequences demonstrate that Spectral GS-SLAM achieves real-time performance (40.14 FPS) while maintaining consistent tracking in both structureless and featureless environments. The proposed method preserves trajectory integrity in degenerate scenes while maintaining competitive performance in non-adverse conditions.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (1) · <a href="topics/driving.md">full list →</a></summary>

- **[Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270)**  
  *Yi Wang, Ziyu Zhan, Yuran Wang, Hao Wang, Qiang Liu, Zuoqiang Shi, Lingyun Qiu, Xing Fu*  
  `2026-06-19` · `physics.optics` · [abs](https://arxiv.org/abs/2606.21270) · [pdf](https://arxiv.org/pdf/2606.21270.pdf)
  > 💡 通过3D高斯原语与可微瞬态渲染，解决了非视距成像中任意中继表面几何与稀疏采样下的重建难题。

  <details><summary>Abstract</summary>

  Imaging objects hidden outside the direct line of sight expands the effective field of view and is critical for applications such as autonomous driving and robotic perception. Despite impressive progress in time-of-flight (ToF)-based non-line-of-sight (NLOS) imaging, real-world deployment remains challenging because practical measurements are often collected over spatially limited, arbitrarily shaped relay regions-conditions that violate the planar-wall and dense-sampling assumptions made by most existing methods. To address these limitations, we propose a LOS-guided NLOS imaging pipeline that imposes no geometric assumptions on the relay surface and naturally supports both confocal and non-confocal configurations. Our method represents the hidden scene using 3D Gaussian primitives and couples them with an efficient, differentiable transient rendering model, enabling end-to-end optimization directly from measured transients. We validate our approach on real-world measurements from both a public dataset and a custom-built capture system. Across settings, our method achieves state-of-the-art reconstruction fidelity under spatially limited, sparsely sampled conditions, and significantly outperforms existing methods on complex, arbitrary relay surface geometries.

  </details>


</details>

<details><summary><b>Medical / Surgical</b> (1) · <a href="topics/medical.md">full list →</a></summary>

- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525)**  
  *Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang*  
  `2026-06-21` · `cs.CV` · [abs](https://arxiv.org/abs/2606.22525) · [pdf](https://arxiv.org/pdf/2606.22525.pdf)
  > 💡 稀疏视角CT中投影优化误导体积退化，提出LADES以退火丢弃和早停抑制退化并提升体积保真度。

  <details><summary>Abstract</summary>

  Sparse-view computed tomography is a severely ill-posed inverse problem, where recent 3D Gaussian Splatting methods offer an efficient explicit representation for tomographic reconstruction. However, we find that projection-domain optimization can be misleading in this setting: the rendered projections may continue to improve while the reconstructed volume deteriorates. We identify this failure mode as Projection-Volume Fidelity Divergence (PVFD), a representation-level optimization drift caused by anisotropic Gaussian deformation and view-specific primitive co-adaptation under sparse Radon constraints. To characterize this behavior, we introduce geometry- and volume-level diagnostics that measure needle-like Gaussian degeneration and the stability of the voxelized density field. Based on these observations, we propose LADES, a ground-truth-free optimization controller for sparse-view Gaussian tomography. LADES combines Linearly Annealed Dropout, which applies strong stochastic masking in early training to disrupt premature primitive co-adaptation and gradually restores full capacity for structural consolidation, with Structure-Aware Early Stopping, which terminates densification according to the saturation of Gaussian population growth rather than validation PSNR. Experiments on sparse-view CT reconstruction show that LADES improves volumetric fidelity, suppresses structural degeneration, and substantially reduces training time while maintaining competitive projection accuracy. These results suggest that robust Gaussian-based tomography requires monitoring and controlling volumetric structure, rather than optimizing projection fit alone.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
