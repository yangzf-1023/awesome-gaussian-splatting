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
| 1 | **Survey & Benchmark** | 74 | **+1** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 267 | **+5** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 40 | **+2** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 59 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 32 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 35 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 54 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 16 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 17 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 6 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 17 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 14 | **+2** | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 24 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-02 (UTC) — 13 new paper(s)

<details><summary><b>Survey & Benchmark</b> (1) · <a href="topics/survey.md">full list →</a></summary>

- **[Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences](https://arxiv.org/abs/2607.00832)**  
  *Zhenjia Li, Jinrang Jia, Yifeng Shi*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00832) · [pdf](https://arxiv.org/pdf/2607.00832.pdf)
  > 💡 针对单全景图生成可探索3D场景中误差累积和多方向覆盖受限问题，提出全景扩散与视图感知路由及潜在特征适配，直接生成3D高斯场景。

  <details><summary>Abstract</summary>

  A single panorama captures the full visual sphere from one camera center, yet confines users to looking around in place without enabling true scene exploration. Converting a single panorama into a persistent, renderable 3D representation for free-viewpoint navigation has attracted growing interest; existing methods either adopt iterative per-view completion that propagates inpainting results to update the underlying geometry, leading to progressive error accumulation and cumbersome multi-step pipelines, or leverage the temporal consistency priors of video generation models, yet the continuous-trajectory constraint intrinsic to such models limits their flexibility in covering scenes from multiple directions simultaneously. We present Pano2World, which takes a single indoor panorama as input and directly outputs a persistent, explorable 3D Gaussian scene. Given the source panorama, Pano2World first reconstructs a coarse 3D Gaussian proxy and renders it at adaptively sampled nearby poses to obtain geometrically aligned guidance panoramas; a panoramic diffusion model then jointly denoises all target views via View-Aware Attention Routing, where each target view simultaneously receives geometric constraints from its corresponding guidance panorama and global semantic guidance from the source panorama, naturally enforcing cross-view consistency. To avoid the information loss incurred by decoding the multi-view hidden features formed during joint denoising back to the pixel domain via VAE, we introduce Latent Feature Adapter, a geometry-aware bridge module that directly distills these hidden features into a scene latent, subsequently decoded into the final 3D Gaussian scene. Experiments demonstrate that Pano2World significantly outperforms existing methods on the multi-position panoramic novel-view synthesis benchmark.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (5) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885)**  
  *Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00885) · [pdf](https://arxiv.org/pdf/2607.00885.pdf)
  > 💡 针对稀疏视图下3DGS泛化差，使用平坦最小值优化结合各向异性高斯扰动与周期性重初始化，提升新视角合成质量。

  <details><summary>Abstract</summary>

  Recent advances in neural rendering have established 3D Gaussian Splatting (3DGS) as a highly efficient representation for novel view synthesis, enabling fast training and real-time rendering with strong fidelity. However, when supervision is limited to sparse input views, 3DGS tends to overfit to the observed images and generalize poorly to unseen viewpoints. We address this challenge from the perspective of flat minima (FM) optimization, which seeks solutions that remain stable under small parameter perturbations. Viewing Gaussian parameters as trainable weights, we adapt FM principles to the geometric and dynamic nature of 3DGS with a lightweight training framework. Our method regularizes optimization with controlled Gaussian perturbations that account for each Gaussian's anisotropy and the training progress, preserving fine details while improving robustness to sparse-view overfitting. To further stabilize this flat minima optimization process, we introduce periodic reinitialization, which temporarily returns non-positional parameters to their initial states for a short window. Together, these techniques integrate seamlessly into existing 3DGS pipelines without architectural changes. Experiments on LLFF and Mip-NeRF360 datasets demonstrate improved quantitative metrics and perceptual quality under sparse-view supervision, producing reconstructions that are sharper, more stable, and better generalized to novel viewpoints.

  </details>


- **[GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting](https://arxiv.org/abs/2607.00595)**  
  *Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo, Chang D. Yoo*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00595) · [pdf](https://arxiv.org/pdf/2607.00595.pdf)
  > 💡 针对基于扭曲的高斯喷溅存在空间不对齐问题，提出几何感知可变形聚合方法，利用可变形偏移和隐式置信加权恢复局部线索，提升高频质量并加速2.13倍。

  <details><summary>Abstract</summary>

  Gaussian Splatting has achieved significant improvements by incorporating warping-based techniques. However, such methods suffer from pixel-level inaccuracies due to uncertain geometry. This uncertainty leads to spatial misalignments in the warped images, which disrupt residual learning used in warping-based methods and fundamentally limit the gains of correction, particularly on thin structures and high-frequency details. Driven by our insight that useful visual cues are not lost but locally preserved under slight displacement, we propose Geometry-Aware Deformable Aggregation (GADA). This method introduces an iterative refinement module with deformable offsets to actively correct spatial misalignments and recover these displaced cues. Furthermore, to address the limitations of standard pipelines where visibility checks (i.e., thresholding) often discard valid pixels and multi-view warped image fusion relies on naive mean aggregation, our module is coupled with an implicit confidence weighting mechanism that selectively suppresses unreliable evidence. Consequently, our approach outperforms prior warping-based Gaussian Splatting, preserving high-frequency quality while achieving 2.13 times faster FPS.

  </details>


- **[World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video](https://arxiv.org/abs/2607.01202)**  
  *Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, Tianye Li, Zan Gojcic, Gordon Wetzstein, Iro Armeni, Shalini De Mello, Alex Trevithick*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.01202) · [pdf](https://arxiv.org/pdf/2607.01202.pdf)
  > 💡 提出生成式动态高斯重建方法，用视频模型纠正伪影和填补缺失区域，从单目视频生成

  <details><summary>Abstract</summary>

  We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To train this model, we construct a dataset of aligned multiview video pairs and dynamic 3DGS representations, with simulated artifacts characteristic of monocular reconstruction. At test time, we distill the model's generations, including newly observed regions and motions, back into a single consistent, high-quality dynamic 3DGS, improving both novel-view synthesis and the underlying 3D motion. Our method sets a new state of the art in 4D reconstruction and seamlessly generalizes to in-the-wild videos with large viewpoint changes and dynamic motions.

  </details>


- **[CORGI: Consistency-Aware 3D Dog Reconstruction from a Single Image in the Wild](https://arxiv.org/abs/2607.00321)**  
  *Yuxiao Wu, Weile Li, Boyi Zhu, Yumeng Liu, Youcheng Cai, Ligang Liu*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00321) · [pdf](https://arxiv.org/pdf/2607.00321.pdf)
  > 💡 提出一致性感知变形3DGS和生成修复的框架，从单张野外图像无监督重建高保真、可动画化的

  <details><summary>Abstract</summary>

  Reconstructing high-fidelity 3D models of highly articulated animals, such as dogs, from a single in-the-wild image remains a formidable challenge. In this paper, we introduce CORGI, a novel framework for consistency-aware 3D dog reconstruction from a single unconstrained image that completely eliminates the need for 3D supervision. To overcome generative inconsistencies and the lack of multi-view capture, our pipeline introduces three core components. First, we propose a Canonical-Driven Orbital Generation (CDOG) strategy, utilizing specialized Canonical and Orbit LoRAs to normalize arbitrary input poses and synthesize reliable 360-degree video observations. Second, we design a Consistency-aware Deformable 3DGS (CA-3DGS) module that anchors on a D-SMAL prior, explicitly modeling per-view generative errors through dedicated neural deformation fields to learn accurate vertex-level displacements. Finally, to eliminate structural distortions and recover high-frequency details, we introduce a self-supervised Deformation-Conditioned Generative Repair (DCGR) module. Extensive experiments demonstrate that CORGI achieves state-of-the-art performance, generalizing seamlessly across diverse dog breeds to produce geometrically accurate, visually coherent, and fully animatable 3D assets ready for downstream applications.

  </details>


- **[Progressive Pose-Guided 4D Animal Reconstruction from Monocular Video](https://arxiv.org/abs/2607.00157)**  
  *Siyuan Li, Weiying Chen, Yilin Wang, Xinxin Zuo, Xingyu Li, Li Cheng*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00157) · [pdf](https://arxiv.org/pdf/2607.00157.pdf)
  > 💡 针对单目视频4D动物重建的泛化与保真问题，提出基于3D高斯泼溅的渐进姿态引导优化，结合对称编码与可变形场实现高精度跨物种重建。

  <details><summary>Abstract</summary>

  Reconstructing 4D animals from monocular videos is challenging due to large inter-species variation, complex articulations, and the lack of reliable templates. Existing approaches typically rely on either strict category-specific priors that restrict generalization, or unconstrained generative models that sacrifice input fidelity. To bridge this gap, we present a progressive test-time optimization framework built on 3D Gaussian Splatting for high-fidelity 4D animal reconstruction from a single video. Our key insight is that a coarse shape prior suffices when coupled with a progressive strategy that disentangles articulated pose from non-rigid deformation. Specifically, we employ a symmetry-aware temporal encoding that exploits bilateral cues while absorbing camera estimation drift and a part-conditioned deformation mechanism guided by learnable part anchors and a learnable skinning field. Extensive experiments demonstrate that our approach generalizes robustly across diverse species, achieving superior geometric accuracy, temporal consistency, and visual fidelity compared to existing baselines, even under severe prior mismatch.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (2) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959)**  
  *Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00959) · [pdf](https://arxiv.org/pdf/2607.00959.pdf)
  > 💡 情感说话头合成中实时可控情感表达挑战，提出基于3DGS的残差变形与空间-音频-情感注意力，实现高保真实时渲染。

  <details><summary>Abstract</summary>

  Audio-driven talking head synthesis has achieved impressive progress in lip synchronization and visual quality, yet generating expressive emotional avatars with controllable intensity remains challenging, especially under real-time constraints. In this paper, we present GaussianEmoTalker, an audio-driven framework for real-time emotional talking head synthesis based on 3D Gaussian Splatting. Instead of directly predicting the final emotional avatar from speech, we formulate emotional animation as a neutral-to-emotional residual deformation problem. GaussianEmoTalker first constructs an identity-specific neutral talking space with GaussianBlendshapes, which provides high-fidelity Gaussian attributes and phoneme-synchronized neutral motion. It then predicts an emotion-conditioned residual deformation by combining mesh displacement cues, audio features, emotion categories, and intensity encodings. To fuse these heterogeneous signals, we introduce a spatial-audio-emotion attention module that estimates the offsets of Gaussian attributes for expressive and temporally stable rendering. Extensive experiments demonstrate that GaussianEmoTalker achieves competitive video quality, accurate lip synchronization, controllable emotional expression, and real-time rendering compared with recent emotional talking head methods. Our project page is available at https://njust-yang.github.io/GaussianEmoTalker.github.io/

  </details>


- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673)**  
  *Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar*  
  `2026-07-01` · `cs.RO` · [abs](https://arxiv.org/abs/2607.00673) · [pdf](https://arxiv.org/pdf/2607.00673.pdf)
  > 💡 通过3D高斯泼溅重建结合物理模拟生成环境变形版本，评估地形变化下路径的长期可行性。

  <details><summary>Abstract</summary>

  Robots deployed in unstructured outdoor environments often plan from scene reconstructions collected before deployment because operators cannot remap large or remote sites before every mission. As a result, robots must make long-horizon planning decisions using stale maps that assume the terrain remains unchanged, even though physical changes to the environment may render previously feasible routes unsafe or unreachable at execution time. We present a physically viable world model for evaluating what-if queries for robot navigation under future terrain change. The system augments reconstructed 3D Gaussian splat scenes with physics-based simulation to generate physically modified versions of the same environment without recollecting sensor data or rebuilding the map. We then implement a terrain-aware planner that accounts for physical events, obstacles, and deformations that are simulated by the world model. This allows robots and human operators to evaluate whether planned routes remain feasible before committing to a planned route, particularly in constrained environments where retreat or recovery may become impossible once conditions change. We evaluate the system on a real outdoor field site in Central Texas using simulated flooding across multiple severity levels. We measure route and mission feasibility as terrain conditions deteriorate under physically simulated interventions. Our results show that physically viable world models expose long-horizon route failures and rerouting behavior that are not apparent when planning only on the original reconstructed environment, allowing robots to evaluate how future terrain changes may affect route feasibility before deployment.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889)**  
  *Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00889) · [pdf](https://arxiv.org/pdf/2607.00889.pdf)
  > 💡 提出深度感知3D语义场景图生成方法，用深度引导滤波和概率高斯节点改进对象表示，聚合时空证据及世界模型先验优化关系，在召回率上显著提升。

  <details><summary>Abstract</summary>

  We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single projected point. To mitigate relational sparsity from frame-wise inference, our framework further aggregates spatiotemporal evidence across object pairs and refines relations using contextual priors derived from a world model (V-JEPA 2). Experiments on the 3DSSG and ReplicaSSG datasets demonstrate state-of-the-art (SoTA) performance in both object and predicate prediction, while producing temporally consistent scene structures. In particular, our method improves triplet recall by 77.4% and predicate recall by 23.2% over prior SoTA approaches, making it suitable for robotic manipulation and AR applications. Our code and models are open-sourced.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164)**  
  *Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, Sidharth Kumar*  
  `2026-07-01` · `cs.LG` · [abs](https://arxiv.org/abs/2607.01164) · [pdf](https://arxiv.org/pdf/2607.01164.pdf)
  > 💡 针对隐式表示非结构体积需存网格限制压缩的问题，提出基于3D高斯的显式标量场表示，消除网格需求，压缩率更高且性能全面领先。

  <details><summary>Abstract</summary>

  Recent work has shown that implicit neural representations (INRs) can be trained to effectively compress structured and unstructured volume data, allowing for direct data querying with a reduced memory footprint. However, as existing INRs for unstructured volumes do not encode geometry, they require partial mesh storage for later sampling, limiting achievable compression. At the same time, novel view synthesis methods have shown that explicit collections of 3D Gaussians can be used to accurately visualize volume data. In this work, we introduce an explicit model for volume data compression based on 3D Gaussian primitives. We reinterpret collections of 3D Gaussians as an explicit representation of a scalar field and use a sampling strategy that reconstructs scalar values at spatial locations through weighted aggregation of intersecting Gaussians. We develop optimized CUDA-accelerated pipelines for structured and unstructured model sampling, loss functions that encourage accurate domain encoding by our models, and a novel sampling-error based densification strategy. Our explicit formulation naturally encodes domain geometry, eliminating the need for mesh storage in unstructured volumes and introducing significantly higher compression opportunities. Compared to existing INRs, we demonstrate that our explicit model achieves competitive reconstruction quality with significant training speedups on structured volumes, while markedly outperforming in all metrics on unstructured volumes.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200)**  
  *Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian*  
  `2026-07-01` · `cs.RO` · [abs](https://arxiv.org/abs/2607.01200) · [pdf](https://arxiv.org/pdf/2607.01200.pdf)
  > 💡 针对3DGS安全滤波器忽略执行器限制问题，提出全四旋翼动力学的执行器感知碰撞锥CBF，降低急动度47%、加速2.25倍。

  <details><summary>Abstract</summary>

  Fast quadrotor flight requires safe obstacle avoidance under tight onboard compute limits. While 3D Gaussian Splatting (3DGS) provides a continuous, geometry-aware scene representation for perception-driven navigation, existing 3DGS safety filters use reduced-order models such as single- and double-integrators that ignore actuator limits and assume commanded accelerations are realized instantaneously. Building on an analytic collision cone barrier for 3DGS, we introduce a nonlinear, actuator-aware safety filter enforced through the full quadrotor dynamics. We derive a high-relative-degree collision cone exponential CBF and a backup CBF that preserves QP feasibility under input constraints using a forward-simulated backup policy. Compared with a state-of-the-art 3DGS safety filter, our approach reduces trajectory jerk by 47% and runs 2.25 times faster. We validate the method in simulation and on hardware for real-time navigation in cluttered, perception-derived environments.

  </details>


</details>

<details><summary><b>Semantic / Scene Understanding</b> (2) · <a href="topics/semantic.md">full list →</a></summary>

- **[Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140)**  
  *Eunsung Cha, Hyunjoon Lee, Jaesik Park*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.01140) · [pdf](https://arxiv.org/pdf/2607.01140.pdf)
  > 💡 将分割任务转化为高斯对间成对关系建模，利用视图贡献和多视图掩码构建关系图，实现快速且准确的开放词汇3D高斯分割。

  <details><summary>Abstract</summary>

  Open-vocabulary 3D Gaussian segmentation is challenging because it requires language understanding for diverse queries and accurate separation of Gaussians along object boundaries. Prior approaches either embed language knowledge into individual Gaussians to improve query responsiveness or optimize per-Gaussian instance features to encode object identity. However, these strategies may produce noisy Gaussian segmentations or rely on cost-inefficient per-scene optimization. We propose PairGS, a framework that reframes Gaussian segmentation as modeling pairwise relations between Gaussians. 3D Gaussian representations provide rich signals for relation estimation, such as view contribution weights and multi-view mask evidence. By leveraging these cues, PairGS explicitly constructs a relation graph for segmentation without a heavy optimization process. PairGS first proposes sparse edge candidates using low-dimensional descriptors, computes precise pairwise affinities only on those candidates, and builds a hierarchical cluster tree for multi-granular querying. It achieves state-of-the-art results on open-vocabulary 3D Gaussian segmentation benchmarks, while the fast variant is 50x faster than optimization-based instance-feature approaches.

  </details>


- **[GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception](https://arxiv.org/abs/2607.00746)**  
  *Xiao Zhao, Chang Liu, Mingxu Zhu, Zheyuan Zhang, Linna Song, Qingliang Luo, Chufan Guo, Kuifeng Su*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00746) · [pdf](https://arxiv.org/pdf/2607.00746.pdf)
  > 💡 提出基于3D高斯表示的多模态融合框架，替代BEV范式，通过高斯初始化与注意力更新，提升感知精度与速度。

  <details><summary>Abstract</summary>

  The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception. However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception. In this work, we break from the conventional BEV paradigm and propose a new universal framework for multi-modal fusion based on 3D Gaussian representation. This approach naturally unifies multi-modal features within a shared and continuous 3D Gaussian space, effectively preserving edge and fine texture details. To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on an attention mechanism. GaussianFusion is inherently a task-agnostic model, with its unified Gaussian representation naturally supporting various 3D perception tasks. Extensive experiments demonstrate the generality and robustness of GaussianFusion. On the nuScenes dataset, it outperforms the 3D object detection baseline BEVFusion by 2.6 NDS. Its variant surpasses GaussFormer on 3D semantic occupancy with 1.55 mIoU improvement while using only 30% of the Gaussians and achieving a 450% speedup.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
