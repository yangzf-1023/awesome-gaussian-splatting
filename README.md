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
| 1 | **Survey & Benchmark** | 56 | **+6** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 227 | **+10** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 29 | **+4** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 43 | **+3** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 20 | **+1** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 31 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 34 | **+4** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 10 | **+2** | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 12 | **+1** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 2 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 13 | **+2** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 21 | **+1** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-06 (UTC) — 35 new paper(s)

<details><summary><b>Survey & Benchmark</b> (6) · <a href="topics/survey.md">full list →</a></summary>

- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871)**  
  *Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz*  
  `2026-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2606.04871) · [pdf](https://arxiv.org/pdf/2606.04871.pdf)
  > 💡 综述了3D表示从离散显式到连续隐式的演变，侧重神经渲染与高斯泼溅，揭示范式转变。

  <details><summary>Abstract</summary>

  The selection of an appropriate 3D representation is a fundamental design decision that dictates the efficiency, quality, and capabilities of modern computer vision and graphics pipelines for tasks such as 3D reconstruction, novel-view synthesis and rendering, shape and motion analysis, recognition, and generation. While traditional representations (\eg meshes, point clouds, and volumetric grids) remain standard outputs of 3D sensors (\eg LiDAR and 3D scanners) and are widely used in downstream applications (\eg editing and simulation), recent neural and primitive-based representations (\eg 3D Gaussian Splatting) offer compact and differentiable alternatives opening a wide range of opportunities in applications such as games, AR/VR, autonomous driving, robot navigation, and medical imaging, to name a few. The goal of this paper is to survey the main families of 3D representations from discrete explicit formats to continuous implicit fields based either on neural rendering or primitive splatting. For each type of representation, we present the general formulation and its variants, discuss its benefits and limitations, and highlight key applications. We conclude the paper by outlining the open challenges and potential directions for future research. Distinct from recent surveys that broadly cover 3D object and scene reconstruction, this paper provides a focused analysis on the evolution of 3D representations themselves. We specifically emphasize the paradigm shift toward implicit representations, offering a novel perspective on how these emerging formats fundamentally alter 3D/4D workflows.

  </details>


- **[GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation](https://arxiv.org/abs/2606.03682)**  
  *Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li*  
  `2026-06-02` · `cs.RO` · [abs](https://arxiv.org/abs/2606.03682) · [pdf](https://arxiv.org/pdf/2606.03682.pdf)
  > 💡 构建GN-Matrix数据集与3DGS仿真平台，提出RL驱动基础模型BAE，统一地图式与地图-free视觉语言导航任务，超越SOTA。

  <details><summary>Abstract</summary>

  Embodied navigation connects intelligent agents with the physical world and is fundamental for general robotic intelligence. Limited availability and quality of navigation data have constrained Vision-and-Language Navigation (VLN) systems' generalization and long-horizon capabilities. To address this, we curate diverse 3D scenes and develop an automated pipeline for large-scale navigation data, resulting in the GN-Matrix dataset. Building on a 3D Gaussian Splatting (3DGS) engine, we introduce a high-fidelity simulation platform supporting interactive roaming and collision-aware navigation. We further propose GN-Bench, the first BEV-based benchmark incorporating dynamic 3DGS avatars for human-robot interaction evaluation. To leverage the simulator, we develop an RL-driven navigation foundation model, Break and Establish (BAE). After supervised learning, DAgger exposes the model to rollout-induced states, breaking narrow expert-centric distributions and enabling downstream RL exploration. This unified VLN paradigm integrates map-based and map-free tasks, including instruction following, human following, and goal navigation. GN-BAE formalizes high-fidelity 3DGS-rendered Bird's Eye View representations as compact memory, unlocking latent spatial reasoning in VLMs. Extensive evaluations on GN-Bench and VLN-CE show that GN0 outperforms state-of-the-art VLN methods. Overall, GN-Matrix offers a unified framework spanning data, simulation, and learning, advancing embodied navigation in research and industrial applications.

  </details>


- **[Characterizing Detectability in 3DGS Poisoning: A Stage-wise Benchmark](https://arxiv.org/abs/2606.03499)**  
  *Quoc-Anh Bui-Huynh, Thanh Duc Ngo, Xue Geng, Kaixin Xu, Wang Zhe, Xulei Yang, Ngai-Man Cheung*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03499) · [pdf](https://arxiv.org/pdf/2606.03499.pdf)
  > 💡 提出Poison-3DGS基准，系统分析3DGS投毒攻击在不同重建阶段的可检测性，发现检测效果高度依赖阶段信号。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has rapidly emerged as a leading representation for real-time novel view synthesis, but recent work shows it is vulnerable to diverse poisoning attacks, including illusory object injection, computation cost amplification, and post hoc model watermarking. Despite this expanding threat surface, existing studies focus mainly on attack success, while defense and detection remain underexplored. From a detection perspective, a key challenge and opportunity arise from the multi-stage nature of the 3DGS reconstruction pipeline, which produces heterogeneous intermediate representations. Forensic signals for detecting poisoning are inherently stage dependent: an attack introduced at one stage may produce signals that emerge only at later stages. This motivates a stage-wise view of detectability that goes beyond single-stage evaluation. We introduce Poison-3DGS, a benchmark for stage-wise characterization of poisoning detection in 3DGS. It exposes stage-specific artifacts, including multi-view images, geometry, training dynamics, and Gaussian parameters, across a diverse set of scenes and attacks. Using it, we conduct a systematic study of detectability across pipeline stages. Our analysis reveals several insights. First, detectability varies significantly across stages, and no single stage consistently dominates across attack types. Second, different attacks exhibit distinct stage-specific forensic signals, so detection effectiveness depends critically on where signals are observed. Third, later-stage signals such as training dynamics and Gaussian parameter statistics provide strong cues not observable at earlier stages. Overall, our work provides a principled benchmark and the first systematic characterization of stage-dependent detectability in 3DGS, offering a foundation for future research on robust and reliable 3DGS systems.

  </details>


- **[A Cookbook of 3D Vision: Data, Learning Paradigms, and Application](https://arxiv.org/abs/2606.04291)**  
  *Hongyang Du, Zongxia Li, Dawei Liu, Runhao Li, Haoyuan Song, Qingyu Zhang, Yubo Wang, Jingcheng Ni, Shihang Gui, Congchao Dong, Tao Hu*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.04291) · [pdf](https://arxiv.org/pdf/2606.04291.pdf)
  > 💡 提出3D视觉数据驱动分类法，系统梳理点云、3D高斯等表示与学习范式，整合重建、生成应用。

  <details><summary>Abstract</summary>

  3D vision has rapidly evolved, driven by increasingly diverse data representations, learning paradigms, and modeling strategies. Yet the field remains fragmented across representations and benchmarks, making it difficult to develop unified perspectives on efficiency, fidelity, and scalability. This work provides a data-centric taxonomy of 3D vision that connects geometric representations, datasets, learning frameworks, and applications within a single conceptual map. We begin by analysing the principal structural representations of 3D data--point clouds, meshes, voxels, and 3D Gaussians--along with their acquisition pipelines. We then examine how dataset design, benchmark construction, and supervision regimes shape recent advances, spanning 2D-supervised 3D learning, implicit neural representations, and 4D world modeling. Through this integrative lens, we clarify the relationships among representations, learning paradigms, and downstream tasks in reconstruction, generation, and video modeling, offering a consolidated view of emerging trends toward balancing efficiency and fidelity and toward multimodal geometric grounding.

  </details>


- **[Beyond Static Gaussians: An Empirical Investigation of Architectural Paradigms for Dynamic 3D Scene Reconstruction](https://arxiv.org/abs/2606.00452)**  
  *Adrian Ramlal, John S. Zelek*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00452) · [pdf](https://arxiv.org/pdf/2606.00452.pdf)
  > 💡 动态3DGS中结构引导方法重建质量高，高斯中心方法渲染更快但质量不稳，揭示了两者

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction via 3D Gaussian Splatting (3DGS) has emerged as a compelling approach for representing evolving environments, yet understanding trade-offs between methodologies remains crucial. This paper presents a comprehensive analysis of dynamic 3DGS methods, categorizing them into two paradigms: structure-guided methods employing auxiliary representations (deformation fields, canonical spaces, grids) to model temporal changes, and gaussian-centric methods encoding dynamics directly into primitives via continuous functions or 4D representations. We evaluate representative methods from both paradigms on the D-NeRF benchmark. Our findings reveal that structure-guided methods achieve superior reconstruction fidelity and compact model sizes, while gaussian-centric approaches demonstrate significantly higher rendering speeds enabling real-time performance, though with greater quality variability and potentially substantial storage overhead. This analysis highlights a fundamental trade-off between reconstruction quality/compactness versus rendering speed, providing insights to guide future research and application development in dynamic scene reconstruction.

  </details>


- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137)**  
  *Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00137) · [pdf](https://arxiv.org/pdf/2606.00137.pdf)
  > 💡 综述了神经3D网格纹理化方法，从GAN到扩散模型，统一分类并分析架构、监督策略及未来挑战。

  <details><summary>Abstract</summary>

  Texturing 3D meshes plays a vital role in determining the visual realism of digital objects and scenes. Although recent generative 3D approaches based on Neural Radiance Fields and Gaussian Splatting can produce textured assets directly, polygonal meshes remain the core representation across modeling, animation, visual effects, and gaming pipelines. Neural 3D mesh texturing therefore continues to be an essential and active area of research. In this survey, we present a comprehensive review of recent advances in neural 3D mesh texturing, covering methods for texture synthesis, transfer, and completion. We first summarize key foundations in mesh geometry, texture mapping, differentiable rendering, and neural generative models, and then organize the literature into a unified taxonomy spanning early GAN-based methods to modern diffusion-based pipelines. We further analyze common architectures and supervision strategies, review datasets and evaluation protocols, and discuss emerging applications, practical/commercial systems, and open challenges. Together, these insights provide a structured perspective on the current landscape and help guide future developments in learning-based 3D mesh texturing.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (10) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds](https://arxiv.org/abs/2606.05650)**  
  *Rajrup Ghosh, Haodong Wang, Haoran Hong, Eduardo Pavez, Amartya Chaudhuri, Weiwu Pang, Harsha V. Madhyastha, Antonio Ortega, Ramesh Govindan*  
  `2026-06-04` · `cs.MM` · [abs](https://arxiv.org/abs/2606.05650) · [pdf](https://arxiv.org/pdf/2606.05650.pdf)
  > 💡 针对动态高斯泼溅流传输中压缩慢的问题，提出GPU并行加速编解码，实现全帧率处理，速度提升1-2个数量级，压缩与渲染质量相当。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian Splatting (3DGS) holds great promise as a 3D video streaming technology since it can represent complex 3D scenes with high fidelity. In this approach, every frame in a 3D video represents the environment as a collection of Gaussians with position and other attributes such as scale, rotation, opacity, and color. Frames capture fine details, permit views from any arbitrary perspective, but are an order of magnitude, or more, larger than 2D video frames. A line of recent work has explored how to compress dynamic 3DGS frames, but these approaches are often slow, in part because their compression techniques are not amenable to efficient acceleration. GS-NFS accelerates dynamic 3DGS compression and decompression on a GPU, to the point where it can encode and decode at full frame rate. It achieves this by developing novel GPU-based parallelizations of existing algorithms for encoding both positions and attributes of Gaussians. As a result, it is 1-2 orders of magnitude faster than the state-of-the-art in encoding and decoding a frame, while offering competitive compression performance and rendering quality.

  </details>


- **[Self-Learning Expression Deformations for Data-Efficient Gaussian Avatars](https://arxiv.org/abs/2606.05912)**  
  *Jiahao Yang, Xiaohang Yang, Qing Wang, Yilan Dong, Gregory Slabaugh, Shanxin Yuan*  
  `2026-06-04` · `cs.CV` · [abs](https://arxiv.org/abs/2606.05912) · [pdf](https://arxiv.org/pdf/2606.05912.pdf)
  > 💡 针对高斯头像数据需求大的问题，提出自监督SAGE框架，联合2D高斯和SDF实现极少量数据的高质量表情动画。

  <details><summary>Abstract</summary>

  Modeling dynamic facial expressions using 3D Gaussian representations remains challenging due to their unstructured nature. Conventional Gaussian avatar pipelines require extensive multiview and sequential expression data, limiting scalability and accessibility. In this work, we introduce Self-Adaptive Gaussian Expression (SAGE), a framework for self-learning expression-induced Gaussian deformations that enables high-fidelity, animatable avatars from minimal input data. Our method jointly optimizes 2D Gaussian surfels and a Signed Distance Field (SDF) to enforce compact, surface-aligned Gaussian distributions, while a self-supervised expression learning phase replaces long training sequences with geometric and appearance consistency constraints. This design allows flexible deployment across multiple reconstruction regimes: in the multiview setting, only a single frame (timestep) is required instead of thousands; in the monocular setting, only head rotations are needed without expression sequences; and in the one-shot setting, no pretraining or priors are necessary. Experiments demonstrate that our approach achieves reconstruction and animation quality comparable to state-of-the-art methods, while reducing data requirements by several orders of magnitude. Our results highlight the potential of self-supervised Gaussian deformation learning as a step toward accessible, data-efficient avatar creation.

  </details>


- **[SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation](https://arxiv.org/abs/2606.03909)**  
  *Qingpo Wuwu, Xiaobao Wei, Peng Chen, Nan Huang, Zhongyu Zhao, Hao Wang, Ming Lu, Ningning Ma, Shanghang Zhang*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03909) · [pdf](https://arxiv.org/pdf/2606.03909.pdf)
  > 💡 街道场景高斯点冗余导致存储渲染瓶颈，提出节点剪枝和背景压缩框架，实现80%压缩率且质量损失极小。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting has shown promising results in street scene reconstruction, existing methods require massive numbers of Gaussian primitives to capture fine details, leading to prohibitive storage costs and slow rendering speeds. We observe that dynamic objects (e.g., vehicles and pedestrians) demand high-fidelity representations to maintain temporal consistency, while static background regions often contain substantial redundancy. Motivated by this, we propose SparseStreet, a general compression framework specifically designed for street scenes. First, we introduce a node-based learnable pruning strategy that systematically removes low-contributing Gaussian primitives while preserving visually critical regions. Second, after the scene representation stabilizes, we apply background compression, further reducing redundancy in static regions. Our method effectively preserves the geometry and appearance of dynamic objects while significantly reducing the total number of Gaussian primitives. Extensive experiments on the Waymo and nuScenes demonstrate that SparseStreet achieves up to 80% compression ratio with minimal quality degradation, enabling resource-efficient, high-fidelity dynamic scene reconstruction. Project website: https://sparsestreet.github.io/.

  </details>


- **[PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting](https://arxiv.org/abs/2606.03479)**  
  *Adrian Ramlal, John S. Zelek*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03479) · [pdf](https://arxiv.org/pdf/2606.03479.pdf)
  > 💡 通过可微刚体模拟与3DGS结合，解决遮挡时物体高斯退化问题，实现物理准确轨迹预测并降低40%轨迹误差。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian Splatting (3DGS) methods reconstruct time-varying scenes from synchronized multi-camera video using photometric supervision. When a moving object becomes fully occluded from all training cameras, this supervision vanishes: the Gaussians representing it receive no gradient signal and degrade. Existing approaches to incomplete observations in neural reconstruction rely on learned generative priors that prioritize visual plausibility over physical correctness. We propose $\textbf{PersistGS}$, a method that restores object permanence during occlusion by coupling differentiable rigid body simulation with 3D Gaussian Splatting. Our approach decomposes the scene into per-object Gaussians and collision meshes, estimates friction and velocity from the observed pre-occlusion trajectory via differentiable simulation, and uses the resulting SE(3) trajectory to position object Gaussians throughout the occlusion period. Because the predicted trajectory satisfies the governing equations of rigid body dynamics, it faithfully captures contact events (bounces, friction-based deceleration, direction changes) that kinematic extrapolation cannot model. We introduce a centroid silhouette loss that isolates positional gradients from appearance noise, yielding 40% lower trajectory error than photometric supervision. We evaluate using cameras withheld from training that observe the object during its occlusion. Experiments on synthetic scenes show that PersistGS outperforms constant velocity extrapolation by +2.46dB PSNR and comes within 0.19dB of a ground-truth trajectory upper bound.

  </details>


- **[FreeStreamGS: Online Feed-forward 3D Gaussian Splatting from Unposed Streaming Inputs](https://arxiv.org/abs/2606.03254)**  
  *Ruiyang Chen, Feiran Li, Chu Zhou, Zonglin Li, Zhanyu Ma, Heng Guo*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03254) · [pdf](https://arxiv.org/pdf/2606.03254.pdf)
  > 💡 提出解耦内在恢复头和动态点细化偏移策略，解决流式无位姿输入下3D高斯溅射的累积漂移与渲染伪影问题。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting (3DGS) allows efficient and high-fidelity novel view synthesis (NVS) from an offline recorded image sequence. However, achieving online NVS from streaming and unposed image inputs remains challenging. Although online feed-forward geometric estimation methods have been proposed for streaming depth and point cloud recovery, they cannot be adapted to NVS due to severe rendering artifacts. This is because NVS demands stricter multi-view consistency in Gaussian scales and pose-geometry alignment; even minor deviations would accumulate over time and visibly degrade rendering quality. To this end, we propose FreeStreamGS, a robust online feed-forward framework for efficient and high-quality NVS. We introduce two key mechanisms: a Decoupled Intrinsic Recovery Head that removes cumulative camera intrinsic bias and prevents scene scale jitter during long-term streaming, and a Dynamic Point Refinement Offset strategy that relaxes rigid unprojection to correct coupled pose-depth drift. Extensive experiments show that FreeStreamGS achieves rendering quality competitive with state-of-the-art offline feed-forward 3DGS methods, despite operating without access to future frames.

  </details>


- **[TIDES: Time-Derivative Event Simulation via Deformable Reconstruction](https://arxiv.org/abs/2606.02058)**  
  *Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02058) · [pdf](https://arxiv.org/pdf/2606.02058.pdf)
  > 💡 基于动态高斯泼溅的连续时间事件模拟器，解决时间戳批处理问题，实现高保真事件流并提升下游任务迁移效果。

  <details><summary>Abstract</summary>

  Event cameras emit asynchronous events in response to environmental appearance changes. The scarcity of real-world event datasets makes simulation essential. However, most simulators infer event timestamps from frame sequences, forcing many threshold crossings to share a small set of discrete times; a failure mode we term timestamp batching that worsens under fast motion and occlusion. We present TIDES, a continuous-time event simulator built on dynamic Gaussian splatting. Because TIDES operates on an explicit 3D scene representation with learnt geometry and motion, it can derive per-pixel intensity dynamics directly from the scene, rather than by differencing rendered frames. This enables accurate threshold-crossing prediction, including multiple crossings per rendering step, without temporal upsampling or frame interpolation. The same 3D scene model reveals where objects partially occlude one another; TIDES uses this to guide adaptive time stepping, concentrating computation only in regions where occlusion dynamics make simple models of brightness change unreliable. Finally, we model finite sensor bandwidth using a tile-level arbiter whose throughput, jitter, and event drops reproduce realistic sensor artifacts. Across paired RGB-event benchmarks, TIDES attains state-of-the-art event-stream fidelity. We also show that events simulated by TIDES transfer more effectively to real downstream tasks than competitors'.

  </details>


- **[Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects](https://arxiv.org/abs/2606.01950)**  
  *Jens U. Kreber, Lukas Mack, Joerg Stueckler*  
  `2026-06-01` · `cs.RO` · [abs](https://arxiv.org/abs/2606.01950) · [pdf](https://arxiv.org/pdf/2606.01950.pdf)
  > 💡 用物体中心高斯和时空Transformer预测刚体动作动力学，处理多物体遮挡，实现无抓取操控。

  <details><summary>Abstract</summary>

  World models enable intelligent agents to predict the consequences of their actions on the environment. In this paper, we propose Multi Rigid Object Gaussian World Model (MRO-GWM), a novel model that learns action-conditional dynamics of rigid objects in 3D. By representing the scene by object-centric Gaussians, we can represent arbitrary object shapes and multi-object scenes. We develop a novel spatio-temporal transformer architecture that predicts future rigid body motion from a history of object Gaussians and future actions. Objects are represented by their Gaussians in a canonical frame, which allows for describing object motion as rigid body transformation. Our model is trained on reconstructions from multiple viewpoints, which requires the model to handle partial observations of objects due to occlusions. We analyze prediction performance of our approach on synthetic datasets composed of typical household objects with multi-object dynamics and interactions by a robot end effector. We also evaluate our model in model-predictive control for non-prehensile manipulation in simulation.

  </details>


- **[MORPHOS: Autoregressive 4D Generation with Temporal Structured Latents](https://arxiv.org/abs/2606.02491)**  
  *Minkyung Kwon, Jinhyeok Choi, Youngjin Shin, Jaeyeong Kim, JongMin Lee, Seungryong Kim*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02491) · [pdf](https://arxiv.org/pdf/2606.02491.pdf)
  > 💡 针对动态3D生成中表示单一和时序不一致问题，提出自回归框架MORPHOS，利用Temporal Structured Latents统一表示实现因果注意力生成，在多种表示上达到SOTA。

  <details><summary>Abstract</summary>

  We present MORPHOS, a novel autoregressive framework that generates dynamic 3D assets from videos across diverse representations, including meshes, 3D Gaussians, and radiance fields. Existing methods are typically limited to a single representation, struggle to model topological changes, or fail to maintain temporal consistency over long videos. To address these limitations, we introduce the Temporal Structured Latents (T-SLAT), a unified 4D representation that jointly encodes geometry and appearance along the temporal dimension. Leveraging T-SLAT, MORPHOS autoregressively generates dynamic 3D assets via causal attention, conditioning each frame on its preceding history to ensure temporal consistency while handling evolving topologies. We also propose a temporal-structural augmentation to mitigate error accumulation in autoregressive generation. MORPHOS achieves state-of-the-art performance in appearance and competitive results in geometry across multiple benchmarks, demonstrating superior generalization across various representations and robustness in long-horizon generation.

  </details>


- **[WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos](https://arxiv.org/abs/2606.02096)**  
  *Jongmin Park, Jeonghwan Yun, Minh-Quan Viet Bui, Munchurl Kim*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02096) · [pdf](https://arxiv.org/pdf/2606.02096.pdf)
  > 💡 针对单目视频动态场景重建的结构与细节平衡难题，提出WebSpline，用结构信息样条和图代理实现快速、高保真渲染，质量领先且提速10倍。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction from monocular videos remains highly challenging, as existing methods often struggle to balance global structural coherence and local fine-grained details under limited multi-view cues. To address this challenge, we propose WebSpline, a novel dynamic 3D Gaussian framework that enables structurally coherent and high-fidelity reconstruction from monocular videos with fast rendering. The core of WebSpline is the Structure-Informed Spline (SIS) representation, which models each dynamic Gaussian trajectory using a learnable cubic Hermite spline whose motion is structurally organized with an auxiliary Structural Proxy Graph (SPG). The proposed framework is optimized in two stages: (i) in the first stage, the SPG is initialized from 2D point tracks and refined with temporal rigidity regularization to establish structural coherence for moving objects across the sequence; and (ii) in the second stage, the SIS representation is initialized from the refined SPG and optimized under both spatial and structural neighborhood constraints. At inference, Gaussian motion is obtained solely by evaluating the learned SIS, enabling fast rendering. Extensive experiments on the challenging monocular dynamic scene benchmarks, iPhone and NVIDIA, demonstrate that our WebSpline achieves state-of-the-art rendering quality while rendering over 10 times faster than WorldTree, the second-best method on the iPhone dataset.

  </details>


- **[Real-Time Physics Simulation with Dynamic Mesh-Gaussian Reconstructions](https://arxiv.org/abs/2606.00444)**  
  *Adrian Ramlal, John S. Zelek*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00444) · [pdf](https://arxiv.org/pdf/2606.00444.pdf)
  > 💡 提出固定拓扑网格与高斯泼溅双表征框架实现4.65倍加速模拟，揭示高质量重建与物理兼容拓扑本质矛盾。

  <details><summary>Abstract</summary>

  Integrating dynamic 3D reconstructions into physics simulation requires fixed mesh topology for efficient collision detection, but state-of-the-art methods like DG-Mesh produce varying topology optimized for geometric quality. We investigate whether topology conversion can enable physics integration while preserving reconstruction fidelity. We propose a dual-representation framework combining fixed-topology meshes for physics with Gaussian splatting for rendering, achieving 4.65$\times$ speedup over varying-topology baselines through runtime vertex buffer updates. We evaluate two conversion strategies, temporal correspondence tracking and template-based projection, against native fixed-topology methods (MaGS) on the DG-Mesh dataset. Our evaluation reveals that both conversion approaches incur 65-80% geometric degradation, producing results inferior to MaGS despite DG-Mesh's superior initial quality. This demonstrates that high-quality reconstruction and physics-compatible topology represent fundamentally distinct objectives that cannot be reconciled through post-processing. Our findings inform future development of physics-aware reconstruction methods and our framework enables real-time simulation with any fixed-topology approach.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (4) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning](https://arxiv.org/abs/2606.02346)**  
  *Aoduo Li, Jiancheng Li, Huan Ye, Hongjian Xu, Shiting Wu, Xiujun Zhang, Zimeng Li, Xuhang Chen*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02346) · [pdf](https://arxiv.org/pdf/2606.02346.pdf)
  > 💡 用变分自由能最小化建模剪枝，提出预测误差门控和变分不确定性头，实现5.2倍压缩仅降0.31 dB PSNR。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves remarkable novel view synthesis quality with real-time rendering, yet suffers from excessive memory consumption due to millions of Gaussian primitives. Existing pruning methods rely on heuristic importance scores or synchronous batch updates, leading to suboptimal compression and training instability. We propose VEDAL, a principled framework that formulates Gaussian pruning as variational free energy minimization. Our approach introduces (1) a prediction-error gating mechanism that asynchronously activates pruning based on per-Gaussian reconstruction uncertainty, and (2) a variational uncertainty head that models pruning decisions as latent variables with learnable priors. The free energy objective naturally balances reconstruction fidelity against model complexity through an information-theoretic lens. Extensive experiments on Mip-NeRF 360, Tanks&Temples, and Deep Blending demonstrate that VEDAL achieves 5.2x compression with only 0.31 dB PSNR drop, outperforming PUP 3D-GS by +0.05 dB at a higher compression ratio and LightGaussian by +0.35 dB at comparable quality, while maintaining real-time rendering at 185 FPS.

  </details>


- **[Splatshot: 3D Face Avatar Generation from a Single Unconstrained Photo](https://arxiv.org/abs/2606.01493)**  
  *Hao Liang, Zhixuan Ge, Soumendu Majee, Joanna Li, Ashok Veeraraghavan, Guha Balakrishnan*  
  `2026-05-31` · `cs.CV` · [abs](https://arxiv.org/abs/2606.01493) · [pdf](https://arxiv.org/pdf/2606.01493.pdf)
  > 💡 针对单张照片重建3D头像，SplatShot在扩散去噪中联合3DGS与2D先验，实现几何一致与逼真结果。

  <details><summary>Abstract</summary>

  Reconstructing a photorealistic 3D face avatar from a single unconstrained photograph is challenging: feed-forward 3D Gaussian Splatting (3DGS) models degrade on out-of-distribution inputs, while pretrained diffusion models produce high-fidelity images but lack multi-view consistency. We observe that these paradigms are fundamentally complementary: explicit 3D representations guarantee geometric consistency, whereas 2D diffusion priors ensure photorealism. Building on this, we propose SplatShot, a training-free framework that couples these representations directly within the denoising process. Given a base 3DGS face model and a single reference image, we jointly denoise all target views using a per-step 3D feedback loop. At each timestep, we predict clean images from the noisy latents, refit the 3DGS to these multi-view predictions, and back-propagate the photometric discrepancy between the 3DGS re-renderings and 2D predictions into the noise estimate. This steers the sampling trajectory toward strictly 3D-coherent, identity-faithful outputs. Experiments on diverse in-the-wild images demonstrate that SplatShot produces 3D avatars with superior identity preservation, photorealism, and multi-view consistency.

  </details>


- **[LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World](https://arxiv.org/abs/2606.01458)**  
  *Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager*  
  `2026-05-31` · `cs.RO` · [abs](https://arxiv.org/abs/2606.01458) · [pdf](https://arxiv.org/pdf/2606.01458.pdf)
  > 💡 LEGS用3DGS背景和程序化基元生成器

  <details><summary>Abstract</summary>

  Training vision-language-action (VLA) policies for humanoid loco-manipulation is constrained by the high cost and complexity of collecting human teleoperation demonstrations. VLA policies fine-tuned in simulators have, until now, failed to transfer effectively in humanoid loco-manipulation tasks. We present LEGS (Loco-manipulation via Embodied Gaussian Splatting), a hybrid simulator that composites a mesh foreground (robot, objects, props) over a photorealistic 3D Gaussian Splatting (3DGS) background reconstructed from a handheld scene capture. LEGS uses a procedural motion-primitive generator to synthesize labeled demonstrations at scale without human teleoperation, and a deterministic two-stage color calibration to align the rendered 3DGS image to the robot's deployment camera. On a Unitree G1 humanoid robot, across three pick-and-place tasks of increasing whole-body difficulty and three VLA backbones (psi_0, pi_0.5, GR00T N1.6), a policy trained purely on LEGS data matches or exceeds one trained on human teleoperation demos on every experiment. It also outperforms a mesh-only simulation baseline that ablates the effect of the 3DGS background, showing that photorealistic rendering is a key enabler for synthetic data transfer. Humanoid motion is recorded independently of scene appearance in LEGS, allowing the same auto-generated demonstrations to be re-rendered under new backgrounds and object meshes--covering a new scene at more than 15x lower cost than teleoperation--to augment training data for robustness to scene variations. Under combined object-and-scene appearance shift, the policy trained on re-rendered LEGS-AUG data maintains task success while the baseline trained on teleoperation data fails entirely. Our project page is located at https://legsvla.github.io/.

  </details>


- **[GeoSAM-3D: Geodesic Prompt Propagation for Open-Vocabulary 3D Scene Segmentation from Monocular Video](https://arxiv.org/abs/2606.00447)**  
  *Arun Sharma*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00447) · [pdf](https://arxiv.org/pdf/2606.00447.pdf)
  > 💡 结合单目视频与3D高斯重建，用测地线热核传播代替欧氏近邻，解决开放词汇分割中曲面连续性与泄漏问题。

  <details><summary>Abstract</summary>

  Open-vocabulary 3D scene segmentation usually assumes RGB-D video, calibrated multi-view imagery, or a reconstructed mesh. GeoSAM-3D studies a lighter setting: a user uploads a short monocular video, clicks or names an object in one frame, and receives a propagated 3D mask over a Gaussian scene. The implementation combines frozen image and video foundation models with a monocular 3D Gaussian Splatting reconstruction and a differentiable graph-geodesic propagation kernel over Gaussian centroids. The central design choice is to propagate prompts by heat-kernel distance on the reconstructed scene graph, rather than by Euclidean nearest neighbors in 3D. This preserves continuity around curved surfaces and reduces leakage across nearby but disconnected objects. This paper describes the repository state, the mathematical kernel implemented in geosam3d.propagate, the feature head trained from Segment Anything masks, and the validation already present in the codebase. The evaluation protocol separates implementation validation, graph propagation quality, leakage control, and interactive latency.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (3) · <a href="topics/generation.md">full list →</a></summary>

- **[Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image](https://arxiv.org/abs/2606.02068)**  
  *Kaidi Zhang, Guanxu Zhu*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02068) · [pdf](https://arxiv.org/pdf/2606.02068.pdf)
  > 💡 利用点图初始化MPI和一步扩散优化，实现比3DGS快30.7%、模型缩小85.2%的轻量级新视角合成。

  <details><summary>Abstract</summary>

  Recently, novel view synthesis has witnessed remarkable progress, with mainstream methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) delivering impressive results. However, these approaches often struggle to balance rendering speed and model size, and their optimization-based training can be highly time-consuming. Furthermore, they typically rely on dense observations, often failing to produce satisfactory results under sparse-view conditions. Although feed-forward reconstruction significantly reduces the optimization time of 3DGS, its pixel-aligned formulation generates millions of Gaussians from a single image, severely limiting its practical deployment on mobile devices. To address these limitations, we revisit the Multiplane Image(MPI) representation, which represents scenes using a compact set of planar layers for efficient novel view synthesis. Leveraging recent advances in visual foundation models, we utilize predicted point maps for reliable geometric initialization, followed by differentiable optimization. To address the issues of holes and artifacts in sparsely initialized MPI, we introduce one-step diffusion, which participates in both the differentiable optimization of MPI and the postprocessing of rendering results. Compared with a representative GS-based method, our approach is 30.7% faster and uses only 14.8% of its model size, while achieving competitive synthesis quality on front-view scenarios

  </details>


- **[DeblurNVS: Geometric Latent Diffusion for Novel View Synthesis from Sparse Motion-Blurred Images](https://arxiv.org/abs/2606.01315)**  
  *Changyue Shi, Wangbo Yu, Chaoran Feng, Li Yuan*  
  `2026-05-31` · `cs.CV` · [abs](https://arxiv.org/abs/2606.01315) · [pdf](https://arxiv.org/pdf/2606.01315.pdf)
  > 💡 从稀疏运动模糊图像合成新视图，提出几何潜在扩散恢复结构表征，无需逐场景优化。

  <details><summary>Abstract</summary>

  Novel view synthesis (NVS) is a fundamental problem in computer vision and graphics. Recent advances in neural radiance fields (NeRF), 3D Gaussian Splatting (3DGS), and generative view synthesis have substantially improved its quality. Yet most methods still rely on clean observations, where image structures and cross-view geometric cues are well preserved. Motion blur breaks this assumption by corrupting local details and weakening multi-view correspondences. Such blur commonly arises from camera shake, scene motion, or finite exposure in practical capture. Blur-aware NVS methods address this degradation by modeling image formation, but their reliance on costly per-scene optimization limits efficient and generalizable sparse-view synthesis. To address this, we propose DeblurNVS, a novel framework for synthesizing high-fidelity novel views directly from sparse motion-blurred images, without requiring per-scene optimization. DeblurNVS restores the intermediate geometric representations needed for multi-view reasoning, enabling blurred inputs to recover reliable structure and correspondence cues. The restored representations are then combined with target camera information to synthesize the target-view representation and reconstruct a sharp RGB novel view. To enable the large-scale training, we construct a motion-blurred NVS dataset from DL3DV-10K using interpolation-based finite-exposure blur synthesis. Extensive experiments demonstrate that DeblurNVS outperforms existing baselines on synthetic motion-blur benchmarks and generalizes to real motion-blurred scenes, producing perceptually sharper and structurally more stable novel views while avoiding costly per-scene optimization. Project page: https://github.com/PKU-YuanGroup/DeblurNVS.

  </details>


- **[Optimizing 3D Gaussian Splatting via Point Cloud Upsampling](https://arxiv.org/abs/2606.00450)**  
  *Adrian Ramlal, Yan Song Hu, John S. Zelek*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00450) · [pdf](https://arxiv.org/pdf/2606.00450.pdf)
  > 💡 利用多种点云上采样和深度引导方法优化3DGS初始化，提升重建质量，并给出场景适应性选择建议。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a technique for creating and rendering 3D scenes, however its performance depends heavily on the quality of initial seed points. To improve 3DGS initialization, this study presents and evaluates several point cloud upsampling approaches: linear interpolation, triangular interpolation, spline-based surface reconstruction, moving least squares surface fitting, and Voronoi-based point generation. Additionally, this research introduces a depth-guided point lifting method that leverages depth maps to maintain geometric consistency with Structure-from-Motion (SfM) reconstructions. Through extensive experiments on the Mip-NeRF360 and Replica datasets, the proposed methods demonstrate improvements in reconstruction quality across diverse scene types. Results indicate that different upsampling strategies excel in different scenarios: surface reconstruction methods perform better with organic, detailed scenes, while simpler interpolation approaches are more suited for scenes dominated by piecewise-smooth geometries. In comparison, the depth-guided approach shows promise for adding geometry-aware points across the entire scene, importantly in texture-less regions. These findings, which provide preliminary practical guidelines for selecting appropriate upsampling methods based on scene characteristics and computational constraints, advances the understanding of how point cloud initialization affects 3DGS quality.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (1) · <a href="topics/editing.md">full list →</a></summary>

- **[MLP Splatting: Object-Centric Neural Fields](https://arxiv.org/abs/2606.03877)**  
  *Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03877) · [pdf](https://arxiv.org/pdf/2606.03877.pdf)
  > 💡 以紧凑MLP光场基元替代高斯基元，实现高效场景分解和新视图合成，内存和渲染速度显著优于语义3DGS。

  <details><summary>Abstract</summary>

  3D representations are fundamental to scene rendering, understanding, and interaction. Recent approaches, such as 3D Gaussian Splatting and Neural Radiance Fields, achieve impressive photorealistic novel-view synthesis, but lack the ability to easily decompose scene elements into a few primitives, requiring additional segmentation or grouping for object-level manipulation. We present MLP-Splatting, a method that enables scene decomposition via a few expressive light-field primitives while providing photorealistic novel-view synthesis. MLP-Splatting models each primitive as an independent compact MLP with localized spatial support that predicts radiance and opacity. In contrast to low-level Gaussian primitives or a single global radiance field, our neural primitives provide greater expressive capacity while remaining spatially localized. Rendering is performed through efficient sparse volumetric compositing over ray-primitive interactions. Our primitives are supervised using RGB supervision alone, which yields primitives that represent local scene regions often corresponding to objects or object parts, enabling interactive object-level editing without segmentation masks by selecting a handful of primitives. Our method, augmented with optional semantic feature distillation, enables open-vocabulary scene interaction and open-set instant segmentation. Compared to state-of-the-art methods, we achieve substantially lower memory usage (1/15$\times$) and faster rendering (3$\times$), as we show in our experiments compared to semantic 3DGS methods. Project Page: https://shinjeongkim.com/mlp-splatting

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[ZipSplat: Fewer Gaussians, Better Splats](https://arxiv.org/abs/2606.05102)**  
  *Alexander Veicht, Sunghwan Hong, Dániel Baráth, Marc Pollefeys*  
  `2026-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2606.05102) · [pdf](https://arxiv.org/pdf/2606.05102.pdf)
  > 💡 用聚类压缩视觉token为场景token，解耦高斯放置与像素网格，实现更少高斯更优质量，无需真值位姿。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting methods reconstruct a scene from posed or pose-free images in a single forward pass, yet current approaches predict one Gaussian per input pixel, tying the representation budget to camera resolution rather than scene complexity. A flat wall and a richly textured object thus produce equally many Gaussians despite very different geometric needs. We propose ZipSplat, a token-based feed-forward model that decouples Gaussian placement from the pixel grid. A multi-view backbone extracts dense visual tokens, and k-means clustering compresses them into a compact set of scene tokens. Cross- and self-attention refine these tokens, and a lightweight MLP decodes each into a group of Gaussians with unconstrained 3D positions. Because clustering is applied at inference, a single trained model spans the quality-efficiency curve without retraining. ZipSplat operates without ground-truth poses or intrinsics, yet sets a new state of the art on DL3DV and RealEstate10K with ${\sim}6{\times}$ fewer Gaussians than pixel-aligned methods, surpassing the best pose-free baseline by 2.1dB and 1.2dB PSNR, respectively. It further generalizes zero-shot to Mip-NeRF360 and ScanNet++, outperforming all comparable baselines. Our project page is at ${\href{https://veichta.com/zipsplat}{https://veichta.com/zipsplat}}$.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (4) · <a href="topics/rendering.md">full list →</a></summary>

- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120)**  
  *Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03120) · [pdf](https://arxiv.org/pdf/2606.03120.pdf)
  > 💡 KC-3DGS用峰度约束的小波域监督弥补标准3DGS高频细节缺失，提升感知质量与稀疏视图性能。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables real-time novel view synthesis by representing scenes as collections of anisotropic Gaussians optimized via differentiable rasterization. However, standard pixel-space losses (L1, SSIM) constrain only aggregate reconstruction error, permitting the optimization to redistribute error across frequency scales. This leads to oversmoothing and structural artifacts, particularly in sparse-view settings where supervision is limited. We propose KC-3DGS, which augments 3DGS training with wavelet-domain supervision based on natural image statistics. Our method combines three components: (1) a multi-scale wavelet coefficient alignment loss that explicitly penalizes missing high-frequency detail, (2) a supervised kurtosis concentration loss that encourages rendered images to match the heavy-tailed frequency statistics of ground-truth images, and (3) a cross-band covariance penalty that promotes frequency specialization. We provide theoretical analysis showing that pixel-space losses admit a family of indistinguishable perturbations under wavelet redistribution, and that our joint objective excludes degenerate solutions. Experiments across MipNeRF360, Tanks&Temples, MVImgNet, DeepBlending, and WRIVA-ULTRRA demonstrate consistent improvements in perceptual quality. On the challenging WRIVA-ULTRRA outdoor dataset, KC-3DGS achieves a 9.48% improvement in DreamSim while also improving PSNR, SSIM, and LPIPS. In sparse-view settings with only 12 training images, our method improves PSNR by up to 0.5 dB on MipNeRF360 while maintaining perceptual quality. The approach integrates seamlessly into existing 3DGS pipelines as a plug-and-play regularization strategy.

  </details>


- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261)**  
  *Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang*  
  `2026-05-31` · `eess.IV` · [abs](https://arxiv.org/abs/2606.01261) · [pdf](https://arxiv.org/pdf/2606.01261.pdf)
  > 💡 面向28GHz室内射线追踪，联合RGB-LiDAR与3DGS构建RF数字孪生，语义分割赋予材质属性，有效路径从742降至52。

  <details><summary>Abstract</summary>

  Real-scene indoor millimeter-wave simulation requires efficient modeling of radio frequency (RF)-computable geometry and electromagnetic material properties. To address the low efficiency of manual scene modeling, the limited RF adaptability of visually reconstructed meshes, and the lack of material binding in 28 GHz ray-tracing simulation, RFDT-Channel is developed as an RF digital twin scene construction workflow based on red-green-blue (RGB) images and light detection and ranging (LiDAR) point clouds. Indoor videos and point clouds are collected by a Jetson Orin platform with LiDAR and GMSL cameras. An initial triangular mesh is generated through COLMAP, 3D Gaussian Splatting, and SuGaR. The LiDAR point cloud then provides geometric and scale references for RF-oriented regularization in Blender, including alignment, wall solidification, door/window opening construction, and topology repair. OpenScene semantic segmentation maps major indoor structures to concrete, glass, wood, and metal materials, and Sionna RT performs 28 GHz ray tracing. Under a fixed transmitter-receiver deployment, the generated channel impulse response (CIR), channel frequency response (CFR), and Radio Map results show that material binding mainly changes weak reflection, transmission, and scattering paths, reducing the number of effective paths from about 742 to about 52 while keeping the dominant path amplitude nearly unchanged.

  </details>


- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817)**  
  *Subhankar MIshra*  
  `2026-05-30` · `cs.GR` · [abs](https://arxiv.org/abs/2606.00817) · [pdf](https://arxiv.org/pdf/2606.00817.pdf)
  > 💡 针对3DGS无法追踪次光线，提出定向距离场(DDF)实现快速恒定时间射线查询，无需网格且内存不随

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) renders new views of a scene in real time. Like every rasterizer, it answers only primary rays, the rays from the camera through the image. It cannot trace the secondary rays that shadows, ambient occlusion, and global illumination need. We turn a trained 3DGS scene into a ray oracle by distilling a Directed Distance Function (DDF). The DDF is a small neural field. It takes a ray, given by an origin and a direction, and returns the distance to the first surface and whether the ray hits anything. Each query is one forward pass. The field is 52~MB, and its size does not depend on the number of Gaussians, so its cost and memory stay flat as the scene grows. We make three points. First, we study what supervision a DDF needs. Depth rendered from the Gaussians is too blurry to teach thin parts, while clean distance supervision recovers them. Second, we measure speed. The DDF is 26 to 72 times faster than sphere tracing an equivalent signed distance field, and unlike a bounding volume hierarchy built over the Gaussians, even on dedicated RT-core hardware, its query time and memory do not grow with the scene. Third, we show a pipeline that needs no mesh: images give a 3DGS scene, a neural surface gives clean distances, and the DDF learns from them. We use the DDF as a secondary-ray oracle for global illumination. It reproduces reference ray-traced shadows at 30.3~dB and ambient occlusion at 21.3~dB across 142 objects, and on real captured scenes. Our codes are available at https://github.com/smlab-niser/ddf-gs.

  </details>


- **[HiGS: A Hierarchical Rendering Architecture for Real-Time 3D Gaussian Splatting](https://arxiv.org/abs/2606.00352)**  
  *Dawid Pająk, Martin Bisson, Rodolfo Lima*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00352) · [pdf](https://arxiv.org/pdf/2606.00352.pdf)
  > 💡 3DGS中分区与光栅化对瓦片大小需求矛盾，提出分层渲染架构HiGS，宏块分区精细光栅化，加速达15.8倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become the standard for real-time novel view synthesis on commodity GPUs. Its pipeline ties spatial partitioning and rasterization to one tile size, yet the two pull in opposite directions: partitioning, which bins and depth-sorts gaussians, grows cheaper with larger tiles, while rasterization gets cheaper with smaller ones. Prior acceleration work reduces the cost of individual stages but keeps both locked to that single scale, where a few dense tiles dominate frame time. We present Hierarchically Tiled Gaussian Splatting (HiGS), which gives each its own scale: partitioning runs over coarse macro-tiles, while rasterization runs over the fine render tiles within them. Rasterization work is then issued in proportion to the gaussians in each macro-tile rather than per tile, so dense regions spread across many parallel units instead of serializing through one. Across tested scenes, HiGS renders up to 15.8x faster than the original 3DGS and outperforms every other rasterizer we evaluate, while preserving exact front-to-back alpha compositing.

  </details>


</details>

<details><summary><b>SLAM / Localization / Mapping</b> (2) · <a href="topics/slam.md">full list →</a></summary>

- **[Multi-Agent Next-Best-View Optimization for Risk-Averse Planning](https://arxiv.org/abs/2606.04158)**  
  *Amirhossein Mollaei Khass, Vivek Pandey, Guangyi Liu, Athanasios Cosse, Emrah Bayrak, Nader Motee*  
  `2026-06-02` · `cs.RO` · [abs](https://arxiv.org/abs/2606.04158) · [pdf](https://arxiv.org/pdf/2606.04158.pdf)
  > 💡 分布式多智能体NBV框架，利用3DGS局部地图和C-ADMM优化，实现风险规避和低通信的路径规划。

  <details><summary>Abstract</summary>

  Multi-agent Next-Best-View (NBV) selection for safe path planning in uncertain and unknown environments requires informative, safety-aware, and efficient coordination. Centralized approaches rely on sharing raw sensor data or significant communication overhead, resulting in limited scalability. We propose a distributed, risk-aware multi-agent NBV framework in which each robot maintains a private local 3D Gaussian Splatting map and the team jointly maximizes expected information gain (EIG) restricted to masked zones along planned trajectories. The resulting distributed objective is solved by Consensus ADMM (C-ADMM) over a communication graph, with each robot exchanging only candidate viewpoints, planned trajectory descriptors, and scalar EIG contributions. Collision risk along each trajectory is modeled via Average Value-at-Risk (AV@R) over the local 3DGS map and used both to shape the masking radius and to score planned paths. Experiments in Gibson environments at multiple team sizes show that the distributed formulation approaches the centralized baseline in mapping quality and trajectory safety while reducing communication by orders of magnitude.

  </details>


- **[BEAST3D: Animal behavioral analysis and neural encoding from multi-view video via Gaussian splatting](https://arxiv.org/abs/2606.02937)**  
  *Yanchen Wang, Lenny Aharon, Wangshu Zhu, Kyle Daruwalla, Linghua Zhang, Jiaru Zou, Selmaan Chettih, Helen Hou, Liam Paninski, Matthew R Whiteway*  
  `2026-06-01` · `q-bio.NC` · [abs](https://arxiv.org/abs/2606.02937) · [pdf](https://arxiv.org/pdf/2606.02937.pdf)
  > 💡 用自监督高斯点云渲染从多视角视频学习3D动物行为特征，无需标注即可进行姿态估计与神经编码。

  <details><summary>Abstract</summary>

  Multi-view video recordings are increasingly used to capture the 3D movements of animals in experimental settings, yet extracting rich 3D representations from these recordings remains challenging. Supervised pose estimation requires extensive manual annotation, while general-purpose 3D reconstruction models trained on generic scene datasets fail on the specialized imagery and sparse-view setting of laboratory experiments. We address these limitations with BEAST3D, a self-supervised pretraining framework that learns 3D visual representations from unlabeled, calibrated multi-view video. BEAST3D uses a vision transformer to predict 3D Gaussian splats that reconstruct held-out views through differentiable rendering, while simultaneously segmenting the animal from the background. BEAST3D reconstructs 3D structure with as few as four views by conditioning directly on known camera parameters--unlike general-purpose models, which must estimate camera geometry from dense overlapping viewpoints that are seldom available in lab settings. Through comprehensive evaluation across four species, we demonstrate that BEAST3D produces rich, viewpoint-invariant features that transfer effectively to three downstream tasks: novel view synthesis, which validates the quality of the learned 3D representations; multi-view pose estimation, which provides the sparse keypoint trajectories widely used in behavioral analysis; and neural encoding, which relates 3D behavioral features to simultaneously recorded neural activity. BEAST3D thus establishes a versatile framework for behavioral analysis that leverages 3D structure in modern multi-view laboratory recordings.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (1) · <a href="topics/driving.md">full list →</a></summary>

- **[UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion](https://arxiv.org/abs/2606.03581)**  
  *Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03581) · [pdf](https://arxiv.org/pdf/2606.03581.pdf)
  > 💡 非结构化场景稀疏长尾问题，提出RenderFusion双向渲染融合与GSRefinement高斯泼溅监督，显著提升语义占用预测鲁棒性。

  <details><summary>Abstract</summary>

  Unstructured scenes present unique challenges for autonomous driving, as irregular obstacles and sparse scene layouts undermine the effectiveness of traditional perception methods such as 3D object detection. 3D semantic occupancy prediction has emerged as a prominent focus due to its ability to provide dense spatial representations by assigning semantic labels to individual voxels in 3D space. However, directly applying 3D semantic occupancy prediction to unstructured scenes remains challenging because scene sparsity hinders effective cross-modal fusion and the more severe long-tail distribution in these scenarios further degrades prediction performance. To validate the effectiveness of our approach, we construct a dedicated dataset of unstructured scenes collected from open-pit mines. Based on this, we propose UnsOcc, a multi-modal 3D semantic occupancy prediction framework that improves robustness in unstructured environments. At its core, we introduce a rendering-based fusion module, RenderFusion, which enhances cross-modal feature alignment through bidirectional rendering supervision. Furthermore, we propose GSRefinement, a detail-aware auxiliary supervision method based on Gaussian Splatting that projects sparse 3D occupancy predictions into dense 2D semantic segmentation maps, enabling effective supervision for long-tail categories. Extensive experiments on both the open-pit mine dataset and the nuScenes dataset demonstrate that our method significantly outperforms existing state-of-the-art approaches.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (2) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[Unpaired RGB-Thermal Gaussian-Splatting Using Visual Geometric Transformers](https://arxiv.org/abs/2606.05491)**  
  *Jean Cordonnier, Chenghao Xu, Olga Fink, Malcolm Mielle*  
  `2026-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2606.05491) · [pdf](https://arxiv.org/pdf/2606.05491.pdf)
  > 💡 用VGGT独立估计位姿后Procrustes对齐，实现未配对RGB-热成像的多模态3DGS渲染，兼顾热像合成与RGB保真。

  <details><summary>Abstract</summary>

  Multi-modal novel view synthesis (NVS) combining RGB and thermal imagery enables precise 3D scene reconstruction with visual and thermal information. However, existing methods typically rely on precisely calibrated RGB-thermal image pairs or stereo setups, limiting scalability and practical deployment. To address this, we introduce a framework for unpaired RGB-thermal NVS that leverages VGGT, a 3D feed-forward transformer architecture, to independently estimate camera poses for each modality. The pose sets are then aligned using the Procrustes algorithm with a cross-modal feature matcher, enabling joint registration without paired calibration. Building on this alignment, we further propose a multi-modal 3D Gaussian Splatting approach that learns directly from unpaired RGB and thermal images. Experiments on diverse scenes demonstrate that our method achieves competitive performance in thermal view synthesis while maintaining RGB fidelity. Moreover, we show that existing reconstruction approaches can produce modality-specific reconstructions that lack cross-modal consistency. We thus introduce a benchmarking framework to rigorously evaluate both per-modality image synthesis and the multi-modal coherence of reconstructed scenes.

  </details>


- **[$\text{VG}^2$GT: Voxel-Gaussian Splatting Visual Geometry Grounded Transformer](https://arxiv.org/abs/2606.01573)**  
  *Yibin Zhao, Yihan Pan, Jun Nan, Wenli Yang, Liwei Chen, Jianjun Yi*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.01573) · [pdf](https://arxiv.org/pdf/2606.01573.pdf)
  > 💡 利用冻结视觉基础模型与多尺度可微分体素模块，从体素特征回归高斯原语，实现几何准确

  <details><summary>Abstract</summary>

  Gaussian splatting has shown strong potential for 3D reconstruction and novel view synthesis. However, most existing methods require accurate camera parameters and per-scene optimization, while feed-forward methods with pixel-aligned Gaussian primitives often suffer from artifacts and non-uniform primitives. In this paper, we propose $\text{VG}^2$GT, a Voxel-Gaussian Splatting Visual Geometry-Grounded Transformer. $\text{VG}^2$GT leverages a frozen pretrained visual foundation model (VFM), incorporates a multi-scale differentiable voxel module to enhance geometric understanding, and directly splits and regresses Gaussian primitive parameters from voxel features. During training, depth maps are supervised through stochastic solid volume rendering, enabling geometrically accurate Gaussian scene reconstruction while keeping the visual foundation model fully frozen. This design enables $\text{VG}^2$GT to be seamlessly plugged into any patch-feature-based VFM, while substantially reducing the required training cost. $\text{VG}^2$GT outperforms current state-of-the-art methods on widely used DTU, Replica, TAT, and ScanNet datasets.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (1) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[Geometry Gaussians: Decoupling Appearance and Geometry in Gaussian Splatting](https://arxiv.org/abs/2606.05124)**  
  *Hongyu Zhou, Zorah Lähner*  
  `2026-06-03` · `cs.GR` · [abs](https://arxiv.org/abs/2606.05124) · [pdf](https://arxiv.org/pdf/2606.05124.pdf)
  > 💡 针对3DGS难以同时建模纹理与几何，通过引入几何不透明度参数和透明度优化管线解耦外观与几何，提升渲染与几何质量，尤其适用透明物体场景。

  <details><summary>Abstract</summary>

  After the success of 3D Gaussian Splatting (3DGS) for novel view synthesis, many works have explored how to also use it for geometric surface representation. However, extracting accurate geometric information directly from 3DGS remains challenging and can often reduce the appearance rendering quality. In this work, we show that 3DGS in its default form is inheritedly unsuited to represent texture and geometry at the same time, by training with complete ground-truth texture and geometry information. We also propose a simple solution by applying a single additional geometry opacity parameter to each splat, together with an optional transparency-curated optimization pipeline. Our experiments, both with ground-truth and vision foundation model geometric input, show that this change leads to improved rendering and geometry performance on a wide variety of dataset, and especially complex scenes with transparent objects benefit significantly from our method.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
