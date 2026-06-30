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
| 1 | **Survey & Benchmark** | 73 | **+3** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 260 | **+12** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 37 | **+2** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 57 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 30 | **+2** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 34 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 50 | **+4** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 16 | **+3** | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 17 | **+1** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 6 | **+1** | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 17 | **+1** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 12 | **+3** | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 23 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-30 (UTC) — 34 new paper(s)

<details><summary><b>Survey & Benchmark</b> (3) · <a href="topics/survey.md">full list →</a></summary>

- **[FastPano3D: Feed-Forward Indoor Panoramic 3D Reconstruction from a Single Image](https://arxiv.org/abs/2606.30352)**  
  *Jianqiang Li, Liumei Zhang, Wenjia Guo, Tianlong Feng, Yongzhi Liao, Di Lu, Hanchi Ren, Jingjing Deng*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30352) · [pdf](https://arxiv.org/pdf/2606.30352.pdf)
  > 💡 针对单张全景图快速重建室内3D场景，提出FastPano3D，用轻量编码器与自适应高斯采样直接生成3D高斯，无测试时优化，速度提升156倍。

  <details><summary>Abstract</summary>

  Recent advances in 3D scene reconstruction have highlighted the intricate trade-offs among rendering quality, inference efficiency, and data dependency. To address the challenge of rapidly reconstructing detailed 3D indoor scenes from minimal input, we introduce FastPano3D, an end-to-end framework that directly generates renderable 3D Gaussian representations from a single panoramic image. Unlike perspective-based methods, panoramic images inherently suffer from equirectangular projection distortions and spatially non-uniform feature distributions, making direct feed-forward Gaussian generation particularly challenging. In contrast to existing Gaussian Splatting based methods that rely on multi-view supervision or per-scene optimization, FastPano3D employs a lightweight feature encoder, adaptive Gaussian sampling, and a point-cloud-guided refinement strategy to achieve efficient and accurate scene generation without any test-time optimization. Our approach reconstructs high-fidelity 3D scenes within seconds, achieving up to 156 times faster inference than prior state-of-the-art methods such as Pano2Room, while using only half the parameters. Extensive experiments demonstrate that FastPano3D delivers rendering quality comparable to NeRF- and 3DGS-based reconstructions, establishing a new benchmark for rapid, single-view 3D scene inference.

  </details>


- **[CubifyGS: Object-Centric 3D Gaussian Splatting for Lifelong Dynamic Scene Maintenance](https://arxiv.org/abs/2606.28720)**  
  *Bohan Ren, Dianyi Yang, Shiyang Liu, Yu Gao, Jiadong Tang, Zhilin Lai, Yi Yang, Mengyin Fu*  
  `2026-06-27` · `cs.RO` · [abs](https://arxiv.org/abs/2606.28720) · [pdf](https://arxiv.org/pdf/2606.28720.pdf)
  > 💡 针对刚体重排场景中3DGS重影问题，提出对象级高斯资产管理框架CubifyGS，通过资产检索与事件触发优化实现高效动态维护。

  <details><summary>Abstract</summary>

  Lifelong scene mapping under rigid object rearrangement remains a fundamental challenge in robotics. While 3D Gaussian Splatting (3DGS) enables high-fidelity modeling, primitive-level updates often cause persistent ghosting and slow recovery. We propose CubifyGS, an object-level mapping framework that shifts dynamic maintenance from passive re-optimization to active asset management. CubifyGS models movable instances as reusable Gaussian assets, detects object appearance and disappearance, and updates maps through asset retrieval, rigid transformation, and explicit pruning rather than reconstruction from scratch. To address geometric voids and local photometric mismatch after such edits, we further propose an event-triggered adaptive optimization strategy that focuses computation on affected regions. We validate our approach on a newly constructed high-fidelity dynamic benchmark, demonstrating that CubifyGS improves artifact suppression and maintenance efficiency over representative reproducible baselines in the evaluated object-rearrangement setting.

  </details>


- **[SatSplat: Geometrically-Accurate Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2606.28581)**  
  *Shuang Song, Jiyong Kim, Rongjun Qin*  
  `2026-06-26` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28581) · [pdf](https://arxiv.org/pdf/2606.28581.pdf)
  > 💡 将2DGS适配至卫星摄影测量，引入在线相机调整、阴影映射与颜色校正，实现几何精确重建并降低误差和显存。

  <details><summary>Abstract</summary>

  High-resolution satellite imagery demands 3D reconstruction methods that deliver both speed and geometric accuracy. Recent adaptations of 3D Gaussian Splatting (3DGS) to satellite imagery demonstrate strong efficiency, but reconstruction quality often degrades under diverse illumination across multi-date, high-altitude acquisitions (with small intersection angles), limiting applicability to remote sensing and vision tasks. We present SatSplat, the first framework to adapt 2D Gaussian Splatting (2DGS) to satellite photogrammetry, with online camera adjustment. We approximate satellite cameras with an affine model and learn a minimal delta parameterization for in-splat camera refinement from dense observations. The formulation is implemented with a 2DGS scene representation. To handle time-varying shadows and illumination changes, we integrate geometric shadow mapping and per-camera color correction during training. Across the evaluated DFC2019 and IARPA2016 benchmark sites, SatSplat achieves strong geometric accuracy while significantly outperforming prior 3DGS-based baselines. On our processed DFC2019 benchmark, SatSplat reduces mean absolute error by 11.93% and peak video memory by 31% relative to the previous state of the art. Our approach enables large-scale digital surface modeling with practical computational efficiency. The project page is available at https://gdaosu.github.io/satsplat/.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (12) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Learning Efficient 4D Gaussian Representations from Monocular Videos with Flow Splatting](https://arxiv.org/abs/2606.29976)**  
  *Shengjun Zhang, Jinzhao Li, Xin Fei, Yueqi Duan*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29976) · [pdf](https://arxiv.org/pdf/2606.29976.pdf)
  > 💡 通过流溅射构建速度场监督动态学习，高效从单目视频重建4D高斯场景，实现更快训练与渲染。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from monocular videos is challenging due to scene complexity and temporal dynamics. With the advancement of 3D Gaussian Splatting in novel view synthesis, existing methods extend 3D Gaussians to 4D domain with deformation fields, trajectories or spatiotemporal 4D volumes to model scene element deformation. However, these methods suffer from long training time, low rendering speed or high memory consumption for per-frame reconstruction of 4D volumes, without fully exploiting dense dynamic information. To address this issue, we propose Flow Splatting, which constructs the velocity field and enables the conventional splatting technique to render optical flow from the velocity field to supervise dynamics learning process from monocular videos. Specifically, we extend 4D volumes with time varying means and covariance to represent complex dynamics. Then, we construct and approximate the velocity field naturally based on this representations. While conventional volume rendering techniques support to render color fields, we extend the volume rendering strategy to splat the velocity field by considering the influence of camera motions. We conduct experiments on various benchmarks to demonstrate the efficiency and effectiveness of our method. Compared to the state-of-the-art methods, our model achieves better image quality with less time consumption and higher rendering speed.

  </details>


- **[FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Sparse Portrait Images](https://arxiv.org/abs/2606.30347)**  
  *Jianjiang Yao, Ke Xian, Renxiang Dai, Robert Caiming Qiu*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30347) · [pdf](https://arxiv.org/pdf/2606.30347.pdf)
  > 💡 从单张或多张稀疏肖像图快速重建可驱动4D头部化身，提出Transformer与3D高斯框架，交替注意力解耦身份与表情，稀疏到稠密学习提升质量。

  <details><summary>Abstract</summary>

  We present FFAvatar, a Transformer-based 3D Gaussian framework for fast construction of high-quality and animatable 4D head avatars from one or more reference portrait images. Unlike existing feed-forward approaches that require a fixed number of input views, FFAvatar supports incremental reconstruction, progressively refining the avatar representation as additional reference images become available. At the core of our method is an alternating attention mechanism that disentangles identity appearance from expression and viewpoint variations, enabling the reconstruction of a canonical 3D appearance that remains consistent across poses and facial expressions. To balance visual fidelity and computational efficiency, we introduce a sparse-to-dense learning paradigm. Coarse appearance features are first learned using sparse primitives anchored to the FLAME vertex level and are subsequently densified in the UV domain to capture fine-grained geometric and texture details. We further propose a plug-and-play motion refinement module that enables subject-specific dynamic personalization by modeling residual motion beyond parametric deformation. Extensive experiments demonstrate that FFAvatar efficiently produces high-fidelity and controllable 4D head avatars, achieving superior flexibility, driving efficiency, and identity-consistent rendering across diverse expressions and viewpoints.

  </details>


- **[DR-GS: Physically-Based Deformable and Relightable 2D Gaussians](https://arxiv.org/abs/2606.29379)**  
  *Jiaxin Li, Tong Wu, Yi Wei, Tailin Wu, Li Zhang*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29379) · [pdf](https://arxiv.org/pdf/2606.29379.pdf)
  > 💡 针对可变形物体光照烘焙和材质编辑难问题，提出解耦几何-光照-材质的可变形重光照高斯框架，

  <details><summary>Abstract</summary>

  Gaussian splatting (GS) has garnered significant attention in VR/AR and digital content creation due to its explicit parameterization and efficient rendering capabilities. However, existing GS-based methods for deformable objects face two key limitations: (i) illumination is erroneously baked into textures, causing physically inconsistent responses under dynamic deformations and lighting changes; (ii) snapshot-based reconstruction restricts post-reconstruction material editing. To address these challenges, we propose Deformable and Relightable GS (DR-GS), a unified Gaussian framework that integrates physically-based inverse rendering, relighting, and deformation-aware manipulation. Through explicitly disentangling geometry, illumination, and material representations, DR-GS overcomes the limitations of static snapshots, resolving unrealistic appearance under varying conditions while enabling post-reconstruction parameter editing. Extensive experiments show that DR-GS achieves leading visual quality across static reconstruction, dynamic deformation, and relighting, reliably preserving reflections and specular highlights on glossy surfaces. It further establishes a fully decoupled geometry-illumination-material pipeline, enabling high-quality 3D asset creation and comprehensive post-editing.

  </details>


- **[L2D2-GS: Learning to Densify for Feedforward Dynamic Gaussian Scene Reconstruction](https://arxiv.org/abs/2606.29374)**  
  *Zetian Song, Chenming Wu, Junnan Liu, Chitian Sun, Liangliang He, Hangjun Ye, Jiaqi Zhang, Siwei Ma, Wen Gao*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29374) · [pdf](https://arxiv.org/pdf/2606.29374.pdf)
  > 💡 针对动态城市场景的高保真重建，提出自监督稠密化策略与几何正则化机制，实现高效零样本泛化，减少原语数量。

  <details><summary>Abstract</summary>

  High-fidelity reconstruction of dynamic urban environments is a cornerstone of autonomous driving simulation and large-scale world modeling. While 3D Gaussian Splatting (3DGS) has established a new standard for real-time rendering, its reliance on expensive per-scene optimization limits scalability. Conversely, recent feedforward methods that infer Gaussian parameters offer faster speed but face fundamental bottlenecks: they are memory-prohibitive at high resolutions and struggle to fuse dense multi-view observations consistently. This paper presents L2D2-GS, a unified framework that reformulates generalizable reconstruction not as a one-shot regression, but as a robust iterative process of optimization and densification. To resolve the ambiguity of supervision in primitive generation, we propose a self-supervised densification policy that derives explicit reward signals from global reconstruction gains to guide local densification. Furthermore, we mitigate irreversible early-stage artifacts through a geometric regularization mechanism, utilizing reparameterization to constrain the optimization manifold and prevent convergence to poor local optima. Extensive experiments on the PandaSet and Waymo datasets demonstrate that our method achieves state-of-the-art reconstruction fidelity and strong zero-shot generalization, while using fewer primitives than competing baselines.

  </details>


- **[RAGA: Real Time Ray Traced Gaussian Shadow Casting for 3DGS Avatar-Scene Interaction](https://arxiv.org/abs/2606.29329)**  
  *Aymen Mir, Riza Alp Guler, Jian Wang, Peter Wonka, Bing Zhou, Gerard Pons-Moll*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29329) · [pdf](https://arxiv.org/pdf/2606.29329.pdf)
  > 💡 针对3DGS虚拟角色阴影问题，提出基于光线-高斯线积分的实时阴影投射方法，无需网格重建，支持多人及物体交互场景。

  <details><summary>Abstract</summary>

  We study the problem of physically plausible shadow casting when animating 3D Gaussian Splatting (3DGS) avatars, either individually or in multi-avatar and object-interaction scenarios, within existing 3DGS scenes. In contrast to prior methods that rely on binary hit tests and mesh-based shadow casters, our method performs shadow computation entirely in Gaussian space, without requiring any mesh reconstruction. We introduce RAGA, a Ray-Traced Gaussian Shadow Casting formulation based on exact ray-Gaussian line integrals. For each occluding Gaussian, we integrate the opacity profile along the shadow ray and normalize by the theoretical maximum integral, producing a weight that captures how the ray traverses the occluder rather than merely whether an intersection occurred. To reduce temporal variance from clothing deformations in animated avatars, we further introduce an avatar proxy representation that stabilizes shadow casting while preserving visual fidelity. We implement RAGA using custom CUDA kernels integrated with the NVIDIA OptiX framework; as such, our shadow tracer runs at rates of about 50 FPS. We evaluate on single-avatar, multi-avatar, and avatar-object interaction scenarios across multiple datasets, demonstrating substantially improved shadow realism, temporal stability, and scene coherence. Our project page is available at https://miraymen.github.io/raga/.

  </details>


- **[Occlusion-Robust Multi-Object Decoupling for Physics-Based Interaction](https://arxiv.org/abs/2606.29303)**  
  *Xin Dong, Wenfeng Deng, Yansong Tang*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29303) · [pdf](https://arxiv.org/pdf/2606.29303.pdf)
  > 💡 无掩码多物体重建，利用3DGS和联合SDS解耦遮挡，结合扩散先验与几何先验，实现物理交互。

  <details><summary>Abstract</summary>

  We propose a mask-free method for lossless multi-object 3D reconstruction from sparse and occluded real-world views, enabling physically plausible interaction via Material Point Method (MPM) simulation. Our key insight is that object coupling stems from occlusion and limited viewpoints, which we address by formulating multi-object decoupling as a sparse-view reconstruction problem. Using 3D Gaussian Splatting as base representation, we first obtain coarse instance partitions with a SAM2-trained segmentation field. Rather than relying on masks, we reconstruct fragmented geometries by leveraging a joint Score Distillation Sampling (SDS) process, which integrates reference-view supervision with novel-view synthesis guided by 2D and 3D diffusion priors to enforce both texture fidelity and 3D consistency. Furthermore, we incorporate geometry-aware priors such as intra-object and inter-object similarity to regularize geometric reasoning. Experimental results demonstrate that our method produces complete, simulation-ready 3D objects without requiring manual masks, enabling realistic dynamic interactions on both synthetic and real-world datasets.

  </details>


- **[MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments](https://arxiv.org/abs/2606.29237)**  
  *Qixin Xiao*  
  `2026-06-28` · `cs.RO` · [abs](https://arxiv.org/abs/2606.29237) · [pdf](https://arxiv.org/pdf/2606.29237.pdf)
  > 💡 动态场景下高斯映射易现鬼影，提出运动持续性原则与记忆感知滤波器MoPe，通过历史后验传播与贝叶斯融合提升鲁棒性。

  <details><summary>Abstract</summary>

  Robust robot autonomy depends on scene representations that remain stable enough to support localization, navigation, and downstream decision making in dynamic environments. Monocular Gaussian Splatting SLAM provides high-fidelity mapping, but current uncertainty-aware methods still treat dynamic regions largely as per-frame observations. This makes the representation effectively memoryless: when a pedestrian slows, pauses, or reappears after occlusion, the current frame may look static, allowing dynamic content to be absorbed into the map and leaving persistent ghosting artifacts. We argue that this failure reflects a representation-level mismatch. Dynamic-ness is not an instantaneous appearance property, but a temporal property defined by motion history. Building on this view, we introduce Motion Permanence: the principle that an object's dynamic identity should persist over time rather than be re-decided from each frame independently. We realize this principle in MoPe, a memory-aware uncertainty filter for monocular Gaussian mapping. MoPe propagates the historical dynamic posterior through geometry-consistent SE(3) warping and fuses it with current-frame evidence using bounded Bayesian log-odds updates. The resulting persistent posterior guides tracking, mapping, dynamic-aware Gaussian insertion, and Gaussian-level post-cleanup. On Wild-SLAM, Bonn, and TUM sequences, MoPe improves tracking robustness and reduces residual ghosting, with the strongest gains on dynamic-human scenes that most directly violate the memoryless assumption. These results show that maintaining temporal dynamic state inside the scene representation is a practical step toward more reliable representation-centric autonomy in changing real-world environments.

  </details>


- **[HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video](https://arxiv.org/abs/2606.29333)**  
  *Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29333) · [pdf](https://arxiv.org/pdf/2606.29333.pdf)
  > 💡 提出无标定稀疏视频下2K人体重建方法HiReFF，用尺度同步标定和前景掩码处理模糊性，高分辨率侧调优降低计算开销。

  <details><summary>Abstract</summary>

  Uncalibrated volumetric video streaming for human reconstruction is essential for holographic communication and AR/VR, yet remains challenging due to the need for temporal consistency and computational efficiency from sparse-view inputs. Existing methods rely on per-scene optimization or calibrated cameras, while recent feed-forward models are limited to low-resolution (0.5K) single-frame synthesis. We present HiReFF, a feed-forward method for 2K-resolution 360° human video reconstruction from uncalibrated sparse-view videos. Our framework decomposes the problem into two key tasks: foreground 3D Gaussian reconstruction from sparse-view videos (four views separated by 90°) and computationally efficient high-resolution synthesis. To enable the former, we propose Scale-synchronized Camera Calibration to resolve scale ambiguity for multi-view supervision, and Gaussian-wise Foreground Masking to reconstruct clean foregrounds by modulating Gaussian parameters. For efficient high-resolution synthesis, our High-resolution Side-tuning achieves 2K rendering by augmenting the Gaussian head with supplementary features while keeping the backbone at 0.5K, drastically reducing computational overhead. Experiments demonstrate that HiReFF significantly outperforms existing methods in high-resolution streaming volumetric video reconstruction. https://iridescentjiang.github.io/HiReFF

  </details>


- **[DLGStream: Dynamic Language-embedded Guassian Splatting for Open-vocabulary Enabled Free-viewpoint Video Streaming](https://arxiv.org/abs/2606.28840)**  
  *Zhihui Ke, Yuyang Liu, Xiaobo Zhou, Tie Qiu*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28840) · [pdf](https://arxiv.org/pdf/2606.28840.pdf)
  > 💡 提出双不透明度动态语言高斯表示和插值变形场，实现低帧大小高帧率的开放词汇自由视点视频流。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting~(3DGS) has emerged as a promising paradigm for reconstructing streamable free-viewpoint video~(FVV) from multi-view videos. However, 3DGS-based FVVs typically lack user interaction and editing capabilities, which diminishes the immersive experience. Recent research has integrated language features from CLIP into 3DGS via distillation, enabling open-vocabulary queries and supporting many downstream applications. Nevertheless, the stringent requirements of FVV, low frame size and high FPS, make current language Gaussian representations unsuitable for language-embedded FVV. In this paper, we propose DLGStream, a novel language-embedded FVV representation that streams time-varying language features alongside Gaussian attributes to support 4D environment interaction, scene editing, and spatial intelligence. Specifically, we propose a dual-opacity dynamic language Gaussian representation, which maintains two opacity attributes for color and language features to deal with performance degradation that occurs when colors and features are jointly optimized. Furthermore, we introduce an interpolation-based deformation field to reduce temporal redundancy. This deformation field can also be used for 4D frame interpolation, boosting FVV sequences from low to high FPS. Experimental results demonstrate that DLGStream achieves superior performance in both on open-vocabulary segmentation and reconstruction quality with an average frame size of merely 43 KB. The code is available on \href{https://github.com/kkkzh/DLGStream}{https://github.com/kkkzh/DLGStream}.

  </details>


- **[Ground4D: Consistency-Aware 4D Reconstruction from Monocular Video](https://arxiv.org/abs/2606.28828)**  
  *Qing Zhao, Weijian Deng, Pengxu Wei, Liang Lin*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28828) · [pdf](https://arxiv.org/pdf/2606.28828.pdf)
  > 💡 用3D基础模型初始化几何，结合动态高斯泼溅进行几何一致性优化，实现单目视频的高保真4D重建与渲染。

  <details><summary>Abstract</summary>

  Learning a 4D scene representation from a single monocular video that supports dynamic novel-view synthesis while maintaining faithful geometry over time remains challenging. Dynamic Gaussian Splatting achieves strong rendering performance through photometric optimization, yet does not explicitly enforce multi-view geometric consistency. In contrast, 3D foundation models recover coherent scene geometry and camera motion, but their point-based outputs are not designed for photorealistic rendering. We propose Ground4D, a geometry-grounded framework built on two stages. First, we perform geometry initialization via 3D foundation models, leveraging VGGT in a training-free manner to reconstruct multi-view-consistent 3D geometry and camera poses from monocular video. The recovered geometry provides a structured and reliable initialization for dynamic Gaussian representations. Second, we conduct geometry-consistency-aware refinement via dynamic Gaussian Splatting, optimizing the representation through differentiable rendering while maintaining multi-view geometric consistency across both observed and synthesized viewpoints. Furthermore, Ground4D inherently models the continuous 4D dynamics of the scene, naturally supporting rendering at arbitrary timestamps. By integrating foundation-level geometric priors into dynamic Gaussian optimization, Ground4D achieves stronger reconstruction fidelity and rendering performance, underscoring the role of geometry-grounded constraints in robust 4D scene modeling.

  </details>


- **[CoGS: Compositional Dynamic Human-Object Scenes Gaussian Splatting from Monocular Video](https://arxiv.org/abs/2606.28820)**  
  *Jerrin Bright, John Zelek*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28820) · [pdf](https://arxiv.org/pdf/2606.28820.pdf)
  > 💡 用组合高斯泼溅分解单目视频中人、物、背景，经六阶段优化提升动态交互场景重建质量。

  <details><summary>Abstract</summary>

  Reconstructing dynamic human--object interaction scenes from monocular video is difficult because the human, manipulated object, and background obey different motion models while sharing the same pixels. Existing dynamic radiance-field and Gaussian-splatting methods often entangle these components, causing object motion to leak into the human or static scene, and monocular human reconstruction remains underconstrained in regions that are rarely observed. We present CoGS, a compositional Gaussian-splatting framework for monocular human--object scene reconstruction. CoGS decomposes the video into three coordinated branches: an articulated human initialized from a complete canonical prior, a rigid object field driven by an estimated object trajectory, and a static scene field regularized by weak scene-only planar primitives when available. A six-stage optimization schedule first stabilizes the human and object independently, then fuses them with the scene under full-image supervision, visibility-aware human anchoring, object silhouette and motion constraints, and delayed scene regularization. This design keeps each component responsible for its own geometry and motion while allowing photometric evidence to correct the final composite. Experiments on HOSNeRF and NeuMan show that CoGS improves both human--object interaction reconstruction and in-the-wild human--scene rendering, achieving stronger fidelity and perceptual quality across full-frame and human-focused evaluations. Code will be released upon publication.

  </details>


- **[SemDynReg: Semantics-Guided Deformation Regularization for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.28656)**  
  *Ruitao Chen, Mozhang Guo, Jinge Li*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28656) · [pdf](https://arxiv.org/pdf/2606.28656.pdf)
  > 💡 利用SAM提取语义引导对象级变形正则化，解决动态3DGS中对象变形不一致问题，提升渲染质量。

  <details><summary>Abstract</summary>

  Deformable 3D Gaussian Splatting (3DGS) has emerged as an efficient approach for rendering dynamic scenes in a wide range of 3D applications. However, existing deformation field-based approaches largely lack explicit object-level modeling, often resulting in inconsistent Gaussian deformations within individual objects and unwanted coupling between different objects. To address this limitation, we introduce a semantics-guided framework that enforces dynamic regularization at the object level, aiming to achieve spatially consistent object-wise deformation. Specifically, we first extract segmentation masks using the Segment Anything Model (SAM) and derive semantic features from input images. An object-ID map is then constructed via feature relevance matching with a predefined object dictionary. Guided by this object-ID map, we identify the pixel-wise top-k contributing Gaussians for each object and impose consistency regularization on their deformation parameters, including position, scale, and rotation. Unlike prior methods that learn deformation fields without explicit object-level constraints, our approach incorporates semantic cues to guide deformation behavior at the object level. Experimental results demonstrate that our semantics-aware regularization improves object-level deformation consistency and outperforms baseline methods in rendering quality, achieving higher PSNR and SSIM and lower LPIPS in dynamic 3DGS rendering. Our project page is available at https://dyn-reg-3dgs.github.io/.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (2) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645)**  
  *Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu*  
  `2026-06-29` · `cs.RO` · [abs](https://arxiv.org/abs/2606.30645) · [pdf](https://arxiv.org/pdf/2606.30645.pdf)
  > 💡 利用3DGS重建场景合成视觉-语言-运动学数据，训练人形机器人全身操作策略，实现仿真到真实迁移。

  <details><summary>Abstract</summary>

  Perception-based humanoid loco-manipulation requires connecting egocentric observations and task instructions to whole-body motion. Learning this mapping requires synchronized egocentric images, language commands, and robot-compatible kinematic trajectories, yet no existing data source provides this complete tuple at scale. We address this bottleneck by generating vision-language-kinematics (VLK) supervision synthetically in reconstructed scenes. Our pipeline leverages 3D Gaussian Splatting to reconstruct metric-scale indoor environments, synthesizes navigation and object-interaction trajectories using privileged scene information, and renders paired egocentric observations after the fact. We produce 48,000 paired trajectories with no human intervention and train a VLK policy that predicts short-horizon whole-body kinematic trajectories. A whole-body tracker converts these predictions into actions on the physical humanoid. We evaluate on the physical Unitree G1 performing navigation and single-object transport, demonstrating that synthesized interactions in reconstructed scenes provide effective supervision for sim-to-real perception-based humanoid loco-manipulation. Project Website: https://vision-language-kinematics.github.io/

  </details>


- **[FalconTrack: Photorealistic Auto-Labeled Perception and Physics-Aware Vision-Based Aerial Tracking](https://arxiv.org/abs/2606.29783)**  
  *Yan Miao, Karteek Gandiboyina, Noah Giles, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Sayan Mitra*  
  `2026-06-29` · `cs.RO` · [abs](https://arxiv.org/abs/2606.29783) · [pdf](https://arxiv.org/pdf/2606.29783.pdf)
  > 💡 针对视觉跟踪中手动标注耗时问题，提出FalconTrack，利用高斯溅射模拟器自动生成标签，结合多感知头和物理感知EKF跟踪，实现零样本仿真到现实高成功率迁移。

  <details><summary>Abstract</summary>

  Vision-based aerial tracking is critical in GPS-denied environments. Reliable perception for tracking depends on large-scale labeled data, yet most photorealistic datasets rely on heavy manual annotation and are time-consuming to produce. We present FalconTrack, a unified perception-and-tracking framework that (i) leverages a photorealistic editable simulator for automated label generation and (ii) combines multi-head perception with physics-aware tracking for zero-shot sim-to-real transfer. FalconTrack provides an automated labeling pipeline in a Gaussian Splatting simulator that isolates target Gaussians from short object videos and composites them with randomized backgrounds to generate RGB, mask, class, and 6-DoF pose labels, producing about 10k labeled images in under 20 minutes. Using this dataset, we train a multi-head perception module with staged learning and reprojection consistency, and fuse its outputs with class-conditioned dynamics priors in an EKF for tracking. Our perception model outperforms two baselines and reaches 96-100% class accuracy in zero-shot sim-to-real transfer on three geometrically diverse objects and two environments, while maintaining consistent performance in unseen simulated and real scenes. In real hardware closed-loop visual tracking, the onboard system runs at about 25 Hz and achieves 100% success in sim-to-real F1-tenth and gate tracking in five trajectories across two environments, while a mask-centered vision baseline drops to 60% success on F1-tenth during fast out-of-view scenarios.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[IBRSteG: Learning a Generalizable Steganography Framework for 3D Gaussian Splatting](https://arxiv.org/abs/2606.30024)**  
  *Fanye Kong, Hongyu Xia, Yu Zheng, Boyang Gong, Jie Zhou, Jiwen Lu*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30024) · [pdf](https://arxiv.org/pdf/2606.30024.pdf)
  > 💡 针对3DGS隐写难以泛化问题，提出IBRSteG框架，利用GAS网络学习场景无关的嵌入函数，实现高容量、安全的隐写且无需逐场景微调。

  <details><summary>Abstract</summary>

  Recent advances in deep learning have notably improved steganographic message hiding. However, designing a generalizable steganographic approach for 3D Gaussian Splatting (3DGS) that can embed meaningful 3D scene content remains challenging. In this paper, we propose IBRSteG, a generalizable framework for 3DGS steganography that enables undetectable concealment of secret scenes within a steganographic scene. Unlike existing approaches whose parameter generation is rigidly coupled with the specific scene, we formulate 3D steganography as a feed-forward 3D Gaussian embedding process that generalizes across different 3DGS scenes. To realize this, we introduce GAS (Gaussian Attributes Steganographer), a network that learns a scene-independent embedding function by injecting the attributes of secret 3D Gaussian points into a cover scene, thereby directly reconstructing the steganographic scenes without per-scene finetuning or optimization. By transforming 3D Gaussian into these structured attributes, these attributes are compatible with 2D learning paradigms and benefit from their structured nature, thereby enhancing generalization to unseen 3DGS scenes. Extensive experiments on established datasets demonstrate that IBRSteG can effectively conceal different scenes with high visual quality, and achieves superior capacity and security. Code is available at https://github.com/LingXiang2023/IBRSteG.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (2) · <a href="topics/editing.md">full list →</a></summary>

- **[Monte Carlo Energy Aggregation for Mobile 3D Gaussian Splatting](https://arxiv.org/abs/2606.30017)**  
  *Xiaobiao Du, YuAn Wang, Hao Li, Bosheng Wang, Xun Sun, Xin Yu*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30017) · [pdf](https://arxiv.org/pdf/2606.30017.pdf)
  > 💡 针对移动端3DGS高开销问题，提出Flux-GS，用蒙特卡洛能量聚合与属性增强模块减少参数，保持多视角一致与高效渲染。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting have demonstrated unprecedented success in novel view synthesis. However, the substantial inference and storage overhead driven by high-order Spherical Harmonics (SH) are primary bottlenecks for mobile platforms. In this paper, we present Flux-GS, a real-time Gaussian Splatting method designed to achieve high-fidelity rendering with significantly reduced overhead for resource-constrained mobile platforms. We first propose a Monte Carlo Specular Energy Aggregator, sampling third-order radiance residuals and aggregating specular energy into a compact latent space. In this way, our method effectively preserves visually salient lighting features in lower-order bands without expensive distillation or pre-training. To mitigate the high-frequency details lost during compression, we introduce an Attribute-Conditioned SH Enhancement module. This module predicts Gaussian-aware offsets based on intrinsic Gaussian attributes, which enhance the first-order SH representation prior to inference, without extra inference costs. Furthermore, the original single-view gradient-based densification is prone to producing excessive Gaussians and overfitting to a certain view. We address these limitations by proposing a Multi-view Alpha-based Densification and Pruning strategy. By leveraging multi-view guidance, we ensure multi-view structure consistency and the precise removal of redundant primitives. Extensive experiments demonstrate that Flux-GS achieves substantial parameter reduction while maintaining competitive visual quality, offering a robust and scalable solution for real-time mobile rendering. Code: \textcolor{magenta}{\href{https://xiaobiaodu.github.io/flux-gs-project/}{https://xiaobiaodu.github.io/flux-gs-project/}}.

  </details>


- **[Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views](https://arxiv.org/abs/2606.29513)**  
  *Mijin Yoo, In Cho, Subin Jeon, Jiwoo Lee, Eunbyung Park, Seon Joo Kim*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29513) · [pdf](https://arxiv.org/pdf/2606.29513.pdf)
  > 💡 提出从无位姿多视图图像分解场景为实例结构化3D token组的前馈框架，无需3D标注即可实现重建、分割与编辑，性能优于逐场景优化基线。

  <details><summary>Abstract</summary>

  A 3D scene is understood through its objects, not the primitives that compose them. Yet feed-forward reconstruction methods output dense, unstructured sets of points or Gaussians, leaving object-level structure to be recovered after the fact. We propose a feed-forward framework that decomposes a scene into instance-structured 3D token groups directly from unposed multi-view images -- compact object-centric units from which reconstruction, segmentation, and manipulation all follow. Each token group pairs an instance token capturing entity-level identity with anchor tokens that encode local geometry and appearance, which are decoded into a set of 3D Gaussians. This two-level factorization decouples object identity from local appearance, making object instances a native interface of the representation rather than a derived product. The token groups are learned through differentiable rendering with joint reconstruction and segmentation supervision, requiring no 3D annotations. Our feed-forward model surpasses per-scene optimization baselines in class-agnostic instance segmentation while remaining competitive in novel view synthesis. Beyond these metrics, the same token groups directly unlock instance-level scene editing -- removing, translating, or inserting objects by operating on their groups -- as well as efficient open-vocabulary 3D instance retrieval, where retrieval complexity scales with the number of instances rather than primitives.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436)**  
  *Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30436) · [pdf](https://arxiv.org/pdf/2606.30436.pdf)
  > 💡 通过运动自适应混合跟踪和生命周期管理高斯映射，解决千米级室外场景中单目3DGS SLAM的长期跟踪漂移和内存爆炸问题。

  <details><summary>Abstract</summary>

  Scaling monocular 3D Gaussian Splatting (3DGS) SLAM to kilometer-level outdoor environments poses two tightly coupled challenges: fragile long-term pose tracking and excessive memory overhead during large-scale mapping. In this paper, we propose KiloGS-SLAM, a highly efficient and robust monocular 3DGS-SLAM system that jointly addresses both bottlenecks. Since high-fidelity scene reconstruction fundamentally relies on drift-free camera poses, we first introduce a motion-adaptive hybrid tracking module. This module features a condition-triggered three-tier solving pipeline. It dynamically switches between Essential matrix and PnP models to handle geometric degeneracies. An on-demand foundation model can also be activated to rescue the trajectory from catastrophic drift. To ensure the system can sustain these long trajectories without memory exhaustion, we subsequently design a lifecycle-managed Gaussian mapping strategy. By integrating probabilistic initialization with chunk-based multi-view densification and pruning, this full-pipeline optimization effectively reduces primitive redundancy while preserving high-frequency details. Together, the robust tracking guarantees the geometric foundation required for accurate mapping, while the memory-efficient lifecycle-managed mapping enables large-scale operation. Extensive experiments across three challenging outdoor datasets demonstrate that our approach achieves state-of-the-art tracking accuracy and rendering quality, successfully scaling to sequences of over 10,000 frames on a single GPU.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (4) · <a href="topics/rendering.md">full list →</a></summary>

- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545)**  
  *Wenhao Yuan, Yiyuan Ge, Deli Cai*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30545) · [pdf](https://arxiv.org/pdf/2606.30545.pdf)
  > 💡 针对稀疏视图下3DGS过拟合与几何缺陷，引入立体先

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has achieved remarkable success in real-time novel view synthesis, yet it suffers from severe overfitting under sparse-view settings due to insufficient geometric constraints. While recent methods introduce monocular depth priors to mitigate this, they inherently struggle with scale ambiguity and cross-view inconsistency, leading to defective geometry. In this paper, we propose StereoGS, a novel sparse-view 3DGS framework that integrates stereo priors to establish reliable binocular consistency. Unlike scale-agnostic monocular constraints, StereoGS introduces a Stereo Depth Regularization by constructing virtual stereo pairs during optimization and leveraging a foundation stereo model to enforce absolute scale and binocular-consistent structures. To further suppress overfitting and eliminate redundant primitives, we design a Gradient-Aware Opacity Decay strategy that dynamically penalizes Gaussians based on their relative opacity gradient magnitudes. Combined with a Consistency-Aware Dense Initialization using zero-shot multi-view depth estimation, StereoGS effectively anchors primitives to accurate scene surfaces. Extensive experiments on LLFF, DTU, Mip-NeRF360, and Blender datasets demonstrate that StereoGS achieves state-of-the-art performance in sparse-view settings without incurring any additional inference overhead. Project Page: https://stringerywh00.github.io/StereoGS_project_page/

  </details>


- **[UniTriSplat: A Unified 3D Gaussian Splatting Framework with Uniform Spherical Rasterization for Universal Cameras](https://arxiv.org/abs/2606.29794)**  
  *Yipeng Zhu, Huajian Huang, Tristan Braud, Sai-Kit Yeung*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29794) · [pdf](https://arxiv.org/pdf/2606.29794.pdf)
  > 💡 针对不同相机模型采样不一致问题，提出基于HEALPix球面均匀光栅化的统一3DGS框架，提升跨相机泛化与重建质量。

  <details><summary>Abstract</summary>

  Existing 3D Gaussian Splatting (3DGS) frameworks rely on camera-specific rasterization, suffering from inconsistent solid-angle sampling and degraded performance across heterogeneous camera models (e.g., perspective, fisheye, omnidirectional). To address this limitation, we propose UniTriSplat, a unified 3DGS framework for universal cameras that reformulates Gaussian splatting on the unit sphere via HEALPix discretization. Leveraging the equal-area property of HEALPix, we construct a spherical sampling grid aligned with the angular resolution of input images. We derive the forward rendering and gradient propagation of Gaussians directly in the spherical radian domain, yielding uniform optimization behavior from narrow-FoV images to full 360-degree panoramas. To enhance perceptual reconstruction quality, we additionally introduce a HEALPix-aware SSIM loss that respects spherical neighborhood structure. Extensive experiments across diverse camera models demonstrate that UniTriSplat consistently improves cross-camera generalization while preserving geometric fidelity and rendering quality.

  </details>


- **[MyGO-Splat: Multi-Objective Closed-Loop Geometric Feedback for RGB-Only Gaussian SLAM](https://arxiv.org/abs/2606.29738)**  
  *Fan Zhu, Ziyu Chen, Zhenjun Zhao, Zhisong Xu, Hui Zhu, Mingrui Li, Chunmao Jiang, Javier Civera*  
  `2026-06-29` · `cs.RO` · [abs](https://arxiv.org/abs/2606.29738) · [pdf](https://arxiv.org/pdf/2606.29738.pdf)
  > 💡 单目SLAM尺度模糊且缺少几何自校正，MyGO-Splat通过闭环Gaussian光栅化深度与法线及尺度自适应对齐，提升尺度稳定性，性能媲美RGB-D。

  <details><summary>Abstract</summary>

  Real-time monocular Simultaneous Localization and Mapping (SLAM) fundamentally suffers from scale ambiguity and a lack of geometric self-correction. While 3D Gaussian Splatting (3DGS) enables high-fidelity rendering, existing RGB-only systems remain open-loop because depth priors are injected into mapping but refined geometry cannot effectively regulate tracking drift. We present MyGO-Splat, a closed-loop Gaussian SLAM framework that analytically rasterizes Gaussian primitives into pixel-wise depth and surface normals, allowing the map to actively supervise camera pose optimization. To bridge monocular priors and scale consistency, our framework introduces scale-aware adaptive alignment that projects foundation-model depth estimates into the globally optimized Gaussian space, forming a self-correcting cycle for scale feedback. Extensive evaluations show that this closed-loop design improves scale stability and appearance-geometry consistency, achieving performance comparable to RGB-D methods while using only monocular input.

  </details>


- **[Resonant Brane Splatting for Arbitrary-Scale Super-Resolution](https://arxiv.org/abs/2606.29453)**  
  *Giulio Federico, Giuseppe Amato, Claudio Gennaro, Fabio Carrara, Marco Di Benedetto*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29453) · [pdf](https://arxiv.org/pdf/2606.29453.pdf)
  > 💡 针对高斯平滑导致的稀疏性问题，RBS引入带高斯-埃尔

  <details><summary>Abstract</summary>

  Arbitrary-Scale Super-Resolution (ASR) reconstructs images at continuous magnification factors. Recent methods accelerate inference by replacing computationally heavy implicit neural decoders with explicit 2D Gaussian Splatting (GS). However, since standard Gaussians are smooth low-pass primitives, modeling edges and fine textures requires multiple overlapping, well-aligned splats, which creates severe bottlenecks during rasterization. To address this, we introduce Resonant Brane Splatting (RBS), a feed-forward ASR framework. RBS replaces flat Gaussians with Branes: expressive primitives that emit spatially varying colors to natively model local contrast and complex textures within a single footprint. We achieve this by augmenting the standard Gaussian envelope with internal Gaussian-Hermite modes, assigning a distinct color coefficient to each. The zero-order mode recovers standard GS, while higher-order modes capture high frequencies. We predict Brane parameters directly from low-resolution features. Because Branes provide a mathematically richer formulation than simple Gaussians, far fewer primitives need to overlap to reconstruct a given target pixel. To exploit this, we introduce an efficient fully differentiable rasterizer with a precise culling strategy based on the classical quantum turning point. This allows us to safely skip negligible regions, drastically reducing the rendering overhead. Experiments on standard ASR benchmarks show that RBS improves reconstruction quality over implicit and GS baselines, while achieving superior speed-quality trade-off than prior GS methods.

  </details>


</details>

<details><summary><b>SLAM / Localization / Mapping</b> (3) · <a href="topics/slam.md">full list →</a></summary>

- **[Graph-GSReg: Leveraging 3D Scene Graphs for Gaussian Splatting Registration](https://arxiv.org/abs/2606.29782)**  
  *Jaewon Lee, Mangyu Kong, Euntai Kim*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29782) · [pdf](https://arxiv.org/pdf/2606.29782.pdf)
  > 💡 用3D场景图将3DGS配准转化为图注册问题，并自监督优化融合质量，实现准确注册与无缝场景。

  <details><summary>Abstract</summary>

  Merging multiple 3D Gaussian Splatting (3DGS) scenes into a single unified Gaussian representation is essential for large-scale 3D mapping and long-term map management. Despite its importance, this area remains underexplored, and existing solutions exhibit several limitations. Learning-based methods attempt direct correspondence between Gaussian primitives and require training on large 3DGS datasets. Image-based optimization methods depend heavily on coarse initialization from generic foundation models and often incur expensive refinement. We present \ourmodel. Our method constructs a 3D scene graph from a 3DGS and its rendered images, \textit{reformulating 3DGS registration as a graph registration problem}. The proposed 3D scene graph represents each 3DGS at a higher-level representation, enabling a globally consistent understanding of semantic information and structural context for accurate registration. To further construct a seamless unified scene, we introduce a Self-Supervised Test-Time Optimization. Naively merging two 3D Gaussian scenes often suffers from occlusion artifacts such as hollows and floaters. To alleviate this issue, we refine the merged Gaussians to preserve visual consistency between the original scenes and the merged scene. We evaluate our method on real and synthetic benchmarks, demonstrating competitive registration accuracy and merged scene rendering quality.

  </details>


- **[VCS-SLAM: Geometry-Validated Semantic Evidence Fusion for 3D Gaussian SLAM](https://arxiv.org/abs/2606.29494)**  
  *Raman Jha, Shuaihang Yuan, Yi Fang*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29494) · [pdf](https://arxiv.org/pdf/2606.29494.pdf)
  > 💡 通过几何验证的语义可靠性评估，抑制遮挡与模糊区域的伪影，提升3D高斯SLAM的一致性与重建质量。

  <details><summary>Abstract</summary>

  Visual SLAM performance often deteriorates in complex real-world applications. Semantic 3D Gaussian SLAM commonly fuses 2D semantic priors into a persistent 3D map using uniform optimization weights. However, such priors are not equally reliable in online mapping: occlusions, unsupported semantic boundaries, and ambiguous ray geometry can introduce persistent semantic artifacts into the global Gaussian map. We propose VCS-SLAM, a geometry-validated semantic evidence fusion framework for RGB-D 3D Gaussian SLAM. Instead of treating all semantic observations as uniformly valid supervision, VCS-SLAM evaluates their geometric reliability through visibility consistency, surface-supported boundary evidence, and ray-level conflict uncertainty. The resulting reliability-aware objective suppresses occluded semantic updates, reduces unsupported semantic bleeding, and delays premature label assignment in ambiguous regions. Experiments on Replica demonstrate improved semantic consistency, boundary preservation, and reconstruction quality. Results on ScanNet further show that VCS-SLAM maintains competitive tracking performance under real RGB-D inputs

  </details>


- **[Articulating then Matching: Zero-Shot Shape Matching for Uncurated Data](https://arxiv.org/abs/2606.29167)**  
  *Qilong Liu, Qinfeng Xiao, Chenyuan Yi, Liying Zhang, Kit-lun Yick*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29167) · [pdf](https://arxiv.org/pdf/2606.29167.pdf)
  > 💡 通过预训练视觉模型估计参数化形状再匹配，零样本解决未整理数据的密集对应，鲁棒处理拓扑噪声和多模态。

  <details><summary>Abstract</summary>

  Finding dense correspondences between 3D shapes is a fundamental yet unresolved challenge, especially in real-world environments. These environments present severe challenges, including the lack of time and sufficient samples for training, the prevalence of uncurated extreme-high resolution data with topological distortions, and the need to handle diverse 3D representations. In this paper, we present ATM, a zero-shot framework that requires no correspondence-specific training and robustly addresses these issues at once through an articulate-then-match paradigm. Rather than relying on intrinsic geometric properties, we leverage powerful pretrained vision foundation models and parametric shape priors to estimate parametric shape models from multi-view renderings, and systematically ground these estimations via multi-view geometric consistency. By mapping diverse inputs into a shared canonical parametric space, we inherently establish robust coarse correspondences that bypass topological noise, which are then refined into precise dense mappings via spectral refinement. Operating purely on test-time optimized parametric reconstructions, ATM requires no correspondence training data, is naturally immune to connectivity artifacts, and seamlessly handles diverse 3D modalities, including meshes, point clouds, and 3D Gaussians. Extensive experiments demonstrate that our method achieves strong results on non-isometric benchmarks (average geodesic errors of 2.4-TOPKIDS, 3.8-SMAL), reducing errors by 73% and 37% respectively compared to the baseline URSSM. Furthermore, it exhibits unprecedented robustness on in-the-wild raw scans of up to 200k vertices per shape while maintaining near-constant computation time and consistent superior accuracy.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (1) · <a href="topics/driving.md">full list →</a></summary>

- **[Shell-Supervised Gaussian Splatting for Urban Real-to-Sim Reconstruction](https://arxiv.org/abs/2606.30014)**  
  *Yuan Yang, Peijun Lu, Fangzhou Lu, Sai Fan, Siqi Yan, Chenyuan Zhang, Haobo Liang, Yichen Wang*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30014) · [pdf](https://arxiv.org/pdf/2606.30014.pdf)
  > 💡 针对城市立面几何不稳定问题，提出用外部结构壳监督高斯溅射，改善朝向与表面一致性。

  <details><summary>Abstract</summary>

  Real-to-sim reconstruction for embodied AI requires geometry that is useful for collision reasoning, navigation, and agent-environment interaction, not only photorealistic novel-view synthesis. However, close-range urban facades are difficult for video-to-3D reconstruction: glass, reflections, repeated windows, and weak texture can produce visually plausible renderings with unstable surface geometry. We introduce shell-supervised Gaussian Splatting, a reconstruction-stage framework that uses an external facade structural shell as lightweight geometric supervision for video-driven Gaussian reconstruction. The method aligns an exterior shell to the video reconstruction frame, renders per-view depth, camera-space normal, and valid-mask maps, and applies these cues through mask-gated losses during Gaussian optimization. This design preserves RGB-driven appearance while regularizing only visible shell-supported facade regions. Experiments on anonymized close-range urban facade scenes show improved facade orientation and visible-surface point-cloud consistency over photo-only, monocular-cue, and surface-oriented Gaussian baselines, while maintaining comparable held-out rendering quality.

  </details>


</details>

<details><summary><b>Relighting / Material / BRDF</b> (1) · <a href="topics/relighting.md">full list →</a></summary>

- **[AEGIR: Modeling Area Emitters for Indoor Inverse Rendering using Gaussian Splatting](https://arxiv.org/abs/2606.28635)**  
  *Mohamed Shawky Sabae, Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik Lensch*  
  `2026-06-26` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28635) · [pdf](https://arxiv.org/pdf/2606.28635.pdf)
  > 💡 通过显式建模局部面光源与可微延迟渲染，实现室内场景的精确光照分解和光传输模拟。

  <details><summary>Abstract</summary>

  Inverse rendering requires separating illumination from surface materials, which is highly ambiguous due to their tight coupling in observed images. While Gaussian Splatting is efficient for novel view synthesis, existing relightable methods approximate scene lighting using discrete point lights, global environment maps, or implicit representations. By ignoring the physical spatial extent of real-world emitters, these approaches produce incorrect light attenuation and unrealistic shadows. We present AEGIR (Area Emitters for Gaussian Inverse Rendering), a framework that explicitly models local area emitters within a relightable Gaussian Splatting representation. Joint optimization of emitters, materials, and geometry is challenging due to flexible emitter parameterization, which increases both the number of parameters and the ambiguity between illumination and materials. We address this by introducing a differentiable deferred rendering pipeline that integrates multiple importance sampling with targeted regularization. As a result, AEGIR accurately simulates local light transport and achieves more consistent decomposition. Experiments show that explicit area emitters improve illumination reconstruction and enhance downstream tasks, including novel view synthesis, controlled relighting, and virtual object insertion, particularly in scenes with complex local lighting.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (1) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[Learning to Adaptively Allocate Gaussians for Arbitrary-Scale Image Super-Resolution](https://arxiv.org/abs/2606.29400)**  
  *Giulio Federico, Giuseppe Amato, Claudio Gennaro, Fabio Carrara, Marco Di Benedetto*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29400) · [pdf](https://arxiv.org/pdf/2606.29400.pdf)
  > 💡 通过神经路由动态分配高斯密度和层次指针卷积，实现高效任意尺度图像超分辨率，克服均匀处理冗余并达到SOTA。

  <details><summary>Abstract</summary>

  In computer graphics, visual content is continuously warped, zoomed and resampled. This occurs when engines upscale frames, users zoom into 3D scenes, or foveated VR applies varying scaling. Handling these transformations requires Arbitrary-Scale Super-Resolution (ASR). Traditional models, designed for fixed scales, typically predict at a lower integer scale (e.g., x4) and rely on sub-optimal interpolation for continuous resolutions, compromising quality. Furthermore, most methods process pixels uniformly. Since fine details are sparse, this creates overhead; efficiency dictates concentrating resources only where structural complexity demands it. While implicit models and Gaussian Splatting (GS) enable continuous representation, GS is advantageous due to adaptive densification. However, transitioning GS into a feed-forward model for ASR is non-trivial. Standard GS optimization needs high-resolution gradients to drive primitive growth, which are unavailable during inference. Thus, the network must autonomously predict GS densification from low-resolution inputs. To solve this, we propose QuADA-GS. After encoding inputs into a latent space, a Neural Routing Architecture evaluates local complexity to distribute a global budget, assigning specific upsampling factors to features to avoid redundant processing. Features are dynamically densified based on these factors, forming an irregular topology decoded into 2D Gaussian primitives. To coordinate features before decoding, we introduce Hierarchical Pointer Convolution. This non-grid operator achieves O(1) neighbor lookup complexity, facilitating efficient spatial communication and bypassing dense bottlenecks. Experiments show QuADA-GS achieves state-of-the-art ASR performance, maintaining low latency and a lean memory footprint.

  </details>


</details>

<details><summary><b>Semantic / Scene Understanding</b> (3) · <a href="topics/semantic.md">full list →</a></summary>

- **[Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors](https://arxiv.org/abs/2606.30638)**  
  *Jameel Hassan, Yasiru Ranasinghe, Vishal Patel*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30638) · [pdf](https://arxiv.org/pdf/2606.30638.pdf)
  > 💡 利用离散2D检测器和多视图

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

  </details>


- **[Rectifying Mask via Entropy for Distractor-Free 3DGS in Ambiguous Scenarios](https://arxiv.org/abs/2606.29496)**  
  *Wongi Park, Jiyeon Lim, Minjae Lee, Myeongseok Nam, Seongjun Choi, Jungwoo Kim, Soomok Lee, William J. Beksi, SangHyun Lee*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29496) · [pdf](https://arxiv.org/pdf/2606.29496.pdf)
  > 💡 用熵感知自适应掩膜和密度控制解决颜色或语义模糊场景中的干扰物问题，实现无干扰新视角合成。

  <details><summary>Abstract</summary>

  We present RefineSplat, a systematic framework that effectively constructs transient masks to identify diverse ambiguous distractors. To do this, we qualitatively and quantitatively analyze issues and propose a novel entropy-aware adaptive masking method. Unlike existing approaches that struggle to distinguish transient elements from static scenes due to color or semantic ambiguity, RefineSplat captures ambiguous distractors leveraging entropy and instance masks. Furthermore, we propose a simple yet effective entropy-aware density control to align Gaussians in ambiguous scenarios considering Entropy-aware positional gradients. Additionally, to rigorously validate our method, we first create and release the Ambiguous wild dataset, including 18 scenes where distractors and static scenes are hard to distinguish due to color or semantic resemblances. Experimental results on various datasets demonstrate that RefineSplat shows state-of-the-art performance, showing distractor-free novel view synthesis.

  </details>


- **[RefGlass-GS: A UAV-Enabled Fusion Framework for Photorealistic, Semantic and Interactive Digitization of Reflective Glass Facades via Gaussian Splatting](https://arxiv.org/abs/2606.28826)**  
  *Zhenyu Liang, Xiao Zhang, Boyu Wang, Zhaolun Liang, Ang Li, Jeff Chak Fu Chan, Mingzhu Wang, Jack C. P. Cheng*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28826) · [pdf](https://arxiv.org/pdf/2606.28826.pdf)
  > 💡 针对反光玻璃幕墙数字化难题，提出RefGlass-GS融合框架，通过个体面板分割、视角优化和反射MLP增强高斯泼

  <details><summary>Abstract</summary>

  Existing digitization of buildings with reflective glass facades suffers from geometric reconstruction distortion, unrealistic view-dependent texture rendering, and difficulties in object-based semantic enhancement. Therefore, we propose RefGlass-GS, a fusion framework that enables end-to-end UAV-based photorealistic, semantic, and interactive digitization of reflective glass facades. The contributions include: (1) proposing an individual glass panel segmentation method based on maximum a posteriori estimation with structural regularities, robust to severe reflection and background interference; (2) formulating a UAV viewpoint planning optimization function that maximizes the coverage of view-dependent appearance for sufficient data capture; (3) developing an optimized Gaussian Splatting framework with a Reflection MLP, a novel deferred shading function, and two enhanced regularization terms for effective modeling of high-frequency near-field reflections; (4) introducing a standardized data organization paradigm for structuring GS-based representations into object-based models, facilitating interactive facility management on digital twin platforms. Experiments on real-world reflective glass facade scenes validate the effectiveness and superiority of the proposed method. Specifically, the glass panel segmentation achieves an improvement of 0.1927 in mIoU over SOTA methods, and only our method enables instance-level panel extraction. The UAV view planning improves novel view synthesis for reflective facades by 13.15 dB in PSNR compared to commercially used nap-of-the-object planning methods. The RefGlass-GS modeling outperforms SOTA Gaussian Splatting approaches for reflective scenes with an average improvement of 5.08 dB in PSNR.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
