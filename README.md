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
| 1 | **Survey & Benchmark** | 78 | **+1** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 272 | **+3** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 41 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 64 | **+3** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 36 | **+2** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 37 | **+2** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 55 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 16 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | **+1** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 7 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 20 | **+1** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 14 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 26 | **+1** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-07 (UTC) — 16 new paper(s)

<details><summary><b>Survey & Benchmark</b> (1) · <a href="topics/survey.md">full list →</a></summary>

- **[PRISM3D: Probabilistic Refinement and Robust Initialization for Physically Consistent Scene Modeling under Extreme Motion Blur](https://arxiv.org/abs/2607.03855)**  
  *Gopi Raju Matta, Reddypalli Trisha, Vemunuri Divya Madhuri, Kaushik Mitra*  
  `2026-07-04` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03855) · [pdf](https://arxiv.org/pdf/2607.03855.pdf)
  > 💡 针对极端运动模糊，提出鲁棒初始化和概率物理耦合优化，首次实现3D高斯泼溅直接重建。

  <details><summary>Abstract</summary>

  We address the inverse problem of blind 3D scene reconstruction from extremely motion-blurred images, a scenario where traditional Structure-from-Motion (SfM) pipelines fail. Existing approaches typically circumvent this bottleneck by relying on impractical sharp-image supervision. In this work, we introduce PRISM3D, a unified framework enabling robust reconstruction directly from severely degraded inputs. To overcome the lack of a reliable starting point, we propose a Robust Initialization strategy utilizing deep dense tracking method (VGGSfM) to recover global topology where feature matching fails. To the best of our knowledge, we are the first to effectively leverage this paradigm to bootstrap 3D Gaussian Splatting from extreme motion blur. However, while robust, this initialization yields sparse and noisy geometry that causes deterministic optimization to diverge. To resolve this, we propose a coupled solution driven by probability and physics: we adopt a probabilistic formulation for geometric densification via Markov Chain Monte Carlo (MCMC) to robustly populate the sparse priors, while simultaneously modeling physical image formation via continuous Bezier Trajectories. Furthermore, while PRISM3D establishes a highly robust standalone pipeline, the availability of complementary event streams offers an opportunity to push the reconstruction fidelity further. To exploit this, we introduce PRISM3D-E, a multi-modal (RGB + Events) extension that seamlessly integrates high-temporal-resolution events as structural priors to maximize geometric recovery. Because existing datasets lack paired event streams under such severe degradation, we concurrently contribute the PRISM3D-E Benchmark to facilitate rigorous evaluation. Extensive experiments demonstrate that both our standalone RGB framework and its multi-modal extension establish new state-of-the-art performance.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (3) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243)**  
  *Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki*  
  `2026-07-06` · `cs.CV` · [abs](https://arxiv.org/abs/2607.05243) · [pdf](https://arxiv.org/pdf/2607.05243.pdf)
  > 💡 提出GUSH3R前馈框架，从单目视频同时重建动态人体和静态场景为

  <details><summary>Abstract</summary>

  Reconstructing dynamic human-scene environments from monocular videos is a challenging problem that requires jointly modeling scene geometry, camera motion, and non-rigid human dynamics while enabling photorealistic rendering. Recent feed-forward methods can efficiently predict geometry, but they are often limited to non-photorealistic representations such as point clouds and meshes, or they fail to handle non-rigid objects, particularly dynamic humans. To fill this gap, we present GUSH3R (Gaussian-Unified Scene Human 3D Reconstruction), a feed-forward framework for online dynamic human-scene reconstruction. From a monocular human-scene video, our method reconstructs dynamic humans (everyone) and static scenes (everywhere) in a single forward pass (all at once) as 3D Gaussian Splatting (3DGS) primitives (as gaussians), which are geometrically consistent and capable of novel view synthesis. Experiments on monocular human-scene datasets demonstrate that our approach achieves competitive novel view synthesis quality while significantly improving inference efficiency compared to optimization-based methods.

  </details>


- **[DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting](https://arxiv.org/abs/2607.04761)**  
  *Yimo Wang, Bin Kang, Shuojue Yang, Yueming Jin*  
  `2026-07-06` · `cs.CV` · [abs](https://arxiv.org/abs/2607.04761) · [pdf](https://arxiv.org/pdf/2607.04761.pdf)
  > 💡 提出几何

  <details><summary>Abstract</summary>

  Real-time, text-promptable 4D reconstruction is indispensable for autonomous surgical interaction. Severe misalignment between semantic meaning and physical anatomy still persists, largely because existing solutions integrate Vision-Language Models into deformable fields via a rigid coupling scheme that tightly binds semantic features to geometric warping. In this paper, we propose DeGenseGS, Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting, a novel framework that independently models semantic evolution and geometric deformation. Specifically, we propose a HexPlane-based spatiotemporal entanglement module that uses shared kinematic latents to synchronize semantic mutations with scene dynamics, while explicitly disentangling semantic updates from geometric deformation. To further ensure robustness against reconstruction artifacts, we devise a Rasterization-Native Semantic Extraction mechanism that infers semantics from topologically continuous feature maps. Additionally, we incorporate an angular-aligned optimization strategy that conforms to the native hyperspherical latent space, thereby preventing semantic distortion. Extensive evaluations on the CholecSeg8k and EndoVis18 datasets demonstrate that DeGenseGS achieves state-of-the-art performance. Our framework yields enhanced geometric completeness and robust semantic-anatomic alignment, enabling spatially continuous segmentation despite drastic tissue deformation and topological transitions.

  </details>


- **[TemporalGS: Training-Free Plug-and-Play Acceleration for 3D Gaussian Splatting Rendering via Temporal Priors](https://arxiv.org/abs/2607.03390)**  
  *Yuhongze Zhou, Zihao Yang, Xinxin Zuo, Juwei Lu*  
  `2026-07-03` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03390) · [pdf](https://arxiv.org/pdf/2607.03390.pdf)
  > 💡 利用时间先验动态剔除与选择性渲染，无训练即插即用加速3DGS，提升渲染速度达1.48倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized novel-view synthesis with its fast and high-fidelity rendering. However, rendering at high FPS and low latency across various scenes remains a challenge, especially when large amounts of 3D Gaussian ellipsoids appear in the scene. To address this issue, we introduce TemporalGS, to the best of our knowledge, the first training-free plug-and-play algorithmic approach to accelerate 3DGS rendering without any post-training or post-processing, implemented on top of tile-based software rasterization. The key idea is that, instead of rendering frames independently as 3DGS, we leverage the temporal priors, represented by novel geometry and appearance buffers, etc., to reduce redundancy of Gaussian preprocessing, sorting, and rasterization operations of consecutive frames. Specifically, we propose two acceleration strategies: (1) temporal dynamic culling, which filters out Gaussians that contribute less to current frame rendering; (2) selective rendering, which renders only a small portion of tiles that cannot be approximated by the temporal priors. By adapting and interleaving these two strategies, TemporalGS yields a simple but effective plug-and-play solution for 3DGS rendering speed-up without any training. Extensive experiments show that TemporalGS achieves comparable or even better performance compared to existing state-of-the-art post-training or post-processing-based 3DGS rendering acceleration approaches. TemporalGS can significantly enhance the rendering speed of various 3DGS methods, achieving up to $1.48\times$ acceleration, while maintaining competitive rendering quality. We further extend our TemporalGS to hardware rasterization-based 3DGS to show the portability of our algorithm.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction](https://arxiv.org/abs/2607.04256)**  
  *Badrinath Singhal, Srihari K G, Sreehari Iyer, Ankit Dhiman, Venkatesh Babu Radhakrishnan*  
  `2026-07-05` · `cs.CV` · [abs](https://arxiv.org/abs/2607.04256) · [pdf](https://arxiv.org/pdf/2607.04256.pdf)
  > 💡 前馈3D高斯重建存在冗余问题，利用局部纹理信息进行感知剪枝，在不需微调下控制高斯数量并保持质量。

  <details><summary>Abstract</summary>

  Current feed-forward 3D reconstruction methods predict pixel aligned Gaussian primitives, resulting in highly redundant representations. A natural solution is to prune the redundant Gaussians, but naive pruning introduces severe artifacts and often requires inference time fine-tuning, breaking the feed-forward paradigm. Based on previous works, high frequency regions require more Gaussian primitives, while low frequency regions can be represented with significantly fewer primitives. Motivated by this, we propose a novel approach to explicitly control the number of Gaussians by leveraging local texture information. Our approach achieves this through three key components: (1) texture estimation to capture spatial variation in scene detail, (2) texture-aware pruning that removes redundant Gaussians from low frequency regions, and (3) an adaptive Gaussian head that predicts the modified attributes of the retained primitives without breaking the feed-forward paradigm. Experiments on RE10K, ACID, DL3DV, Tanks and Temples, and DTU demonstrate the effectiveness of our approach, while ablation studies validate the contributions of its key components.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (3) · <a href="topics/generation.md">full list →</a></summary>

- **[Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.04770)**  
  *Davide Jannussi, Stefano Carlo Lambertenghi, Constantin Carste, Andrea Stocco*  
  `2026-07-06` · `cs.SE` · [abs](https://arxiv.org/abs/2607.04770) · [pdf](https://arxiv.org/pdf/2607.04770.pdf)
  > 💡 利用Gaussian Splatting将真实驾驶记录重建为可交互CARLA场景，减少仿真与真实视觉差距并提升行为相似性。

  <details><summary>Abstract</summary>

  Simulation-based testing enables safe and repeatable evaluation of autonomous driving systems, but its effectiveness is limited by the gap between synthetic simulator outputs and real-world camera observations. To address this problem, we present Cam2Sim, a tool that transforms real-world driving recordings into playable CARLA simulation scenarios. Starting from camera images and poses, Cam2Sim reconstructs road geometry, ego trajectories, parked vehicles, and simulation assets, and augments the reconstructed environment with Gaussian Splatting to render camera observations that resemble the original recording. The framework supports ROS-based data extraction, parked-vehicle detection, OpenStreetMap-based map generation, CARLA scenario construction, Gaussian Splatting training, trajectory replay, and closed-loop execution with a system under test. We validate Cam2Sim on a real-world urban-driving scenario with a camera-based end-to-end driving model, comparing reconstruction quality, image-generation quality, and closed-loop behavior against both a simulation-only baseline and the real-world target. Results show that Gaussian-Splatting-based rendering reduces the visual gap with respect to standard simulator rendering and improves behavioral similarity to the real-world reference runs. The artifact is publicly available at https: //github.com/ast-fortiss-tum/cam2sim, and a screencast showing the tool is available at https://youtu.be/KmZ74l1__lI

  </details>


- **[MACRO: Training-free Multi-plane Attention for Closeup Render Optimization](https://arxiv.org/abs/2607.03875)**  
  *Nitzan Hodos, Roy Amoyal, Lior Fritz, Ianir Ideses, Sagie Benaim, Netalee Efrat*  
  `2026-07-04` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03875) · [pdf](https://arxiv.org/pdf/2607.03875.pdf)
  > 💡 针对3DGS近距离渲染尺度失配问题，提出多平面注意力训练-free优化方法，实现高质量渲染并创立新基准。

  <details><summary>Abstract</summary>

  Close-up rendering, zooming into a scene well beyond any training camera, is important for virtual production and interactive 3D content, yet remains an open challenge. 3D Gaussian splatting (3DGS) enables high-fidelity, real-time novel view synthesis, but its rendering quality degrades at close range. Recent diffusion-based methods that enhance the rendering by conditioning on reference images from the training set produce significant artifacts in this setting. We analyze this failure and identify its root cause: the scale gap between the close-up and reference views. We show that the features in reference-conditioned enhancement models are not scale-invariant, causing cross-view attention to retrieve incorrect correspondences when the same content appears at different scales, and that this mismatch cannot be corrected in latent space because the VAE encoder is not scale-equivariant. Building on this analysis we introduce MACRO, Multi-plane Attention for Closeup Render Optimization, a training-free method for high-quality close-up novel view synthesis from 3DGS. MACRO resolves the scale gap by leveraging the scene's known 3D structure: it decomposes the close-up into depth planes, crops and resizes references in image space to match the scale of each plane before encoding, and applies a depth-aware attention mask so each token attends only to scale-matched references. The method requires no architectural changes or additional training. We further contribute two new close-up novel view synthesis benchmarks, the first standardized evaluation protocol for this setting, and demonstrate state-of-the-art results on both, outperforming existing 3DGS and diffusion-based methods on both reconstruction and perceptual metrics. Project page: https://nitzanhod.github.io/MACRO

  </details>


- **[CGGS: Consistency-Augmented Geometric Gaussian Splatting for Ego-centric 3D Scene Generation](https://arxiv.org/abs/2607.03819)**  
  *Zhenyu Sun, Xiaohan Zhang, Qi Liu, Huan Wang*  
  `2026-07-04` · `cs.GR` · [abs](https://arxiv.org/abs/2607.03819) · [pdf](https://arxiv.org/pdf/2607.03819.pdf)
  > 💡 针对第一人称视角下几何失真与视角不一致，提出一致性增强扩散模型和互信息深度损失优化3D高斯，生成高质量文本驱动场景。

  <details><summary>Abstract</summary>

  Challenges remain in ego-centric 3D scene generation due to limited view overlap and the dominant influence of individual perspectives on scene interpretation. These factors hinder the creation of viewpoint-consistent and semantically aligned visual content, as well as the construction of accurate geometric structures. In this paper, we propose CGGS, a text-to-3D framework aiming to enhance 3D-content-awareness and address geometric distortions in ego-centric scene generation. Firstly, the Ego-centric Generator is proposed by fine-tuning a Multi-View Latent Diffusion Model with consistency-augmented loss to generate consistent, high-fidelity 2D content aligned with textual descriptions. Then, Layout Decorator leverages optical flow and point-track correspondence to estimate depth, therefore producing dense point clouds as coarse layouts from the ego-centric 2D priors. Building on this initialization, Geometric Refiner is proposed to enhance 3D Gaussian reconstruction via an entropy-based Mutual Information Depth Loss (MID) combined with a hierarchical optimization scheme for improving visual quality and geometric structure. Comprehensive experiments demonstrate that \textcolor{softred}{CGGS} outperforms previous methods in generating coherent and accurate text-driven 3D scenes. Project page: https://cggs-26.github.io/cggs26/.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (2) · <a href="topics/editing.md">full list →</a></summary>

- **[WildSplat: Feedforward Gaussian Splatting from Unposed In-the-Wild Images](https://arxiv.org/abs/2607.05347)**  
  *Xiyu Zhang, Jingyu Zhuang, Hongjia Zhai, Zizheng Yan, Jinwei Chen, Guofeng Zhang, Qingnan Fan*  
  `2026-07-06` · `cs.CV` · [abs](https://arxiv.org/abs/2607.05347) · [pdf](https://arxiv.org/pdf/2607.05347.pdf)
  > 💡 为处理野外图像光照变化，提出双分支解耦几何与外观的3DGS框架，实现前馈式新视角合成与外观编辑。

  <details><summary>Abstract</summary>

  While feedforward 3D reconstruction excels at efficient novel view synthesis, it typically falters when faced with scenes under varying illumination. To this end, we introduce WildSplat, the first feedforward 3D Gaussian Splatting framework capable of appearance-conditioned novel-view synthesis for unposed in-the-wild images. To handle inconsistent photometric conditions, we propose a dual-branch architecture that explicitly decouples geometry from appearance. The geometry branch extracts an appearance-invariant 3D structure and jointly predicts camera poses. To govern the rendering appearance, the appearance branch injects target appearance cues into the content features via a globally pre-modulated cross-attention mechanism. To further prevent feature entanglement, we introduce a joint multi-reference training strategy that stabilizes the training process. Extensive experiments show that WildSplat surpasses existing optimization-based and feedforward methods, achieving state-of-the-art performance in in-the-wild novel view synthesis and appearance editing from sparse inputs in a single forward pass.

  </details>


- **[Semantic-Guided Progressive Object Removal with Gaussian Splatting](https://arxiv.org/abs/2607.04144)**  
  *Xianliang Huang, Chen Xiao, Yuanxiang Ni, Guanming Liu, Mingkai Liu, Dikai Fan, Xiao Liu, Hao Zhang*  
  `2026-07-05` · `cs.RO` · [abs](https://arxiv.org/abs/2607.04144) · [pdf](https://arxiv.org/pdf/2607.04144.pdf)
  > 💡 利用语义引导块匹配和区域逐步细化，解决了高斯泼溅中复杂几何纹理的物体去除难题，提升了感知质量与一致性。

  <details><summary>Abstract</summary>

  Removing unwanted objects from reconstructed 3D scenes is an important task in computer vision, supporting applications in AR/VR, robotics, and digital content creation. Existing methods typically complete the entire masked region in a single step and without effectively utilizing semantic information from other views, leading to difficulties in handling complex geometric details and textures. In this work, we propose a novel framework that integrates Semantic-guided Block Matching (SBM) and Region-Wise Progressive Refinement (RPR) for high-quality 3D object removal. First, we leverage DINOv2 to encode semantic guidance from multi-view observations, and the best match tokens are decoded to complete missing regions in the target view while maintaining cross-view consistency. Second, we introduce a RPR strategy that segments the target mask into multiple subregions and selectively refines those with poor visual quality. Our method is built upon Gaussian Splatting, ensuring high-fidelity scene reconstruction with efficient computation. Experimental results demonstrate that our approach outperforms existing Gaussian-based methods in terms of perceptual quality and coherence in 3D object removal.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (2) · <a href="topics/compression.md">full list →</a></summary>

- **[Real-Time LiDAR Gaussian Splatting SLAM](https://arxiv.org/abs/2607.04127)**  
  *Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu*  
  `2026-07-05` · `cs.CV` · [abs](https://arxiv.org/abs/2607.04127) · [pdf](https://arxiv.org/pdf/2607.04127.pdf)
  > 💡 将G-ICP配准与球形光栅化高斯建图紧耦合，利用LiDAR几何先验优化地图并实时反馈提升跟踪鲁棒性，实现86.78% F-score的实时SLAM。

  <details><summary>Abstract</summary>

  We present a real-time LiDAR-based framework for Gaussian Splatting SLAM that tightly couples fast G-ICP registration with spherical rasterization-based dense mapping for large-scale sequences. Leveraging LiDAR geometry rather than appearance, we reuse tracking-estimated local covariances to initialize Gaussians with range-aware scales and to derive surface normals for geometry-aware map optimization. We further introduce a covariance-derived geometry score that measures local complexity and drives pruning in planar regions and selective densification in structurally rich areas, while optimized Gaussians and LiDAR-specific confidence cues are fed back to improve tracking robustness. On the Newer College dataset, our method achieves an F-score of 86.78\% using purely online trajectories at real-time speed ($>$20 FPS), and additional experiments on other datasets confirm its stability and scalability.

  </details>


- **[Provable Pruning for Efficient 3D Gaussian Splatting via Coresets](https://arxiv.org/abs/2607.02721)**  
  *Waseem Mousa, Alaa Maalouf*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.02721) · [pdf](https://arxiv.org/pdf/2607.02721.pdf)
  > 💡 通过敏感性加权子集实现对3DGS的可证明剪枝，在激进压缩下达到SOTA且无需或极少微调。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables high-quality real-time novel-view synthesis, but practical scenes often contain millions of Gaussians, making compression essential for deployment on limited hardware. Existing reduction methods are effective but mostly heuristic: they provide no multiplicative approximation guarantee for the rendered objective, and thus rely heavily on costly post-pruning finetuning to recover quality. We ask a basic question: can a 3DGS scene be provably replaced by a much smaller weighted subset (coreset) while preserving the objective of interest? We first show that, in the unrestricted setting, no non-trivial multiplicative 3DGS coreset exists. We then show that multiplicative guarantees are not impossible, but resolution-dependent. For a prescribed rendering resolution, such as representative views or grids of views/rays, we provide the first weighted coreset construction theorem for 3DGS. The construction samples Gaussians by sensitivity: provable importance scores measuring each Gaussian's role in the full-scene objective. Finally, under explicit validity and log-transmittance stability assumptions, we turn this objective guarantee into a rendering guarantee. Empirically, our method is strongest where deployment needs it most: aggressive compression with no or minimal recovery compute. In prune-only and very short finetuning regimes, it achieves state-of-the-art performance, showing that principled importance estimation can be both theoretically meaningful and practically useful. Open-source code is available at https://github.com/waseem-m/3dgs_provable_coresets.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209)**  
  *Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård*  
  `2026-07-03` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03209) · [pdf](https://arxiv.org/pdf/2607.03209.pdf)
  > 💡 利用3D基础模型初始化位姿和点云，联合深度引导优化与MLP位姿细化，实现无SfM的3分钟高质量3DGS重建。

  <details><summary>Abstract</summary>

  This paper introduces a fast method for high-quality 3D Gaussian Splatting (3DGS) reconstruction without traditional Structure-from-Motion (SfM). The proposed approach leverages 3D Foundation Models (3DFMs) for camera pose and point-cloud initialization, then jointly optimizes both camera poses and Gaussian primitives using a depth-guided loss function. This enables fast convergence even from rough initialization with as few as 50-60 input views. To further improve reconstruction quality in sparse-view scenarios, an MLP-based pose refinement module is introduced alongside depth-guided supervision from the foundation model. Extensive experiments on Mip-NeRF 360, Tanks and Temples, and RobustNeRF demonstrate that the proposed method achieves competitive reconstruction quality (23.61 dB PSNR, 0.19 LPIPS) while reducing training time to approximately three minutes per scene. The proposed method produces ready-to-use 3DGS models at a fraction of the time required by existing pipelines, making it suitable for near real-time applications in robotics, VR, and autonomous navigation.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (1) · <a href="topics/driving.md">full list →</a></summary>

- **[SharpSplat: Edge-Regularized 3D Gaussian Splatting for High Fidelity Urban Building Reconstruction from UAV images](https://arxiv.org/abs/2607.03872)**  
  *Porus Vaid, Shivam Chopra, Vaibhav Kumar*  
  `2026-07-04` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03872) · [pdf](https://arxiv.org/pdf/2607.03872.pdf)
  > 💡 针对3DGS重建建筑边缘模糊问题，提出语义边缘正则化框架，利用SAM边缘监督提升锐利度。

  <details><summary>Abstract</summary>

  Reconstructing high-fidelity 3D building models from UAV imagery is essential for large-scale digital twin development. However, existing 3D Gaussian Splatting (3DGS) techniques often struggle with building facades, failing to capture sharp geometric transitions. To address this, we propose a semantic edge regularization framework that supervises 3DGS to produce crisp architectural boundaries. Our method leverages SAM 3 to generate precise building masks, from which we extract architecturally significant edges. During training, we align rendered image gradients with these extracted edges, forcing the Gaussians to converge into sharp structural geometries. Evaluations across campus environments, dense urban centers, and custom residential datasets demonstrate significant improvements in edge fidelity without requiring architectural modifications to the 3DGS pipeline. Our approach proves robust across diverse building types, roof geometries, and urban densities.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (1) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765)**  
  *Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han*  
  `2026-07-04` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03765) · [pdf](https://arxiv.org/pdf/2607.03765.pdf)
  > 💡 针对稀疏视图表面重建，提出法线引导的高置信深度传播与异常深度边缘感知正则化，显著提升几何质量。

  <details><summary>Abstract</summary>

  3D reconstruction from sparse views is a challenging task in 3D computer vision. Recent studies on 3D Gaussian Splatting (3DGS) have achieved remarkable results with sparse views in novel view synthesis, yet reconstructing high-quality geometric surfaces from sparse views remains a challenge, due to the limited geometry clues and the discreteness of Gaussians. In this paper, we propose a novel 3DGS-based method for high-fidelity surface reconstruction from sparse views. Our key insight is to introduce a normal-guided depth propagation approach, which can extend depth information from high-confidence regions to constrain the depth in low-confidence areas. Additionally, we propose an abnormal depth edge-aware regularization to address depth discontinuities caused by the discreteness of Gaussians. Extensive experiments on DTU and Tanks-and-Temples datasets demonstrate that our method outperforms the state-of-the-art methods in sparse view surface reconstruction. Project page: https://hanl2010.github.io/DP-GS.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (1) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[City-Level 3D Surface Reconstruction with Viewpoint Orientation Partitioning and Scene Completion](https://arxiv.org/abs/2607.03771)**  
  *Liang Han, Wenyuan Zhang, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han*  
  `2026-07-04` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03771) · [pdf](https://arxiv.org/pdf/2607.03771.pdf)
  > 💡 针对大规模场景表面重建难度，提出基于视角方向划分的场景分割法实现精确深度估计与并行计算，并修复缺失区域提升几何质量。

  <details><summary>Abstract</summary>

  Multi-view 3D surface reconstruction is a longstanding challenge in computer vision. Although recent large-scale reconstruction methods based on 3D Gaussian Splatting (3DGS) achieve impressive novel-view synthesis, producing high-quality surfaces over large scenes remains difficult, due to complex geometry, long optimization, and limited memory. In this paper, we propose a novel yet simple partitioning method to efficiently and faithfully reconstruct large-scale scene surfaces. Our key insight lies in a scene partitioning method based on viewpoint orientation. This partitioning approach ensures that views with similar orientations are jointly involved for more accurate depth estimations, leading to precise surface reconstructions and balanced computation on multiple GPUs in parallel. In addition, we propose a strategy to detect and repair missing regions in the initial point cloud caused by sparse viewpoints or insufficient textures, thereby further improving the geometric quality. Extensive experiments on the GauU-Scene, MatrixCity, and UrbanScene3D datasets demonstrate that our method outperforms the state-of-the-art approaches in surface reconstruction for large-scale scenes. Project page: https://hanl2010.github.io/VOP-GS.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
