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
| 1 | **Survey & Benchmark** | 62 | **+3** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 238 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 30 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 46 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 23 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 32 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 37 | **+2** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 12 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 13 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 4 | **+1** | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 14 | **+1** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 23 | **+1** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-16 (UTC) — 10 new paper(s)

<details><summary><b>Survey & Benchmark</b> (3) · <a href="topics/survey.md">full list →</a></summary>

- **[MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods](https://arxiv.org/abs/2606.16638)**  
  *Robert Langendörfer, Markus Hillemann, Markus Ulrich*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16638) · [pdf](https://arxiv.org/pdf/2606.16638.pdf)
  > 💡 针对工业物体3D重建评估缺乏真实数据集的问题，提出MVM-IOD基准，评估多种方法并发现前馈方法在分布外图像上效果不佳。

  <details><summary>Abstract</summary>

  3D object reconstruction, and camera pose estimation in industrial applications are challenging tasks, as errors are costly while the computation time is often limited. The complexity of typical industrial objects further complicates these tasks. Most of the existing datasets in this context do not depict realistic industrial scenarios. Therefore, we introduce the Machine Vision Metrology Industrial Object Dataset (MVM-IOD). Images of typical industrial objects are captured systematically, by moving a camera, mounted at the end effector of an industrial robot arm, on a hemisphere around the objects. MVM-IOD contains reference camera poses and reference 3D point clouds, the acquired RGB images of 9 objects and 2 background choices resulting in 18 scenes, which allows evaluation of all image based methods that compute a 3D reconstruction, camera poses, or novel views of a scene. Based on MVM-IOD, we extensively evaluate current SOTA 3D reconstruction and camera pose estimation methods, such as Structure from Motion, Multi-View Stereo, recent feed forward methods (Visual Geometry Grounded Transformer, π3), and 2D Gaussian Splatting and report our findings as a baseline for future research. The experiments show that capture setups like ours generate out-of distribution images for feed forward methods, leading to suboptimal point clouds and camera poses. However, these out-of-distribution images can be shifted closer to the training distribution by applying simple preprocessing steps. Consequently, in certain industrial applications, feed forward methods should be used with caution.

  </details>


- **[Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing](https://arxiv.org/abs/2606.16168)**  
  *Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Kunyang Huang, Wenbo Chu, Keqiang Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16168) · [pdf](https://arxiv.org/pdf/2606.16168.pdf)
  > 💡 采用频率感知隐式高斯泼溅解耦高低频信息，结合物理散射重归一化，实现单图像去雾SOTA。

  <details><summary>Abstract</summary>

  Single image dehazing continues to be hindered by the loss of high-frequency details and the difficulty of accurate physical scattering modeling. To address these issues, we propose Fi-Gaussian, a frequency-aware implicit Gaussian splatting network for single image dehazing. Unlike explicit rendering methods that rely on 3D point clouds, our method employs implicit Gaussian splatting to adaptively model the underlying distribution of clear images as a continuous representation in 2D feature space. The core of the network is a frequency-aware implicit Gaussian splatting module, which decouples low-frequency structural information and high-frequency texture information in the frequency domain and then performs adaptive Gaussian aggregation with complex-valued weights to recover fine details. In addition, a physics-driven scattering renormalization mechanism is introduced to estimate the transmission map and atmospheric light under the guidance of implicit Gaussian priors. Extensive experiments on multiple benchmark datasets demonstrate that Fi-Gaussian achieves state-of-the-art quantitative performance and produces visually superior dehazed results, validating the effectiveness of implicit Gaussian splatting for low-level vision tasks.

  </details>


- **[SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction](https://arxiv.org/abs/2606.15659)**  
  *Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao*  
  `2026-06-14` · `cs.CV` · [abs](https://arxiv.org/abs/2606.15659) · [pdf](https://arxiv.org/pdf/2606.15659.pdf)
  > 💡 通过共享FLAME绑定的高斯表示和多阶段重建，解决前馈与优化器

  <details><summary>Abstract</summary>

  High-quality 4D head avatars from one or a few source portraits are central to telepresence, AR/VR, and digital-human interaction. 3D Gaussian Splatting (3DGS) has emerged as the dominant representation, with two complementary regimes (generalizable feed-forward predictors and per-subject refiners) maturing in parallel. However, existing feed-forward predictors are trained on a single dataset family with a hard-coded source count, inheriting the corresponding domain bias. Per-subject refiners require 300K--600K iterations and rely on adaptive densification that destroys upstream Gaussian layouts, preventing the two regimes from sharing a representation end-to-end. To bridge both regimes we propose SpatialAvatar-0 on a shared FLAME-mesh-bound Gaussian representation: a feed-forward generator with a parameter-free K-source mean-pool and a monocular-temporal to multi-view-spatial two-phase schedule that anchors against identity-prior collapse onto the smaller multi-view set. We further introduce a 10K-iter layout-preserving per-subject refinement loop that freezes the FLAME-binding and Gaussian count and replaces densification with a three-component anti-spike regularization. On VFHQ/HDTF cross-domain zero-shot we surpass the in-domain leader GAGAvatar by +1.5 dB PSNR despite never training on either test domain, and on the SplattingAvatar monocular benchmark we lead every reported metric, surpassing the 300K-iter GeoAvatar by +1.3 dB PSNR at up to 60x shorter per-subject schedule than common SOTA baselines. Website: https://spatialwalk.github.io/SpatialAvatar-0.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278)**  
  *Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16278) · [pdf](https://arxiv.org/pdf/2606.16278.pdf)
  > 💡 针对可编辑3DGS仿真视频与现实差距，提出RealityBridge，利用多模态控制和门控网络改善伪影、光照和

  <details><summary>Abstract</summary>

  Long-tail hazardous scenarios are essential for safety-oriented autonomous driving, yet they are difficult to collect and reproduce at scale. Editable 3D Gaussian Splatting (3DGS) simulation offers a promising alternative by reconstructing real driving scenes and supporting controllable scene editing. However, edited 3DGS-rendered videos still suffer from a significant Sim-to-Real gap, including rendering artifacts, degraded foreground assets, inconsistent illumination, and temporal flickering. Existing restoration and video generation methods are insufficient for this task, as they often fail to jointly repair 3DGS-specific artifacts, improve visual realism, and ensure temporal consistency. To fill this gap, we propose RealityBridge, a structure-preserving and asset-aware Sim-to-Real framework for edited 3DGS driving videos. RealityBridge uses multimodal controls, including rendered videos, foreground masks, edge maps, and semantic masks, together with a lightweight GateNet for adaptive condition allocation across backbone layers. We further construct targeted training data and introduce autoregressive long-video training with reward-guided post-training to improve restoration quality, temporal stability, and hallucination suppression. Extensive experiments on internal and public driving datasets show that RealityBridge outperforms existing methods in artifact removal, illumination harmonization, and long-sequence temporal consistency.

  </details>


- **[EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848)**  
  *Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen*  
  `2026-06-14` · `cs.CV` · [abs](https://arxiv.org/abs/2606.15848) · [pdf](https://arxiv.org/pdf/2606.15848.pdf)
  > 💡 提出了EmoZone-Talker，利用区域语义解耦AU编码，实现音频驱动3DGS说话头的精细表情控制，提升上脸精度和时间一致性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has shown strong potential for high-fidelity talking head synthesis. However, enabling fine-grained, interpretable, and editable facial expression control remains fundamentally challenging due to intrinsic conflicts between speech-driven facial dynamics and explicit expression signals. Existing methods rely on implicit multimodal fusion, leading to spatial entanglement and temporal instability. We present EmoZone-Talker, a novel framework that reformulates audio-driven facial animation as a structured spatial-temporal coordination problem under cross-modal conflicts. Our approach introduces an explicit spatial disentanglement and temporal dynamics modeling of facial motion. Specifically, we propose Synergy Zones with Prioritized Attention Bias (SZ-PAB) to explicitly decouple modality contributions via region-wise constraints guided by anatomical priors, and a Channel-Independent Temporal AU Encoder (CIT-AE) to model temporally coherent AU dynamics. By integrating these representations into 3D Gaussian deformation, EmoZone-Talker enables precise and interpretable control over facial expressions. Extensive experiments demonstrate that our method improves expression controllability and realism, with notable gains in upper-face accuracy and temporal coherence, while preserving high rendering quality and accurate lip synchronization. Code will be publicly released to facilitate reproducibility and further research.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (2) · <a href="topics/rendering.md">full list →</a></summary>

- **[Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence](https://arxiv.org/abs/2606.16566)**  
  *Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16566) · [pdf](https://arxiv.org/pdf/2606.16566.pdf)
  > 💡 针对3DGS翘曲分歧致GPU低效，提出基于瓦片局部

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has significantly advanced real-time novel view synthesis by representing scenes as dense collections of anisotropic 3D Gaussian primitives. However, the irregular spatial distribution of Gaussians often leads to poor GPU utilization, as warp divergence and redundant computation degrade rendering performance. To address this, we present Local-GS, a warp-coherent rendering paradigm that, organizes Gaussian primitives with respect to SIMT (Single Instruction, Multiple Threads) execution boundaries rather than scene geometry. Specifically, we propose three warp-coherent stages: a hoisting stage that precomputes shared parameters at tile level, a culling stage that discards warps with no contribution, and a blending stage that replaces per-pixel branching with a uniform instruction stream. Across extensive benchmarks on multiple datasets, Local-GS improves efficiency without compromising quality. As a plug-and-play optimization, it provides additional performance gains to all tested baselines, culminating in a $7.76\times$ speedup on Deep Blending scenes.

  </details>


- **[PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation](https://arxiv.org/abs/2606.16232)**  
  *Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou*  
  `2026-06-15` · `cs.RO` · [abs](https://arxiv.org/abs/2606.16232) · [pdf](https://arxiv.org/pdf/2606.16232.pdf)
  > 💡 将3DGS模型转化为凸多面体覆盖，压缩并保证安全，实现资源受限下的实时避障导航。

  <details><summary>Abstract</summary>

  Obstacle avoidance is essential for safe navigation and motion planning. Recent radiance field reconstruction methods enable object detection and modeling with high fidelity, but remain too memory- and compute-intensive for on-board perception-based path planning. To address these limitations, we propose PolyMerge to convert a large, photorealistic 3D Gaussian Splatting (3DGS) model of a scene into a lightweight representation of convex polytopes whose union provably over-approximates all obstacles in the original 3DGS model. PolyMerge tunes the polytope count to trade off conservativeness and compute cost, and integrates with control barrier functions (CBFs) to plan collision-free paths. We showcase PolyMerge in simulation and hardware experiments on a Crazyflie drone, which uses PolyMerge to compute and follow safe trajectories in real time under severe onboard compute constraints, outperforming baselines in speed while guaranteeing safety. For our code and videos, visit https://athlon76.github.io/PolyMerge-website/.

  </details>


</details>

<details><summary><b>Relighting / Material / BRDF</b> (1) · <a href="topics/relighting.md">full list →</a></summary>

- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159)**  
  *Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16159) · [pdf](https://arxiv.org/pdf/2606.16159.pdf)
  > 💡 提出CGS-Retinex，融合连续高斯溅

  <details><summary>Abstract</summary>

  Low-light image enhancement aims to recover clear images from low-illumination observations and is crucial for high-level downstream vision tasks. However, existing methods frequently encounter color distortion and structural artifacts when balancing global smooth illumination adjustment and local high-frequency detail recovery. To address these issues, we propose CGS-Retinex as the first low-light image enhancement framework based on explicit-implicit joint modeling. Our framework deeply integrates continuous Gaussian splatting with Retinex theory. Specifically, we represent the image grid as a continuous parameter field and propose a continuous Gaussian renderer to estimate the spatially continuous global illumination distribution. This approach fundamentally eliminates grid artifacts caused by discrete Gaussian sampling. Furthermore, we introduce an implicit neural representation to model reflectance independently. We leverage shallow high-frequency features to guide the network in accurately reconstructing degraded texture details. Within the Retinex framework, we incorporate physics-inspired brightness consistency constraints and illumination smoothness regularization to enable explicit illumination and implicit reflectance to maintain proper exposure and achieve high-fidelity recovery of high-frequency structures and colors. Extensive experiments demonstrate that CGS-Retinex significantly suppresses dark-region noise and overexposure while achieving exceptional high-frequency structural fidelity and color restoration by precisely decoupling illumination and texture. This work establishes a novel continuous physical representation paradigm for low-light image enhancement.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (1) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163)**  
  *Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16163) · [pdf](https://arxiv.org/pdf/2606.16163.pdf)
  > 💡 用2D高斯泼溅零样本去雾，嵌入大气散射模型实现几何解耦，以最少参数达到SOTA。

  <details><summary>Abstract</summary>

  Existing single image dehazing methods are often constrained by computational redundancy in pixel-level optimization and the lack of physical interpretability in implicit neural networks. These limitations hinder the balance between representation efficiency and reconstruction fidelity. To address these issues, we propose Dehaze-GaussianImage, the first zero-shot framework that introduces 2D Gaussian Splatting (2DGS) into the image dehazing domain to break the traditional pixel-grid processing paradigm. Distinct from static convolutional neural networks (CNNs) or Transformers, our approach models hazy images as continuous and dynamically evolvable anisotropic Gaussian fields. Specifically, we propose a novel reconstruction-decoupling zero-shot learning strategy that embeds the atmospheric scattering model into the Gaussian parameter space. This strategy drives Gaussian primitives to adaptively split, clone, and prune during optimization, achieving geometric-level decoupling of the transmission medium and clear textures. Furthermore, explicit structure-preserving constraints are introduced to suppress artifacts commonly caused by traditional physical priors. Experimental results demonstrate that the proposed method achieves state-of-the-art (SOTA) performance in a fully unsupervised manner with minimal parameters, highlighting the potential of explicit Gaussian representation for low-level vision tasks.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (1) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[TurboGS: Accelerating 3D Gaussian Splatting via Error-Guided Sparse Pixel Sampling and Optimization](https://arxiv.org/abs/2606.15924)**  
  *Zheng Dong, Daifei Qiu, Pinxuan Dai, Ke Xu, Jiamin Xu, Lili He, Rynson W. H. Lau, Weiwei Xu*  
  `2026-06-14` · `cs.CV` · [abs](https://arxiv.org/abs/2606.15924) · [pdf](https://arxiv.org/pdf/2606.15924.pdf)
  > 💡 通过错误引导稀疏采样和结构感知损失优化冗余像素，TurboGS在单GPU上100秒内实现10倍加速且保持高质量渲染。

  <details><summary>Abstract</summary>

  Consumer-level applications require fast optimization of 3D Gaussian Splatting (3DGS) with high-fidelity novel view rendering. However, existing 3DGS acceleration approaches still incur substantial computation on redundant pixels while sacrificing fine details. In this paper, we present TurboGS, an error-guided training framework that accelerates 3DGS by concentrating optimization on perceptually informative pixels. TurboGS is built upon four core components: (1) a tile-wise sparse pixel sampling, which, driven by multi-view reconstruction errors during training, prioritizes challenging regions and skips well-reconstructed ones to avoid redundant gradient computation; (2) a tile-wise structure-aware loss with sparse Normalized Cross-Correlation, which provides sparse yet effective supervision to preserve fine details and stabilize training; (3) an error-driven Gaussian density control strategy, which dynamically allocates model capacity and removes redundant primitives; and (4) a tailored hybrid optimizer that couples Hessian-informed updates with Adam moment damping to stabilize and improve convergence under sparse supervision. Experiments on standard benchmarks demonstrate that TurboGS can deliver on par or superior rendering quality within 100 seconds on a single RTX 5090 GPU card (up to 10x training speedup over vanilla 3DGS).

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
