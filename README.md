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
| 1 | **Survey & Benchmark** | 49 | **+49** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 214 | **+214** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 24 | **+24** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 40 | **+40** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 18 | **+18** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 30 | **+30** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 29 | **+29** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 8 | **+8** | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 11 | **+11** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | **+2** | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 2 | **+2** | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 11 | **+11** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | **+9** | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 20 | **+20** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | **+7** | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-05-30 (UTC) — 474 new paper(s)

<details><summary><b>Survey & Benchmark</b> (49) · <a href="topics/survey.md">full list →</a></summary>

- **[Learning Representations from 3D Gaussian Splats](https://arxiv.org/abs/2605.29549)**  
  *Julia Farganus, Krzysztof Żurawicki, Arkadiusz Gaweł, Weronika Jakubowska, Halina Kwaśnicka*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29549) · [pdf](https://arxiv.org/pdf/2605.29549.pdf)
  > 💡 评估点云和图模型对3D高斯场景分类的性能，揭示高斯属性对表示质量的影响。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a recent approach for scene rendering. Although primarily designed for view synthesis, its potential for scene understanding tasks remains underexplored. In this work, we conduct a comparative evaluation of various geometric deep learning architectures for the classification of 3D scenes represented using Gaussian Splatting. We benchmark point-based and graph-based models across both traditional point cloud datasets and dedicated Gaussian Splatting datasets. Scenes are embedded into latent representations, which are evaluated through end-to-end classification, linear probing, and clustering analysis. Our study provides insight into the suitability of different geometry-aware architectures and input feature configurations for learning effective 3D Gaussian Splat representations. The results highlight consistent differences between architectural families and reveal the impact of Gaussian-specific attributes on the quality of representation.

  </details>


- **[POINav: Benchmarking and Enhancing Final-Meters Arrival in Real-World Vision-Language Navigation](https://arxiv.org/abs/2605.28237)**  
  *Ruiyan Gong, Meisheng Zhang, Yuxiang Zhao, Mingchao Sun, Yanfen Shen, Zedong Chu, Zhining Gu, Wei Guo, Xiaolong Cheng, Qiming Li, Kangning Niu, Yanqing Zhu, Xiaolong Wu, Tianlun Li, Mu Xu*  
  `2026-05-27` · `cs.RO` · [abs](https://arxiv.org/abs/2605.28237) · [pdf](https://arxiv.org/pdf/2605.28237.pdf)
  > 💡 面对真实世界POI导航的“最后几米”挑战，提出基于3DGS重建的POINav-Bench基准和脑-动作框架，实现闭环评估与连续航点预测。

  <details><summary>Abstract</summary>

  Real-world navigation is fundamentally driven by Points of Interest (POIs), yet reaching a precise POI remains a critical "final-meters" challenge. Existing Vision-Language Navigation (VLN) benchmarks of POI-goal navigation often suffer from coarse granularity or significant sim-to-real gaps due to generated scene. To bridge this gap, we present POINav-Bench, the first benchmark designed for closed-loop evaluation of real-world POI-goal navigation. It comprises 11 commercial areas reconstructed from real-world captures using 3D Gaussian Splatting (3DGS), covering 126,398 $m^{2}$ in total and spanning 163 distinct POIs. With traversability-aware annotations and reference trajectories, POINav-Bench enables high-fidelity evaluation of navigation agents in realistic, POI-rich real-world environments. Building on this, we propose the POINav Brain-Action Framework where a Brain module performs POI-grounded reasoning to guide an Action module in predicting continuous waypoints for real-world execution. We further curate the POINav-Dataset, containing 70K real-world signage-entrance pairs. Experiments show that our framework provides a viable path toward refining real-world POI-goal navigation.

  </details>


- **[GScomp-QA: A Subjective Dataset for Quality Assessment of Compressed Gaussian Splatting](https://arxiv.org/abs/2605.26880)**  
  *Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz*  
  `2026-05-26` · `eess.IV` · [abs](https://arxiv.org/abs/2605.26880) · [pdf](https://arxiv.org/pdf/2605.26880.pdf)
  > 💡 针对Gaussian Splatting压缩缺乏感知评估，构建GScomp-QA主观数据集，含331视频覆盖9种压缩方案，提供基准与感知率失真分析。

  <details><summary>Abstract</summary>

  Gaussian Splatting (GS) has emerged as an efficient representation for high-quality 3D reconstruction and novel view synthesis. However, its large model size poses challenges for storage and transmission. While several GS compression solutions have been proposed, their perceptual impact remains poorly understood due to the lack of dedicated evaluation datasets. To address this gap, this paper introduces GScomp-QA, a subjective quality assessment dataset for evaluating synthesis quality from compressed GS models. The dataset comprises 331 video stimuli from 13 real-world scenes, covering 9 state-of-the-art GS compression solutions. By using videos synthesized from uncompressed models as reference, GScomp-QA isolates compression-induced distortions from synthesis artifacts. A subjective study with 20 participants was conducted, providing reliable perceptual scores. Based on these data, GS compression solutions are evaluated through perceptual rate-distortion analysis. In addition, 18 objective quality metrics are evaluated, showing that they do not fully capture GS-specific distortions. GScomp-QA will be publicly available and provide a benchmark for evaluating GS compression solutions and supporting the development of quality metrics tailored to GS compression.

  </details>


- **[DelowlightSplat: Feed-Forward Gaussian Splatting for Lowlight 3D Scene Reconstruction](https://arxiv.org/abs/2605.26629)**  
  *Fuzhen Jiang, Zengtian Xie, Zhuoran Li*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26629) · [pdf](https://arxiv.org/pdf/2605.26629.pdf)
  > 💡 针对弱光噪声与色偏导致前馈3DGS失败的问题，提出低光适配器增强匹配性，结合成本体积推理直接预测干净3D高斯，实现高质量重建。

  <details><summary>Abstract</summary>

  Novel-view synthesis and 3D reconstruction from sparse posed images are central to robotics and AR/VR. Yet, feed-forward 3D Gaussian reconstruction fails under lowlight due to noise, color shifts, and unreliable correspondence. We propose DelowlightSplat, a lowlight-aware feed-forward Gaussian splatting framework for clean novel-view rendering. We build a controllable multi-view lowlight benchmark by degrading only context views while keeping target views clean. We introduce a lightweight Lowlight Adapter for residual enhancement to improve matchability, and couple it with cost-volume-based multi-view inference to directly predict clean 3D Gaussians. Experiments show that DelowlightSplat significantly outperforms previous feed-forward method and two-stage pipeline under lowlight conditions.

  </details>


- **[Underwater360: Reconstructing Underwater Scenes from Panoramic Images with Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2605.26447)**  
  *Jiangbei Hu, Weichao Song, Shibo Yu, Mohan Wang, Zihan Yi, Rui Wu, Mingkang Xiang, Na Lei, Shengfa Wang, Zhongxuan Luo, Ying He*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26447) · [pdf](https://arxiv.org/pdf/2605.26447.pdf)
  > 💡 用物理感知的全向3DGS直接球面光线投射和介质建模，恢复水下场景并提升渲染质量与一致性。

  <details><summary>Abstract</summary>

  Underwater scene reconstruction is essential for immersive exploration of aquatic environments, yet remains challenging due to complex participating-media effects such as absorption and scattering, as well as the limited field of view (FoV) of conventional cameras. Although combining panoramic imaging with 3D Gaussian Splatting (3DGS) offers a promising direction for photorealistic underwater rendering, traditional 3DGS struggles with both spherical projection distortion and underwater medium degradation. In this paper, we propose \textbf{Underwater360}, a physics-informed omnidirectional 3DGS framework for underwater panoramic scene reconstruction. First, we introduce an Omnidirectional Gaussian Splatting module that performs ray casting directly in spherical camera space instead of relying on 2D projection approximations, thereby reducing geometric distortions under 360$^\circ$ FoV. Second, we design a physics-based appearance-medium modeling architecture with pose-conditioned appearance embeddings to explicitly decouple intrinsic scene radiance from depth-dependent backscatter and attenuation, enabling physically grounded scene appearance restoration. Finally, we establish a new panoramic underwater benchmark dataset containing both synthetic and real-world scenes. Extensive experiments demonstrate that Underwater360 achieves superior performance in underwater novel view synthesis and scene appearance restoration, delivering improved rendering quality and cross-view consistency in complex underwater environments. The code and datasets are released at https://github.com/SwcK423/Underwater360

  </details>


- **[SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation](https://arxiv.org/abs/2605.22536)**  
  *Xiaolong Zhou, Yifei Liu, Ziyang Gong, Jiarui Li, Qiyue Zhao, Muyao Niu, Yuanyuan Gao, Le Ma, Xue Yang, Hongjie Zhang, Zhihang Zhong*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22536) · [pdf](https://arxiv.org/pdf/2605.22536.pdf)
  > 💡 提出空间智能对九种视觉退化的鲁棒性基准SpaceDG，利用3DGS渲染合成退化场景，揭示多模态大模型在退化条件下空间推理能力显著下降。

  <details><summary>Abstract</summary>

  Multimodal Large Language Models (MLLMs) have made rapid progress in spatial intelligence, yet existing spatial reasoning benchmarks largely assume pristine visual inputs and overlook the degradations that commonly occur in real-world deployment, such as motion blur, low light, adverse weather, lens distortion, and compression artifacts. This raises a fundamental question: how robust is the spatial intelligence of current MLLMs when visual observations are imperfect? To answer this question, we introduce SpaceDG, the first large-scale dataset for degradation-aware spatial understanding. It is constructed with a physically grounded degradation synthesis engine that embeds degradation formation process into 3D Gaussian Splatting (3DGS) rendering, enabling realistic simulation of nine degradation types. The resulting dataset contains approximately 1M QA pairs from nearly 1,000 indoor scenes. We further introduce SpaceDG-Bench, an human-verified benchmark with 1,102 questions spanning 11 reasoning categories and 9 visual degradation types, yielding over 10K VQA instances. Evaluating 25 open- and closed-source MLLMs reveals that visual degradations consistently and substantially impair spatial reasoning, exposing a critical robustness gap. Finally, we show that finetuning on SpaceDG markedly improves degradation robustness and can even surpass human performance under degraded conditions without any performance drop on clean images, highlighting the promise of degradation-aware training for robust spatial intelligence.

  </details>


- **[RCGDet3D: Rethinking 4D Radar-Camera Fusion-based 3D Object Detection with Enhanced Radar Feature Encoding](https://arxiv.org/abs/2605.21112)**  
  *Weiyi Xiong, Bing Zhu*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.21112) · [pdf](https://arxiv.org/pdf/2605.21112.pdf)
  > 💡 4D雷达-相机融合检测速度慢，通过增强雷达特征编码（R-PGE和语义注入）简化融合，RCGDet3D实现精度与速度双领先。

  <details><summary>Abstract</summary>

  4D automotive radar is indispensable for autonomous driving due to its low cost and robustness, yet its point cloud sparsity challenges 3D object detection. Existing 4D radar-camera fusion methods focus on complex fusion strategies, trading inference speed for marginal gains. This trade-off hinders real-time deployment due to heavy computation on dense feature maps. In contrast, feature extraction from sparse radar points is less time-consuming but remains under-explored. This work uncovers that simply enhancing radar feature extraction can achieve comparable or even higher performance than elaborate fusion modules, while maintaining real-time performance. Based on this finding, we propose RCGDet3D, which centers on radar feature encoding and simplifies multi-modal fusion. Its encoder inherits from the efficient Gaussian Splatting-based Point Gaussian Encoder (PGE) in RadarGaussianDet3D with two key improvements. First, the Ray-centric PGE (R-PGE) predicts Gaussian attributes in ray-aligned coordinate systems before unifying them to Bird's-Eye View (BEV) space, significantly improving geometric consistency and reducing learning difficulty by decoupling the coordinate transformation from representation learning. Second, a Semantic Injection (SI) module incorporates visual cues from images, producing more geometrically accurate and semantically enriched radar features. Experiments on View-of-Delft (VoD) and TJ4DRadSet show that RCGDet3D outperforms state-of-the-art methods in both accuracy and speed, setting a new benchmark for real-time deployment.

  </details>


- **[ArtMesh: Part-Aware Articulated Mesh Fields with Motion-Consistent Dynamics](https://arxiv.org/abs/2605.16582)**  
  *Sylvia Yuan, Dan Wang, Ravi Ramamoorthi, Xinrui Cui*  
  `2026-05-15` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16582) · [pdf](https://arxiv.org/pdf/2605.16582.pdf)
  > 💡 针对3DGS缺乏表面拓扑问题，提出基于网格的关节重建，用部分感知重网格和双向运动一致性，在关节参数估计和几何重建上超越现有方法。

  <details><summary>Abstract</summary>

  We present ArtMesh, a mesh-native method for reconstructing articulated objects explicitly as connected triangle meshes with per-part rigid motion from multi-view images in start and end states. Existing 3D Gaussian Splatting pipelines for articulated reconstruction inherit the unstructured point-based geometry of their splatting base, which provides no surface topology for reasoning about part boundaries or enforcing motion consistency along the object's connectivity. ArtMesh instead builds on a mesh-based differentiable rendering backbone, enabling part-aware dynamics to act directly on the structured topology. To make the topology compatible with articulation, we introduce part-aware restricted Delaunay remeshing, producing connected submeshes whose triangles do not cross semantic part boundaries. The dynamic mesh field then optimizes articulation using bidirectional Vertex-wise Motion Consistency on transported mesh vertices and Pixel-wise Motion Consistency on rendered RGB-D observations. We introduce Articulate-100, a new benchmark of 100 articulated objects spanning 16 PartNet-Mobility categories. On this benchmark, ArtMesh outperforms prior 3DGS-based pipelines in joint parameter estimation and part-level geometric reconstruction, with the largest gains on objects with many movable parts.

  </details>


- **[3DEditSafe: Defending 3D Editing Pipelines from Unsafe Generation](https://arxiv.org/abs/2605.15398)**  
  *Nicole Meng, Zheyuan Liu, Meng Jiang, Yingjie Lao*  
  `2026-05-14` · `cs.GR` · [abs](https://arxiv.org/abs/2605.15398) · [pdf](https://arxiv.org/pdf/2605.15398.pdf)
  > 💡 针对3DGS编辑中不安全NSFW内容传播，提出安全正则化与语义投影的3DEditSafe框架，首次防御3D编辑不安全生成。

  <details><summary>Abstract</summary>

  Recent advances in 3D generative editing, particularly pipelines based on 3D Gaussian Splatting (3DGS), have achieved high-fidelity, multi-view-consistent scene manipulation from text prompts. However, we find that these pipelines also introduce new safety risks when unsafe prompts produce edits that are propagated and optimized across views. In this work, we study unsafe generation in 3D editing pipelines and show that such behavior can lead to coherent, undesirable Not-Safe-For-Work (NSFW) content in the final 3D representation. To address this, we propose 3DEditSafe, a safety-regularized 3D editing framework that constrains unsafe semantic propagation during optimization. 3DEditSafe combines generation-stage safety guidance with rendered-view 3D safety regularization, safe semantic projection, residue suppression, and mask-aware preservation to steer optimization away from unsafe editing directions. We evaluate our approach on EditSplat scenes using an object-compatible unsafe prompt benchmark and show that 2D safety guidance alone is not consistently sufficient to prevent unsafe 3D edits. 3DEditSafe reduces unsafe semantic alignment and view-level attack success rates, while revealing a safety-quality tradeoff in which stronger unsafe suppression can introduce artifacts or reduce unsafe-prompt fidelity. To our knowledge, this work is the first attempt to study and defend against unsafe generation in text-driven 3D editing pipelines, highlighting the need for safety mechanisms that operate directly on optimized 3D representations.

  </details>


- **[Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880)**  
  *Qingyuan Zhou, Xinyi Liu, Weidong Yang, Ning Wang, Shuquan Ye, Ben Fei, Ying He, Wanli Ouyang*  
  `2026-05-14` · `cs.CV` · [abs](https://arxiv.org/abs/2605.14880) · [pdf](https://arxiv.org/pdf/2605.14880.pdf)
  > 💡 针对3DGS中噪声原语问题，提出空间感知去噪框架，联合位置与空间结构优化，提升新视图合成质量与紧凑性。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable success in high-fidelity Novel View Synthesis (NVS), yet the optimization process inevitably introduces noisy Gaussian primitives due to the sparse and incomplete initialization from Structure-from-Motion (SfM) point clouds. Most existing methods focus solely on adjusting the positions of primitives during optimization, while neglecting the underlying spatial structure. To this end, we introduce a new perspective by formulating the optimization of 3DGS as a primitive denoising process and propose Denoising-GS, a spatial-aware denoising framework for Gaussian primitives by taking both the positions and spatial structure into consideration. Specifically, we design an optimizer that preserves the spatial optimization flow of primitives, facilitating coherent and directed denoising rather than random perturbations. Building upon this, the Spatial Gradient-based Denoising strategy jointly considers the spatial supports of primitives to ensure gradient-consistent updates. Furthermore, the Uncertainty-based Denoising module estimates primitive-wise uncertainty to prune redundant or noisy primitives, while the Spatial Coherence Refinement strategy selectively splits primitives in sparse regions to maintain structural completeness. Experiments conducted on three benchmark datasets demonstrate that Denoising-GS consistently enhances NVS fidelity while maintaining representation compactness, achieving state-of-the-art performance across all benchmarks. Source code and models will be made publicly available.

  </details>


- **[FFAvatar: Few-Shot, Feed-Forward, and Generalizable Avatar Reconstruction](https://arxiv.org/abs/2605.15320)**  
  *Thuan Hoang Nguyen, Jiahao Luo, Yinyu Nie, Hao Li, Gordon Guocheng Qian, Jian Wang*  
  `2026-05-14` · `cs.GR` · [abs](https://arxiv.org/abs/2605.15320) · [pdf](https://arxiv.org/pdf/2605.15320.pdf)
  > 💡 FFAvatar利用多视图

  <details><summary>Abstract</summary>

  Avatar reconstruction has traditionally relied on per-subject optimization that requires hours of computation or on expensive preprocessing that limits scalability. We introduce FFAvatar, a generalizable feed-forward framework that reconstructs high-quality, animatable 3D Gaussian head avatars from few-shot unposed portrait images in seconds. FFAvatar fuses information from multiple source images into a unified canonical Gaussian representation through Multi-View Query-Former, which is animated via FLAME parameters predicted end-to-end directly from pixels, eliminating the overhead of offline FLAME extraction. We further propose a three-stage training curriculum that achieves both broad generalization and high-fidelity reconstruction: (i) scalable pretraining on extensive monocular video data with over 1M identities to learn strong generalizable priors; (ii) multi-view fine-tuning on a small but high-quality dataset of 360-degree captures to enhance geometric fidelity and extreme-view awareness; and (iii) optional personalization that adapts to specific identities for maximum fidelity within 500 optimization steps. Extensive experiments demonstrate that FFAvatar sets a new standard for identity preservation, geometric consistency, and animation fidelity. On the NeRSemble benchmark, it outperforms the state-of-the-art LAM by a substantial 5.5 PSNR gain. Furthermore, FFAvatar enables real-time deployment, reconstructing avatars in 2 seconds without personalization and 10 seconds with personalization, while supporting 49 FPS animation on a single NVIDIA A100 GPU.

  </details>


- **[RoSplat: Robust Feed-Forward Pixel-wise Gaussian Splatting for Varying Input Views and High-Resolution Rendering](https://arxiv.org/abs/2605.13093)**  
  *Hoang Chuong Nguyen, Renjie Wu, Jose M. Alvarez, Miaomiao Liu*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13093) · [pdf](https://arxiv.org/pdf/2605.13093.pdf)
  > 💡 提出alpha归一化和3D采样正则化，解决变输入视图过亮与高分辨率渲染空洞问题，提升前馈高斯泼溅鲁棒性。

  <details><summary>Abstract</summary>

  Generalizable 3D Gaussian Splatting has recently emerged as an efficient approach for novel-view synthesis, enabling feed-forward synthesis from only a few input views. However, existing pixel-wise feed-forward methods suffer from over-bright renderings when the number of input views varies during inference, as well as insufficient supervision for accurate Gaussian scale estimation, which leads to hole artifacts, particularly in high-resolution renderings. To address these issues, we identify that the over-brightness is caused by the varying number of overlapping Gaussians and propose a simple alpha normalization strategy to maintain brightness consistency across different number of input views. In addition, we introduce an auxiliary 3D sampling-based regularizer to improve Gaussian scale estimation, thereby mitigating hole artifacts in high-resolution rendering. Experiments on benchmark datasets demonstrate that our method significantly improves baseline models under varying input-view and high-resolution rendering settings.

  </details>


- **[3D Gaussian Splatting for Efficient Retrospective Dynamic Scene Novel View Synthesis with a Standardized Benchmark](https://arxiv.org/abs/2605.12437)**  
  *Yunxiao Zhang, Suryansh Kumar*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12437) · [pdf](https://arxiv.org/pdf/2605.12437.pdf)
  > 💡 针对同步多视角动态场景，提出无需时间变形约束的3DGS方法，并构建标准化基准实现高效回顾性新视图合成。

  <details><summary>Abstract</summary>

  Retrospective novel view synthesis (NVS) of dynamic scenes is fundamental to applications such as sports. Recent dynamic 3D Gaussian Splatting (3DGS) approaches introduce temporally coupled formulations to enforce motion coherence across time. In this paper, we argue that, in a synchronized multi-view (MV) setting typical of sports, the dynamic scene at each time step is already strongly geometrically constrained. We posit that the availability of calibrated, synchronized viewpoints provides sufficient spatial consistency, and therefore, explicit temporal coupling, or complex multi-body constraints seems unnecessary for retrospective NVS. To this end, we propose an approach tailored for synchronized MV dynamic scene. By initializing the SfM-derived point cloud at the start time and propagating optimized Gaussians over time, we show that efficient retrospective NVS can be achieved without imposing a temporal deformation constraint. Complementing our methodological contribution, we introduce a Dynamic MV dataset framework built on Blender for reproducible NeRF and 3DGS research. The framework generates high-quality, synchronized camera rigs and exports training-ready datasets in standard formats, eliminating inconsistencies in coordinate conventions and data pipelines. Using the framework, we construct a dynamic benchmark suite and evaluate representative NeRF and 3DGS approaches under controlled conditions. Together, we show that, under a synchronized MV setup, efficient retrospective dynamic scene NVS can be achieved using 3DGS. At the same time, the dataset-generation framework enables reproducible and principled benchmarking of dynamic NVS methods.

  </details>


- **[PD-4DGS:Progressive Decomposition of 4D Gaussian Splatting for Bandwidth-Adaptive Dynamic Scene Streaming](https://arxiv.org/abs/2605.11427)**  
  *Jiachen Li, Guangzhi Han, Jin Wan, Delong Han, Yuan Gao, Min Li, Mingle Zhou, Gang Li*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11427) · [pdf](https://arxiv.org/pdf/2605.11427.pdf)
  > 💡 针对4DGS全量下载延迟问题，提出渐进式分解带宽自适应流媒体方法，层次化变形分解与率失真损失降低首帧延迟至1.7秒。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting (4DGS) enables high-quality dynamic novel view synthesis, yet current models remain monolithic bitstreams that clients must download in full before any frame can be rendered, causing black-screen waits of tens to hundreds of seconds on mobile bandwidth and leaving 4DGS incompatible with modern adaptive-bitrate delivery. Progressive 3DGS compression alleviates this for static scenes, but it acts only on spatial anchors and cannot partition the temporal deformation networks that dominate dynamic-scene size. We present PD-4DGS, the first framework for progressive compression and on-demand transmission of 4DGS. Hierarchical Deformation Decomposition (HDD) externalises the coarse-to-fine motion hierarchy already latent in 4DGS into three independently transmittable layers -- a static scaffold, a global deformation, and a local refinement -- so that any prefix of the bitstream is already renderable, turning a single training run into a scalable, DASH/HLS-compatible bitstream. A Gaussian-entropy attribute rate-distortion loss together with a temporal mask consistency regulariser shrink the base layer while suppressing low-bitrate flicker; a capacity-weighted rollout schedule, gated online by a learnt activation rate rho, then prevents deformation-network under-training without any per-scene hyperparameter. On the Dycheck iPhone benchmark, PD-4DGS cuts the streamed bitstream by >60% at matched rendering fidelity and reduces first-frame latency from 73--930 s to ~1.7 s on a 2 Mbps link, uniquely enabling true on-demand progressive streaming for 4DGS.

  </details>


- **[MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction](https://arxiv.org/abs/2605.10760)**  
  *Zhihao Cao, Qi Shao, Shuhao Zhai, Jing Zhang, Anh Nguyen, Baoru Huang*  
  `2026-05-11` · `cs.RO` · [abs](https://arxiv.org/abs/2605.10760) · [pdf](https://arxiv.org/pdf/2605.10760.pdf)
  > 💡 针对多智能体SLAM依赖

  <details><summary>Abstract</summary>

  Collaborative photorealistic 3D reconstruction from multiple agents enables rapid large-scale scene capture for virtual production and cooperative multi-robot exploration. While recent 3D Gaussian Splatting (3DGS) SLAM algorithms can generate high-fidelity real-time mapping, most of the existing multi-agent Gaussian SLAM methods still rely on RGB-D sensors to obtain metric depth and simplify cross-agent alignment, which limits the deployment on lightweight, low-cost, or power-constrained robotic platforms. To address this challenge, we propose MAGS-SLAM, the first RGB-only multi-agent 3DGS SLAM framework for collaborative scene reconstruction. Each agent independently builds local monocular Gaussian submaps and transmits compact submap summaries rather than raw observations or dense maps. To facilitate robust collaboration in the presence of monocular scale ambiguity, our framework integrates compact submap communication, geometry- and appearance-aware loop verification, and occupancy-aware Gaussian fusion, enabling coherent global reconstruction without active depth sensors. We further introduce ReplicaMultiagent Plus benchmark for evaluating collaborative Gaussian SLAM. Intensive experiments on synthetic and real-world datasets show that MAGS-SLAM achieves competitive tracking accuracy and comparable or superior rendering quality to state-of-the-art RGB-D collaborative Gaussian SLAM methods while relying only RGB images.

  </details>


- **[VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models](https://arxiv.org/abs/2605.10485)**  
  *Hao Wang, Xiaobao Wei, Jingyang He, Chengyu Bai, Chun-Kai Fan, Jiajun Cao, Jintao Chen, Ying Li, Shanyu Rong, Ming Lu, Xiaozhu Ju, Jian Tang, Shanghang Zhang*  
  `2026-05-11` · `cs.RO` · [abs](https://arxiv.org/abs/2605.10485) · [pdf](https://arxiv.org/pdf/2605.10485.pdf)
  > 💡 VLA模型缺乏空间感知，VEGA通过对齐视觉编码器输出与3DGS微调的DINOv2-FiT3D，提升空间推理且无额外开销。

  <details><summary>Abstract</summary>

  Precise spatial reasoning is fundamental to robotic manipulation, yet the visual backbones of current vision-language-action (VLA) models are predominantly pretrained on 2D image data without explicit 3D geometric supervision, resulting in representations that lack accurate spatial awareness. Existing implicit spatial grounding methods partially address this by aligning VLA features with those of 3D-aware foundation models, but they rely on empirical layer search and perform alignment on LLM-level visual tokens where spatial structure has already been entangled with linguistic semantics, limiting both generalizability and geometric interpretability. We propose VEGA (Visual Encoder Grounding Alignment), a simple yet effective framework that directly aligns the output of the VLA's visual encoder with spatially-aware features from DINOv2-FiT3D, a DINOv2 model fine-tuned with multi-view consistent 3D Gaussian Splatting supervision. By performing alignment at the visual encoder output level, VEGA grounds spatial awareness before any linguistic entanglement occurs, offering a more interpretable and principled alignment target. The alignment is implemented via a lightweight projector trained with a cosine similarity loss alongside the standard action prediction objective, and is discarded at inference time, introducing no additional computational overhead. Extensive experiments on simulation benchmark and real-world manipulation tasks demonstrate that VEGA consistently outperforms existing implicit spatial grounding baselines, establishing a new state-of-the-art among implicit spatial grounding methods for VLA models.

  </details>


- **[Aes3D: Aesthetic Assessment in 3D Gaussian Splatting](https://arxiv.org/abs/2605.05155)**  
  *Chuanzhi Xu, Boyu Wei, Haoxian Zhou, Xuanhua Yin, Zihan Deng, Haodong Chen, Qiang Qu, Weidong Cai*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.05155) · [pdf](https://arxiv.org/pdf/2605.05155.pdf)
  > 💡 针对3DGS场景缺乏美学评估，提出首个数据集Aesthetic3D和轻量模型Aes3DGSNet，直接预测场景美学分数。

  <details><summary>Abstract</summary>

  As 3D Gaussian Splatting (3DGS) gains attention in immersive media and digital content creation, assessing the aesthetics of 3D scenes becomes important in helping creators build more visually compelling 3D content. However, existing evaluation methods for 3D scenes primarily emphasize reconstruction fidelity and perceptual realism, largely overlooking higher-level aesthetic attributes such as composition, harmony, and visual appeal. This limitation comes from two key challenges: (1) the absence of general 3DGS datasets with aesthetic annotations, and (2) the intrinsic nature of 3DGS as a low-level primitive representation, which makes it difficult to capture high-level aesthetic features. To address these challenges, we propose Aes3D, the first systematic framework for assessing the aesthetics of 3D neural rendering scenes. Aes3D includes Aesthetic3D, the first dataset dedicated to 3D scene aesthetic assessment, built on our proposed annotation strategy for 3D scene aesthetics. In addition, we present Aes3DGSNet, a lightweight model that directly predicts scene-level aesthetic scores from 3DGS representations. Notably, our model operates solely on 3D Gaussian primitives, eliminating the need for rendering multi-view images and thus reducing computational cost and hardware requirements. Through aesthetics-supervised learning on multi-view 3DGS scene representations, Aes3DGSNet effectively captures high-level aesthetic cues and accurately regresses aesthetic scores. Experimental results demonstrate that our approach achieves strong performance while maintaining a lightweight design, establishing a new benchmark for 3D scene aesthetic assessment. Code and datasets will be made available in a future version.

  </details>


- **[SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion](https://arxiv.org/abs/2605.01466)**  
  *Zhaoyang Li, Zhichao You, Tianrui Li*  
  `2026-05-02` · `cs.CV` · [abs](https://arxiv.org/abs/2605.01466) · [pdf](https://arxiv.org/pdf/2605.01466.pdf)
  > 💡 点云补全中硬投影导致跨模态熵崩溃，提出可微高斯泼溅与注意力框架实现密集连续表示，达SOTA并增强视觉依赖。

  <details><summary>Abstract</summary>

  Although multi-modal learning has advanced point cloud completion, the theoretical mechanisms remain unclear. Recent works attribute success to the connection between modalities, yet we identify that standard hard projection severs this connection: projecting a sparse point cloud onto the image plane yields an extremely sparse support, which hinders visual prior propagation, a failure mode we term Cross-Modal Entropy Collapse. To address this practical limitation, we propose SplAttN, which replaces hard projection with Differentiable Gaussian Splatting to produce a dense, continuous image-plane representation. By reformulating projection as continuous density estimation, SplAttN avoids collapsed sparse support, facilitates gradient flow, and improves cross-modal connection learnability. Extensive experiments show that SplAttN achieves state-of-the-art performance on PCN and ShapeNet-55/34. Crucially, we utilize the real-world KITTI benchmark as a stress test for multi-modal reliance. Counter-factual evaluation reveals that while baselines degenerate into unimodal template retrievers insensitive to visual removal, SplAttN maintains a robust dependency on visual cues, validating that our method establishes an effective cross-modal connection. Code is available at https://github.com/zay002/SplAttN.

  </details>


- **[Fake3DGS: A Benchmark for 3D Manipulation Detection in Neural Rendering](https://arxiv.org/abs/2604.27590)**  
  *Davide Di Nucci, Riccardo Catalini, Guido Borghi, Roberto Vezzani*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.27590) · [pdf](https://arxiv.org/pdf/2604.27590.pdf)
  > 💡 为3D高斯泼溅提出伪造检测基准与多视图一致性特征方法，显著提升识别能力。

  <details><summary>Abstract</summary>

  Recent advances in 3D reconstruction and neural rendering,particularly 3D Gaussian Splatting, make it feasible and simple to edit 3D scenes and re-render them as highly realistic images. Therefore, security concerns arise regarding the authenticity of 3D content. Despite this threat, 3D fake detection remains largely unexplored in the literature, and most existing work is limited to 2D space. Therefore, in this paper, we formalize the concept of 3D fake detection and introduce Fake3DGS, a dataset of 3D Gaussian splatting scenes and corresponding rendered views, where fake images are produced by controlled manipulations of geometry, appearance, and spatial layout, while preserving high visual realism. Using this benchmark, we demonstrate that current state-of-the-art 2D detectors struggle to distinguish between original and 3D manipulated images. To bridge this gap, we introduce a 3D-aware detection method that leverages multi-view coherence and features derived from the Gaussian splatting representation. Experimental results demonstrate a substantial improvement in recognizing modified 3D content, underscoring the validity of the new dataset and the necessity for authenticity assessment techniques that extend beyond 2D evidence. Code and data are publicly released for future investigations.

  </details>


- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193)**  
  *Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.28193) · [pdf](https://arxiv.org/pdf/2604.28193.pdf)
  > 💡 提出GenWildSplat，用前馈框架从稀疏无约束图像预测深度、相机参数和3D高斯，结合外观适配与语义分割实现泛化实时重建。

  <details><summary>Abstract</summary>

  Reconstructing 3D scenes from sparse, unposed images remains challenging under real-world conditions with varying illumination and transient occlusions. Existing methods rely on scene-specific optimization using appearance embeddings or dynamic masks, which requires extensive per-scene training and fails under sparse views. Moreover, evaluations on limited scenes raise questions about generalization. We present GenWildSplat, a feed-forward framework for sparse-view outdoor reconstruction that requires no per-scene optimization. Given unposed internet images, GenWildSplat predicts depth, camera parameters, and 3D Gaussians in a canonical space using learned geometric priors. An appearance adapter modulates appearance for target lighting conditions, while semantic segmentation handles transient objects. Through curriculum learning on synthetic and real data, GenWildSplat generalizes across diverse illumination and occlusion patterns. Evaluations on PhotoTourism and MegaScenes benchmark demonstrate state-of-the-art feed-forward rendering quality, achieving real-time inference without test-time optimization

  </details>


- **[FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)**  
  *Zeyu Jiang, Changqing Zhou, Xingxing Zuo, Changhao Chen*  
  `2026-04-30` · `cs.RO` · [abs](https://arxiv.org/abs/2604.28115) · [pdf](https://arxiv.org/pdf/2604.28115.pdf)
  > 💡 针对占据预测依赖3D标注和泛化差的问题，FreeOcc无需训练，结合SLAM、高斯图和视觉语言模型实现开放词汇预测，性能提升2倍以上。

  <details><summary>Abstract</summary>

  Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments. We present FreeOcc, a training-free framework for open-vocabulary occupancy prediction from monocular or RGB-D sequences. Unlike prior approaches that require voxel-level supervision and ground-truth camera poses, FreeOcc operates without 3D annotations, pose ground truth, or any learning stage. FreeOcc incrementally builds a globally consistent occupancy map via a four-layer pipeline: a SLAM backbone estimates poses and sparse geometry; a geometrically consistent Gaussian update constructs dense 3D Gaussian maps; open-vocabulary semantics from off-the-shelf vision-language models are associated with Gaussian primitives; and a probabilistic Gaussian-to-occupancy projection produces dense voxel occupancy. Despite being entirely training-free and pose-agnostic, FreeOcc achieves over $2\times$ improvements in IoU and mIoU on EmbodiedOcc-ScanNet compared to prior self-supervised methods. We further introduce ReplicaOcc, a benchmark for indoor open-vocabulary occupancy prediction, and show that FreeOcc transfers zero-shot to novel environments, substantially outperforming both supervised and self-supervised baselines. Project page: https://the-masses.github.io/freeocc-web/.

  </details>


- **[Generalizable Human Gaussian Splatting via Multi-view Semantic Consistency](https://arxiv.org/abs/2604.25466)**  
  *Jingi Kim, Wonjun Kim*  
  `2026-04-28` · `cs.CV` · [abs](https://arxiv.org/abs/2604.25466) · [pdf](https://arxiv.org/pdf/2604.25466.pdf)
  > 💡 通过跨视图注意力校准多视图潜在特征，解决人体高斯溅射中特征不一致问题，提升稀疏视图渲染质量。

  <details><summary>Abstract</summary>

  Recently, generalizable human Gaussian splatting from sparse-view inputs has been actively studied for the photorealistic human rendering. Most existing methods rely on explicit geometric constraints or predefined structural representations to accurately position 3D Gaussians. Although these approaches have shown the remarkable progress in this field, they still suffer from inconsistent feature representations across multi-view inputs due to complex articulations of the human body and limited overlaps between different views. To address this problem, we propose a novel method to accurately localize 3D Gaussians and ultimately improve the quality of human rendering. The key idea is to unproject latent embeddings encoded from each viewpoint into a shared 3D space through predicted depth maps and recalibrate them belonging to the same body part based on cross-view attention. This helps the model resolve the spatial ambiguity occurring in highly textured regions as well as occluded body parts, thus leading to the accurate localization of 3D Gaussians. Experimental results on benchmark datasets show that the proposed method efficiently improves the performance of generalizable human Gaussian splatting from sparse-view inputs.

  </details>


- **[Spatiotemporal Degradation-Aware 3D Gaussian Splatting for Realistic Underwater Scene Reconstruction](https://arxiv.org/abs/2604.23551)**  
  *Shaohua Liu, Ning Gao, Zuoya Gu, Hongkun Dou, Yue Deng, Hongjue Li*  
  `2026-04-26` · `cs.CV` · [abs](https://arxiv.org/abs/2604.23551) · [pdf](https://arxiv.org/pdf/2604.23551.pdf)
  > 💡 针对水下视频中的时空退化，提出MarineSTD-GS框架，利用成对高斯原语和时空退化建模实现自监督解耦，重建高质量场景。

  <details><summary>Abstract</summary>

  Reconstructing realistic underwater scenes from underwater video remains a meaningful yet challenging task in the multimedia domain. The inherent spatiotemporal degradations in underwater imaging, including caustics, flickering, attenuation, and backscattering, frequently result in inaccurate geometry and appearance in existing 3D reconstruction methods. While a few recent works have explored underwater degradation-aware reconstruction, they often address either spatial or temporal degradation alone, falling short in more real-world underwater scenarios where both types of degradation occur. We propose MarineSTD-GS, a novel 3D Gaussian Splatting-based framework that explicitly models both temporal and spatial degradations for realistic underwater scene reconstruction. Specifically, we introduce two paired Gaussian primitives: Intrinsic Gaussians represent the true scene, while Degraded Gaussians render the degraded observations. The color of each Degraded Gaussian is physically derived from its paired Intrinsic Gaussian via a Spatiotemporal Degradation Modeling (SDM) module, enabling self-supervised disentanglement of realistic appearance from degraded images. To ensure stable training and accurate geometry, we further propose a Depth-Guided Geometry Loss and a Multi-Stage Optimization strategy. We also construct a simulated benchmark with diverse spatial and temporal degradations and ground-truth appearances for comprehensive evaluation. Experiments on both simulated and real-world datasets show that MarineSTD-GS robustly handles spatiotemporal degradations and outperforms existing methods in novel view synthesis with realistic, water-free scene appearances.

  </details>


- **[BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination](https://arxiv.org/abs/2604.19133)**  
  *Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.19133) · [pdf](https://arxiv.org/pdf/2604.19133.pdf)
  > 💡 提出空气-水下跨域3D重建基准BALTIC，评估光照变化，发现3DGS经白平衡预处理可媲美专用方法。

  <details><summary>Abstract</summary>

  Robust 3D reconstruction across varying environmental conditions remains a critical challenge for robotic perception, particularly when transitioning between air and water. To address this, we introduce BALTIC, a controlled benchmark designed to systematically evaluate modern 3D reconstruction methods under variations in medium and lighting. The benchmark comprises 13 datasets spanning two media (air and water) and three lighting conditions (ambient, artificial, and mixed), with additional variations in motion type, scanning pattern, and initialization trajectory, resulting in a diverse set of sequences. Our experimental setup features a custom water tank equipped with a monocular camera and an HTC Vive tracker, enabling accurate ground-truth pose estimation. We further investigate cross-domain reconstruction by augmenting underwater image sequences with a small number of in-air views captured under similar lighting conditions. We evaluate Structure-from-Motion reconstruction using COLMAP in terms of both trajectory accuracy and scene geometry, and use these reconstructions as input to Neural Radiance Fields and 3D Gaussian Splatting methods. The resulting models are assessed against ground-truth trajectories and in-air references, while rendered outputs are compared using perceptual and photometric metrics. Additionally, we perform a color restoration analysis to evaluate radiometric consistency across domains. Our results show that under controlled, texture-consistent conditions, Gaussian Splatting with simple preprocessing (e.g., white balance correction) can achieve performance comparable to specialized underwater methods, although its robustness decreases in more complex and heterogeneous real-world environments

  </details>


- **[A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting](https://arxiv.org/abs/2604.18205)**  
  *Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada, Jan Baturo, Mateusz Capala, Dominik Belter*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18205) · [pdf](https://arxiv.org/pdf/2604.18205.pdf)
  > 💡 聚焦几何精度的NeRF与Gaussian Splatting评估流程与基准，弥补视觉指标对表面形状保真度的忽视。

  <details><summary>Abstract</summary>

  Recent advances in neural rendering have introduced numerous 3D scene representations. Although standard computer vision metrics evaluate the visual quality of generated images, they often overlook the fidelity of surface geometry. This limitation is particularly critical in robotics, where accurate geometry is essential for tasks such as grasping and object manipulation. In this paper, we present an evaluation pipeline for neural rendering methods that focuses on geometric accuracy, along with a benchmark comprising 19 diverse scenes. Our approach enables a systematic assessment of reconstruction methods in terms of surface and shape fidelity, complementing traditional visual metrics.

  </details>


- **[E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969)**  
  *Koya Sakamoto, Taiki Miyanishi, Daichi Azuma, Shuhei Kurita, Shu Morikuni, Naoya Chiba, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17969) · [pdf](https://arxiv.org/pdf/2604.17969.pdf)
  > 💡 针对现有基准无法评估5自由度视点依赖主动感知，提出

  <details><summary>Abstract</summary>

  Visual search in 3D environments requires embodied agents to actively explore their surroundings and acquire task-relevant evidence. However, existing visual search and embodied AI benchmarks, including EQA, typically rely on static observations or constrained egocentric motion, and thus do not explicitly evaluate fine-grained viewpoint-dependent phenomena that arise under unrestricted 5-DoF viewpoint control in real-world 3D environments, such as visibility changes caused by vertical viewpoint shifts, revealing contents inside containers, and disambiguating object attributes that are only observable from specific angles. To address this limitation, we introduce {E3VS-Bench}, a benchmark for embodied 3D visual search where agents must control their viewpoints in 5-DoF to gather viewpoint-dependent evidence for question answering. E3VS-Bench consists of 99 high-fidelity 3D scenes reconstructed using 3D Gaussian Splatting and 2,014 question-driven episodes. 3D Gaussian Splatting enables photorealistic free-viewpoint rendering that preserves fine-grained visual details (e.g., small text and subtle attributes) often degraded in mesh-based simulators, thereby allowing the construction of questions that cannot be answered from a single view and instead require active inspection across viewpoints in 5-DoF. We evaluate multiple state-of-the-art VLMs and compare their performance with humans. Despite strong 2D reasoning ability, all models exhibit a substantial gap from humans, highlighting limitations in active perception and coherent viewpoint planning specifically under full 5-DoF viewpoint changes.

  </details>


- **[Voronoi-guided Bilateral 2D Gaussian Splatting for Arbitrary-Scale Hyperspectral Image Super-Resolution](https://arxiv.org/abs/2604.17727)**  
  *Jie Zhang, Jinkun You, Shi Chen, Yicong Zhou*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17727) · [pdf](https://arxiv.org/pdf/2604.17727.pdf)
  > 💡 针对任意尺度高光谱超分难题，提出Voronoi引导双边2D高斯散射与光谱增强模块，实现灵活空间重建并保持光谱保真度。

  <details><summary>Abstract</summary>

  Most existing hyperspectral image super-resolution methods require modifications for different scales, limiting their flexibility in arbitrary-scale reconstruction. 2D Gaussian splatting provides a continuous representation that is compatible with arbitrary-scale super-resolution. Existing methods often rely on rasterization strategies, which may limit flexible spatial modeling. Extending them to hyperspectral image super-resolution remains challenging, as the task requires adaptive spatial reconstruction while preserving spectral fidelity. This paper proposes GaussianHSI, a Gaussian-Splatting-based framework for arbitrary-scale hyperspectral image super-resolution. We develop a Voronoi-Guided Bilateral 2D Gaussian Splatting for spatial reconstruction. After predicting a set of Gaussian functions to represent the input, it associates each target pixel with relevant Gaussian functions through Voronoi-guided selection. The target pixel is then reconstructed by aggregating the selected Gaussian functions with reference-aware bilateral weighting, which considers both geometric relevance and consistency with low-resolution features. We further introduce a Spectral Detail Enhancement module to improve spectral reconstruction. Extensive experiments on benchmark datasets demonstrate the effectiveness of GaussianHSI over state-of-the-art methods for arbitrary-scale hyperspectral image super-resolution.

  </details>


- **[Incoherent Deformation, Not Capacity: Diagnosing and Mitigating Overfitting in Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.16747)**  
  *Ahmad Droby*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16747) · [pdf](https://arxiv.org/pdf/2604.16747.pdf)
  > 💡 动态高斯泼溅中分割操作导致形变不连贯引发过拟合，弹性能量正则化缩小测试PSNR差距。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian Splatting methods achieve strong training-view PSNR on monocular video but generalize poorly: on the D-NeRF benchmark we measure an average train-test PSNR gap of 6.18 dB, rising to 11 dB on individual scenes. We report two findings that together account for most of that gap. Finding 1 (the role of splitting). A systematic ablation of the Adaptive Density Control pipeline (split, clone, prune, frequency, threshold, schedule) shows that splitting is responsible for over 80% of the gap: disabling split collapses the cloud from 44K to 3K Gaussians and the gap from 6.18 dB to 1.15 dB. Across all threshold-varying ablations, gap is log-linear in count (r = 0.995, bootstrap 95% CI [0.99, 1.00]), which suggests a capacity-based explanation. Finding 2 (the role of deformation coherence). We show that the capacity explanation is incomplete. A local-smoothness penalty on the per-Gaussian deformation field -- Elastic Energy Regularization (EER) -- reduces the gap by 40.8% while growing the cloud by 85%. Measuring per-Gaussian strain directly on trained checkpoints, EER reduces mean strain by 99.72% (median 99.80%) across all 8 scenes; on 8/8 scenes the median Gaussian under EER is less strained than the 1st-percentile (best-behaved) Gaussian under baseline. Alongside EER, we evaluate two further regularizers: GAD, a loss-rate-aware densification threshold, and PTDrop, a jitter-weighted Gaussian dropout. GAD+EER reduces the gap by 48%; adding PTDrop and a soft growth cap reaches 57%. We confirm that coherence generalizes to (a) a different deformation architecture (Deformable-3DGS, +40.6% gap reduction at re-tuned lambda), and (b) real monocular video (4 HyperNeRF scenes, reducing the mean PSNR gap by 14.9% at the same lambda as D-NeRF, with near-zero quality cost). The overfitting in dynamic 3DGS is driven by incoherent deformation, not parameter count.

  </details>


- **[DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416)**  
  *Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi, Hao-Ping Wang, Charlie Li-Ting Tsai, Yu-Cheng Chang, Yu-Lun Liu, Thomas Do, Chin-Teng Lin*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13416) · [pdf](https://arxiv.org/pdf/2604.13416.pdf)
  > 💡 针对无干扰辐射场缺乏大规模数据集的问题，构建含1048场景的DF3DV-1K数据集，用于基准测试并提升方法性能。

  <details><summary>Abstract</summary>

  Advances in radiance fields have enabled photorealistic novel view synthesis. In several domains, large-scale real-world datasets have been developed to support comprehensive benchmarking and to facilitate progress beyond scene-specific reconstruction. However, for distractor-free radiance fields, a large-scale dataset with clean and cluttered images per scene remains lacking, limiting the development. To address this gap, we introduce DF3DV-1K, a large-scale real-world dataset comprising 1,048 scenes, each providing clean and cluttered image sets for benchmarking. In total, the dataset contains 89,924 images captured using consumer cameras to mimic casual capture, spanning 128 distractor types and 161 scene themes across indoor and outdoor environments. A curated subset of 41 scenes, DF3DV-41, is systematically designed to evaluate the robustness of distractor-free radiance field methods under challenging scenarios. Using DF3DV-1K, we benchmark nine recent distractor-free radiance field methods and 3D Gaussian Splatting, identifying the most robust methods and the most challenging scenarios. Beyond benchmarking, we demonstrate an application of DF3DV-1K by fine-tuning a diffusion-based 2D enhancer to improve radiance field methods, achieving average improvements of 0.96 dB PSNR and 0.057 LPIPS on the held-out set (e.g., DF3DV-41) and the On-the-go dataset. We hope DF3DV-1K facilitates the development of distractor-free vision and promotes progress beyond scene-specific approaches.

  </details>


- **[PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction](https://arxiv.org/abs/2604.13153)**  
  *Prajas Wadekar, Venkata Sai Pranav Bachina, Kunal Bhosikar, Ankit Gangwal, Charu Sharma*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13153) · [pdf](https://arxiv.org/pdf/2604.13153.pdf)
  > 💡 针对多视图数据集，通过添加高频棋盘格补丁破坏SfM特征匹配，显著提升3DGS重建误差，无需修改pipeline。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently enabled highly photorealistic 3D reconstruction from casually captured multi-view images. However, this accessibility raises a privacy concern: publicly available images or videos can be exploited to reconstruct detailed 3D models of scenes or objects without the owner's consent. We present PatchPoison, a lightweight dataset-poisoning method that prevents unauthorized 3D reconstruction. Unlike global perturbations, PatchPoison injects a small high-frequency adversarial patch, a structured checkerboard, into the periphery of each image in a multi-view dataset. The patch is designed to corrupt the feature-matching stage of Structure-from-Motion (SfM) pipelines such as COLMAP by introducing spurious correspondences that systematically misalign estimated camera poses. Consequently, downstream 3DGS optimization diverges from the correct scene geometry. On the NeRF-Synthetic benchmark, inserting a 12 X 12 pixel patch increases reconstruction error by 6.8x in LPIPS, while the poisoned images remain unobtrusive to human viewers. PatchPoison requires no pipeline modifications, offering a practical, "drop-in" preprocessing step for content creators to protect their multi-view data.

  </details>


- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992)**  
  *Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar*  
  `2026-04-13` · `cs.RO` · [abs](https://arxiv.org/abs/2604.11992) · [pdf](https://arxiv.org/pdf/2604.11992.pdf)
  > 💡 提出ReefMapGS，融合多模态SLAM与3DGS闭环迭代，摆脱COLMAP依赖，实现大规模水下场景重建与精准位姿估计。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting is a powerful visual representation, providing high-quality and efficient 3D scene reconstruction, but it is crucially dependent on accurate camera poses typically obtained from computationally intensive processes like structure-from-motion that are unsuitable for field robot applications. However, in these domains, multimodal sensor data from acoustic, inertial, pressure, and visual sensors are available and suitable for pose-graph optimization-based SLAM methods that can estimate the vehicle's trajectory and thus our needed camera poses while providing uncertainty. We propose a 3DGS-based incremental reconstruction framework, ReefMapGS, that builds an initial model from a high certainty region and progressively expands to incorporate the whole scene. We reconstruct the scene incrementally by interleaving local tracking of new image observations with optimization of the underlying 3DGS scene. These refined poses are integrated back into the pose-graph to globally optimize the whole trajectory. We show COLMAP-free 3D reconstruction of two underwater reef sites with complex geometry as well as more accurate global pose estimation of our AUV over survey trajectories spanning up to 700 m.

  </details>


- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482)**  
  *Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16482) · [pdf](https://arxiv.org/pdf/2604.16482.pdf)
  > 💡 引入α=峰值内存/地图大小，揭示神经方法内存架构决定部署可行性，提出标准化协议与帕累托分析，提供参考值与预算算法。

  <details><summary>Abstract</summary>

  As vision-based robots navigate larger environments, their spatial memory grows without bound, eventually exhausting computational resources, particularly on embedded platforms (8-16GB shared memory, $<$30W) where adding hardware is not an option. This survey examines the spatial memory efficiency problem across 88 references spanning 52 systems (1989-2025), from occupancy grids to neural implicit representations. We introduce the $α= M_{\text{peak}} / M_{\text{map}}$, the ratio of peak runtime memory (the total RAM or GPU memory consumed during operation) to saved map size (the persistent checkpoint written to disk), exposing the gap between published map sizes and actual deployment cost. Independent profiling on an NVIDIA A100 GPU reveals that $α$ spans two orders of magnitude within neural methods alone, ranging from 2.3 (Point-SLAM) to 215 (NICE-SLAM, whose 47,MB map requires 10GB at runtime), showing that memory architecture, not paradigm label, determines deployment feasibility. We propose a standardized evaluation protocol comprising memory growth rate, query latency, memory-completeness curves, and throughput degradation, none of which current benchmarks capture. Through a Pareto frontier analysis with explicit benchmark separation, we show that no single paradigm dominates within its evaluation regime: 3DGS methods achieve the best absolute accuracy at 90-254,MB map size on Replica, while scene graphs provide semantic abstraction at predictable cost. We provide the first independently measured $α$ reference values and an $α$-aware budgeting algorithm enabling practitioners to assess deployment feasibility on target hardware prior to implementation.

  </details>


- **[AnchorSplat: Feed-Forward 3D Gaussian Splatting with 3D Geometric Priors](https://arxiv.org/abs/2604.07053)**  
  *Xiaoxue Zhang, Xiaoxu Zheng, Yixuan Yin, Tiao Zhao, Kaihua Tang, Michael Bi Mi, Zhan Xu, Dave Zhenyu Chen*  
  `2026-04-08` · `cs.CV` · [abs](https://arxiv.org/abs/2604.07053) · [pdf](https://arxiv.org/pdf/2604.07053.pdf)
  > 💡 提出AnchorSplat，利用3D几何先验的锚点对齐高斯表示替代像素对齐，减少高斯数量，提升重建质量与效率。

  <details><summary>Abstract</summary>

  Recent feed-forward Gaussian reconstruction models adopt a pixel-aligned formulation that maps each 2D pixel to a 3D Gaussian, entangling Gaussian representations tightly with the input images. In this paper, we propose AnchorSplat, a novel feed-forward 3DGS framework for scene-level reconstruction that represents the scene directly in 3D space. AnchorSplat introduces an anchor-aligned Gaussian representation guided by 3D geometric priors (e.g., sparse point clouds, voxels, or RGB-D point clouds), enabling a more geometry-aware renderable 3D Gaussians that is independent of image resolution and number of views. This design substantially reduces the number of required Gaussians, improving computational efficiency while enhancing reconstruction fidelity. Beyond the anchor-aligned design, we utilize a Gaussian Refiner to adjust the intermediate Gaussiansy via merely a few forward passes. Experiments on the ScanNet++ v2 NVS benchmark demonstrate the SOTA performance, outperforming previous methods with more view-consistent and substantially fewer Gaussian primitives.

  </details>


- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638)**  
  *Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05638) · [pdf](https://arxiv.org/pdf/2604.05638.pdf)
  > 💡 针对动态4D场景语言推理不足，提出基于4D Gaussian Splatting与多视图语义共识的查询推理框架，在复杂查询上达

  <details><summary>Abstract</summary>

  Understanding dynamic 4D environments through natural language queries requires not only accurate scene reconstruction but also robust semantic grounding across space, time, and viewpoints. While recent methods using neural representations have advanced 4D reconstruction, they remain limited in contextual reasoning, especially for complex semantics such as interactions, temporal actions, and spatial relations. A key challenge lies in transforming noisy, view-dependent predictions into globally consistent 4D interpretations. We introduce PanopticQuery, a framework for unified query-time reasoning in 4D scenes. Our approach builds on 4D Gaussian Splatting for high-fidelity dynamic reconstruction and introduces a multi-view semantic consensus mechanism that grounds natural language queries by aggregating 2D semantic predictions across multiple views and time frames. This process filters inconsistent outputs, enforces geometric consistency, and lifts 2D semantics into structured 4D groundings via neural field optimization. To support evaluation, we present Panoptic-L4D, a new benchmark for language-based querying in dynamic scenes. Experiments demonstrate that PanopticQuery sets a new state of the art on complex language queries, effectively handling attributes, actions, spatial relationships, and multi-object interactions. A video demonstration is available in the supplementary materials.

  </details>


- **[GenSmoke-GS: A Multi-Stage Method for Novel View Synthesis from Smoke-Degraded Images Using a Generative Model](https://arxiv.org/abs/2604.03039)**  
  *Qida Cao, Xinyuan Hu, Changyue Shi, Jiajun Ding, Zhou Yu, Jun Yu*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03039) · [pdf](https://arxiv.org/pdf/2604.03039.pdf)
  > 💡 针对烟尘降质图像，提出含去雾、大模型增强与3DGS-MCMC的多阶段方法，提升可见性并保持视图一致性，在挑战赛获第一。

  <details><summary>Abstract</summary>

  This paper describes our method for Track 2 of the NTIRE 2026 3D Restoration and Reconstruction (3DRR) Challenge on smoke-degraded images. In this task, smoke reduces image visibility and weakens the cross-view consistency required by scene optimization and rendering. We address this problem with a multi-stage pipeline consisting of image restoration, dehazing, MLLM-based enhancement, 3DGS-MCMC optimization, and averaging over repeated runs. The main purpose of the pipeline is to improve visibility before rendering while limiting scene-content changes across input views. Experimental results on the challenge benchmark show improved quantitative performance and better visual quality than the provided baselines. The code is available at https://github.com/plbbl/GenSmoke-GS. Our method achieved a ranking of 1 out of 14 participants in Track 2 of the NTIRE 3DRR Challenge, as reported on the official competition website: https://www.codabench.org/competitions/13993/#/results-tab.

  </details>


- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209)**  
  *Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2603.29209) · [pdf](https://arxiv.org/pdf/2603.29209.pdf)
  > 💡 在3DGS中插入网格物体时照明与阴影难以一致，提出生成模块预测360° HDR环境图，实现物理逼真渲染并建立首个专用基准。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables high-fidelity reconstruction of scene geometry and appearance. Building on this capability, inserting external mesh objects into reconstructed 3DGS scenes enables interactive editing and content augmentation for immersive applications such as AR/VR, virtual staging, and digital content creation. However, achieving physically consistent lighting and shadows for mesh insertion remains challenging, as it requires accurate scene illumination estimation and multi-view consistent rendering. To address this challenge, we present LightHarmony3D, a novel framework for illumination-consistent mesh insertion in 3DGS scenes. Central to our approach is our proposed generative module that predicts a full 360° HDR environment map at the insertion location via a single forward pass. By leveraging generative priors instead of iterative optimization, our method efficiently captures dominant scene illumination and enables physically grounded shading and shadows for inserted meshes while maintaining multi-view coherence. Furthermore, we introduce the first dedicated benchmark for mesh insertion in 3DGS, providing a standardized evaluation framework for assessing lighting consistency and photorealism. Extensive experiments across multiple real-world reconstruction datasets demonstrate that LightHarmony3D achieves state-of-the-art realism and multi-view consistency.

  </details>


- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781)**  
  *Linfei Li, Lin Zhang, Zhong Wang, Ying Shen*  
  `2026-03-29` · `cs.CV` · [abs](https://arxiv.org/abs/2603.27781) · [pdf](https://arxiv.org/pdf/2603.27781.pdf)
  > 💡 GS3LAM用语义高斯场联合优化位姿与场景，引入深度自适应尺度和随机采样关键帧映射，实现实时稠密语义SLAM。

  <details><summary>Abstract</summary>

  Recently, the multi-modal fusion of RGB, depth, and semantics has shown great potential in dense Simultaneous Localization and Mapping (SLAM). However, a prerequisite for generating consistent semantic maps is the availability of dense, efficient, and scalable scene representations. Existing semantic SLAM systems based on explicit representations are often limited by resolution and an inability to predict unknown areas. Conversely, implicit representations typically rely on time-consuming ray tracing, failing to meet real-time requirements. Fortunately, 3D Gaussian Splatting (3DGS) has emerged as a promising representation that combines the efficiency of point-based methods with the continuity of geometric structures. To this end, we propose GS3LAM, a Gaussian Semantic Splatting SLAM framework that processes multimodal data to render consistent, dense semantic maps in real-time. GS3LAM models the scene as a Semantic Gaussian Field (SG-Field) and jointly optimizes camera poses and the field via multimodal error constraints. Furthermore, a Depth-adaptive Scale Regularization (DSR) scheme is introduced to resolve misalignments between scale-invariant Gaussians and geometric surfaces. To mitigate catastrophic forgetting, we propose a Random Sampling-based Keyframe Mapping (RSKM) strategy, which demonstrates superior performance over common local covisibility optimization methods. Extensive experiments on benchmark datasets show that GS3LAM achieves increased tracking robustness, superior rendering quality, and enhanced semantic precision compared to state-of-the-art methods. Source code is available at https://github.com/lif314/GS3LAM.

  </details>


- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516)**  
  *Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang*  
  `2026-03-29` · `cs.CV` · [abs](https://arxiv.org/abs/2603.27516) · [pdf](https://arxiv.org/pdf/2603.27516.pdf)
  > 💡 针对稀疏视角室内逆渲染，提出语义不变高斯泼溅，利用语义几何先验构建密集场，结合混合光照和材质先验解耦，提升重建与逆渲染质量。

  <details><summary>Abstract</summary>

  We present SGS-Intrinsic, an indoor inverse rendering framework that works well for sparse-view images. Unlike existing 3D Gaussian Splatting (3DGS) based methods that focus on object-centric reconstruction and fail to work under sparse view settings, our method allows to achieve high-quality geometry reconstruction and accurate disentanglement of material and illumination. The core idea is to construct a dense and geometry-consistent Gaussian semantic field guided by semantic and geometric priors, providing a reliable foundation for subsequent inverse rendering. Building upon this, we perform material-illumination disentanglement by combining a hybrid illumination model and material prior to effectively capture illumination-material interactions. To mitigate the impact of cast shadows and enhance the robustness of material recovery, we introduce illumination-invariant material constraint together with a deshadowing model. Extensive experiments on benchmark datasets show that our method consistently improves both reconstruction fidelity and inverse rendering quality over existing 3DGS-based inverse rendering approaches. Our code is available at https://github.com/GrumpySloths/SGS_Intrinsic.github.io.

  </details>


- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197)**  
  *Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh*  
  `2025-12-08` · `cs.CV` · [abs](https://arxiv.org/abs/2512.07197) · [pdf](https://arxiv.org/pdf/2512.07197.pdf)
  > 💡 综述高效3D/4D高斯泼溅，按参数压缩与结构压缩分类方法，系统总结趋势与基准。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a powerful explicit representation enabling real-time, high-fidelity 3D reconstruction and novel view synthesis. However, its practical use is hindered by the massive memory and computational demands required to store and render millions of Gaussians. These challenges become even more severe in 4D dynamic scenes. To address these issues, the field of Efficient Gaussian Splatting has rapidly evolved, proposing methods that reduce redundancy while preserving reconstruction quality. This survey provides the first unified overview of efficient 3D and 4D Gaussian Splatting techniques. For both 3D and 4D settings, we systematically categorize existing methods into two major directions, Parameter Compression and Restructuring Compression, and comprehensively summarize the core ideas and methodological trends within each category. We further cover widely used datasets, evaluation metrics, and representative benchmark comparisons. Finally, we discuss current limitations and outline promising research directions toward scalable, compact, and real-time Gaussian Splatting for both static and dynamic 3D scene representation.

  </details>


- **[Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from Alternating-exposure Monocular Videos](https://arxiv.org/abs/2510.18489)**  
  *Jinfeng Liu, Lingtong Kong, Mi Zhou, Jinwen Chen, Dan Xu*  
  `2025-10-21` · `cs.CV` · [abs](https://arxiv.org/abs/2510.18489) · [pdf](https://arxiv.org/pdf/2510.18489.pdf)
  > 💡 用两阶段高斯泼溅从交替曝光单目LDR视频重建4D HDR场景，无需相机位姿，实现了高质量快速渲染。

  <details><summary>Abstract</summary>

  We introduce Mono4DGS-HDR, the first system for reconstructing renderable 4D high dynamic range (HDR) scenes from unposed monocular low dynamic range (LDR) videos captured with alternating exposures. To tackle such a challenging problem, we present a unified framework with two-stage optimization approach based on Gaussian Splatting. The first stage learns a video HDR Gaussian representation in orthographic camera coordinate space, eliminating the need for camera poses and enabling robust initial HDR video reconstruction. The second stage transforms video Gaussians into world space and jointly refines the world Gaussians with camera poses. Furthermore, we propose a temporal luminance regularization strategy to enhance the temporal consistency of the HDR appearance. Since our task has not been studied before, we construct a new evaluation benchmark using publicly available datasets for HDR video reconstruction. Extensive experiments demonstrate that Mono4DGS-HDR significantly outperforms alternative solutions adapted from state-of-the-art methods in both rendering quality and speed.

  </details>


- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857)**  
  *Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park*  
  `2025-10-04` · `cs.CV` · [abs](https://arxiv.org/abs/2510.03857) · [pdf](https://arxiv.org/pdf/2510.03857.pdf)
  > 💡 通过三阶段渐进剪枝和隐式外观压缩及4D SVQ，将4DGS模型大小减少60%以上，同时保持高质量。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting has emerged as a new paradigm for dynamic scene representation, enabling real-time rendering of scenes with complex motions. However, it faces a major challenge of storage overhead, as millions of Gaussians are required for high-fidelity reconstruction. While several studies have attempted to alleviate this memory burden, they still face limitations in compression ratio or visual quality. In this work, we present OMG4 (Optimized Minimal 4D Gaussian Splatting), a framework that constructs a compact set of salient Gaussians capable of faithfully representing 4D Gaussian models. Our method progressively prunes Gaussians in three stages: (1) Gaussian Sampling to identify primitives critical to reconstruction fidelity, (2) Gaussian Pruning to remove redundancies, and (3) Gaussian Merging to fuse primitives with similar characteristics. In addition, we integrate implicit appearance compression and generalize Sub-Vector Quantization (SVQ) to 4D representations, further reducing storage while preserving quality. Extensive experiments on standard benchmark datasets demonstrate that OMG4 significantly outperforms recent state-of-the-art methods, reducing model sizes by over 60% while maintaining reconstruction quality. These results position OMG4 as a significant step forward in compact 4D scene representation, opening new possibilities for a wide range of applications. Our source code is available at https://minshirley.github.io/OMG4/.

  </details>


- **[WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving](https://arxiv.org/abs/2509.23402)**  
  *Ziyue Zhu, Zhanqian Wu, Zhenxin Zhu, Lijun Zhou, Haiyang Sun, Bing Wan, Kun Ma, Guang Chen, Hangjun Ye, Jin Xie, jian Yang*  
  `2025-09-27` · `cs.CV` · [abs](https://arxiv.org/abs/2509.23402) · [pdf](https://arxiv.org/pdf/2509.23402.pdf)
  > 💡 引入4D感知扩散生成像素对齐4D高斯，结合视频扩散细化，实现高保真时空一致多视角驾驶场景生成。

  <details><summary>Abstract</summary>

  Recent advances in driving-scene generation and reconstruction have demonstrated significant potential for enhancing autonomous driving systems by producing scalable and controllable training data. Existing generation methods primarily focus on synthesizing diverse and high-fidelity driving videos; however, due to limited 3D consistency and sparse viewpoint coverage, they struggle to support convenient and high-quality novel-view synthesis (NVS). Conversely, recent 3D/4D reconstruction approaches have significantly improved NVS for real-world driving scenes, yet inherently lack generative capabilities. To overcome this dilemma between scene generation and reconstruction, we propose WorldSplat, a novel feed-forward framework for 4D driving-scene generation. Our approach effectively generates consistent multi-track videos through two key steps: (i) We introduce a 4D-aware latent diffusion model integrating multi-modal information to produce pixel-aligned 4D Gaussians in a feed-forward manner. (ii) Subsequently, we refine the novel view videos rendered from these Gaussians using a enhanced video diffusion model. Extensive experiments conducted on benchmark datasets demonstrate that WorldSplat effectively generates high-fidelity, temporally and spatially consistent multi-track novel view driving videos. Project: https://wm-research.github.io/worldsplat/

  </details>


- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759)**  
  *Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen*  
  `2025-09-13` · `cs.CV` · [abs](https://arxiv.org/abs/2509.10759) · [pdf](https://arxiv.org/pdf/2509.10759.pdf)
  > 💡 结合4D高斯泼溅与物理光线追踪模拟相机效应，实现快速、可控的高质量动态场景渲染。

  <details><summary>Abstract</summary>

  Common computer vision systems typically assume ideal pinhole cameras but fail when facing real-world camera effects such as fisheye distortion and rolling shutter, mainly due to the lack of learning from training data with camera effects. Existing data generation approaches suffer from either high costs, sim-to-real gaps or fail to accurately model camera effects. To address this bottleneck, we propose 4D Gaussian Ray Tracing (4D-GRT), a novel two-stage pipeline that combines 4D Gaussian Splatting with physically-based ray tracing for camera effect simulation. Given multi-view videos, 4D-GRT first reconstructs dynamic scenes, then applies ray tracing to generate videos with controllable, physically accurate camera effects. 4D-GRT achieves the fastest rendering speed while performing better or comparable rendering quality compared to existing baselines. Additionally, we construct eight synthetic dynamic scenes in indoor environments across four camera effects as a benchmark to evaluate generated videos with camera effects.

  </details>


- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243)**  
  *Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang*  
  `2025-08-26` · `cs.CV` · [abs](https://arxiv.org/abs/2508.19243) · [pdf](https://arxiv.org/pdf/2508.19243.pdf)
  > 💡 首个4D风格化基准，提出基于4D高斯泼溅的Style4D，用MLP实现时空感知风格化与几何保持。

  <details><summary>Abstract</summary>

  We introduce Style4D-Bench, the first benchmark suite specifically designed for 4D stylization, with the goal of standardizing evaluation and facilitating progress in this emerging area. Style4D-Bench comprises: 1) a comprehensive evaluation protocol measuring spatial fidelity, temporal coherence, and multi-view consistency through both perceptual and quantitative metrics, 2) a strong baseline that make an initial attempt for 4D stylization, and 3) a curated collection of high-resolution dynamic 4D scenes with diverse motions and complex backgrounds. To establish a strong baseline, we present Style4D, a novel framework built upon 4D Gaussian Splatting. It consists of three key components: a basic 4DGS scene representation to capture reliable geometry, a Style Gaussian Representation that leverages lightweight per-Gaussian MLPs for temporally and spatially aware appearance control, and a Holistic Geometry-Preserved Style Transfer module designed to enhance spatio-temporal consistency via contrastive coherence learning and structural content preservation. Extensive experiments on Style4D-Bench demonstrate that Style4D achieves state-of-the-art performance in 4D stylization, producing fine-grained stylistic details with stable temporal dynamics and consistent multi-view rendering. We expect Style4D-Bench to become a valuable resource for benchmarking and advancing research in stylized rendering of dynamic 3D scenes. Project page: https://becky-catherine.github.io/Style4D . Code: https://github.com/Becky-catherine/Style4D-Bench .

  </details>


- **[CharacterShot: Controllable and Consistent 4D Character Animation](https://arxiv.org/abs/2508.07409)**  
  *Junyao Gao, Jiaxing Li, Wenran Liu, Yanhong Zeng, Fei Shen, Kai Chen, Yanan Sun, Cairong Zhao*  
  `2025-08-10` · `cs.CV` · [abs](https://arxiv.org/abs/2508.07409) · [pdf](https://arxiv.org/pdf/2508.07409.pdf)
  > 💡 从单张角色图和2D姿态生成可控一致4D动画，采用DiT模型、双注意力与邻域约束4D高斯泼溅，构建大规模数据集。

  <details><summary>Abstract</summary>

  In this paper, we propose \textbf{CharacterShot}, a controllable and consistent 4D character animation framework that enables any individual designer to create dynamic 3D characters (i.e., 4D character animation) from a single reference character image and a 2D pose sequence. We begin by pretraining a powerful 2D character animation model based on a cutting-edge DiT-based image-to-video model, which allows for any 2D pose sequnce as controllable signal. We then lift the animation model from 2D to 3D through introducing dual-attention module together with camera prior to generate multi-view videos with spatial-temporal and spatial-view consistency. Finally, we employ a novel neighbor-constrained 4D gaussian splatting optimization on these multi-view videos, resulting in continuous and stable 4D character representations. Moreover, to improve character-centric performance, we construct a large-scale dataset Character4D, containing 13,115 unique characters with diverse appearances and motions, rendered from multiple viewpoints. Extensive experiments on our newly constructed benchmark, CharacterBench, demonstrate that our approach outperforms current state-of-the-art methods. Code, models, and datasets will be publicly available at https://github.com/Jeoyal/CharacterShot.

  </details>


- **[4DVD: Cascaded Dense-view Video Diffusion Model for High-quality 4D Content Generation](https://arxiv.org/abs/2508.04467)**  
  *Shuzhou Yang, Xiaodong Cun, Xiaoyu Li, Yaowei Li, Jian Zhang*  
  `2025-08-06` · `cs.CV` · [abs](https://arxiv.org/abs/2508.04467) · [pdf](https://arxiv.org/pdf/2508.04467.pdf)
  > 💡 提出级联扩散模型4DVD，将4D生成解耦为布局预测和结构感知生成，由单目视频生成高质量密集视图视频，实现SOTA的4D内容生成。

  <details><summary>Abstract</summary>

  Given the high complexity of directly generating high-dimensional data such as 4D, we present 4DVD, a cascaded video diffusion model that generates 4D content in a decoupled manner. Unlike previous multi-view video methods that directly model 3D space and temporal features simultaneously with stacked cross view/temporal attention modules, 4DVD decouples this into two subtasks: coarse multi-view layout generation and structure-aware conditional generation, and effectively unifies them. Specifically, given a monocular video, 4DVD first predicts the dense view content of its layout with superior cross-view and temporal consistency. Based on the produced layout priors, a structure-aware spatio-temporal generation branch is developed, combining these coarse structural priors with the exquisite appearance content of input monocular video to generate final high-quality dense-view videos. Benefit from this, explicit 4D representation~(such as 4D Gaussian) can be optimized accurately, enabling wider practical application. To train 4DVD, we collect a dynamic 3D object dataset, called D-Objaverse, from the Objaverse benchmark and render 16 videos with 21 frames for each object. Extensive experiments demonstrate our state-of-the-art performance on both novel view synthesis and 4D generation. Our project page is https://4dvd.github.io/

  </details>


- **[PhysGaia: A Physics-Aware Benchmark with Multi-Body Interactions for Dynamic Novel View Synthesis](https://arxiv.org/abs/2506.02794)**  
  *Mijeong Kim, Gunhee Kim, Jungyoon Choi, Wonjae Roh, Bohyung Han*  
  `2025-06-03` · `cs.GR` · [abs](https://arxiv.org/abs/2506.02794) · [pdf](https://arxiv.org/pdf/2506.02794.pdf)
  > 💡 针对动态新视角合成缺乏物理感知基准的问题，提出包含多体交互与多种材料的PhysGaia，提供3D轨迹和物理参数以评估物理建模一致性。

  <details><summary>Abstract</summary>

  We introduce PhysGaia, a novel physics-aware benchmark for Dynamic Novel View Synthesis (DyNVS) that encompasses both structured objects and unstructured physical phenomena. While existing datasets primarily focus on photorealistic appearance, PhysGaia is specifically designed to support physics-consistent dynamic reconstruction. Our benchmark features complex scenarios with rich multi-body interactions, where objects realistically collide and exchange forces. Furthermore, it incorporates a diverse range of materials, including liquid, gas, textile, and rheological substance, moving beyond the rigid-body assumptions prevalent in prior work. To ensure physical fidelity, all scenes in PhysGaia are generated using material-specific physics solvers that strictly adhere to fundamental physical laws. We provide comprehensive ground-truth information, including 3D particle trajectories and physical parameters (e.g., viscosity), enabling the quantitative evaluation of physical modeling. To facilitate research adoption, we also provide integration pipelines for recent 4D Gaussian Splatting models along with our dataset and their results. By addressing the critical shortage of physics-aware benchmarks, PhysGaia can significantly advance research in dynamic view synthesis, physics-based scene understanding, and the integration of deep learning with physical simulation, ultimately enabling more faithful reconstruction and interpretation of complex dynamic scenes.

  </details>


- **[Disentangled 4D Gaussian Splatting: Rendering High-Resolution Dynamic World at 343 FPS](https://arxiv.org/abs/2503.22159)**  
  *Hao Feng, Hao Sun, Wei Xie, Zhi Zuo, Zhengzhe Liu*  
  `2025-03-28` · `cs.GR` · [abs](https://arxiv.org/abs/2503.22159) · [pdf](https://arxiv.org/pdf/2503.22159.pdf)
  > 💡 通过解耦4D高斯的时空分量并引入动态2D高斯与流损失，实现了343 FPS的高质量动态场景渲染。

  <details><summary>Abstract</summary>

  While dynamic novel view synthesis from 2D videos has seen progress, achieving efficient reconstruction and rendering of dynamic scenes remains a challenging task. In this paper, we introduce Disentangled 4D Gaussian Splatting (Disentangled4DGS), a novel representation and rendering pipeline that achieves real-time performance without compromising visual fidelity. Disentangled4DGS decouples the temporal and spatial components of 4D Gaussians, avoiding the need for slicing first and four-dimensional matrix calculations in prior methods. By projecting temporal and spatial deformations into dynamic 2D Gaussians and deferring temporal processing, we minimize redundant computations of 4DGS. Our approach also features a gradient-guided flow loss and temporal splitting strategy to reduce artifacts. Experiments demonstrate a significant improvement in rendering speed and quality, achieving 343 FPS when render 1352*1014 resolution images on a single RTX3090 while reducing storage requirements by at least 4.5%. Our approach sets a new benchmark for dynamic novel view synthesis, outperforming existing methods on both multi-view and monocular dynamic scene datasets.

  </details>


- **[SDD-4DGS: Static-Dynamic Aware Decoupling in Gaussian Splatting for 4D Scene Reconstruction](https://arxiv.org/abs/2503.09332)**  
  *Dai Sun, Huhao Guan, Kun Zhang, Xike Xie, S. Kevin Zhou*  
  `2025-03-12` · `cs.CV` · [abs](https://arxiv.org/abs/2503.09332) · [pdf](https://arxiv.org/pdf/2503.09332.pdf)
  > 💡 针对动静不加区分问题，提出SDD-4DGS，引入概率动态感知系数实现高斯泼溅的动静解耦，提升重建保真度。

  <details><summary>Abstract</summary>

  Dynamic and static components in scenes often exhibit distinct properties, yet most 4D reconstruction methods treat them indiscriminately, leading to suboptimal performance in both cases. This work introduces SDD-4DGS, the first framework for static-dynamic decoupled 4D scene reconstruction based on Gaussian Splatting. Our approach is built upon a novel probabilistic dynamic perception coefficient that is naturally integrated into the Gaussian reconstruction pipeline, enabling adaptive separation of static and dynamic components. With carefully designed implementation strategies to realize this theoretical framework, our method effectively facilitates explicit learning of motion patterns for dynamic elements while maintaining geometric stability for static structures. Extensive experiments on five benchmark datasets demonstrate that SDD-4DGS consistently outperforms state-of-the-art methods in reconstruction fidelity, with enhanced detail restoration for static structures and precise modeling of dynamic motions. The code will be released.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (214) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[MonoPhysics: Estimating Geometry, Appearance, and Physical Parameters from Monocular Videos](https://arxiv.org/abs/2605.30320)**  
  *Daniel Rho, Jun Myeong Choi, Matthew Thornton, Biswadip Dey, Roni Sengupta*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30320) · [pdf](https://arxiv.org/pdf/2605.30320.pdf)
  > 💡 单目视频缺乏几何约束，提出结合3DGS和可微MPM仿真的MonoPhysics，通过三个视觉-物理桥梁联合优化几何、外观和物理参数，性能媲美多视图方法。

  <details><summary>Abstract</summary>

  Existing inverse physics methods recover physical parameters from multi-view videos, where geometric constraints across views resolve scale and 3D structure. In monocular settings, however, such constraints are absent, leading to severe scale ambiguity, inaccurate geometry, and weak coupling between appearance optimization and physical simulation. We propose MonoPhysics, a framework for monocular inverse physics estimation of deformable objects using differentiable MPM simulation and 3D Gaussian Splatting, which jointly optimizes geometry, appearance, and physical parameters from a single camera view. We address these challenges through three visual-physical bridges: global scale alignment, physics-aware geometry refinement, and a differentiable position map, which together enable accurate optimization from monocular observations alone. We evaluate on Vid2Sim and our new dataset of elastic and plastic objects, showing that MonoPhysics outperforms existing baselines in monocular settings and achieves performance comparable to multi-view baselines using only a single camera. Our project page is available at https://daniel03c1.github.io/MonoPhysics/

  </details>


- **[PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions](https://arxiv.org/abs/2605.30268)**  
  *Omer Benishu, Gal Fiebelman, Sagie Benaim*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30268) · [pdf](https://arxiv.org/pdf/2605.30268.pdf)
  > 💡 结合运动扩散与物质点物理模拟，以3D高斯为统一表示，生成物理一致的4D人-物交互动态场景。

  <details><summary>Abstract</summary>

  We address the task of generating physically accurate and visually faithful 4D Human-Object Interaction (HOI). Given a static 3D human and target object represented as 3D Gaussian Splats (3DGS), our goal is to synthesize dynamic scenes where the human actively engages with the object through actions, such as punching or kicking, in accordance with a given input text. To this end, we introduce PhyGenHOI, a novel framework that couples generative human motion with an explicit physical object simulation. We model the human as a semantic agent driven by a Motion Diffusion Model (MDM) and the object as a physical agent simulated via the Material Point Method (MPM), utilizing 3D Gaussians as a unified, differentiable representation. We supervise their interaction through three coupled mechanisms: (1) A Windowed Attraction Loss that temporally synchronizes generative motion to intercept the object; (2) A Contact-Driven Re-simulation step that triggers physically consistent momentum transfer upon impact; and (3) A Masked Video-SDS objective that injects video-based priors to enhance contact fidelity. Experiments show PhyGenHOI generates physically consistent 4D HOI across diverse actions, humans, and objects, outperforming baselines. Project page and videos: https://omerbenishu.github.io/PhyGenHOI/

  </details>


- **[FRUC: Feedforward Dynamic Scene Reconstruction from Uncalibrated Collaborative Driving Views](https://arxiv.org/abs/2605.29997)**  
  *Yihang Tao, Yu Guo, Zhengru Fang, Haonan An, Yuguang Fang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29997) · [pdf](https://arxiv.org/pdf/2605.29997.pdf)
  > 💡 提出无标定协作驾驶动态场景重建方法FRUC，利用前馈3D高斯和因果遮挡场实现高效单次重建，显著提升渲染质量。

  <details><summary>Abstract</summary>

  We present FRUC, a feed-forward 3D Gaussian splatting framework for dynamic scene reconstruction from uncalibrated collaborative driving views. Existing multi-agent reconstruction frameworks are often hindered by rigid prerequisites, demanding precise spatial calibration and slow per-scene optimization. In this paper, we rethink this task by conceptualizing a distributed multi-vehicle network as a spatio-temporally unstructured ego-centric multi-camera system, where the core challenge lies in enhancing ego-centric occluded geometry through collaboration without degrading the ego's accurately observed visible geometry, while preserving reconstruction efficiency. For efficient reconstruction, FRUC is built upon a visual grounded geometric Transformer backbone to enable one-shot, calibration-free inference from a flexible number of multi-vehicle views. To achieve non-destructive geometric supplementation under uncalibrated cross-agent misalignment, FRUC first introduces an ego-centric causal occlusion field that explicitly derives occlusion evolution as latent priors by modeling agent-wise spatio-temporal correlations. Guided by these occlusion priors, it further formulates cross-agent integration as a deterministic residual denoising process via zero-initialized injection, turning challenging cross-agent fusion into bounded residual learning for robust collaborative blind-spot completion. Through extensive evaluations on the real-world V2XReal and UrbanIng-V2X datasets, FRUC is shown to be a new state-of-the-art for the scene reconstruction of dynamic collaborative driving environments, significantly outperforming existing methods in both rendering quality and efficiency.

  </details>


- **[DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](https://arxiv.org/abs/2605.29879)**  
  *Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29879) · [pdf](https://arxiv.org/pdf/2605.29879.pdf)
  > 💡 提出混合实例感知3D高斯动态场景图系统，结合概率体素与显式高斯实现跨模态融合和动态更新，零样本3D视觉定位和语义分割性能领先。

  <details><summary>Abstract</summary>

  Integrating open-vocabulary semantic information into dynamic 3D scene representations is essential for long-term embodied scene understanding. However, existing methods often suffer from fragile instance association due to incomplete cross-view cues, while their limited ability to handle object-level topological changes restricts long-term robotic task execution. Moreover, current 3D scene understanding methods either rely on simple feature matching without explicit spatial reasoning or assume offline ground-truth 3D geometry. To address these challenges, we present DGSG-Mind, a hybrid instance-aware 3D Gaussian dynamic scene graph system with an embodied reasoning agent. Our system couples a probabilistic voxel grid with explicit 3D Gaussians to enable robust cross-modal instance fusion and incremental semantic mapping. It handles dynamic changes through Gaussian-based visual relocalization and localized masked refinement guided by geometric-semantic consistency. Built on the instance Gaussian map, DGSG-Mind further constructs a hierarchical scene graph and develops the 3D Gaussian Mind, which integrates structural relations, spatial-semantic information, and visually annotated RoI Gaussian renderings for multimodal reasoning. Extensive experiments show that DGSG-Mind achieves the best zero-shot 3DVG performance among methods operating on self-reconstructed maps, while also delivering strong performance in 3D open-vocabulary semantic segmentation and scene reconstruction. We further deploy DGSG-Mind on real-world robots to demonstrate its target-oriented reasoning and dynamic update capabilities. The project page of DGSG-Mind is available at https://icr-lab.github.io/DGSG-Mind

  </details>


- **[R5DGS: Semantic-Aware 4D Gaussian Splatting with Rigid Body Constraints for Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.25909)**  
  *Denis Gridusov, Maxim Popov, Sergey Kolyubin*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25909) · [pdf](https://arxiv.org/pdf/2605.25909.pdf)
  > 💡 利用语义编码和CLIP查找表实现物体关联，通过刚体中心推理加速外推，实现高效动态场景重建。

  <details><summary>Abstract</summary>

  Reconstructing and predicting dynamic 3D scenes from multi-view videos is a foundational task for robotics, AR/VR, and digital twins. Recent physics-informed Gaussian Splatting methods achieve impressive future frame extrapolation but lack semantic awareness and suffer from large computational overhead. We introduce $\textbf{R5DGS}$, a framework that augments a physics-driven 4D Gaussian representation with compact Identity Encoding vectors, enabling precise Gaussian-to-object association. By constructing an offline CLIP-based object lookup table, we support open-vocabulary text prompting to retrieve and render object-specific Gaussians across arbitrary timestamps and viewpoints. Furthermore, we propose a rigid-body inference constraint that predicts and integrates physical dynamics exclusively for object centroids, propagating motion to associated Gaussians via relative transformations. This optimization yields a 11 FPS speedup during extrapolation without compromising trajectories plausibility.

  </details>


- **[SplitAvatar: One-shot Head Avatar with Autoregressive Gaussian Splitting](https://arxiv.org/abs/2605.25751)**  
  *Hongzhe Liao, Chuhua Xian, Hongmin Cai, Haiyang Liu, Fa-Ting Hong*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25751) · [pdf](https://arxiv.org/pdf/2605.25751.pdf)
  > 💡 基于单图重建可动头部头像，提出自回归图分裂网络逐步细化高斯分布，解决数量不匹配问题，提升表情细节与重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) provides an efficient method for high-quality scene reconstruction using anisotropic Gaussians. Recently, 3DGS-based methods have significantly improved the rendering quality of human avatars while enabling real-time performance. However, existing methods suffer from a magnitude mismatch in the number of Gaussians generated by image-based and 3DMM-based approaches. This discrepancy results in reconstructed expressions that lack fine-grained detail. In this paper, we introduce a novel method for reconstructing an animatable head avatar from a single image. We propose a Graph splitting network to progressively generate Gaussians from coarse to fine using an autoregressive architecture. To address the graph inconsistency caused by split Gaussians, we employ a mesh topology extension method to align the GNN's connectivity with the increased Gaussian count. Furthermore, we introduce a novel density control method that includes a gating mechanism that generates soft masks for Gaussians, preventing over-densification after the splitting operation. This allows for dynamic control over Gaussian density across different facial regions. For smooth and rapid training, we employ a delayed filtering strategy to avoid re-computing the graph topology during training. Experimental results demonstrate that our autoregressive structure effectively improves expression representation ability by progressively splitting Gaussians. This process, enabled by the GNN-guided splitting, synthesizes more precise facial details and achieves higher reconstruction quality.

  </details>


- **[Physics-Aware 3D Gaussian Editing for Driving Scene Generation](https://arxiv.org/abs/2605.25373)**  
  *Feng Zhou, Jian Zhang, Yuhang Sun, He Wang, Qiong Wen, Debao Kong, Tieru Wu, Rui Ma*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25373) · [pdf](https://arxiv.org/pdf/2605.25373.pdf)
  > 💡 现有3DGS编辑缺乏道路几何修改和车辆动力学耦合，提出RoVES通过单图驱动和半车模型实现物理感知的快速道路插入与姿态校正。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has shown great potential in autonomous driving simulation and data generation, enabling photorealistic reconstruction and flexible scene manipulation. However, existing 3DGS scene editing methods have limited support for road geometry editing (e.g., inserting speed humps or sunken roads), and generally do not couple such edits with plausible vehicle-road interaction dynamics. Such editing is essential for generating training data under extreme driving scenarios or evaluating system reliability under these road irregularities. Moreover, many optimization-based methods require minutes of per-edit refinement, while existing efficient alternatives mainly focus on appearance-level or object-level manipulation rather than physics-aware road irregularity editing. To address these limitations, we propose RoVES, a Road-and-Vehicle Editing System for physics-aware 3D Gaussian editing in driving scenes. RoVES enables single-image-driven road geometry insertion and couples the edited road profile with a 4-DOF half-car vehicle dynamics model to achieve physics-aware vehicle pose correction in vertical displacement and pitch. RoVES inserts road elements in a one-shot, optimization-free pipeline (1.84s), and the full pipeline (including color transfer and vehicle-dynamics-based pose correction) completes in 6.24s; it edits dynamic vehicles via pose editing and corrects poses frame-by-frame to approximate dynamics-consistent vertical displacement and pitch responses. Experiments on the Waymo dataset show that RoVES provides practical efficiency and competitive visual consistency for physics-aware driving scene generation.

  </details>


- **[Full-4D: Generating Full-Scope 4D Scenes from a Single-View Video](https://arxiv.org/abs/2605.25500)**  
  *Tingxi Chen, Ke Hao, Yabo Chen, Zhengxue Cheng, Rong Xie, Li Song, Haibin Huang, Chi Zhang, Xuelong Li*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25500) · [pdf](https://arxiv.org/pdf/2605.25500.pdf)
  > 💡 从单视角视频生成全范围4D场景，通过多

  <details><summary>Abstract</summary>

  Generating 4D scenes from a single-view video is inherently ill-posed: a single viewpoint lacks the information needed to recover a complete, dynamic scene with full coverage. Existing methods are typically limited to monocular videos, simple 3D effects, or only small viewpoint perturbations around the original viewpoint, falling short of true 4D generation. Meanwhile, the lack of large-scale datasets capturing full-scope 4D scenes with synchronized multi-view videos further hinders progress in this direction. We propose a novel single-view video-to-4D framework that casts full-scope 4D generation as a multi-view video synthesis followed by optimization-based 4D reconstruction from the generated views. To instantiate this formulation end-to-end, we make three key contributions. First, we introduce Real-MV-4D, a large-scale dataset of synchronized multi-view videos captured in diverse real-world environments to provide the 4D supervision. Second, we train a multi-view video diffusion model driven by a novel fused time(T)-view(V) attention mechanism that directly embeds geometric reprojection priors and explicit camera conditioning into its view-time interactions. Unlike basic feature fusion, this direct binding strictly aligns the generation process with physical 3D priors to produce a dense, synchronized T$\times $V video grid. Third, rather than relying on non-interactive and inconsistent 2D video interpolations, we lift the synthesized multi-view videos into an explicit 4D representation (i.e. 4DGS), regularized by a Flow Matching Distillation loss that exploits the multi-view prior to improve novel-view rendering. Extensive experiments demonstrate that our method outperforms existing approaches in both visual fidelity and geometric consistency, enabling full-scope 4D scene generation from single-view videos.

  </details>


- **[Learning a Particle Dynamics Model with Real-world Videos](https://arxiv.org/abs/2605.23845)**  
  *Chanho Kim, Suhas V. Sumukh, Li Fuxin*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23845) · [pdf](https://arxiv.org/pdf/2605.23845.pdf)
  > 💡 从真实视频无监督学习高斯泼溅粒子动力学模型，通过渲染监督训练，避免模拟到真实差距。

  <details><summary>Abstract</summary>

  Data-driven learning approaches for physics simulation, sometimes referred to as world models, have emerged as promising alternatives to traditional physics simulators due to their differentiable nature. Prior work has demonstrated impressive results in predicting the motions of rigid and non-rigid objects in complex scenes involving multiple interacting bodies. However, these models are typically trained in simulated environments because obtaining perfect state information such as complete scene point clouds and point correspondences over time is challenging in real-world settings. This reliance on synthetic data can limit their applicability when the sim-to-real gap is large. In this work, we aim to overcome these limitations by introducing a novel framework for training neural object dynamics models directly from unlabeled real-world videos. Specifically, we propose to learn a particle-based dynamics model compatible with a Gaussian splatting framework, which operates on dense particles derived from Gaussians (i.e., particles with scales and rotations) and predicts their position and rotation changes over time. The model is trained via rendering supervision, enabling learning from real-world videos without requiring particle-level labeled states. Our model operates directly on dense Gaussians without relying on heuristic subsampling anchor points. To enable this study, we also present a real-world dataset consisting of about 500 videos capturing diverse object interactions.

  </details>


- **[RiGS: Rigid-aware 4D Gaussian Splatting from a Single Monocular Video](https://arxiv.org/abs/2605.23672)**  
  *Chenyu Wu, Wanhua Li, Zhu-Tian Chen, Hanspeter Pfister*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23672) · [pdf](https://arxiv.org/pdf/2605.23672.pdf)
  > 💡 针对单目视频动态场景重建，RiGS引入静态、刚体、瞬态高斯基元，结合物体动态掩码与场景流，实现多时间

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from monocular videos is a fundamental yet highly challenging task, as real-world motions often involve both long-term smooth transformations and short-term complex deformations. Existing methods either struggle to maintain temporal consistency or fail to capture high-frequency dynamics due to limited motion modeling capacity. In this work, we present Rigid-aware 4D Gaussian Splatting (RiGS), which simultaneously captures motions across multiple temporal scales. Specifically, RiGS introduces three types of Gaussian primitives: static, rigid, and transient, which represent static backgrounds, long-term low-frequency motions, and short-term high-frequency dynamics, respectively. An object-wise dynamic mask is proposed to aggregate long-range spatiotemporal motion information and guide the decomposition of static and dynamic regions. To jointly model motion across scales, rigid Gaussians are allowed to transition into transient Gaussians based on their temporal duration, and both are optimized under scene flow guidance, providing dense 3D motion supervision. Extensive experiments demonstrate that RiGS achieves state-of-the-art performance on novel view synthesis benchmarks. Code is available at \hyperlink{https://github.com/ladvu/RiGS}{https://github.com/ladvu/RiGS}.

  </details>


- **[Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving](https://arxiv.org/abs/2605.22809)**  
  *Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng, Zehao Zhu, Meng-Li Shih, Xander Masotto, Shih-Yang Su, Kanaad V Parvate, Tiancheng Ge, Linn Bieske, Dragomir Anguelov, Mingxing Tan, Chiyu Max Jiang*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22809) · [pdf](https://arxiv.org/pdf/2605.22809.pdf)
  > 💡 针对行车记录仪视频与多模态传感器数据不兼容问题，用4DGS和扩散模型实现跨传感器转换，解锁外部数据源。

  <details><summary>Abstract</summary>

  Robust training and validation of Autonomous Driving Systems (ADS) require massive, diverse datasets. Proprietary data collected by Autonomous Vehicle (AV) fleets, while high-fidelity, are limited in scale, diversity of sensor configurations, as well as geographic and long-tail-behavioral coverage. In contrast, in-the-wild data from sources like dashcams offers immense scale and diversity, capturing critical long-tail scenarios and novel environments. However, this unstructured, in-the-wild video data is incompatible with ADS expecting structured, multi-modal sensor inputs for validation and training. To bridge this data gap, we propose Sensor2Sensor, a novel generative modeling paradigm that translates in-the-wild monocular dashcam videos into a high-fidelity, multi-modal sensor suite (AV logs) comprising multi-view camera images and LiDAR point clouds. A core challenge is the lack of paired training data. We address this by converting real AV logs into dashcam-style videos via 4D Gaussian Splatting (4DGS) reconstruction and novel-view rendering. Sensor2Sensor then utilizes a diffusion architecture to perform the generative conversion. We perform comprehensive quantitative evaluations on the fidelity and realism of the generated sensor data. We demonstrate Sensor2Sensor's practical utility by converting challenging in-the-wild internet and dashcam footage into realistic, multi-modal data formats, further unlocking vast external data sources for AV development.

  </details>


- **[4D-GSW: Kinematic-Aware Spatio-Temporal Consistent Watermarking for 4D Gaussian Splatting](https://arxiv.org/abs/2605.22342)**  
  *Sifan Zhou, Hang Zhang, Yuhang Wang, Ming Li*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22342) · [pdf](https://arxiv.org/pdf/2605.22342.pdf)
  > 💡 针对4D高斯溅射水印缺乏运动感知导致时序伪影，引入时空曲率度量与HMM-MRF能量模型实现鲁棒且高时空一致的水印嵌入。

  <details><summary>Abstract</summary>

  While 4D Gaussian Splatting (4DGS) has revolutionized high-fidelity dynamic reconstruction, safeguarding the intellectual property of these assets remains an open challenge. Conventional steganographic techniques often neglect the underlying kinematic manifolds, triggering non-physical artifacts such as severe temporal flickering and "FVD collapse". To address this, we propose \textbf{4D-GSW}, a kinematic-aware watermarking framework designed to embed robust copyright information while preserving high spatio-temporal consistency. Unlike prior 4D steganography that primarily focuses on opacity-guided invisibility, our approach explicitly addresses the physical coherence of motion trajectories. We introduce a \textbf{Spatio-Temporal Curvature (STC)} metric to identify "Dynamic Instants," adaptively gating watermark gradient injection to shield critical motion manifolds from non-physical perturbations. To ensure global coherence across complex deformations, we formulate a joint \textbf{HMM-MRF energy minimization} model that synchronizes watermark phases within both temporal trajectories and spatial neighborhoods. Furthermore, an \textbf{anisotropic gradient routing} mechanism ensures that watermark embedding remains strictly decoupled from photometric reconstruction fidelity. Extensive experiments have demonstrated the superior performance of our method in robustly hiding watermarks while resisting various attacks and maintaining high rendering quality and spatiotemporal consistency.

  </details>


- **[No Pose, No Problem in 4D: Feed-Forward Dynamic Gaussians from Unposed Multi-View Videos](https://arxiv.org/abs/2605.22190)**  
  *Matteo Balice, Yanik Kunzi, Chenyangguang Zhang, Matteo Matteucci, Marc Pollefeys, Sungwhan Hong*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22190) · [pdf](https://arxiv.org/pdf/2605.22190.pdf)
  > 💡 提出无位姿多视图动态高斯泼溅方法，通过速度分解与双向运动编码器，实现高效前馈4D重建，性能超越以往基线。

  <details><summary>Abstract</summary>

  Recent feed-forward 3D gaussian splatting methods have made dramatic progress on individual aspects of 3D scene reconstruction, but no existing method jointly addresses dynamic content, multi-view input, and unknown camera poses in a single feed-forward pass. Methods that handle dynamics either require accurate camera poses or accept only monocular input; pose-free multi-view methods address only static scenes; and per-scene optimization methods bridge some of these gaps but at minutes-to-hours cost per scene. We introduce NoPo4D, the first feed-forward system that addresses this empty quadrant. Building on a pretrained geometry backbone and recent 4D Gaussian frameworks, NoPo4D introduces a velocity decomposition that splits Gaussian motion into per-pixel image-plane shifts and depth changes, allowing direct supervision from pseudo ground-truth optical flow on the 2D component. This sidesteps both the differentiable rendering that couples prior posed methods to pose accuracy and the 3D motion ground truth that prior pose-free methods require. The system is rounded out by a bidirectional motion encoder for cross-view and cross-frame feature aggregation, and view-dependent opacity that mitigates cross-view and cross-timestep Gaussian misalignments. On four multi-view dynamic benchmarks, NoPo4D consistently outperforms prior feed-forward baselines, and with an optional post-optimization stage surpasses per-scene optimization methods, while running orders of magnitude faster.

  </details>


- **[TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.22069)**  
  *Hyeseong Kim, Geonhui Son, Deukhee Lee, Dosik Hwang*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22069) · [pdf](https://arxiv.org/pdf/2605.22069.pdf)
  > 💡 针对稀疏视图下3DGS点云稀疏问题，采用薄板样条对齐反投影点初始化，提升几何精度与重建质量。

  <details><summary>Abstract</summary>

  Novel view synthesis from sparse-view inputs poses a significant challenge in 3D computer vision, particularly for achieving high-quality scene reconstructions with limited viewpoints. We introduce TWINGS, a framework that enhances 3D Gaussian Splatting (3DGS) by directly addressing point sparsity. We employ Thin Plate Splines (TPS), a smooth non-rigid deformation model that minimizes bending energy to estimate a globally coherent warp from control-point correspondences, to align backprojected points from estimated depth with triangulated 3D control points, yielding calibrated backprojected points. By sampling these calibrated points near the control points, TWINGS provides a fast and geometrically accurate initialization for 3DGS, ultimately improving structural detail preservation and color fidelity in reconstructed scenes. Extensive experiments on DTU, LLFF, and Mip-NeRF360 demonstrate that TWINGS consistently outperforms existing methods, delivering detailed and accurate reconstructions under sparse-view scenarios.

  </details>


- **[Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935)**  
  *Peifeng Jiang, Hong Liu, Jin Jin, Wenshuai Wang, Xia Li*  
  `2026-05-21` · `cs.RO` · [abs](https://arxiv.org/abs/2605.21935) · [pdf](https://arxiv.org/pdf/2605.21935.pdf)
  > 💡 提出多模态交互场，联合不确定感知3DGS与动态更新，实现动态环境下人形机器人鲁棒导航，重定位成功率从12%提升至94%。

  <details><summary>Abstract</summary>

  Safe manipulation-oriented navigation for humanoid robots requires scene memory that remains reliable under locomotion-induced perceptual distortion, environmental changes, and interaction-level geometric safety constraints. Existing semantic mapping and scene-graph systems are difficult to deploy directly in this setting because they often assume stable camera trajectories, static environments, or coarse object geometry. We introduce the Multi-modal Interactive Field (MIF), a humanoid-oriented system that integrates confidence-aware semantic 3D Gaussian Splatting, discrepancy-triggered spatial memory updates, and task-driven geometric reconstruction within a closed-loop perception-adaptation pipeline. MIF couples three fields: an uncertainty-aware 3DGS Appearance Field that suppresses gait-induced blur, a Spatial Field that maintains topological memory, and a Geometry Field that supports Interaction Pose Safety (IPS) before manipulation. A discrepancy detection score is introduced to separate locomotion-induced false-positive changes from persistent changes and updates only locally inconsistent regions. On a Unitree-G1 humanoid in a real dynamic office, MIF improves relocation success in non-static environments from 12% to 94% compared with static scene-graph memory, while reducing semantic memory footprint by 91.4% through feature distillation for practical online operation. Project page and code: https://ziya-jiang.github.io/MIF-homepage/

  </details>


- **[Latent Dynamics for Full Body Avatar Animation](https://arxiv.org/abs/2605.21478)**  
  *Shichong Peng, Chengxiang Yin, Fei Jiang, Zhongshi Jiang, Lingchen Yang, Qingyang Tan, Amin Jourabloo, Jason Saragih, Ke Li, Christian Häne*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.21478) · [pdf](https://arxiv.org/pdf/2605.21478.pdf)
  > 💡 为松散衣物动态建模，提出基于3D高斯与transformer的潜在动力学残差模型，实现历史依赖、时间连贯且可控的全身动画。

  <details><summary>Abstract</summary>

  Pose-driven full-body avatars built on neural rendering produce high-quality novel views of a captured subject. Yet loose clothing and other dynamic elements deform in ways pose alone cannot explain: the same pose can correspond to many different states, because their motion depends on history, inertia, and contact. Explicit simulation and layered-garment methods can model such dynamics, but they require either a dedicated garment template, which raw multi-view capture does not naturally provide, or a test-time physics simulator with non-trivial runtime cost. A parallel line of work learns data-driven clothing avatars that avoid explicit garment layers. These methods add an auxiliary latent for variation beyond pose; at inference, they fix it, regress it from pose, or retrieve it from training data, without explicitly modeling how the latent evolves with its own dynamics. Additionally, even in everyday motion with loose clothing, existing architectures often struggle to capture fine-grained detail, producing blurry renderings and temporal artifacts. We augment a pose-conditioned 3D Gaussian avatar with a transformer-based decoder and a dynamics residual latent that captures temporal appearance and geometry variation beyond the driving signals. At inference, a learned latent dynamics model evolves the residual latent from a short pose history and the previous latent state. The model decomposes each update into driving, restoring, and dissipative forces, producing temporally coherent, history-dependent rollouts with negligible added cost. Different initial conditions yield diverse yet plausible motion trajectories, and the force decomposition exposes controls such as stiffness. Across nine captured sequences of everyday motion with diverse loose garments, quantitative metrics and a perceptual user study show improved animation quality over recent data-driven baselines.

  </details>


- **[Towards Physically Consistent 4D Scene Reconstruction for Closed-loop Autonomous Driving Simulation](https://arxiv.org/abs/2605.21032)**  
  *Bowyn Tan, Yutong Xie, Bai Huang, Fan Luo, Xiao Li, Naizheng Wang, Yang Guan, Shengbo Eben Li*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.21032) · [pdf](https://arxiv.org/pdf/2605.21032.pdf)
  > 💡 现有4DGS方法因空间-时间参数耦合导致低秩歧义，提出正交投影梯度与时序正则化实现物理一致重建。

  <details><summary>Abstract</summary>

  High-fidelity street scene reconstruction is pivotal for end-to-end autonomous driving simulation, where novel-view synthesis (NVS) and time-varying information modeling are two fundamental capabilities to facilitate closed-loop training. However, existing 3DGS methods and their 4D extensions fail to simultaneously achieve both. To bridge this gap, we establish an information-geometric diagnostic framework, revealing that this limitation stems from a credit assignment dilemma between spatial and temporal parameters. Specifically, the deterministic coupling between viewpoint and time in single-source observation creates a low-rank structure that induces massive null-space ambiguity between static view-dependent and dynamic time-varying components. Temporal information overshadows spatial cues, causing the estimation variance of spatial parameters to diverge. To address this issue, we propose Orthogonal Projected Gradient (OPG), a hierarchical training method designed to restore spatial identifiability. OPG prioritizes the integrity of spatial representations by securing them in an initial stage, then restricts temporal updates to the spatial null space, enabling proactive credit assignment. While OPG isolates temporal updates algebraically, Temporal Regularization Strategy is proposed to further refine the temporal solution space by imposing a smoothness constraint based on the physical prior of consistent appearance evolution, ensuring that the reconstructed scene remains physically consistent in closed-loop simulation. Extensive experiments demonstrate that our method not only maintains stable NVS capabilities but also demonstrates superior performance in traditional observation-reproducing metrics, which indirectly reflect the capability of modeling temporal dynamics.

  </details>


- **[FlowLong: Inference-time Long Video Generation via Manifold-constrained Tweedie Matching](https://arxiv.org/abs/2605.20910)**  
  *Jangho Park, Geon Yeong Park, Gihyun Kwon, Jong Chul Ye*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20910) · [pdf](https://arxiv.org/pdf/2605.20910.pdf)
  > 💡 用重叠滑动窗口和Tweedie匹配施加流形约束与时间一致性，随机早期采样同步轨迹，实现无

  <details><summary>Abstract</summary>

  Extending the generation horizon of video diffusion models to long sequences remains a long-standing and important challenge. Existing training-free approaches fall into two categories: extensions of bidirectional models, which are tightly coupled to specific architectures and suffer from quality degradation over long horizons, and autoregressive models, which accumulate drift errors due to exposure bias and tend to produce repetitive motion patterns. To address these issues, we propose a novel but simple inference-time approach for long video generation that is architecture-agnostic and requires no additional training. Our method generates long videos via overlapping sliding windows, where predicted clean samples from adjacent windows are blended via \emph{Tweedie matching} to enforce both \textbf{manifold constraint and temporal consistency} across overlap regions. \emph{Stochastic early-phase sampling} then synchronizes per-window trajectories by injecting fresh noise after each Tweedie matching correction in the high-noise phase, before transitioning to deterministic ODE sampling to preserve fine-grained visual fidelity. Applied to various video generation models, our method generates videos several times longer than the native window length while outperforming both training-free and autoregressive baselines in temporal consistency and visual quality, and further extends to audio-video joint generation and text-to-3DGS without any fine-tuning.

  </details>


- **[TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization](https://arxiv.org/abs/2605.20150)**  
  *Chonghao Zhong, Linfeng Shi, Hua Chen, Tiecheng Sun, Hao Zhao, Binhang Yuan, Chaojian Li*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20150) · [pdf](https://arxiv.org/pdf/2605.20150.pdf)
  > 💡 针对大规模3DGS训练内存瓶颈，提出TideGS框架，利用SSD-CPU-GPU层次存储和轨迹自适应差分流，单24GB GPU训练超十亿

  <details><summary>Abstract</summary>

  Training 3D Gaussian Splatting (3DGS) at billion-primitive scale is fundamentally memory-bound: each Gaussian primitive carries a large attribute vector, and the aggregate parameter table quickly exceeds GPU capacity, limiting prior systems to tens of millions of Gaussians on commodity single-GPU hardware. We observe that 3DGS training is inherently sparse and trajectory-conditioned: each iteration activates only the Gaussians visible from the current camera batch, so GPU memory can serve as a working-set cache rather than a persistent parameter store. Building on this insight, we introduce TideGS, an out-of-core training framework that manages parameters across an SSD-CPU-GPU hierarchy via three synergistic techniques: block-virtualized geometry for SSD-aligned spatial locality, a hierarchical asynchronous pipeline to overlap I/O with computation, and trajectory-adaptive differential streaming that transfers only incremental working-set deltas between iterations. Experiments show that TideGS enables training with over one billion Gaussians on a single 24 GB GPU while achieving the best reconstruction quality among evaluated single-GPU baselines on large-scale scenes, scaling beyond prior out-of-core baselines (e.g., approximately 100M Gaussians) and standard in-memory training (e.g., approximately 11M Gaussians).

  </details>


- **[PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis](https://arxiv.org/abs/2605.17916)**  
  *Jinrang Jia, Zhenjia Li, Yijiang Hu, Yifeng Shi*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.17916) · [pdf](https://arxiv.org/pdf/2605.17916.pdf)
  > 💡 将全屋全景合成建模为自回归节点生成，用3D外壳引导几何

  <details><summary>Abstract</summary>

  Generating a consistent whole-house VR tour from a floorplan and style reference requires both photorealistic panoramas and cross-view spatial coherence. Pure 2D generators produce appealing single panoramas but re-imagine geometry and materials when the viewpoint changes, whereas monolithic 3D generation becomes expensive and loses fine texture at multi-room scale. We introduce PanoWorld, a generative spatial world model that treats whole-house synthesis as autoregressive generation of node-based 360-degree panoramas, matching the discrete navigation used by real VR tour products. PanoWorld uses a floorplan-derived 3D shell as a global geometric proxy and a dynamic 3D Gaussian Splatting cache as renderable spatial memory. A feed-forward panoramic LRM designed for metric-scale multi-room 360-degree inputs lifts generated panoramas into local 3DGS updates, while Room-aware Group Attention suppresses cross-room feature interference. A topology-aware progressive caching strategy fuses these local updates without repeatedly reconstructing the full history. By decoupling shell-based geometry guidance from cache-rendered visual memory, PanoWorld preserves high-frequency 2D synthesis quality while improving cross-node layout and material consistency. The project link is https://jjrcn.github.io/PanoWorld-project-home/

  </details>


- **[Xiaomi Auto World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving](https://arxiv.org/abs/2605.18137)**  
  *Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu, Kaixin Xiong, Lei Gong, Zhanqian Wu, Zehan Zhang, Fangzhen Li, Hao Li, Yingying Shen, Jiale He, Haohui Zhu, Shan Zhao, Kai Wang, Zhiwei Zhan, Yuechuan Pu, Kaiyuan Tan, Ruiling Yang, Xianqi Wang, Tianyi Yan, Jiawei Zhou, Lei Zhang, Jingyang Zhao, Xi Zhou, Chitian Sun, Chenming Wu, Jiong Deng, Hongwei Xie, Ming Lu, Kun Ma, Long Chen, Guang Chen, Hangjun Ye, Bing Wang, Haiyang Sun*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18137) · [pdf](https://arxiv.org/pdf/2605.18137.pdf)
  > 💡 提出联合重建与生成的世界模型JWM，用稀疏查询和两阶段训练实现高保真场景表示与高效在线视频生成。

  <details><summary>Abstract</summary>

  This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.

  </details>


- **[CATRF: Codec-Adaptive TriPlane Radiance Fields for Volumetric Content Delivery](https://arxiv.org/abs/2605.18054)**  
  *Tung-I Chen, Lingdong Wang, Subhransu Maji, Ramesh K. Sitaraman*  
  `2026-05-18` · `eess.IV` · [abs](https://arxiv.org/abs/2605.18054) · [pdf](https://arxiv.org/pdf/2605.18054.pdf)
  > 💡 提出CATRF，用标准编解码器回路训练辐射场，自适应压缩失真，实现更低码率下更优率失真性能。

  <details><summary>Abstract</summary>

  Volumetric media promises next-generation content delivery applications, but its bandwidth demand remains a key bottleneck. Implicit and hybrid volumetric representations reduce model sizes, yet still require careful coding to reach 2D video-like bitrates. We present CATRF, a standard-codec-in-the-loop compression framework for plane-factorized radiance fields. During training, we quantize and pack 2D feature planes into codec-friendly canvases, run a standard codec roundtrip (JPEG/VP9/HEVC/AV1), then unpack and dequantize the decoded features before volume rendering. We use a straight-through estimator (STE) to insert the non-differentiable, standard codec pipeline into the training loop, allowing radiance-field features to adapt directly to the real, client-side codec distortions without introducing any learned codec parameters. On both static and dynamic benchmarks, CATRF consistently achieves a better rate-distortion trade-off over codec-agnostic and learned-codec-in-the-loop baselines, and also outperforms recent compressed 3DGS methods in both compression efficiency and decoding speed. These results highlight a practical path toward low-bitrate, compression-resilient volumetric representations for free-viewpoint video streaming.

  </details>


- **[GEM: Gaussian Evolution Model for Occupancy Forecasting and Motion Planning](https://arxiv.org/abs/2605.17682)**  
  *Cheng Chen, Hao Huang, Saurabh Bagchi*  
  `2026-05-17` · `cs.CV` · [abs](https://arxiv.org/abs/2605.17682) · [pdf](https://arxiv.org/pdf/2605.17682.pdf)
  > 💡 针对离散自回归占用预测的时序限制与误差累积，提出基于4D高斯原语的非自回归语义占用查询与运动规划模型，实现SOTA性能。

  <details><summary>Abstract</summary>

  Future 3D semantic occupancy forecasting and motion planning are central to autonomous driving, as they require models to reason about how surrounding scenes evolve and how the ego vehicle should act. Existing occupancy world models commonly discretize scenes into latent embeddings, volumetric features, or quantized tokens, and forecast future states through fixed-step autoregressive generation. This limits temporal flexibility, obscures scene evolution, accumulates errors over long horizons, and poorly matches the continuous-time dynamics of real driving scenes. We propose GEM, a Gaussian Evolution Model for non-autoregressive occupancy world modeling, where driving scenes are represented as explicit continuous 4D Gaussian primitives with learned dynamics. Instead of rolling out future occupancy states step by step, GEM directly queries the Gaussian world representation at arbitrary timestamps and splats the corresponding conditional 3D Gaussians into semantic occupancy volumes. This enables efficient forecasting over the full horizon while retaining a compact and interpretable scene representation. By decoupling spatial geometry, temporal support, and primitive motion, GEM makes the predicted world easier to inspect, as each primitive's evolution can be followed continuously over time. The same representation also supports motion planning by predicting future ego trajectories from the learned Gaussian world. Extensive experiments show that GEM achieves state-of-the-art future semantic occupancy forecasting and strong motion planning performance, while providing flexible temporal querying.

  </details>


- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925)**  
  *Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi*  
  `2026-05-16` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16925) · [pdf](https://arxiv.org/pdf/2605.16925.pdf)
  > 💡 针对跨视角光度不一致，P2

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently emerged as a powerful explicit representation enabling fast, high-fidelity rendering, making it a promising foundation for closed-loop simulators and perception models in autonomous driving. However, conventional 3DGS implicitly assumes consistent exposure and tone mapping across views. Real driving data violates this assumption due to heterogeneous camera pipelines and dynamic outdoor illumination, baking exposure discrepancies and sensor noise into the radiance field and producing artifacts and inconsistent illumination especially in static backgrounds crucial for realistic simulation. These issues are amplified in autonomous driving, where sparse viewpoints, varying exposures, and outdoor lighting interact, while prior work mainly targets dynamic-object reconstruction and overlooks cross-view photometric consistency. To address this limitation, we introduce P2GS, a physically consistent Gaussian Splatting framework that jointly decomposes a view-invariant linear HDR radiance field, per-view exposure scales, and tone-mapping functions from only LDR images without HDR supervision. P2GS employs a unified optimization strategy grounded in the physical image-formation process, enforcing relative-exposure consistency and HDR-domain radiance regularization. This yields a radiance field robust to inter-camera illumination differences while preserving the real-time efficiency of standard 3DGS. Experiments across real and simulated driving environments show that P2GS matches or surpasses prior methods in LDR reconstruction while providing substantially improved photometric consistency, reliable exposure normalization, and physically coherent illumination across diverse scenes.

  </details>


- **[EndoGSim: Physics-Aware 4D Dynamic Endoscopic Scene Simulations via MLLM-Guided Gaussian Splatting](https://arxiv.org/abs/2605.16022)**  
  *Changjing Liu, Yiming Huang, Long Bai, Beilei Cui, Hongliang Ren*  
  `2026-05-15` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16022) · [pdf](https://arxiv.org/pdf/2605.16022.pdf)
  > 💡 通过MLLM引导4D高斯泼溅与可微分MPM，实现内窥镜场景的物理感知重建与高保真动态模拟。

  <details><summary>Abstract</summary>

  In robot-assisted minimally invasive surgery, high-fidelity dynamic endoscopic scene reconstruction and simulation are crucial to enhancing downstream tasks and advancing surgical outcomes. However, existing methods primarily focus on visual reconstruction, lacking physics-based descriptions of the scene required for realistic simulation. We propose a unified framework that achieves physics-aware reconstruction and physical simulation of endoscopic scenes through Multi-modal Large Language Models (MLLMs)-guided Gaussian Splatting. Our approach utilizes 4D Gaussian Splatting (4DGS) integrated with pre-trained segmentation and depth estimation to represent deformable tissues and tools. To achieve automatic inference of physical properties, we introduce an object-wise material field that initializes material parameters via MLLM and refines them through a differentiable Material Point Method (MPM) under joint supervision from rendered images and optical flow. Validated on both open-source and in-house datasets, our framework achieves superior simulation fidelity and physical accuracy compared to state-of-the-art methods, underscoring its potential to advance robot-assisted surgical applications.

  </details>


- **[Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes](https://arxiv.org/abs/2605.13591)**  
  *Kaicong Huang, Talha Azfar, Weisong Shi, Ruimin Ke*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13591) · [pdf](https://arxiv.org/pdf/2605.13591.pdf)
  > 💡 结合4DGS与可微MPM，实现物理感知、可编辑的动态驾驶场景合成，支持碰撞等极端情况。

  <details><summary>Abstract</summary>

  Reliable autonomous driving relies on large-scale, well-labeled data and robust models. However, manual data collection is resource-intensive, and traditional simulation suffers from a persistent reality gap. While recent generative frameworks and radiance-field methods improve visual fidelity, they still struggle with temporal and spatial consistency and cannot ensure physics-aware behavior, limiting their applicability to driving scenario generation. To address these challenges, we propose Real2Sim, an unified framework that combines 4D Gaussian Splatting (4DGS) with a differentiable Material Point Method (MPM) solver. Real2Sim explicitly reconstructs dynamic driving scenes as temporally continuous Gaussian primitives, supports instance-level editing, and simulates realistic object-object and object-environment interactions. This framework enables physics-aware, high-fidelity synthesis of diverse, editable scenarios, including challenging corner cases such as collisions and post-impact trajectories. Experiments on the Waymo Open Dataset validate Real2Sim's capabilities in rendering, reconstruction, editing, and physics simulation, demonstrating its potential as a scalable tool for data generation in downstream tasks such as perception, tracking, trajectory prediction, and end-to-end policy learning.

  </details>


- **[PointForward: Feedforward Driving Reconstruction through Point-Aligned Representations](https://arxiv.org/abs/2605.11594)**  
  *Cheng Chi, Xianqi Wang, Hongcheng Luo, Mingfei Tu, Gangwei Xu, Zehan Zhang, Bing Wang, Guang Chen, Hangjun Ye, Sida Peng, Xin Yang, Haiyang Sun*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11594) · [pdf](https://arxiv.org/pdf/2605.11594.pdf)
  > 💡 针对前馈驾驶重建的多视图不一致和动态建模问题，提出点对齐表示与场景图，实现显式跨视图一致与实例级运动传播，性能领先。

  <details><summary>Abstract</summary>

  High-fidelity reconstruction of driving scenes is crucial for autonomous driving. While recent feedforward 3D Gaussian Splatting (3DGS) methods enable fast reconstruction, their per-pixel Gaussian prediction paradigm often suffers from multi-view inconsistency and layering artifacts. Moreover, existing methods often model dynamic instances via dense flow prediction, which lacks explicit cross-view correspondence and instance-level consistency. In this paper, we propose PointForward, a feedforward driving reconstruction framework through point-aligned representations. Unlike pixel-aligned methods, we initialize sparse 3D queries in world space and aggregate multi-view image information via spatial-temporal fusion onto these queries, enforcing explicit cross-view consistency in a single feedforward pass. To handle scene dynamics, we introduce scene graphs that explicitly organize moving instances during reconstruction. By leveraging 3D bounding boxes, our method enables instance-level motion propagation and temporally consistent dynamic representations. Extensive experiments demonstrate that PointForward achieves state-of-the-art performance on large-scale driving benchmarks. The code will be available upon the publication of the paper.

  </details>


- **[3DGS$^3$: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering](https://arxiv.org/abs/2605.11489)**  
  *Yibo Zhao, Fan Gao, Youcheng Cai, Ligang Liu*  
  `2026-05-12` · `cs.GR` · [abs](https://arxiv.org/abs/2605.11489) · [pdf](https://arxiv.org/pdf/2605.11489.pdf)
  > 💡 针对3D

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables high-quality real-time 3D rendering but faces challenges in efficiently scaling to ultra-dense scenes and high-resolution due to computational bottlenecks that limit its use in latency-sensitive applications. Instead of optimizing the splatting pipeline itself, we propose \textbf{3DGS$^3$}, a unified post-rendering framework that jointly performs super sampling and frame interpolation through differentiable processing of low-resolution outputs to achieve both high-resolution and high-frame-rate rendering. Our \textbf{Gradient\- \-Aware Super Sampling (GASS)} module leverages the continuous differentiability of 3DGS to extract image gradients that guide a GRU-based refinement network to enable high-fidelity super sampling. Furthermore, a \textbf{Lightweight Temporal Frame Interpolation (LTFI)} module based on a compact U-Net-like backbone fuses temporal and differentiable spatial cues from consecutive frames to synthesize temporally coherent intermediate frames. Experiments on public datasets demonstrate that 3DGS$^3$ achieves superior rendering efficiency and visual quality when compared with state-of-the-art methods and remains compatible with existing 3DGS acceleration techniques. The code will be publicly released upon acceptance.

  </details>


- **[DySurface: Consistent 4D Surface Reconstruction via Bridging Explicit Gaussians and Implicit Functions](https://arxiv.org/abs/2605.10360)**  
  *Minje Kim, Younghyun Noh, Jaesoon Kim, Tae-Kyun Kim*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10360) · [pdf](https://arxiv.org/pdf/2605.10360.pdf)
  > 💡 针对动态

  <details><summary>Abstract</summary>

  While novel view synthesis (NVS) for dynamic scenes has seen significant progress, reconstructing temporally consistent geometric surfaces remains a challenge. Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) offer powerful dynamic scene rendering capabilities; however, relying solely on photometric optimization often leads to geometric ambiguities. This results in discontinuous surfaces, severe artifacts, and broken surfaces over time. To address these limitations, we present DySurface, a novel framework that bridges the effectiveness of explicit Gaussians with the geometric fidelity of implicit Signed Distance Functions (SDFs) in dynamic scenes. Our approach tackles the structural discrepancy between the forward deformation of 3DGS ($canonical \rightarrow dynamic$) and the backward deformation required for volumetric SDF rendering ($dynamic \rightarrow canonical$). Specifically, we propose the VoxGS-DSDF branch that leverages deformed Gaussians to construct a dynamic sparse voxel grid, providing explicit geometric guidance to the implicit SDF field. This explicit anchoring effectively regularizes the volumetric rendering process, significantly improving surface reconstruction quality, with watertight boundaries and detailed representations. Quantitative and qualitative experiments demonstrate that DySurface significantly outperforms state-of-the-art baselines in geometric accuracy metrics while maintaining competitive rendering performance.

  </details>


- **[PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.10307)**  
  *Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10307) · [pdf](https://arxiv.org/pdf/2605.10307.pdf)
  > 💡 动态场景复杂运动重建中，提出PaMoSplat，结合部位感知与运动先验，实现高保真渲染、精准跟踪和快速收敛。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.

  </details>


- **[LagrangianSplats: Divergence-Free Transport of Gaussian Primitives for Fluid Reconstruction](https://arxiv.org/abs/2605.09299)**  
  *Ningxiao Tao, Baoquan Chen, Mengyu Chu*  
  `2026-05-10` · `cs.GR` · [abs](https://arxiv.org/abs/2605.09299) · [pdf](https://arxiv.org/pdf/2605.09299.pdf)
  > 💡 从稀疏2D视频重建流体使用散度自由核驱动3D高斯泼溅，保证不可压缩性和长程传输，滑动窗口优化提升精度。

  <details><summary>Abstract</summary>

  Reconstructing 3D fluid velocity fields from sparse 2D video observations is a highly ill-posed inverse problem, demanding both transport consistency with observed motion and physical validity under fluid laws. Existing methods typically impose these constraints through soft penalties, often leading to compromised accuracy and convergence issues. We introduce a reconstruction framework that structurally enforces both constraints. Specifically, we parameterize the reconstructed velocity using a continuous Divergence-Free Kernel representation, driving the advection of a Lagrangian 3D Gaussian Splatting representation. This formulation intrinsically guarantees both flow incompressibility and long-range transport coherence by construction. To enable the efficient optimization of such a constrained system, we introduce a novel Sliding Window scheme that propagates gradients over meaningful temporal horizons while maintaining tractable training costs. Experiments on synthetic and real-world datasets demonstrate that our method outperforms state-of-the-art baselines in both transport consistency and physical accuracy, enabling applications such as high-quality re-simulation and flow analysis.

  </details>


- **[CAGS: Color-Adaptive Volumetric Video Streaming with Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2605.09279)**  
  *Daheng Yin, Yili Jin, Jianxin Shi, Isaac Ding, Miao Zhang, Fangxin Wang, Zhaowu Huang, Cong Zhang, Jiangchuan Liu, Fang Dong*  
  `2026-05-10` · `cs.GR` · [abs](https://arxiv.org/abs/2605.09279) · [pdf](https://arxiv.org/pdf/2605.09279.pdf)
  > 💡 针对3DGS流中带宽与质量矛盾，提出矢量量化LoD及低分辨率参考图颜色校正方案，PSNR提升5~20dB。

  <details><summary>Abstract</summary>

  Volumetric video (VV) streaming enables real-time, immersive access to remote 3D environments, powering telepresence, ecological monitoring, and robotic teleoperation. These applications turn VV streaming into a real-time interface to remote physical environments, imposing new system-level demands for photorealistic scene representation, low-latency interaction, and robust performance under heterogeneous networks. 3D Gaussian Splatting (3DGS) has been widely used for real-time photorealistic rendering, offering superior visual quality and rendering performance, but it faces challenges due to bandwidth consumption. Furthermore, as the foundation of adaptive VV streaming, existing Levels of Detail (LoD) methods based on density are not well-suited to Gaussian representations, leading to visible gaps and severe quality degradation. Recent studies have also explored attribute compression techniques to reduce bandwidth consumption. Our preliminary studies reveal that aggressive attribute compression primarily causes color distortion, which can be effectively corrected in the rendered image using a reference image. Motivated by these findings, we propose a novel Color-Adaptive scheme for adaptive VV streaming that uses vector quantization (VQ) to establish LoDs and correct color distortions with low-resolution reference images. We further present CAGS, an adaptive VV streaming system compatible with diverse Gaussian representations, which integrates the Color-Adaptive scheme by rendering reference images on the streaming server and performing color restoration on the client. Extensive experiments on our prototype system demonstrate that CAGS outperforms the existing adaptive streaming systems in PSNR by 5$\sim$20 dB under fluctuating bandwidth, operates significantly faster than existing scalable Gaussian compression methods, and generalizes across different Gaussian representations.

  </details>


- **[Thin-Client Interactive Gaussian Adaptive Streaming over HTTP/3](https://arxiv.org/abs/2605.08699)**  
  *Emanuele Artioli, Philipp Fößl, Daniele Lorenzi, Farzad Tashtarian, Mahdi Dolati, Cheng-Hsin Hsu, Christian Timmerer*  
  `2026-05-09` · `eess.IV` · [abs](https://arxiv.org/abs/2605.08699) · [pdf](https://arxiv.org/pdf/2605.08699.pdf)
  > 💡 针对3DGS移动端计算与带宽瓶颈，提出TIGAS远程渲染框架，通过QUIC和ABR算法实现低延迟高质量流式传输。

  <details><summary>Abstract</summary>

  Recent advancements in 3D Gaussian Splatting (3DGS) have enabled photorealistic rendering of complex scenes, yet widespread adoption on mobile and Extended Reality (XR) devices is hindered by substantial computational and bandwidth requirements. While existing solutions often focus on model compression for client-side rendering, they still demand significant GPU power, limiting applicability on resource-constrained hardware. We propose TIGAS (Thin-client Interactive Gaussian Adaptive Streaming), a remote rendering framework offloading rasterization to a backend. To bypass the prohibitive latencies connected to fluctuating network conditions, TIGAS streams view-dependent 2D projections to a lightweight web client over QUIC, minimizing head-of-line (HoL) blocking. A dedicated ABR algorithm adapts rendering quality to fluctuating network conditions, maintaining motion-to-photon latency within strict 6DoF interactive constraints. Furthermore, we discuss the integration of an experimental WebGPU super-resolution pipeline to analyze the trade-offs between perceptual quality enhancements and thin-client processing bottlenecks. We extensively evaluate TIGAS across multi-continental environments using 14 3DGS models and real 6DoF EyeNavGS movement traces. Powered by a backend rendering frames in under 10 milliseconds, TIGAS maintains latency within interactive thresholds while achieving an average SSIM of 0.88, serving both as a robust testbed for 3DGS streaming research and a capable delivery system. The source code is available at: https://github.com/Rekenar/GaussianAdaptiveStreamer.

  </details>


- **[AsyncEvGS: Asynchronous Event-Assisted Gaussian Splatting for Handheld Motion-Blurred Scenes](https://arxiv.org/abs/2605.07192)**  
  *Jun Dai, Renbiao Jin, Bo Xu, Yutian Chen, Linning Xu, Mulin Yu, Tianfan Xue, Shi Guo*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07192) · [pdf](https://arxiv.org/pdf/2605.07192.pdf)
  > 💡 使用异步事件相机辅助3DGS，通过事件重建锐图和跨域位姿估计，解决手持运动

  <details><summary>Abstract</summary>

  3D reconstruction methods such as 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) achieve impressive photorealism but fail when input images suffer from severe motion blur. While event cameras provide high-temporal-resolution motion cues, existing event-assisted approaches rely on low-resolution sensors and strict synchronization, limiting their practicality for handheld 3D capture on common devices, such as smartphones. We introduce a flexible, high-resolution asynchronous RGB-Event dual-camera system and a corresponding reconstruction framework. Our approach first reconstructs sharp images from the event data and then employs a cross-domain pose estimation module based on the Visual Geometry Transformer (VGGT) to obtain robust initialization for 3DGS. During optimization, we employ a structure-driven event loss and view-specific consistency regularizers to mitigate the ill-posed behavior of traditional event losses and deblurring losses, ensuring both stable and high-fidelity reconstruction. We further contribute AsyncEv-Deblur, a new high-resolution RGB-Event dataset captured with our asynchronous system. Experiments demonstrate that our method achieves state-of-the-art performance on both our challenging dataset and existing benchmarks, substantially improving reconstruction robustness under severe motion blur. Project page: https://openimaginglab.github.io/AsyncEvGS/

  </details>


- **[ST-Gen4D: Embedding 4D Spatiotemporal Cognition into World Model for 4D Generation](https://arxiv.org/abs/2605.07390)**  
  *Haonan Wang, Hanyu Zhou, Tao Gu, Luxin Yan*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07390) · [pdf](https://arxiv.org/pdf/2605.07390.pdf)
  > 💡 现有4D生成模型忽视局部动态，ST-Gen4D通过构建4D认知图结合世界模型与扩散生成，实现结构合理且拓扑一致的4D高斯。

  <details><summary>Abstract</summary>

  Generative models have achieved success in producing apparently coherent 2D videos, but remain challenging in the physical world due to lack of 4D spatiotemporal scale. Typically, existing 4D generative models directly embed macro scale constraints to enhance overall spatiotemporal consistency. However, these methods only ensure global appearance coherence and fail to reveal the local dynamics of the physical world. Our insight is that global appearance structure and local dynamic topology empower 4D spatiotemporal cognition, thereby enabling 4D generation with spatiotemporal regularities. In this work, we propose ST-Gen4D, a 4D generation framework with 4D spatiotemporal cognition-based world model. Our model is guided by four key designs: 1) Spatiotemporal representation. We encode various modalities into multiple representations as a feature basis. 2) Spatiotemporal cognition. We sculpture these representations into global appearance graph and local dynamic graph, and fuse them via semantic-bridged spatiotemporal fusion to obtain a 4D cognition graph. 3) Spatiotemporal reasoning. We utilize a world model to derive future state based on the 4D cognition. 4) Spatiotemporal generation. We leverage the derived cognition as condition to guide latent diffusion for 4D Gaussian generation. By deeply integrating 4D intrinsic cognition with generative priors, our model guarantees the structural rationality and topological consistency of 4D generation. Moreover, we propose ST-4D datasets by aggregating public 4D datasets and self-built subset. Extensive experiments demonstrate the superiority of our ST-Gen4D across 3D and 4D generation tasks.

  </details>


- **[Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435)**  
  *Shuo Wang, Jilin Mei, Fuyang Liu, Wenfei Guan, Fanjie Kong, Zhihua Zhao, Shuai Wang, Chen Min, Yu Hu*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04435) · [pdf](https://arxiv.org/pdf/2605.04435.pdf)
  > 💡 针对越野场景4D重建中时序冲突问题，提出体素接地时序高斯聚合和表面法线正则化，提升质量并泛化到未知域。

  <details><summary>Abstract</summary>

  Feedforward Gaussian Splatting has recently emerged as an efficient paradigm for 4D reconstruction in autonomous driving. However, in unstructured off-road scenes, its performance degrades due to high-frequency geometry, ego-motion jitter, and increased non-rigid dynamics. These factors introduce conflicting Gaussian observations across timestamps, leading to either over-smoothed renderings or structural artifacts. To address this issue, we propose Ground4D, a spatially-grounded 4D feedforward framework for pose-free off-road reconstruction. The key idea is to resolve temporal conflicts through spatially localized conditioning. Specifically, we introduce voxel-grounded temporal Gaussian aggregation, which partitions the canonical Gaussian space into spatial voxels and performs query-conditioned temporal attention within each voxel. Intra-voxel softmax normalization ensures that temporal selectivity and spatial occupancy become mutually reinforcing rather than conflicting. We furthermore introduce surface normal cues as auxiliary geometric guidance to regularize the geometry of Gaussian primitives. Extensive experiments on ORAD-3D and RELLIS-3D demonstrate that Ground4D consistently outperforms existing feedforward methods in reconstruction quality and generalizes zero-shot to unseen off-road domains. Project page and code:https://github.com/wsnbws/Ground4D.

  </details>


- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527)**  
  *Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04527) · [pdf](https://arxiv.org/pdf/2605.04527.pdf)
  > 💡 用编码器将动态点云压缩为形状token，经表面与高斯解码器学习4D几何外观，在生成跟踪等任务性能优异。

  <details><summary>Abstract</summary>

  We introduce a framework for learning latent representations of 4D objects which are descriptive, faithfully capturing object geometry and appearance; compressive, aiding in downstream efficiency; and accessible, requiring minimal input, i.e., an unstructured dynamic point cloud, to construct. Specifically, Velox trains an encoder to compress spatiotemporal color point clouds into a set of dynamic shape tokens. These tokens are supervised using two complementary decoders: a 4D surface decoder, which models the time-varying surface distribution capturing the geometry; and a Gaussian decoder, which maps the tokens to 3D Gaussians, helping learn appearance. To demonstrate the utility of our representation, we evaluate it across three downstream tasks -- video-to-4D generation, 3D tracking, and cloth simulation via image-to-4D generation -- and observe strong performances in all settings.

  </details>


- **[FreeTimeGS++: Secrets of Dynamic Gaussian Splatting and Their Principles](https://arxiv.org/abs/2605.03337)**  
  *Lucas Yunkyu Lee, Soonho Kim, Youngwook Kim, Sangmin Kim, Jaesik Park*  
  `2026-05-05` · `cs.CV` · [abs](https://arxiv.org/abs/2605.03337) · [pdf](https://arxiv.org/pdf/2605.03337.pdf)
  > 💡 分析4DGS隐藏驱动因素，发现时间分区与光度-时空差异，提出门控边缘化和神经速度场实现稳定动态重建。

  <details><summary>Abstract</summary>

  The recent surge in 4D Gaussian Splatting (4DGS) has achieved impressive dynamic scene reconstruction. While these methods demonstrate remarkable performance, the specific drivers behind such gains remain less explored, making a systematic understanding of the underlying principles challenging. In this paper, we perform a comprehensive analysis of these hidden factors to provide a clearer perspective on the 4DGS framework. We first establish a controlled baseline, FreeTimeGS_ours, by formalizing and reproducing the heuristics of the state-of-the-art FreeTimeGS. Using this framework, we dissect 4DGS along its fundamental axes and uncover key secrets, including the emergent temporal partitioning driven by Gaussian durations and the discrepancy between photometric fidelity and spatiotemporal consistency. Based on these insights, we propose FreeTimeGS++, a principled method that employs gated marginalization and neural velocity fields to achieve superior stability and robust dynamic representations. Our approach yields reproducible results with reduced run-to-run variance. We will release our implementation to provide a reliable foundation for future 4DGS research.

  </details>


- **[From Concept to Capability: Evaluating 3D Gaussian Splatting for Synthetic Scene Editing in Autonomous Driving](https://arxiv.org/abs/2605.01995)**  
  *Ali Nouri, Yifei Zhang, Yifan Zhang, Tayssir Bouraffa, Zhennan Fei, Zijian Han, Håkan Sivencrona, Anders Heyden*  
  `2026-05-03` · `cs.CV` · [abs](https://arxiv.org/abs/2605.01995) · [pdf](https://arxiv.org/pdf/2605.01995.pdf)
  > 💡 评估3DGS在自动驾驶安全场景重建中的保真度，提出系统分析框架，揭示多视角下车辆与行人的质量退化。

  <details><summary>Abstract</summary>

  The perception of an Autonomous Driving System (ADS) critically depends on relevant, comprehensive, and diverse datasets to ensure its safety while operating in the environment. Field data collection lacks completeness with respect to the list of rare but still possible safety-related scenarios needed for the development, verification, and validation of the ADS. 3D Gaussian Splatting (3DGS) has shown promising capabilities for the reconstruction and editing of scenes based on data collected by cameras and LiDAR sensors. However, the industrial fidelity evaluation of reconstructions is underexplored, which is crucial when employing such methods in safety-related systems, especially for ADS. This becomes more challenging as ADS operates in a dynamic, uncontrolled environment with limited viewpoints and often partially occluded objects. This paper addresses this gap by proposing and implementing a framework (Fig. 1) to systematically analyze the capabilities and limitations of 3DGS for use in the reconstruction of safety-related scenes. It focuses on the quality of reconstruction for vehicles and pedestrians, which are the two most critical object classes for ADS. Our findings provide industry insights into the fidelity degradation of reconstructions from multiple novel viewpoints, both lateral and longitudinal, enabling the integration of these methods into real-world industrial AD software development and testing pipelines.

  </details>


- **[A Principled Approach for Creating High-fidelity Synthetic Demonstrations for Imitation Learning](https://arxiv.org/abs/2605.01232)**  
  *Moniruzzaman Akash, Momotaz Begum*  
  `2026-05-02` · `cs.RO` · [abs](https://arxiv.org/abs/2605.01232) · [pdf](https://arxiv.org/pdf/2605.01232.pdf)
  > 💡 针对3DGS生成演示偏离专家轨迹的问题，提出以动态运动基元保留运动结构，并引入解析避障DMP直接操作密度场，实现高保真多样化合成。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled visually realistic demonstration generation from a single expert trajectory and a short multi-view scan. However, existing 3DGS-based synthesis pipelines typically generate new motions using sampling-based planners or trajectory optimization, which often deviate substantially from the expert's demonstrated path. While such deviations may be acceptable for tasks insensitive to motion shape, they discard subtle spatial and temporal structure that is critical for contact-rich and shape-sensitive manipulation, causing increased demonstration diversity to harm downstream policy learning. We argue that demonstration synthesis should treat the expert trajectory as a strong prior. Building on this principle, we propose a framework that synthesizes diverse task demonstrations while explicitly preserving expert motion structure. We model the expert trajectory using Dynamic Movement Primitives (DMPs) and retarget it to new goals, object configurations, and viewpoints within a reconstructed 3DGS scene, yielding phase-consistent, shape-preserving motion by construction. To safely realize this expert-preserving diversity in cluttered scenes, we introduce an analytic obstacle-aware DMP formulation that operates directly on the continuous density field induced by the 3DGS representation. This enables collision avoidance while minimally perturbing the nominal expert motion, unifying photorealistic rendering and geometric reasoning without additional scene representations. We evaluate our approach on a Spot mobile manipulator across three manipulation tasks with increasing sensitivity to trajectory fidelity. Compared to planner- and optimization-based synthesis, our method produces trajectories with lower deviation and collision rates and yields higher task success when training diffusion-based visuomotor policies.

  </details>


- **[Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179)**  
  *Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.28179) · [pdf](https://arxiv.org/pdf/2604.28179.pdf)
  > 💡 利用配对CT呼吸扫描建模变形空间，嵌入网格锚定高斯泼溅实现无屏气动态支气管镜重建，实现高精度定位与快速训练。

  <details><summary>Abstract</summary>

  Bronchoscopic navigation relies on registering endoscopic video to a preoperative CT scan, but respiratory motion deforms the airway by 5-20 mm, creating CT-to-body divergence that limits localization accuracy. In practice, this is mitigated through breath-hold protocols, which attempt to match the intraoperative anatomy to a static CT, but are difficult to reproduce and disrupt clinical workflow. We propose to eliminate the need for breath-hold protocols by leveraging patient-specific respiratory modeling. Paired inhale-exhale CT scans, already acquired for planning, implicitly define the patient-specific deformation space of the breathing airway. By registering these scans, we reduce respiratory motion to a single scalar breathing phase per frame, constraining all reconstructions to anatomically observed configurations. We embed this representation within a mesh-anchored Gaussian splatting framework, where a lightweight estimator infers breathing phase directly from endoscopic RGB, enabling continuous, deformation-aware reconstruction throughout the respiratory cycle without breath-holds or external sensing. To enable quantitative evaluation, we introduce RESPIRE, a physically grounded bronchoscopy simulation pipeline with per-frame ground truth for geometry, pose, breathing phase, and deformation. Experiments on RESPIRE show that our approach achieves geometrically faithful reconstruction, over 20x faster training, and 1.22 mm target localization accuracy (within the 3mm clinically relevant tolerances) outperforming unconstrained single-CT baselines. Please check out our website for additional visuals: https://asdunnbe.github.io/RESPIRE/

  </details>


- **[Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction](https://arxiv.org/abs/2604.26920)**  
  *David Novikov, Eilon Vaknin, Narek Tumanyan, Mark Sheinin*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26920) · [pdf](https://arxiv.org/pdf/2604.26920.pdf)
  > 💡 利用颜色编码照明将高速时序信息编码至低速相机图像，结合动态高斯泼溅解码重建高速体积场景。

  <details><summary>Abstract</summary>

  The task of capturing and rendering 3D dynamic scenes from 2D images has become increasingly popular in recent years. However, most conventional cameras are bandwidth-limited to 30-60 FPS, restricting these methods to static or slowly evolving scenes. While overcoming bandwidth limitations is difficult for general scenes, recent years have seen a flurry of computational imaging methods that yield high-speed videos using conventional cameras for specific applications (e.g., motion capture and particle image velocimetry). However, most of these methods require modifications to a camera's optics or the addition of mechanically moving components, limiting them to a single-view high-speed capture. Consequently, these methods cannot be readily used to capture a 3D representation of rapid scene motion. In this paper, we propose a novel method to capture and reconstruct a volumetric representation of a high-speed scene using only unaugmented low-speed cameras. Instead of modifying the hardware or optics of each individual camera, we encode high-speed scene dynamics by illuminating the scene with a rapid, sequential color-coded sequence. This results in simultaneous multi-view capture of the scene, where high-speed temporal information is encoded in the spatial intensity and color variations of the captured images. To construct a high-speed volumetric representation of the dynamic scene, we develop a novel dynamic Gaussian Splatting-based approach that decodes the temporal information from the images. We evaluate our approach on simulated scenes and real-world experiments using a multi-camera imaging setup, showing first-of-a-kind high-speed volumetric scene reconstructions.

  </details>


- **[Generalizable 3D Gaussian Splatting enabled Semantic Coding for Real-Time Immersive Video Communications](https://arxiv.org/abs/2604.25330)**  
  *Dingxi Yang, Wenqi Guo, Yue Liu, Jungong Han, Zhijin Qin*  
  `2026-04-28` · `eess.IV` · [abs](https://arxiv.org/abs/2604.25330) · [pdf](https://arxiv.org/pdf/2604.25330.pdf)
  > 💡 提出GS-SCNet统一框架，融合可泛化3DGS与语义编码，以视差引导编解码和轻量预测器实现高效实时沉浸式视频通信。

  <details><summary>Abstract</summary>

  Real-time immersive video communications, particularly high-fidelity 3D telepresence, necessitates a synergistic balance between instantaneous dynamic scene reconstruction and high-efficiency data transmission. While recent advancements in feed-forward 3D Gaussian Splatting (3DGS) have enabled real-time rendering, performing multi-view video coding and 3D reconstruction in a decoupled manner leads to suboptimal compression efficiency and high computational complexity. To address this, we propose GS-SCNet, the first unified end-to-end framework that seamlessly integrates generalizable 3DGS reconstruction with a dedicated deep Semantic Coding pipeline. Our architecture is underpinned by two core technical contributions: (i) we introduce a Disparity-Guided Parallel Semantic Codec that exploits epipolar geometric priors to facilitate cross-view contextual interaction via disparity compensation and semantic fusion, thereby enabling real-time parallel processing of stereo streams while significantly enhancing rate-distortion performance, and (ii) we develop a Lightweight Gaussian Parameter Predictor which directly projects decoded semantic latents into 3DGS attributes, obviating the need for intermediate pixel-domain reconstruction. By coupling the codec with the task-specific predictor, our framework extracts geometric correlations only once, effectively eliminating the redundant computational bottleneck inherent in conventional decoupled paradigms. Extensive evaluations on both synthetic and real-world human datasets demonstrate that GS-SCNet achieves a superior trade-off across compression efficiency, rendering quality, and real-time performance. Notably, our framework exhibits strong cross-domain generalization and robustness against compression artifacts when applied to out-of-domain real-world data, significantly outperforming conventional decoupled transmission paradigms.

  </details>


- **[Bringing a Personal Point of View: Evaluating Dynamic 3D Gaussian Splatting for Egocentric Scene Reconstruction](https://arxiv.org/abs/2604.23803)**  
  *Jan Warchocki, Xi Wang, Jonas Kulhanek, Jan van Gemert*  
  `2026-04-26` · `cs.CV` · [abs](https://arxiv.org/abs/2604.23803) · [pdf](https://arxiv.org/pdf/2604.23803.pdf)
  > 💡 评估动态3D

  <details><summary>Abstract</summary>

  Egocentric video provides a unique view into human perception and interaction, with growing relevance for augmented reality, robotics, and assistive technologies. However, rapid camera motion and complex scene dynamics pose major challenges for 3D reconstruction from this perspective. While 3D Gaussian Splatting (3DGS) has become a state-of-the-art method for efficient, high-quality novel view synthesis, variants, that focus on reconstructing dynamic scenes from monocular video are rarely evaluated on egocentric video. It remains unclear whether existing models generalize to this setting or if egocentric-specific solutions are needed. In this work, we evaluate dynamic monocular 3DGS models on egocentric and exocentric video using paired ego-exo recordings from the EgoExo4D dataset. We find that reconstruction quality is consistently lower in egocentric views. Analysis reveals that the difference in reconstruction quality, measured in peak signal-to-noise ratio, stems from the reconstruction of static, not dynamic, content. Our findings underscore current limitations and motivate the development of egocentric-specific approaches, while also highlighting the value of separately evaluating static and dynamic regions of a video.

  </details>


- **[Flow4DGS-SLAM: Optical Flow-Guided 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2604.22339)**  
  *Yunsong Wang, Gim Hee Lee*  
  `2026-04-24` · `cs.CV` · [abs](https://arxiv.org/abs/2604.22339) · [pdf](https://arxiv.org/pdf/2604.22339.pdf)
  > 💡 面向动态场景SLAM，提出光流引导的4DGS，通过运动掩码分离动态静态并显式建模时间中心与GMM，实现追踪、重建

  <details><summary>Abstract</summary>

  Handling the dynamic environments is a significant research challenge in Visual Simultaneous Localization and Mapping (SLAM). Recent research combines 3D Gaussian Splatting (3DGS) with SLAM to achieve both robust camera pose estimation and photorealistic renderings. However, using SLAM to efficiently reconstruct both static and dynamic regions remains challenging. In this work, we propose an efficient framework for dynamic 3DGS SLAM guided by optical flow. Using the input depth and prior optical flow, we first propose a category-agnostic motion mask generation strategy by fitting a camera ego-motion model to decompose the optical flow. This module separates dynamic and static Gaussians and simultaneously provides flow-guided camera pose initialization. We boost the training speed of dynamic 3DGS by explicitly modeling their temporal centers at keyframes. These centers are propagated using 3D scene flow priors and are dynamically initialized with an adaptive insertion strategy. Alongside this, we model the temporal opacity and rotation using a Gaussian Mixture Model (GMM) to adaptively learn the complex dynamics. The empirical results demonstrate our state-of-the-art performance in tracking, dynamic reconstruction, and training efficiency.

  </details>


- **[EvFlow-GS: Event Enhanced Motion Deblurring with Optical Flow for 3D Gaussian Splatting](https://arxiv.org/abs/2604.22183)**  
  *Feiyu An, Yufei Deng, Zihui Zhang, Rong Xiao*  
  `2026-04-24` · `cs.CV` · [abs](https://arxiv.org/abs/2604.22183) · [pdf](https://arxiv.org/pdf/2604.22183.pdf)
  > 💡 利用事件流与光流联合优化可学习双重积分和3DGS，提出新事件损失和残差先验，实现高质量运动去模糊三维重建。

  <details><summary>Abstract</summary>

  Achieving sharp 3D reconstruction from motion-blurred images alone becomes challenging, motivating recent methods to incorporate event cameras, benefiting from microsecond temporal resolution. However, they suffer from residual artifacts and blurry texture details due to misleading supervision from inaccurate event double integral priors and noisy, blurry events. In this study, we propose EvFlow-GS, a unified framework that leverages event streams and optical flow to optimize an end-to-end learnable double integral (LDI), camera poses, and 3D Gaussian Splatting (3DGS) jointly on-the-fly. Specifically, we first extract edge information from the events using optical flow and then formulate a novel event-based loss applied separately to different modules. Additionally, we exploit a novel event-residual prior to strengthen the supervision of intensity changes between images rendered from 3DGS. Finally, we integrate the outputs of both 3DGS and LDI into a joint loss, enabling their optimization to mutually facilitate each other. Experiments demonstrate the leading performance of our EvFlow-GS.

  </details>


- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784)**  
  *Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang*  
  `2026-04-22` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20784) · [pdf](https://arxiv.org/pdf/2604.20784.pdf)
  > 💡 针对动态稀疏视图重建的几何崩溃问题，提出结合3D一致性与扩散整流器的闭环优化框架，实现高保真度和时空一致性。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from sparse multi-view videos is highly ill-posed, often leading to geometric collapse, trajectory drift, and floating artifacts. Recent attempts introduce generative priors to hallucinate missing content, yet naive integration frequently causes structural drift and temporal inconsistency due to the mismatch between stochastic 2D generation and deterministic 3D geometry. In this paper, we propose GeoRect4D, a novel unified framework for sparse-view dynamic reconstruction that couples explicit 3D consistency with generative refinement via a closed-loop optimization process. Specifically, GeoRect4D introduces a degradation-aware feedback mechanism that incorporates a robust anchor-based dynamic 3DGS substrate with a single-step diffusion rectifier to hallucinate high-fidelity details. This rectifier utilizes a structural locking mechanism and spatiotemporal coordinated attention, effectively preserving physical plausibility while restoring missing content. Furthermore, we present a progressive optimization strategy that employs stochastic geometric purification to eliminate floaters and generative distillation to infuse texture details into the explicit representation. Extensive experiments demonstrate that GeoRect4D achieves state-of-the-art performance in reconstruction fidelity, perceptual quality, and spatiotemporal consistency across multiple datasets.

  </details>


- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714)**  
  *Yang Liu, Zhiyong Zhang*  
  `2026-04-20` · `cs.MM` · [abs](https://arxiv.org/abs/2604.21714) · [pdf](https://arxiv.org/pdf/2604.21714.pdf)
  > 💡 针对动态人体重建细节丢失和伪影问题，提出结合SMPL-X区域感知初始化与几何先验的3D高斯方法，实现高质量

  <details><summary>Abstract</summary>

  Real-time, high-fidelity 3D human reconstruction from RGB images is essential for interactive applications such as virtual reality and gaming, yet remains challenging due to the complex non-rigid deformations of dynamic human bodies. Although 3D Gaussian Splatting enables efficient rendering, existing methods struggle to capture fine geometric details and often produce artifacts such as fused fingers and over-smoothed faces. Moreover, conventional spatial-field-based dynamic modeling faces a trade-off between reconstruction fidelity and GPU memory consumption. To address these issues, we propose a novel 3D Gaussian human reconstruction framework that combines region-aware initialization with rich geometric priors. Specifically, we leverage the expressive SMPL-X model to initialize both 3D Gaussians and skinning weights, providing a robust geometric foundation for precise reconstruction. We further introduce a region-aware density initialization strategy and a geometry-aware multi-scale hash encoding module to improve local detail recovery while maintaining computational efficiency.Experiments on PeopleSnapshot and GalaBasketball show that our method achieves superior reconstruction quality and finer detail preservation under complex motions, while maintaining real-time rendering speed.

  </details>


- **[GS-STVSR: Ultra-Efficient Continuous Spatio-Temporal Video Super-Resolution via 2D Gaussian Splatting](https://arxiv.org/abs/2604.18047)**  
  *Mingyu Shi, Xin Di, Long Peng, Boxiang Cao, Anran Wu, Zhanfeng Feng, Jiaming Guo, Renjing Pei, Xueyang Fu, Yang Cao, Zhengjun Zha*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18047) · [pdf](https://arxiv.org/pdf/2604.18047.pdf)
  > 💡 针对连续时空视频超分存在的低效密集查询问题，提出基于2D高斯泼溅的GS-STVSR框架，通过运动建模驱动高斯核演化，实现高质量、近乎恒定时间的超高效推理。

  <details><summary>Abstract</summary>

  Continuous Spatio-Temporal Video Super-Resolution (C-STVSR) aims to simultaneously enhance the spatial resolution and frame rate of videos by arbitrary scale factors, offering greater flexibility than fixed-scale methods that are constrained by predefined upsampling ratios. In recent years, methods based on Implicit Neural Representations (INR) have made significant progress in C-STVSR by learning continuous mappings from spatio-temporal coordinates to pixel values. However, these methods fundamentally rely on dense pixel-wise grid queries, causing computational cost to scale linearly with the number of interpolated frames and severely limiting inference efficiency. We propose GS-STVSR, an ultra-efficient C-STVSR framework based on 2D Gaussian Splatting (2D-GS) that drives the spatiotemporal evolution of Gaussian kernels through continuous motion modeling, bypassing dense grid queries entirely. We exploit the strong temporal stability of covariance parameters for lightweight intermediate fitting, design an optical flow-guided motion module to derive Gaussian position and color at arbitrary time steps, introduce a Covariance resampling alignment module to prevent covariance drift, and propose an adaptive offset window for large-scale motion. Extensive experiments on Vid4, GoPro, and Adobe240 show that GS-STVSR achieves state-of-the-art quality across all benchmarks. Moreover, its inference time remains nearly constant at conventional temporal scales (X2--X8) and delivers over X3 speedup at extreme scales X32, demonstrating strong practical applicability.

  </details>


- **[D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082)**  
  *Xingyuan Yu, Yijin Li, Chong Zeng, Yuhang Ming, Hujun Bao, Guofeng Zhang*  
  `2026-04-18` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17082) · [pdf](https://arxiv.org/pdf/2604.17082.pdf)
  > 💡 针对结构化动态物体，通过可微基元绑定3DGS与变形网络及自适应控制，实现高保真几何与运动联合建模。

  <details><summary>Abstract</summary>

  Capturing both geometry and rigid motion for structured dynamic objects, like multi-part assemblies or jointed mechanisms, remains a key challenge. Existing dynamic methods, such as deformable meshes or 3DGS, rely on unstructured representations and fail to jointly model suitable geometry and articulated motion. Primitive-based methods excel at structured static scenes, but their dynamic potential is still unexplored. We propose D-Prism, the first framework to achieve high-fidelity structured dynamic modeling by extending differentiable primitives to the dynamic domain. Specifically, we bind 3DGS to primitive surfaces, leveraging their respective strengths in appearance and geometry. We introduce a deformation network to control primitive motion, ensuring it accurately matches the object's movement. Furthermore, we design a novel adaptive control strategy to dynamically adjust primitive counts, better matching objects' true spatial footprint. Experiments confirm that our method excels at structured dynamic modeling, providing both structured geometry and precise motion tracking.

  </details>


- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862)**  
  *Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15862) · [pdf](https://arxiv.org/pdf/2604.15862.pdf)
  > 💡 针对3DGS隐写，提出基于SH重要性加密与哈希网格引导不透明度映射的框架，实现高容量、鲁棒且快速的不可感知信息嵌入。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently redefined the paradigm of 3D reconstruction, striking an unprecedented balance between visual fidelity and computational efficiency. As its adoption proliferates, safeguarding the copyright of explicit 3DGS assets has become paramount. However, existing invisible message embedding frameworks struggle to reconcile secure and high-capacity data embedding with intrinsic asset utility, often disrupting the native rendering pipeline or exhibiting vulnerability to structural perturbations. In this work, we present \textbf{\textit{Splats in Splats++}}, a unified and pipeline-agnostic steganography framework that seamlessly embeds high-capacity 3D/4D content directly within the native 3DGS representation. Grounded in a principled analysis of the frequency distribution of Spherical Harmonics (SH), we propose an importance-graded SH coefficient encryption scheme that achieves imperceptible embedding without compromising the original expressive power. To fundamentally resolve the geometric ambiguities that lead to message leakage, we introduce a \textbf{Hash-Grid Guided Opacity Mapping} mechanism. Coupled with a novel \textbf{Gradient-Gated Opacity Consistency Loss}, our formulation enforces a stringent spatial-attribute coupling between the original and hidden scenes, effectively projecting the discrete attribute mapping into a continuous, attack-resilient latent manifold. Extensive experiments demonstrate that our method substantially outperforms existing approaches, achieving up to \textbf{6.28 db} higher message fidelity, \textbf{3$\times$} faster rendering, and exceptional robustness against aggressive 3D-targeted structural attacks (e.g., GSPure). Furthermore, our framework exhibits remarkable versatility, generalizing seamlessly to 2D image embedding, 4D dynamic scene steganography, and diverse downstream tasks.

  </details>


- **[TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239)**  
  *Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang, Zan Gojcic*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15239) · [pdf](https://arxiv.org/pdf/2604.15239.pdf)
  > 💡 针对传统沿射线回归深度的缺陷，提出直接预测3D坐标的可学习高斯令牌编码-解码架构，实现解耦预测与更优重建。

  <details><summary>Abstract</summary>

  In this work, we revisit several key design choices of modern Transformer-based approaches for feed-forward 3D Gaussian Splatting (3DGS) prediction. We argue that the common practice of regressing Gaussian means as depths along camera rays is suboptimal, and instead propose to directly regress 3D mean coordinates using only a self-supervised rendering loss. This formulation allows us to move from the standard encoder-only design to an encoder-decoder architecture with learnable Gaussian tokens, thereby unbinding the number of predicted primitives from input image resolution and number of views. Our resulting method, TokenGS, demonstrates improved robustness to pose noise and multiview inconsistencies, while naturally supporting efficient test-time optimization in token space without degrading learned priors. TokenGS achieves state-of-the-art feed-forward reconstruction performance on both static and dynamic scenes, producing more regularized geometry and more balanced 3DGS distribution, while seamlessly recovering emergent scene attributes such as static-dynamic decomposition and scene flow.

  </details>


- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782)**  
  *Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.14782) · [pdf](https://arxiv.org/pdf/2604.14782.pdf)
  > 💡 单张图像构建可动3D头像，显式解耦头发与面部，分别用FLAME网格和PBD笼控制变形，实现逼真头发动态。

  <details><summary>Abstract</summary>

  We propose a compositional method for constructing a complete 3D head avatar from a single image. Prior one-shot holistic approaches frequently fail to produce realistic hair dynamics during animation, largely due to inadequate decoupling of hair from the facial region, resulting in entangled geometry and unnatural deformations. Our method explicitly decouples hair from the face, modeling these components using distinct deformation paradigms while integrating them into a unified rendering pipeline. Furthermore, by leveraging image-to-3D lifting techniques, we preserve fine-grained textures from the input image to the greatest extent possible, effectively mitigating the common issue of high-frequency information loss in generalized models. Specifically, given a frontal portrait image, we first perform hair removal to obtain a bald image. Both the original image and the bald image are then lifted to dense, detail-rich 3D Gaussian Splatting (3DGS) representations. For the bald 3DGS, we rig it to a FLAME mesh via non-rigid registration with a prior model, enabling natural deformation that follows the mesh triangles during animation. For the hair component, we employ semantic label supervision combined with a boundary-aware reassignment strategy to extract a clean and isolated set of hair Gaussians. To control hair deformation, we introduce a cage structure that supports Position-Based Dynamics (PBD) simulation, allowing realistic and physically plausible transformations of the hair Gaussian primitives under head motion, gravity, and inertial effects. Striking qualitative results, including dynamic animations under diverse head motions, gravity effects, and expressions, showcase substantially more realistic hair behavior alongside faithfully preserved facial details, outperforming state-of-the-art one-shot methods in perceptual realism.

  </details>


- **[4D Radar Gaussian Modeling and Scan Matching with RCS](https://arxiv.org/abs/2604.14868)**  
  *Fernando Amodeo, Luis Merino, Fernando Caballero*  
  `2026-04-16` · `cs.RO` · [abs](https://arxiv.org/abs/2604.14868) · [pdf](https://arxiv.org/pdf/2604.14868.pdf)
  > 💡 针对4D雷达RCS被忽视问题，提出融合RCS物理特性的高斯建模与扫描匹配方法，提升匹配鲁棒性。

  <details><summary>Abstract</summary>

  4D millimeter-wave (mmWave) radars are increasingly used in robotics, as they offer robustness against adverse environmental conditions. Besides the usual XYZ position, they provide Doppler velocity measurements as well as Radar Cross Section (RCS) information for every point. While Doppler is widely used to filter out dynamic points, RCS is often overlooked and not usually used in modeling and scan matching processes. Building on previous 3D Gaussian modeling and scan matching work, we propose incorporating the physical behavior of RCS in the model, in order to further enrich the summarized information about the scene, and improve the scan matching process.

  </details>


- **[ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction](https://arxiv.org/abs/2604.13746)**  
  *Jie Liang, Jiahao Wu, Chao Wang, Jiayu Yang, Xiaoyun Zheng, Kaiqiang Xiong, Zhanke Wang, Jinbo Yan, Feng Gao, Ronggang Wang*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13746) · [pdf](https://arxiv.org/pdf/2604.13746.pdf)
  > 💡 针对长序列大运动动态场景，提出Clip-Stream高斯混合优化，用clip级时空场与残差锚点实现可扩展无闪烁高质量重建。

  <details><summary>Abstract</summary>

  Dynamic 3D scene reconstruction is essential for immersive media such as VR, MR, and XR, yet remains challenging for long multi-view sequences with large-scale motion. Existing dynamic Gaussian approaches are either Frame-Stream, offering scalability but poor temporal stability, or Clip, achieving local consistency at the cost of high memory and limited sequence length. We propose ClipGStream, a hybrid reconstruction framework that performs stream optimization at the clip level rather than the frame level. The sequence is divided into short clips, where dynamic motion is modeled using clip-independent spatio-temporal fields and residual anchor compensation to capture local variations efficiently, while inter-clip inherited anchors and decoders maintain structural consistency across clips. This Clip-Stream design enables scalable, flicker-free reconstruction of long dynamic videos with high temporal coherence and reduced memory overhead. Extensive experiments demonstrate that ClipGStream achieves state-of-the-art reconstruction quality and efficiency. The project page is available at: https://liangjie1999.github.io/ClipGStreamWeb/

  </details>


- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476)**  
  *Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo*  
  `2026-04-15` · `cs.RO` · [abs](https://arxiv.org/abs/2604.13476) · [pdf](https://arxiv.org/pdf/2604.13476.pdf)
  > 💡 现有机器人视觉系统视野窄、易抖动，提出RobotPan结合六相机与LiDAR，用稀疏视图预测度量尺度的紧凑3D高斯实现360度实时渲染与重建。

  <details><summary>Abstract</summary>

  Surround-view perception is increasingly important for robotic navigation and loco-manipulation, especially in human-in-the-loop settings such as teleoperation, data collection, and emergency takeover. However, current robotic visual interfaces are often limited to narrow forward-facing views, or, when multiple on-board cameras are available, require cumbersome manual switching that interrupts the operator's workflow. Both configurations suffer from motion-induced jitter that causes simulator sickness in head-mounted displays. We introduce a surround-view robotic vision system that combines six cameras with LiDAR to provide full 360$^\circ$ visual coverage, while meeting the geometric and real-time constraints of embodied deployment. We further present \textsc{RobotPan}, a feed-forward framework that predicts \emph{metric-scaled} and \emph{compact} 3D Gaussians from calibrated sparse-view inputs for real-time rendering, reconstruction, and streaming. \textsc{RobotPan} lifts multi-view features into a unified spherical coordinate representation and decodes Gaussians using hierarchical spherical voxel priors, allocating fine resolution near the robot and coarser resolution at larger radii to reduce computational redundancy without sacrificing fidelity. To support long sequences, our online fusion updates dynamic content while preventing unbounded growth in static regions by selectively updating appearance. Finally, we release a multi-sensor dataset tailored to 360$^\circ$ novel view synthesis and metric 3D reconstruction for robotics, covering navigation, manipulation, and locomotion on real platforms. Experiments show that \textsc{RobotPan} achieves competitive quality against prior feed-forward reconstruction and view-synthesis methods while producing substantially fewer Gaussians, enabling practical real-time embodied deployment.

  </details>


- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837)**  
  *Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu*  
  `2026-04-14` · `cs.RO` · [abs](https://arxiv.org/abs/2604.12837) · [pdf](https://arxiv.org/pdf/2604.12837.pdf)
  > 💡 针对动态环境单目SLAM位姿估计和密集重建退化问题，提出通用运动模型、动态语义分离与遮挡填充，实现性能领先。

  <details><summary>Abstract</summary>

  Visual SLAM algorithms achieve significant improvements through the exploration of 3D Gaussian Splatting (3DGS) representations, particularly in generating high-fidelity dense maps. However, they depend on a static environment assumption and experience significant performance degradation in dynamic environments. This paper presents GGD-SLAM, a framework that employs a generalizable motion model to address the challenges of localization and dense mapping in dynamic environments - without predefined semantic annotations or depth input. Specifically, the proposed system employs a First-In-First-Out (FIFO) queue to manage incoming frames, facilitating dynamic semantic feature extraction through a sequential attention mechanism. This is integrated with a dynamic feature enhancer to separate static and dynamic components. Additionally, to minimize dynamic distractors' impact on the static components, we devise a method to fill occluded areas via static information sampling and design a distractor-adaptive Structure Similarity Index Measure (SSIM) loss tailored for dynamic environments, significantly enhancing the system's resilience. Experiments conducted on real-world dynamic datasets demonstrate that the proposed system achieves state-of-the-art performance in camera pose estimation and dense reconstruction in dynamic scenes.

  </details>


- **[Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.12626)**  
  *Ziyuan Xia, Jingyi Xu, Chong Cui, Yuanhong Yu, Jiazhao Zhang, Qingsong Yan, Tao Ni, Junbo Chen, Xiaowei Zhou, Hujun Bao, Ruizhen Hu, Sida Peng*  
  `2026-04-14` · `cs.RO` · [abs](https://arxiv.org/abs/2604.12626) · [pdf](https://arxiv.org/pdf/2604.12626.pdf)
  > 💡 集成3DGS渲染与可驱动高斯化身，实现高保真动态导航模拟，提升跨域泛化和人类感知能力。

  <details><summary>Abstract</summary>

  Training embodied AI agents depends critically on the visual fidelity of simulation environments and the ability to model dynamic humans. Current simulators rely on mesh-based rasterization with limited visual realism, and their support for dynamic human avatars, where available, is constrained to mesh representations, hindering agent generalization to human-populated real-world scenarios. We present Habitat-GS, a navigation-centric embodied AI simulator extended from Habitat-Sim that integrates 3D Gaussian Splatting scene rendering and drivable gaussian avatars while maintaining full compatibility with the Habitat ecosystem. Our system implements a 3DGS renderer for real-time photorealistic rendering and supports scalable 3DGS asset import from diverse sources. For dynamic human modeling, we introduce a gaussian avatar module that enables each avatar to simultaneously serve as a photorealistic visual entity and an effective navigation obstacle, allowing agents to learn human-aware behaviors in realistic settings. Experiments on point-goal navigation demonstrate that agents trained on 3DGS scenes achieve stronger cross-domain generalization, with mixed-domain training being the most effective strategy. Evaluations on avatar-aware navigation further confirm that gaussian avatars enable effective human-aware navigation. Finally, performance benchmarks validate the system's scalability across varying scene complexity and avatar counts.

  </details>


- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251)**  
  *Xinliang Wang, Yifeng Shi, Zhenyu Wu*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.12251) · [pdf](https://arxiv.org/pdf/2604.12251.pdf)
  > 💡 针对3DGS稀疏视图退化，用大规模视频数据扩展和同构双模型范式的视频扩散及热图引导修复，实现SOTA性能。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) delivers high-fidelity real-time rendering but suffers from geometric and photometric degradations under sparse-view constraints. Current generative restoration approaches are often limited by insufficient temporal coherence, a lack of explicit spatial constraints, and a lack of large-scale training data, resulting in multi-view inconsistencies, erroneous geometric hallucinations, and limited generalization to diverse real-world artifact distributions. In this paper, we present ArtifactWorld, a framework that resolves 3DGS artifact repair through systematic data expansion and a homogeneous dual-model paradigm. To address the data bottleneck, we establish a fine-grained phenomenological taxonomy of 3DGS artifacts and construct a comprehensive training set of 107.5K diverse paired video clips to enhance model robustness. Architecturally, we unify the restoration process within a video diffusion backbone, utilizing an isomorphic predictor to localize structural defects via an artifact heatmap. This heatmap then guides the restoration through an Artifact-Aware Triplet Fusion mechanism, enabling precise, intensity-guided spatio-temporal repair within native self-attention. Extensive experiments demonstrate that ArtifactWorld achieves state-of-the-art performance in sparse novel view synthesis and robust 3D reconstruction. Code and dataset will be made public.

  </details>


- **[Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis](https://arxiv.org/abs/2604.11685)**  
  *Yuqin Lu, Yang Zhou, Yihua Dai, Guiqing Li, Shengfeng He*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11685) · [pdf](https://arxiv.org/pdf/2604.11685.pdf)
  > 💡 通过自顶向下的可学习掩码剪枝和层次空间网格与共享锚点码本，实现紧凑多级LOD的3DGS高效渐进渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become a state-of-the-art framework for real-time, high-fidelity novel view synthesis. However, its substantial storage requirements and inherently unstructured representation pose challenges for deployment in streaming and resource-constrained environments. Existing Level-of-Detail (LOD) strategies, particularly those based on bottom-up construction, often introduce redundancy or lead to fidelity degradation. To overcome these limitations, we propose Iterative Gaussian Synopsis, a novel framework for compact and progressive rendering through a top-down "unfolding" scheme. Our approach begins with a full-resolution 3DGS model and iteratively derives coarser LODs using an adaptive, learnable mask-based pruning mechanism. This process constructs a multi-level hierarchy that preserves visual quality while improving efficiency. We integrate hierarchical spatial grids, which capture the global scene structure, with a shared Anchor Codebook that models localized details. This combination produces a compact yet expressive feature representation, designed to minimize redundancy and support efficient, level-specific adaptation. The unfolding mechanism promotes inter-layer reusability and requires only minimal data overhead for progressive refinement. Experiments show that our method maintains high rendering quality across all LODs while achieving substantial storage reduction. These results demonstrate the practicality and scalability of our approach for real-time 3DGS rendering in bandwidth- and memory-constrained scenarios.

  </details>


- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671)**  
  *Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka*  
  `2026-04-08` · `eess.IV` · [abs](https://arxiv.org/abs/2604.06671) · [pdf](https://arxiv.org/pdf/2604.06671.pdf)
  > 💡 多相机4D高斯泼溅重建硅胶血管模型，实现时间分辨位移与应力代理测量，支持血栓切除台架分析。

  <details><summary>Abstract</summary>

  Introduction: Mechanical thrombectomy can cause vessel deformation and procedure-related injury. Benchtop models are widely used for device testing, but time-resolved, full-field 3D vessel-motion measurements remain limited. Methods: We developed a nine-camera, low-cost multi-view workflow for benchtop thrombectomy in silicone middle cerebral artery phantoms (2160p, 20 fps). Multi-view videos were calibrated, segmented, and reconstructed with 4D Gaussian Splatting. Reconstructed point clouds were converted to fixed-connectivity edge graphs for region-of-interest (ROI) displacement tracking and a relative surface-based stress proxy. Stress-proxy values were derived from edge stretch using a Neo-Hookean mapping and reported as comparative surface metrics. A synthetic Blender pipeline with known deformation provided geometric and temporal validation. Results: In synthetic bulk translation, the stress proxy remained near zero for most edges (median $\approx$ 0 MPa; 90th percentile 0.028 MPa), with sparse outliers. In synthetic pulling (1-5 mm), reconstruction showed close geometric and temporal agreement with ground truth, with symmetric Chamfer distance of 1.714-1.815 mm and precision of 0.964-0.972 at $τ= 1$ mm. In preliminary benchtop comparative trials (one trial per condition), cervical aspiration catheter placement showed higher max-median ROI displacement and stress-proxy values than internal carotid artery terminus placement. Conclusion: The proposed protocol provides standardized, time-resolved surface kinematics and comparative relative displacement and stress proxy measurements for thrombectomy benchtop studies. The framework supports condition-to-condition comparisons and methods validation, while remaining distinct from absolute wall-stress estimation. Implementation code and example data are available at https://ethanuser.github.io/vessel4D

  </details>


- **[AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://arxiv.org/abs/2604.04787)**  
  *Hongyu Liu, Xuan Wang, Zijian Wu, Yating Wang, Ziyu Wan, Yue Ma, Runtao Liu, Boyao Zhou, Yujun Shen, Qifeng Chen*  
  `2026-04-06` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04787) · [pdf](https://arxiv.org/pdf/2604.04787.pdf)
  > 💡 提出自回归Transformer生成3D高斯点云，从单图创建高质量可控4D动态化身。

  <details><summary>Abstract</summary>

  We introduce AvatarPointillist, a novel framework for generating dynamic 4D Gaussian avatars from a single portrait image. At the core of our method is a decoder-only Transformer that autoregressively generates a point cloud for 3D Gaussian Splatting. This sequential approach allows for precise, adaptive construction, dynamically adjusting point density and the total number of points based on the subject's complexity. During point generation, the AR model also jointly predicts per-point binding information, enabling realistic animation. After generation, a dedicated Gaussian decoder converts the points into complete, renderable Gaussian attributes. We demonstrate that conditioning the decoder on the latent features from the AR generator enables effective interaction between stages and markedly improves fidelity. Extensive experiments validate that AvatarPointillist produces high-quality, photorealistic, and controllable avatars. We believe this autoregressive formulation represents a new paradigm for avatar generation, and we will release our code inspire future research.

  </details>


- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063)**  
  *Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu*  
  `2026-04-05` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04063) · [pdf](https://arxiv.org/pdf/2604.04063.pdf)
  > 💡 提出4C4D框架，用神经衰减函数增强高斯不透明度几何学习，以极稀疏四相机视频实现高保真4D动态场景渲染。

  <details><summary>Abstract</summary>

  This paper tackles the challenge of recovering 4D dynamic scenes from videos captured by as few as four portable cameras. Learning to model scene dynamics for temporally consistent novel-view rendering is a foundational task in computer graphics, where previous works often require dense multi-view captures using camera arrays of dozens or even hundreds of views. We propose \textbf{4C4D}, a novel framework that enables high-fidelity 4D Gaussian Splatting from video captures of extremely sparse cameras. Our key insight lies that the geometric learning under sparse settings is substantially more difficult than modeling appearance. Driven by this observation, we introduce a Neural Decaying Function on Gaussian opacities for enhancing the geometric modeling capability of 4D Gaussians. This design mitigates the inherent imbalance between geometry and appearance modeling in 4DGS by encouraging the 4DGS gradients to focus more on geometric learning. Extensive experiments across sparse-view datasets with varying camera overlaps show that 4C4D achieves superior performance over prior art. Project page at: https://junshengzhou.github.io/4C4D.

  </details>


- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016)**  
  *Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang*  
  `2026-04-05` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04016) · [pdf](https://arxiv.org/pdf/2604.04016.pdf)
  > 💡 提出交叉注意力HOI模块显式建模人-物交互形变，用HexPlane和CHS分别处理人体和物体，提升动态场景重建质量。

  <details><summary>Abstract</summary>

  Reconstructing dynamic scenes with complex human-object interactions is a fundamental challenge in computer vision and graphics. Existing Gaussian Splatting methods either rely on human pose priors while neglecting dynamic objects, or approximate all motions within a single field, limiting their ability to capture interaction-rich dynamics. To address this gap, we propose Human-Object Interaction Gaussian Splatting (HOIGS), which explicitly models interaction-induced deformation between humans and objects through a cross-attention-based HOI module. Distinct deformation baselines are employed to extract features: HexPlane for humans and Cubic Hermite Spline (CHS) for objects. By integrating these heterogeneous features, HOIGS effectively captures interdependent motions and improves deformation estimation in scenarios involving occlusion, contact, and object manipulation. Comprehensive experiments on multiple datasets demonstrate that our method consistently outperforms state-of-the-art human-centric and 4D Gaussian approaches, highlighting the importance of explicitly modeling human-object interactions for high-fidelity reconstruction.

  </details>


- **[GP-4DGS: Probabilistic 4D Gaussian Splatting from Monocular Video via Variational Gaussian Processes](https://arxiv.org/abs/2604.02915)**  
  *Mijeong Kim, Jungtaek Kim, Bohyung Han*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02915) · [pdf](https://arxiv.org/pdf/2604.02915.pdf)
  > 💡 针对4DGS缺少运动不确定性量化，引入变分高斯过程实现概率建模和可靠预测。

  <details><summary>Abstract</summary>

  We present GP-4DGS, a novel framework that integrates Gaussian Processes (GPs) into 4D Gaussian Splatting (4DGS) for principled probabilistic modeling of dynamic scenes. While existing 4DGS methods focus on deterministic reconstruction, they are inherently limited in capturing motion ambiguity and lack mechanisms to assess prediction reliability. By leveraging the kernel-based probabilistic nature of GPs, our approach introduces three key capabilities: (i) uncertainty quantification for motion predictions, (ii) motion estimation for unobserved or sparsely sampled regions, and (iii) temporal extrapolation beyond observed training frames. To scale GPs to the large number of Gaussian primitives in 4DGS, we design spatio-temporal kernels that capture the correlation structure of deformation fields and adopt variational Gaussian Processes with inducing points for tractable inference. Our experiments show that GP-4DGS enhances reconstruction quality while providing reliable uncertainty estimates that effectively identify regions of high motion ambiguity. By addressing these challenges, our work takes a meaningful step toward bridging probabilistic modeling and neural graphics.

  </details>


- **[Streaming Real-Time Rendered Scenes as 3D Gaussians](https://arxiv.org/abs/2604.02851)**  
  *Matti Siekkinen, Teemu Kämäräinen*  
  `2026-04-03` · `eess.IV` · [abs](https://arxiv.org/abs/2604.02851) · [pdf](https://arxiv.org/pdf/2604.02851.pdf)
  > 💡 针对云渲染2D视频流视点受限

  <details><summary>Abstract</summary>

  Cloud rendering is widely used in gaming and XR to overcome limited client-side GPU resources and to support heterogeneous devices. Existing systems typically deliver the rendered scene as a 2D video stream, which tightly couples the transmitted content to the server-rendered viewpoint and limits latency compensation to image-space reprojection or warping. In this paper, we investigate an alternative approach based on streaming a live 3D Gaussian Splatting (3DGS) scene representation instead of only rendered video. We present a Unity-based prototype in which a server constructs and continuously optimizes a 3DGS model from real-time rendered reference views, while streaming the evolving representation to remote clients using full model snapshots and incremental updates supporting relighting and rigid object dynamics. The clients reconstruct the streamed Gaussian model locally and render their current viewpoint from the received representation. This approach aims to improve viewpoint flexibility for latency compensation and to better amortize server-side scene modeling across multiple users than per-user rendering and video streaming. We describe the system design, evaluate it, and compare it with conventional image warping.

  </details>


- **[NavCrafter: Exploring 3D Scenes from a Single Image](https://arxiv.org/abs/2604.02828)**  
  *Hongbo Duan, Peiyu Zhuang, Yi Liu, Zhengyang Zhang, Yuxin Zhang, Pengting Luo, Fangming Liu, Xueqian Wang*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02828) · [pdf](https://arxiv.org/pdf/2604.02828.pdf)
  > 💡 从单张图像生成可控制相机路径的3D场景，利用视频扩散几何扩展和增强3DGS实现大视角新视图合成与高保真重建。

  <details><summary>Abstract</summary>

  Creating flexible 3D scenes from a single image is vital when direct 3D data acquisition is costly or impractical. We introduce NavCrafter, a novel framework that explores 3D scenes from a single image by synthesizing novel-view video sequences with camera controllability and temporal-spatial consistency. NavCrafter leverages video diffusion models to capture rich 3D priors and adopts a geometry-aware expansion strategy to progressively extend scene coverage. To enable controllable multi-view synthesis, we introduce a multi-stage camera control mechanism that conditions diffusion models with diverse trajectories via dual-branch camera injection and attention modulation. We further propose a collision-aware camera trajectory planner and an enhanced 3D Gaussian Splatting (3DGS) pipeline with depth-aligned supervision, structural regularization and refinement. Extensive experiments demonstrate that NavCrafter achieves state-of-the-art novel-view synthesis under large viewpoint shifts and substantially improves 3D reconstruction fidelity.

  </details>


- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781)**  
  *Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen*  
  `2026-04-03` · `cs.SD` · [abs](https://arxiv.org/abs/2604.02781) · [pdf](https://arxiv.org/pdf/2604.02781.pdf)
  > 💡 针对动态声学复杂场景，提出DynFOA结合3DGS重建与条件扩散生成一阶高保真立体声，并贡献M2G-360数据集。

  <details><summary>Abstract</summary>

  Spatial audio is crucial for immersive 360-degree video experiences, yet most 360-degree videos lack it due to the difficulty of capturing spatial audio during recording. Automatically generating spatial audio such as first-order ambisonics (FOA) from video therefore remains an important but challenging problem. In complex scenes, sound perception depends not only on sound source locations but also on scene geometry, materials, and dynamic interactions with the environment. However, existing approaches only rely on visual cues and fail to model dynamic sources and acoustic effects such as occlusion, reflections, and reverberation. To address these challenges, we propose DynFOA, a generative framework that synthesizes FOA from 360-degree videos by integrating dynamic scene reconstruction with conditional diffusion modeling. DynFOA analyzes the input video to detect and localize dynamic sound sources, estimate depth and semantics, and reconstruct scene geometry and materials using 3D Gaussian Splatting (3DGS). The reconstructed scene representation provides physically grounded features that capture acoustic interactions between sources, environment, and listener viewpoint. Conditioned on these features, a diffusion model generates spatial audio consistent with the scene dynamics and acoustic context. We introduce M2G-360, a dataset of 600 real-world clips divided into MoveSources, Multi-Source, and Geometry subsets for evaluating robustness under diverse conditions. Experiments show that DynFOA consistently outperforms existing methods in spatial accuracy, acoustic fidelity, distribution matching, and perceived immersive experience.

  </details>


- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678)**  
  *Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01678) · [pdf](https://arxiv.org/pdf/2604.01678.pdf)
  > 💡 针对动态场景缺乏实例级语义的问题，提出将实例一致语义嵌入4D高斯，结合光流与SDF约束，实现高保真渲染、实例分割和开放词汇查询。

  <details><summary>Abstract</summary>

  Volumetric video seeks to model dynamic scenes as temporally coherent 4D representations. While recent Gaussian-based approaches achieve impressive rendering fidelity, they primarily emphasize appearance but are largely agnostic to instance-level structure, limiting stable tracking and semantic reasoning in highly dynamic scenarios. In this paper, we present Director, a unified spatio-temporal Gaussian representation that jointly models human performance, high-fidelity rendering, and instance-level semantics. Our key insight is that embedding instance-consistent semantics naturally complements 4D modeling, enabling more accurate scene decomposition while supporting robust dynamic scene understanding. To this end, we leverage temporally aligned instance masks and sentence embeddings derived from Multimodal Large Language Models to supervise the learnable semantic features of each Gaussian via two MLP decoders, enabling language-aligned 4D representations and enforcing identity consistency over time. To enhance temporal stability, we bridge 2D optical flow with 4D Gaussians and finetune their motions, yielding reliable initialization and reducing drift. For the training, we further introduce a geometry-aware SDF constraints, along with regularization terms that enforces surface continuity, enhancing temporal coherence in dynamic foreground modeling. Experiments demonstrate that Director achieves temporally coherent 4D reconstructions while simultaneously enabling instance segmentation and open-vocabulary querying.

  </details>


- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586)**  
  *Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02586) · [pdf](https://arxiv.org/pdf/2604.02586.pdf)
  > 💡 将点跟踪与3D高斯结合，用像素轨迹指导高斯变换，解决大位移下的伪影问题，提升动态重建鲁棒性与吞吐量。

  <details><summary>Abstract</summary>

  Recent advancements in 3D Gaussian Splatting (3DGS) have demonstrated its potential for efficient and photorealistic 3D reconstructions, which is crucial for diverse applications such as robotics and immersive media. However, current Gaussian-based methods for dynamic scene reconstruction struggle with large inter-frame displacements, leading to artifacts and temporal inconsistencies under fast object motions. To address this, we introduce \textit{TrackerSplat}, a novel method that integrates advanced point tracking methods to enhance the robustness and scalability of 3DGS for dynamic scene reconstruction. TrackerSplat utilizes off-the-shelf point tracking models to extract pixel trajectories and triangulate per-view pixel trajectories onto 3D Gaussians to guide the relocation, rotation, and scaling of Gaussians before training. This strategy effectively handles large displacements between frames, dramatically reducing the fading and recoloring artifacts prevalent in prior methods. By accurately positioning Gaussians prior to gradient-based optimization, TrackerSplat overcomes the quality degradation associated with large frame gaps when processing multiple adjacent frames in parallel across multiple devices, thereby boosting reconstruction throughput while preserving rendering quality. Experiments on real-world datasets confirm the robustness of TrackerSplat in challenging scenarios with significant displacements, achieving superior throughput under parallel settings and maintaining visual quality compared to baselines. The code is available at https://github.com/yindaheng98/TrackerSplat.

  </details>


- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538)**  
  *Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.00538) · [pdf](https://arxiv.org/pdf/2604.00538.pdf)
  > 💡 现有4DGS因分段线性近似导致时间碎片化和内存爆炸，TRiGS用SE(3)变换和贝塞尔残差实现连续刚体运动，高效扩展至长视频。

  <details><summary>Abstract</summary>

  Recent 4D Gaussian Splatting (4DGS) methods achieve impressive dynamic scene reconstruction but often rely on piecewise linear velocity approximations and short temporal windows. This disjointed modeling leads to severe temporal fragmentation, forcing primitives to be repeatedly eliminated and regenerated to track complex nonlinear dynamics. This makeshift approximation eliminates the long-term temporal identity of objects and causes an inevitable proliferation of Gaussians, hindering scalability to extended video sequences. To address this, we propose TRiGS, a novel 4D representation that utilizes unified, continuous geometric transformations. By integrating $SE(3)$ transformations, hierarchical Bezier residuals, and learnable local anchors, TRiGS models geometrically consistent rigid motions for individual primitives. This continuous formulation preserves temporal identity and effectively mitigates unbounded memory growth. Extensive experiments demonstrate that TRiGS achieves high fidelity rendering on standard benchmarks while uniquely scaling to extended video sequences (e.g., 600 to 1200 frames) without severe memory bottlenecks, significantly outperforming prior works in temporal stability.

  </details>


- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296)**  
  *Haoran Zhou, Gim Hee Lee*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2603.29296) · [pdf](https://arxiv.org/pdf/2603.29296.pdf)
  > 💡 提出可缩放4D高斯泼溅框架，用簇中心基础变换和渐进优化实现大规模动态场景的高质量几何与运动重建。

  <details><summary>Abstract</summary>

  Realistic reconstruction of dynamic 4D scenes from monocular videos is essential for understanding the physical world. Despite recent progress in neural rendering, existing methods often struggle to recover accurate 3D geometry and temporally consistent motion in complex environments. To address these challenges, we propose MotionScale, a 4D Gaussian Splatting framework that scales efficiently to large scenes and extended sequences while maintaining high-fidelity structural and motion coherence. At the core of our approach is a scalable motion field parameterized by cluster-centric basis transformations that adaptively expand to capture diverse and evolving motion patterns. To ensure robust reconstruction over long durations, we introduce a progressive optimization strategy comprising two decoupled propagation stages: 1) A background extension stage that adapts to newly visible regions, refines camera poses, and explicitly models transient shadows; 2) A foreground propagation stage that enforces motion consistency through a specialized three-stage refinement process. Extensive experiments on challenging real-world benchmarks demonstrate that MotionScale significantly outperforms state-of-the-art methods in both reconstruction quality and temporal stability. Project page: https://hrzhou2.github.io/motion-scale-web/.

  </details>


- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152)**  
  *Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi*  
  `2026-03-30` · `cs.CV` · [abs](https://arxiv.org/abs/2603.28152) · [pdf](https://arxiv.org/pdf/2603.28152.pdf)
  > 💡 针对2D编辑缺乏3D感知，提出ObjectMorpher，利用

  <details><summary>Abstract</summary>

  Achieving precise, object-level control in image editing remains challenging: 2D methods lack 3D awareness and often yield ambiguous or implausible results, while existing 3D-aware approaches rely on heavy optimization or incomplete monocular reconstructions. We present ObjectMorpher, a unified, interactive framework that converts ambiguous 2D edits into geometry-grounded operations. ObjectMorpher lifts target instances with an image-to-3D generator into editable 3D Gaussian Splatting (3DGS), enabling fast, identity-preserving manipulation. Users drag control points; a graph-based non-rigid deformation with as-rigid-as-possible (ARAP) constraints ensures physically sensible shape and pose changes. A composite diffusion module harmonizes lighting, color, and boundaries for seamless reintegration. Across diverse categories, ObjectMorpher delivers fine-grained, photorealistic edits with superior controllability and efficiency, outperforming 2D drag and 3D-aware baselines on KID, LPIPS, SIFID, and user preference.

  </details>


- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067)**  
  *Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao*  
  `2026-03-27` · `cs.CV` · [abs](https://arxiv.org/abs/2603.26067) · [pdf](https://arxiv.org/pdf/2603.26067.pdf)
  > 💡 针对物理对抗伪装不鲁棒，提出可重照明3DGS与硬物理配置挖掘，提升模拟真实性和优化鲁棒性。

  <details><summary>Abstract</summary>

  Physical adversarial camouflage poses a severe security threat to autonomous driving systems by mapping adversarial textures onto 3D objects. Nevertheless, current methods remain brittle in complex dynamic scenarios, failing to generalize across diverse geometric (e.g., viewing configurations) and radiometric (e.g., dynamic illumination, atmospheric scattering) variations. We attribute this deficiency to two fundamental limitations in simulation and optimization. First, the reliance on coarse, oversimplified simulations (e.g., via CARLA) induces a significant domain gap, confining optimization to a biased feature space. Second, standard strategies targeting average performance result in a rugged loss landscape, leaving the camouflage vulnerable to configuration shifts.To bridge these gaps, we propose the Relightable Physical 3D Gaussian Splatting (3DGS) based Attack framework (R-PGA). Technically, to address the simulation fidelity issue, we leverage 3DGS to ensure photo-realistic reconstruction and augment it with physically disentangled attributes to decouple intrinsic material from lighting. Furthermore, we design a hybrid rendering pipeline that leverages precise Relightable 3DGS for foreground rendering, while employing a pre-trained image translation model to synthesize plausible relighted backgrounds that align with the relighted foreground.To address the optimization robustness issue, we propose the Hard Physical Configuration Mining (HPCM) module, designed to actively mine worst-case physical configurations and suppress their corresponding loss peaks. This strategy not only diminishes the overall loss magnitude but also effectively flattens the rugged loss landscape, ensuring consistent adversarial effectiveness and robustness across varying physical configurations.

  </details>


- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814)**  
  *Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu*  
  `2026-03-26` · `cs.CV` · [abs](https://arxiv.org/abs/2603.26814) · [pdf](https://arxiv.org/pdf/2603.26814.pdf)
  > 💡 利用3DGS与XPBD融合物理感知变形约束，实现手术环境中更稳定可解释的可操作推理。

  <details><summary>Abstract</summary>

  Affordance reasoning provides a principled link between perception and action, yet remains underexplored in surgical robotics, where tissues are highly deformable, compliant, and dynamically coupled with tool motion. We present arg-VU, a physics-aware affordance reasoning framework that integrates temporally consistent geometry tracking with constraint-induced mechanical modeling for surgical visual understanding. Surgical scenes are reconstructed using 3D Gaussian Splatting (3DGS) and converted into a temporally tracked surface representation. Extended Position-Based Dynamics (XPBD) embeds local deformation constraints and produces representative geometry points (RGPs) whose constraint sensitivities define anisotropic stiffness metrics capturing the local constraint-manifold geometry. Robotic tool poses in SE(3) are incorporated to compute rigidly induced displacements at RGPs, from which we derive two complementary measures: a physics-aware compliance energy that evaluates mechanical feasibility with respect to local deformation constraints, and a positional agreement score that captures motion alignment (as kinematic motion baseline). Experiments on surgical video datasets show that arg-VU yields more stable, physically consistent, and interpretable affordance predictions than kinematic baselines. These results demonstrate that physics-aware geometric representations enable reliable affordance reasoning for deformable surgical environments and support embodied robotic interaction.

  </details>


- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402)**  
  *Yonghan Lee, Dinesh Manocha*  
  `2026-03-19` · `cs.CV` · [abs](https://arxiv.org/abs/2603.18402) · [pdf](https://arxiv.org/pdf/2603.18402.pdf)
  > 💡 通过可微排列学习对齐多视频实例标签，实现实例分解4DGS，显著提升渲染与分割质量。

  <details><summary>Abstract</summary>

  We present Inst4DGS, an instance-decomposed 4D Gaussian Splatting (4DGS) approach with long-horizon per-Gaussian trajectories. While dynamic 4DGS has advanced rapidly, instance-decomposed 4DGS remains underexplored, largely due to the difficulty of associating inconsistent instance labels across independently segmented multi-view videos. We address this challenge by introducing per-video label-permutation latents that learn cross-video instance matches through a differentiable Sinkhorn layer, enabling direct multi-view supervision with consistent identity preservation. This explicit label alignment yields sharp decision boundaries and temporally stable identities without identity drift. To further improve efficiency, we propose instance-decomposed motion scaffolds that provide low-dimensional motion bases per object for long-horizon trajectory optimization. Experiments on Panoptic Studio and Neural3DV show that Inst4DGS jointly supports tracking and instance decomposition while achieving state-of-the-art rendering and segmentation quality. On the Panoptic Studio dataset, Inst4DGS improves PSNR from 26.10 to 28.36, and instance mIoU from 0.6310 to 0.9129, over the strongest baseline.

  </details>


- **[Adaptive Anchor Policies for Efficient 4D Gaussian Streaming](https://arxiv.org/abs/2603.17227)**  
  *Ashim Dahal, Rabab Abdelfattah, Nick Rahimi*  
  `2026-03-18` · `cs.CV` · [abs](https://arxiv.org/abs/2603.17227) · [pdf](https://arxiv.org/pdf/2603.17227.pdf)
  > 💡 针对固定锚点选择导致计算浪费的问题，提出强化学习驱动的自适应锚点策略，在4D高斯流中提升质量-效率权衡。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction with Gaussian Splatting has enabled efficient streaming for real-time rendering and free-viewpoint video. However, most pipelines rely on fixed anchor selection such as Farthest Point Sampling (FPS), typically using 8,192 anchors regardless of scene complexity, which over-allocates computation under strict budgets. We propose Efficient Gaussian Streaming (EGS), a plug-in, budget-aware anchor sampler that replaces FPS with a reinforcement-learned policy while keeping the Gaussian streaming reconstruction backbone unchanged. The policy jointly selects an anchor budget and a subset of informative anchors under discrete constraints, balancing reconstruction quality and runtime using spatial features of the Gaussian representation. We evaluate EGS in two settings: fast rendering, which prioritizes runtime efficiency, and high-quality refinement, which enables additional optimization. Experiments on dynamic multi-view datasets show consistent improvements in the quality--efficiency trade-off over FPS sampling. On unseen data, in fast rendering at 256 anchors ($32\times$ fewer than 8,192), EGS improves PSNR by $+0.52$--$0.61$\,dB while running $1.29$--$1.35\times$ faster than IGS@8192 (N3DV and MeetingRoom). In high-quality refinement, EGS remains competitive with the full-anchor baseline at substantially lower anchor budgets. \emph{Code and pretrained checkpoints will be released upon acceptance.} \keywords{4D Gaussian Splatting \and 4D Gaussian Streaming \and Reinforcement Learning}

  </details>


- **[4D Synchronized Fields: Motion-Language Gaussian Splatting for Temporal Scene Understanding](https://arxiv.org/abs/2603.14301)**  
  *Mohamed Rayan Barhdadi, Samir Abdaljalil, Rasul Khanbayov, Erchin Serpedin, Hasan Kurban*  
  `2026-03-15` · `cs.CV` · [abs](https://arxiv.org/abs/2603.14301) · [pdf](https://arxiv.org/pdf/2603.14301.pdf)
  > 💡 因子化物体运动并同步语言场的4D高斯表示，实现重建-运动-语义耦合，时空查询精度领先。

  <details><summary>Abstract</summary>

  Current 4D representations decouple geometry, motion, and semantics: reconstruction methods discard interpretable motion structure; language-grounded methods attach semantics after motion is learned, blind to how objects move; and motion-aware methods encode dynamics as opaque per-point residuals without object-level organization. We propose 4D Synchronized Fields, a 4D Gaussian representation that learns object-factored motion in-loop during reconstruction and synchronizes language to the resulting kinematics through a per-object conditioned field. Each Gaussian trajectory is decomposed into shared object motion plus an implicit residual, and a kinematic-conditioned ridge map predicts temporal semantic variation, yielding a single representation in which reconstruction, motion, and semantics are structurally coupled and enabling open-vocabulary temporal queries that retrieve both objects and moments. On HyperNeRF, 4D Synchronized Fields achieves 28.52 dB mean PSNR, the highest among all language-grounded and motion-aware baselines, within 1.5 dB of reconstruction-only methods. On targeted temporal-state retrieval, the kinematic-conditioned field attains 0.884 mean accuracy, 0.815 mean vIoU, and 0.733 mean tIoU, surpassing 4D LangSplat (0.620, 0.433, and 0.439 respectively) and LangSplat (0.415, 0.304, and 0.262). Ablation confirms that kinematic conditioning is the primary driver, accounting for +0.45 tIoU over a static-embedding-only baseline. 4D Synchronized Fields is the only method that jointly exposes interpretable motion primitives and temporally grounded language fields from a single trained representation. Code will be released.

  </details>


- **[RetimeGS: Continuous-Time Reconstruction of 4D Gaussian Splatting](https://arxiv.org/abs/2603.13783)**  
  *Xuezhen Wang, Li Ma, Yulin Shen, Zeyu Wang, Pedro V. Sander*  
  `2026-03-14` · `cs.CV` · [abs](https://arxiv.org/abs/2603.13783) · [pdf](https://arxiv.org/pdf/2603.13783.pdf)
  > 💡 针对4DGS时间混叠导致的插值鬼影，提出显式高斯时间行为建模与光流引导策略，实现无鬼影连续时间渲染。

  <details><summary>Abstract</summary>

  Temporal retiming, the ability to reconstruct and render dynamic scenes at arbitrary timestamps, is crucial for applications such as slow-motion playback, temporal editing, and post-production. However, most existing 4D Gaussian Splatting (4DGS) methods overfit at discrete frame indices but struggle to represent continuous-time frames, leading to ghosting artifacts when interpolating between timestamps. We identify this limitation as a form of temporal aliasing and propose RetimeGS, a simple yet effective 4DGS representation that explicitly defines the temporal behavior of the 3D Gaussian and mitigates temporal aliasing. To achieve smooth and consistent interpolation, we incorporate optical flow-guided initialization and supervision, triple-rendering supervision, and other targeted strategies. Together, these components enable ghost-free, temporally coherent rendering even under large motions. Experiments on datasets featuring fast motion, non-rigid deformation, and severe occlusions demonstrate that RetimeGS achieves superior quality and coherence over state-of-the-art methods.

  </details>


- **[Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation](https://arxiv.org/abs/2603.12766)**  
  *Shifeng Chen, Yihui Li, Jun Liao, Hongyu Yang, Di Huang*  
  `2026-03-13` · `cs.CV` · [abs](https://arxiv.org/abs/2603.12766) · [pdf](https://arxiv.org/pdf/2603.12766.pdf)
  > 💡 引入锚点运动引导和颜色不确定性外观精炼，解决动态编辑时序闪烁与运动漂移，实现高保真4D编辑。

  <details><summary>Abstract</summary>

  Recent advances in 3D scene editing using NeRF and 3DGS enable high-quality static scene editing. In contrast, dynamic scene editing remains challenging, as methods that directly extend 2D diffusion models to 4D often produce motion artifacts, temporal flickering, and inconsistent style propagation. We introduce Catalyst4D, a framework that transfers high-quality 3D edits to dynamic 4D Gaussian scenes while maintaining spatial and temporal coherence. At its core, Anchor-based Motion Guidance (AMG) builds a set of structurally stable and spatially representative anchors from both original and edited Gaussians. These anchors serve as robust region-level references, and their correspondences are established via optimal transport to enable consistent deformation propagation without cross-region interference or motion drift. Complementarily, Color Uncertainty-guided Appearance Refinement (CUAR) preserves temporal appearance consistency by estimating per-Gaussian color uncertainty and selectively refining regions prone to occlusion-induced artifacts. Extensive experiments demonstrate that Catalyst4D achieves temporally stable, high-fidelity dynamic scene editing and outperforms existing methods in both visual quality and motion coherence.

  </details>


- **[Mango-GS: Enhancing Spatio-Temporal Consistency in Dynamic Scenes Reconstruction using Multi-Frame Node-Guided 4D Gaussian Splatting](https://arxiv.org/abs/2603.11543)**  
  *Tingxuan Huang, Haowei Zhu, Jun-hai Yong, Hao Pan, Bin Wang*  
  `2026-03-12` · `cs.CV` · [abs](https://arxiv.org/abs/2603.11543) · [pdf](https://arxiv.org/pdf/2603.11543.pdf)
  > 💡 使用多帧节点引导与时序Transformer解决动态场景时空不一致，实现高保真重建与实时渲染。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes with photorealistic detail and strong temporal coherence remains a significant challenge. Existing Gaussian splatting approaches for dynamic scene modeling often rely on per-frame optimization, which can overfit to instantaneous states instead of capturing underlying motion dynamics. To address this, we present Mango-GS, a multi-frame, node-guided framework for high-fidelity 4D reconstruction. Mango-GS leverages a temporal Transformer to model motion dependencies within a short window of frames, producing temporally consistent deformations. For efficiency, temporal modeling is confined to a sparse set of control nodes. Each node is represented by a decoupled canonical position and a latent code, providing a stable semantic anchor for motion propagation and preventing correspondence drift under large motion. Our framework is trained end-to-end, enhanced by an input masking strategy and two multi-frame losses to improve robustness. Extensive experiments demonstrate that Mango-GS achieves state-of-the-art reconstruction quality and real-time rendering speed, enabling high-fidelity reconstruction and interactive rendering of dynamic scenes.

  </details>


- **[HDR-NSFF: High Dynamic Range Neural Scene Flow Fields](https://arxiv.org/abs/2603.08313)**  
  *Shin Dong-Yeon, Kim Jun-Seong, Kwon Byung-Ki, Tae-Hyun Oh*  
  `2026-03-09` · `cs.CV` · [abs](https://arxiv.org/abs/2603.08313) · [pdf](https://arxiv.org/pdf/2603.08313.pdf)
  > 💡 用4D时空建模替换2D对齐，结合曝光不变运动估计和生成先验，实现动态场景高动态范围重建与时空视图合成。

  <details><summary>Abstract</summary>

  Radiance of real-world scenes typically spans a much wider dynamic range than what standard cameras can capture. While conventional HDR methods merge alternating-exposure frames, these approaches are inherently constrained to 2D pixel-level alignment, often leading to ghosting artifacts and temporal inconsistency in dynamic scenes. To address these limitations, we present HDR-NSFF, a paradigm shift from 2D-based merging to 4D spatio-temporal modeling. Our framework reconstructs dynamic HDR radiance fields from alternating-exposure monocular videos by representing the scene as a continuous function of space and time, and is compatible with both neural radiance field and 4D Gaussian Splatting (4DGS) based dynamic representations. This unified end-to-end pipeline explicitly models HDR radiance, 3D scene flow, geometry, and tone-mapping, ensuring physical plausibility and global coherence. We further enhance robustness by (i) extending semantic-based optical flow with DINO features to achieve exposure-invariant motion estimation, and (ii) incorporating a generative prior as a regularizer to compensate for limited observation in monocular captures and saturation-induced information loss. To evaluate HDR space-time view synthesis, we present the first real-world HDR-GoPro dataset specifically designed for dynamic HDR scenes. Experiments demonstrate that HDR-NSFF recovers fine radiance details and coherent dynamics even under challenging exposure variations, thereby achieving state-of-the-art performance in novel space-time view synthesis. Project page: https://shin-dong-yeon.github.io/HDR-NSFF/

  </details>


- **[ReconDrive: Fast Feed-Forward 4D Gaussian Splatting for Autonomous Driving Scene Reconstruction](https://arxiv.org/abs/2603.07552)**  
  *Haibao Yu, Kuntao Xiao, Jiahang Wang, Ruiyang Hao, Yuxin Huang, Guoran Hu, Haifang Qin, Bowen Jing, Yuntian Bo, Ping Luo*  
  `2026-03-08` · `cs.CV` · [abs](https://arxiv.org/abs/2603.07552) · [pdf](https://arxiv.org/pdf/2603.07552.pdf)
  > 💡 基于3D基础模型VGGT，提出混合高斯预测头和静动态组合策略，实现快速高保真4DGS重建，性能与逐场景优化相当且速度更快。

  <details><summary>Abstract</summary>

  High-fidelity visual reconstruction and novel-view synthesis are essential for realistic closed-loop evaluation in autonomous driving. While 4D Gaussian Splatting (4DGS) offers a promising balance of accuracy and efficiency, existing per-scene optimization methods require costly iterative refinement, rendering them unscalable for extensive urban environments. Conversely, current feed-forward approaches often suffer from degraded photometric quality. To address these limitations, we propose ReconDrive, a feed-forward framework that leverages and extends the 3D foundation model VGGT for rapid, high-fidelity 4DGS generation. Our architecture introduces two core adaptations to tailor the foundation model to dynamic driving scenes: (1) Hybrid Gaussian Prediction Heads, which decouple the regression of spatial coordinates and appearance attributes to overcome the photometric deficiencies inherent in generalized foundation features; and (2) a Static-Dynamic 4D Composition strategy that explicitly captures temporal motion via velocity modeling to represent complex dynamic environments. Benchmarked on nuScenes, ReconDrive significantly outperforms existing feed-forward baselines in reconstruction, novel-view synthesis, and 3D perception. It achieves performance competitive with per-scene optimization while being orders of magnitude faster, providing a scalable and practical solution for realistic driving simulation.

  </details>


- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081)**  
  *Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu*  
  `2026-03-05` · `cs.CV` · [abs](https://arxiv.org/abs/2603.05081) · [pdf](https://arxiv.org/pdf/2603.05081.pdf)
  > 💡 针对4D数据集匮乏导致质量受限，提出正交时空分布转移机制，利用STD-4D扩散与ST-HexPlane，实现高质量时空一致4D生成。

  <details><summary>Abstract</summary>

  In the AIGC era, generating high-quality 4D content has garnered increasing research attention. Unfortunately, current 4D synthesis research is severely constrained by the lack of large-scale 4D datasets, preventing models from adequately learning the critical spatial-temporal features necessary for high-quality 4D generation, thus hindering progress in this domain. To combat this, we propose a novel framework that transfers rich spatial priors from existing 3D diffusion models and temporal priors from video diffusion models to enhance 4D synthesis. We develop a spatial-temporal-disentangled 4D (STD-4D) Diffusion model, which synthesizes 4D-aware videos through disentangled spatial and temporal latents. To facilitate the best feature transfer, we design a novel Orthogonal Spatial-temporal Distributional Transfer (Orster) mechanism, where the spatiotemporal feature distributions are carefully modeled and injected into the STD-4D Diffusion. Furthermore, during the 4D construction, we devise a spatial-temporal-aware HexPlane (ST-HexPlane) to integrate the transferred spatiotemporal features, thereby improving 4D deformation and 4D Gaussian feature modeling. Experiments demonstrate that our method significantly outperforms existing approaches, achieving superior spatial-temporal consistency and higher-quality 4D synthesis.

  </details>


- **[Decoupling Motion and Geometry in 4D Gaussian Splatting](https://arxiv.org/abs/2603.00952)**  
  *Yi Zhang, Yulei Kang, Jiangxin Sun, Beihao Xia, Jisheng Dang, Jian-Fang Hu*  
  `2026-03-01` · `cs.CV` · [abs](https://arxiv.org/abs/2603.00952) · [pdf](https://arxiv.org/pdf/2603.00952.pdf)
  > 💡 针对4DGS中运动与几何耦合限制动态表达的问题，提出基于速度的解耦框架VeGaS，引入伽利略剪切矩阵和几何变形网络，实现高保真动态场景重建。

  <details><summary>Abstract</summary>

  High-fidelity reconstruction of dynamic scenes is an important yet challenging problem. While recent 4D Gaussian Splatting (4DGS) has demonstrated the ability to model temporal dynamics, it couples Gaussian motion and geometric attributes within a single covariance formulation, which limits its expressiveness for complex motions and often leads to visual artifacts. To address this, we propose VeGaS, a novel velocity-based 4D Gaussian Splatting framework that decouples Gaussian motion and geometry. Specifically, we introduce a Galilean shearing matrix that explicitly incorporates time-varying velocity to flexibly model complex non-linear motions, while strictly isolating the effects of Gaussian motion from the geometry-related conditional Gaussian covariance. Furthermore, a Geometric Deformation Network is introduced to refine Gaussian shapes and orientations using spatio-temporal context and velocity cues, enhancing temporal geometric modeling. Extensive experiments on public datasets demonstrate that VeGaS achieves state-of-the-art performance.

  </details>


- **[PackUV: Packed Gaussian UV Maps for 4D Volumetric Video](https://arxiv.org/abs/2602.23040)**  
  *Aashish Rai, Angela Xing, Anushka Agarwal, Xiaoyan Cong, Zekun Li, Tao Lu, Aayush Prakash, Srinath Sridhar*  
  `2026-02-26` · `cs.CV` · [abs](https://arxiv.org/abs/2602.23040) · [pdf](https://arxiv.org/pdf/2602.23040.pdf)
  > 💡 将高斯点云属性编码为多尺度UV图集，实现与标准视频编码兼容的4D体视频，解决长序列大运动下的时空不一致问题。

  <details><summary>Abstract</summary>

  Volumetric videos offer immersive 4D experiences, but remain difficult to reconstruct, store, and stream at scale. Existing Gaussian Splatting based methods achieve high-quality reconstruction but break down on long sequences, temporal inconsistency, and fail under large motions and disocclusions. Moreover, their outputs are typically incompatible with conventional video coding pipelines, preventing practical applications. We introduce PackUV, a novel 4D Gaussian representation that maps all Gaussian attributes into a sequence of structured, multi-scale UV atlas, enabling compact, image-native storage. To fit this representation from multi-view videos, we propose PackUV-GS, a temporally consistent fitting method that directly optimizes Gaussian parameters in the UV domain. A flow-guided Gaussian labeling and video keyframing module identifies dynamic Gaussians, stabilizes static regions, and preserves temporal coherence even under large motions and disocclusions. The resulting UV atlas format is the first unified volumetric video representation compatible with standard video codecs (e.g., FFV1) without losing quality, enabling efficient streaming within existing multimedia infrastructure. To evaluate long-duration volumetric capture, we present PackUV-2B, the largest multi-view video dataset to date, featuring more than 50 synchronized cameras, substantial motion, and frequent disocclusions across 100 sequences and 2B (billion) frames. Extensive experiments demonstrate that our method surpasses existing baselines in rendering fidelity while scaling to sequences up to 30 minutes with consistent quality.

  </details>


- **[AeroDGS: Physically Consistent Dynamic Gaussian Splatting for Single-Sequence Aerial 4D Reconstruction](https://arxiv.org/abs/2602.22376)**  
  *Hanyang Liu, Rongjun Qin*  
  `2026-02-25` · `cs.CV` · [abs](https://arxiv.org/abs/2602.22376) · [pdf](https://arxiv.org/pdf/2602.22376.pdf)
  > 💡 提出AeroDGS，以单目几何提升和物理引导优化解决航拍动态重建的深度模糊，实现高保真四维重建。

  <details><summary>Abstract</summary>

  Recent advances in 4D scene reconstruction have significantly improved dynamic modeling across various domains. However, existing approaches remain limited under aerial conditions with single-view capture, wide spatial range, and dynamic objects of limited spatial footprint and large motion disparity. These challenges cause severe depth ambiguity and unstable motion estimation, making monocular aerial reconstruction inherently ill-posed. To this end, we present AeroDGS, a physics-guided 4D Gaussian splatting framework for monocular UAV videos. AeroDGS introduces a Monocular Geometry Lifting module that reconstructs reliable static and dynamic geometry from a single aerial sequence, providing a robust basis for dynamic estimation. To further resolve monocular ambiguity, we propose a Physics-Guided Optimization module that incorporates differentiable ground-support, upright-stability, and trajectory-smoothness priors, transforming ambiguous image cues into physically consistent motion. The framework jointly refines static backgrounds and dynamic entities with stable geometry and coherent temporal evolution. We additionally build a real-world UAV dataset that spans various altitudes and motion conditions to evaluate dynamic aerial reconstruction. Experiments on synthetic and real UAV scenes demonstrate that AeroDGS outperforms state-of-the-art methods, achieving superior reconstruction fidelity in dynamic aerial environments.

  </details>


- **[Space-Time Forecasting of Dynamic Scenes with Motion-aware Gaussian Grouping](https://arxiv.org/abs/2602.21668)**  
  *Junmyeong Lee, Hoseung Choi, Minsu Cho*  
  `2026-02-25` · `cs.CV` · [abs](https://arxiv.org/abs/2602.21668) · [pdf](https://arxiv.org/pdf/2602.21668.pdf)
  > 💡 MoGaF利用运动感知高斯分组和分组优化，基于4DGS实现长期动态场景预测，提升运动一致性和稳定性。

  <details><summary>Abstract</summary>

  Forecasting dynamic scenes remains a fundamental challenge in computer vision, as limited observations make it difficult to capture coherent object-level motion and long-term temporal evolution. We present Motion Group-aware Gaussian Forecasting (MoGaF), a framework for long-term scene extrapolation built upon the 4D Gaussian Splatting representation. MoGaF introduces motion-aware Gaussian grouping and group-wise optimization to enforce physically consistent motion across both rigid and non-rigid regions, yielding spatially coherent dynamic representations. Leveraging this structured space-time representation, a lightweight forecasting module predicts future motion, enabling realistic and temporally stable scene evolution. Experiments on synthetic and real-world datasets demonstrate that MoGaF consistently outperforms existing baselines in rendering quality, motion plausibility, and long-term forecasting stability. Our project page is available at https://slime0519.github.io/mogaf

  </details>


- **[RU4D-SLAM: Reweighting Uncertainty in Gaussian Splatting SLAM for 4D Scene Reconstruction](https://arxiv.org/abs/2602.20807)**  
  *Yangfan Zhao, Hanwei Zhang, Ke Huang, Qiufeng Wang, Zhenzhou Shao, Dengyu Wu*  
  `2026-02-24` · `cs.CV` · [abs](https://arxiv.org/abs/2602.20807) · [pdf](https://arxiv.org/pdf/2602.20807.pdf)
  > 💡 针对动态环境下的SLAM与4D重建困难，提出不确定性重加权4D高斯溅射框架，引入运动模糊渲染与语义引导重加权，显著提升轨迹精度与场景重建质量。

  <details><summary>Abstract</summary>

  Combining 3D Gaussian splatting with Simultaneous Localization and Mapping (SLAM) has gained popularity as it enables continuous 3D environment reconstruction during motion. However, existing methods struggle in dynamic environments, particularly moving objects complicate 3D reconstruction and, in turn, hinder reliable tracking. The emergence of 4D reconstruction, especially 4D Gaussian splatting, offers a promising direction for addressing these challenges, yet its potential for 4D-aware SLAM remains largely underexplored. Along this direction, we propose a robust and efficient framework, namely Reweighting Uncertainty in Gaussian Splatting SLAM (RU4D-SLAM) for 4D scene reconstruction, that introduces temporal factors into spatial 3D representation while incorporating uncertainty-aware perception of scene changes, blurred image synthesis, and dynamic scene reconstruction. We enhance dynamic scene representation by integrating motion blur rendering, and improve uncertainty-aware tracking by extending per-pixel uncertainty modeling, which is originally designed for static scenarios, to handle blurred images. Furthermore, we propose a semantic-guided reweighting mechanism for per-pixel uncertainty estimation in dynamic scenes, and introduce a learnable opacity weight to support adaptive 4D mapping. Extensive experiments on standard benchmarks demonstrate that our method substantially outperforms state-of-the-art approaches in both trajectory accuracy and 4D scene reconstruction, particularly in dynamic environments with moving objects and low-quality inputs. Code available: https://ru4d-slam.github.io

  </details>


- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181)**  
  *Yunxiao Zhang, William Stone, Suryansh Kumar*  
  `2026-02-16` · `cs.CV` · [abs](https://arxiv.org/abs/2602.15181) · [pdf](https://arxiv.org/pdf/2602.15181.pdf)
  > 💡 针对动态场景快速运动及多物体不连贯问题，采用神经体素渲染和刚性变换建模，实现时间存档与回顾性渲染。

  <details><summary>Abstract</summary>

  Camera virtualization -- an emerging solution to novel view synthesis -- holds transformative potential for visual entertainment, live performances, and sports broadcasting by enabling the generation of photorealistic images from novel viewpoints using images from a limited set of calibrated multiple static physical cameras. Despite recent advances, achieving spatially and temporally coherent and photorealistic rendering of dynamic scenes with efficient time-archival capabilities, particularly in fast-paced sports and stage performances, remains challenging for existing approaches. Recent methods based on 3D Gaussian Splatting (3DGS) for dynamic scenes could offer real-time view-synthesis results. Yet, they are hindered by their dependence on accurate 3D point clouds from the structure-from-motion method and their inability to handle large, non-rigid, rapid motions of different subjects (e.g., flips, jumps, articulations, sudden player-to-player transitions). Moreover, independent motions of multiple subjects can break the Gaussian-tracking assumptions commonly used in 4DGS, ST-GS, and other dynamic splatting variants. This paper advocates reconsidering a neural volume rendering formulation for camera virtualization and efficient time-archival capabilities, making it useful for sports broadcasting and related applications. By modeling a dynamic scene as rigid transformations across multiple synchronized camera views at a given time, our method performs neural representation learning, providing enhanced visual rendering quality at test time. A key contribution of our approach is its support for time-archival, i.e., users can revisit any past temporal instance of a dynamic scene and can perform novel view synthesis, enabling retrospective rendering for replay, analysis, and archival of live events, a functionality absent in existing neural rendering approaches and novel view synthesis...

  </details>


- **[Faster-GS: Analyzing and Improving Gaussian Splatting Optimization](https://arxiv.org/abs/2602.09999)**  
  *Florian Hahlbohm, Linus Franke, Martin Eisemann, Marcus Magnor*  
  `2026-02-10` · `cs.CV` · [abs](https://arxiv.org/abs/2602.09999) · [pdf](https://arxiv.org/pdf/2602.09999.pdf)
  > 💡 通过整合并改进数值稳定性等优化，实现5倍训练加速且保持质量，并扩展到4DGS。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have focused on accelerating optimization while preserving reconstruction quality. However, many proposed methods entangle implementation-level improvements with fundamental algorithmic modifications or trade performance for fidelity, leading to a fragmented research landscape that complicates fair comparison. In this work, we consolidate and evaluate the most effective and broadly applicable strategies from prior 3DGS research and augment them with several novel optimizations. We further investigate underexplored aspects of the framework, including numerical stability, Gaussian truncation, and gradient approximation. The resulting system, Faster-GS, provides a rigorously optimized algorithm that we evaluate across a comprehensive suite of benchmarks. Our experiments demonstrate that Faster-GS achieves up to 5$\times$ faster training while maintaining visual quality, establishing a new cost-effective and resource efficient baseline for 3DGS optimization. Furthermore, we demonstrate that optimizations can be applied to 4D Gaussian reconstruction, leading to efficient non-rigid scene optimization.

  </details>


- **[Grow with the Flow: 4D Reconstruction of Growing Plants with Gaussian Flow Fields](https://arxiv.org/abs/2602.08958)**  
  *Weihan Luo, Lily Goli, Sherwin Bahmani, Felix Taubner, Andrea Tagliasacchi, David B. Lindell*  
  `2026-02-09` · `cs.CV` · [abs](https://arxiv.org/abs/2602.08958) · [pdf](https://arxiv.org/pdf/2602.08958.pdf)
  > 💡 针对植物生长中几何持续变化导致时间不一致问题，提出GrowFlow用3D高斯与神经ODE建模连续流场，实现高质量渲染与时序连贯重建。

  <details><summary>Abstract</summary>

  Modeling the time-varying 3D appearance of plants during growth poses unique challenges: unlike most dynamic scenes, plants continuously generate new geometry as they expand, branch, and differentiate. Existing dynamic scene representations are ill-suited to this setting: deformation fields provide insufficient constraints to yield physically plausible scene dynamics, and 4D Gaussian splatting represents the same physical structures with different Gaussian primitives at different times, breaking temporal consistency. We introduce GrowFlow, a dynamic representation that couples 3D Gaussian primitives with a neural ordinary differential equation to model plant growth as a continuous flow field over geometric parameters (position, scale, and orientation). Our representation enables consistent appearance rendering and models nonlinear, continuous-time growth dynamics with full temporal correspondences for every primitive. To initialize a sufficient set of Gaussian primitives, we first reconstruct the mature plant and then learn a reverse-growth process, effectively simulating the plant's developmental history in reverse. GrowFlow achieves superior image quality and geometric coherence compared to prior methods on a new, multi-view timelapse dataset of plant growth, and provides the first temporally coherent representation for appearance modeling of growing 3D structures.

  </details>


- **[TIBR4D: Tracing-Guided Iterative Boundary Refinement for Efficient 4D Gaussian Segmentation](https://arxiv.org/abs/2602.08540)**  
  *He Wu, Xia Yan, Yanghui Xu, Liegang Xia, Jiazhou Chen*  
  `2026-02-09` · `cs.CV` · [abs](https://arxiv.org/abs/2602.08540) · [pdf](https://arxiv.org/pdf/2602.08540.pdf)
  > 💡 提出无学习4D高斯分割框架，通过迭代实例追踪和渲染范围控制，高效处理运动遮挡并细化边界。

  <details><summary>Abstract</summary>

  Object-level segmentation in dynamic 4D Gaussian scenes remains challenging due to complex motion, occlusions, and ambiguous boundaries. In this paper, we present an efficient learning-free 4D Gaussian segmentation framework that lifts video segmentation masks to 4D spaces, whose core is a two-stage iterative boundary refinement, TIBR4D. The first stage is an Iterative Gaussian Instance Tracing (IGIT) at the temporal segment level. It progressively refines Gaussian-to-instance probabilities through iterative tracing, and extracts corresponding Gaussian point clouds that better handle occlusions and preserve completeness of object structures compared to existing one-shot threshold-based methods. The second stage is a frame-wise Gaussian Rendering Range Control (RCC) via suppressing highly uncertain Gaussians near object boundaries while retaining their core contributions for more accurate boundaries. Furthermore, a temporal segmentation merging strategy is proposed for IGIT to balance identity consistency and dynamic awareness. Longer segments enforce stronger multi-frame constraints for stable identities, while shorter segments allow identity changes to be captured promptly. Experiments on HyperNeRF and Neu3D demonstrate that our method produces accurate object Gaussian point clouds with clearer boundaries and higher efficiency compared to SOTA methods.

  </details>


- **[Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering](https://arxiv.org/abs/2602.06343)**  
  *Weiquan Wang, Feifei Shao, Lin Li, Zhen Wang, Jun Xiao, Long Chen*  
  `2026-02-06` · `cs.CV` · [abs](https://arxiv.org/abs/2602.06343) · [pdf](https://arxiv.org/pdf/2602.06343.pdf)
  > 💡 单目视频遮挡下人体渲染退化，提出U-4DGS用概率形变网络渲染不确定性图调节梯度，并施加置信度正则化，达SOTA保真度和鲁棒性。

  <details><summary>Abstract</summary>

  High-fidelity rendering of dynamic humans from monocular videos typically degrades catastrophically under occlusions. Existing solutions incorporate external priors-either hallucinating missing content via generative models, which induces severe temporal flickering, or imposing rigid geometric heuristics that fail to capture diverse appearances. To this end, we reformulate the task as a Maximum A Posteriori estimation problem under heteroscedastic observation noise. In this paper, we propose U-4DGS, a framework integrating a Probabilistic Deformation Network and a Joint Rasterization pipeline. This architecture renders pixel-aligned uncertainty maps that act as an adaptive gradient modulator, automatically attenuating artifacts from unreliable observations. Furthermore, to prevent geometric drift in regions lacking reliable visual cues, we enforce Confidence-Aware Regularizations, which leverage the learned uncertainty to selectively propagate spatial-temporal validity. Extensive experiments on the ZJU-MoCap and OcMotion datasets demonstrate that U-4DGS achieves state-of-the-art rendering fidelity and robustness.

  </details>


- **[ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors](https://arxiv.org/abs/2602.05572)**  
  *Zhenxiao Liang, Ning Zhang, Youbao Tang, Ruei-Sung Lin, Qixing Huang, Peng Chang, Jing Xiao*  
  `2026-02-05` · `cs.CV` · [abs](https://arxiv.org/abs/2602.05572) · [pdf](https://arxiv.org/pdf/2602.05572.pdf)
  > 💡 利用2D视觉先验和无模板两步法（粗几何+神经变形细化），实现单目视频中高保真且稳健的4D人体重建。

  <details><summary>Abstract</summary>

  We introduce ShapeGaussian, a high-fidelity, template-free method for 4D human reconstruction from casual monocular videos. Generic reconstruction methods lacking robust vision priors, such as 4DGS, struggle to capture high-deformation human motion without multi-view cues. While template-based approaches, primarily relying on SMPL, such as HUGS, can produce photorealistic results, they are highly susceptible to errors in human pose estimation, often leading to unrealistic artifacts. In contrast, ShapeGaussian effectively integrates template-free vision priors to achieve both high-fidelity and robust scene reconstructions. Our method follows a two-step pipeline: first, we learn a coarse, deformable geometry using pretrained models that estimate data-driven priors, providing a foundation for reconstruction. Then, we refine this geometry using a neural deformation model to capture fine-grained dynamic details. By leveraging 2D vision priors, we mitigate artifacts from erroneous pose estimation in template-based methods and employ multiple reference frames to resolve the invisibility issue of 2D keypoints in a template-free manner. Extensive experiments demonstrate that ShapeGaussian surpasses template-based methods in reconstruction accuracy, achieving superior visual quality and robustness across diverse human motions in casual monocular videos.

  </details>


- **[SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation](https://arxiv.org/abs/2602.02989)**  
  *Zhanfeng Liao, Jiajun Zhang, Hanzhang Tu, Zhixi Wang, Yunqi Gao, Hongwen Zhang, Yebin Liu*  
  `2026-02-03` · `cs.CV` · [abs](https://arxiv.org/abs/2602.02989) · [pdf](https://arxiv.org/pdf/2602.02989.pdf)
  > 💡 提出可学习寿命参数调制时间可见性和运动，解耦运动与时长，实现动态场景清晰稳定渲染，达SOTA 4

  <details><summary>Abstract</summary>

  Novel view synthesis of dynamic scenes is fundamental to achieving photorealistic 4D reconstruction and immersive visual experiences. Recent progress in Gaussian-based representations has significantly improved real-time rendering quality, yet existing methods still struggle to maintain a balance between long-term static and short-term dynamic regions in both representation and optimization. To address this, we present SharpTimeGS, a lifespan-aware 4D Gaussian framework that achieves temporally adaptive modeling of both static and dynamic regions under a unified representation. Specifically, we introduce a learnable lifespan parameter that reformulates temporal visibility from a Gaussian-shaped decay into a flat-top profile, allowing primitives to remain consistently active over their intended duration and avoiding redundant densification. In addition, the learned lifespan modulates each primitives' motion, reducing drift in long-lived static points while retaining unrestricted motion for short-lived dynamic ones. This effectively decouples motion magnitude from temporal duration, improving long-term stability without compromising dynamic fidelity. Moreover, we design a lifespan-velocity-aware densification strategy that mitigates optimization imbalance between static and dynamic regions by allocating more capacity to regions with pronounced motion while keeping static areas compact and stable. Extensive experiments on multiple benchmarks demonstrate that our method achieves state-of-the-art performance while supporting real-time rendering up to 4K resolution at 100 FPS on one RTX 4090.

  </details>


- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148)**  
  *Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu*  
  `2026-01-29` · `cs.CV` · [abs](https://arxiv.org/abs/2602.00148) · [pdf](https://arxiv.org/pdf/2602.00148.pdf)
  > 💡 针对物理动态建模成本高问题，提出神经高斯力场端到端框架，整合感知与物理建模实现快速4D视频生成，速度提升两个数量级。

  <details><summary>Abstract</summary>

  Predicting physical dynamics from raw visual data remains a major challenge in AI. While recent video generation models have achieved impressive visual quality, they still cannot consistently generate physically plausible videos due to a lack of modeling of physical laws. Recent approaches combining 3D Gaussian splatting and physics engines can produce physically plausible videos, but are hindered by high computational costs in both reconstruction and simulation, and often lack robustness in complex real-world scenarios. To address these issues, we introduce Neural Gaussian Force Field (NGFF), an end-to-end neural framework that integrates 3D Gaussian perception with physics-based dynamic modeling to generate interactive, physically realistic 4D videos from multi-view RGB inputs, achieving two orders of magnitude faster than prior Gaussian simulators. To support training, we also present GSCollision, a 4D Gaussian dataset featuring diverse materials, multi-object interactions, and complex scenes, totaling over 640k rendered physical videos (~4 TB). Evaluations on synthetic and real 3D scenarios show NGFF's strong generalization and robustness in physical reasoning, advancing video prediction towards physics-grounded world models.

  </details>


- **[Graphical X Splatting (GraphiXS): A Graphical Model for 4D Gaussian Splatting under Uncertainty](https://arxiv.org/abs/2601.19843)**  
  *Doğa Yılmaz, Jialin Zhu, Deshan Gong, He Wang*  
  `2026-01-27` · `cs.GR` · [abs](https://arxiv.org/abs/2601.19843) · [pdf](https://arxiv.org/pdf/2601.19843.pdf)
  > 💡 GraphiXS 提出概率框架，系统性建模 4DGS 中多种数据不确定性，支持多种基元，性能优于现有方法。

  <details><summary>Abstract</summary>

  We propose a new framework to systematically incorporate data uncertainty in Gaussian Splatting. Being the new paradigm of neural rendering, Gaussian Splatting has been investigated in many applications, with the main effort in extending its representation, improving its optimization process, and accelerating its speed. However, one orthogonal, much needed, but under-explored area is data uncertainty. In standard 4D Gaussian Splatting, data uncertainty can manifest as view sparsity, missing frames, camera asynchronization, etc. So far, there has been little research to holistically incorporating various types of data uncertainty under a single framework. To this end, we propose Graphical X Splatting, or GraphiXS, a new probabilistic framework that considers multiple types of data uncertainty, aiming for a fundamental augmentation of the current 4D Gaussian Splatting paradigm into a probabilistic setting. GraphiXS is general and can be instantiated with a range of primitives, e.g. Gaussians, Student's-t. Furthermore, GraphiXS can be used to `upgrade' existing methods to accommodate data uncertainty. Through exhaustive evaluation and comparison, we demonstrate that GraphiXS can systematically model various uncertainties in data, outperform existing methods in many settings where data are missing or polluted in space and time, and therefore is a major generalization of the current 4D Gaussian Splatting research.

  </details>


- **[Uncertainty-Aware 3D Emotional Talking Face Synthesis with Emotion Prior Distillation](https://arxiv.org/abs/2601.19112)**  
  *Nanhan Shen, Zhilei Liu*  
  `2026-01-27` · `cs.AI` · [abs](https://arxiv.org/abs/2601.19112) · [pdf](https://arxiv.org/pdf/2601.19112.pdf)
  > 💡 针对情感对齐差和融合忽略不确定性问题，提出UA-3DTalk采用情感先验

  <details><summary>Abstract</summary>

  Emotional Talking Face synthesis is pivotal in multimedia and signal processing, yet existing 3D methods suffer from two critical challenges: poor audio-vision emotion alignment, manifested as difficult audio emotion extraction and inadequate control over emotional micro-expressions; and a one-size-fits-all multi-view fusion strategy that overlooks uncertainty and feature quality differences, undermining rendering quality. We propose UA-3DTalk, Uncertainty-Aware 3D Emotional Talking Face Synthesis with emotion prior distillation, which has three core modules: the Prior Extraction module disentangles audio into content-synchronized features for alignment and person-specific complementary features for individualization; the Emotion Distillation module introduces a multi-modal attention-weighted fusion mechanism and 4D Gaussian encoding with multi-resolution code-books, enabling fine-grained audio emotion extraction and precise control of emotional micro-expressions; the Uncertainty-based Deformation deploys uncertainty blocks to estimate view-specific aleatoric (input noise) and epistemic (model parameters) uncertainty, realizing adaptive multi-view fusion and incorporating a multi-head decoder for Gaussian primitive optimization to mitigate the limitations of uniform-weight fusion. Extensive experiments on regular and emotional datasets show UA-3DTalk outperforms state-of-the-art methods like DEGSTalk and EDTalk by 5.2% in E-FID for emotion alignment, 3.1% in SyncC for lip synchronization, and 0.015 in LPIPS for rendering quality. Project page: https://mrask999.github.io/UA-3DTalk

  </details>


- **[DriveExplorer: Images-Only Decoupled 4D Reconstruction with Progressive Restoration for Driving View Extrapolation](https://arxiv.org/abs/2512.23983)**  
  *Yuang Jia, Jinlong Wang, Jiayi Zhao, Chunlam Li, Shunzhou Wang, Wei Gao*  
  `2025-12-30` · `cs.CV` · [abs](https://arxiv.org/abs/2512.23983) · [pdf](https://arxiv.org/pdf/2512.23983.pdf)
  > 💡 仅用图像和相机位姿，通过静态与动态点云融合及可变形4D高斯重建，结合扩散模型逐步细化实现高质量驾驶视图外推。

  <details><summary>Abstract</summary>

  This paper presents an effective solution for view extrapolation in autonomous driving scenarios. Recent approaches focus on generating shifted novel view images from given viewpoints using diffusion models. However, these methods heavily rely on priors such as LiDAR point clouds, 3D bounding boxes, and lane annotations, which demand expensive sensors or labor-intensive labeling, limiting applicability in real-world deployment. In this work, with only images and optional camera poses, we first estimate a global static point cloud and per-frame dynamic point clouds, fusing them into a unified representation. We then employ a deformable 4D Gaussian framework to reconstruct the scene. The initially trained 4D Gaussian model renders degraded and pseudo-images to train a video diffusion model. Subsequently, progressively shifted Gaussian renderings are iteratively refined by the diffusion model,and the enhanced results are incorporated back as training data for 4DGS. This process continues until extrapolation reaches the target viewpoints. Compared with baselines, our method produces higher-quality images at novel extrapolated viewpoints.

  </details>


- **[AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences](https://arxiv.org/abs/2512.20943)**  
  *Zhe Wang, Jinghang Li, Yifei Zhu*  
  `2025-12-24` · `cs.GR` · [abs](https://arxiv.org/abs/2512.20943) · [pdf](https://arxiv.org/pdf/2512.20943.pdf)
  > 💡 针对4DGS长序列质量退化与高带宽问题，AirGS采用多通道2D转换、关键帧识别及自适应剪枝，降低质量偏差20%并提速6倍。

  <details><summary>Abstract</summary>

  Free-viewpoint video (FVV) enables immersive viewing experiences by allowing users to view scenes from arbitrary perspectives. As a prominent reconstruction technique for FVV generation, 4D Gaussian Splatting (4DGS) models dynamic scenes with time-varying 3D Gaussian ellipsoids and achieves high-quality rendering via fast rasterization. However, existing 4DGS approaches suffer from quality degradation over long sequences and impose substantial bandwidth and storage overhead, limiting their applicability in real-time and wide-scale deployments. Therefore, we present AirGS, a streaming-optimized 4DGS framework that rearchitects the training and delivery pipeline to enable high-quality, low-latency FVV experiences. AirGS converts Gaussian video streams into multi-channel 2D formats and intelligently identifies keyframes to enhance frame reconstruction quality. It further combines temporal coherence with inflation loss to reduce training time and representation size. To support communication-efficient transmission, AirGS models 4DGS delivery as an integer linear programming problem and design a lightweight pruning level selection algorithm to adaptively prune the Gaussian updates to be transmitted, balancing reconstruction quality and bandwidth consumption. Extensive experiments demonstrate that AirGS reduces quality deviation in PSNR by more than 20% when scene changes, maintains frame-level PSNR consistently above 30, accelerates training by 6 times, reduces per-frame transmission size by nearly 50% compared to the SOTA 4DGS approaches.

  </details>


- **[4D Gaussian Splatting as a Learned Dynamical System](https://arxiv.org/abs/2512.19648)**  
  *Arnold Caleb Asiimwe, Carl Vondrick*  
  `2025-12-22` · `cs.CV` · [abs](https://arxiv.org/abs/2512.19648) · [pdf](https://arxiv.org/pdf/2512.19648.pdf)
  > 💡 将4D高斯溅射视为学习动力学系统，通过神经动力学场建模运动，实现样本高效学习与时间外推。

  <details><summary>Abstract</summary>

  We reinterpret 4D Gaussian Splatting as a continuous-time dynamical system, where scene motion arises from integrating a learned neural dynamical field rather than applying per-frame deformations. This formulation, which we call EvoGS, treats the Gaussian representation as an evolving physical system whose state evolves continuously under a learned motion law. This unlocks capabilities absent in deformation-based approaches:(1) sample-efficient learning from sparse temporal supervision by modeling the underlying motion law; (2) temporal extrapolation enabling forward and backward prediction beyond observed time ranges; and (3) compositional dynamics that allow localized dynamics injection for controllable scene synthesis. Experiments on dynamic scene benchmarks show that EvoGS achieves better motion coherence and temporal consistency compared to deformation-field baselines while maintaining real-time rendering

  </details>


- **[D$^2$GSLAM: 4D Dynamic Gaussian Splatting SLAM](https://arxiv.org/abs/2512.09411)**  
  *Siting Zhu, Yuxiang Huang, Wenhua Wu, Chaokang Jiang, Yongbo Chen, I-Ming Chen, Hesheng Wang*  
  `2025-12-10` · `cs.RO` · [abs](https://arxiv.org/abs/2512.09411) · [pdf](https://arxiv.org/pdf/2512.09411.pdf)
  > 💡 利用动态静态高斯表示和几何提示分离，实现动态场景下高精度重建与鲁棒跟踪。

  <details><summary>Abstract</summary>

  Recent advances in Dense Simultaneous Localization and Mapping (SLAM) have demonstrated remarkable performance in static environments. However, dense SLAM in dynamic environments remains challenging. Most methods directly remove dynamic objects and focus solely on static scene reconstruction, which ignores the motion information contained in these dynamic objects. In this paper, we present D$^2$GSLAM, a novel dynamic SLAM system utilizing Gaussian representation, which simultaneously performs accurate dynamic reconstruction and robust tracking within dynamic environments. Our system is composed of four key components: (i) We propose a geometric-prompt dynamic separation method to distinguish between static and dynamic elements of the scene. This approach leverages the geometric consistency of Gaussian representation and scene geometry to obtain coarse dynamic regions. The regions then serve as prompts to guide the refinement of the coarse mask for achieving accurate motion mask. (ii) To facilitate accurate and efficient mapping of the dynamic scene, we introduce dynamic-static composite representation that integrates static 3D Gaussians with dynamic 4D Gaussians. This representation allows for modeling the transitions between static and dynamic states of objects in the scene for composite mapping and optimization. (iii) We employ a progressive pose refinement strategy that leverages both the multi-view consistency of static scene geometry and motion information from dynamic objects to achieve accurate camera tracking. (iv) We introduce a motion consistency loss, which leverages the temporal continuity in object motions for accurate dynamic modeling. Our D$^2$GSLAM demonstrates superior performance on dynamic scenes in terms of mapping and tracking accuracy, while also showing capability in accurate dynamic modeling.

  </details>


- **[MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification](https://arxiv.org/abs/2512.09270)**  
  *Sangwoon Kwak, Weeyoung Kwon, Jun Young Jeong, Geonho Kim, Won-Sik Cheong, Jihyong Oh*  
  `2025-12-10` · `cs.CV` · [abs](https://arxiv.org/abs/2512.09270) · [pdf](https://arxiv.org/pdf/2512.09270.pdf)
  > 💡 针对长范围4D动态场景的内存爆炸与闪烁问题，提出锚点中继双向混合与层次稠密化，实现无闪烁高效重建。

  <details><summary>Abstract</summary>

  Recent advances in 4D Gaussian Splatting (4DGS) have extended the high-speed rendering capability of 3D Gaussian Splatting (3DGS) into the temporal domain, enabling real-time rendering of dynamic scenes. However, one of the major remaining challenges lies in modeling long-range motion-contained dynamic videos, where a naive extension of existing methods leads to severe memory explosion, temporal flickering, and failure to handle appearing or disappearing occlusions over time. To address these challenges, we propose a novel 4DGS framework characterized by an Anchor Relay-based Bidirectional Blending (ARBB) mechanism, named MoRel, which enables temporally consistent and memory-efficient modeling of long-range dynamic scenes. Our method progressively constructs locally canonical anchor spaces at key-frame time index and models inter-frame deformations at the anchor level, enhancing temporal coherence. By learning bidirectional deformations between KfA and adaptively blending them through learnable opacity control, our approach mitigates temporal discontinuities and flickering artifacts. We further introduce a Feature-variance-guided Hierarchical Densification (FHD) scheme that effectively densifies KfA's while keeping rendering quality, based on an assigned level of feature-variance. To effectively evaluate our model's capability to handle real-world long-range 4D motion, we newly compose long-range 4D motion-contained dataset, called SelfCap$_{\text{LR}}$. It has larger average dynamic motion magnitude, captured at spatially wider spaces, compared to previous dynamic video datasets. Overall, our MoRel achieves temporally coherent and flicker-free long-range 4D reconstruction while maintaining bounded memory usage, demonstrating both scalability and efficiency in dynamic Gaussian-based representations.

  </details>


- **[Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform](https://arxiv.org/abs/2512.08478)**  
  *Yuning Gong, Yifei Liu, Yifan Zhan, Muyao Niu, Xueying Li, Yuanjun Liao, Jiaming Chen, Yuanyuan Gao, Jiaqi Chen, Minming Chen, Li Zhou, Yuning Zhang, Wei Wang, Xiaoqing Hou, Huaxi Huang, Shixiang Tang, Le Ma, Dingwen Zhang, Xue Yang, Junchi Yan, Yanchi Zhang, Yinqiang Zheng, Xiao Sun, Zhihang Zhong*  
  `2025-12-09` · `cs.CV` · [abs](https://arxiv.org/abs/2512.08478) · [pdf](https://arxiv.org/pdf/2512.08478.pdf)
  > 💡 提出WebGPU驱动的Gaussian Splatting平台Visionary，实现高效神经渲染和生成后处理，降低3DGS部署门槛。

  <details><summary>Abstract</summary>

  Neural rendering, particularly 3D Gaussian Splatting (3DGS), has evolved rapidly and become a key component for building world models. However, existing viewer solutions remain fragmented, heavy, or constrained by legacy pipelines, resulting in high deployment friction and limited support for dynamic content and generative models. In this work, we present Visionary, an open, web-native platform for real-time various Gaussian Splatting and meshes rendering. Built on an efficient WebGPU renderer with per-frame ONNX inference, Visionary enables dynamic neural processing while maintaining a lightweight, "click-to-run" browser experience. It introduces a standardized Gaussian Generator contract, which not only supports standard 3DGS rendering but also allows plug-and-play algorithms to generate or update Gaussians each frame. Such inference also enables us to apply feedforward generative post-processing. The platform further offers a plug in three.js library with a concise TypeScript API for seamless integration into existing web applications. Experiments show that, under identical 3DGS assets, Visionary achieves superior rendering efficiency compared to current Web viewers due to GPU-based primitive sorting. It already supports multiple variants, including MLP-based 3DGS, 4DGS, neural avatars, and style transformation or enhancement networks. By unifying inference and rendering directly in the browser, Visionary significantly lowers the barrier to reproduction, comparison, and deployment of 3DGS-family methods, serving as a unified World Model Carrier for both reconstructive and generative paradigms.

  </details>


- **[Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation](https://arxiv.org/abs/2512.06158)**  
  *Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Victor Chen, Mei Chen*  
  `2025-12-05` · `cs.CV` · [abs](https://arxiv.org/abs/2512.06158) · [pdf](https://arxiv.org/pdf/2512.06158.pdf)
  > 💡 提出Track4DGen，将跟踪运动先验注入扩散模型和混合4D高斯泼溅，解决稀疏输入4D生成的视图不一致与时序漂移。

  <details><summary>Abstract</summary>

  Generating dynamic 4D objects from sparse inputs is difficult because it demands joint preservation of appearance and motion coherence across views and time while suppressing artifacts and temporal drift. We hypothesize that the view discrepancy arises from supervision limited to pixel- or latent-space video-diffusion losses, which lack explicitly temporally aware, feature-level tracking guidance. We present \emph{Track4DGen}, a two-stage framework that couples a multi-view video diffusion model with a foundation point tracker and a hybrid 4D Gaussian Splatting (4D-GS) reconstructor. The central idea is to explicitly inject tracker-derived motion priors into intermediate feature representations for both multi-view video generation and 4D-GS. In Stage One, we enforce dense, feature-level point correspondences inside the diffusion generator, producing temporally consistent features that curb appearance drift and enhance cross-view coherence. In Stage Two, we reconstruct a dynamic 4D-GS using a hybrid motion encoding that concatenates co-located diffusion features (carrying Stage-One tracking priors) with Hex-plane features, and augment them with 4D Spherical Harmonics for higher-fidelity dynamics modeling. \emph{Track4DGen} surpasses baselines on both multi-view video generation and 4D generation benchmarks, yielding temporally stable, text-editable 4D assets. Lastly, we curate \emph{Sketchfab28}, a high-quality dataset for benchmarking object-centric 4D generation and fostering future research.

  </details>


- **[TED-4DGS: Temporally Activated and Embedding-based Deformation for 4DGS Compression](https://arxiv.org/abs/2512.05446)**  
  *Cheng-Yuan Ho, He-Bi Yang, Jui-Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng*  
  `2025-12-05` · `cs.CV` · [abs](https://arxiv.org/abs/2512.05446) · [pdf](https://arxiv.org/pdf/2512.05446.pdf)
  > 💡 针对动态3DGS压缩，提出时间激活与嵌入变形方法，结合隐式神经超先验和自回归模型，实现率失真优化SOTA。

  <details><summary>Abstract</summary>

  Building on the success of 3D Gaussian Splatting (3DGS) in static 3D scene representation, its extension to dynamic scenes, commonly referred to as 4DGS or dynamic 3DGS, has attracted increasing attention. However, designing more compact and efficient deformation schemes together with rate-distortion-optimized compression strategies for dynamic 3DGS representations remains an underexplored area. Prior methods either rely on space-time 4DGS with overspecified, short-lived Gaussian primitives or on canonical 3DGS with deformation that lacks explicit temporal control. To address this, we present TED-4DGS, a temporally activated and embedding-based deformation scheme for rate-distortion-optimized 4DGS compression that unifies the strengths of both families. TED-4DGS is built on a sparse anchor-based 3DGS representation. Each canonical anchor is assigned learnable temporal-activation parameters to specify its appearance and disappearance transitions over time, while a lightweight per-anchor temporal embedding queries a shared deformation bank to produce anchor-specific deformation. For rate-distortion compression, we incorporate an implicit neural representation (INR)-based hyperprior to model anchor attribute distributions, along with a channel-wise autoregressive model to capture intra-anchor correlations. With these novel elements, our scheme achieves state-of-the-art rate-distortion performance on several real-world datasets. To the best of our knowledge, this work represents one of the first attempts to pursue a rate-distortion-optimized compression framework for dynamic 3DGS representations.

  </details>


- **[SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting](https://arxiv.org/abs/2512.04315)**  
  *Yonghan Lee, Tsung-Wei Huang, Shiv Gehlot, Jaehoon Choi, Guan-Ming Su, Dinesh Manocha*  
  `2025-12-03` · `cs.CV` · [abs](https://arxiv.org/abs/2512.04315) · [pdf](https://arxiv.org/pdf/2512.04315.pdf)
  > 💡 利用密集4D轨迹和最优传输实现未同步视频的跨视频对齐与亚帧同步，首个通用多视频4D高斯泼溅方法。

  <details><summary>Abstract</summary>

  Modeling dynamic 3D scenes is challenging due to their high-dimensional nature, which requires aggregating information from multiple views to reconstruct time-evolving 3D geometry and motion. We present a novel multi-video 4D Gaussian Splatting (4DGS) approach designed to handle real-world, unsynchronized video sets. Our approach, SyncTrack4D, directly leverages dense 4D track representation of dynamic scene parts as cues for simultaneous cross-video synchronization and 4DGS reconstruction. We first compute dense per-video 4D feature tracks and cross-video track correspondences by Fused Gromov-Wasserstein optimal transport approach. Next, we perform global frame-level temporal alignment to maximize overlapping motion of matched 4D tracks. Finally, we achieve sub-frame synchronization through our multi-video 4D Gaussian splatting built upon a motion-spline scaffold representation. The final output is a synchronized 4DGS representation with dense, explicit 3D trajectories, and temporal offsets for each video. We evaluate our approach on the Panoptic Studio and SyncNeRF Blender, demonstrating sub-frame synchronization accuracy with an average temporal error below 0.26 frames, and high-fidelity 4D reconstruction reaching 26.3 PSNR scores on the Panoptic Studio dataset. To the best of our knowledge, our work is the first general 4D Gaussian Splatting approach for unsynchronized video sets, without assuming the existence of predefined scene objects or prior models.

  </details>


- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601)**  
  *Haoran Zhou, Gim Hee Lee*  
  `2025-12-03` · `cs.CV` · [abs](https://arxiv.org/abs/2512.03601) · [pdf](https://arxiv.org/pdf/2512.03601.pdf)
  > 💡 融合2D先验到4D高斯泼溅，通过两阶段优化和3D置信图解决动态场景3D不一致，显著提升跟踪、分割和新视图合成精度。

  <details><summary>Abstract</summary>

  Recent advancements in foundation models for 2D vision have substantially improved the analysis of dynamic scenes from monocular videos. However, despite their strong generalization capabilities, these models often lack 3D consistency, a fundamental requirement for understanding scene geometry and motion, thereby causing severe spatial misalignment and temporal flickering in complex 3D environments. In this paper, we present Motion4D, a novel framework that addresses these challenges by integrating 2D priors from foundation models into a unified 4D Gaussian Splatting representation. Our method features a two-part iterative optimization framework: 1) Sequential optimization, which updates motion and semantic fields in consecutive stages to maintain local consistency, and 2) Global optimization, which jointly refines all attributes for long-term coherence. To enhance motion accuracy, we introduce a 3D confidence map that dynamically adjusts the motion priors, and an adaptive resampling process that inserts new Gaussians into under-represented regions based on per-pixel RGB and semantic errors. Furthermore, we enhance semantic coherence through an iterative refinement process that resolves semantic inconsistencies by alternately optimizing the semantic fields and updating prompts of SAM2. Extensive evaluations demonstrate that our Motion4D significantly outperforms both 2D foundation models and existing 3D-based approaches across diverse scene understanding tasks, including point-based tracking, video object segmentation, and novel view synthesis. Our code is available at https://hrzhou2.github.io/motion4d-web/.

  </details>


- **[Dynamic-eDiTor: Training-Free Text-Driven 4D Scene Editing with Multimodal Diffusion Transformer](https://arxiv.org/abs/2512.00677)**  
  *Dong In Lee, Hyungjun Doh, Seunggeun Chi, Runlin Duan, Sangpil Kim, Karthik Ramani*  
  `2025-11-30` · `cs.CV` · [abs](https://arxiv.org/abs/2512.00677) · [pdf](https://arxiv.org/pdf/2512.00677.pdf)
  > 💡 针对4D编辑时空不一致问题，提出基于多模态扩散变压器的无训练框架，通过STGA和CTP实现全局一致编辑。

  <details><summary>Abstract</summary>

  Recent progress in 4D representations, such as Dynamic NeRF and 4D Gaussian Splatting (4DGS), has enabled dynamic 4D scene reconstruction. However, text-driven 4D scene editing remains under-explored due to the challenge of ensuring both multi-view and temporal consistency across space and time during editing. Existing studies rely on 2D diffusion models that edit frames independently, often causing motion distortion, geometric drift, and incomplete editing. We introduce Dynamic-eDiTor, a training-free text-driven 4D editing framework leveraging Multimodal Diffusion Transformer (MM-DiT) and 4DGS. This mechanism consists of Spatio-Temporal Sub-Grid Attention (STGA) for locally consistent cross-view and temporal fusion, and Context Token Propagation (CTP) for global propagation via token inheritance and optical-flow-guided token replacement. Together, these components allow Dynamic-eDiTor to perform seamless, globally consistent multi-view video without additional training and directly optimize pre-trained source 4DGS. Extensive experiments on multi-view video dataset DyNeRF demonstrate that our method achieves superior editing fidelity and both multi-view and temporal consistency prior approaches. Project page for results and code: https://di-lee.github.io/dynamic-eDiTor/

  </details>


- **[Geometry-Consistent 4D Gaussian Splatting for Sparse-Input Dynamic View Synthesis](https://arxiv.org/abs/2511.23044)**  
  *Yiwei Li, Jiannong Cao, Penghui Ruan, Divya Saxena, Songye Zhu, Yinfeng Cao*  
  `2025-11-28` · `cs.CV` · [abs](https://arxiv.org/abs/2511.23044) · [pdf](https://arxiv.org/pdf/2511.23044.pdf)
  > 💡 针对稀疏输入动态视图合成中几何不一致问题，提出动态一致性检查与全局-局部深度正则化，显著提升渲染质量且保持实时性。

  <details><summary>Abstract</summary>

  Gaussian Splatting has been considered as a novel way for view synthesis of dynamic scenes, which shows great potential in AIoT applications such as digital twins. However, recent dynamic Gaussian Splatting methods significantly degrade when only sparse input views are available, limiting their applicability in practice. The issue arises from the incoherent learning of 4D geometry as input views decrease. This paper presents GC-4DGS, a novel framework that infuses geometric consistency into 4D Gaussian Splatting (4DGS), offering real-time and high-quality dynamic scene rendering from sparse input views. While learning-based Multi-View Stereo (MVS) and monocular depth estimators (MDEs) provide geometry priors, directly integrating these with 4DGS yields suboptimal results due to the ill-posed nature of sparse-input 4D geometric optimization. To address these problems, we introduce a dynamic consistency checking strategy to reduce estimation uncertainties of MVS across spacetime. Furthermore, we propose a global-local depth regularization approach to distill spatiotemporal-consistent geometric information from monocular depths, thereby enhancing the coherent geometry and appearance learning within the 4D volume. Extensive experiments on the popular N3DV and Technicolor datasets validate the effectiveness of GC-4DGS in rendering quality without sacrificing efficiency. Notably, our method outperforms RF-DeRF, the latest dynamic radiance field tailored for sparse-input dynamic view synthesis, and the original 4DGS by 2.62dB and 1.58dB in PSNR, respectively, with seamless deployability on resource-constrained IoT edge devices.

  </details>


- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367)**  
  *Yangle Liu, Fengze Li, Kan Liu, Jieming Ma*  
  `2025-11-26` · `cs.CV` · [abs](https://arxiv.org/abs/2511.21367) · [pdf](https://arxiv.org/pdf/2511.21367.pdf)
  > 💡 针对内窥镜场景几何漂移，提出几何引导先验蒸馏与时间嵌入4DGS，联合深度和运动正则化实现时序一致与最优重建。

  <details><summary>Abstract</summary>

  Endoscopic (endo) video exhibits strong view-dependent effects such as specularities, wet reflections, and occlusions. Pure photometric supervision misaligns with geometry and triggers early geometric drift, where erroneous shapes are reinforced during densification and become hard to correct. We ask how to anchor geometry early for 4D Gaussian splatting (4DGS) while maintaining temporal consistency and efficiency in dynamic endoscopic scenes. Thus, we present Endo-G$^{2}$T, a geometry-guided and temporally aware training scheme for time-embedded 4DGS. First, geo-guided prior distillation converts confidence-gated monocular depth into supervision with scale-invariant depth and depth-gradient losses, using a warm-up-to-cap schedule to inject priors softly and avoid early overfitting. Second, a time-embedded Gaussian field represents dynamics in XYZT with a rotor-like rotation parameterization, yielding temporally coherent geometry with lightweight regularization that favors smooth motion and crisp opacity boundaries. Third, keyframe-constrained streaming improves efficiency and long-horizon stability through keyframe-focused optimization under a max-points budget, while non-keyframes advance with lightweight updates. Across EndoNeRF and StereoMIS-P1 datasets, Endo-G$^{2}$T achieves state-of-the-art results among monocular reconstruction baselines.

  </details>


- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367)**  
  *Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao*  
  `2025-11-23` · `cs.CV` · [abs](https://arxiv.org/abs/2511.18367) · [pdf](https://arxiv.org/pdf/2511.18367.pdf)
  > 💡 针对动态场景重建中分辨率变化导致伪影的问题，引入4D尺度自适应滤波与尺度损失，消除高频伪影并减少冗余高斯。

  <details><summary>Abstract</summary>

  Existing dynamic scene reconstruction methods based on Gaussian Splatting enable real-time rendering and generate realistic images. However, adjusting the camera's focal length or the distance between Gaussian primitives and the camera to modify rendering resolution often introduces strong artifacts, stemming from the frequency constraints of 4D Gaussians and Gaussian scale mismatch induced by the 2D dilated filter. To address this, we derive a maximum sampling frequency formulation for 4D Gaussian Splatting and introduce a 4D scale-adaptive filter and scale loss, which flexibly regulates the sampling frequency of 4D Gaussian Splatting. Our approach eliminates high-frequency artifacts under increased rendering frequencies while effectively reducing redundant Gaussians in multi-view video reconstruction. We validate the proposed method through monocular and multi-view video reconstruction experiments.Ours project page: https://4d-alias-free.github.io/4D-Alias-free/

  </details>


- **[Clustered Error Correction with Grouped 4D Gaussian Splatting](https://arxiv.org/abs/2511.16112)**  
  *Taeho Kang, Jaeyeon Park, Kyungjin Lee, Youngki Lee*  
  `2025-11-20` · `cs.CV` · [abs](https://arxiv.org/abs/2511.16112) · [pdf](https://arxiv.org/pdf/2511.16112.pdf)
  > 💡 针对4DGS动态场景重建模糊问题，提出椭圆错误聚类与分组高斯致密化，显著提升渲染质量及时空一致性。

  <details><summary>Abstract</summary>

  Existing 4D Gaussian Splatting (4DGS) methods struggle to accurately reconstruct dynamic scenes, often failing to resolve ambiguous pixel correspondences and inadequate densification in dynamic regions. We address these issues by introducing a novel method composed of two key components: (1) Elliptical Error Clustering and Error Correcting Splat Addition that pinpoints dynamic areas to improve and initialize fitting splats, and (2) Grouped 4D Gaussian Splatting that improves consistency of mapping between splats and represented dynamic objects. Specifically, we classify rendering errors into missing-color and occlusion types, then apply targeted corrections via backprojection or foreground splitting guided by cross-view color consistency. Evaluations on Neural 3D Video and Technicolor datasets demonstrate that our approach significantly improves temporal consistency and achieves state-of-the-art perceptual rendering quality, improving 0.39dB of PSNR on the Technicolor Light Field dataset. Our visualization shows improved alignment between splats and dynamic objects, and the error correction method's capability to identify errors and properly initialize new splats. Our implementation details and source code are available at https://github.com/tho-kn/cem-4dgs.

  </details>


- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540)**  
  *Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin*  
  `2025-11-18` · `cs.CV` · [abs](https://arxiv.org/abs/2511.14540) · [pdf](https://arxiv.org/pdf/2511.14540.pdf)
  > 💡 针对无先验的手-物交互动态重建，提出交互感知4D高斯和分段线性假设，结合手信息变形场与渐进优化，实现SOTA。

  <details><summary>Abstract</summary>

  This paper focuses on a challenging setting of simultaneously modeling geometry and appearance of hand-object interaction scenes without any object priors. We follow the trend of dynamic 3D Gaussian Splatting based methods, and address several significant challenges. To model complex hand-object interaction with mutual occlusion and edge blur, we present interaction-aware hand-object Gaussians with newly introduced optimizable parameters aiming to adopt piecewise linear hypothesis for clearer structural representation. Moreover, considering the complementarity and tightness of hand shape and object shape during interaction dynamics, we incorporate hand information into object deformation field, constructing interaction-aware dynamic fields to model flexible motions. To further address difficulties in the optimization process, we propose a progressive strategy that handles dynamic regions and static background step by step. Correspondingly, explicit regularizations are designed to stabilize the hand-object representations for smooth motion transition, physical interaction reality, and coherent lighting. Experiments show that our approach surpasses existing dynamic 3D-GS-based methods and achieves state-of-the-art performance in reconstructing dynamic hand-object interaction.

  </details>


- **[Dynamic Gaussian Scene Reconstruction from Unsynchronized Videos](https://arxiv.org/abs/2511.11175)**  
  *Zhixin Xu, Hengyu Zhou, Yuan Liu, Wenhan Xue, Hao Pan, Wenping Wang, Bin Wang*  
  `2025-11-14` · `cs.CV` · [abs](https://arxiv.org/abs/2511.11175) · [pdf](https://arxiv.org/pdf/2511.11175.pdf)
  > 💡 针对非同步多视角视频，提出粗到细时间对齐模块，消除时移误差以增强4DGS重建鲁棒性。

  <details><summary>Abstract</summary>

  Multi-view video reconstruction plays a vital role in computer vision, enabling applications in film production, virtual reality, and motion analysis. While recent advances such as 4D Gaussian Splatting (4DGS) have demonstrated impressive capabilities in dynamic scene reconstruction, they typically rely on the assumption that input video streams are temporally synchronized. However, in real-world scenarios, this assumption often fails due to factors like camera trigger delays or independent recording setups, leading to temporal misalignment across views and reduced reconstruction quality. To address this challenge, a novel temporal alignment strategy is proposed for high-quality 4DGS reconstruction from unsynchronized multi-view videos. Our method features a coarse-to-fine alignment module that estimates and compensates for each camera's time shift. The method first determines a coarse, frame-level offset and then refines it to achieve sub-frame accuracy. This strategy can be integrated as a readily integrable module into existing 4DGS frameworks, enhancing their robustness when handling asynchronous data. Experiments show that our approach effectively processes temporally misaligned videos and significantly enhances baseline methods.

  </details>


- **[4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation](https://arxiv.org/abs/2511.07241)**  
  *Mengmeng Liu, Jiuming Liu, Yunpeng Zhang, Jiangtao Li, Michael Ying Yang, Francesco Nex, Hao Cheng*  
  `2025-11-10` · `cs.CV` · [abs](https://arxiv.org/abs/2511.07241) · [pdf](https://arxiv.org/pdf/2511.07241.pdf)
  > 💡 4D生成缺乏时空一致性，提出时空矫正与自适应密集化剪枝策略，实现高质量、一致性的动态4D内容生成。

  <details><summary>Abstract</summary>

  Remarkable advances in recent 2D image and 3D shape generation have induced a significant focus on dynamic 4D content generation. However, previous 4D generation methods commonly struggle to maintain spatial-temporal consistency and adapt poorly to rapid temporal variations, due to the lack of effective spatial-temporal modeling. To address these problems, we propose a novel 4D generation network called 4DSTR, which modulates generative 4D Gaussian Splatting with spatial-temporal rectification. Specifically, temporal correlation across generated 4D sequences is designed to rectify deformable scales and rotations and guarantee temporal consistency. Furthermore, an adaptive spatial densification and pruning strategy is proposed to address significant temporal variations by dynamically adding or deleting Gaussian points with the awareness of their pre-frame movements. Extensive experiments demonstrate that our 4DSTR achieves state-of-the-art performance in video-to-4D generation, excelling in reconstruction quality, spatial-temporal consistency, and adaptation to rapid temporal movements.

  </details>


- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122)**  
  *Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu*  
  `2025-11-10` · `cs.CV` · [abs](https://arxiv.org/abs/2511.07122) · [pdf](https://arxiv.org/pdf/2511.07122.pdf)
  > 💡 针对稀疏帧动态场景重建中纹理丰富区域失效问题，提出纹理感知变形正则化和规范优化，实现高质量4D重建。

  <details><summary>Abstract</summary>

  Dynamic Gaussian Splatting approaches have achieved remarkable performance for 4D scene reconstruction. However, these approaches rely on dense-frame video sequences for photorealistic reconstruction. In real-world scenarios, due to equipment constraints, sometimes only sparse frames are accessible. In this paper, we propose Sparse4DGS, the first method for sparse-frame dynamic scene reconstruction. We observe that dynamic reconstruction methods fail in both canonical and deformed spaces under sparse-frame settings, especially in areas with high texture richness. Sparse4DGS tackles this challenge by focusing on texture-rich areas. For the deformation network, we propose Texture-Aware Deformation Regularization, which introduces a texture-based depth alignment loss to regulate Gaussian deformation. For the canonical Gaussian field, we introduce Texture-Aware Canonical Optimization, which incorporates texture-based noise into the gradient descent process of canonical Gaussians. Extensive experiments show that when taking sparse frames as inputs, our method outperforms existing dynamic or few-shot techniques on NeRF-Synthetic, HyperNeRF, NeRF-DS, and our iPhone-4D datasets.

  </details>


- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632)**  
  *Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang*  
  `2025-11-10` · `cs.CV` · [abs](https://arxiv.org/abs/2511.06632) · [pdf](https://arxiv.org/pdf/2511.06632.pdf)
  > 💡 利用外观位置不一致识别动态实例，结合实例感知4D高斯实现无标签街景重建与编辑。

  <details><summary>Abstract</summary>

  Urban scene reconstruction is critical for autonomous driving, enabling structured 3D representations for data synthesis and closed-loop testing. Supervised approaches rely on costly human annotations and lack scalability, while current self-supervised methods often confuse static and dynamic elements and fail to distinguish individual dynamic objects, limiting fine-grained editing. We propose DIAL-GS, a novel dynamic instance-aware reconstruction method for label-free street scenes with 4D Gaussian Splatting. We first accurately identify dynamic instances by exploiting appearance-position inconsistency between warped rendering and actual observation. Guided by instance-level dynamic perception, we employ instance-aware 4D Gaussians as the unified volumetric representation, realizing dynamic-adaptive and instance-aware reconstruction. Furthermore, we introduce a reciprocal mechanism through which identity and dynamics reinforce each other, enhancing both integrity and consistency. Experiments on urban driving scenarios show that DIAL-GS surpasses existing self-supervised baselines in reconstruction quality and instance-level editing, offering a concise yet powerful solution for urban scene modeling.

  </details>


- **[Detail Enhanced Gaussian Splatting for Large-Scale Volumetric Capture](https://arxiv.org/abs/2511.21697)**  
  *Julien Philip, Li Ma, Pascal Clausen, Wenqi Xian, Ahmet Levent Taşel, Mingming He, Xueming Yu, David M. George, Ning Yu, Oliver Pilarski, Paul Debevec*  
  `2025-10-31` · `cs.GR` · [abs](https://arxiv.org/abs/2511.21697) · [pdf](https://arxiv.org/pdf/2511.21697.pdf)
  > 💡 提出动态高斯泼溅与扩散细节增强的4D捕捉管遍，实现大规模场景到4K面部特写的高质量渲染。

  <details><summary>Abstract</summary>

  We present a unique system for large-scale, multi-performer, high resolution 4D volumetric capture providing realistic free-viewpoint video up to and including 4K resolution facial closeups. To achieve this, we employ a novel volumetric capture, reconstruction and rendering pipeline based on Dynamic Gaussian Splatting and Diffusion-based Detail Enhancement. We design our pipeline specifically to meet the demands of high-end media production. We employ two capture rigs: the Scene Rig, which captures multi-actor performances at a resolution which falls short of 4K production quality, and the Face Rig, which records high-fidelity single-actor facial detail to serve as a reference for detail enhancement. We first reconstruct dynamic performances from the Scene Rig using 4D Gaussian Splatting, incorporating new model designs and training strategies to improve reconstruction, dynamic range, and rendering quality. Then to render high-quality images for facial closeups, we introduce a diffusion-based detail enhancement model. This model is fine-tuned with high-fidelity data from the same actors recorded in the Face Rig. We train on paired data generated from low- and high-quality Gaussian Splatting (GS) models, using the low-quality input to match the quality of the Scene Rig, with the high-quality GS as ground truth. Our results demonstrate the effectiveness of this pipeline in bridging the gap between the scalable performance capture of a large-scale rig and the high-resolution standards required for film and media production.

  </details>


- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694)**  
  *Bernhard Kerbl*  
  `2025-10-30` · `cs.CV` · [abs](https://arxiv.org/abs/2510.26694) · [pdf](https://arxiv.org/pdf/2510.26694.pdf)
  > 💡 回顾3DGS在效率、动态化、数学基础及平台适配方面的进展，展现其成为3D视觉与图形基础工具的演变。

  <details><summary>Abstract</summary>

  Since its introduction, 3D Gaussian Splatting (3DGS) has rapidly transformed the landscape of 3D scene representations, inspiring an extensive body of associated research. Follow-up work includes analyses and contributions that enhance the efficiency, scalability, and real-world applicability of 3DGS. In this summary, we present an overview of several key directions that have emerged in the wake of 3DGS. We highlight advances enabling resource-efficient training and rendering, the evolution toward dynamic (or four-dimensional, 4DGS) representations, and deeper exploration of the mathematical foundations underlying its appearance modeling and rendering process. Furthermore, we examine efforts to bring 3DGS to mobile and virtual reality platforms, its extension to massive-scale environments, and recent progress toward near-instant radiance field reconstruction via feed-forward or distributed computation. Collectively, these developments illustrate how 3DGS has evolved from a breakthrough representation into a versatile and foundational tool for 3D vision and graphics.

  </details>


- **[EndoWave: Rational-Wavelet 4D Gaussian Splatting for Endoscopic Reconstruction](https://arxiv.org/abs/2510.23087)**  
  *Taoyu Wu, Yiyi Miao, Jiaxin Guo, Ziyan Chen, Sihang Zhao, Zhuoxiao Li, Zhe Tang, Baoru Huang, Limin Yu*  
  `2025-10-27` · `cs.CV` · [abs](https://arxiv.org/abs/2510.23087) · [pdf](https://arxiv.org/pdf/2510.23087.pdf)
  > 💡 针对内窥镜动态场景，提出4D高斯泼溅结合光流约束与有理小波监督，实现高质量时空重建。

  <details><summary>Abstract</summary>

  In robot-assisted minimally invasive surgery, accurate 3D reconstruction from endoscopic video is vital for downstream tasks and improved outcomes. However, endoscopic scenarios present unique challenges, including photometric inconsistencies, non-rigid tissue motion, and view-dependent highlights. Most 3DGS-based methods that rely solely on appearance constraints for optimizing 3DGS are often insufficient in this context, as these dynamic visual artifacts can mislead the optimization process and lead to inaccurate reconstructions. To address these limitations, we present EndoWave, a unified spatio-temporal Gaussian Splatting framework by incorporating an optical flow-based geometric constraint and a multi-resolution rational wavelet supervision. First, we adopt a unified spatio-temporal Gaussian representation that directly optimizes primitives in a 4D domain. Second, we propose a geometric constraint derived from optical flow to enhance temporal coherence and effectively constrain the 3D structure of the scene. Third, we propose a multi-resolution rational orthogonal wavelet as a constraint, which can effectively separate the details of the endoscope and enhance the rendering performance. Extensive evaluations on two real surgical datasets, EndoNeRF and StereoMIS, demonstrate that our method EndoWave achieves state-of-the-art reconstruction quality and visual accuracy compared to the baseline method.

  </details>


- **[DynaPose4D: High-Quality 4D Dynamic Content Generation via Pose Alignment Loss](https://arxiv.org/abs/2510.22473)**  
  *Jing Yang, Yufeng Yang*  
  `2025-10-26` · `cs.CV` · [abs](https://arxiv.org/abs/2510.22473) · [pdf](https://arxiv.org/pdf/2510.22473.pdf)
  > 💡 单图生成4D动态内容困难，融合4D高斯溅射与类别无关姿态估计，通过姿态对齐损失增强运动一致性与流畅性。

  <details><summary>Abstract</summary>

  Recent advancements in 2D and 3D generative models have expanded the capabilities of computer vision. However, generating high-quality 4D dynamic content from a single static image remains a significant challenge. Traditional methods have limitations in modeling temporal dependencies and accurately capturing dynamic geometry changes, especially when considering variations in camera perspective. To address this issue, we propose DynaPose4D, an innovative solution that integrates 4D Gaussian Splatting (4DGS) techniques with Category-Agnostic Pose Estimation (CAPE) technology. This framework uses 3D Gaussian Splatting to construct a 3D model from single images, then predicts multi-view pose keypoints based on one-shot support from a chosen view, leveraging supervisory signals to enhance motion consistency. Experimental results show that DynaPose4D achieves excellent coherence, consistency, and fluidity in dynamic motion generation. These findings not only validate the efficacy of the DynaPose4D framework but also indicate its potential applications in the domains of computer vision and animation production.

  </details>


- **[Virtually Being: Customizing Camera-Controllable Video Diffusion Models with Multi-View Performance Captures](https://arxiv.org/abs/2510.14179)**  
  *Yuancheng Xu, Wenqi Xian, Li Ma, Julien Philip, Ahmet Levent Taşel, Yiwei Zhao, Ryan Burgert, Mingming He, Oliver Hermann, Oliver Pilarski, Rahul Garg, Paul Debevec, Ning Yu*  
  `2025-10-16` · `cs.CV` · [abs](https://arxiv.org/abs/2510.14179) · [pdf](https://arxiv.org/pdf/2510.14179.pdf)
  > 💡 利用4DGS与重照明生成多视角数据，微调视频扩散模型实现角色一致与相机可控，提升虚拟制作视频质量。

  <details><summary>Abstract</summary>

  We introduce a framework that enables both multi-view character consistency and 3D camera control in video diffusion models through a novel customization data pipeline. We train the character consistency component with recorded volumetric capture performances re-rendered with diverse camera trajectories via 4D Gaussian Splatting (4DGS), lighting variability obtained with a video relighting model. We fine-tune state-of-the-art open-source video diffusion models on this data to provide strong multi-view identity preservation, precise camera control, and lighting adaptability. Our framework also supports core capabilities for virtual production, including multi-subject generation using two approaches: joint training and noise blending, the latter enabling efficient composition of independently customized models at inference time; it also achieves scene and real-life video customization as well as control over motion and spatial layout during customization. Extensive experiments show improved video quality, higher personalization accuracy, and enhanced camera control and lighting adaptability, advancing the integration of video generation into virtual production. Our project page is available at: https://eyeline-labs.github.io/Virtually-Being.

  </details>


- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030)**  
  *Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen*  
  `2025-10-11` · `cs.CV` · [abs](https://arxiv.org/abs/2510.10030) · [pdf](https://arxiv.org/pdf/2510.10030.pdf)
  > 💡 利用帧间预测与自适应量化熵编码压缩动态3DGS时空冗余，实现90倍压缩且保持高质量与高速渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has garnered significant attention due to its superior scene representation fidelity and real-time rendering performance, especially for dynamic 3D scene reconstruction (\textit{i.e.}, 4D reconstruction). However, despite achieving promising results, most existing algorithms overlook the substantial temporal and spatial redundancies inherent in dynamic scenes, leading to prohibitive memory consumption. To address this, we propose P-4DGS, a novel dynamic 3DGS representation for compact 4D scene modeling. Inspired by intra- and inter-frame prediction techniques commonly used in video compression, we first design a 3D anchor point-based spatial-temporal prediction module to fully exploit the spatial-temporal correlations across different 3D Gaussian primitives. Subsequently, we employ an adaptive quantization strategy combined with context-based entropy coding to further reduce the size of the 3D anchor points, thereby achieving enhanced compression efficiency. To evaluate the rate-distortion performance of our proposed P-4DGS in comparison with other dynamic 3DGS representations, we conduct extensive experiments on both synthetic and real-world datasets. Experimental results demonstrate that our approach achieves state-of-the-art reconstruction quality and the fastest rendering speed, with a remarkably low storage footprint (around \textbf{1MB} on average), achieving up to \textbf{40$\times$} and \textbf{90$\times$} compression on synthetic and real-world scenes, respectively.

  </details>


- **[SIMSplat: Predictive Driving Scene Editing with Language-aligned 4D Gaussian Splatting](https://arxiv.org/abs/2510.02469)**  
  *Sung-Yeon Park, Adam Lee, Juanwu Lu, Can Cui, Luyang Jiang, Rohit Gupta, Kyungtae Han, Ahmadreza Moradipari, Ziran Wang*  
  `2025-10-02` · `cs.RO` · [abs](https://arxiv.org/abs/2510.02469) · [pdf](https://arxiv.org/pdf/2510.02469.pdf)
  > 💡 语言对齐4D高斯泼溅实现自然语言驱动的驾驶场景编辑，支持物体级添加与轨迹修改，并通过运动预测细化路径。

  <details><summary>Abstract</summary>

  Driving scene manipulation with sensor data is emerging as a promising alternative to traditional virtual driving simulators. However, existing frameworks struggle to generate realistic scenarios efficiently due to limited editing capabilities. To address these challenges, we present SIMSplat, a predictive driving scene editor with language-aligned Gaussian splatting. As a language-controlled editor, SIMSplat enables intuitive manipulation using natural language prompts. By aligning language with Gaussian-reconstructed scenes, it further supports direct querying of road objects, allowing precise and flexible editing. Our method provides detailed object-level editing, including adding new objects and modifying the trajectories of both vehicles and pedestrians, while also incorporating predictive path refinement through multi-agent motion prediction to generate realistic interactions among all agents in the scene. Experiments on the Waymo dataset demonstrate SIMSplat's extensive editing capabilities and adaptability across a wide range of scenarios. Project page: https://sungyeonparkk.github.io/simsplat/

  </details>


- **[4DGS-Craft: Consistent and Interactive 4D Gaussian Splatting Editing](https://arxiv.org/abs/2510.01991)**  
  *Lei Liu, Can Wang, Zhenghao Chen, Dong Xu*  
  `2025-10-02` · `cs.CV` · [abs](https://arxiv.org/abs/2510.01991) · [pdf](https://arxiv.org/pdf/2510.01991.pdf)
  > 💡 针对4DGS编辑中一致性与交互性不足，提出4D感知模型与LLM模块，实现可控

  <details><summary>Abstract</summary>

  Recent advances in 4D Gaussian Splatting (4DGS) editing still face challenges with view, temporal, and non-editing region consistency, as well as with handling complex text instructions. To address these issues, we propose 4DGS-Craft, a consistent and interactive 4DGS editing framework. We first introduce a 4D-aware InstructPix2Pix model to ensure both view and temporal consistency. This model incorporates 4D VGGT geometry features extracted from the initial scene, enabling it to capture underlying 4D geometric structures during editing. We further enhance this model with a multi-view grid module that enforces consistency by iteratively refining multi-view input images while jointly optimizing the underlying 4D scene. Furthermore, we preserve the consistency of non-edited regions through a novel Gaussian selection mechanism, which identifies and optimizes only the Gaussians within the edited regions. Beyond consistency, facilitating user interaction is also crucial for effective 4DGS editing. Therefore, we design an LLM-based module for user intent understanding. This module employs a user instruction template to define atomic editing operations and leverages an LLM for reasoning. As a result, our framework can interpret user intent and decompose complex instructions into a logical sequence of atomic operations, enabling it to handle intricate user commands and further enhance editing performance. Compared to related works, our approach enables more consistent and controllable 4D scene editing. Our code will be made available upon acceptance.

  </details>


- **[Instant4D: 4D Gaussian Splatting in Minutes](https://arxiv.org/abs/2510.01119)**  
  *Zhanpeng Luo, Haoxi Ran, Li Lu*  
  `2025-10-01` · `cs.CV` · [abs](https://arxiv.org/abs/2510.01119) · [pdf](https://arxiv.org/pdf/2510.01119.pdf)
  > 💡 针对非标定视频动态重建，提出Instant4D，结合视觉SLAM与网格剪枝的4D高斯表示，实现分钟级高效重建。

  <details><summary>Abstract</summary>

  Dynamic view synthesis has seen significant advances, yet reconstructing scenes from uncalibrated, casual video remains challenging due to slow optimization and complex parameter estimation. In this work, we present Instant4D, a monocular reconstruction system that leverages native 4D representation to efficiently process casual video sequences within minutes, without calibrated cameras or depth sensors. Our method begins with geometric recovery through deep visual SLAM, followed by grid pruning to optimize scene representation. Our design significantly reduces redundancy while maintaining geometric integrity, cutting model size to under 10% of its original footprint. To handle temporal dynamics efficiently, we introduce a streamlined 4D Gaussian representation, achieving a 30x speed-up and reducing training time to within two minutes, while maintaining competitive performance across several benchmarks. Our method reconstruct a single video within 10 minutes on the Dycheck dataset or for a typical 200-frame video. We further apply our model to in-the-wild videos, showcasing its generalizability. Our project website is published at https://instant4d.github.io/.

  </details>


- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853)**  
  *Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu*  
  `2025-09-26` · `cs.CV` · [abs](https://arxiv.org/abs/2509.21853) · [pdf](https://arxiv.org/pdf/2509.21853.pdf)
  > 💡 针对动态高动态范围新视角合成难题，提出HDR-4DGS，通过动态色调映射实现时空一致的逼真渲染。

  <details><summary>Abstract</summary>

  High Dynamic Range Novel View Synthesis (HDR NVS) seeks to learn an HDR 3D model from Low Dynamic Range (LDR) training images captured under conventional imaging conditions. Current methods primarily focus on static scenes, implicitly assuming all scene elements remain stationary and non-living. However, real-world scenarios frequently feature dynamic elements, such as moving objects, varying lighting conditions, and other temporal events, thereby presenting a significantly more challenging scenario. To address this gap, we propose a more realistic problem named HDR Dynamic Novel View Synthesis (HDR DNVS), where the additional dimension ``Dynamic'' emphasizes the necessity of jointly modeling temporal radiance variations alongside sophisticated 3D translation between LDR and HDR. To tackle this complex, intertwined challenge, we introduce HDR-4DGS, a Gaussian Splatting-based architecture featured with an innovative dynamic tone-mapping module that explicitly connects HDR and LDR domains, maintaining temporal radiance coherence by dynamically adapting tone-mapping functions according to the evolving radiance distributions across the temporal dimension. As a result, HDR-4DGS achieves both temporal radiance consistency and spatially accurate color translation, enabling photorealistic HDR renderings from arbitrary viewpoints and time instances. Extensive experiments demonstrate that HDR-4DGS surpasses existing state-of-the-art methods in both quantitative performance and visual fidelity. Source code is available at https://github.com/prinasi/HDR-4DGS.

  </details>


- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251)**  
  *Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen*  
  `2025-09-24` · `cs.CV` · [abs](https://arxiv.org/abs/2509.20251) · [pdf](https://arxiv.org/pdf/2509.20251.pdf)
  > 💡 提出PhiGenesis框架，结合视频VAE与Stereo Forcing条件策略，实现无需逐场景优化的4D驾驶场景生成，在几何与时间一致性上达到SOTA。

  <details><summary>Abstract</summary>

  Current generative models struggle to synthesize dynamic 4D driving scenes that simultaneously support temporal extrapolation and spatial novel view synthesis (NVS) without per-scene optimization. Bridging generation and novel view synthesis remains a major challenge. We present PhiGenesis, a unified framework for 4D scene generation that extends video generation techniques with geometric and temporal consistency. Given multi-view image sequences and camera parameters, PhiGenesis produces temporally continuous 4D Gaussian splatting representations along target 3D trajectories. In its first stage, PhiGenesis leverages a pre-trained video VAE with a novel range-view adapter to enable feed-forward 4D reconstruction from multi-view images. This architecture supports single-frame or video inputs and outputs complete 4D scenes including geometry, semantics, and motion. In the second stage, PhiGenesis introduces a geometric-guided video diffusion model, using rendered historical 4D scenes as priors to generate future views conditioned on trajectories. To address geometric exposure bias in novel views, we propose Stereo Forcing, a novel conditioning strategy that integrates geometric uncertainty during denoising. This method enhances temporal coherence by dynamically adjusting generative influence based on uncertainty-aware perturbations. Our experimental results demonstrate that our method achieves state-of-the-art performance in both appearance and geometric reconstruction, temporal generation and novel view synthesis (NVS) tasks, while simultaneously delivering competitive performance in downstream evaluations. Homepage is at \href{https://jiangxb98.github.io/PhiGensis}{PhiGensis}.

  </details>


- **[4DGCPro: Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming](https://arxiv.org/abs/2509.17513)**  
  *Zihan Zheng, Zhenlong Wu, Houqiang Zhong, Yuan Tian, Ning Cao, Lan Xu, Jiangchao Yao, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang*  
  `2025-09-22` · `cs.CV` · [abs](https://arxiv.org/abs/2509.17513) · [pdf](https://arxiv.org/pdf/2509.17513.pdf)
  > 💡 针对现有体积视频压缩缺乏灵活性和实时移动端渲染问题，提出层次化4D高斯压缩框架，实现单模型内可伸缩多码率与实时移动端解码。

  <details><summary>Abstract</summary>

  Achieving seamless viewing of high-fidelity volumetric video, comparable to 2D video experiences, remains an open challenge. Existing volumetric video compression methods either lack the flexibility to adjust quality and bitrate within a single model for efficient streaming across diverse networks and devices, or struggle with real-time decoding and rendering on lightweight mobile platforms. To address these challenges, we introduce 4DGCPro, a novel hierarchical 4D Gaussian compression framework that facilitates real-time mobile decoding and high-quality rendering via progressive volumetric video streaming in a single bitstream. Specifically, we propose a perceptually-weighted and compression-friendly hierarchical 4D Gaussian representation with motion-aware adaptive grouping to reduce temporal redundancy, preserve coherence, and enable scalable multi-level detail streaming. Furthermore, we present an end-to-end entropy-optimized training scheme, which incorporates layer-wise rate-distortion (RD) supervision and attribute-specific entropy modeling for efficient bitstream generation. Extensive experiments show that 4DGCPro enables flexible quality and multiple bitrate within a single model, achieving real-time decoding and rendering on mobile devices while outperforming existing methods in RD performance across multiple datasets. Project Page: https://mediax-sjtu.github.io/4DGCPro

  </details>


- **[4D-MoDe: Towards Editable and Scalable Volumetric Streaming via Motion-Decoupled 4D Gaussian Compression](https://arxiv.org/abs/2509.17506)**  
  *Houqiang Zhong, Zihan Zheng, Qiang Hu, Yuan Tian, Ning Cao, Lan Xu, Xiaoyun Zhang, Zhengxue Cheng, Li Song, Wenjun Zhang*  
  `2025-09-22` · `cs.CV` · [abs](https://arxiv.org/abs/2509.17506) · [pdf](https://arxiv.org/pdf/2509.17506.pdf)
  > 💡 提出

  <details><summary>Abstract</summary>

  Volumetric video has emerged as a key medium for immersive telepresence and augmented/virtual reality, enabling six-degrees-of-freedom (6DoF) navigation and realistic spatial interactions. However, delivering high-quality dynamic volumetric content at scale remains challenging due to massive data volume, complex motion, and limited editability of existing representations. In this paper, we present 4D-MoDe, a motion-decoupled 4D Gaussian compression framework designed for scalable and editable volumetric video streaming. Our method introduces a layered representation that explicitly separates static backgrounds from dynamic foregrounds using a lookahead-based motion decomposition strategy, significantly reducing temporal redundancy and enabling selective background/foreground streaming. To capture continuous motion trajectories, we employ a multi-resolution motion estimation grid and a lightweight shared MLP, complemented by a dynamic Gaussian compensation mechanism to model emergent content. An adaptive grouping scheme dynamically inserts background keyframes to balance temporal consistency and compression efficiency. Furthermore, an entropy-aware training pipeline jointly optimizes the motion fields and Gaussian parameters under a rate-distortion (RD) objective, while employing range-based and KD-tree compression to minimize storage overhead. Extensive experiments on multiple datasets demonstrate that 4D-MoDe consistently achieves competitive reconstruction quality with an order of magnitude lower storage cost (e.g., as low as \textbf{11.4} KB/frame) compared to state-of-the-art methods, while supporting practical applications such as background replacement and foreground-only streaming.

  </details>


- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event Cameras](https://arxiv.org/abs/2508.09912)**  
  *Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian*  
  `2025-08-13` · `cs.CV` · [abs](https://arxiv.org/abs/2508.09912) · [pdf](https://arxiv.org/pdf/2508.09912.pdf)
  > 💡 针对RGB相机在高速场景中的局限，利用多视角事件相机结合4D Gaussian Splatting实现高保真动态重建。

  <details><summary>Abstract</summary>

  Novel view synthesis and 4D reconstruction techniques predominantly rely on RGB cameras, thereby inheriting inherent limitations such as the dependence on adequate lighting, susceptibility to motion blur, and a limited dynamic range. Event cameras, offering advantages of low power, high temporal resolution and high dynamic range, have brought a new perspective to addressing the scene reconstruction challenges in high-speed motion and

  </details>


- **[S^2VG: 3D Stereoscopic and Spatial Video Generation via Denoising Frame Matrix](https://arxiv.org/abs/2508.08048)**  
  *Peng Dai, Feitong Tan, Qiangeng Xu, Yihua Huang, David Futschik, Ruofei Du, Sean Fanello, Yinda Zhang, Xiaojuan Qi*  
  `2025-08-11` · `cs.CV` · [abs](https://arxiv.org/abs/2508.08048) · [pdf](https://arxiv.org/pdf/2508.08048.pdf)
  > 💡 提出无姿态无训练方法，利用单目视频模型结合帧矩阵修复和双重更新生成3D立体和空间视频，无需微调。

  <details><summary>Abstract</summary>

  While video generation models excel at producing high-quality monocular videos, generating 3D stereoscopic and spatial videos for immersive applications remains an underexplored challenge. We present a pose-free and training-free method that leverages an off-the-shelf monocular video generation model to produce immersive 3D videos. Our approach first warps the generated monocular video into pre-defined camera viewpoints using estimated depth information, then applies a novel \textit{frame matrix} inpainting framework. This framework utilizes the original video generation model to synthesize missing content across different viewpoints and timestamps, ensuring spatial and temporal consistency without requiring additional model fine-tuning. Moreover, we develop a \dualupdate~scheme that further improves the quality of video inpainting by alleviating the negative effects propagated from disoccluded areas in the latent space. The resulting multi-view videos are then adapted into stereoscopic pairs or optimized into 4D Gaussians for spatial video synthesis. We validate the efficacy of our proposed method by conducting experiments on videos from various generative models, such as Sora, Lumiere, WALT, and Zeroscope. The experiments demonstrate that our method has a significant improvement over previous methods. Project page at: https://daipengwa.github.io/S-2VG_ProjectPage/

  </details>


- **[Splat4D: Diffusion-Enhanced 4D Gaussian Splatting for Temporally and Spatially Consistent Content Creation](https://arxiv.org/abs/2508.07557)**  
  *Minghao Yin, Yukang Cao, Songyou Peng, Kai Han*  
  `2025-08-11` · `cs.CV` · [abs](https://arxiv.org/abs/2508.07557) · [pdf](https://arxiv.org/pdf/2508.07557.pdf)
  > 💡 使用多视图渲染、不一致识别、视频扩散模型和非对称U-Net，Splat4D实现高质量时空一致的4D内容生成。

  <details><summary>Abstract</summary>

  Generating high-quality 4D content from monocular videos for applications such as digital humans and AR/VR poses challenges in ensuring temporal and spatial consistency, preserving intricate details, and incorporating user guidance effectively. To overcome these challenges, we introduce Splat4D, a novel framework enabling high-fidelity 4D content generation from a monocular video. Splat4D achieves superior performance while maintaining faithful spatial-temporal coherence by leveraging multi-view rendering, inconsistency identification, a video diffusion model, and an asymmetric U-Net for refinement. Through extensive evaluations on public benchmarks, Splat4D consistently demonstrates state-of-the-art performance across various metrics, underscoring the efficacy of our approach. Additionally, the versatility of Splat4D is validated in various applications such as text/image conditioned 4D generation, 4D human generation, and text-guided content editing, producing coherent outcomes following user instructions.

  </details>


- **[VDEGaussian: Video Diffusion Enhanced 4D Gaussian Splatting for Dynamic Urban Scenes Modeling](https://arxiv.org/abs/2508.02129)**  
  *Yuru Xiao, Zihan Lin, Chao Lu, Deming Zhai, Kui Jiang, Wenbo Zhao, Wei Zhang, Junjun Jiang, Huanran Wang, Xianming Liu*  
  `2025-08-04` · `cs.CV` · [abs](https://arxiv.org/abs/2508.02129) · [pdf](https://arxiv.org/pdf/2508.02129.pdf)
  > 💡 利用视频扩散模型蒸馏时间一致先验，结合联合时间戳优化与不确定性蒸馏，提升动态城市场景中快速运动物体的建模，PSNR提升约2dB。

  <details><summary>Abstract</summary>

  Dynamic urban scene modeling is a rapidly evolving area with broad applications. While current approaches leveraging neural radiance fields or Gaussian Splatting have achieved fine-grained reconstruction and high-fidelity novel view synthesis, they still face significant limitations. These often stem from a dependence on pre-calibrated object tracks or difficulties in accurately modeling fast-moving objects from undersampled capture, particularly due to challenges in handling temporal discontinuities. To overcome these issues, we propose a novel video diffusion-enhanced 4D Gaussian Splatting framework. Our key insight is to distill robust, temporally consistent priors from a test-time adapted video diffusion model. To ensure precise pose alignment and effective integration of this denoised content, we introduce two core innovations: a joint timestamp optimization strategy that refines interpolated frame poses, and an uncertainty distillation method that adaptively extracts target content while preserving well-reconstructed regions. Extensive experiments demonstrate that our method significantly enhances dynamic modeling, especially for fast-moving objects, achieving an approximate PSNR gain of 2 dB for novel view synthesis over baseline approaches.

  </details>


- **[MVG4D: Image Matrix-Based Multi-View and Motion Generation for 4D Content Creation from a Single Image](https://arxiv.org/abs/2507.18371)**  
  *DongFu Yin, Xiaotian Chen, Fei Richard Yu, Xuanchen Li, Xinhao Zhang*  
  `2025-07-24` · `cs.CV` · [abs](https://arxiv.org/abs/2507.18371) · [pdf](https://arxiv.org/pdf/2507.18371.pdf)
  > 💡 提出MVG4D框架，用图像矩阵合成时空一致多视角图像，结合4D高斯泼溅和变形网络，从单图生成高保真动态4D内容。

  <details><summary>Abstract</summary>

  Advances in generative modeling have significantly enhanced digital content creation, extending from 2D images to complex 3D and 4D scenes. Despite substantial progress, producing high-fidelity and temporally consistent dynamic 4D content remains a challenge. In this paper, we propose MVG4D, a novel framework that generates dynamic 4D content from a single still image by combining multi-view synthesis with 4D Gaussian Splatting (4D GS). At its core, MVG4D employs an image matrix module that synthesizes temporally coherent and spatially diverse multi-view images, providing rich supervisory signals for downstream 3D and 4D reconstruction. These multi-view images are used to optimize a 3D Gaussian point cloud, which is further extended into the temporal domain via a lightweight deformation network. Our method effectively enhances temporal consistency, geometric fidelity, and visual realism, addressing key challenges in motion discontinuity and background degradation that affect prior 4D GS-based methods. Extensive experiments on the Objaverse dataset demonstrate that MVG4D outperforms state-of-the-art baselines in CLIP-I, PSNR, FVD, and time efficiency. Notably, it reduces flickering artifacts and sharpens structural details across views and time, enabling more immersive AR/VR experiences. MVG4D sets a new direction for efficient and controllable 4D generation from minimal inputs.

  </details>


- **[Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian Splatting](https://arxiv.org/abs/2507.17336)**  
  *Hyeongmin Lee, Kyungjune Baek*  
  `2025-07-23` · `cs.GR` · [abs](https://arxiv.org/abs/2507.17336) · [pdf](https://arxiv.org/pdf/2507.17336.pdf)
  > 💡 针对4DGS存储庞大问题，提出端到端率失真优化压缩框架，利用小波变换及时序平滑先验，实现91倍压缩且保持高保真。

  <details><summary>Abstract</summary>

  Dynamic 4D Gaussian Splatting (4DGS) effectively extends the high-speed rendering capabilities of 3D Gaussian Splatting (3DGS) to represent volumetric videos. However, the large number of Gaussians, substantial temporal redundancies, and especially the absence of an entropy-aware compression framework result in large storage requirements. Consequently, this poses significant challenges for practical deployment, efficient edge-device processing, and data transmission. In this paper, we introduce a novel end-to-end RD-optimized compression framework tailored for 4DGS, aiming to enable flexible, high-fidelity rendering across varied computational platforms. Leveraging Fully Explicit Dynamic Gaussian Splatting (Ex4DGS), one of the state-of-the-art 4DGS methods, as our baseline, we start from the existing 3DGS compression methods for compatibility while effectively addressing additional challenges introduced by the temporal axis. In particular, instead of storing motion trajectories independently per point, we employ a wavelet transform to reflect the real-world smoothness prior, significantly enhancing storage efficiency. This approach yields significantly improved compression ratios and provides a user-controlled balance between compression efficiency and rendering quality. Extensive experiments demonstrate the effectiveness of our method, achieving up to 91$\times$ compression compared to the original Ex4DGS model while maintaining high visual fidelity. These results highlight the applicability of our framework for real-time dynamic scene rendering in diverse scenarios, from resource-constrained edge devices to high-performance environments. The source code is available at https://github.com/HyeongminLEE/RD4DGS.

  </details>


- **[SD-GS: Structured Deformable 3D Gaussians for Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2507.07465)**  
  *Wei Yao, Shuzhao Xie, Letian Li, Weixiang Zhang, Zhixin Lai, Shiqi Dai, Ke Zhang, Zhi Wang*  
  `2025-07-10` · `cs.GR` · [abs](https://arxiv.org/abs/2507.07465) · [pdf](https://arxiv.org/pdf/2507.07465.pdf)
  > 💡 提出可变形锚点网格与变形感知密集化策略，实现动态场景重建模型大小减少60%、速度提升100%且质量不减。

  <details><summary>Abstract</summary>

  Current 4D Gaussian frameworks for dynamic scene reconstruction deliver impressive visual fidelity and rendering speed, however, the inherent trade-off between storage costs and the ability to characterize complex physical motions significantly limits the practical application of these methods. To tackle these problems, we propose SD-GS, a compact and efficient dynamic Gaussian splatting framework for complex dynamic scene reconstruction, featuring two key contributions. First, we introduce a deformable anchor grid, a hierarchical and memory-efficient scene representation where each anchor point derives multiple 3D Gaussians in its local spatiotemporal region and serves as the geometric backbone of the 3D scene. Second, to enhance modeling capability for complex motions, we present a deformation-aware densification strategy that adaptively grows anchors in under-reconstructed high-dynamic regions while reducing redundancy in static areas, achieving superior visual quality with fewer anchors. Experimental results demonstrate that, compared to state-of-the-art methods, SD-GS achieves an average of 60\% reduction in model size and an average of 100\% improvement in FPS, significantly enhancing computational efficiency while maintaining or even surpassing visual quality.

  </details>


- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308)**  
  *Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren*  
  `2025-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2506.23308) · [pdf](https://arxiv.org/pdf/2506.23308.pdf)
  > 💡 针对内窥镜场景光照不均问题，提出光照自适应高斯泼溅，通过嵌入与模块建模亮度变化，实现鲁棒重建与校正。

  <details><summary>Abstract</summary>

  Accurate reconstruction of soft tissue is crucial for advancing automation in image-guided robotic surgery. The recent 3D Gaussian Splatting (3DGS) techniques and their variants, 4DGS, achieve high-quality renderings of dynamic surgical scenes in real-time. However, 3D-GS-based methods still struggle in scenarios with varying illumination, such as low light and over-exposure. Training 3D-GS in such extreme light conditions leads to severe optimization problems and devastating rendering quality. To address these challenges, we present Endo-4DGX, a novel reconstruction method with illumination-adaptive Gaussian Splatting designed specifically for endoscopic scenes with uneven lighting. By incorporating illumination embeddings, our method effectively models view-dependent brightness variations. We introduce a region-aware enhancement module to model the sub-area lightness at the Gaussian level and a spatial-aware adjustment module to learn the view-consistent brightness adjustment. With the illumination adaptive design, Endo-4DGX achieves superior rendering performance under both low-light and over-exposure conditions while maintaining geometric accuracy. Additionally, we employ an exposure control loss to restore the appearance from adverse exposure to the normal level for illumination-adaptive optimization. Experimental results demonstrate that Endo-4DGX significantly outperforms combinations of state-of-the-art reconstruction and restoration methods in challenging lighting environments, underscoring its potential to advance robot-assisted surgical applications. Our code is available at https://github.com/lastbasket/Endo-4DGX.

  </details>


- **[DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian Splatting and a Low-Rank Free-Form Deformation Model](https://arxiv.org/abs/2506.22280)**  
  *Yuliang Huang, Imraj Singh, Thomas Joyce, Kris Thielemans, Jamie R. McClelland*  
  `2025-06-27` · `eess.IV` · [abs](https://arxiv.org/abs/2506.22280) · [pdf](https://arxiv.org/pdf/2506.22280.pdf)
  > 💡 用变形引导的4D高斯散点结合低秩自由变形模型，实现高效动态CBCT重建，抑制呼吸运动伪影且速度比HexPlane快6倍。

  <details><summary>Abstract</summary>

  3D Cone-Beam CT (CBCT) is widely used in radiotherapy but suffers from motion artifacts due to breathing. A common clinical approach mitigates this by sorting projections into respiratory phases and reconstructing images per phase, but this does not account for breathing variability. Dynamic CBCT instead reconstructs images at each projection, capturing continuous motion without phase sorting. Recent advancements in 4D Gaussian Splatting (4DGS) offer powerful tools for modeling dynamic scenes, yet their application to dynamic CBCT remains underexplored. Existing 4DGS methods, such as HexPlane, use implicit motion representations, which are computationally expensive. While explicit low-rank motion models have been proposed, they lack spatial regularization, leading to inconsistencies in Gaussian motion. To address these limitations, we introduce a free-form deformation (FFD)-based spatial basis function and a deformation-informed framework that enforces consistency by coupling the temporal evolution of Gaussian's mean position, scale, and rotation under a unified deformation field. We evaluate our approach on six CBCT datasets, demonstrating superior image quality with a 6x speedup over HexPlane. These results highlight the potential of deformation-informed 4DGS for efficient, motion-compensated CBCT reconstruction. The code is available at https://github.com/Yuliang-Huang/DIGS.

  </details>


- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291)**  
  *Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang*  
  `2025-06-24` · `cs.CV` · [abs](https://arxiv.org/abs/2506.19291) · [pdf](https://arxiv.org/pdf/2506.19291.pdf)
  > 💡 针对长单目视频具身视图合成，提出可逆高斯泼溅形变网络分层分解静态背景与动态物体，实现高效高质量重建。

  <details><summary>Abstract</summary>

  We propose HoliGS, a novel deformable Gaussian splatting framework that addresses embodied view synthesis from long monocular RGB videos. Unlike prior 4D Gaussian splatting and dynamic NeRF pipelines, which struggle with training overhead in minute-long captures, our method leverages invertible Gaussian Splatting deformation networks to reconstruct large-scale, dynamic environments accurately. Specifically, we decompose each scene into a static background plus time-varying objects, each represented by learned Gaussian primitives undergoing global rigid transformations, skeleton-driven articulation, and subtle non-rigid deformations via an invertible neural flow. This hierarchical warping strategy enables robust free-viewpoint novel-view rendering from various embodied camera trajectories by attaching Gaussians to a complete canonical foreground shape (\eg, egocentric or third-person follow), which may involve substantial viewpoint changes and interactions between multiple actors. Our experiments demonstrate that \ourmethod~ achieves superior reconstruction quality on challenging datasets while significantly reducing both training and rendering time compared to state-of-the-art monocular deformable NeRFs. These results highlight a practical and scalable solution for EVS in real-world scenarios. The source code will be released.

  </details>


- **[4D-LRM: Large Space-Time Reconstruction Model From and To Any View at Any Time](https://arxiv.org/abs/2506.18890)**  
  *Ziqiao Ma, Xuweiyi Chen, Shoubin Yu, Sai Bi, Kai Zhang, Chen Ziwen, Sihan Xu, Jianing Yang, Zexiang Xu, Kalyan Sunkavalli, Mohit Bansal, Joyce Chai, Hao Tan*  
  `2025-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2506.18890) · [pdf](https://arxiv.org/pdf/2506.18890.pdf)
  > 💡 从任意视角和时间输入重建任意视角时间，提出4D-LRM用4D高斯原语统一时空表示，实现高效高质量渲染。

  <details><summary>Abstract</summary>

  Can we scale 4D pretraining to learn general space-time representations that reconstruct an object from a few views at some times to any view at any time? We provide an affirmative answer with 4D-LRM, the first large-scale 4D reconstruction model that takes input from unconstrained views and timestamps and renders arbitrary novel view-time combinations. Unlike prior 4D approaches, e.g., optimization-based, geometry-based, or generative, that struggle with efficiency, generalization, or faithfulness, 4D-LRM learns a unified space-time representation and directly predicts per-pixel 4D Gaussian primitives from posed image tokens across time, enabling fast, high-quality rendering at, in principle, infinite frame rate. Our results demonstrate that scaling spatiotemporal pretraining enables accurate and efficient 4D reconstruction. We show that 4D-LRM generalizes to novel objects, interpolates across time, and handles diverse camera setups. It reconstructs 24-frame sequences in one forward pass with less than 1.5 seconds on a single A100 GPU.

  </details>


- **[BulletGen: Improving 4D Reconstruction with Bullet-Time Generation](https://arxiv.org/abs/2506.18601)**  
  *Denis Rozumny, Jonathon Luiten, Numair Khan, Johannes Schönberger, Peter Kontschieder*  
  `2025-06-23` · `cs.GR` · [abs](https://arxiv.org/abs/2506.18601) · [pdf](https://arxiv.org/pdf/2506.18601.pdf)
  > 💡 利用扩散模型对齐子弹时间步骤监督4D高斯优化，修复单目视频动态重建中的缺失与错误，在新视图合成和跟踪任务上取得最优。

  <details><summary>Abstract</summary>

  Transforming casually captured, monocular videos into fully immersive dynamic experiences is a highly ill-posed task, and comes with significant challenges, e.g., reconstructing unseen regions, and dealing with the ambiguity in monocular depth estimation. In this work we introduce BulletGen, an approach that takes advantage of generative models to correct errors and complete missing information in a Gaussian-based dynamic scene representation. This is done by aligning the output of a diffusion-based video generation model with the 4D reconstruction at a single frozen "bullet-time" step. The generated frames are then used to supervise the optimization of the 4D Gaussian model. Our method seamlessly blends generative content with both static and dynamic scene components, achieving state-of-the-art results on both novel-view synthesis, and 2D/3D tracking tasks.

  </details>


- **[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](https://arxiv.org/abs/2506.08015)**  
  *Zhen Xu, Zhengqin Li, Zhao Dong, Xiaowei Zhou, Richard Newcombe, Zhaoyang Lv*  
  `2025-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2506.08015) · [pdf](https://arxiv.org/pdf/2506.08015.pdf)
  > 💡 使用4D高斯作为归纳偏置的Transformer模型，通过密度控制和滚动窗口处理，将动态场景重建从小时级缩短至秒级，性能优于现有方法。

  <details><summary>Abstract</summary>

  We propose 4DGT, a 4D Gaussian-based Transformer model for dynamic scene reconstruction, trained entirely on real-world monocular posed videos. Using 4D Gaussian as an inductive bias, 4DGT unifies static and dynamic components, enabling the modeling of complex, time-varying environments with varying object lifespans. We proposed a novel density control strategy in training, which enables our 4DGT to handle longer space-time input and remain efficient rendering at runtime. Our model processes 64 consecutive posed frames in a rolling-window fashion, predicting consistent 4D Gaussians in the scene. Unlike optimization-based methods, 4DGT performs purely feed-forward inference, reducing reconstruction time from hours to seconds and scaling effectively to long video sequences. Trained only on large-scale monocular posed video datasets, 4DGT can outperform prior Gaussian-based networks significantly in real-world videos and achieve on-par accuracy with optimization-based methods on cross-domain videos. Project page: https://4dgt.github.io

  </details>


- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471)**  
  *Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula*  
  `2025-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2505.20471) · [pdf](https://arxiv.org/pdf/2505.20471.pdf)
  > 💡 提出WeatherEdit，结合全适配器与4D高斯场，实现3D场景中可控类型和强度的逼真天气编辑，用于自动驾驶模拟。

  <details><summary>Abstract</summary>

  In this work, we present WeatherEdit, a novel weather editing pipeline for generating realistic weather effects with controllable types and severity in 3D scenes. Our approach is structured into two key components: weather background editing and weather particle construction. For weather background editing, we introduce an all-in-one adapter that integrates multiple weather styles into a single pretrained diffusion model, enabling the generation of diverse weather effects in 2D image backgrounds. During inference, we design a Temporal-View (TV-) attention mechanism that follows a specific order to aggregate temporal and spatial information, ensuring consistent editing across multi-frame and multi-view images. To construct the weather particles, we first reconstruct a 3D scene using the edited images and then introduce a dynamic 4D Gaussian field to generate snowflakes, raindrops and fog in the scene. The attributes and dynamics of these particles are precisely controlled through physical-based modelling and simulation, ensuring realistic weather representation and flexible severity adjustments. Finally, we integrate the 4D Gaussian field with the 3D scene to render consistent and highly realistic weather effects. Experiments on multiple driving datasets demonstrate that WeatherEdit can generate diverse weather effects with controllable condition severity, highlighting its potential for autonomous driving simulation in adverse weather. See project page: https://jumponthemoon.github.io/w-edit

  </details>


- **[CTRL-GS: Cascaded Temporal Residue Learning for 4D Gaussian Splatting](https://arxiv.org/abs/2505.18306)**  
  *Karly Hou, Wanhua Li, Hanspeter Pfister*  
  `2025-05-23` · `cs.CV` · [abs](https://arxiv.org/abs/2505.18306) · [pdf](https://arxiv.org/pdf/2505.18306.pdf)
  > 💡 将动态场景分解为视频-片段-帧结构并利用残差学习建模，实现4D高斯泼溅的实时渲染与最优视觉质量。

  <details><summary>Abstract</summary>

  Recently, Gaussian Splatting methods have emerged as a desirable substitute for prior Radiance Field methods for novel-view synthesis of scenes captured with multi-view images or videos. In this work, we propose a novel extension to 4D Gaussian Splatting for dynamic scenes. Drawing on ideas from residual learning, we hierarchically decompose the dynamic scene into a "video-segment-frame" structure, with segments dynamically adjusted by optical flow. Then, instead of directly predicting the time-dependent signals, we model the signal as the sum of video-constant values, segment-constant values, and frame-specific residuals, as inspired by the success of residual learning. This approach allows more flexible models that adapt to highly variable scenes. We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets, with the greatest improvements on complex scenes with large movements, occlusions, and fine details, where current methods degrade most.

  </details>


- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535)**  
  *Asrar Alruwayqi*  
  `2025-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2505.16535) · [pdf](https://arxiv.org/pdf/2505.16535.pdf)
  > 💡 使用三平面变形场和球谐注意力渲染，结合潜在扩散先验实现紧凑一致的动态三维重建，显著提升稀疏视图下的质量与鲁棒性。

  <details><summary>Abstract</summary>

  We present a novel framework for dynamic 3D scene reconstruction that integrates three key components: an explicit tri-plane deformation field, a view-conditioned canonical radiance field with spherical harmonics (SH) attention, and a temporally-aware latent diffusion prior. Our method encodes 4D scenes using three orthogonal 2D feature planes that evolve over time, enabling efficient and compact spatiotemporal representation. These features are explicitly warped into a canonical space via a deformation offset field, eliminating the need for MLP-based motion modeling. In canonical space, we replace traditional MLP decoders with a structured SH-based rendering head that synthesizes view-dependent color via attention over learned frequency bands improving both interpretability and rendering efficiency. To further enhance fidelity and temporal consistency, we introduce a transformer-guided latent diffusion module that refines the tri-plane and deformation features in a compressed latent space. This generative module denoises scene representations under ambiguous or out-of-distribution (OOD) motion, improving generalization. Our model is trained in two stages: the diffusion module is first pre-trained independently, and then fine-tuned jointly with the full pipeline using a combination of image reconstruction, diffusion denoising, and temporal consistency losses. We demonstrate state-of-the-art results on synthetic benchmarks, surpassing recent methods such as HexPlane and 4D Gaussian Splatting in visual quality, temporal coherence, and robustness to sparse-view dynamic inputs.

  </details>


- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215)**  
  *Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park*  
  `2025-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2505.13215) · [pdf](https://arxiv.org/pdf/2505.13215.pdf)
  > 💡 针对动态场景中4D高斯冗余问题，提出混合3D-4D高斯表示，迭代转换静态区域，降低计算开销并加速训练。

  <details><summary>Abstract</summary>

  Recent advancements in dynamic 3D scene reconstruction have shown promising results, enabling high-fidelity 3D novel view synthesis with improved temporal consistency. Among these, 4D Gaussian Splatting (4DGS) has emerged as an appealing approach due to its ability to model high-fidelity spatial and temporal variations. However, existing methods suffer from substantial computational and memory overhead due to the redundant allocation of 4D Gaussians to static regions, which can also degrade image quality. In this work, we introduce hybrid 3D-4D Gaussian Splatting (3D-4DGS), a novel framework that adaptively represents static regions with 3D Gaussians while reserving 4D Gaussians for dynamic elements. Our method begins with a fully 4D Gaussian representation and iteratively converts temporally invariant Gaussians into 3D, significantly reducing the number of parameters and improving computational efficiency. Meanwhile, dynamic Gaussians retain their full 4D representation, capturing complex motions with high fidelity. Our approach achieves significantly faster training times compared to baseline 4D Gaussian Splatting methods while maintaining or improving the visual quality.

  </details>


- **[ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.08196)**  
  *He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li*  
  `2025-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2505.08196) · [pdf](https://arxiv.org/pdf/2505.08196.pdf)
  > 💡 针对动态场景重建中高斯原语冗余，提出锚定驱动变形压缩GS，结合分层运动捕获与率失真优化，渲染速度提升300%-800%且存储高效。

  <details><summary>Abstract</summary>

  Existing 4D Gaussian Splatting methods rely on per-Gaussian deformation from a canonical space to target frames, which overlooks redundancy among adjacent Gaussian primitives and results in suboptimal performance. To address this limitation, we propose Anchor-Driven Deformable and Compressed Gaussian Splatting (ADC-GS), a compact and efficient representation for dynamic scene reconstruction. Specifically, ADC-GS organizes Gaussian primitives into an anchor-based structure within the canonical space, enhanced by a temporal significance-based anchor refinement strategy. To reduce deformation redundancy, ADC-GS introduces a hierarchical coarse-to-fine pipeline that captures motions at varying granularities. Moreover, a rate-distortion optimization is adopted to achieve an optimal balance between bitrate consumption and representation fidelity. Experimental results demonstrate that ADC-GS outperforms the per-Gaussian deformation approaches in rendering speed by 300%-800% while achieving state-of-the-art storage efficiency without compromising rendering quality. The code is released at https://github.com/H-Huang774/ADC-GS.git.

  </details>


- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539)**  
  *Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao*  
  `2025-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2505.07539) · [pdf](https://arxiv.org/pdf/2505.07539.pdf)
  > 💡 使用规范空间和变形场结合时间特征流，实现30Mbps高质沉浸视频实时渲染与快速解码。

  <details><summary>Abstract</summary>

  Immersive video offers a 6-Dof-free viewing experience, potentially playing a key role in future video technology. Recently, 4D Gaussian Splatting has gained attention as an effective approach for immersive video due to its high rendering efficiency and quality, though maintaining quality with manageable storage remains challenging. To address this, we introduce GIFStream, a novel 4D Gaussian representation using a canonical space and a deformation field enhanced with time-dependent feature streams. These feature streams enable complex motion modeling and allow efficient compression by leveraging temporal correspondence and motion-aware pruning. Additionally, we incorporate both temporal and spatial compression networks for end-to-end compression. Experimental results show that GIFStream delivers high-quality immersive video at 30 Mbps, with real-time rendering and fast decoding on an RTX 4090. Project page: https://xdimlab.github.io/GIFStream

  </details>


- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650)**  
  *Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan*  
  `2025-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2504.21650) · [pdf](https://arxiv.org/pdf/2504.21650.pdf)
  > 💡 提出HoloTime，用视频扩散模型生成全景视频，结合时空深度估计与4D高斯泼溅重建一致性4D场景。

  <details><summary>Abstract</summary>

  The rapid advancement of diffusion models holds the promise of revolutionizing the application of VR and AR technologies, which typically require scene-level 4D assets for user experience. Nonetheless, existing diffusion models predominantly concentrate on modeling static 3D scenes or object-level dynamics, constraining their capacity to provide truly immersive experiences. To address this issue, we propose HoloTime, a framework that integrates video diffusion models to generate panoramic videos from a single prompt or reference image, along with a 360-degree 4D scene reconstruction method that seamlessly transforms the generated panoramic video into 4D assets, enabling a fully immersive 4D experience for users. Specifically, to tame video diffusion models for generating high-fidelity panoramic videos, we introduce the 360World dataset, the first comprehensive collection of panoramic videos suitable for downstream 4D scene reconstruction tasks. With this curated dataset, we propose Panoramic Animator, a two-stage image-to-video diffusion model that can convert panoramic images into high-quality panoramic videos. Following this, we present Panoramic Space-Time Reconstruction, which leverages a space-time depth estimation method to transform the generated panoramic videos into 4D point clouds, enabling the optimization of a holistic 4D Gaussian Splatting representation to reconstruct spatially and temporally consistent 4D scenes. To validate the efficacy of our method, we conducted a comparative analysis with existing approaches, revealing its superiority in both panoramic video generation and 4D scene reconstruction. This demonstrates our method's capability to create more engaging and realistic immersive environments, thereby enhancing user experiences in VR and AR applications.

  </details>


- **[4DGS-CC: A Contextual Coding Framework for 4D Gaussian Splatting Data Compression](https://arxiv.org/abs/2504.18925)**  
  *Zicong Chen, Zhenghao Chen, Wei Jiang, Wei Wang, Lei Liu, Dong Xu*  
  `2025-04-26` · `cs.CE` · [abs](https://arxiv.org/abs/2504.18925) · [pdf](https://arxiv.org/pdf/2504.18925.pdf)
  > 💡 针对4DGS数据存储挑战，提出上下文编码框架，通过NVCC和VQCC分解压缩4D神经体素与规范3DGS，实现约12倍存储缩减且保持渲染质量。

  <details><summary>Abstract</summary>

  Storage is a significant challenge in reconstructing dynamic scenes with 4D Gaussian Splatting (4DGS) data. In this work, we introduce 4DGS-CC, a contextual coding framework that compresses 4DGS data to meet specific storage constraints. Building upon the established deformable 3D Gaussian Splatting (3DGS) method, our approach decomposes 4DGS data into 4D neural voxels and a canonical 3DGS component, which are then compressed using Neural Voxel Contextual Coding (NVCC) and Vector Quantization Contextual Coding (VQCC), respectively. Specifically, we first decompose the 4D neural voxels into distinct quantized features by separating the temporal and spatial dimensions. To losslessly compress each quantized feature, we leverage the previously compressed features from the temporal and spatial dimensions as priors and apply NVCC to generate the spatiotemporal context for contextual coding. Next, we employ a codebook to store spherical harmonics information from canonical 3DGS as quantized vectors, which are then losslessly compressed by using VQCC with the auxiliary learned hyperpriors for contextual coding, thereby reducing redundancy within the codebook. By integrating NVCC and VQCC, our contextual coding framework, 4DGS-CC, enables multi-rate 4DGS data compression tailored to specific storage requirements. Extensive experiments on three 4DGS data compression benchmarks demonstrate that our method achieves an average storage reduction of approximately 12 times while maintaining rendering fidelity compared to our baseline 4DGS approach.

  </details>


- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318)**  
  *Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu*  
  `2025-04-25` · `cs.CV` · [abs](https://arxiv.org/abs/2504.18318) · [pdf](https://arxiv.org/pdf/2504.18318.pdf)
  > 💡 现有方法缺乏时空-提示一致性导致4D生成质量低，提出时变提示嵌入、几何增强和时域变形模块，首个扩散模型生成4D高斯，实现高质量高效生成（约4.6s/资产）。

  <details><summary>Abstract</summary>

  Text-to-4D generation is rapidly developing and widely applied in various scenarios. However, existing methods often fail to incorporate adequate spatio-temporal modeling and prompt alignment within a unified framework, resulting in temporal inconsistencies, geometric distortions, or low-quality 4D content that deviates from the provided texts. Therefore, we propose STP4D, a novel approach that aims to integrate comprehensive spatio-temporal-prompt consistency modeling for high-quality text-to-4D generation. Specifically, STP4D employs three carefully designed modules: Time-varying Prompt Embedding, Geometric Information Enhancement, and Temporal Extension Deformation, which collaborate to accomplish this goal. Furthermore, STP4D is among the first methods to exploit the Diffusion model to generate 4D Gaussians, combining the fine-grained modeling capabilities and the real-time rendering process of 4DGS with the rapid inference speed of the Diffusion model. Extensive experiments demonstrate that STP4D excels in generating high-fidelity 4D content with exceptional efficiency (approximately 4.6s per asset), surpassing existing methods in both quality and speed.

  </details>


- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844)**  
  *Zhicong Sun, Jacqueline Lo, Jinxing Hu*  
  `2025-04-07` · `cs.RO` · [abs](https://arxiv.org/abs/2504.04844) · [pdf](https://arxiv.org/pdf/2504.04844.pdf)
  > 💡 首个基于4DGS动态场景表示的SLAM，用动力学感知模块滤除不稳定点并施加各向同性正则化，提升了跟踪与建图质量。

  <details><summary>Abstract</summary>

  Simultaneous localization and mapping (SLAM) technology has recently achieved photorealistic mapping capabilities thanks to the real-time, high-fidelity rendering enabled by 3D Gaussian Splatting (3DGS). However, due to the static representation of scenes, current 3DGS-based SLAM encounters issues with pose drift and failure to reconstruct accurate maps in dynamic environments. To address this problem, we present D4DGS-SLAM, the first SLAM method based on 4DGS map representation for dynamic environments. By incorporating the temporal dimension into scene representation, D4DGS-SLAM enables high-quality reconstruction of dynamic scenes. Utilizing the dynamics-aware InfoModule, we can obtain the dynamics, visibility, and reliability of scene points, and filter out unstable dynamic points for tracking accordingly. When optimizing Gaussian points, we apply different isotropic regularization terms to Gaussians with varying dynamic characteristics. Experimental results on real-world dynamic scene datasets demonstrate that our method outperforms state-of-the-art approaches in both camera pose tracking and map quality.

  </details>


- **[Optimizing 4D Gaussians for Dynamic Scene Video from Single Landscape Images](https://arxiv.org/abs/2504.05458)**  
  *In-Hwan Jin, Haesoo Choo, Seong-Hun Jeong, Heemoon Park, Junghwan Kim, Oh-joon Kwon, Kyeongbo Kong*  
  `2025-04-04` · `cs.CV` · [abs](https://arxiv.org/abs/2504.05458) · [pdf](https://arxiv.org/pdf/2504.05458.pdf)
  > 💡 针对单图动画深度感和视角缺陷，提出4D高斯优化完整3D空间，通过多视图生成和一致运动估计实现动态场景视频。

  <details><summary>Abstract</summary>

  To achieve realistic immersion in landscape images, fluids such as water and clouds need to move within the image while revealing new scenes from various camera perspectives. Recently, a field called dynamic scene video has emerged, which combines single image animation with 3D photography. These methods use pseudo 3D space, implicitly represented with Layered Depth Images (LDIs). LDIs separate a single image into depth-based layers, which enables elements like water and clouds to move within the image while revealing new scenes from different camera perspectives. However, as landscapes typically consist of continuous elements, including fluids, the representation of a 3D space separates a landscape image into discrete layers, and it can lead to diminished depth perception and potential distortions depending on camera movement. Furthermore, due to its implicit modeling of 3D space, the output may be limited to videos in the 2D domain, potentially reducing their versatility. In this paper, we propose representing a complete 3D space for dynamic scene video by modeling explicit representations, specifically 4D Gaussians, from a single image. The framework is focused on optimizing 3D Gaussians by generating multi-view images from a single image and creating 3D motion to optimize 4D Gaussians. The most important part of proposed framework is consistent 3D motion estimation, which estimates common motion among multi-view images to bring the motion in 3D space closer to actual motions. As far as we know, this is the first attempt that considers animation while representing a complete 3D space from a single landscape image. Our model demonstrates the ability to provide realistic immersion in various landscape images through diverse experiments and metrics. Extensive experimental results are https://cvsp-lab.github.io/ICLR2025_3D-MOM/.

  </details>


- **[Divide-and-Conquer: Dual-Hierarchical Optimization for Semantic 4D Gaussian Spatting](https://arxiv.org/abs/2503.19332)**  
  *Zhiying Yan, Yiyuan Liang, Shilv Cai, Tao Zhang, Sheng Zhong, Luxin Yan, Xu Zou*  
  `2025-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2503.19332) · [pdf](https://arxiv.org/pdf/2503.19332.pdf)
  > 💡 针对语义4D高斯泼溅中动静部分混同导致伪影的问题，提出分治双层次优化，用层次化高斯流与引导实现有效划分，显著提升动态场景

  <details><summary>Abstract</summary>

  Semantic 4D Gaussians can be used for reconstructing and understanding dynamic scenes, with temporal variations than static scenes. Directly applying static methods to understand dynamic scenes will fail to capture the temporal features. Few works focus on dynamic scene understanding based on Gaussian Splatting, since once the same update strategy is employed for both dynamic and static parts, regardless of the distinction and interaction between Gaussians, significant artifacts and noise appear. We propose Dual-Hierarchical Optimization (DHO), which consists of Hierarchical Gaussian Flow and Hierarchical Gaussian Guidance in a divide-and-conquer manner. The former implements effective division of static and dynamic rendering and features. The latter helps to mitigate the issue of dynamic foreground rendering distortion in textured complex scenes. Extensive experiments show that our method consistently outperforms the baselines on both synthetic and real-world datasets, and supports various downstream tasks. Project Page: https://sweety-yan.github.io/DHO.

  </details>


- **[4DGC: Rate-Aware 4D Gaussian Compression for Efficient Streamable Free-Viewpoint Video](https://arxiv.org/abs/2503.18421)**  
  *Qiang Hu, Zihan Zheng, Houqiang Zhong, Sihua Fu, Li Song, XiaoyunZhang, Guangtao Zhai, Yanfeng Wang*  
  `2025-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2503.18421) · [pdf](https://arxiv.org/pdf/2503.18421.pdf)
  > 💡 针对动态3DGS存储传输挑战，提出运动感知动态高斯表示与率失真联合优化压缩框架，显著降低存储且优于现有方法。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has substantial potential for enabling photorealistic Free-Viewpoint Video (FVV) experiences. However, the vast number of Gaussians and their associated attributes poses significant challenges for storage and transmission. Existing methods typically handle dynamic 3DGS representation and compression separately, neglecting motion information and the rate-distortion (RD) trade-off during training, leading to performance degradation and increased model redundancy. To address this gap, we propose 4DGC, a novel rate-aware 4D Gaussian compression framework that significantly reduces storage size while maintaining superior RD performance for FVV. Specifically, 4DGC introduces a motion-aware dynamic Gaussian representation that utilizes a compact motion grid combined with sparse compensated Gaussians to exploit inter-frame similarities. This representation effectively handles large motions, preserving quality and reducing temporal redundancy. Furthermore, we present an end-to-end compression scheme that employs differentiable quantization and a tiny implicit entropy model to compress the motion grid and compensated Gaussians efficiently. The entire framework is jointly optimized using a rate-distortion trade-off. Extensive experiments demonstrate that 4DGC supports variable bitrates and consistently outperforms existing methods in RD performance across multiple datasets.

  </details>


- **[4D Gaussian Splatting SLAM](https://arxiv.org/abs/2503.16710)**  
  *Yanyan Li, Youxu Fang, Zunjie Zhu, Kunyi Li, Yong Ding, Federico Tombari*  
  `2025-03-20` · `cs.CV` · [abs](https://arxiv.org/abs/2503.16710) · [pdf](https://arxiv.org/pdf/2503.16710.pdf)
  > 💡 在动态场景中分类静态与动态高斯，结合控制点与光流监督，实现鲁棒跟踪与高质量视图合成。

  <details><summary>Abstract</summary>

  Simultaneously localizing camera poses and constructing Gaussian radiance fields in dynamic scenes establish a crucial bridge between 2D images and the 4D real world. Instead of removing dynamic objects as distractors and reconstructing only static environments, this paper proposes an efficient architecture that incrementally tracks camera poses and establishes the 4D Gaussian radiance fields in unknown scenarios by using a sequence of RGB-D images. First, by generating motion masks, we obtain static and dynamic priors for each pixel. To eliminate the influence of static scenes and improve the efficiency on learning the motion of dynamic objects, we classify the Gaussian primitives into static and dynamic Gaussian sets, while the sparse control points along with an MLP is utilized to model the transformation fields of the dynamic Gaussians. To more accurately learn the motion of dynamic Gaussians, a novel 2D optical flow map reconstruction algorithm is designed to render optical flows of dynamic objects between neighbor images, which are further used to supervise the 4D Gaussian radiance fields along with traditional photometric and geometric constraints. In experiments, qualitative and quantitative evaluation results show that the proposed method achieves robust tracking and high-quality view synthesis performance in real-world environments.

  </details>


- **[1000+ FPS 4D Gaussian Splatting for Dynamic Scene Rendering](https://arxiv.org/abs/2503.16422)**  
  *Yuheng Yuan, Qiuhong Shen, Xingyi Yang, Xinchao Wang*  
  `2025-03-20` · `cs.CV` · [abs](https://arxiv.org/abs/2503.16422) · [pdf](https://arxiv.org/pdf/2503.16422.pdf)
  > 💡 针对4DGS存储大渲染慢，用时空变化分数剪枝短寿命高斯和活跃掩码减少冗余，实现1000+ FPS。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting (4DGS) has recently gained considerable attention as a method for reconstructing dynamic scenes. Despite achieving superior quality, 4DGS typically requires substantial storage and suffers from slow rendering speed. In this work, we delve into these issues and identify two key sources of temporal redundancy. (Q1) \textbf{Short-Lifespan Gaussians}: 4DGS uses a large portion of Gaussians with short temporal span to represent scene dynamics, leading to an excessive number of Gaussians. (Q2) \textbf{Inactive Gaussians}: When rendering, only a small subset of Gaussians contributes to each frame. Despite this, all Gaussians are processed during rasterization, resulting in redundant computation overhead. To address these redundancies, we present \textbf{4DGS-1K}, which runs at over 1000 FPS on modern GPUs. For Q1, we introduce the Spatial-Temporal Variation Score, a new pruning criterion that effectively removes short-lifespan Gaussians while encouraging 4DGS to capture scene dynamics using Gaussians with longer temporal spans. For Q2, we store a mask for active Gaussians across consecutive frames, significantly reducing redundant computations in rendering. Compared to vanilla 4DGS, our method achieves a $41\times$ reduction in storage and $9\times$ faster rasterization speed on complex dynamic scenes, while maintaining comparable visual quality. Please see our project page at https://4DGS-1K.github.io.

  </details>


- **[Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model](https://arxiv.org/abs/2503.13948)**  
  *Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu*  
  `2025-03-18` · `cs.CV` · [abs](https://arxiv.org/abs/2503.13948) · [pdf](https://arxiv.org/pdf/2503.13948.pdf)
  > 💡 针对4DGS存储开销大，提出时空显著性剪枝与深度上下文模型，实现120倍压缩并提升渲染速度。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as an efficient and high-fidelity paradigm for novel view synthesis. To adapt 3DGS for dynamic content, deformable 3DGS incorporates temporally deformable primitives with learnable latent embeddings to capture complex motions. Despite its impressive performance, the high-dimensional embeddings and vast number of primitives lead to substantial storage requirements. In this paper, we introduce a \textbf{Light}weight \textbf{4}D\textbf{GS} framework, called Light4GS, that employs significance pruning with a deep context model to provide a lightweight storage-efficient dynamic 3DGS representation. The proposed Light4GS is based on 4DGS that is a typical representation of deformable 3DGS. Specifically, our framework is built upon two core components: (1) a spatio-temporal significance pruning strategy that eliminates over 64\% of the deformable primitives, followed by an entropy-constrained spherical harmonics compression applied to the remainder; and (2) a deep context model that integrates intra- and inter-prediction with hyperprior into a coarse-to-fine context structure to enable efficient multiscale latent embedding compression. Our approach achieves over 120x compression and increases rendering FPS up to 20\% compared to the baseline 4DGS, and also superior to frame-wise state-of-the-art 3DGS compression methods, revealing the effectiveness of our Light4GS in terms of both intra- and inter-prediction methods without sacrificing rendering quality.

  </details>


- **[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](https://arxiv.org/abs/2503.07946)**  
  *Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu*  
  `2025-03-11` · `cs.CV` · [abs](https://arxiv.org/abs/2503.07946) · [pdf](https://arxiv.org/pdf/2503.07946.pdf)
  > 💡 针对动态场景和视角依赖效果缺乏统一方法的问题，提出7D高斯表示与条件切片机制，实现联合优化及实时高质量渲染，PSNR提升7.36 dB。

  <details><summary>Abstract</summary>

  Real-time rendering of dynamic scenes with view-dependent effects remains a fundamental challenge in computer graphics. While recent advances in Gaussian Splatting have shown promising results separately handling dynamic scenes (4DGS) and view-dependent effects (6DGS), no existing method unifies these capabilities while maintaining real-time performance. We present 7D Gaussian Splatting (7DGS), a unified framework representing scene elements as seven-dimensional Gaussians spanning position (3D), time (1D), and viewing direction (3D). Our key contribution is an efficient conditional slicing mechanism that transforms 7D Gaussians into view- and time-conditioned 3D Gaussians, maintaining compatibility with existing 3D Gaussian Splatting pipelines while enabling joint optimization. Experiments demonstrate that 7DGS outperforms prior methods by up to 7.36 dB in PSNR while achieving real-time rendering (401 FPS) on challenging dynamic scenes with complex view-dependent effects. The project page is: https://gaozhongpai.github.io/7dgs/.

  </details>


- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744)**  
  *Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll*  
  `2025-03-09` · `cs.CV` · [abs](https://arxiv.org/abs/2503.06744) · [pdf](https://arxiv.org/pdf/2503.06744.pdf)
  > 💡 针对自动驾驶动态场景渲染，提出上下文和变形感知的4DGS，利用语义自监督和时域变形跟踪提升动态表示精度。

  <details><summary>Abstract</summary>

  Dynamic scene rendering opens new avenues in autonomous driving by enabling closed-loop simulations with photorealistic data, which is crucial for validating end-to-end algorithms. However, the complex and highly dynamic nature of traffic environments presents significant challenges in accurately rendering these scenes. In this paper, we introduce a novel 4D Gaussian Splatting (4DGS) approach, which incorporates context and temporal deformation awareness to improve dynamic scene rendering. Specifically, we employ a 2D semantic segmentation foundation model to self-supervise the 4D semantic features of Gaussians, ensuring meaningful contextual embedding. Simultaneously, we track the temporal deformation of each Gaussian across adjacent frames. By aggregating and encoding both semantic and temporal deformation features, each Gaussian is equipped with cues for potential deformation compensation within 3D space, facilitating a more precise representation of dynamic scenes. Experimental results show that our method improves 4DGS's ability to capture fine details in dynamic scene rendering for autonomous driving and outperforms other self-supervised methods in 4D reconstruction and novel view synthesis. Furthermore, CoDa-4DGS deforms semantic features with each Gaussian, enabling broader applications.

  </details>


- **[Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction](https://arxiv.org/abs/2503.06161)**  
  *Kai Li, Junhao Wang, William Han, Ding Zhao*  
  `2025-03-08` · `cs.CV` · [abs](https://arxiv.org/abs/2503.06161) · [pdf](https://arxiv.org/pdf/2503.06161.pdf)
  > 💡 提出特征蒸馏4D高斯泼溅实现手术变形场景实时重建与语义分割，在渲染保真度与分割精度上达到最优。

  <details><summary>Abstract</summary>

  Minimally invasive surgery (MIS) requires high-fidelity, real-time visual feedback of dynamic and low-texture surgical scenes. To address these requirements, we introduce FeatureEndo-4DGS (FE-4DGS), the first real time pipeline leveraging feature-distilled 4D Gaussian Splatting for simultaneous reconstruction and semantic segmentation of deformable surgical environments. Unlike prior feature-distilled methods restricted to static scenes, and existing 4D approaches that lack semantic integration, FE-4DGS seamlessly leverages pre-trained 2D semantic embeddings to produce a unified 4D representation-where semantics also deform with tissue motion. This unified approach enables the generation of real-time RGB and semantic outputs through a single, parallelized rasterization process. Despite the additional complexity from feature distillation, FE-4DGS sustains real-time rendering (61 FPS) with a compact footprint, achieves state-of-the-art rendering fidelity on EndoNeRF (39.1 PSNR) and SCARED (27.3 PSNR), and delivers competitive EndoVis18 segmentation, matching or exceeding strong 2D baselines for binary segmentation tasks (0.93 DSC) and remaining competitive for multi-label segmentation (0.77 DSC).

  </details>


- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115)**  
  *Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang*  
  `2025-03-05` · `cs.CV` · [abs](https://arxiv.org/abs/2503.03115) · [pdf](https://arxiv.org/pdf/2503.03115.pdf)
  > 💡 针对夜间动态热重建，提出基于热力学和4DGS的NTR-Gaussian，用神经网络预测热力学参数，实现温度预测误差低于1°C。

  <details><summary>Abstract</summary>

  Thermal infrared imaging offers the advantage of all-weather capability, enabling non-intrusive measurement of an object's surface temperature. Consequently, thermal infrared images are employed to reconstruct 3D models that accurately reflect the temperature distribution of a scene, aiding in applications such as building monitoring and energy management. However, existing approaches predominantly focus on static 3D reconstruction for a single time period, overlooking the impact of environmental factors on thermal radiation and failing to predict or analyze temperature variations over time. To address these challenges, we propose the NTR-Gaussian method, which treats temperature as a form of thermal radiation, incorporating elements like convective heat transfer and radiative heat dissipation. Our approach utilizes neural networks to predict thermodynamic parameters such as emissivity, convective heat transfer coefficient, and heat capacity. By integrating these predictions, we can accurately forecast thermal temperatures at various times throughout a nighttime scene. Furthermore, we introduce a dynamic dataset specifically for nighttime thermal imagery. Extensive experiments and evaluations demonstrate that NTR-Gaussian significantly outperforms comparison methods in thermal reconstruction, achieving a predicted temperature error within 1 degree Celsius.

  </details>


- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941)**  
  *Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang*  
  `2025-02-24` · `cs.CV` · [abs](https://arxiv.org/abs/2502.16941) · [pdf](https://arxiv.org/pdf/2502.16941.pdf)
  > 💡 利用4D高斯分布嵌入图像并对比实例ID，实现鲁棒的3D场景实例级变化检测，显著优于现有方法。

  <details><summary>Abstract</summary>

  Instance-level change detection in 3D scenes presents significant challenges, particularly in uncontrolled environments lacking labeled image pairs, consistent camera poses, or uniform lighting conditions. This paper addresses these challenges by introducing a novel approach for detecting changes in real-world scenarios. Our method leverages 4D Gaussians to embed multiple images into Gaussian distributions, enabling the rendering of two coherent image sequences. We segment each image and assign unique identifiers to instances, facilitating efficient change detection through ID comparison. Additionally, we utilize change maps and classification encodings to categorize 4D Gaussians as changed or unchanged, allowing for the rendering of comprehensive change maps from any viewpoint. Extensive experiments across various instance-level change detection datasets demonstrate that our method significantly outperforms state-of-the-art approaches like C-NERF and CYWS-3D, especially in scenarios with substantial lighting variations. Our approach offers improved detection accuracy, robustness to lighting changes, and efficient processing times, advancing the field of 3D change detection.

  </details>


- **[Efficient 4D Gaussian Stream with Low Rank Adaptation](https://arxiv.org/abs/2502.16575)**  
  *Zhenhuan Liu, Shuai Liu, Yidong Lu, Yirui Chen, Jie Yang, Wei Liu*  
  `2025-02-23` · `cs.CV` · [abs](https://arxiv.org/abs/2502.16575) · [pdf](https://arxiv.org/pdf/2502.16575.pdf)
  > 💡 利用3D高斯和低秩自适应模型进行动态场景连续学习，减少90%流带宽并保持高渲染质量。

  <details><summary>Abstract</summary>

  Recent methods have made significant progress in synthesizing novel views with long video sequences. This paper proposes a highly scalable method for dynamic novel view synthesis with continual learning. We leverage the 3D Gaussians to represent the scene and a low-rank adaptation-based deformation model to capture the dynamic scene changes. Our method continuously reconstructs the dynamics with chunks of video frames, reduces the streaming bandwidth by $90\%$ while maintaining high rendering quality comparable to the off-line SOTA methods.

  </details>


- **[High-Dynamic Radar Sequence Prediction for Weather Nowcasting Using Spatiotemporal Coherent Gaussian Representation](https://arxiv.org/abs/2502.14895)**  
  *Ziye Wang, Yiran Qin, Lin Zeng, Ruimao Zhang*  
  `2025-02-17` · `cs.CV` · [abs](https://arxiv.org/abs/2502.14895) · [pdf](https://arxiv.org/pdf/2502.14895.pdf)
  > 💡 针对天气预测中3D雷达序列预测难题，提出时空一致高斯表示STC-GS与GauMamba，实现高效高分辨率动态表示与精准预测。

  <details><summary>Abstract</summary>

  Weather nowcasting is an essential task that involves predicting future radar echo sequences based on current observations, offering significant benefits for disaster management, transportation, and urban planning. Current prediction methods are limited by training and storage efficiency, mainly focusing on 2D spatial predictions at specific altitudes. Meanwhile, 3D volumetric predictions at each timestamp remain largely unexplored. To address such a challenge, we introduce a comprehensive framework for 3D radar sequence prediction in weather nowcasting, using the newly proposed SpatioTemporal Coherent Gaussian Splatting (STC-GS) for dynamic radar representation and GauMamba for efficient and accurate forecasting. Specifically, rather than relying on a 4D Gaussian for dynamic scene reconstruction, STC-GS optimizes 3D scenes at each frame by employing a group of Gaussians while effectively capturing their movements across consecutive frames. It ensures consistent tracking of each Gaussian over time, making it particularly effective for prediction tasks. With the temporally correlated Gaussian groups established, we utilize them to train GauMamba, which integrates a memory mechanism into the Mamba framework. This allows the model to learn the temporal evolution of Gaussian groups while efficiently handling a large volume of Gaussian tokens. As a result, it achieves both efficiency and accuracy in forecasting a wide range of dynamic meteorological radar signals. The experimental results demonstrate that our STC-GS can efficiently represent 3D radar sequences with over $16\times$ higher spatial resolution compared with the existing 3D representation methods, while GauMamba outperforms state-of-the-art methods in forecasting a broad spectrum of high-dynamic weather conditions.

  </details>


- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297)**  
  *Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu*  
  `2025-02-12` · `cs.GR` · [abs](https://arxiv.org/abs/2502.08297) · [pdf](https://arxiv.org/pdf/2502.08297.pdf)
  > 💡 引入4D高斯与物理渲染结合，通过粗到细优化恢复几何与PBR属性，实现高质量可重光照体积视频。

  <details><summary>Abstract</summary>

  Volumetric video enables immersive experiences by capturing dynamic 3D scenes, enabling diverse applications for virtual reality, education, and telepresence. However, traditional methods struggle with fixed lighting conditions, while neural approaches face trade-offs in efficiency, quality, or adaptability for relightable scenarios. To address these limitations, we present BEAM, a novel pipeline that bridges 4D Gaussian representations with physically-based rendering (PBR) to produce high-quality, relightable volumetric videos from multi-view RGB footage. BEAM recovers detailed geometry and PBR properties via a series of available Gaussian-based techniques. It first combines Gaussian-based human performance tracking with geometry-aware rasterization in a coarse-to-fine optimization framework to recover spatially and temporally consistent geometries. We further enhance Gaussian attributes by incorporating PBR properties step by step. We generate roughness via a multi-view-conditioned diffusion model, and then derive AO and base color using a 2D-to-3D strategy, incorporating a tailored Gaussian-based ray tracer for efficient visibility computation. Once recovered, these dynamic, relightable assets integrate seamlessly into traditional CG pipelines, supporting real-time rendering with deferred shading and offline rendering with ray tracing. By offering realistic, lifelike visualizations under diverse lighting conditions, BEAM opens new possibilities for interactive entertainment, storytelling, and creative visualization.

  </details>


- **[Instruct-4DGS: Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091)**  
  *Joohyun Kwon, Hanbyel Cho, Junmo Kim*  
  `2025-02-04` · `cs.CV` · [abs](https://arxiv.org/abs/2502.02091) · [pdf](https://arxiv.org/pdf/2502.02091.pdf)
  > 💡 利用4D高斯静态-动态分离表示仅编辑静态部分，配合分数蒸馏对齐，实现高效4D场景编辑，时间减半且质量高。

  <details><summary>Abstract</summary>

  Recent 4D dynamic scene editing methods require editing thousands of 2D images used for dynamic scene synthesis and updating the entire scene with additional training loops, resulting in several hours of processing to edit a single dynamic scene. Therefore, these methods are not scalable with respect to the temporal dimension of the dynamic scene (i.e., the number of timesteps). In this work, we propose Instruct-4DGS, an efficient dynamic scene editing method that is more scalable in terms of temporal dimension. To achieve computational efficiency, we leverage a 4D Gaussian representation that models a 4D dynamic scene by combining static 3D Gaussians with a Hexplane-based deformation field, which captures dynamic information. We then perform editing solely on the static 3D Gaussians, which is the minimal but sufficient component required for visual editing. To resolve the misalignment between the edited 3D Gaussians and the deformation field, which may arise from the editing process, we introduce a refinement stage using a score distillation mechanism. Extensive editing results demonstrate that Instruct-4DGS is efficient, reducing editing time by more than half compared to existing methods while achieving high-quality edits that better follow user instructions. Code and results: https://hanbyelcho.info/instruct-4dgs/

  </details>


- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978)**  
  *Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan*  
  `2025-01-17` · `cs.CV` · [abs](https://arxiv.org/abs/2501.09978) · [pdf](https://arxiv.org/pdf/2501.09978.pdf)
  > 💡 通过加权Alpha混合方程处理运动遮挡，条件对抗学习保证时空一致性，实现可动画4D高斯头像的真实感文本驱动编辑。

  <details><summary>Abstract</summary>

  We introduce GaussianAvatar-Editor, an innovative framework for text-driven editing of animatable Gaussian head avatars that can be fully controlled in expression, pose, and viewpoint. Unlike static 3D Gaussian editing, editing animatable 4D Gaussian avatars presents challenges related to motion occlusion and spatial-temporal inconsistency. To address these issues, we propose the Weighted Alpha Blending Equation (WABE). This function enhances the blending weight of visible Gaussians while suppressing the influence on non-visible Gaussians, effectively handling motion occlusion during editing. Furthermore, to improve editing quality and ensure 4D consistency, we incorporate conditional adversarial learning into the editing process. This strategy helps to refine the edited results and maintain consistency throughout the animation. By integrating these methods, our GaussianAvatar-Editor achieves photorealistic and consistent results in animatable 4D Gaussian editing. We conduct comprehensive experiments across various subjects to validate the effectiveness of our proposed techniques, which demonstrates the superiority of our approach over existing methods. More results and code are available at: [Project Link](https://xiangyueliu.github.io/GaussianAvatar-Editor/).

  </details>


- **[Spatiotemporal Gaussian Optimization for 4D Cone Beam CT Reconstruction from Sparse Projections](https://arxiv.org/abs/2501.04140)**  
  *Yabo Fu, Hao Zhang, Weixing Cai, Huiqiao Xie, Licheng Kuo, Laura Cervino, Jean Moran, Xiang Li, Tianfang Li*  
  `2025-01-07` · `physics.med-ph` · [abs](https://arxiv.org/abs/2501.04140) · [pdf](https://arxiv.org/pdf/2501.04140.pdf)
  > 💡 用时空高斯优化从稀疏投影重建4D锥束CT，平衡伪影消除、动态保留和细节恢复。

  <details><summary>Abstract</summary>

  In image-guided radiotherapy (IGRT), four-dimensional cone-beam computed tomography (4D-CBCT) is critical for assessing tumor motion during a patients breathing cycle prior to beam delivery. However, generating 4D-CBCT images with sufficient quality requires significantly more projection images than a standard 3D-CBCT scan, leading to extended scanning times and increased imaging dose to the patient. To address these limitations, there is a strong demand for methods capable of reconstructing high-quality 4D-CBCT images from a 1-minute 3D-CBCT acquisition. The challenge lies in the sparse sampling of projections, which introduces severe streaking artifacts and compromises image quality. This paper introduces a novel framework leveraging spatiotemporal Gaussian representation for 4D-CBCT reconstruction from sparse projections, achieving a balance between streak artifact reduction, dynamic motion preservation, and fine detail restoration. Each Gaussian is characterized by its 3D position, covariance, rotation, and density. Two-dimensional X-ray projection images can be rendered from the Gaussian point cloud representation via X-ray rasterization. The properties of each Gaussian were optimized by minimizing the discrepancy between the measured projections and the rendered X-ray projections. A Gaussian deformation network is jointly optimized to deform these Gaussian properties to obtain a 4D Gaussian representation for dynamic CBCT scene modeling. The final 4D-CBCT images are reconstructed by voxelizing the 4D Gaussians, achieving a high-quality representation that preserves both motion dynamics and spatial detail. The code and reconstruction results can be found at https://github.com/fuyabo/4DGS_for_4DCBCT/tree/main

  </details>


- **[GS-DiT: Advancing Video Generation with Pseudo 4D Gaussian Fields through Efficient Dense 3D Point Tracking](https://arxiv.org/abs/2501.02690)**  
  *Weikang Bian, Zhaoyang Huang, Xiaoyu Shi, Yijin Li, Fu-Yun Wang, Hongsheng Li*  
  `2025-01-05` · `cs.CV` · [abs](https://arxiv.org/abs/2501.02690) · [pdf](https://arxiv.org/pdf/2501.02690.pdf)
  > 💡 用伪4D高斯场和高效密集3D点跟踪赋予DiT视频生成4D可控性，支持镜头变换与创意制作。

  <details><summary>Abstract</summary>

  4D video control is essential in video generation as it enables the use of sophisticated lens techniques, such as multi-camera shooting and dolly zoom, which are currently unsupported by existing methods. Training a video Diffusion Transformer (DiT) directly to control 4D content requires expensive multi-view videos. Inspired by Monocular Dynamic novel View Synthesis (MDVS) that optimizes a 4D representation and renders videos according to different 4D elements, such as camera pose and object motion editing, we bring pseudo 4D Gaussian fields to video generation. Specifically, we propose a novel framework that constructs a pseudo 4D Gaussian field with dense 3D point tracking and renders the Gaussian field for all video frames. Then we finetune a pretrained DiT to generate videos following the guidance of the rendered video, dubbed as GS-DiT. To boost the training of the GS-DiT, we also propose an efficient Dense 3D Point Tracking (D3D-PT) method for the pseudo 4D Gaussian field construction. Our D3D-PT outperforms SpatialTracker, the state-of-the-art sparse 3D point tracking method, in accuracy and accelerates the inference speed by two orders of magnitude. During the inference stage, GS-DiT can generate videos with the same dynamic content while adhering to different camera parameters, addressing a significant limitation of current video generation models. GS-DiT demonstrates strong generalization capabilities and extends the 4D controllability of Gaussian splatting to video generation beyond just camera poses. It supports advanced cinematic effects through the manipulation of the Gaussian field and camera intrinsics, making it a powerful tool for creative video production. Demos are available at https://wkbian.github.io/Projects/GS-DiT/.

  </details>


- **[EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation](https://arxiv.org/abs/2501.01895)**  
  *Siyuan Huang, Liliang Chen, Pengfei Zhou, Shengcong Chen, Zhengkai Jiang, Yue Hu, Yue Liao, Peng Gao, Hongsheng Li, Maoqing Yao, Guanghui Ren*  
  `2025-01-03` · `cs.RO` · [abs](https://arxiv.org/abs/2501.01895) · [pdf](https://arxiv.org/pdf/2501.01895.pdf)
  > 💡 块式自回归视频扩散预测未来空间，融合多视角表示与4D高斯泼溅数据引擎，实现机器人操控SOTA性能。

  <details><summary>Abstract</summary>

  We introduce EnerVerse, a generative robotics foundation model that constructs and interprets embodied spaces. EnerVerse employs a chunk-wise autoregressive video diffusion framework to predict future embodied spaces from instructions, enhanced by a sparse context memory for long-term reasoning. To model the 3D robotics world, we adopt a multi-view video representation, providing rich perspectives to address challenges like motion ambiguity and 3D grounding. Additionally, EnerVerse-D, a data engine pipeline combining generative modeling with 4D Gaussian Splatting, forms a self-reinforcing data loop to reduce the sim-to-real gap. Leveraging these innovations, EnerVerse translates 4D world representations into physical actions via a policy head (EnerVerse-A), achieving state-of-the-art performance in both simulation and real-world tasks. For efficiency, EnerVerse-A reuses features from the first denoising step and predicts action chunks, achieving about 280 ms per 8-step action chunk on a single RTX 4090. Further video demos, dataset samples could be found in our project page.

  </details>


- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720)**  
  *Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Jianfeng Feng, Yu-Gang Jiang, Philip H. S. Torr*  
  `2024-12-30` · `cs.CV` · [abs](https://arxiv.org/abs/2412.20720) · [pdf](https://arxiv.org/pdf/2412.20720.pdf)
  > 💡 针对动态场景新视角合成难题，提出原生4D高斯原语建模时空体积，首次实现实时高分辨率逼真渲染并压缩内存。

  <details><summary>Abstract</summary>

  Dynamic 3D scene representation and novel view synthesis are crucial for enabling immersive experiences required by AR/VR and metaverse applications. It is a challenging task due to the complexity of unconstrained real-world scenes and their temporal dynamics. In this paper, we reformulate the reconstruction of a time-varying 3D scene as approximating its underlying spatiotemporal 4D volume by optimizing a collection of native 4D primitives, i.e., 4D Gaussians, with explicit geometry and appearance modeling. Equipped with a tailored rendering pipeline, our representation can be end-to-end optimized using only photometric supervision while free viewpoint viewing at interactive frame rate, making it suitable for representing real world scene with complex dynamic. This approach has been the first solution to achieve real-time rendering of high-resolution, photorealistic novel views for complex dynamic scenes. To facilitate real-world applications, we derive several compact variants that effectively reduce the memory footprint to address its storage bottleneck. Extensive experiments validate the superiority of 4DGS in terms of visual quality and efficiency across a range of dynamic scene-related tasks (e.g., novel view synthesis, 4D generation, scene understanding) and scenarios (e.g., single object, indoor scenes, driving environments, synthetic and real data).

  </details>


- **[Representing Long Volumetric Video with Temporal Gaussian Hierarchy](https://arxiv.org/abs/2412.09608)**  
  *Zhen Xu, Yinghao Xu, Zhiyuan Yu, Sida Peng, Jiaming Sun, Hujun Bao, Xiaowei Zhou*  
  `2024-12-12` · `cs.CV` · [abs](https://arxiv.org/abs/2412.09608) · [pdf](https://arxiv.org/pdf/2412.09608.pdf)
  > 💡 针对长体积视频重建的内存瓶颈，提出时序高斯层级表示，通过多级自适应共享原语，实现分钟级视频的高效低存储高质量渲染。

  <details><summary>Abstract</summary>

  This paper aims to address the challenge of reconstructing long volumetric videos from multi-view RGB videos. Recent dynamic view synthesis methods leverage powerful 4D representations, like feature grids or point cloud sequences, to achieve high-quality rendering results. However, they are typically limited to short (1~2s) video clips and often suffer from large memory footprints when dealing with longer videos. To solve this issue, we propose a novel 4D representation, named Temporal Gaussian Hierarchy, to compactly model long volumetric videos. Our key observation is that there are generally various degrees of temporal redundancy in dynamic scenes, which consist of areas changing at different speeds. Motivated by this, our approach builds a multi-level hierarchy of 4D Gaussian primitives, where each level separately describes scene regions with different degrees of content change, and adaptively shares Gaussian primitives to represent unchanged scene content over different temporal segments, thus effectively reducing the number of Gaussian primitives. In addition, the tree-like structure of the Gaussian hierarchy allows us to efficiently represent the scene at a particular moment with a subset of Gaussian primitives, leading to nearly constant GPU memory usage during the training or rendering regardless of the video length. Extensive experimental results demonstrate the superiority of our method over alternative methods in terms of training cost, rendering speed, and storage usage. To our knowledge, this work is the first approach capable of efficiently handling minutes of volumetric video data while maintaining state-of-the-art rendering quality. Our project page is available at: https://zju3dv.github.io/longvolcap.

  </details>


- **[DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving](https://arxiv.org/abs/2412.09043)**  
  *Hao Lu, Tianshuo Xu, Wenzhao Zheng, Yunpeng Zhang, Wei Zhan, Dalong Du, Masayoshi Tomizuka, Kurt Keutzer, Yingcong Chen*  
  `2024-12-12` · `cs.CV` · [abs](https://arxiv.org/abs/2412.09043) · [pdf](https://arxiv.org/pdf/2412.09043.pdf)
  > 💡 现有街景4D重建耗时长，提出DrivingRecon模型，用Prune and Dilate块和动静态解耦直接预测4D高斯，显著提升质量与效率。

  <details><summary>Abstract</summary>

  Photorealistic 4D reconstruction of street scenes is essential for developing real-world simulators in autonomous driving. However, most existing methods perform this task offline and rely on time-consuming iterative processes, limiting their practical applications. To this end, we introduce the Large 4D Gaussian Reconstruction Model (DrivingRecon), a generalizable driving scene reconstruction model, which directly predicts 4D Gaussian from surround view videos. To better integrate the surround-view images, the Prune and Dilate Block (PD-Block) is proposed to eliminate overlapping Gaussian points between adjacent views and remove redundant background points. To enhance cross-temporal information, dynamic and static decoupling is tailored to better learn geometry and motion features. Experimental results demonstrate that DrivingRecon significantly improves scene reconstruction quality and novel view synthesis compared to existing methods. Furthermore, we explore applications of DrivingRecon in model pre-training, vehicle adaptation, and scene editing. Our code is available at https://github.com/EnVision-Research/DriveRecon.

  </details>


- **[Deblur4DGS: 4D Gaussian Splatting from Blurry Monocular Video](https://arxiv.org/abs/2412.06424)**  
  *Renlong Wu, Zhilu Zhang, Mingyang Chen, Zifei Yan, Wangmeng Zuo*  
  `2024-12-09` · `cs.CV` · [abs](https://arxiv.org/abs/2412.06424) · [pdf](https://arxiv.org/pdf/2412.06424.pdf)
  > 💡 针对模糊单目视频，提出将动态估计转化为曝光时间估计并引入正则项与模糊感知高斯，实现高质量4D重建及多任务应用。

  <details><summary>Abstract</summary>

  Recent 4D reconstruction methods have yielded impressive results but rely on sharp videos as supervision. However, motion blur often occurs in videos due to camera shake and object movement, while existing methods render blurry results when using such videos for reconstructing 4D models. Although a few approaches attempted to address the problem, they struggled to produce high-quality results, due to the inaccuracy in estimating continuous dynamic representations within the exposure time. Encouraged by recent works in 3D motion trajectory modeling using 3D Gaussian Splatting (3DGS), we take 3DGS as the scene representation manner, and propose Deblur4DGS to reconstruct a high-quality 4D model from blurry monocular video. Specifically, we transform continuous dynamic representations estimation within an exposure time into the exposure time estimation. Moreover, we introduce the exposure regularization term, multi-frame, and multi-resolution consistency regularization term to avoid trivial solutions. Furthermore, to better represent objects with large motion, we suggest blur-aware variable canonical Gaussians. Beyond novel-view synthesis, Deblur4DGS can be applied to improve blurry video from multiple perspectives, including deblurring, frame interpolation, and video stabilization. Extensive experiments in both synthetic and real-world data on the above four tasks show that Deblur4DGS outperforms state-of-the-art 4D reconstruction methods. The codes are available at https://github.com/ZcsrenlongZ/Deblur4DGS.

  </details>


- **[4D Gaussian Splatting with Scale-aware Residual Field and Adaptive Optimization for Real-time Rendering of Temporally Complex Dynamic Scenes](https://arxiv.org/abs/2412.06299)**  
  *Jinbo Yan, Rui Peng, Luyang Tang, Ronggang Wang*  
  `2024-12-09` · `cs.CV` · [abs](https://arxiv.org/abs/2412.06299) · [pdf](https://arxiv.org/pdf/2412.06299.pdf)
  > 💡 针对动态场景渲染慢和时间复杂性难题，提出尺度感知残差场和自适应优化4D高斯溅射，实现实时渲染和最优性能。

  <details><summary>Abstract</summary>

  Reconstructing dynamic scenes from video sequences is a highly promising task in the multimedia domain. While previous methods have made progress, they often struggle with slow rendering and managing temporal complexities such as significant motion and object appearance/disappearance. In this paper, we propose SaRO-GS as a novel dynamic scene representation capable of achieving real-time rendering while effectively handling temporal complexities in dynamic scenes. To address the issue of slow rendering speed, we adopt a Gaussian primitive-based representation and optimize the Gaussians in 4D space, which facilitates real-time rendering with the assistance of 3D Gaussian Splatting. Additionally, to handle temporally complex dynamic scenes, we introduce a Scale-aware Residual Field. This field considers the size information of each Gaussian primitive while encoding its residual feature and aligns with the self-splitting behavior of Gaussian primitives. Furthermore, we propose an Adaptive Optimization Schedule, which assigns different optimization strategies to Gaussian primitives based on their distinct temporal properties, thereby expediting the reconstruction of dynamic regions. Through evaluations on monocular and multi-view datasets, our method has demonstrated state-of-the-art performance. Please see our project page at https://yjb6.github.io/SaRO-GS.github.io.

  </details>


- **[Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2412.05700)**  
  *Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann*  
  `2024-12-07` · `cs.CV` · [abs](https://arxiv.org/abs/2412.05700) · [pdf](https://arxiv.org/pdf/2412.05700.pdf)
  > 💡 针对动态场景高斯泼溅内存占用高问题，TC3DGS通过时间相关剪枝、混合精度量化和轨迹插值实现高达67倍压缩。

  <details><summary>Abstract</summary>

  Recent advancements in high-fidelity dynamic scene reconstruction have leveraged dynamic 3D Gaussians and 4D Gaussian Splatting for realistic scene representation. However, to make these methods viable for real-time applications such as AR/VR, gaming, and rendering on low-power devices, substantial reductions in memory usage and improvements in rendering efficiency are required. While many state-of-the-art methods prioritize lightweight implementations, they struggle in handling {scenes with complex motions or long sequences}. In this work, we introduce Temporally Compressed 3D Gaussian Splatting (TC3DGS), a novel technique designed specifically to effectively compress dynamic 3D Gaussian representations. TC3DGS selectively prunes Gaussians based on their temporal relevance and employs gradient-aware mixed-precision quantization to dynamically compress Gaussian parameters. In addition, TC3DGS exploits an adapted version of the Ramer-Douglas-Peucker algorithm to further reduce storage by interpolating Gaussian trajectories across frames. Our experiments on multiple datasets demonstrate that TC3DGS achieves up to 67$\times$ compression with minimal or no degradation in visual quality. More results and videos are provided in the supplementary. Project Page: https://ahmad-jarrar.github.io/tc-3dgs/

  </details>


- **[UrbanGS: Semantic-Guided Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473)**  
  *Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong*  
  `2024-12-04` · `cs.CV` · [abs](https://arxiv.org/abs/2412.03473) · [pdf](https://arxiv.org/pdf/2412.03473.pdf)
  > 💡 使用2D语义图区分静态与动态区域，通过全局一致性和KNN正则化优化静态，时间嵌入建模动态，实现高质量高效重建。

  <details><summary>Abstract</summary>

  Reconstructing urban scenes is challenging due to their complex geometries and the presence of potentially dynamic objects. 3D Gaussian Splatting (3DGS)-based methods have shown strong performance, but existing approaches often incorporate manual 3D annotations to improve dynamic object modeling, which is impractical due to high labeling costs. Some methods leverage 4D Gaussian Splatting (4DGS) to represent the entire scene, but they treat static and dynamic objects uniformly, leading to unnecessary updates for static elements and ultimately degrading reconstruction quality. To address these issues, we propose UrbanGS, which leverages 2D semantic maps and an existing dynamic Gaussian approach to distinguish static objects from the scene, enabling separate processing of definite static and potentially dynamic elements. Specifically, for definite static regions, we enforce global consistency to prevent unintended changes in dynamic Gaussian and introduce a K-nearest neighbor (KNN)-based regularization to improve local coherence on low-textured ground surfaces. Notably, for potentially dynamic objects, we aggregate temporal information using learnable time embeddings, allowing each Gaussian to model deformations over time. Extensive experiments on real-world datasets demonstrate that our approach outperforms state-of-the-art methods in reconstruction quality and efficiency, accurately preserving static content while capturing dynamic elements.

  </details>


- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684)**  
  *Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong*  
  `2024-12-03` · `cs.CV` · [abs](https://arxiv.org/abs/2412.02684) · [pdf](https://arxiv.org/pdf/2412.02684.pdf)
  > 💡 从单图生成可动画化人体头像，利用生成模型输出多视图规范姿态，结合4D高斯溅射处理不一致性，实现逼真实时动画。

  <details><summary>Abstract</summary>

  Generating animatable human avatars from a single image is essential for various digital human modeling applications. Existing 3D reconstruction methods often struggle to capture fine details in animatable models, while generative approaches for controllable animation, though avoiding explicit 3D modeling, suffer from viewpoint inconsistencies in extreme poses and computational inefficiencies. In this paper, we address these challenges by leveraging the power of generative models to produce detailed multi-view canonical pose images, which help resolve ambiguities in animatable human reconstruction. We then propose a robust method for 3D reconstruction of inconsistent images, enabling real-time rendering during inference. Specifically, we adapt a transformer-based video generation model to generate multi-view canonical pose images and normal maps, pretraining on a large-scale video dataset to improve generalization. To handle view inconsistencies, we recast the reconstruction problem as a 4D task and introduce an efficient 3D modeling approach using 4D Gaussian Splatting. Experiments demonstrate that our method achieves photorealistic, real-time animation of 3D human avatars from in-the-wild images, showcasing its effectiveness and generalization capability.

  </details>


- **[Gaussians on their Way: Wasserstein-Constrained 4D Gaussian Splatting with State-Space Modeling](https://arxiv.org/abs/2412.00333)**  
  *Junli Deng, Yihao Luo*  
  `2024-11-30` · `cs.CV` · [abs](https://arxiv.org/abs/2412.00333) · [pdf](https://arxiv.org/pdf/2412.00333.pdf)
  > 💡 融合状态空间建模与Wasserstein几何，通过状态一致性滤波和Wasserstein正则化实现4D高斯的平滑运动，提升动态场景渲染质量和效率。

  <details><summary>Abstract</summary>

  Dynamic scene rendering has taken a leap forward with the rise of 4D Gaussian Splatting, but there's still one elusive challenge: how to make 3D Gaussians move through time as naturally as they would in the real world, all while keeping the motion smooth and consistent. In this paper, we unveil a fresh approach that blends state-space modeling with Wasserstein geometry, paving the way for a more fluid and coherent representation of dynamic scenes. We introduce a State Consistency Filter that merges prior predictions with the current observations, enabling Gaussians to stay true to their way over time. We also employ Wasserstein distance regularization to ensure smooth, consistent updates of Gaussian parameters, reducing motion artifacts. Lastly, we leverage Wasserstein geometry to capture both translational motion and shape deformations, creating a more physically plausible model for dynamic scenes. Our approach guides Gaussians along their natural way in the Wasserstein space, achieving smoother, more realistic motion and stronger temporal coherence. Experimental results show significant improvements in rendering quality and efficiency, outperforming current state-of-the-art techniques.

  </details>


- **[4D Scaffold Gaussian Splatting with Dynamic-Aware Anchor Growing for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2411.17044)**  
  *Woong Oh Cho, In Cho, Seoha Kim, Jeongmin Bae, Youngjung Uh, Seon Joo Kim*  
  `2024-11-26` · `cs.CV` · [abs](https://arxiv.org/abs/2411.17044) · [pdf](https://arxiv.org/pdf/2411.17044.pdf)
  > 💡 针对动态场景重建存储与质量权衡问题，提出保留高斯的4D锚定框架和动态感知锚增长策略，实现高效高保真重建。

  <details><summary>Abstract</summary>

  Modeling dynamic scenes through 4D Gaussians offers high visual fidelity and fast rendering speeds, but comes with significant storage overhead. Recent approaches mitigate this cost by aggressively reducing the number of Gaussians. However, this inevitably removes Gaussians essential for high-quality rendering, leading to severe degradation in dynamic regions. In this paper, we introduce a novel 4D anchor-based framework that tackles the storage cost in different perspective. Rather than reducing the number of Gaussians, our method retains a sufficient quantity to accurately model dynamic contents, while compressing them into compact, grid-aligned 4D anchor features. Each anchor is processed by an MLP to spawn a set of neural 4D Gaussians, which represent a local spatiotemporal region. We design these neural 4D Gaussians to capture temporal changes with minimal parameters, making them well-suited for the MLP-based spawning. Moreover, we introduce a dynamic-aware anchor growing strategy to effectively assign additional anchors to under-reconstructed dynamic regions. Our method adjusts the accumulated gradients with Gaussians' temporal coverage, significantly improving reconstruction quality in dynamic regions. Experimental results highlight that our method achieves state-of-the-art visual quality in dynamic regions, outperforming all baselines by a large margin with practical storage costs.

  </details>


- **[EMD: Explicit Motion Modeling for High-Quality Street Gaussian Splatting](https://arxiv.org/abs/2411.15582)**  
  *Xiaobao Wei, Qingpo Wuwu, Zhongyu Zhao, Zhuangzhe Wu, Nan Huang, Ming Lu, Ningning MA, Shanghang Zhang*  
  `2024-11-23` · `cs.CV` · [abs](https://arxiv.org/abs/2411.15582) · [pdf](https://arxiv.org/pdf/2411.15582.pdf)
  > 💡 针对街景动态物体运动建模不足，提出显式运动分解（EMD）嵌入可学习运动嵌入，实现最先进新视角合成。

  <details><summary>Abstract</summary>

  Photorealistic reconstruction of street scenes is essential for developing real-world simulators in autonomous driving. While recent methods based on 3D/4D Gaussian Splatting (GS) have demonstrated promising results, they still encounter challenges in complex street scenes due to the unpredictable motion of dynamic objects. Current methods typically decompose street scenes into static and dynamic objects, learning the Gaussians in either a supervised manner (e.g., w/ 3D bounding-box) or a self-supervised manner (e.g., w/o 3D bounding-box). However, these approaches do not effectively model the motions of dynamic objects (e.g., the motion speed of pedestrians is clearly different from that of vehicles), resulting in suboptimal scene decomposition. To address this, we propose Explicit Motion Decomposition (EMD), which models the motions of dynamic objects by introducing learnable motion embeddings to the Gaussians, enhancing the decomposition in street scenes. The proposed plug-and-play EMD module compensates for the lack of motion modeling in self-supervised street Gaussian splatting methods. We also introduce tailored training strategies to extend EMD to supervised approaches. Comprehensive experiments demonstrate the effectiveness of our method, achieving state-of-the-art novel view synthesis performance in self-supervised settings. The code is available at: https://qingpowuwu.github.io/emd.

  </details>


- **[SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving](https://arxiv.org/abs/2411.15482)**  
  *Su Sun, Cheng Zhao, Zhuoyang Sun, Yingjie Victor Chen, Mei Chen*  
  `2024-11-23` · `cs.CV` · [abs](https://arxiv.org/abs/2411.15482) · [pdf](https://arxiv.org/pdf/2411.15482.pdf)
  > 💡 用自监督神经运动流场建模4D高斯，无需标注即可实现动态城市场景重建与视图合成，性能领先。

  <details><summary>Abstract</summary>

  Most existing Dynamic Gaussian Splatting methods for complex dynamic urban scenarios rely on accurate object-level supervision from expensive manual labeling, limiting their scalability in real-world applications. In this paper, we introduce SplatFlow, a Self-Supervised Dynamic Gaussian Splatting within Neural Motion Flow Fields (NMFF) to learn 4D space-time representations without requiring tracked 3D bounding boxes, enabling accurate dynamic scene reconstruction and novel view RGB/depth/flow synthesis. SplatFlow designs a unified framework to seamlessly integrate time-dependent 4D Gaussian representation within NMFF, where NMFF is a set of implicit functions to model temporal motions of both LiDAR points and Gaussians as continuous motion flow fields. Leveraging NMFF, SplatFlow effectively decomposes static background and dynamic objects, representing them with 3D and 4D Gaussian primitives, respectively. NMFF also models the correspondences of each 4D Gaussian across time, which aggregates temporal features to enhance cross-view consistency of dynamic components. SplatFlow further improves dynamic object identification by distilling features from 2D foundation models into 4D space-time representation. Comprehensive evaluations conducted on the Waymo and KITTI Datasets validate SplatFlow's state-of-the-art (SOTA) performance for both image reconstruction and novel view synthesis in dynamic urban scenarios.

  </details>


- **[4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization](https://arxiv.org/abs/2411.08879)**  
  *Mijeong Kim, Jongwoo Lim, Bohyung Han*  
  `2024-11-13` · `cs.CV` · [abs](https://arxiv.org/abs/2411.08879) · [pdf](https://arxiv.org/pdf/2411.08879.pdf)
  > 💡 提出不确定性感知正则化和动态区域致密化，解决单目视频4DGS过拟合与初始化问题，提升动态场景新视图合成质量。

  <details><summary>Abstract</summary>

  Novel view synthesis of dynamic scenes is becoming important in various applications, including augmented and virtual reality. We propose a novel 4D Gaussian Splatting (4DGS) algorithm for dynamic scenes from casually recorded monocular videos. To overcome the overfitting problem of existing work for these real-world videos, we introduce an uncertainty-aware regularization that identifies uncertain regions with few observations and selectively imposes additional priors based on diffusion models and depth smoothness on such regions. This approach improves both the performance of novel view synthesis and the quality of training image reconstruction. We also identify the initialization problem of 4DGS in fast-moving dynamic regions, where the Structure from Motion (SfM) algorithm fails to provide reliable 3D landmarks. To initialize Gaussian primitives in such regions, we present a dynamic region densification method using the estimated depth maps and scene flow. Our experiments show that the proposed method improves the performance of 4DGS reconstruction from a video captured by a handheld monocular camera and also exhibits promising results in few-shot static scene reconstruction.

  </details>


- **[Real-Time Spatio-Temporal Reconstruction of Dynamic Endoscopic Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2411.01218)**  
  *Fengze Li, Jishuai He, Jieming Ma, Zhijing Wu*  
  `2024-11-02` · `cs.CV` · [abs](https://arxiv.org/abs/2411.01218) · [pdf](https://arxiv.org/pdf/2411.01218.pdf)
  > 💡 用无偏4DGS和球柱谐函数实时重建动态内窥镜场景，法线对齐约束提升几何精度，达新SOTA。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction is essential in robotic minimally invasive surgery, providing crucial spatial information that enhances surgical precision and outcomes. However, existing methods struggle to address the complex, temporally dynamic nature of endoscopic scenes. This paper presents ST-Endo4DGS, a novel framework that models the spatio-temporal volume of dynamic endoscopic scenes using unbiased 4D Gaussian Splatting (4DGS) primitives, parameterized by anisotropic ellipses with flexible 4D rotations. This approach enables precise representation of deformable tissue dynamics, capturing intricate spatial and temporal correlations in real time. Additionally, we extend spherindrical harmonics to represent time-evolving appearance, achieving realistic adaptations to lighting and view changes. A new endoscopic normal alignment constraint (ENAC) further enhances geometric fidelity by aligning rendered normals with depth-derived geometry. Extensive evaluations show that ST-Endo4DGS outperforms existing methods in both visual quality and real-time performance, establishing a new state-of-the-art in dynamic scene reconstruction for endoscopic surgery.

  </details>


- **[Fully Explicit Dynamic Gaussian Splatting](https://arxiv.org/abs/2410.15629)**  
  *Junoh Lee, Chang-Yeon Won, Hyunjun Jung, Inhwan Bae, Hae-Gon Jeon*  
  `2024-10-21` · `cs.CV` · [abs](https://arxiv.org/abs/2410.15629) · [pdf](https://arxiv.org/pdf/2410.15629.pdf)
  > 💡 针对动态场景渲染，通过分离静动态高斯并显式插值位置旋转，结合渐进训练和点回溯，实现高质量快速渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting has shown fast and high-quality rendering results in static scenes by leveraging dense 3D prior and explicit representations. Unfortunately, the benefits of the prior and representation do not involve novel view synthesis for dynamic motions. Ironically, this is because the main barrier is the reliance on them, which requires increasing training and rendering times to account for dynamic motions. In this paper, we design a Explicit 4D Gaussian Splatting(Ex4DGS). Our key idea is to firstly separate static and dynamic Gaussians during training, and to explicitly sample positions and rotations of the dynamic Gaussians at sparse timestamps. The sampled positions and rotations are then interpolated to represent both spatially and temporally continuous motions of objects in dynamic scenes as well as reducing computational cost. Additionally, we introduce a progressive training scheme and a point-backtracking technique that improves Ex4DGS's convergence. We initially train Ex4DGS using short timestamps and progressively extend timestamps, which makes it work well with a few point clouds. The point-backtracking is used to quantify the cumulative error of each Gaussian over time, enabling the detection and removal of erroneous Gaussians in dynamic scenes. Comprehensive experiments on various scenes demonstrate the state-of-the-art rendering quality from our method, achieving fast rendering of 62 fps on a single 2080Ti GPU.

  </details>


- **[MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2410.13613)**  
  *Xinjie Zhang, Zhening Liu, Yifan Zhang, Xingtong Ge, Dailan He, Tongda Xu, Yan Wang, Zehong Lin, Shuicheng Yan, Jun Zhang*  
  `2024-10-17` · `cs.CV` · [abs](https://arxiv.org/abs/2410.13613) · [pdf](https://arxiv.org/pdf/2410.13613.pdf)
  > 💡 针对4DGS内存大问题，提出分解颜色属性和熵约束变形，实现约190倍和125倍存储压缩，保持渲染速度和质量。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting (4DGS) has recently emerged as a promising technique for capturing complex dynamic 3D scenes with high fidelity. It utilizes a 4D Gaussian representation and a GPU-friendly rasterizer, enabling rapid rendering speeds. Despite its advantages, 4DGS faces significant challenges, notably the requirement of millions of 4D Gaussians, each with extensive associated attributes, leading to substantial memory and storage cost. This paper introduces a memory-efficient framework for 4DGS. We streamline the color attribute by decomposing it into a per-Gaussian direct color component with only 3 parameters and a shared lightweight alternating current color predictor. This approach eliminates the need for spherical harmonics coefficients, which typically involve up to 144 parameters in classic 4DGS, thereby creating a memory-efficient 4D Gaussian representation. Furthermore, we introduce an entropy-constrained Gaussian deformation technique that uses a deformation field to expand the action range of each Gaussian and integrates an opacity-based entropy loss to limit the number of Gaussians, thus forcing our model to use as few Gaussians as possible to fit a dynamic scene well. With simple half-precision storage and zip compression, our framework achieves a storage reduction by approximately 190$\times$ and 125$\times$ on the Technicolor and Neural 3D Video datasets, respectively, compared to the original 4DGS. Meanwhile, it maintains comparable rendering speeds and scene representation quality, setting a new standard in the field. Code is available at https://github.com/Xinjie-Q/MEGA.

  </details>


- **[DN-4DGS: Denoised Deformable Network with Temporal-Spatial Aggregation for Dynamic Scene Rendering](https://arxiv.org/abs/2410.13607)**  
  *Jiahao Lu, Jiacheng Deng, Ruijie Zhu, Yanzhe Liang, Wenfei Yang, Tianzhu Zhang, Xu Zhou*  
  `2024-10-17` · `cs.CV` · [abs](https://arxiv.org/abs/2410.13607) · [pdf](https://arxiv.org/pdf/2410.13607.pdf)
  > 💡 提出噪声抑制策略和解耦时空聚合模块，解决规范3D高斯坐标噪声和4D信息缺失问题，实现实时高质量动态场景渲染。

  <details><summary>Abstract</summary>

  Dynamic scenes rendering is an intriguing yet challenging problem. Although current methods based on NeRF have achieved satisfactory performance, they still can not reach real-time levels. Recently, 3D Gaussian Splatting (3DGS) has garnered researchers attention due to their outstanding rendering quality and real-time speed. Therefore, a new paradigm has been proposed: defining a canonical 3D gaussians and deforming it to individual frames in deformable fields. However, since the coordinates of canonical 3D gaussians are filled with noise, which can transfer noise into the deformable fields, and there is currently no method that adequately considers the aggregation of 4D information. Therefore, we propose Denoised Deformable Network with Temporal-Spatial Aggregation for Dynamic Scene Rendering (DN-4DGS). Specifically, a Noise Suppression Strategy is introduced to change the distribution of the coordinates of the canonical 3D gaussians and suppress noise. Additionally, a Decoupled Temporal-Spatial Aggregation Module is designed to aggregate information from adjacent points and frames. Extensive experiments on various real-world datasets demonstrate that our method achieves state-of-the-art rendering quality under a real-time level.

  </details>


- **[DriveDreamer4D: World Models Are Effective Data Machines for 4D Driving Scene Representation](https://arxiv.org/abs/2410.13571)**  
  *Guosheng Zhao, Chaojun Ni, Xiaofeng Wang, Zheng Zhu, Xueyang Zhang, Yida Wang, Guan Huang, Xinze Chen, Boyuan Wang, Youyi Zhang, Wenjun Mei, Xingang Wang*  
  `2024-10-17` · `cs.CV` · [abs](https://arxiv.org/abs/2410.13571) · [pdf](https://arxiv.org/pdf/2410.13571.pdf)
  > 💡 利用世界模型生成新轨迹视频并采用cousin数据策略优化4DGS，首次提升4D驾驶场景重建的时空一致性和质量。

  <details><summary>Abstract</summary>

  Closed-loop simulation is essential for advancing end-to-end autonomous driving systems. Contemporary sensor simulation methods, such as NeRF and 3DGS, rely predominantly on conditions closely aligned with training data distributions, which are largely confined to forward-driving scenarios. Consequently, these methods face limitations when rendering complex maneuvers (e.g., lane change, acceleration, deceleration). Recent advancements in autonomous-driving world models have demonstrated the potential to generate diverse driving videos. However, these approaches remain constrained to 2D video generation, inherently lacking the spatiotemporal coherence required to capture intricacies of dynamic driving environments. In this paper, we introduce DriveDreamer4D, which enhances 4D driving scene representation leveraging world model priors. Specifically, we utilize the world model as a data machine to synthesize novel trajectory videos, where structured conditions are explicitly leveraged to control the spatial-temporal consistency of traffic elements. Besides, the cousin data training strategy is proposed to facilitate merging real and synthetic data for optimizing 4DGS. To our knowledge, DriveDreamer4D is the first to utilize video generation models for improving 4D reconstruction in driving scenarios. Experimental results reveal that DriveDreamer4D significantly enhances generation quality under novel trajectory views, achieving a relative improvement in FID by 32.1%, 46.4%, and 16.3% compared to PVG, S3Gaussian, and Deformable-GS. Moreover, DriveDreamer4D markedly enhances the spatiotemporal coherence of driving agents, which is verified by a comprehensive user study and the relative increases of 22.6%, 43.5%, and 15.6% in the NTA-IoU metric.

  </details>


- **[4DStyleGaussian: Zero-shot 4D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2410.10412)**  
  *Wanlin Liang, Hongbin Xu, Weitao Chen, Feng Xiao, Wenxiong Kang*  
  `2024-10-14` · `cs.CV` · [abs](https://arxiv.org/abs/2410.10412) · [pdf](https://arxiv.org/pdf/2410.10412.pdf)
  > 💡 针对动态场景风格迁移的时域一致性问题，嵌入4D高斯泼溅与可逆网络，实现零样本实时风格迁移。

  <details><summary>Abstract</summary>

  3D neural style transfer has gained significant attention for its potential to provide user-friendly stylization with spatial consistency. However, existing 3D style transfer methods often fall short in terms of inference efficiency, generalization ability, and struggle to handle dynamic scenes with temporal consistency. In this paper, we introduce 4DStyleGaussian, a novel 4D style transfer framework designed to achieve real-time stylization of arbitrary style references while maintaining reasonable content affinity, multi-view consistency, and temporal coherence. Our approach leverages an embedded 4D Gaussian Splatting technique, which is trained using a reversible neural network for reducing content loss in the feature distillation process. Utilizing the 4D embedded Gaussians, we predict a 4D style transformation matrix that facilitates spatially and temporally consistent style transfer with Gaussian Splatting. Experiments demonstrate that our method can achieve high-quality and zero-shot stylization for 4D scenarios with enhanced efficiency and spatial-temporal consistency.

  </details>


- **[EmoTalk3D: High-Fidelity Free-View Synthesis of Emotional 3D Talking Head](https://arxiv.org/abs/2408.00297)**  
  *Qianyun He, Xinya Ji, Yicheng Gong, Yuanxun Lu, Zhengyu Diao, Linjia Huang, Yao Yao, Siyu Zhu, Zhan Ma, Songcen Xu, Xiaofei Wu, Zixiao Zhang, Xun Cao, Hao Zhu*  
  `2024-08-01` · `cs.CV` · [abs](https://arxiv.org/abs/2408.00297) · [pdf](https://arxiv.org/pdf/2408.00297.pdf)
  > 💡 提出情感可控3D说话头合成方法，利用语音到几何到外观框架和4D高斯表示实现高保真自由视角渲染与动态细节捕捉。

  <details><summary>Abstract</summary>

  We present a novel approach for synthesizing 3D talking heads with controllable emotion, featuring enhanced lip synchronization and rendering quality. Despite significant progress in the field, prior methods still suffer from multi-view consistency and a lack of emotional expressiveness. To address these issues, we collect EmoTalk3D dataset with calibrated multi-view videos, emotional annotations, and per-frame 3D geometry. By training on the EmoTalk3D dataset, we propose a \textit{`Speech-to-Geometry-to-Appearance'} mapping framework that first predicts faithful 3D geometry sequence from the audio features, then the appearance of a 3D talking head represented by 4D Gaussians is synthesized from the predicted geometry. The appearance is further disentangled into canonical and dynamic Gaussians, learned from multi-view videos, and fused to render free-view talking head animation. Moreover, our model enables controllable emotion in the generated talking heads and can be rendered in wide-range views. Our method exhibits improved rendering quality and stability in lip motion generation while capturing dynamic facial details such as wrinkles and subtle expressions. Experiments demonstrate the effectiveness of our approach in generating high-fidelity and emotion-controllable 3D talking heads. The code and EmoTalk3D dataset are released at https://nju-3dv.github.io/projects/EmoTalk3D.

  </details>


- **[Registering Neural 4D Gaussians for Endoscopic Surgery](https://arxiv.org/abs/2407.20213)**  
  *Yiming Huang, Beilei Cui, Ikemura Kei, Jiekai Zhang, Long Bai, Hongliang Ren*  
  `2024-07-29` · `cs.RO` · [abs](https://arxiv.org/abs/2407.20213) · [pdf](https://arxiv.org/pdf/2407.20213.pdf)
  > 💡 针对动态手术场景配准难题，利用4D高斯泼溅表示和空间感知特征聚合SWC，提出可变形配准策略，实现精确对齐。

  <details><summary>Abstract</summary>

  The recent advance in neural rendering has enabled the ability to reconstruct high-quality 4D scenes using neural networks. Although 4D neural reconstruction is popular, registration for such representations remains a challenging task, especially for dynamic scene registration in surgical planning and simulation. In this paper, we propose a novel strategy for dynamic surgical neural scene registration. We first utilize 4D Gaussian Splatting to represent the surgical scene and capture both static and dynamic scenes effectively. Then, a spatial aware feature aggregation method, Spatially Weight Cluttering (SWC) is proposed to accurately align the feature between surgical scenes, enabling precise and realistic surgical simulations. Lastly, we present a novel strategy of deformable scene registration to register two dynamic scenes. By incorporating both spatial and temporal information for correspondence matching, our approach achieves superior performance compared to existing registration methods for implicit neural representation. The proposed method has the potential to improve surgical planning and training, ultimately leading to better patient outcomes.

  </details>


- **[Segment Any 4D Gaussians](https://arxiv.org/abs/2407.04504)**  
  *Shengxiang Ji, Guanjun Wu, Jiemin Fang, Jiazhong Cen, Taoran Yi, Wenyu Liu, Qi Tian, Xinggang Wang*  
  `2024-07-05` · `cs.CV` · [abs](https://arxiv.org/abs/2407.04504) · [pdf](https://arxiv.org/pdf/2407.04504.pdf)
  > 💡 提出首个基于4D高斯的分割一切框架SA4D，用时域身份特征场和细化过程实现精确分割。

  <details><summary>Abstract</summary>

  Modeling, understanding, and reconstructing the real world are crucial in XR/VR. Recently, 3D Gaussian Splatting (3D-GS) methods have shown remarkable success in modeling and understanding 3D scenes. Similarly, various 4D representations have demonstrated the ability to capture the dynamics of the 4D world. However, there is a dearth of research focusing on segmentation within 4D representations. In this paper, we propose Segment Any 4D Gaussians (SA4D), one of the first frameworks to segment anything in the 4D digital world based on 4D Gaussians. In SA4D, an efficient temporal identity feature field is introduced to handle Gaussian drifting, with the potential to learn precise identity features from noisy and sparse input. Additionally, a 4D segmentation refinement process is proposed to remove artifacts. Our SA4D achieves precise, high-quality segmentation within seconds in 4D Gaussians and shows the ability to remove, recolor, compose, and render high-quality anything masks. More demos are available at: https://jsxzs.github.io/sa4d/.

  </details>


- **[Dynamic Gaussian Marbles for Novel View Synthesis of Casual Monocular Videos](https://arxiv.org/abs/2406.18717)**  
  *Colton Stearns, Adam Harley, Mikaela Uy, Florian Dubost, Federico Tombari, Gordon Wetzstein, Leonidas Guibas*  
  `2024-06-26` · `cs.CV` · [abs](https://arxiv.org/abs/2406.18717) · [pdf](https://arxiv.org/pdf/2406.18717.pdf)
  > 💡 针对单目视频新视角合成，提出各向同性高斯球结合层次化学习和点跟踪先验，实现高质量动态重建。

  <details><summary>Abstract</summary>

  Gaussian splatting has become a popular representation for novel-view synthesis, exhibiting clear strengths in efficiency, photometric quality, and compositional edibility. Following its success, many works have extended Gaussians to 4D, showing that dynamic Gaussians maintain these benefits while also tracking scene geometry far better than alternative representations. Yet, these methods assume dense multi-view videos as supervision. In this work, we are interested in extending the capability of Gaussian scene representations to casually captured monocular videos. We show that existing 4D Gaussian methods dramatically fail in this setup because the monocular setting is underconstrained. Building off this finding, we propose a method we call Dynamic Gaussian Marbles, which consist of three core modifications that target the difficulties of the monocular setting. First, we use isotropic Gaussian "marbles'', reducing the degrees of freedom of each Gaussian. Second, we employ a hierarchical divide and-conquer learning strategy to efficiently guide the optimization towards solutions with globally coherent motion. Finally, we add image-level and geometry-level priors into the optimization, including a tracking loss that takes advantage of recent progress in point tracking. By constraining the optimization, Dynamic Gaussian Marbles learns Gaussian trajectories that enable novel-view rendering and accurately capture the 3D motion of the scene elements. We evaluate on the Nvidia Dynamic Scenes dataset and the DyCheck iPhone dataset, and show that Gaussian Marbles significantly outperforms other Gaussian baselines in quality, and is on-par with non-Gaussian representations, all while maintaining the efficiency, compositionality, editability, and tracking benefits of Gaussians. Our project page can be found here https://geometry.stanford.edu/projects/dynamic-gaussian-marbles.github.io/.

  </details>


- **[LGS: A Light-weight 4D Gaussian Splatting for Efficient Surgical Scene Reconstruction](https://arxiv.org/abs/2406.16073)**  
  *Hengyu Liu, Yifan Liu, Chenxin Li, Wuyang Li, Yixuan Yuan*  
  `2024-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2406.16073) · [pdf](https://arxiv.org/pdf/2406.16073.pdf)
  > 💡 针对动态手术场景重建中4D高斯泼溅存储和渲染瓶颈，提出变形感知剪枝与特征场压缩的轻量框架，实现9倍以上压缩并保持高质量实时渲染。

  <details><summary>Abstract</summary>

  The advent of 3D Gaussian Splatting (3D-GS) techniques and their dynamic scene modeling variants, 4D-GS, offers promising prospects for real-time rendering of dynamic surgical scenarios. However, the prerequisite for modeling dynamic scenes by a large number of Gaussian units, the high-dimensional Gaussian attributes and the high-resolution deformation fields, all lead to serve storage issues that hinder real-time rendering in resource-limited surgical equipment. To surmount these limitations, we introduce a Lightweight 4D Gaussian Splatting framework (LGS) that can liberate the efficiency bottlenecks of both rendering and storage for dynamic endoscopic reconstruction. Specifically, to minimize the redundancy of Gaussian quantities, we propose Deformation-Aware Pruning by gauging the impact of each Gaussian on deformation. Concurrently, to reduce the redundancy of Gaussian attributes, we simplify the representation of textures and lighting in non-crucial areas by pruning the dimensions of Gaussian attributes. We further resolve the feature field redundancy caused by the high resolution of 4D neural spatiotemporal encoder for modeling dynamic scenes via a 4D feature field condensation. Experiments on public benchmarks demonstrate efficacy of LGS in terms of a compression rate exceeding 9 times while maintaining the pleasing visual quality and real-time rendering efficiency. LGS confirms a substantial step towards its application in robotic surgical services.

  </details>


- **[L4GM: Large 4D Gaussian Reconstruction Model](https://arxiv.org/abs/2406.10324)**  
  *Jiawei Ren, Kevin Xie, Ashkan Mirzaei, Hanxue Liang, Xiaohui Zeng, Karsten Kreis, Ziwei Liu, Antonio Torralba, Sanja Fidler, Seung Wook Kim, Huan Ling*  
  `2024-06-14` · `cs.CV` · [abs](https://arxiv.org/abs/2406.10324) · [pdf](https://arxiv.org/pdf/2406.10324.pdf)
  > 💡 单视图视频输入生成动画3D物体，利用3D高斯和时间自注意力实现快速前馈，合成训练泛化真实视频。

  <details><summary>Abstract</summary>

  We present L4GM, the first 4D Large Reconstruction Model that produces animated objects from a single-view video input -- in a single feed-forward pass that takes only a second. Key to our success is a novel dataset of multiview videos containing curated, rendered animated objects from Objaverse. This dataset depicts 44K diverse objects with 110K animations rendered in 48 viewpoints, resulting in 12M videos with a total of 300M frames. We keep our L4GM simple for scalability and build directly on top of LGM, a pretrained 3D Large Reconstruction Model that outputs 3D Gaussian ellipsoids from multiview image input. L4GM outputs a per-frame 3D Gaussian Splatting representation from video frames sampled at a low fps and then upsamples the representation to a higher fps to achieve temporal smoothness. We add temporal self-attention layers to the base LGM to help it learn consistency across time, and utilize a per-timestep multiview rendering loss to train the model. The representation is upsampled to a higher framerate by training an interpolation model which produces intermediate 3D Gaussian representations. We showcase that L4GM that is only trained on synthetic data generalizes extremely well on in-the-wild videos, producing high quality animated 3D assets.

  </details>


- **[Improving Gaussian Splatting with Localized Points Management](https://arxiv.org/abs/2406.04251)**  
  *Haosen Yang, Chenhao Zhang, Wenqing Wang, Marco Volino, Adrian Hilton, Li Zhang, Xiatian Zhu*  
  `2024-06-06` · `cs.CV` · [abs](https://arxiv.org/abs/2406.04251) · [pdf](https://arxiv.org/pdf/2406.04251.pdf)
  > 💡 针对3DGS点管理局限，提出局部点管理（LPM），利用多视图几何识别需优化区域，提升静态/动态GS渲染质量达SOTA。

  <details><summary>Abstract</summary>

  Point management is critical for optimizing 3D Gaussian Splatting models, as point initiation (e.g., via structure from motion) is often distributionally inappropriate. Typically, Adaptive Density Control (ADC) algorithm is adopted, leveraging view-averaged gradient magnitude thresholding for point densification, opacity thresholding for pruning, and regular all-points opacity reset. We reveal that this strategy is limited in tackling intricate/special image regions (e.g., transparent) due to inability of identifying all 3D zones requiring point densification, and lacking an appropriate mechanism to handle ill-conditioned points with negative impacts (e.g., occlusion due to false high opacity). To address these limitations, we propose a Localized Point Management (LPM) strategy, capable of identifying those error-contributing zones in greatest need for both point addition and geometry calibration. Zone identification is achieved by leveraging the underlying multiview geometry constraints, subject to image rendering errors. We apply point densification in the identified zones and then reset the opacity of the points in front of these regions, creating a new opportunity to correct poorly conditioned points. Serving as a versatile plugin, LPM can be seamlessly integrated into existing static 3D and dynamic 4D Gaussian Splatting models with minimal additional cost. Experimental evaluations validate the efficacy of our LPM in boosting a variety of existing 3D/4D models both quantitatively and qualitatively. Notably, LPM improves both static 3DGS and dynamic SpaceTimeGS to achieve state-of-the-art rendering quality while retaining real-time speeds, excelling on challenging datasets such as Tanks & Temples and the Neural 3D Video dataset.

  </details>


- **[Self-Calibrating 4D Novel View Synthesis from Monocular Videos Using Gaussian Splatting](https://arxiv.org/abs/2406.01042)**  
  *Fang Li, Hao Zhang, Narendra Ahuja*  
  `2024-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2406.01042) · [pdf](https://arxiv.org/pdf/2406.01042.pdf)
  > 💡 现有4DGS依赖COLMAP参数精度差且耗时，本文用自校准联合优化相机参数与4D场景，提升大运动及极端视角下新视角合成质量。

  <details><summary>Abstract</summary>

  Gaussian Splatting (GS) has significantly elevated scene reconstruction efficiency and novel view synthesis (NVS) accuracy compared to Neural Radiance Fields (NeRF), particularly for dynamic scenes. However, current 4D NVS methods, whether based on GS or NeRF, primarily rely on camera parameters provided by COLMAP and even utilize sparse point clouds generated by COLMAP for initialization, which lack accuracy as well are time-consuming. This sometimes results in poor dynamic scene representation, especially in scenes with large object movements, or extreme camera conditions e.g. small translations combined with large rotations. Some studies simultaneously optimize the estimation of camera parameters and scenes, supervised by additional information like depth, optical flow, etc. obtained from off-the-shelf models. Using this unverified information as ground truth can reduce robustness and accuracy, which does frequently occur for long monocular videos (with e.g. > hundreds of frames). We propose a novel approach that learns a high-fidelity 4D GS scene representation with self-calibration of camera parameters. It includes the extraction of 2D point features that robustly represent 3D structure, and their use for subsequent joint optimization of camera parameters and 3D structure towards overall 4D scene optimization. We demonstrate the accuracy and time efficiency of our method through extensive quantitative and qualitative experimental results on several standard benchmarks. The results show significant improvements over state-of-the-art methods for 4D novel view synthesis. The source code will be released soon at https://github.com/fangli333/SC-4DGS.

  </details>


- **[PLA4D: Pixel-Level Alignments for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2405.19957)**  
  *Qiaowei Miao, JinSheng Quan, Kehan Li, Yawei Luo*  
  `2024-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2405.19957) · [pdf](https://arxiv.org/pdf/2405.19957.pdf)
  > 💡 提出像素级对齐（PLA4D）解决文本到4D高斯泼溅中运动-几何冲突，通过静态和动态对齐实现一致的高质量4D生成。

  <details><summary>Abstract</summary>

  Previous text-to-4D methods have leveraged multiple Score Distillation Sampling (SDS) techniques, combining motion priors from video-based diffusion models (DMs) with geometric priors from multiview DMs to implicitly guide 4D renderings. However, differences in these priors result in conflicting gradient directions during optimization, causing trade-offs between motion fidelity and geometry accuracy, and requiring substantial optimization time to reconcile the models. In this paper, we introduce \textbf{P}ixel-\textbf{L}evel \textbf{A}lignment for text-driven \textbf{4D} Gaussian splatting (PLA4D) to resolve this motion-geometry conflict. PLA4D provides an anchor reference, i.e., text-generated video, to align the rendering process conditioned by different DMs in pixel space. For static alignment, our approach introduces a focal alignment method and Gaussian-Mesh contrastive learning to iteratively adjust focal lengths and provide explicit geometric priors at each timestep. At the dynamic level, a motion alignment technique and T-MV refinement method are employed to enforce both pose alignment and motion continuity across unknown viewpoints, ensuring intrinsic geometric consistency across views. With such pixel-level multi-DM alignment, our PLA4D framework is able to generate 4D objects with superior geometric, motion, and semantic consistency. Fully implemented with open-source tools, PLA4D offers an efficient and accessible solution for high-quality 4D digital content creation with significantly reduced generation time.

  </details>


- **[HFGS: 4D Gaussian Splatting with Emphasis on Spatial and Temporal High-Frequency Components for Endoscopic Scene Reconstruction](https://arxiv.org/abs/2405.17872)**  
  *Haoyu Zhao, Xingyue Zhao, Lingting Zhu, Weixi Zheng, Yongchao Xu*  
  `2024-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2405.17872) · [pdf](https://arxiv.org/pdf/2405.17872.pdf)
  > 💡 提出HFGS，通过空间和时间高频强调重建，解决内窥镜动态场景中3DGS的欠重建问题，显著提升渲染质量。

  <details><summary>Abstract</summary>

  Robot-assisted minimally invasive surgery benefits from enhancing dynamic scene reconstruction, as it improves surgical outcomes. While Neural Radiance Fields (NeRF) have been effective in scene reconstruction, their slow inference speeds and lengthy training durations limit their applicability. To overcome these limitations, 3D Gaussian Splatting (3D-GS) based methods have emerged as a recent trend, offering rapid inference capabilities and superior 3D quality. However, these methods still struggle with under-reconstruction in both static and dynamic scenes. In this paper, we propose HFGS, a novel approach for deformable endoscopic reconstruction that addresses these challenges from spatial and temporal frequency perspectives. Our approach incorporates deformation fields to better handle dynamic scenes and introduces Spatial High-Frequency Emphasis Reconstruction (SHF) to minimize discrepancies in spatial frequency spectra between the rendered image and its ground truth. Additionally, we introduce Temporal High-Frequency Emphasis Reconstruction (THF) to enhance dynamic awareness in neural rendering by leveraging flow priors, focusing optimization on motion-intensive parts. Extensive experiments on two widely used benchmarks demonstrate that HFGS achieves superior rendering quality.

  </details>


- **[NeuroGauss4D-PCI: 4D Neural Fields and Gaussian Deformation Fields for Point Cloud Interpolation](https://arxiv.org/abs/2405.14241)**  
  *Chaokang Jiang, Dalong Du, Jiuming Liu, Siting Zhu, Zhenqiang Liu, Zhuang Ma, Zhujin Liang, Jie Zhou*  
  `2024-05-23` · `cs.CV` · [abs](https://arxiv.org/abs/2405.14241) · [pdf](https://arxiv.org/pdf/2405.14241.pdf)
  > 💡 利用迭代高斯聚类、时变高斯残差和4D变形场与神经场融合，实现复杂非刚性动态点云的高效插值。

  <details><summary>Abstract</summary>

  Point Cloud Interpolation confronts challenges from point sparsity, complex spatiotemporal dynamics, and the difficulty of deriving complete 3D point clouds from sparse temporal information. This paper presents NeuroGauss4D-PCI, which excels at modeling complex non-rigid deformations across varied dynamic scenes. The method begins with an iterative Gaussian cloud soft clustering module, offering structured temporal point cloud representations. The proposed temporal radial basis function Gaussian residual utilizes Gaussian parameter interpolation over time, enabling smooth parameter transitions and capturing temporal residuals of Gaussian distributions. Additionally, a 4D Gaussian deformation field tracks the evolution of these parameters, creating continuous spatiotemporal deformation fields. A 4D neural field transforms low-dimensional spatiotemporal coordinates ($x,y,z,t$) into a high-dimensional latent space. Finally, we adaptively and efficiently fuse the latent features from neural fields and the geometric features from Gaussian deformation fields. NeuroGauss4D-PCI outperforms existing methods in point cloud frame interpolation, delivering leading performance on both object-level (DHB) and large-scale autonomous driving datasets (NL-Drive), with scalability to auto-labeling and point cloud densification tasks. The source code is released at https://github.com/jiangchaokang/NeuroGauss4D-PCI.

  </details>


- **[PhysAvatar: Learning the Physics of Dressed 3D Avatars from Visual Observations](https://arxiv.org/abs/2404.04421)**  
  *Yang Zheng, Qingqing Zhao, Guandao Yang, Wang Yifan, Donglai Xiang, Florian Dubost, Dmitry Lagun, Thabo Beeler, Federico Tombari, Leonidas Guibas, Gordon Wetzstein*  
  `2024-04-05` · `cs.GR` · [abs](https://arxiv.org/abs/2404.04421) · [pdf](https://arxiv.org/pdf/2404.04421.pdf)
  > 💡 结合逆向渲染与物理模拟，利用4D高斯和物理基础渲染器自动估计人体形状、外观及衣物物理参数，实现宽松衣物下的高质量新视角渲染。

  <details><summary>Abstract</summary>

  Modeling and rendering photorealistic avatars is of crucial importance in many applications. Existing methods that build a 3D avatar from visual observations, however, struggle to reconstruct clothed humans. We introduce PhysAvatar, a novel framework that combines inverse rendering with inverse physics to automatically estimate the shape and appearance of a human from multi-view video data along with the physical parameters of the fabric of their clothes. For this purpose, we adopt a mesh-aligned 4D Gaussian technique for spatio-temporal mesh tracking as well as a physically based inverse renderer to estimate the intrinsic material properties. PhysAvatar integrates a physics simulator to estimate the physical parameters of the garments using gradient-based optimization in a principled manner. These novel capabilities enable PhysAvatar to create high-quality novel-view renderings of avatars dressed in loose-fitting clothes under motions and lighting conditions not seen in the training data. This marks a significant advancement towards modeling photorealistic digital humans using physically based inverse rendering with physics in the loop. Our project website is at: https://qingqing-zhao.github.io/PhysAvatar

  </details>


- **[STAG4D: Spatial-Temporal Anchored Generative 4D Gaussians](https://arxiv.org/abs/2403.14939)**  
  *Yifei Zeng, Yanqin Jiang, Siyu Zhu, Yuanxun Lu, Youtian Lin, Hao Zhu, Weiming Hu, Xun Cao, Yao Yao*  
  `2024-03-22` · `cs.CV` · [abs](https://arxiv.org/abs/2403.14939) · [pdf](https://arxiv.org/pdf/2403.14939.pdf)
  > 💡 结合多视图扩散与动态3D高斯泼溅，使用时序锚点和自适应密度策略，实现高保真、时空一致的4D生成。

  <details><summary>Abstract</summary>

  Recent progress in pre-trained diffusion models and 3D generation have spurred interest in 4D content creation. However, achieving high-fidelity 4D generation with spatial-temporal consistency remains a challenge. In this work, we propose STAG4D, a novel framework that combines pre-trained diffusion models with dynamic 3D Gaussian splatting for high-fidelity 4D generation. Drawing inspiration from 3D generation techniques, we utilize a multi-view diffusion model to initialize multi-view images anchoring on the input video frames, where the video can be either real-world captured or generated by a video diffusion model. To ensure the temporal consistency of the multi-view sequence initialization, we introduce a simple yet effective fusion strategy to leverage the first frame as a temporal anchor in the self-attention computation. With the almost consistent multi-view sequences, we then apply the score distillation sampling to optimize the 4D Gaussian point cloud. The 4D Gaussian spatting is specially crafted for the generation task, where an adaptive densification strategy is proposed to mitigate the unstable Gaussian gradient for robust optimization. Notably, the proposed pipeline does not require any pre-training or fine-tuning of diffusion networks, offering a more accessible and practical solution for the 4D generation task. Extensive experiments demonstrate that our method outperforms prior 4D generation works in rendering quality, spatial-temporal consistency, and generation robustness, setting a new state-of-the-art for 4D generation from diverse inputs, including text, image, and video.

  </details>


- **[4D-Rotor Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes](https://arxiv.org/abs/2402.03307)**  
  *Yuanxing Duan, Fangyin Wei, Qiyu Dai, Yuhang He, Wenzheng Chen, Baoquan Chen*  
  `2024-02-05` · `cs.CV` · [abs](https://arxiv.org/abs/2402.03307) · [pdf](https://arxiv.org/pdf/2402.03307.pdf)
  > 💡 用各向异性4D XYZT高斯表示动态场景，通过时间切片实现高效新视角合成，实时渲染达277-583 FPS，优于现有方法。

  <details><summary>Abstract</summary>

  We consider the problem of novel-view synthesis (NVS) for dynamic scenes. Recent neural approaches have accomplished exceptional NVS results for static 3D scenes, but extensions to 4D time-varying scenes remain non-trivial. Prior efforts often encode dynamics by learning a canonical space plus implicit or explicit deformation fields, which struggle in challenging scenarios like sudden movements or generating high-fidelity renderings. In this paper, we introduce 4D Gaussian Splatting (4DRotorGS), a novel method that represents dynamic scenes with anisotropic 4D XYZT Gaussians, inspired by the success of 3D Gaussian Splatting in static scenes. We model dynamics at each timestamp by temporally slicing the 4D Gaussians, which naturally compose dynamic 3D Gaussians and can be seamlessly projected into images. As an explicit spatial-temporal representation, 4DRotorGS demonstrates powerful capabilities for modeling complicated dynamics and fine details--especially for scenes with abrupt motions. We further implement our temporal slicing and splatting techniques in a highly optimized CUDA acceleration framework, achieving real-time inference rendering speeds of up to 277 FPS on an RTX 3090 GPU and 583 FPS on an RTX 4090 GPU. Rigorous evaluations on scenes with diverse motions showcase the superior efficiency and effectiveness of 4DRotorGS, which consistently outperforms existing methods both quantitatively and qualitatively.

  </details>


- **[Endo-4DGS: Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting](https://arxiv.org/abs/2401.16416)**  
  *Yiming Huang, Beilei Cui, Long Bai, Ziqi Guo, Mengya Xu, Mobarakol Islam, Hongliang Ren*  
  `2024-01-29` · `cs.CV` · [abs](https://arxiv.org/abs/2401.16416) · [pdf](https://arxiv.org/pdf/2401.16416.pdf)
  > 💡 针对内窥镜动态重建慢与深度不一致，提出4DGS结合轻量MLP变形场和深度先验，实现实时高精度重建。

  <details><summary>Abstract</summary>

  In the realm of robot-assisted minimally invasive surgery, dynamic scene reconstruction can significantly enhance downstream tasks and improve surgical outcomes. Neural Radiance Fields (NeRF)-based methods have recently risen to prominence for their exceptional ability to reconstruct scenes but are hampered by slow inference speed, prolonged training, and inconsistent depth estimation. Some previous work utilizes ground truth depth for optimization but is hard to acquire in the surgical domain. To overcome these obstacles, we present Endo-4DGS, a real-time endoscopic dynamic reconstruction approach that utilizes 3D Gaussian Splatting (GS) for 3D representation. Specifically, we propose lightweight MLPs to capture temporal dynamics with Gaussian deformation fields. To obtain a satisfactory Gaussian Initialization, we exploit a powerful depth estimation foundation model, Depth-Anything, to generate pseudo-depth maps as a geometry prior. We additionally propose confidence-guided learning to tackle the ill-pose problems in monocular depth estimation and enhance the depth-guided reconstruction with surface normal constraints and depth regularization. Our approach has been validated on two surgical datasets, where it can effectively render in real-time, compute efficiently, and reconstruct with remarkable accuracy.

  </details>


- **[Efficient4D: Fast Dynamic 3D Object Generation from a Single-view Video](https://arxiv.org/abs/2401.08742)**  
  *Zijie Pan, Zeyu Yang, Xiatian Zhu, Li Zhang*  
  `2024-01-16` · `cs.CV` · [abs](https://arxiv.org/abs/2401.08742) · [pdf](https://arxiv.org/pdf/2401.08742.pdf)
  > 💡 单视频生成动态3D物体速度慢，提出Efficient4D框架，用4D高斯溅射和置信度加权损失，实现10倍加速与实时渲染。

  <details><summary>Abstract</summary>

  Generating dynamic 3D object from a single-view video is challenging due to the lack of 4D labeled data. An intuitive approach is to extend previous image-to-3D pipelines by transferring off-the-shelf image generation models such as score distillation sampling.However, this approach would be slow and expensive to scale due to the need for back-propagating the information-limited supervision signals through a large pretrained model. To address this, we propose an efficient video-to-4D object generation framework called Efficient4D. It generates high-quality spacetime-consistent images under different camera views, and then uses them as labeled data to directly reconstruct the 4D content through a 4D Gaussian splatting model. Importantly, our method can achieve real-time rendering under continuous camera trajectories. To enable robust reconstruction under sparse views, we introduce inconsistency-aware confidence-weighted loss design, along with a lightly weighted score distillation loss. Extensive experiments on both synthetic and real videos show that Efficient4D offers a remarkable 10-fold increase in speed when compared to prior art alternatives while preserving the quality of novel view synthesis. For example, Efficient4D takes only 10 minutes to model a dynamic object, vs 120 minutes by the previous art model Consistent4D.

  </details>


- **[DreamGaussian4D: Generative 4D Gaussian Splatting](https://arxiv.org/abs/2312.17142)**  
  *Jiawei Ren, Liang Pan, Jiaxiang Tang, Chi Zhang, Ang Cao, Gang Zeng, Ziwei Liu*  
  `2023-12-28` · `cs.CV` · [abs](https://arxiv.org/abs/2312.17142) · [pdf](https://arxiv.org/pdf/2312.17142.pdf)
  > 💡 针对4D生成耗时长、运动难控、细节不足，提出结合高斯溅射与HexPlane变形及视频纹理细化，数分钟生成高质量可控4D内容。

  <details><summary>Abstract</summary>

  4D content generation has achieved remarkable progress recently. However, existing methods suffer from long optimization times, a lack of motion controllability, and a low quality of details. In this paper, we introduce DreamGaussian4D (DG4D), an efficient 4D generation framework that builds on Gaussian Splatting (GS). Our key insight is that combining explicit modeling of spatial transformations with static GS makes an efficient and powerful representation for 4D generation. Moreover, video generation methods have the potential to offer valuable spatial-temporal priors, enhancing the high-quality 4D generation. Specifically, we propose an integral framework with two major modules: 1) Image-to-4D GS - we initially generate static GS with DreamGaussianHD, followed by HexPlane-based dynamic generation with Gaussian deformation; and 2) Video-to-Video Texture Refinement - we refine the generated UV-space texture maps and meanwhile enhance their temporal consistency by utilizing a pre-trained image-to-video diffusion model. Notably, DG4D reduces the optimization time from several hours to just a few minutes, allows the generated 3D motion to be visually controlled, and produces animated meshes that can be realistically rendered in 3D engines.

  </details>


- **[HiFi4G: High-Fidelity Human Performance Rendering via Compact Gaussian Splatting](https://arxiv.org/abs/2312.03461)**  
  *Yuheng Jiang, Zhehao Shen, Penghao Wang, Zhuo Su, Yu Hong, Yingliang Zhang, Jingyi Yu, Lan Xu*  
  `2023-12-06` · `cs.CV` · [abs](https://arxiv.org/abs/2312.03461) · [pdf](https://arxiv.org/pdf/2312.03461.pdf)
  > 💡 提出紧凑高斯溅射与非刚性跟踪结合，通过双图机制和自适应正则化实现高保真人体性能渲染，压缩率达25倍。

  <details><summary>Abstract</summary>

  We have recently seen tremendous progress in photo-real human modeling and rendering. Yet, efficiently rendering realistic human performance and integrating it into the rasterization pipeline remains challenging. In this paper, we present HiFi4G, an explicit and compact Gaussian-based approach for high-fidelity human performance rendering from dense footage. Our core intuition is to marry the 3D Gaussian representation with non-rigid tracking, achieving a compact and compression-friendly representation. We first propose a dual-graph mechanism to obtain motion priors, with a coarse deformation graph for effective initialization and a fine-grained Gaussian graph to enforce subsequent constraints. Then, we utilize a 4D Gaussian optimization scheme with adaptive spatial-temporal regularizers to effectively balance the non-rigid prior and Gaussian updating. We also present a companion compression scheme with residual compensation for immersive experiences on various platforms. It achieves a substantial compression rate of approximately 25 times, with less than 2MB of storage per frame. Extensive experiments demonstrate the effectiveness of our approach, which significantly outperforms existing approaches in terms of optimization speed, rendering quality, and storage overhead.

  </details>


- **[Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting](https://arxiv.org/abs/2310.10642)**  
  *Zeyu Yang, Hongye Yang, Zijie Pan, Li Zhang*  
  `2023-10-16` · `cs.CV` · [abs](https://arxiv.org/abs/2310.10642) · [pdf](https://arxiv.org/pdf/2310.10642.pdf)
  > 💡 针对动态场景时空结构建模困难，提出4D高斯原语表示时空体积，实现实时高质量新视角合成。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from 2D images and generating diverse views over time is challenging due to scene complexity and temporal dynamics. Despite advancements in neural implicit models, limitations persist: (i) Inadequate Scene Structure: Existing methods struggle to reveal the spatial and temporal structure of dynamic scenes from directly learning the complex 6D plenoptic function. (ii) Scaling Deformation Modeling: Explicitly modeling scene element deformation becomes impractical for complex dynamics. To address these issues, we consider the spacetime as an entirety and propose to approximate the underlying spatio-temporal 4D volume of a dynamic scene by optimizing a collection of 4D primitives, with explicit geometry and appearance modeling. Learning to optimize the 4D primitives enables us to synthesize novel views at any desired time with our tailored rendering routine. Our model is conceptually simple, consisting of a 4D Gaussian parameterized by anisotropic ellipses that can rotate arbitrarily in space and time, as well as view-dependent and time-evolved appearance represented by the coefficient of 4D spherindrical harmonics. This approach offers simplicity, flexibility for variable-length video and end-to-end training, and efficient real-time rendering, making it suitable for capturing complex dynamic scene motions. Experiments across various benchmarks, including monocular and multi-view scenarios, demonstrate our 4DGS model's superior visual quality and efficiency.

  </details>


- **[4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2310.08528)**  
  *Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Qi Tian, Xinggang Wang*  
  `2023-10-12` · `cs.CV` · [abs](https://arxiv.org/abs/2310.08528) · [pdf](https://arxiv.org/pdf/2310.08528.pdf)
  > 💡 提出4D高斯溅

  <details><summary>Abstract</summary>

  Representing and rendering dynamic scenes has been an important but challenging task. Especially, to accurately model complex motions, high efficiency is usually hard to guarantee. To achieve real-time dynamic scene rendering while also enjoying high training and storage efficiency, we propose 4D Gaussian Splatting (4D-GS) as a holistic representation for dynamic scenes rather than applying 3D-GS for each individual frame. In 4D-GS, a novel explicit representation containing both 3D Gaussians and 4D neural voxels is proposed. A decomposed neural voxel encoding algorithm inspired by HexPlane is proposed to efficiently build Gaussian features from 4D neural voxels and then a lightweight MLP is applied to predict Gaussian deformations at novel timestamps. Our 4D-GS method achieves real-time rendering under high resolutions, 82 FPS at an 800$\times$800 resolution on an RTX 3090 GPU while maintaining comparable or better quality than previous state-of-the-art methods. More demos and code are available at https://guanjunwu.github.io/4dgs/.

  </details>


- **[Equilibrium and off-equilibrium simulations of the 4d Gaussian spin glass](https://arxiv.org/abs/cond-mat/9606051)**  
  *Giorgio Parisi, Federico Ricci-Tersenghi, Juan J. Ruiz-Lorenzo*  
  `1996-06-09` · `cond-mat` · [abs](https://arxiv.org/abs/cond-mat/9606051) · [pdf](https://arxiv.org/pdf/cond-mat/9606051.pdf)
  > 💡 通过平衡与非平衡模拟，更精确确定了四维高斯自旋玻璃的临界温度与指数，并首次动态获取了序参量值。

  <details><summary>Abstract</summary>

  In this paper we study the on and off-equilibrium properties of the four dimensional Gaussian spin glass. In the static case we determine with more precision that in previous simulations both the critical temperature as well as the critical exponents. In the off-equilibrium case we settle the general form of the autocorrelation function, and show that is possible to obtain dynamically, for the first time, a value for the order parameter.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (24) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[Eulerian Gaussian Splatting using Hashed Probability Pyramids](https://arxiv.org/abs/2605.29136)**  
  *Mia Gaia Polansky, George Kopanas, Stephan Garbin, Todd Zickler, Dor Verbin*  
  `2026-05-27` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29136) · [pdf](https://arxiv.org/pdf/2605.29136.pdf)
  > 💡 提出概率密度与多尺度分层网格优化，替代启发式原始操作，实现SOTA重建质量并保持快速渲染。

  <details><summary>Abstract</summary>

  We introduce a probabilistic splat-based radiance field framework that retains the fast rasterization and test-time efficiency of 3D Gaussian Splatting (3DGS) while replacing heuristic primitive manipulation with gradient-based optimization of a volumetric probability density. Rather than relocating, splitting, or culling Gaussians via hand-tuned densification (e.g., ADC), we treat primitive locations as samples drawn from a persistent, learnable density. We instantiate this density using a novel, memory-efficient multi-scale hierarchical grid that enables end-to-end gradient-based optimization. To stabilize the optimization, we derive an unbiased gradient estimator with control variates that markedly reduces variance. By allowing probability mass to flow to where the loss demands, our framework eliminates brittle priors and naturally explores the volume, achieving state-of-the-art reconstruction quality on mip-NeRF 360 while preserving 3DGS-level rendering speed.

  </details>


- **[ParkingWorld: End-to-End Autonomous Parking Reinforcement Learning from Corrective Experience in 3DGS Simulation](https://arxiv.org/abs/2605.25029)**  
  *Zhengcheng Yu, Changze Li, Haoran Liu, Tong Qin*  
  `2026-05-24` · `cs.RO` · [abs](https://arxiv.org/abs/2605.25029) · [pdf](https://arxiv.org/pdf/2605.25029.pdf)
  > 💡 针对自动泊车训练低效问题，提出在3DGS仿真中利用校正循环和多级回放缓冲区的CIL-SERL框架，显著提升成功率与安全性。

  <details><summary>Abstract</summary>

  Autonomous parking demands precise low-speed maneuvering within narrow, cluttered, and highly constrained environments, where vehicles must navigate tight spaces while avoiding static obstacles and complex geometric boundaries. Unlike imitation learning, which typically requires massive volumes of high-quality expert demonstrations to converge to a stable policy and often suffers from limited generalization to unseen scenarios, traditional reinforcement learning (RL) methods face persistent challenges including excessive training overhead, inefficient exploration, and even failure to learn viable parking strategies in challenging settings. To address these limitations, this paper presents a correction-in-the-loop sample-efficient reinforcement learning (CIL-SERL) framework for end-to-end autonomous parking, which is entirely trained in a photorealistic 3D Gaussian Splatting (3DGS) parking simulator that enables high-fidelity digital reconstruction of real-world scenes. Inspired by error-correction notebooks used in learning practice, we design a novel multi-level replay buffer mechanism. These buffers hierarchically organize and store standard RL rollouts, human corrective interventions, failed exploration trajectories, and rollback-based correction segments in separate yet interconnected memory regions, facilitating structured sampling and targeted learning during training. The proposed framework is systematically evaluated in both the 3DGS simulation environment and a physical vehicle platform. Extensive experimental results demonstrate that our method achieves substantial improvements in parking success rate, operational efficiency, and safety performance across diverse scenarios, validating the effectiveness and practical applicability of the proposed CIL-SERL-based end-to-end autonomous parking solution.

  </details>


- **[Multi-view Consistent 3D Gaussian Head Avatars 'without' Multi-view Generation](https://arxiv.org/abs/2605.25220)**  
  *Aviral Chharia, Fernando De la Torre*  
  `2026-05-24` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25220) · [pdf](https://arxiv.org/pdf/2605.25220.pdf)
  > 💡 单图生成多视图一致3D高斯头部，提出层次化状态空间与双向扫描及多视图评判器，超越先前方法并发布FaceGS-10K数据集。

  <details><summary>Abstract</summary>

  High-fidelity 3D Gaussian head avatar generation is critical for applications such as AR/VR, telepresence, and digital humans. Existing methods depend on multi-view datasets, 3D captures, or intermediate 2D view synthesis. In contrast, we learn both conditional and unconditional 3D head models from randomly sampled 2D images alone, without using multi-view data, 3D supervision, or intermediate view generation. We introduce MVCHead, a single-shot state space model that enforces multi-view consistency (MVC) directly in the 3D representation while regressing 3D Gaussians under these constraints. At its core, we propose a Hierarchical State Space (HiSS) block that progressively refines Gaussians from coarse to fine, while capturing long-range dependencies. Within each HiSS block, we modify Mamba's standard unidirectional scan with the proposed Hierarchical Bi-directional State Scan (HiBiSS) that aligns recurrence with the axes along which multi-view inconsistencies are strongest. Finally, we design an SE(3) Multi-view Critic that judges whether a set of self-renders arises from a single underlying 3D configuration, rewarding cross-view pixel alignment without observing real multi-view pairs. MVCHead achieves state-of-the-art perceptual quality, surpasses prior methods in both texture and geometric consistency, and maintains comparable shape consistency. To demonstrate scalability, we release FaceGS-10K, the first large-scale dataset of ready-to-use 3D Gaussian head assets for training and evaluation of 3D head models. Project Page and code: https://humansensinglab.github.io/MVCHead/

  </details>


- **[COSY: Compositional 3DGS Synthesis for Disentangled Human Head Editing](https://arxiv.org/abs/2605.24114)**  
  *Florian Barthel, Shalini De Mello, Koki Nagano, Wieland Morgenstern, Anna Hilsmann, Peter Eisert*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.24114) · [pdf](https://arxiv.org/pdf/2605.24114.pdf)
  > 💡 针对3DGS头部编辑中语义属性解耦难的问题，用独立成分合成与上下文token实现精准解耦编辑。

  <details><summary>Abstract</summary>

  Recent 3D Gaussian Splatting (3DGS) GANs for human heads synthesize and render photorealistic 3D models in real-time and offer a vast variety in identity and appearance. However, controlling specific semantic attributes such as hair color or glasses remains challenging, as edits in the entangled latent space often induce unintended changes in identity or appearance. Although there are several methods that aim to disentangle the latent space post training by estimating directions that only modify certain features, these methods cannot guarantee complete disentanglement and often require pre-trained classifiers. In our approach, we propose a new generator architecture that synthesizes components, such as hair, skin, glasses, and torso, completely independently. This allows for changing the latent vector for one region while keeping the remaining parts fixed. Further, we achieve this separation using only sparse information such as the hair or skin color, eliminating the requirement of segmentation masks or geometric priors, often seen in prior work. To ensure matching shape and lighting conditions during editing, we allow minimal shared information via context tokens between the independent generators. These tokens even allow us to control the shape and light, without any prior annotation. Compared to existing works on GAN-based generation and editing, our method shows better disentanglement, more precise editing control, and competitive visual quality.

  </details>


- **[ForeSplat: Optimization-Aware Foresight for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.22020)**  
  *Yuke Li, Weihang Liu, Cheng Zhang, Yuefeng Zhang, Jiadi Cui, Zixuan Wang, Junran Ding, Haoyu Wu, Yujiao Shi, Jingyi Yu, Xin Lou*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22020) · [pdf](https://arxiv.org/pdf/2605.22020.pdf)
  > 💡 用MetaGrad优化感知训练使前馈3DGS生成适于快速优化的初始化，缩小了与逐个场景优化的差距。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting models offer fast single-pass reconstruction,but scaling them to match per-scene optimization quality is fundamentally hindered by the scarcity of large-scale 3D annotations. A practical compromise is predict-then-refine,where post-prediction optimization compensates for the limited capacity of the feed-forward network. However,standard feed-forward 3DGS is trained solely for zero-step rendering error,ignoring whether its output constitutes a good initialization for the downstream optimizer. We present ForeSplat,an optimization-aware training framework that equips feed-forward 3DGS models to produce initializations explicitly designed for rapid,effective refinement. By offloading part of the scene-modeling burden to the optimizer,ForeSplat substantially reduces the capacity pressure on the feed-forward model,making high-quality reconstruction feasible even with compact networks. At its core is MetaGrad,a lightweight multi-anchor meta-gradient training rule that bypasses costly higher-order differentiation through the 3DGS optimizer. MetaGrad unrolls a short inner-loop refinement trajectory,samples anchor states,and back-propagates aggregated first-order gradients to the prediction head as a surrogate optimization-aware signal. This fine-tuning adds no inference cost and enables high-quality reconstruction within seconds after a few refinement steps. We instantiate ForeSplat on diverse backbones,including AnySplat,Pi3X,and a distilled variant tailored for edge deployment. Across all tested architectures,a ForeSplat-trained initialization converges in fewer refinement steps and reaches a higher peak reconstruction quality than its vanilla counterpart,even fully converged. The framework consistently bridges the gap between amortized prediction and per-scene optimization,establishing a practical path toward lightweight,high-fidelity 3D reconstruction.

  </details>


- **[GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](https://arxiv.org/abs/2605.20752)**  
  *Zijian Zhang, Yuqing Jiang, Qian Cheng, Xiaofan Li, Si Liu, Ding Zhao, Ping Luo, Weitao Zhou, Haibao Yu*  
  `2026-05-20` · `cs.RO` · [abs](https://arxiv.org/abs/2605.20752) · [pdf](https://arxiv.org/pdf/2605.20752.pdf)
  > 💡 针对VLA策略缺乏3D空间与未来演化建模，提出前馈3D高斯

  <details><summary>Abstract</summary>

  Vision-language-action (VLA) policies have advanced language-conditioned robotic manipulation by transferring semantic priors from pretrained vision-language models to action generation. However, standard action-imitation learning often lacks sufficient modeling of explicit 3D spatial information, dense geometric supervision, and future environment evolution, all critical for precise robotic interaction. To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in. Specifically, we introduce learnable GaussianDream Queries in the encoder, enabling the model to capture current-frame 3D spatial structure and short-horizon future evolution. During training, the latent GaussianDream prefix is processed by a static reconstruction head and a future prediction head to produce current 3D Gaussian scene states and future Gaussian evolution states. The current branch is supervised by RGB rendering and depth, while the future branch uses future RGB, depth, and pseudo 3D scene-flow signals. During inference, GaussianDream discards all auxiliary heads and retains only the learned prefix to condition action generation, without test-time Gaussian reconstruction or future prediction. Experimental results demonstrate that GaussianDream achieves state-of-the-art performance across multiple robotic manipulation benchmarks, reaching \textbf{98.4\%} on LIBERO, \textbf{54.8\%} on RoboCasa Human-50, and \textbf{50.0\%} on real-robot tasks. Compared with existing 3D-enhanced VLA methods, GaussianDream achieves strong accuracy while providing higher inference efficiency than video-based world-model approaches.

  </details>


- **[FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model](https://arxiv.org/abs/2605.19600)**  
  *Jinhan Li, Xijie Huang, Zhaoqi Wang, Yijin Wang, Weiqi Ge, Qiyi He, Mo Zhu, Fei Gao, Yuze Wu, Xin Zhou*  
  `2026-05-19` · `cs.RO` · [abs](https://arxiv.org/abs/2605.19600) · [pdf](https://arxiv.org/pdf/2605.19600.pdf)
  > 💡 采用LLM设计环境与3D高斯溅射生成世界模型，自动化生成多样可扩展的高保真无人机飞行数据。

  <details><summary>Abstract</summary>

  In the field of Vision-Language Navigation (VLN), aerial datasets remain limited in their ability to combine scale, diversity, and realism, often relying on either costly real-world scenes or visually limited simulations. To address these challenges, we introduce FlyMirage, a highly scalable and fully automated data generation pipeline for aerial VLN. Our approach leverages large language models (LLM) as an environment designer to promote scene diversity, paired with a generative world model that instantiates these designs into high-fidelity 3D Gaussian Splatting (3DGS) scenes. To substantially reduce human labor and ensure the feasibility of flight data, FlyMirage automates scene exploration and semantic information acquisition, and further integrates a dynamically feasible planner for uncrewed aerial vehicle (UAV) trajectory generation. Utilizing this toolchain, we generate a large-scale, diverse, and photorealistic aerial VLN dataset, with dynamically feasible flying trajectories, designed to support the development of next-generation embodied navigation models.

  </details>


- **[3D Skew Gaussian Splatting with Any Camera Trajectory Visualization Engine](https://arxiv.org/abs/2605.18334)**  
  *Beizhen Zhao, Yifan Zhou, Gaochao Song, Ziran Yin, Hao Wang*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18334) · [pdf](https://arxiv.org/pdf/2605.18334.pdf)
  > 💡 针对对称高斯分布导致视觉伪影的问题，提出3D偏斜高斯泼洒，通过非

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) has revolutionized real-time photorealistic view synthesis, its fundamental reliance on symmetric Gaussian distributions introduces visual artifacts that hinder accurate spatial data exploration. Specifically, symmetric kernels struggle to capture shape and color discontinuities , which cause blurriness and primitive redundancy that mislead human perception during visual analysis. To address these visualization barriers, we introduce 3D Skew Gaussian Splatting (3DSGS), a novel framework that significantly enhances the structural fidelity and compactness of explicit scene representations. Our key insight lies in extending the standard primitive to a general Skew Gaussian counterpart. This generalized primitive inherits the highly efficient rasterization properties of standard Gaussians while gaining intrinsic asymmetric modeling capabilities. We couple this with an enhanced opacity representation to better handle complex transparency, alongside a depth-aware densification strategy that intelligently manages primitive allocation. Furthermore, to make these advancements actionable for real-world visual analytics, we re-derive the CUDA rasterization pipeline to universally support both symmetric and skew Gaussians, integrating it into a decoupled, free-camera interactive visualization engine. Extensive experiments demonstrate that 3DSGS achieves superior rendering quality and structural compactness, particularly in regions with intricate details, while maintaining the real-time frame rates necessary for fluid interactive exploration. Supplementary derivations and visual results are available at \textbf{\textit{https://3d-skew-gs.github.io/}}.

  </details>


- **[Towards Accurate Single Panoramic 3D Detection: A Semantic Gaussian Centric Approach](https://arxiv.org/abs/2605.14601)**  
  *Kanglin Ning, Yiran Zhao, Wenrui Li, Shaoru Sun, Xingtao Wang, Xiaopeng Fan*  
  `2026-05-14` · `cs.CV` · [abs](https://arxiv.org/abs/2605.14601) · [pdf](https://arxiv.org/pdf/2605.14601.pdf)
  > 💡 针对全景3D检测中离散网格几何不连续问题，提出

  <details><summary>Abstract</summary>

  Three-dimensional object detection in panoramic imagery is crucial for comprehensive scene understanding, yet accurately mapping 2D features to 3D remains a significant challenge. Prevailing methods often project 2D features onto discrete 3D grids, which break geometric continuity and limit representation efficiency. To overcome this limitation, this paper proposes PanoGSDet, a monocular panoramic 3D detection framework built upon continuous semantic 3D Gaussian representations. The proposed framework comprises a panoramic depth estimation component and a semantic Gaussian component. The panoramic depth estimation component extracts the equirectangular semantic and depth features from the monocular panorama input. The semantic Gaussian component includes a semantic Gaussian lifting module that projects spherical features into 3D semantic Gaussians, a semantic Gaussian optimization module that refines these semantic Gaussians, and a Gaussian guided prediction head that generates 3D bounding boxes from optimized Gaussian representations. Extensive experiments on the Structured3D dataset demonstrate that our method significantly outperforms existing methods.

  </details>


- **[Forecast-aware Gaussian Splatting for Predictive 3D Representation in Language-Guided Pick-and-Place Manipulation](https://arxiv.org/abs/2605.11144)**  
  *Kaixin Jia, Jiacheng Xu*  
  `2026-05-11` · `cs.RO` · [abs](https://arxiv.org/abs/2605.11144) · [pdf](https://arxiv.org/pdf/2605.11144.pdf)
  > 💡 提出预测性三维高斯泼溅框架，显式建模任务完成状态，提升语言引导拾放操作成功率。

  <details><summary>Abstract</summary>

  We introduce Forecast-aware Gaussian Splatting (Forecast-GS), a predictive 3D representation framework for language-conditioned robotic manipulation. While recent manipulation systems have made progress by grounding language instructions into robot affordances, value maps, or relational keypoint constraints, they usually reason over the current scene and do not explicitly model the task-completed state. This limitation is critical when success depends on satisfying spatial and semantic goals under partial observations, where the robot must evaluate whether a candidate action leads to a feasible task-consistent outcome. We validate Forecast-GS on real-world pick-and-place manipulation tasks, including Cutter-to-Box, Apple-to-Bowl, and Sponge-to-Tray. For each task, we conduct 25 real-world trials under varied initial object configurations using the same robot platform and sensing setup. Forecast-GS with automatic candidate selection achieves success rates of 21/25, 23/25, and 16/25 on the three tasks, respectively, outperforming the ReKep baseline, which achieves 15/25, 19/25, and 10/25. A diagnostic human-assisted setting further improves success rates to 23/25, 24/25, and 19/25, suggesting that candidate generation is effective while automatic ranking remains imperfect. These results suggest that explicitly forecasting task-completed 3D states enables more reliable action evaluation, while the gap between automatic and human-assisted selection indicates that robust final-state ranking remains an important challenge for fully autonomous manipulation. Overall, Forecast-GS provides an interpretable bridge between language understanding, 3D perception, and robotic manipulation planning.

  </details>


- **[SDTalk: Structured Facial Priors and Dual-Branch Motion Fields for Generalizable Gaussian Talking Head Synthesis](https://arxiv.org/abs/2605.09956)**  
  *Peng Jia, Zhen Xiao, Jia Li, Xueliang Liu, Zhenzhen Hu, Lingyun Yu*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09956) · [pdf](https://arxiv.org/pdf/2605.09956.pdf)
  > 💡 提出SDTalk，利用结构化面部先验和双分支运动场实现单图像3DGS泛化说话头合成，无需个性化训练。

  <details><summary>Abstract</summary>

  High-quality, real-time talking head synthesis remains a fundamental challenge in computer vision. Existing reconstruction- and rendering-based methods typically rely on identity-specific models, limiting cross-identity generalization. To address this issue, we propose SDTalk, a one-shot 3D Gaussian Splatting (3DGS)-based framework that generalizes to unseen identities without personalized training or fine-tuning. Our framework comprises two modules with a two-stage training strategy. In the first stage, we incorporate structured facial priors into the reconstruction module and separately predict 3DGS parameters for visible and occluded regions, enabling complete head reconstruction from a single image. In the second stage, we introduce a dual-branch motion field to model coarse and fine facial dynamics, improving detail fidelity and lip synchronization. Experiments demonstrate that SDTalk surpasses existing methods in both visual quality and inference efficiency.

  </details>


- **[REAP: Reinforcement-Learning End-to-End Autonomous Parking with Gaussian Splatting Simulator for Real2Sim2Real Transfer](https://arxiv.org/abs/2605.08713)**  
  *Changze Li, Zhe Chen, Shaoyu Chen, Lisen Mu, Yijian Li, Yuelong Yu, Qian Zhang, Qing Su, Ming Yang, Tong Qin*  
  `2026-05-09` · `cs.RO` · [abs](https://arxiv.org/abs/2605.08713) · [pdf](https://arxiv.org/pdf/2605.08713.pdf)
  > 💡 提出REAP端到端自动泊车方法，结合SAC强化学习与3DGS仿真器，通过行为克隆和碰撞惩罚实现Real2Sim2Real迁移并提升极端场景性能。

  <details><summary>Abstract</summary>

  In recent years, autonomous parking has made significant advances, yet parking tasks still face challenges in extreme scenarios such as mechanical and dead-end parking slots, often resulting in failures. This is mainly due to traditional parking methods adopting a multistage approach, lacking the ability to optimize the parking problem as a whole. End-to-end methods enable joint optimization across perception and planning modules to eliminate the accumulation of errors, enhancing algorithm performance in extreme scenarios. Although several end-to-end parking methods use imitation or reinforcement learning, the former is limited by data cost and distribution coverage, while the latter suffers from inefficient exploration. To address these challenges, we propose a Reinforcement learning End-to-end Autonomous Parking method (REAP). REAP employs Soft Actor-Critic (SAC) within an asymmetric reinforcement learning framework to improve training efficiency and inference performance. To accelerate model convergence, we distill the capabilities of a rule-based planner into the end-to-end network through behavior cloning. We further introduce a soft predictive collision penalty mechanism to reduce collision rates by penalizing obstacle-approaching actions. To ensure that the trained reinforcement learning network can directly transfer to real-world scenarios, we have established a Real2Sim2Real simulator. In the Real2Sim step, we use 3D Gaussian Splatting (3DGS) to transform real-world scenes into digital scenes. In the Sim2Real step, we deploy the end-to-end model onto the vehicle to bridge the Sim2Real gap. Trained in the 3DGS simulator and deployed on physical vehicles, REAP successfully parks in various types of parking spaces, especially demonstrating the feasibility of end-to-end RL parking in extremely narrow mechanical slots.

  </details>


- **[Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://arxiv.org/abs/2605.04035)**  
  *Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi, Fabio Maninchedda, Dmitry Kostiaev, Artem Sevastopolsky, Vittorio Megaro, Trevor Phillips, Alejandro Blumentals, Shridhar Ravikumar, Mehak Gupta, Reinhard Knothe, Jeronimo Bayer, Matthias Vestner, Simon Schaefer, Thomas Etterlin, Christian Zimmermann, Mathias Deschler, Peter Kaufmann, Stefan Brugger, Sebastian Martin, Brian Amberg, Tom Runia*  
  `2026-05-05` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04035) · [pdf](https://arxiv.org/pdf/2605.04035.pdf)
  > 💡 提出HeadsUp，用编码器-解码器与UV参数化高斯，从多视角捕获大规模重建高质量3D头部，在万级数据集上达SOTA并泛化。

  <details><summary>Abstract</summary>

  We propose HeadsUp, a scalable feed-forward method for reconstructing high-quality 3D Gaussian heads from large-scale multi-camera setups. Our method employs an efficient encoder-decoder architecture that compresses input views into a compact latent representation. This latent representation is then decoded into a set of UV-parameterized 3D Gaussians anchored to a neutral head template. This UV representation decouples the number of 3D Gaussians from the number and resolution of input images, enabling training with many high-resolution input views. We train and evaluate our model on an internal dataset with more than 10,000 subjects, which is an order of magnitude larger than existing multi-view human head datasets. HeadsUp achieves state-of-the-art reconstruction quality and generalizes to novel identities without test-time optimization. We extensively analyze the scaling behavior of our model across identities, views, and model capacity, revealing practical insights for quality-compute trade-offs. Finally, we highlight the strength of our latent space by showcasing two downstream applications: generating novel 3D identities and animating the 3D heads with expression blendshapes.

  </details>


- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784)**  
  *Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner*  
  `2026-05-04` · `cs.CV` · [abs](https://arxiv.org/abs/2605.02784) · [pdf](https://arxiv.org/pdf/2605.02784.pdf)
  > 💡 人体姿态恢复和虚拟形象渲染分离导致几何不准确，提出HumanSplatHMR通过闭环优化联合细化姿态并学习高保真虚拟形象。

  <details><summary>Abstract</summary>

  Accurately recovering human pose and appearance from video is an essential component of scene reconstruction, with applications to motion capture, motion prediction, virtual reality, and digital twinning. Despite significant interest in building realistic human avatars from video, this paper demonstrates that existing methods do not accurately recover the 3D geometry of humans. ViT-based approaches are not consistently reliable and can overfit to 2D views, while NeRF- and Gaussian Splatting-based avatars treat pose and appearance separately, limiting rendering generalization to new poses. To resolve these shortcomings, this paper proposes HumanSplatHMR, a joint optimization framework that refines 3D human poses while simultaneously learning a high-fidelity avatar for novel-view and novel-pose synthesis. Our key insight is to close the loop between geometric pose estimation and differentiable rendering. Unlike prior human avatar methods that rely on accurate human pose obtained through motion capture systems or offline refinement, which are impractical in in-the-wild scenarios, our approach uses only human mesh estimates from a state-of-the-art human pose estimator to better reflect real-world conditions. Therefore, instead of using the human pose only as a deformation prior, HumanSplatHMR backpropagates photometric, segmentation, and depth losses through a differentiable renderer to the pose parameters and global position. This coupling refines the global 3D pose over time, improving accuracy and alignment while producing better renderings from novel views. Experiments show consistent improvements over pose recovery baselines that omit image-level refinement and avatar baselines that decouple pose estimation from avatar reconstruction.

  </details>


- **[GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.02086)**  
  *Baobing Zhang, Wanxin Sui*  
  `2026-05-03` · `cs.LG` · [abs](https://arxiv.org/abs/2605.02086) · [pdf](https://arxiv.org/pdf/2605.02086.pdf)
  > 💡 针对3DGS压缩中手工阈值与分阶段短板，提出端到端联合结构化剪枝与量化框架GETA-3DGS，利用QADG、渲染感知显著性及异构混合精度实现自动压缩。

  <details><summary>Abstract</summary>

  3D Gaussian splatting (3DGS) is a state-of-the-art representation for real-time photorealistic novel-view synthesis, yet a single high-fidelity scene typically occupies hundreds of megabytes to several gigabytes, exceeding the budgets of mobile, immersive, and volumetric video platforms. Existing 3DGS compression methods (e.g., HAC++, FlexGaussian, LP-3DGS) treat pruning, quantization, and entropy coding as separate stages and rely on hand-tuned heuristics (opacity thresholds, fixed bit-widths, SH truncation), limiting cross-scene generalization and preventing users from specifying a target rate or quality budget. We propose GETA-3DGS, to our knowledge the first end-to-end automatic joint structured pruning and quantization framework for 3DGS. Building on GETA for joint pruning-quantization of deep networks, we contribute: (i) a 3DGS-aware quantization-aware dependency graph (QADG) treating each Gaussian primitive as a group with five attribute sub-nodes and degree-aware SH sub-nodes; (ii) a render-aware saliency fusing transmittance-weighted contribution, screen-space gradient, and pixel coverage into a Gaussian-level importance score; and (iii) a heterogeneous per-attribute mixed-precision scheme co-optimized with structural sparsity under a projected partial saliency-guided (PPSG) descent guarantee. On Mip-NeRF 360, Tanks and Temples, and Deep Blending, GETA-3DGS operates directly on raw Gaussian primitives rather than a post-hoc anchor representation, delivering ~5x storage reduction over Vanilla 3DGS with no per-scene thresholds. Bit-width policy is the dominant rate-distortion lever: a uniform 6-bit cap costs up to -6.74 dB on view-dependent scenes versus our heterogeneous allocation, matching an information-theoretic reverse-water-filling analysis we develop. GETA-3DGS is complementary to existing codecs: entropy coding (HAC++, CompGS) is downstream, so the two can be composed.

  </details>


- **[Semantic Foam: Unifying Spatial and Semantic Scene Decomposition](https://arxiv.org/abs/2604.26262)**  
  *Amr Sharafeldin, Shrisudhan Govindarajan, Thomas Walker, Aryan Mikaeili, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26262) · [pdf](https://arxiv.org/pdf/2604.26262.pdf)
  > 💡 提出基于Voronoi网格和显式语义特征场的语义分解方法，通过空间正则化提升分割一致性，优于现有技术。

  <details><summary>Abstract</summary>

  Modern scene reconstruction methods, such as 3D Gaussian Splatting, deliver photo-realistic novel view synthesis at real-time speeds, yet their adoption in interactive graphics applications has been limited. A major bottleneck is the difficulty of interacting with these representations compared to traditional, human-authored 3D assets. While previous research has attempted to impose semantic decomposition on these models, significant challenges remain regarding segmentation quality and consistency. To address this, we introduce Semantic Foam, extending the recently proposed Radiant Foam representations to semantic decomposition tasks. Our approach integrates the natural spatial volumetric decomposition of Radiant Foam's Voronoi mesh with an explicit semantic feature field parameterized at the cell level. This explicit structure enables direct spatial regularization, which prevents artifacts caused by occlusion or inconsistent supervision across views - common pitfalls for other point-based representations. Experimental results show that our method achieves superior object-level segmentation performance compared to state-of-the-art methods like Gaussian Grouping and SAGA.

  </details>


- **[Light 'em Up: Enabling Few-Shot Low-Light 3D Gaussian Splatting with Multi-Scale Explicit Retinex Illumination Decoupling](https://arxiv.org/abs/2604.24053)**  
  *YuHao Yin, Zongji Wang, Yuanben Zhang, Biqing Li, Jiesong Bai, Junyi Liu*  
  `2026-04-27` · `cs.CV` · [abs](https://arxiv.org/abs/2604.24053) · [pdf](https://arxiv.org/pdf/2604.24053.pdf)
  > 💡 针对低光360度新视图合成问题，提出MERID-GS框架，通过多尺度显式Retinex光照解

  <details><summary>Abstract</summary>

  Full 360$^\circ$ novel view synthesis under low-light conditions remains challenging. Insufficient illumination, noise amplification, and view-dependent photometric inconsistencies prevent existing methods from jointly preserving geometric consistency and photorealism. Unsupervised approaches often exhibit color drift under large viewpoint variations, while supervised low-light enhancement models, though effective for 2D tasks, struggle to generalize to new scenes and typically require retraining. To address this issue, we propose MERID-GS, a Multi-Scale Explicit Retinex Illumination-Decoupled Gaussian framework for low-light 360$^\circ$ synthesis. Based on Retinex theory, the method explicitly separates illumination and reflectance, and suppresses noise propagation while enhancing dark-region structures via a learnable gain and Illumination-State-Guided Frequency Gating. Combined with lightweight Reflection Head and 3D Gaussian Splatting, MERID-GS adapts to new scenes with only a few shots and enables stable low-light novel view synthesis from sparse-view observations. In addition, we construct a low-light multi-view dataset covering full 360$^\circ$ scenes for joint evaluation. Thorough experiments across multiple datasets in this area demonstrate that MERID-GS achieves SOTA performance, exhibiting superior cross-scene generalization and view consistency. The source code and pre-trained models are available at https://github.com/YhuoyuH/MERID-GS..

  </details>


- **[DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures](https://arxiv.org/abs/2604.21631)**  
  *Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen*  
  `2026-04-23` · `cs.CV` · [abs](https://arxiv.org/abs/2604.21631) · [pdf](https://arxiv.org/pdf/2604.21631.pdf)
  > 💡 利用重建失败生成伪掩码引导二次优化，解决3DGS在瞬态物体干扰下的性能退化问题，效果显著。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) achieves real-time photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency. Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks. We address this challenge with DualSplat, a Failure-to-Prior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage. We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training. We exploit these failures to construct object-level pseudo-masks by combining photometric residuals, feature mismatches, and SAM2 instance boundaries. These pseudo-masks then guide a clean second-pass 3DGS optimization, while a lightweight MLP refines them online by gradually shifting from prior supervision to self-consistency. Experiments on RobustNeRF and NeRF On-the-go show that DualSplat outperforms existing baselines, demonstrating particularly clear advantages in transient-heavy scenes and transient regions.

  </details>


- **[SketchFaceGS: Real-Time Sketch-Driven Face Editing and Generation with Gaussian Splatting](https://arxiv.org/abs/2604.19202)**  
  *Bo Li, Jiahao Kang, Yubo Ma, Feng-Lin Liu, Bin Liu, Fang-Lue Zhang, Lin Gao*  
  `2026-04-21` · `cs.GR` · [abs](https://arxiv.org/abs/2604.19202) · [pdf](https://arxiv.org/pdf/2604.19202.pdf)
  > 💡 针对草图生成与编辑3D高斯人头困难，提出粗到细架构与UV特征增强，实现实时高保真编辑。

  <details><summary>Abstract</summary>

  3D Gaussian representations have emerged as a powerful paradigm for digital head modeling, achieving photorealistic quality with real-time rendering. However, intuitive and interactive creation or editing of 3D Gaussian head models remains challenging. Although 2D sketches provide an ideal interaction modality for fast, intuitive conceptual design, they are sparse, depth-ambiguous, and lack high-frequency appearance cues, making it difficult to infer dense, geometrically consistent 3D Gaussian structures from strokes - especially under real-time constraints. To address these challenges, we propose SketchFaceGS, the first sketch-driven framework for real-time generation and editing of photorealistic 3D Gaussian head models from 2D sketches. Our method uses a feed-forward, coarse-to-fine architecture. A Transformer-based UV feature-prediction module first reconstructs a coarse but geometrically consistent UV feature map from the input sketch, and then a 3D UV feature enhancement module refines it with high-frequency, photorealistic detail to produce a high-fidelity 3D head. For editing, we introduce a UV Mask Fusion technique combined with a layer-by-layer feature-fusion strategy, enabling precise, real-time, free-viewpoint modifications. Extensive experiments show that SketchFaceGS outperforms existing methods in both generation fidelity and editing flexibility, producing high-quality, editable 3D heads from sketches in a single forward pass.

  </details>


- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875)**  
  *Sadia Mubashshira, Nazanin Amini, Kevin Desai*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15875) · [pdf](https://arxiv.org/pdf/2604.15875.pdf)
  > 💡 提出基于高斯泼溅的神经渲染框架，用分离的身体和衣物高斯层解耦重建，通过物理约束提升衣物真实感，实现高质量

  <details><summary>Abstract</summary>

  We present Cloth-HUGS, a Gaussian Splatting based neural rendering framework for photorealistic clothed human reconstruction that explicitly disentangles body and clothing. Unlike prior methods that absorb clothing into a single body representation and struggle with loose garments and complex deformations, Cloth-HUGS represents the performer using separate Gaussian layers for body and cloth within a shared canonical space. The canonical volume jointly encodes body, cloth, and scene primitives and is deformed through SMPL-driven articulation with learned linear blend skinning weights. To improve cloth realism, we initialize cloth Gaussians from mesh topology and apply physics-inspired constraints, including simulation-consistency, ARAP regularization, and mask supervision. We further introduce a depth-aware multi-pass rendering strategy for robust body-cloth-scene compositing, enabling real-time rendering at over 60 FPS. Experiments on multiple benchmarks show that Cloth-HUGS improves perceptual quality and geometric fidelity over state-of-the-art baselines, reducing LPIPS by up to 28% while producing temporally coherent cloth dynamics.

  </details>


- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856)**  
  *Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13856) · [pdf](https://arxiv.org/pdf/2604.13856.pdf)
  > 💡 使用统一数据集和Plücker感知结构化高斯支架，一步去噪生成完整3D头部头像，兼顾速度与高保真外观。

  <details><summary>Abstract</summary>

  Reconstructing a complete 3D head from a single portrait remains challenging because existing methods still face a sharp quality-speed trade-off: high-fidelity pipelines often rely on multi-stage processing and per-subject optimization, while fast feed-forward models struggle with complete geometry and fine appearance details. To bridge this gap, we propose Any3DAvatar, a fast and high-quality method for single-image 3D Gaussian head avatar generation, whose fastest setting reconstructs a full head in under one second while preserving high-fidelity geometry and texture. First, we build AnyHead, a unified data suite that combines identity diversity, dense multi-view supervision, and realistic accessories, filling the main gaps of existing head data in coverage, full-head geometry, and complex appearance. Second, rather than sampling unstructured noise, we initialize from a Plücker-aware structured 3D Gaussian scaffold and perform one-step conditional denoising, formulating full-head reconstruction into a single forward pass while retaining high fidelity. Third, we introduce auxiliary view-conditioned appearance supervision on the same latent tokens alongside 3D Gaussian reconstruction, improving novel-view texture details at zero extra inference cost. Experiments show that Any3DAvatar outperforms prior single-image full-head reconstruction methods in rendering fidelity while remaining substantially faster.

  </details>


- **[3DRealHead: Few-Shot Detailed Head Avatar](https://arxiv.org/abs/2604.13171)**  
  *Jalees Nehvi, Timo Bolkart, Thabo Beeler, Justus Thies*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13171) · [pdf](https://arxiv.org/pdf/2604.13171.pdf)
  > 💡 针对头部身份和表情细节缺失问题，提出基于Style U-Net发射3D高斯原语、融合3DMM与

  <details><summary>Abstract</summary>

  The human face is central to communication. For immersive applications, the digital presence of a person should mirror the physical reality, capturing the users idiosyncrasies and detailed facial expressions. However, current 3D head avatar methods often struggle to faithfully reproduce the identity and facial expressions, despite having multi-view data or learned priors. Learning priors that capture the diversity of human appearances, especially, for regions with highly person-specific features, like the mouth and teeth region is challenging as the underlying training data is limited. In addition, many of the avatar methods are purely relying on 3D morphable model-based expression control which strongly limits expressivity. To address these challenges, we are introducing 3DRealHead, a few-shot head avatar reconstruction method with a novel expression control signal that is extracted from a monocular video stream of the subject. Specifically, the subject can take a few pictures of themselves, recover a 3D head avatar and drive it with a consumer-level webcam. The avatar reconstruction is enabled via a novel few-shot inversion process of a 3D human head prior which is represented as a Style U-Net that emits 3D Gaussian primitives which can be rendered under novel views. The prior is learned on the NeRSemble dataset. For animating the avatar, the U-Net is conditioned on 3DMM-based facial expression signals, as well as features of the mouth region extracted from the driving video. These additional mouth features allow us to recover facial expressions that cannot be represented by the 3DMM leading to a higher expressivity and closer resemblance to the physical reality.

  </details>


- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138)**  
  *Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter*  
  `2026-04-13` · `cs.RO` · [abs](https://arxiv.org/abs/2604.11138) · [pdf](https://arxiv.org/pdf/2604.11138.pdf)
  > 💡 利用3D高斯溅射实现视觉域随机化，单目RGB手中重定向训练，成本低且鲁棒。

  <details><summary>Abstract</summary>

  In-hand object reorientation requires precise estimation of the object pose to handle complex task dynamics. While RGB sensing offers rich semantic cues for pose tracking, existing solutions rely on multi-camera setups or costly ray tracing. We present a sim-to-real framework for monocular RGB in-hand reorientation that integrates 3D Gaussian Splatting (3DGS) to bridge the visual sim-to-real gap. Our key insight is performing domain randomization in the Gaussian representation space: by applying physically consistent, pre-rendering augmentations to 3D Gaussians, we generate photorealistic, randomized visual data for object pose estimation. The manipulation policy is trained using curriculum-based reinforcement learning with teacher-student distillation, enabling efficient learning of complex behaviors. Importantly, both perception and control models can be trained independently on consumer-grade hardware, eliminating the need for large compute clusters. Experiments show that the pose estimator trained with 3DGS data outperforms those trained using conventional rendering data in challenging visual environments. We validate the system on a physical multi-fingered hand equipped with an RGB camera, demonstrating robust reorientation of five diverse objects even under challenging lighting conditions. Our results highlight Gaussian splatting as a practical path for RGB-only dexterous manipulation. For videos of the hardware deployments and additional supplementary materials, please refer to the project website: https://rffr.leggedrobotics.com/works/viserdex/

  </details>


- **[Real-Time Human Reconstruction and Animation using Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2604.10259)**  
  *Devdoot Chatterjee, Zakaria Laskar, C. V. Jawahar*  
  `2026-04-11` · `cs.CV` · [abs](https://arxiv.org/abs/2604.10259) · [pdf](https://arxiv.org/pdf/2604.10259.pdf)
  > 💡 提出前馈高斯溅射框架，通过将高斯原语与SMPL-X顶点关联，实现单次前馈下的实时人体重建与动画。

  <details><summary>Abstract</summary>

  We present a generalizable feed-forward Gaussian splatting framework for human 3D reconstruction and real-time animation that operates directly on multi-view RGB images and their associated SMPL-X poses. Unlike prior methods that rely on depth supervision, fixed input views, UV map, or repeated feed-forward inference for each target view or pose, our approach predicts, in a canonical pose, a set of 3D Gaussian primitives associated with each SMPL-X vertex. One Gaussian is regularized to remain close to the SMPL-X surface, providing a strong geometric prior and stable correspondence to the parametric body model, while an additional small set of unconstrained Gaussians per vertex allows the representation to capture geometric structures that deviate from the parametric surface, such as clothing and hair. In contrast to recent approaches such as HumanRAM, which require repeated network inference to synthesize novel poses, our method produces an animatable human representation from a single forward pass; by explicitly associating Gaussian primitives with SMPL-X vertices, the reconstructed model can be efficiently animated via linear blend skinning without further network evaluation. We evaluate our method on the THuman 2.1, AvatarReX and THuman 4.0 datasets, where it achieves reconstruction quality comparable to state-of-the-art methods while uniquely supporting real-time animation and interactive applications. Code and pre-trained models are available at https://github.com/Devdoot57/HumanGS .

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (40) · <a href="topics/generation.md">full list →</a></summary>

- **[TrackRef3D: Multi-View Consistent Track-then-Label for Open-World Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2605.26576)**  
  *Yuyang Tan, Renhe Zhang, Hang Zhang, Ao Li, Xin Tan*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26576) · [pdf](https://arxiv.org/pdf/2605.26576.pdf)
  > 💡 针对3DGS指代分割的多视图不一致和泛化差问题，TrackRef3D提出轨迹感知语义共识与

  <details><summary>Abstract</summary>

  Referring 3D Gaussian Splatting (R3DGS), which utilizes natural language for 3D object segmentation, has emerged as a crucial capability for embodied AI. However, existing methods typically rely on expensive per-scene manual annotation and per-view pseudo mask generation, which suffer from multi-view inconsistency and poor generalization to varying query specificities. To address this, we present TrackRef3D, a fully automatic pipeline that achieves open-world referring segmentation in 3D Gaussian Splatting (3DGS) without manual annotation by introducing a multi-view consistent track-then-label paradigm that fundamentally decouples object discovery from semantic grounding. Specifically, we propose a Trajectory-Aware Semantic Consensus Module (TSCM) which aggregates cross-view predictions via synonymous clustering and trajectory-aware voting to establish a canonical semantic identity, thereby ensuring multi-view consistency. Furthermore, we employ a visibility-aware description generation strategy to mitigate ambiguity and propose a Hybrid Training Strategy (HTS) that jointly optimizes coarse category semantics and fine-grained referential cues to ensure robustness under varying query specificities using a multi-positive contrastive objective. Extensive experiments on benchmarks demonstrate that TrackRef3D achieves state-of-the-art performance.

  </details>


- **[CodecSplat: Ultra-Compact Latent Coding for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.25563)**  
  *Pengpeng Yu, Runqing Jiang, Qi Zhang, Dingquan Li, Jing Wang, Yulan Guo*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25563) · [pdf](https://arxiv.org/pdf/2605.25563.pdf)
  > 💡 针对前馈3DGS场景表示不紧凑，提出CodecSplat对中间2D特征进行熵编码，避免压缩不规则高斯基元，比特率降低一个数量级。

  <details><summary>Abstract</summary>

  While feed-forward 3D Gaussian splatting reconstructs renderable Gaussian primitives from sparse context views without per-scene optimization, existing pipelines do not provide a compact scene representation for storage or transmission. A natural solution is to apply existing 3DGS compression methods to the generated Gaussian primitives. However, this approach operates on the final irregular 3D representation and is decoupled from the internal feature-to-Gaussian generation process, which limits compression efficiency. To address this, we introduce CodecSplat, an ultra-compact latent coding framework for feed-forward 3D Gaussian splatting. CodecSplat first encodes an intermediate 2D Gaussian-generation feature into an entropy-coded scene bitstream. At the decoder, the latent feature is reconstructed and used to predict depth and Gaussian parameters, which are then mapped to 3D Gaussian primitives. Note that, by integrating compression into the feed-forward Gaussian generation pipeline, CodecSplat avoids inefficient compression over irregular 3D Gaussian primitives and allows the codec to exploit the structured intermediate feature representation. We instantiate CodecSplat on a feed-forward Gaussian splatting backbone with depth-guided multi-view feature refinement and a hierarchical learned feature codec. On DL3DV and RealEstate10K datasets, CodecSplat achieves 23.56-26.36 dB and 24.76-27.05 dB PSNR with only 20.00-107.77 KiB and 3.37-12.51 KiB per scene, respectively. This is roughly one order of magnitude smaller than compressing feed-forward generated Gaussian primitives, while preserving controllable rate-distortion behavior.

  </details>


- **[GlowGS: Generative Semantic Feature Learning for 3D Gaussian Splatting in Nighttime Glow Scenes](https://arxiv.org/abs/2605.23602)**  
  *Beibei Lin, Xiao Cao, Jingyuan Guo, Robby T. Tan*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23602) · [pdf](https://arxiv.org/pdf/2605.23602.pdf)
  > 💡 针对夜间发光场景3DGS缺乏结构特征，利用扩散模型和视觉基础模型生成并学习语义特征，提升渲染质量。

  <details><summary>Abstract</summary>

  Existing 3DGS methods effectively render high-quality novel views in clear-day scenes. However, they struggle with night scenes, particularly in glow regions, due to the lack of structural features such as textures and edges, which are key cues for splatting-based reconstruction. To address this problem, we leverage a diffusion model and a Vision Foundation Model (VFM) to compensate for missing structural cues. Our method consists of two key novel ideas: semantic feature generation and novel-view semantic learning. First, semantic feature generation produces high-quality semantic features as implicit structural cues for novel views. Specifically, a diffusion model synthesizes novel views with unknown camera poses from training views, while a VFM evaluates their quality. Once high-quality novel views are identified, the VFM extracts robust features to construct the semantic feature bank. Second, novel-view semantic learning enables 3DGS to optimize rendered novel views without requiring ground truth. It achieves this by extracting semantic features from a rendered novel view, searching the feature bank for the most similar features, and minimizing their distance. This process enforces implicit structural constraints, ensuring semantically coherent, artifact-free rendered views. Extensive experiments demonstrate the effectiveness of our GlowGS in generating semantically accurate 3D views, showing significant improvements over existing methods.

  </details>


- **[Flow-based Gaussian Splatting for Continuous-Scale Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2605.22147)**  
  *Jiangwei Mo, Xi Lu, Hanlin Wu*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22147) · [pdf](https://arxiv.org/pdf/2605.22147.pdf)
  > 💡 针对遥感图像超分推理慢且缺乏连续尺度灵活性，提出FlowGS，结合流匹配与2D高斯泼溅实现高效任意尺度重建。

  <details><summary>Abstract</summary>

  High-resolution remote sensing images (RSIs) are crucial for Earth observation applications, yet acquiring them is often limited by sensor constraints and costs. In recent years, generative super-resolution (SR) methods, particularly diffusion models, have made significant progress. However, they typically require slow iterative inference with 40--1000 steps and exhibit limited flexibility in continuous-scale SR settings. To address these issues, we propose FlowGS, a generative reconstruction framework for arbitrary-scale SR of RSIs. FlowGS models the high-frequency detail representations between high- and low-resolution images and learns a continuous probability flow from noise to detail priors via flow matching (FM) constrained by shortcut consistency, thereby reducing generative complexity and improving inference efficiency. Additionally, we employ 2D Gaussian splatting to construct a continuous feature field, thereby enabling flexible reconstruction at arbitrary query locations. Experimental results show that FlowGS delivers competitive perceptual quality compared with existing methods in both continuous-scale and fixed-scale SR settings, with substantially improved inference efficiency.

  </details>


- **[Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction](https://arxiv.org/abs/2605.22420)**  
  *Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, Raquel Urtasun*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22420) · [pdf](https://arxiv.org/pdf/2605.22420.pdf)
  > 💡 针对大视角下城市重建质量退化，提出扩散引导的通用增强器GenRe，快速修复3D高斯表示，实现鲁棒泛化。

  <details><summary>Abstract</summary>

  Urban scene reconstruction from real-world observations has emerged as a powerful tool for self-driving development and testing. While current neural rendering approaches achieve high-fidelity rendering along the recorded trajectories, their quality degrades significantly under large viewpoint shifts, limiting the applicability for closed-loop simulation. Recent works have shown promising results in using diffusion models to enhance quality at these challenging viewpoints and distill improvements back into 3D representations. However, they often require costly per-scene optimization, and the distilled representations remain fragile and fail to generalize beyond limited synthesized views. To address these limitations, we propose GenRe, a novel diffusion-guided generalizable enhancer for urban scene reconstruction. GenRe takes as input any pretrained 3D Gaussian representation and fixes the deficiencies within a few minutes. By learning to distill generative priors across diverse scenes, GenRe produces robust and high-fidelity representation efficiently that generalizes reliably to challenging unseen viewpoints (e.g., lane change). Experiments show that GenRe outperforms existing methods in both quality and efficiency and benefits various downstream tasks, enabling robust and scalable sensor simulation for autonomous driving.

  </details>


- **[CAdam: Context-Adaptive Moment Estimation for 3D Gaussian Densification in Generative Distillation](https://arxiv.org/abs/2605.20872)**  
  *SeungJeh Chung, Geonho Park, Misong Kim, HyeongYeop Kang*  
  `2026-05-20` · `cs.LG` · [abs](https://arxiv.org/abs/2605.20872) · [pdf](https://arxiv.org/pdf/2605.20872.pdf)
  > 💡 生成蒸馏中3DGS稠密化困境，CAdam利用梯度一阶矩与信噪比门控分离信号噪声，减少85-97%高斯点。

  <details><summary>Abstract</summary>

  Adaptive densification is the engine of 3D Gaussian Splatting (3DGS). However, when transposed to the optimization-based Generative Distillation paradigm, this reconstruction-native mechanism reveals fundamental limitations, resulting in inefficient representations cluttered with redundant primitives. We diagnose this failure as a Densification Dilemma stemming from the stochastic nature of generative guidance: the standard magnitude-based accumulation indiscriminately aggregates transient noise alongside geometric signals, making it difficult to strike a balance between over-densification and under-fitting. To resolve this, we introduce Context-Adaptive Moment Estimation (CAdam), a novel framework that reinterprets densification as a statistically grounded signal verification problem. CAdam leverages the first moment of gradients to exploit the interference principle, where stochastic fluctuations cancel out via destructive interference while consistent geometric drifts accumulate via constructive interference, effectively disentangling the underlying signal from the generative noise floor. This is further augmented by a quantile-based context awareness and an intrinsic Signal-to-Noise Ratio (SNR) gating mechanism, which ensure robust adaptation across optimization stages and enable the soft termination of densification. Extensive experiments across diverse objectives (SDS, ISM, VFDS) and strong generative 3DGS backbones show that CAdam reduces Gaussian count by 85%-97% relative to standard densification while preserving overall comparable perceptual quality. These results highlight signal-aware density control as a practical way to improve memory efficiency in optimization-based generative distillation.

  </details>


- **[Feed-Forward Gaussian Splatting from Sparse Aerial Views](https://arxiv.org/abs/2605.19949)**  
  *Dongli Wu, Zhuoxiao Li, Tongyan Hua, Yinrui Ren, Xiaobao Wei, Rongjun Qin, Wufan Zhao*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.19949) · [pdf](https://arxiv.org/pdf/2605.19949.pdf)
  > 💡 从稀疏航拍视图重建城市场景，AnyCity通过几何潜码与气动补全令牌生成门控残差更新，实现一致且秒级的前馈3D高斯重建。

  <details><summary>Abstract</summary>

  Reconstructing large-scale urban scenes from sparse aerial views is a crucial yet challenging task. Due to biased top-down and shallow-oblique camera poses, sparse aerial captures exhibit strong evidence imbalance: roofs and open regions are repeatedly observed, while facades, distant buildings, and occluded structures receive little multi-view support. Existing feed-forward 3D Gaussian Splatting methods directly regress a deterministic representation from sparse inputs, but this often leads to ghosting, melted facades, and stretched textures. Recent pseudo-view and video-based generative reconstruction methods use additional supervision or generative priors. However, they often lack a clear separation between observed geometry and prior-driven content, which can lead to plausible but inconsistent structures. We propose AnyCity, an observation-grounded generative reconstruction framework for sparse aerial urban scenes. AnyCity first predicts an observation-supported geometry latent to anchor reliable structures, and then uses scaffold-conditioned aerial completion tokens to predict a gated residual update for weakly constrained content before Gaussian decoding. During training, dense-to-sparse distillation transfers structural cues from dense-view reconstruction, while an aerial-adapted video diffusion prior provides fine-grained urban appearance cues through gated token conditioning. Observation-preserving objectives keep the refined representation consistent with input-supported geometry. At inference time, AnyCity reconstructs the final 3D Gaussian scene from sparse aerial views in a single feed-forward pass, achieving coherent urban novel-view synthesis with second-level inference. Experiments on synthetic, aerial-domain, UAV-textured, and real-world scenes show consistent improvements over feed-forward baselines.

  </details>


- **[GaussianZoom: Progressive Zoom-in Generative 3D Gaussian Splatting with Geometric and Semantic Guidance](https://arxiv.org/abs/2605.18252)**  
  *Jiale Shi, Jiarui Hu, Zesong Yang, Kaixuan Luan, Hujun Bao, Zhaopeng Cui*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18252) · [pdf](https://arxiv.org/pdf/2605.18252.pdf)
  > 💡 针对低分辨率输入的极距放大渲染，提出渐进式3D高斯泼溅，结合几何一致建模与多尺度语义推理，实现高质量多视图一致放大。

  <details><summary>Abstract</summary>

  We introduce GaussianZoom, a generative zoom-in 3D reconstruction system with an iterative progressive framework that combines geometry-consistent scene modeling and multi-scale semantic reasoning to enable high-fidelity extreme zoom-in rendering from low-resolution inputs. To achieve this, we develop a novel multi-view consistent super-resolution module with depth-based feature warping and VLM-driven detail synthesis, ensuring accurate multi-view correspondence while enriching fine-scale appearance beyond the observed resolution. To support zooming across large magnification ranges, we further introduce a new expandable continuous Level-of-Detail hierarchy that dynamically modulates Gaussian visibility for smooth, alias-free cross-scale rendering. Experiments on Mip-NeRF360 and Tanks\&Temples demonstrate that GaussianZoom achieves superior perceptual quality, multi-view consistency, and robustness under extreme magnification, establishing a strong baseline for generative zoom-in 3D scene reconstruction.

  </details>


- **[Eff-WRFGS: Efficient Wireless Radiance Field Using 3D Gaussian Splatting](https://arxiv.org/abs/2605.15324)**  
  *Chenghong Bian, Meng Hua, Deniz Gunduz*  
  `2026-05-14` · `eess.SP` · [abs](https://arxiv.org/abs/2605.15324) · [pdf](https://arxiv.org/pdf/2605.15324.pdf)
  > 💡 针对无线信道建模效率问题，提出基于3DGS的可学习mask剪枝法，实现44倍存储压缩与7倍渲染加速。

  <details><summary>Abstract</summary>

  Wireless channel modeling is a key building block for next-generation wireless systems. Predicting the channel state information (CSI) across different transmitter locations can substantially reduce the pilot and feedback overhead of conventional channel estimation. We propose Eff-WRFGS, an efficient wireless radiance field modeling framework built upon 3D Gaussian Splatting. Eff-WRFGS introduces a learnable mask for each 3D Gaussian primitive to indicate its importance, which guides the pruning of less significant primitives for more efficient rendering. The model is trained using a weighted combination of rendering and regularization losses, allowing a flexible trade-off between rendering quality and efficiency. Numerical results on the $\text{NeRF}^2$ dataset demonstrate that Eff-WRFGS achieves up to 44$\times$ storage reduction and 7$\times$ rendering speed-up with only marginal quality degradation. Moreover, initializing the Gaussian primitives from a 3D point cloud of the scene further improves the entire quality-efficiency trade-off.

  </details>


- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135)**  
  *Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.14135) · [pdf](https://arxiv.org/pdf/2605.14135.pdf)
  > 💡 对稀疏视图室内场景，提出全景补全和平面感知注意力引导，无需训练扩散模型，实现高质量新视角合成，PSNR提升17.8%。

  <details><summary>Abstract</summary>

  We present PanoPlane, an approach for high-fidelity sparse-view indoor novel view synthesis that reconstructs closed room geometry via panoramic scene completion. Unlike perspective-based methods that generate training views from limited fields of view, PanoPlane leverages $360^{\circ}$ panoramic completion to condition the generative process on the full spatial layout. We propose Layout Anchored Attention Steering, a training-free mechanism that steers attention within the diffusion model's internal representation toward scene's detected planar surfaces at inference time. By directing each unobserved region's attention toward geometrically consistent observed content, our method replaces unconstrained hallucination with grounded surface extrapolation. The resulting panoramic completions provide supervision for 3D Gaussian Splatting, enabling accurate novel-view synthesis across unobserved regions from as few as three input views. Experiments on Replica, ScanNet++, and Matterport3D demonstrate state-of-the-art novel view synthesis quality across 3, 6, and 9 input views, achieving up to $+17.8\%$ improvement in PSNR over the current state-of-the-art baseline without any training or fine-tuning of the diffusion model.

  </details>


- **[OCH3R: Object-Centric Holistic 3D Reconstruction](https://arxiv.org/abs/2605.13018)**  
  *Yi Du, Yang You, Xiang Wan, Leonidas Guibas*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13018) · [pdf](https://arxiv.org/pdf/2605.13018.pdf)
  > 💡 提出OCH3R，用Transformer单次前向从单图同时预测所有物体6D姿态与3D高斯重建，实现全前馈且与物体数无关的快速高保真重建。

  <details><summary>Abstract</summary>

  Object-centric scene understanding is a fundamental challenge in computer vision. Existing approaches often rely on multi-stage pipelines that first apply pre-trained segmentors to extract individual objects, followed by per-object 3D reconstruction. Such methods are computationally expensive, fragile to segmentation errors, and scale poorly with scene complexity. We introduce OCH3R, a unified framework for Object-Centric Holistic 3D Reconstruction from a single RGB image. OCH3R performs one forward pass to simultaneously predict all object instances with their 6D poses and detailed 3D reconstructions. The key idea is a transformer architecture that predicts per-pixel attributes, including CLIP-based category embeddings, metric depth, normalized object coordinates (NOCS), and a fixed number of 3D Gaussians representing each object. To supervise these Gaussian reconstructions, we transform them into canonical space using the predicted 6D poses and align them with pre-rendered canonical ground truth, avoiding costly per-image Gaussian label generation. On standard indoor benchmarks, OCH3R achieves state-of-the-art performance across monocular depth estimation, open-vocabulary semantic segmentation, and RGB-only category-level 6D pose estimation, while producing high-fidelity, editable per-object reconstructions. Crucially, inference is fully feed-forward and scales independently of the number of objects, offering orders-of-magnitude speedups over conventional multi-stage pipelines in cluttered scenes.

  </details>


- **[GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://arxiv.org/abs/2605.12399)**  
  *Xiao Cao, Yuze Li, Youmin Zhang, Jiayu Song, Cheng Yan, Wen Li, Lixin Duan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12399) · [pdf](https://arxiv.org/pdf/2605.12399.pdf)
  > 💡 针对稀疏视图下3DGS渲染特征受损导致跨视角检索错误，提出GeoQuery框架，用深度映射构建几何对齐代理查询和局部窗口注意力，实现鲁棒重建。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a prominent paradigm for 3D reconstruction and novel view synthesis. However, it remains vulnerable to severe artifacts when trained under sparse-view constraints. While recent methods attempt to rectify artifacts in rendered views using image diffusion models, they typically rely on multi-view self-attention to retrieve information from reference images. We observe that this mechanism often fails when the rendered novel views output by 3DGS are heavily corrupted: damaged query features lead to erroneous cross-view retrieval, resulting in inconsistent rendering refinement. To address this, we propose GeoQuery, a geometry-guided diffusion framework that integrates generative priors with explicit geometric cues via a novel Geometry-guided Cross-view Attention (GCA) mechanism. First, by leveraging predicted depth maps and camera poses, we construct a geometry-induced correspondence field to sample reference features, forming a geometry-aligned proxy query that replaces the corrupted rendering features. Furthermore, we design a new cross-view feature aggregation pipeline, in which we restrict the cross-view attention to a local window around each proxy query to effectively retrieve useful features while suppressing spurious matches. GeoQuery can be seamlessly integrated into existing diffusion-based pipelines, enabling robust reconstruction even under extreme view sparsity. Extensive experiments on sparse-view novel view synthesis and rendering artifact removal demonstrate the effectiveness of our approach.

  </details>


- **[PoseCompass: Intelligent Synthetic Pose Selection for Visual Localization](https://arxiv.org/abs/2605.12144)**  
  *Yanan Zhou, Zhaoyan Qian, Yanli Li, Nan Yang, Zhongliang Guo, Dong Yuan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12144) · [pdf](https://arxiv.org/pdf/2605.12144.pdf)
  > 💡 针对APR数据质量与冗余问题，提出PoseCompass智能姿态选择管道，融合三类评分机制，实现3倍加速与53.8%误差降低。

  <details><summary>Abstract</summary>

  In visual localization, Absolute Pose Regression (APR) enables real-time 6-DoF camera pose inference from single images, yet critically depends on fine-tuning data quality and coverage. While recent methods leverage 3D Gaussian Splatting (3DGS) for novel view synthesis-based data augmentation, random sampling generates redundant views and noisy samples from poorly reconstructed regions. To mitigate this research gap, we propose PoseCompass, an intelligent pose selection pipeline for 3DGS-based APR. PoseCompass formulates synthetic pose selection and derives a value-based pose ranking mechanism to identify informative poses. The ranking integrates three dimensions: Localization Difficulty, favoring challenging regions; Coverage Novelty, exploring under-sampled areas; and Rendering Observability, filtering artifacts and noise. PoseCompass then generates trajectory-constrained candidates, selects the top-K ranked poses, and synthesizes views using 3DGS with lightweight diffusion-based alignment. Finally, the pose regressor is fine-tuned on mixed real and synthetic data. We evaluate PoseCompass on 7-Scenes, where it reduces adaptation time from 15.2 to 5.1 minutes, a 3x speedup, while cutting median pose errors by 53.8 percent and significantly outperforming random baselines.

  </details>


- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424)**  
  *Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11424) · [pdf](https://arxiv.org/pdf/2605.11424.pdf)
  > 💡 稀疏视图下3DGS退化，VidSplat利用几何引导视频扩散先验迭代合成视角，实现鲁棒场景重建。

  <details><summary>Abstract</summary>

  Gaussian Splatting has achieved remarkable progress in multi-view surface reconstruction, yet it exhibits notable degradation when only few views are available. Although recent efforts alleviate this issue by enhancing multi-view consistency to produce plausible surfaces, they struggle to infer unseen, occluded, or weakly constrained regions beyond the input coverage. To address this limitation, we present VidSplat, a training-free generative reconstruction framework that leverages powerful video diffusion priors to iteratively synthesize novel views that compensate for missing input coverage, and thereby recover complete 3D scenes from sparse inputs. Specifically, we tackle two key challenges that enable the effective integration of generation and reconstruction. First, for 3D consistent generation, we elaborate a training-free, stage-wise denoising strategy that adaptively guides the denoising direction toward the underlying geometry using the rendered RGB and mask images. Second, to enhance the reconstruction, we develop an iterative mechanism that samples camera trajectories, explores unobserved regions, synthesizes novel views, and supplements training through confidence weighted refinement. VidSplat performs robustly to sparse input and even a single image. Extensive experiments on widely used benchmarks demonstrate our superior performance in sparse-view scene reconstruction.

  </details>


- **[PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266)**  
  *Zachary Lee, Maxwell Jacobson, Yexiang Xue*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11266) · [pdf](https://arxiv.org/pdf/2605.11266.pdf)
  > 💡 3DGS缺乏物理理解，提出可微物理仿真耦合3D高斯，用物理目标引导形状优化，生成视觉逼真且物理功能正确的结构。

  <details><summary>Abstract</summary>

  Recent advances in Gaussian Splatting have enabled fast, high-fidelity 3D scene generation, yet these methods remain purely visual and lack an understanding of how shapes behave in the physical world. We introduce Physics-Guided 3D Gaussian Splatting (PG-3DGS), a framework that couples differentiable physics simulation with 3D Gaussian representations to generate 3D structures satisfying physics functionalities. By allowing physical objectives to guide the shape optimization process alongside visual losses, our approach produces geometries that are not only photometrically accurate but also physically functional. The model learns to adjust shapes so that the generated objects exhibit physically meaningful behaviors, for example, teapots that can pour and airplanes that can generate lift, without sacrificing visual quality. Experiments on pouring and aerodynamic lift tasks show that PG-3DGS improves physical functionality while preserving visual quality. In addition to simulation gains, bench-top physical lift tests with 3D-printed aircraft (Cessna, B-2 Spirit, and paper plane) under identical airflow conditions show higher scale-measured lift for PG-3DGS, generated structures than an appearance-matching baseline in all three cases. Our unified framework connects appearance-based reconstruction with physics-based reasoning, enabling end-to-end generation of 3D structures that both look realistic and function correctly.

  </details>


- **[ConFixGS: Learning to Fix Feedforward 3D Gaussian Splatting with Confidence-Aware Diffusion Priors in Driving Scenes](https://arxiv.org/abs/2605.09688)**  
  *Rui Song, Tianhui Cai, Markus Gross, Xingcheng Zhou, Zewei Zhou, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma*  
  `2026-05-10` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09688) · [pdf](https://arxiv.org/pdf/2605.09688.pdf)
  > 💡 针对前馈3DGS在驾驶稀疏视图中的修复问题，ConFixGS利用置信度感知扩散先验和重投影交叉检查生成伪目标，显著提升新视角合成质量。

  <details><summary>Abstract</summary>

  Feedforward 3D Gaussian Splatting (3DGS) often struggles in trajectory-based sparse-view driving scenes. Existing Gaussian repair methods mainly target optimization-based 3DGS, while diffusion-based repair is typically restricted to iterative refinement near observed viewpoints, leaving feedforward 3DGS repair underexplored. We propose ConFixGS, a plug-and-play method that learns to fix feedforward 3DGS with confidence-aware diffusion priors. Starting from a pretrained feedforward model, ConFixGS generates diffusion-enhanced local pseudo-targets and validates them through reprojection-based cross-checking against support views. The resulting dense confidence maps guide refinement, enhancing reliable details while suppressing hallucinated or inconsistent evidence. On Waymo, nuScenes, and KITTI, ConFixGS improves challenging novel view synthesis, with PSNR gains of up to 3.68 dB and FID reduced by nearly half. Our results highlight confidence-aware fusion of generative priors and support-view consistency as a key principle for robust feedforward 3D driving scene reconstruction.

  </details>


- **[Generative 3D Gaussians with Learned Density Control](https://arxiv.org/abs/2605.16355)**  
  *Runjie Yan, Yan-Pei Cao, Peng Wang, Ding Liang, Yuan-Chen Guo*  
  `2026-05-08` · `cs.GR` · [abs](https://arxiv.org/abs/2605.16355) · [pdf](https://arxiv.org/pdf/2605.16355.pdf)
  > 💡 提出密度采样高斯，用可学习八叉树密度控制替代固定网格，实现自适应渲染基元与生成建模的统一，单图3D生成SOTA。

  <details><summary>Abstract</summary>

  We present Density-Sampled Gaussians (DeG), a novel 3D representation designed to bridge the gap between adaptive rendering primitives and scalable generative modeling. Unlike existing approaches that constrain 3D Gaussians to fixed voxel grids or arrays, DeG models Gaussian centers as samples from a learnable probability density function defined over an octree. This formulation provides a rigorous mathematical framework for adaptive density control: by jointly optimizing the spatial density and Gaussian attributes under rendering supervision, our model naturally concentrates primitives in regions of high geometric complexity. We achieve this via a new render loss contribution gradient that serves as a fully differentiable analogue to the discrete densification and pruning heuristics used in standard Gaussian Splatting. The resulting representation is highly flexible, supporting variable-resolution decoding from a single latent code by simply adjusting the sampling budget. To enable generative synthesis, we train a latent diffusion model on DeG. We identify a critical challenge in applying diffusion to unordered set-structured latents, which can significantly slow convergence, and propose VecSeq, a canonical re-indexing mechanism that anchors latent tokens to a deterministic 3D Sobol sequence. This transforms the ambiguous set-generation problem into a robust sequence modeling task. Extensive experiments demonstrate that our pipeline achieves state-of-the-art quality in single-image-to-3D generation, combining the structural adaptivity of unstructured primitives with the training stability of grid-based methods.

  </details>


- **[Sparse-to-Complete: From Sparse Image Captures to Complete 3D Scenes](https://arxiv.org/abs/2605.05664)**  
  *Yiyang Shen, Yin Yang, Kun Zhou, Tianjia Shao*  
  `2026-05-07` · `cs.CV` · [abs](https://arxiv.org/abs/2605.05664) · [pdf](https://arxiv.org/pdf/2605.05664.pdf)
  > 💡 针对稀疏输入场景，提出S2C-3D框架，利用扩散模型修复、视图一致性采样和轨迹规划实现完整高保真3D重建。

  <details><summary>Abstract</summary>

  We introduce S2C-3D, a novel sparse-view 3D reconstruction framework for high-fidelity and complete scene reconstruction from as few as six to eight images. Our framework features three components: a specialized diffusion model for scene-specific image restoration, a training-free view-consistency conditioned sampling process in the diffusion model for refined Gaussian optimization, and a camera trajectory planning scheme to ensure comprehensive scene coverage. The specialized diffusion model is developed by finetuning a pretrained architecture on the input views and their corresponding degraded counterparts. The adaptation to the scene distribution allows the model to repair Gaussian renderings while effectively eliminating domain gaps. Meanwhile, the trajectory planning scheme optimizes scene coverage by connecting each newly sampled camera to its two nearest neighbors. By iteratively constructing paths and retaining only those that significantly enhance visibility, the scheme establishes a trajectory that covers the entire scene. To address multi-view conflicts, the view-consistency conditioned sampling process quantifies the consistency between neighboring repaired images. This information is injected as a condition into the sampling process of the frozen diffusion model, facilitating the generation of view-consistent images without additional training. Consequently, our approach produces high-fidelity 3D Gaussians that are robust to artifacts. Experimental results demonstrate that S2C-3D outperforms state-of-the-art methods, constructing high-quality scenes that are free from missing regions, blurring, or other artifacts with very sparse inputs. The source code and data are available at https://gapszju.github.io/S2C-3D.

  </details>


- **[TAIL-Safe: Task-Agnostic Safety Monitoring for Imitation Learning Policies](https://arxiv.org/abs/2605.01195)**  
  *Riad Ahmed, Momotaz Begum*  
  `2026-05-02` · `cs.RO` · [abs](https://arxiv.org/abs/2605.01195) · [pdf](https://arxiv.org/pdf/2605.01195.pdf)
  > 💡 模仿学习策略部署不安全，提出Lipschitz连续Q函数定义安全集，结合3DGS数字孪生，实现任务无关的安全监控与恢复。

  <details><summary>Abstract</summary>

  Recent imitation learning (IL) algorithms such as flow-matching and diffusion policies demonstrate remarkable performance in learning complex manipulation tasks. However, these policies often fail even when operating within their training distribution due to extreme sensitivity to initial conditions and irreducible approximation errors that lead to compounding drift. This makes it unsafe to deploy IL policies in the field where out-of-distribution scenarios are prevalent. A prerequisite for safe deployment is enabling the policy to determine whether it can execute a task the way it was learned from demonstrations. This paper presents TAIL-Safe, a principled approach to identify, for a trained IL policy, a safe set from where the policy empirically succeeds in completing the learned task. We propose a Lipschitz-continuous Q-value function that maps state-action pairs to a long-term safety score based on three short-term task-agnostic criteria: visibility, recognizability, and graspability. The zero-superlevel set of this function characterizes an empirical control invariant set over state-action pairs. When the nominal policy proposes an action outside this set, we apply a recovery mechanism inspired by Nagumo's theorem that uses gradient ascent to the Q-function to steer the policy back to safety. To learn this Q-function, we construct a high-fidelity digital twin using Gaussian Splatting that enables systematic collection of failure data without risk to physical hardware. Experiments with a Franka Emika robot demonstrate that flow-matching policies, which fail under run-time perturbations, achieve consistent task success when guided by the proposed TAIL-Safe.

  </details>


- **[SandSim: Curve-Guided Gaussian Splatting for Reconstructing Sand Painting Processes](https://arxiv.org/abs/2604.27572)**  
  *Yilin Wang, Haojie Huang, Chen Li, Yang Li, Changbo Wang, Chenhui Li*  
  `2026-04-30` · `cs.GR` · [abs](https://arxiv.org/abs/2604.27572) · [pdf](https://arxiv.org/pdf/2604.27572.pdf)
  > 💡 针对单图沙画过程重建缺乏结构连贯问题，提出曲线引导高斯表示和各向异性基元，联合优化几何

  <details><summary>Abstract</summary>

  Sand painting is a process-driven art where visual appearance emerges from granular accumulation. Given a single image, reconstructing a plausible sand painting process requires modeling coherent stroke structures and material-dependent effects. Existing methods, including stroke-based optimization and diffusion-based video synthesis, often lack structural coherence and material consistency, leading to unrealistic drawing sequences. We present SandSim, a framework that reconstructs a sand painting process from a single image. We introduce a curve-guided Gaussian representation that models strokes as sequences of anisotropic primitives along continuous trajectories, whose smooth kernels capture the soft boundaries of sand strokes and enable coherent stroke formation. We further adopt a subtractive compositing scheme to model light attenuation during sand accumulation. We incorporate a semantic-guided planning module for scene decomposition and drawing order inference. Our framework jointly optimizes stroke geometry and appearance and can be integrated with a physics-based simulator for interactive sand dynamics and editing. Experiments show that our method produces temporally coherent and visually realistic results, achieving improved reconstruction quality and perceptual fidelity compared to existing approaches.

  </details>


- **[Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2604.27422)**  
  *Wongi Park, Jordan A. James, Myeongseok Nam, Minjae Lee, Soomok Lee, Sang-Hyun Lee, William J. Beksi*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.27422) · [pdf](https://arxiv.org/pdf/2604.27422.pdf)
  > 💡 针对无约束场景稀疏视图含干扰物问题，引入扩散模型参考引导细化及伪视图生成与稀疏感知复制，高质量3D渲染性能提升显著。

  <details><summary>Abstract</summary>

  We propose a 3D novel sparse-view synthesis framework for unconstrained real-world scenarios that contain distractors. Unlike existing methods that primarily perform novel-view synthesis from a sparse set of constrained images without transient elements or leverage unconstrained dense image collections to enhance 3D representation in real-world scenarios, our method not only effectively tackles sparse unconstrained image collections, but also shows high-quality 3D rendering results. To do this, we introduce reference-guided view refinement with a diffusion model using a transient mask and a reference image to enhance the 3D representation and mitigate artifacts in rendered views. Furthermore, we address sparse regions in the Gaussian field via pseudo-view generation along with a sparsity-aware Gaussian replication strategy to amplify Gaussians in the sparse regions. Extensive experiments on publicly available datasets demonstrate that our methodology consistently outperforms existing methods (e.g., PSNR - 17.2%, SSIM - 10.8%, LPIPS - 4.0%) and provides high-fidelity 3D rendering results. This advancement paves the way for realizing unconstrained real-world scenarios without labor-intensive data acquisition. Our project page is available at $\href{https://robotic-vision-lab.github.io/SaveWildGS/}{here}$

  </details>


- **[GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning](https://arxiv.org/abs/2604.25459)**  
  *Yufei Jia, Heng Zhang, Ziheng Zhang, Junzhe Wu, Mingrui Yu, Zifan Wang, Dixuan Jiang, Zheng Li, Chenyu Cao, Zhuoyuan Yu, Xun Yang, Haizhou Ge, Yuchi Zhang, Jiayuan Zhang, Zhenbiao Huang, Tianle Liu, Shenyu Chen, Jiacheng Wang, Bin Xie, Xuran Yao, Xiwa Deng, Guangyu Wang, Jinzhi Zhang, Lei Hao, Zhixing Chen, Yuxiang Chen, Anqi Wang, Hongyun Tian, Yiyi Yan, Zhanxiang Cao, Yizhou Jiang, Hanyang Shao, Yue Li, Lu Shi, Bokui Chen, Wei Sui, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Guyue Zhou*  
  `2026-04-28` · `cs.RO` · [abs](https://arxiv.org/abs/2604.25459) · [pdf](https://arxiv.org/pdf/2604.25459.pdf)
  > 💡 提出高通量视觉仿真框架，集成并行物理引擎与3DGS渲染，实现10^4 FPS及自动Real2Sim，加速视觉机器人学习。

  <details><summary>Abstract</summary>

  Embodied AI research is undergoing a shift toward vision-centric perceptual paradigms. While massively parallel simulators have catalyzed breakthroughs in proprioception-based locomotion, their potential remains largely untapped for vision-informed tasks due to the prohibitive computational overhead of large-scale photorealistic rendering. Furthermore, the creation of simulation-ready 3D assets heavily relies on labor-intensive manual modeling, while the significant sim-to-real physical gap hinders the transfer of contact-rich manipulation policies. To address these bottlenecks, we propose GS-Playground, a multi-modal simulation framework designed to accelerate end-to-end perceptual learning. We develop a novel high-performance parallel physics engine, specifically designed to integrate with a batch 3D Gaussian Splatting (3DGS) rendering pipeline to ensure high-fidelity synchronization. Our system achieves a breakthrough throughput of 10^4 FPS at 640x480 resolution, significantly lowering the barrier for large-scale visual RL. Additionally, we introduce an automated Real2Sim workflow that reconstructs photorealistic, physically consistent, and memory-efficient environments, streamlining the generation of complex simulation-ready scenes. Extensive experiments on locomotion, navigation, and manipulation demonstrate that GS-Playground effectively bridges the perceptual and physical gaps across diverse embodied tasks. Project homepage: https://gsplayground.github.io.

  </details>


- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994)**  
  *Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi*  
  `2026-04-27` · `cs.GR` · [abs](https://arxiv.org/abs/2604.24994) · [pdf](https://arxiv.org/pdf/2604.24994.pdf)
  > 💡 将V

  <details><summary>Abstract</summary>

  We introduce a differentiable 3D representation that unifies the ray tracing capabilities of foam-based ray tracing with the efficiency of modern rasterization pipelines. While prior foam representations enable constant-time ray traversal through an explicit volumetric partition of space, their potentially unbounded cells hinder efficient tile-based rasterization. We address this limitation by generalizing Voronoi foams to bounded power diagrams with controllable cell extents, enabling spatially bounded primitives without requiring expensive Delaunay triangulations during training. We further introduce an oriented surface formulation that explicitly models interfaces between interior and exterior regions, and decouple geometry from appearance by embedding differentiable texture directly on these surfaces. Together, these contributions yield a representation that preserves state-of-the-art ray tracing efficiency while achieving rasterization performance competitive with current generation 3DGS, providing a practical path toward unified real-time differentiable rendering.

  </details>


- **[GS-DOT: Gaussian splatting-based image reconstruction for diffuse optical tomography](https://arxiv.org/abs/2604.23675)**  
  *Jingjing Jiang*  
  `2026-04-26` · `eess.IV` · [abs](https://arxiv.org/abs/2604.23675) · [pdf](https://arxiv.org/pdf/2604.23675.pdf)
  > 💡 首次将高斯散点引入光子扩散领域，用各向异性高斯基元优化拟合点扩散函数实现高精度重建，降低内存。

  <details><summary>Abstract</summary>

  This work presents GS-DOT, a novel image reconstruction framework based on Gaussian Splatting (GS) for diffuse optical tomography (DOT). Inspired by GS for rendering applications, absorption coefficients are represented as a sparse sum of anisotropic Gaussian primitives optimized to fit measured time-resolved point-spread functions through analytic gradients and Adam optimization. This is the first adaptation of GS algorithms in the photon diffusion regime, where the ray transport function is replaced by the diffusion functions to enable accurate modeling of light transport in highly scattering media. Validation on synthetic tissue models demonstrate high accuracy in localization and quantification of reconstructed absorption maps for both clean and noisy signals. GS-DOT has demonstrated high robustness to noise and showed a huge reduction in memory demand.

  </details>


- **[DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction](https://arxiv.org/abs/2604.21518)**  
  *Shiyan Su, Ruyi Zha, Danli Shi, Hongdong Li, Xuelian Cheng*  
  `2026-04-23` · `eess.IV` · [abs](https://arxiv.org/abs/2604.21518) · [pdf](https://arxiv.org/pdf/2604.21518.pdf)
  > 💡 稀疏视角CT重建中神经表示有伪影，提出DiffNR框架利用扩散先验和单步扩散模型SliceFixer修复，显著提升PSNR并保持高效优化。

  <details><summary>Abstract</summary>

  Neural representations (NRs), such as neural fields and 3D Gaussians, effectively model volumetric data in computed tomography (CT) but suffer from severe artifacts under sparse-view settings. To address this, we propose DiffNR, a novel framework that enhances NR optimization with diffusion priors. At its core is SliceFixer, a single-step diffusion model designed to correct artifacts in degraded slices. We integrate specialized conditioning layers into the network and develop tailored data curation strategies to support model finetuning. During reconstruction, SliceFixer periodically generates pseudo-reference volumes, providing auxiliary 3D perceptual supervision to fix underconstrained regions. Compared to prior methods that embed CT solvers into time-consuming iterative denoising, our repair-and-augment strategy avoids frequent diffusion model queries, leading to better runtime performance. Extensive experiments show that DiffNR improves PSNR by 3.99 dB on average, generalizes well across domains, and maintains efficient optimization.

  </details>


- **[FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038)**  
  *Haitao Huang, Shin-Fang Chng, Huangying Zhan, Qingan Yan, Yi Xu*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20038) · [pdf](https://arxiv.org/pdf/2604.20038.pdf)
  > 💡 针对测试时优化耗时且视图不一致问题，提出前馈框架结合跨视图正则化，实现稀疏视图3D编辑，极大加速推理。

  <details><summary>Abstract</summary>

  Recent advances in text-guided image editing and 3D Gaussian Splatting (3DGS) have enabled high-quality 3D scene manipulation. However, existing pipelines rely on iterative edit-and-fit optimization at test time, alternating between 2D diffusion editing and 3D reconstruction. This process is computationally expensive, scene-specific, and prone to cross-view inconsistencies. We propose a feed-forward framework for cross-view consistent 3D scene editing from sparse views. Instead of enforcing consistency through iterative 3D refinement, we introduce a cross-view regularization scheme in the image domain during training. By jointly supervising multi-view edits with geometric alignment constraints, our model produces view-consistent results without per-scene optimization at inference. The edited views are then lifted into 3D via a feedforward 3DGS model, yielding a coherent 3DGS representation in a single forward pass. Experiments demonstrate competitive editing fidelity and substantially improved cross-view consistency compared to optimization-based methods, while reducing inference time by orders of magnitude.

  </details>


- **[Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468)**  
  *Tianshi Cao, Jiawei Ren, Yuxuan Zhang, Jaewoo Seo, Jiahui Huang, Shikhar Solanki, Haotian Zhang, Mingfei Guo, Haithem Turki, Muxingzi Li, Yue Zhu, Sipeng Zhang, Zan Gojcic, Sanja Fidler, Kangxue Yin*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18468) · [pdf](https://arxiv.org/pdf/2604.18468.pdf)
  > 💡 用稀疏视图多视图生成和3D高斯提升，将自动驾驶日志中的稀疏对象观测转为完整仿真资产

  <details><summary>Abstract</summary>

  Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge, we present Asset Harvester, an image-to-3D model and end-to-end pipeline that converts sparse, in-the-wild object observations from real driving logs into complete, simulation-ready assets. Rather than relying on a single model component, we developed a system-level design for real-world AV data that combines large-scale curation of object-centric training tuples, geometry-aware preprocessing across heterogeneous sensors, and a robust training recipe that couples sparse-view-conditioned multiview generation with 3D Gaussian lifting. Within this system, SparseViewDiT is explicitly designed to address limited-angle views and other real-world data challenges. Together with hybrid data curation, augmentation, and self-distillation, this system enables scalable conversion of sparse AV object observations into reusable 3D assets.

  </details>


- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268)**  
  *Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.14268) · [pdf](https://arxiv.org/pdf/2604.14268.pdf)
  > 💡 提出多模态世界模型HY-World 2.0，从文本/图像/视频生成3DGS场景，通过四阶段流程与多项创新实现开源最优性能。

  <details><summary>Abstract</summary>

  We introduce HY-World 2.0, a multi-modal world model framework that advances our prior project HY-World 1.0. HY-World 2.0 accommodates diverse input modalities, including text prompts, single-view images, multi-view images, and videos, and produces 3D world representations. With text or single-view image inputs, the model performs world generation, synthesizing high-fidelity, navigable 3D Gaussian Splatting (3DGS) scenes. This is achieved through a four-stage method: a) Panorama Generation with HY-Pano 2.0, b) Trajectory Planning with WorldNav, c) World Expansion with WorldStereo 2.0, and d) World Composition with WorldMirror 2.0. Specifically, we introduce key innovations to enhance panorama fidelity, enable 3D scene understanding and planning, and upgrade WorldStereo, our keyframe-based view generation model with consistent memory. We also upgrade WorldMirror, a feed-forward model for universal 3D prediction, by refining model architecture and learning strategy, enabling world reconstruction from multi-view images or videos. Also, we introduce WorldLens, a high-performance 3DGS rendering platform featuring a flexible engine-agnostic architecture, automatic IBL lighting, efficient collision detection, and training-rendering co-design, enabling interactive exploration of 3D worlds with character support. Extensive experiments demonstrate that HY-World 2.0 achieves state-of-the-art performance on several benchmarks among open-source approaches, delivering results comparable to the closed-source model Marble. We release all model weights, code, and technical details to facilitate reproducibility and support further research on 3D world models.

  </details>


- **[Dehaze-then-Splat: Generative Dehazing with Physics-Informed 3D Gaussian Splatting for Smoke-Free Novel View Synthesis](https://arxiv.org/abs/2604.13589)**  
  *Boss Chen, Hanqing Wang*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13589) · [pdf](https://arxiv.org/pdf/2604.13589.pdf)
  > 💡 针对逐帧去雾导致多视图不一致问题，提出融合物理先验与MCMC密度化的3DGS方法，提升新视图合成质量。

  <details><summary>Abstract</summary>

  We present Dehaze-then-Splat, a two-stage pipeline for multi-view smoke removal and novel view synthesis developed for Track~2 of the NTIRE 2026 3D Restoration and Reconstruction Challenge. In the first stage, we produce pseudo-clean training images via per-frame generative dehazing using Nano Banana Pro, followed by brightness normalization. In the second stage, we train 3D Gaussian Splatting (3DGS) with physics-informed auxiliary losses -- depth supervision via Pearson correlation with pseudo-depth, dark channel prior regularization, and dual-source gradient matching -- that compensate for cross-view inconsistencies inherent in frame-wise generative processing. We identify a fundamental tension in dehaze-then-reconstruct pipelines: per-image restoration quality does not guarantee multi-view consistency, and such inconsistency manifests as blurred renders and structural instability in downstream 3D reconstruction.Our analysis shows that MCMC-based densification with early stopping, combined with depth and haze-suppression priors, effectively mitigates these artifacts. On the Akikaze validation scene, our pipeline achieves 20.98\,dB PSNR and 0.683 SSIM for novel view synthesis, a +1.50\,dB improvement over the unregularized baseline.

  </details>


- **[Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias](https://arxiv.org/abs/2604.13905)**  
  *Zhiyuan Xu, Jiuming Liu, Yuxin Chen, Masayoshi Tomizuka, Chenfeng Xu, Chensheng Peng*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13905) · [pdf](https://arxiv.org/pdf/2604.13905.pdf)
  > 💡 用稀疏3D锚点查询和扩展算子生成3D高斯原语，降低输入视图偏差，显著提升效率与容量。

  <details><summary>Abstract</summary>

  We present SparseGen, a novel framework for efficient image-to-3D generation, which exhibits low input-view bias while being significantly faster. Unlike traditional approaches that rely on dense volumetric grids, triplanes, or pixel-aligned primitives, we model scenes with a compact sparse set of learned 3D anchor queries and a learned expansion operator that decodes each transformed query into a small local set of 3D Gaussian primitives. Trained under a rectified-flow reconstruction objective without 3D supervision, our model learns to allocate representation capacity where geometry and appearance matter, achieving significant reductions in memory and inference time while preserving multi-view fidelity. We introduce quantitative measures of input-view bias and utilization to show that sparse queries reduce overfitting to conditioning views while being representationally efficient. Our results argue that sparse set-latent expansion is a principled, practical alternative for efficient 3D generative modeling.

  </details>


- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578)**  
  *Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu*  
  `2026-04-12` · `cs.CV` · [abs](https://arxiv.org/abs/2604.10578) · [pdf](https://arxiv.org/pdf/2604.10578.pdf)
  > 💡 利用视频扩散模型的时间先验与3DGS耦合，以恢复-优化范式生成全局一致的3D室内场景，显著提升长距离探索质量。

  <details><summary>Abstract</summary>

  The growing demand for Embodied AI and VR applications has highlighted the need for synthesizing high-quality 3D indoor scenes from sparse inputs. However, existing approaches struggle to infer massive amounts of missing geometry in large unseen areas while maintaining global consistency, often producing locally plausible but globally inconsistent reconstructions. We present Rein3D, a framework that reconstructs full 360-degree indoor environments by coupling explicit 3D Gaussian Splatting (3DGS) with temporally coherent priors from video diffusion models. Our approach follows a "restore-and-refine" paradigm: we employ a radial exploration strategy to render imperfect panoramic videos along trajectories starting from the origin, effectively uncovering occluded regions from a coarse 3DGS initialization. These sequences are restored by a panoramic video-to-video diffusion model and further enhanced via video super-resolution to synthesize high-fidelity geometry and textures. Finally, these refined videos serve as pseudo-ground truths to update the global 3D Gaussian field. To support this task, we construct PanoV2V-15K, a dataset of over 15K paired clean and degraded panoramic videos for diffusion-based scene restoration. Experiments demonstrate that Rein3D produces photorealistic and globally consistent 3D scenes and significantly improves long-range camera exploration compared with existing baselines.

  </details>


- **[FreeScale: Scaling 3D Scenes via Certainty-Aware Free-View Generation](https://arxiv.org/abs/2604.10512)**  
  *Chenhan Jiang, Yu Chen, Qingwen Zhang, Jifei Song, Songcen Xu, Dit-Yan Yeung, Jiankang Deng*  
  `2026-04-12` · `cs.CV` · [abs](https://arxiv.org/abs/2604.10512) · [pdf](https://arxiv.org/pdf/2604.10512.pdf)
  > 💡 利用场景重建与确定性感知自由视角采样，将有限真实图像转化为高质量训练数据，显著提升NVS与3DGS性能。

  <details><summary>Abstract</summary>

  The development of generalizable Novel View Synthesis (NVS) models is critically limited by the scarcity of large-scale training data featuring diverse and precise camera trajectories. While real-world captures are photorealistic, they are typically sparse and discrete. Conversely, synthetic data scales but suffers from a domain gap and often lacks realistic semantics. We introduce FreeScale, a novel framework that leverages the power of scene reconstruction to transform limited real-world image sequences into a scalable source of high-quality training data. Our key insight is that an imperfect reconstructed scene serves as a rich geometric proxy, but naively sampling from it amplifies artifacts. To this end, we propose a certainty-aware free-view sampling strategy identifying novel viewpoints that are both semantically meaningful and minimally affected by reconstruction errors. We demonstrate FreeScale's effectiveness by scaling up the training of feedforward NVS models, achieving a notable gain of 2.7 dB in PSNR on challenging out-of-distribution benchmarks. Furthermore, we show that the generated data can actively enhance per-scene 3D Gaussian Splatting optimization, leading to consistent improvements across multiple datasets. Our work provides a practical and powerful data generation engine to overcome a fundamental bottleneck in 3D vision. Project page: https://mvp-ai-lab.github.io/FreeScale.

  </details>


- **[SIC3D: Style Image Conditioned Text-to-3D Gaussian Splatting Generation](https://arxiv.org/abs/2604.08760)**  
  *Ming He, Zhixiang Chen, Steve Maddock*  
  `2026-04-09` · `cs.CV` · [abs](https://arxiv.org/abs/2604.08760) · [pdf](https://arxiv.org/pdf/2604.08760.pdf)
  > 💡 文本到3D生成缺乏可控性，提出SIC3D两阶段管线，用VSSD损失和缩放正则化实现风格迁移，提升几何与纹理保真度。

  <details><summary>Abstract</summary>

  Recent progress in text-to-3D object generation enables the synthesis of detailed geometry from text input by leveraging 2D diffusion models and differentiable 3D representations. However, the approaches often suffer from limited controllability and texture ambiguity due to the limitation of the text modality. To address this, we present SIC3D, a controllable image-conditioned text-to-3D generation pipeline with 3D Gaussian Splatting (3DGS). There are two stages in SIC3D. The first stage generates the 3D object content from text with a text-to-3DGS generation model. The second stage transfers style from a reference image to the 3DGS. Within this stylization stage, we introduce a novel Variational Stylized Score Distillation (VSSD) loss to effectively capture both global and local texture patterns while mitigating conflicts between geometry and appearance. A scaling regularization is further applied to prevent the emergence of artifacts and preserve the pattern from the style image. Extensive experiments demonstrate that SIC3D enhances geometric fidelity and style adherence, outperforming prior approaches in both qualitative and quantitative evaluations.

  </details>


- **[PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis](https://arxiv.org/abs/2604.04576)**  
  *Inseong Choi, Siwoo Lee, Seung-Hun Nam, Soohwan Song*  
  `2026-04-06` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04576) · [pdf](https://arxiv.org/pdf/2604.04576.pdf)
  > 💡 针对扩散生成视图的质量评估难题，提出PR-IQA利用部分参考图进行交叉注意力质量补全，有效筛选高置信区域提升3DGS重建。

  <details><summary>Abstract</summary>

  Diffusion models are promising for sparse-view novel view synthesis (NVS), as they can generate pseudo-ground-truth views to aid 3D reconstruction pipelines like 3D Gaussian Splatting (3DGS). However, these synthesized images often contain photometric and geometric inconsistencies, and their direct use for supervision can impair reconstruction. To address this, we propose Partial-Reference Image Quality Assessment (PR-IQA), a framework that evaluates diffusion-generated views using reference images from different poses, eliminating the need for ground truth. PR-IQA first computes a geometrically consistent partial quality map in overlapping regions. It then performs quality completion to inpaint this partial map into a dense, full-image map. This completion is achieved via a cross-attention mechanism that incorporates reference-view context, ensuring cross-view consistency and enabling thorough quality assessment. When integrated into a diffusion-augmented 3DGS pipeline, PR-IQA restricts supervision to high-confidence regions identified by its quality maps. Experiments demonstrate that PR-IQA outperforms existing IQA methods, achieving full-reference-level accuracy without ground-truth supervision. Thus, our quality-aware 3DGS approach more effectively filters inconsistencies, producing superior 3D reconstructions and NVS results. The project page is available at https://kakaomacao.github.io/pr-iqa-project-page/.

  </details>


- **[M2StyleGS: Multi-Modality 3D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2604.03773)**  
  *Xingyu Miao, Xueqi Qiu, Haoran Duan, Yawen Huang, Xian Wu, Jingjing Deng, Yang Long*  
  `2026-04-04` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03773) · [pdf](https://arxiv.org/pdf/2604.03773.pdf)
  > 💡 利用3DGS与CLIP多模态知识，通过特征对齐和损失函数实现灵活文本图像输入下的实时3D风格迁移，一致性提升32.92%。

  <details><summary>Abstract</summary>

  Conventional 3D style transfer methods rely on a fixed reference image to apply artistic patterns to 3D scenes. However, in practical applications such as virtual or augmented reality, users often prefer more flexible inputs, including textual descriptions and diverse imagery. In this work, we introduce a novel real-time styling technique M2StyleGS to generate a sequence of precisely color-mapped views. It utilizes 3D Gaussian Splatting (3DGS) as a 3D presentation and multi-modality knowledge refined by CLIP as a reference style. M2StyleGS resolves the abnormal transformation issue by employing a precise feature alignment, namely subdivisive flow, it strengthens the projection of the mapped CLIP text-visual combination feature to the VGG style feature. In addition, we introduce observation loss, which assists in the stylized scene better matching the reference style during the generation, and suppression loss, which suppresses the offset of reference color information throughout the decoding process. By integrating these approaches, M2StyleGS can employ text or images as references to generate a set of style-enhanced novel views. Our experiments show that M2StyleGS achieves better visual quality and surpasses the previous work by up to 32.92% in terms of consistency.

  </details>


- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716)**  
  *Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre*  
  `2026-04-04` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03716) · [pdf](https://arxiv.org/pdf/2604.03716.pdf)
  > 💡 针对高开销头发重建，以聚类股线为卡片和共享纹理码本，

  <details><summary>Abstract</summary>

  We present a compact pipeline for high-fidelity hair reconstruction from multi-view images. While recent 3D Gaussian Splatting (3DGS) methods achieve realistic results, they often require millions of primitives, leading to high storage and rendering costs. Observing that hair exhibits structural and visual similarities across a hairstyle, we cluster strands into representative hair cards and group these into shared texture codebooks. Our approach integrates this structure with 3DGS rendering, significantly reducing reconstruction time and storage while maintaining comparable visual quality. In addition, we propose a generative prior accelerated method to reconstruct the initial strand geometry from a set of images. Our experiments demonstrate a 4-fold reduction in strand reconstruction time and achieve comparable rendering performance with over 200x lower memory footprint.

  </details>


- **[VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping](https://arxiv.org/abs/2604.02696)**  
  *Yuhan Zhu, Yanyu Zhang, Jie Xu, Wei Ren*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02696) · [pdf](https://arxiv.org/pdf/2604.02696.pdf)
  > 💡 变分贝叶斯框架将地图与位姿追踪概率化，利用共轭先验闭式更新，解决初始化敏感与漂移问题。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has shown promising results for 3D scene modeling using mixtures of Gaussians, yet its existing simultaneous localization and mapping (SLAM) variants typically rely on direct, deterministic pose optimization against the splat map, making them sensitive to initialization and susceptible to catastrophic forgetting as map evolves. We propose Variational Bayesian Gaussian Splatting SLAM (VBGS-SLAM), a novel framework that couples the splat map refinement and camera pose tracking in a generative probabilistic form. By leveraging conjugate properties of multivariate Gaussians and variational inference, our method admits efficient closed-form updates and explicitly maintains posterior uncertainty over both poses and scene parameters. This uncertainty-aware method mitigates drift and enhances robustness in challenging conditions, while preserving the efficiency and rendering quality of existing 3DGS. Our experiments demonstrate superior tracking performance and robustness in long sequence prediction, alongside efficient, high-quality novel view synthesis across diverse synthetic and real-world scenes.

  </details>


- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207)**  
  *Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01207) · [pdf](https://arxiv.org/pdf/2604.01207.pdf)
  > 💡 用网格引导3DGS编辑，通过多视图锚点合成、有形几何锚定和上下文视频掩蔽，实现高保真部件级场景变换，保持结构完整性。

  <details><summary>Abstract</summary>

  We present TRACE, a mesh-guided 3DGS editing framework that achieves automated, high-fidelity scene transformation. By anchoring video diffusion with explicit 3D geometry, TRACE uniquely enables fine-grained, part-level manipulatio--such as local pose shifting or component replacemen--while preserving the structural integrity of the central subject, a capability largely absent in existing editing methods. Our approach comprises three key stages: (1) Multi-view 3D-Anchor Synthesis, which leverages a sparse-view editor trained on our MV-TRACE datase--the first multi-view consistent dataset dedicated to scene-coherent object addition and modificatio--to generate spatially consistent 3D-anchors; (2) Tangible Geometry Anchoring (TGA), which ensures precise spatial synchronization between inserted meshes and the 3DGS scene via two-phase registration; and (3) Contextual Video Masking (CVM), which integrates 3D projections into an autoregressive video pipeline to achieve temporally stable, physically-grounded rendering. Extensive experiments demonstrate that TRACE consistently outperforms existing methods especially in editing versatility and structural integrity.

  </details>


- **[SVGS: Single-View to 3D Object Editing via Gaussian Splatting](https://arxiv.org/abs/2603.28126)**  
  *Pengcheng Xue, Yan Tian, Qiutao Song, Ziyi Wang, Linyang He, Weiping Ding, Mahmoud Hassaballah, Karen Egiazarian, Wei-Fa Yang, Leszek Rutkowski*  
  `2026-03-30` · `cs.CV` · [abs](https://arxiv.org/abs/2603.28126) · [pdf](https://arxiv.org/pdf/2603.28126.pdf)
  > 💡 提出基于3D高斯泼溅的单视图编辑方法，利用多视图扩散模型保证一致性并显著提升编辑效率。

  <details><summary>Abstract</summary>

  Text-driven 3D scene editing has attracted considerable interest due to its convenience and user-friendliness. However, methods that rely on implicit 3D representations, such as Neural Radiance Fields (NeRF), while effective in rendering complex scenes, are hindered by slow processing speeds and limited control over specific regions of the scene. Moreover, existing approaches, including Instruct-NeRF2NeRF and GaussianEditor, which utilize multi-view editing strategies, frequently produce inconsistent results across different views when executing text instructions. This inconsistency can adversely affect the overall performance of the model, complicating the task of balancing the consistency of editing results with editing efficiency. To address these challenges, we propose a novel method termed Single-View to 3D Object Editing via Gaussian Splatting (SVGS), which is a single-view text-driven editing technique based on 3D Gaussian Splatting (3DGS). Specifically, in response to text instructions, we introduce a single-view editing strategy grounded in multi-view diffusion models, which reconstructs 3D scenes by leveraging only those views that yield consistent editing results. Additionally, we employ sparse 3D Gaussian Splatting as the 3D representation, which significantly enhances editing efficiency. We conducted a comparative analysis of SVGS against existing baseline methods across various scene settings, and the results indicate that SVGS outperforms its counterparts in both editing capability and processing speed, representing a significant advancement in 3D editing technology. For further details, please visit our project page at: https://amateurc.github.io/svgs.github.io.

  </details>


- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053)**  
  *Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni*  
  `2026-03-26` · `cs.CV` · [abs](https://arxiv.org/abs/2603.25053) · [pdf](https://arxiv.org/pdf/2603.25053.pdf)
  > 💡 针对3DGS野外重建伪影问题，用几何感知视频生成器结合高斯原语缓冲细化，实现高质量实时重建。

  <details><summary>Abstract</summary>

  We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation. GaussFusion mitigates common 3DGS artifacts, including floaters, flickering, and blur caused by camera pose errors, incomplete coverage, and noisy geometry initialization. Unlike prior RGB-based approaches limited to a single reconstruction pipeline, our method introduces a geometry-informed video-to-video generator that refines 3DGS renderings across both optimization-based and feed-forward methods. Given an existing reconstruction, we render a Gaussian primitive video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, artifact-free frames. We further introduce an artifact synthesis pipeline that simulates diverse degradation patterns, ensuring robustness and generalization. GaussFusion achieves state-of-the-art performance on novel-view synthesis benchmarks, and an efficient variant runs in real time at 15 FPS while maintaining similar performance, enabling interactive 3D applications.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (18) · <a href="topics/editing.md">full list →</a></summary>

- **[Boosting Zero-Shot 3D Style Transfer with 2D Pre-trained Priors](https://arxiv.org/abs/2605.30065)**  
  *Xin Dong, Yunzhi Teng, Wenfeng Deng, Yansong Tang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30065) · [pdf](https://arxiv.org/pdf/2605.30065.pdf)
  > 💡 融合2D预训练解码器与特征高斯泼溅，解决数据稀缺问题，实现高质量零样本3D风格迁移。

  <details><summary>Abstract</summary>

  In this work, we focus on zero-shot 3D style transfer that can generate multi-view consistent stylized views of the 3D scene given an arbitrary style image. We primarily tackle the issue of data scarcity in 3D style transfer, which arises when each model is trained on only a single scene, thereby limiting the number of available content images. This scarcity significantly hampers stylization performance, as model optimization relies on a sufficient number of content-style image pairs to provide supervisory signals. Our core idea is to integrate a decoder pre-trained on large-scale 2D image datasets into the 3D style transfer pipeline, thereby leveraging the prior knowledge encoded in the decoder from learning over numerous content-style image pairs. Our method combines feature Gaussian splatting and deferred stylization, enabling high-quality stylization with the data-sufficient decoder network while ensuring view consistency by unifying view-dependent operations into a view-invariant process. Experiments demonstrate that our Data-Sufficient StyleGaussian (DS-StyleGaussian) model outperforms existing zero-shot 3D style transfer methods in terms of visual quality across various datasets. This work also suggests that 2D pre-training can serve as a strong enhancement for 3D tasks, bridging the data gap between 2D and 3D.

  </details>


- **[BitC-3DGS: High-Capacity 3D Gaussian Splatting Watermarking via Bit Compression](https://arxiv.org/abs/2605.29583)**  
  *Yuquan Bi, Baosheng Yu, Yingke Lei, Jianwei Yang, Hongsong Wang, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29583) · [pdf](https://arxiv.org/pdf/2605.29583.pdf)
  > 💡 现有3DGS水印受限于77位容量，提出BitC-3DGS位压缩方案，通过双分支架构与硬消息采样实现128位高容量水印。

  <details><summary>Abstract</summary>

  High-capacity watermarking is necessary for 3D Gaussian Splatting (3DGS) assets to embed rich information (e.g., ownership, provenance, and authentication codes), enabling reliable identification and integrity verification in large-scale 3D asset pipelines. Existing bit-to-token watermarking methods based on a pre-trained text encoder are limited to 77-bit messages due to CLIP's fixed 77-token context length, as tokens beyond this limit are unsupported by learned positional embeddings. To address this limitation, we introduce BitC-3DGS, a bit-compression framework that encodes multiple message bits per token. It employs a bit-compressed tokenization scheme that encodes multiple bits within the same chunk into a single semantic token. To enable recovery of the compressed information, it further introduces a dual-branch architecture for joint chunk decompression and bit decoding, along with a hard-message sampling strategy to improve combinatorial coverage during decoder training. Extensive experiments on the Blender and LLFF datasets demonstrate the effectiveness of BitC-3DGS for high-capacity watermarking, achieving high message recovery accuracy and rendering fidelity. For example, it supports 128-bit message capacity with recovery accuracy comparable to that of 64-bit messages in recent state-of-the-art methods.

  </details>


- **[Learning Structural Latent Points for Efficient Visual Representations in Robotic Manipulation](https://arxiv.org/abs/2605.21258)**  
  *Yicheng Jiang, Jiaxu Wang, Junhao He, Zesen Gan, Junhao Li, Qiang Zhang, Jingkai Sun, Jiahang Cao, Mingyuan Sun, Xiangyu Yue, Qiming Shao*  
  `2026-05-20` · `cs.RO` · [abs](https://arxiv.org/abs/2605.21258) · [pdf](https://arxiv.org/pdf/2605.21258.pdf)
  > 💡 针对隐式和显式表示的缺陷，提出结构潜点混合表示，通过潜变量变分自编码器正则化，在机器人操作任务上取得一致性能提升。

  <details><summary>Abstract</summary>

  Current 3D-aware pretraining methods for embodied perception and manipulation are largely built on differentiable rendering frameworks, producing either fully implicit neural fields or fully explicit geometric primitives. Implicit representations, while expressive, lack explicit structural cues, whereas explicit ones preserve geometry but suffer from resolution limits and weak generalization. To address these limitations, we propose a novel pretraining framework that learns a hybrid representation-structural latent points. Specifically, we insert a point-wise latent variational autoencoder into the latent space of a point-cloud autoencoder, jointly regularizing point-wise features and coordinates toward a Gaussian prior. The resulting compact latent preserves coarse structural tendencies, which do not encode precise geometry but capture richer rough shape and semantic information, effectively combining the expressiveness of implicit representations with the structural priors of explicit ones. In addition, informed by shared design choices in prior work, we develop a streamlined, efficient 3DGS-based rendering pipeline that is deliberately kept lightweight, improving efficiency while leaving greater representational capacity to the front-end latent module. Extensive evaluations on RLBench, ManiSkill2, and a real-robot platform demonstrate consistent gains in task success, sample efficiency, and robustness to viewpoint and scene variations over strong baselines. Ablation studies further confirm that each component of our framework is critical to overall performance.

  </details>


- **[GLUT: 3D Gaussian Lookup Table for Continuous Color Transformation](https://arxiv.org/abs/2605.19889)**  
  *Danna Xue, David Serrano-Lozano, Shaolin Su, Javier Vazquez-Corral*  
  `2026-05-19` · `cs.GR` · [abs](https://arxiv.org/abs/2605.19889) · [pdf](https://arxiv.org/pdf/2605.19889.pdf)
  > 💡 针对3D LUT离散化导致容量-内存权衡和不可解释性，提出基于可学习3D高斯原语的连续显式颜色变换

  <details><summary>Abstract</summary>

  3D Lookup Tables (3D LUTs) are widely used for color mapping, but their grid-based representation requires discretizing the RGB space, leading to a capacity-memory trade-off that becomes prohibitive when storing large numbers of LUTs. Recent approaches adopt implicit neural representations to improve scalability, yet their black-box nature limits interpretability and hinders intuitive, localized editing. In this paper, we propose Gaussian LUT (GLUT), a continuous and explicit color representation that models color transformations using a set of learnable 3D Gaussian primitives. By avoiding fixed-resolution grids, GLUT achieves flexible representational capacity while maintaining a compact memory footprint. Its explicit, spatially localized formulation further enables both accurate modeling and interpretability. Building on this representation, we introduce a compact conditional generator (CGLUT) that predicts GLUT parameters for multiple LUT instances, encoding diverse color styles in a single framework to enable smooth and controllable LUT style blending. Moreover, GLUT supports efficient, user-friendly editing by allowing localized adjustments to specific color regions without global retraining. Experimental results demonstrate that our approach outperforms prior neural LUT representations in both accuracy and efficiency, while offering improved interpretability and interactive control.

  </details>


- **[RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting](https://arxiv.org/abs/2605.18263)**  
  *Ji Shi, Xianghua Ying, Bowei Xing, Ruohao Guo, Wenzhen Yue*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18263) · [pdf](https://arxiv.org/pdf/2605.18263.pdf)
  > 💡 针对半透明镜面场景，将高斯几何占据与光学透明度解耦，通过混合渲染和梯度门控实现高保真反射与清晰透射的实时渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables real-time novel view synthesis with high visual quality. However, existing methods struggle with semi-transparent specular surfaces that exhibit both complex reflections and clear transmission, often producing blurry reflections or overly occluded transmission. To address this, we present RT-Splatting, a framework that disentangles each Gaussian's geometric occupancy from its optical opacity. This factorization yields a unified surface-volume scene representation with a single set of Gaussian primitives. Our hybrid renderer interprets this representation both as a surface to capture high-frequency reflections and as a volume to preserve clear transmission. To mitigate the ambiguity in jointly optimizing reflection and transmission, we introduce Specular-Aware Gradient Gating, which suppresses misleading gradients from highly specular regions into the transmission branch, effectively reducing distracting floaters. Experiments on challenging semi-transparent scenes show that RT-Splatting achieves state-of-the-art performance, delivering high-fidelity reflections and clear transmission with real-time rendering. Moreover, our factorization naturally enables flexible scene editing. The project page is available at https://sjj118.github.io/RT-Splatting.

  </details>


- **[Robust Prior-Guided Segmentation for Editable 3D Gaussian Splatting](https://arxiv.org/abs/2605.16065)**  
  *Raushan Joshi, Jean-Yves Guillemaut*  
  `2026-05-15` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16065) · [pdf](https://arxiv.org/pdf/2605.16065.pdf)
  > 💡 提出先验引导分割，利用SAM-HQ生成精确掩码并多视图一致分配标签，实现高精度可编辑3DGS。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3D-GS) enables real-time 3D scene reconstruction but lacks robust segmentation for editing tasks such as object removal, extraction, and recoloring. Existing approaches that lift 2D segmentations to the 3D domain suffer from view inconsistencies and coarse masks. In this paper, we propose a novel framework that leverages the Segment Anything Model High Quality (SAM-HQ) to generate accurate 2D masks, addressing the limitations of the standard SAM in boundary fidelity and fine-structure preservation. To achieve robust 3D segmentation of any target object in a given scene, we introduce a prior-guided label reassignment method that assigns labels to 3D Gaussians by enforcing multiview consistency with learned priors. Our approach achieves state-of-the-art segmentation accuracy and enables interactive, real-time object editing while maintaining high visual fidelity. Qualitative results demonstrate superior boundary preservation and practical utility in Virtual Reality (VR) and robotics, advancing 3D scene editing.

  </details>


- **[GuardMarkGS: Unified Ownership Tracing and Edit Deterrence for 3D Gaussian Splatting](https://arxiv.org/abs/2605.12919)**  
  *Utae Jeong, Jaewan Choi, Junseok Lee, Jongheon Jeong, Sang Ho Yoon, ByoungSoo Koh, Sangpil Kim*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12919) · [pdf](https://arxiv.org/pdf/2605.12919.pdf)
  > 💡 首个针对3DGS的统一保护框架，联合场景水印与对抗编辑阻止，平衡了所有权追踪、编辑阻止和渲染质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is becoming a practical representation for novel view synthesis, but its growing adoption, together with rapid advances in instruction-driven 3DGS editing, also exposes a dual copyright risk: once a 3DGS-based asset is released, it can be used without permission and manipulated through 3D editing. Existing protection methods address only one side of this problem. Watermarking can trace ownership after unauthorized use, but it cannot prevent malicious editing. Adversarial edit-deterrence methods can disrupt editing, but they do not provide evidence of ownership. To the best of our knowledge, we present the first unified protection framework for 3DGS that jointly optimizes ownership tracing and unauthorized editing deterrence. Our framework combines a scene-wide watermarking objective over all Gaussians with an adversarial objective for edit deterrence. The adversarial branch combines latent-anchor separation, denoising-trajectory diversion, and cross-attention diversion to divert the editing trajectory, while an update-saliency-motivated Gaussian selection strategy assigns stronger adversarial updates to mask-selected Gaussians, improving the balance among watermark recovery, edit deterrence, and rendering fidelity. Experiments on scenes from Mip-NeRF 360 and Instruct-NeRF2NeRF demonstrate that the proposed framework achieves a favorable balance among bit accuracy, edit deterrence, and rendering quality. These results suggest that practical copyright protection of 3DGS-based assets can be more effectively addressed by integrating ownership tracing and unauthorized editing deterrence into a single optimization framework.

  </details>


- **[BEA-GS: BEyond RAdiance Supervision in 3DGS for Precise Object Extraction](https://arxiv.org/abs/2605.09662)**  
  *Alessio Mazzucchelli, Maria Naranjo-Almeida, Jorge Bustos-Sanchez, Mariella Dimiccoli, Francesc Moreno-Noguer, Jordi Sanchez-Riera, Adrian Penate-Sanchez*  
  `2026-05-10` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09662) · [pdf](https://arxiv.org/pdf/2605.09662.pdf)
  > 💡 针对3DGS对象提取边界不精确问题，提出几何优化与不可见高斯调整损失，实现最佳边界分割。

  <details><summary>Abstract</summary>

  Most Gaussian Splatting techniques that provide a 3D semantic representation of the scene do not optimize the underlying 3D geometry, making object-level editing or asset extraction challenging. Recent methods, such as COBGS, Trace3D, ObjectGS, acknowledge this limitation and propose approaches that modify the scene's geometry to represent the underlying semantics. We advance this concept further by proposing a novel solution that provides near perfect boundaries in object extraction. We do so by introducing two new losses in the optimization that take care of: 1) a loss that modifies the geometry of visible Gaussians to respect semantic boundaries, and 2) a loss that adjusts the geometry of non-visible Gaussians that appear once the object is extracted. Our first loss propagates gradients directly through the rasterization, allowing for seamless integration within the optimization of the Gaussian parameters. The second loss also propagates gradients to Gaussian parameters but does so without passing through the rasterization, enabling modification of the scene's geometry even when little transmittance reaches a Gaussian (partial or non-visible). Exhaustive comparisons with 12 state of the art methods across 4 datasets, using six metrics, demonstrate that our approach produces overall the best boundary segmentation to date.

  </details>


- **[Relightable Gaussian Splatting for Virtual Production Using Image-Based Illumination](https://arxiv.org/abs/2605.09024)**  
  *Adrian Azzarelli, Nantheera Anantrasirichai, James Pollock, David R. Bull*  
  `2026-05-09` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09024) · [pdf](https://arxiv.org/pdf/2605.09024.pdf)
  > 💡 针对虚拟制作中LED墙照明耦合问题，提出高斯溅射重照明框架，利用背景图像条件化与图元参数化实现高质量高效重渲染。

  <details><summary>Abstract</summary>

  Virtual production (VP) use LED walls to provide both background imagery and image-based lighting. While this enables on-set compositing, it couples lighting to background and scene appearance, limiting flexibility for downstream editing. In addition, inverse rendering conventionally relies on physically-based rendering to estimates 3D geometry and lighting, using environment maps. However, these maps are typically low-resolution and assume far-field lighting. In VP, with near-field and high-resolution image-based lighting, this can lead to inaccuracies and introduce complexities when editing. Addressing this, we propose a VP-specific framework for 3D reconstruction and relighting using Gaussian Splatting. This uses the known background imagery to condition the relighting process. This avoids relying on environment maps and reduces compositing to a background-image editing task. To realize our framework, we introduce a process (and associated dataset) that captures real VP scenes under varying background content and illumination conditions. This data is used to decompose a 3D scene into fixed appearance and variable lighting components. The variable lighting process simulates light transport by parameterizing each primitive with a UV coordinate, intensity value and resolution modifier. Using mipmaps, these directly sample the background texture in image space - implicitly capturing reflections and refractions without physically-based rendering. Combined with the fixed appearance component, this allows us to render relit scenes using a Gaussian Splatting rasterizer. Compared to baselines, our approach achieves higher-quality 3D reconstruction and controllable relighting. The method is efficient (<3 GB RAM, <5 GB VRAM, <2 hours training, ~35 FPS) and supports rendering useful arbitrary output variables including depth, lighting intensity, lighting color, and unlit renders.

  </details>


- **[GOR-IS: 3D Gaussian Object Removal in the Intrinsic Space](https://arxiv.org/abs/2605.00498)**  
  *Yonghao Zhao, Yupeng Gao, Jian Yang, Jin Xie, Beibei Wang*  
  `2026-05-01` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00498) · [pdf](https://arxiv.org/pdf/2605.00498.pdf)
  > 💡 通过内在空间分解与光传输建模，解决3DGS物体移除中光照不一致和非朗伯表面问题，实现物理与视觉连贯修复。

  <details><summary>Abstract</summary>

  Recent advances in Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have made it standard practice to reconstruct 3D scenes from multi-view images. Removing objects from such 3D representations is a fundamental editing task that requires complete and seamless inpainting of occluded regions, ensuring consistency in geometry and appearance. Although existing methods have made notable progress in improving inpainting consistency, they often neglect global lighting effects, leading to physically implausible results. Moreover, these methods struggle with view-dependent non-Lambertian surfaces, where appearance varies across viewpoints, leading to unreliable inpainting. In this paper, we present 3D Gaussian Object Removal in the Intrinsic Space (GOR-IS), a novel framework for physically consistent and visually coherent 3D object removal. Our approach decomposes the scene into intrinsic components and explicitly models light transport to maintain global lighting effects consistency. Furthermore, we introduce an intrinsic-space inpainting module that operates directly in the material and lighting domains, effectively addressing the challenges posed by non-Lambertian surfaces. Extensive experiments on both synthetic and real-world datasets demonstrate that our framework substantially improves the physical consistency and visual coherence of object removal, outperforming existing methods by 13% in perceptual similarity (LPIPS) and 2dB in peak signal-to-noise ratio (PSNR). Code is publicly available at https://applezyh.github.io/GOR-IS-project-page/

  </details>


- **[Point Group Symmetry of Polyhedral Diagrams in Graphic Statics](https://arxiv.org/abs/2604.25695)**  
  *Yefan Zhi, Yao Lu, Masoud Akbarzadeh*  
  `2026-04-28` · `cs.CG` · [abs](https://arxiv.org/abs/2604.25695) · [pdf](https://arxiv.org/pdf/2604.25695.pdf)
  > 💡 针对图形静力学中多面体图对称性易破坏问题，引入点群并约束等边长度，实现对称保持与优化。

  <details><summary>Abstract</summary>

  Symmetry is an implicit objective in structural form-finding that often reconciles efficiency and aesthetics. This paper identifies the symmetry of polyhedral diagrams in three-dimensional graphic statics (3DGS) as point groups and formulates them as constraints, enabling the optimization and manipulation of polyhedral diagrams that preserve such symmetry. 3DGS has been an efficient and effective tool for the form-finding of funicular structures. However, when modifying complex diagrams for design exploration or optimization, one can easily break the symmetry of the reciprocal design input, rendering the result undesirable for practical use. To address this problem, this paper investigates symmetry transformations and introduces point groups, an abstract algebra tool commonly used in crystallography to represent the symmetry and equivalence between a network of atoms (points with labels). It then discusses the hierarchy of symmetry in the geometry types of a polyhedral diagram, and proposes the constraint of symmetry through edge lengths. Based on the crystal symmetry search algorithm by spglib and pymatgen, a fast fingerprinting algorithm is developed to identify the point group of a polyhedral diagram and sort equivalent edges into sets. Finally, the paper shows that the necessary and sufficient condition for preserving the point group symmetry is that each set of edges has the same length. This constraint is compatible with the algebraic formulation of 3DGS and effectively preserves symmetry while reducing the dimension of the solution space. The method is implemented in the PolyFrame 2 plug-in for Rhino and Grasshopper.

  </details>


- **[TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing](https://arxiv.org/abs/2604.19571)**  
  *Yanhui Chen, Jiahong Li, Jingchao Wang, Junyi Lin, Zixin Zeng, Yang Shi*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.19571) · [pdf](https://arxiv.org/pdf/2604.19571.pdf)
  > 💡 针对语言驱动3DGS编辑中2D与3D语义对应缺失，提出多视图不平衡语义传输方法显式建模对应关系并抑制编辑泄露，提升局部编辑精度和结构一致性。

  <details><summary>Abstract</summary>

  Language-driven 3D Gaussian Splatting (3DGS) editing provides a more convenient approach for modifying complex scenes in VR/AR. Standard pipelines typically adopt a two-stage strategy: first editing multiple 2D views, and then optimizing the 3D representation to match these edited observations. Existing methods mainly improve view consistency through multi-view feature fusion, attention filtering, or iterative recalibration. However, they fail to explicitly address a more fundamental issue: the semantic correspondence between edited 2D evidence and 3D Gaussians. To tackle this problem, we propose TransSplat, which formulates language-driven 3DGS editing as a multi-view unbalanced semantic transport problem. Specifically, our method establishes correspondences between visible Gaussians and view-specific editing prototypes, thereby explicitly characterizing the semantic relationship between edited 2D evidence and 3D Gaussians. It further recovers a cross-view shared canonical 3D edit field to guide unified 3D appearance updates. In addition, we use transport residuals to suppress erroneous edits in non-target regions, mitigating edit leakage and improving local control precision. Qualitative and quantitative results show that, compared with existing 3D editing methods centered on enhancing view consistency, TransSplat achieves superior performance in local editing accuracy and structural consistency.

  </details>


- **[Instant Colorization of Gaussian Splats](https://arxiv.org/abs/2604.17155)**  
  *Daniel Lieber, Alexander Mock, Nils Wandel*  
  `2026-04-18` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17155) · [pdf](https://arxiv.org/pdf/2604.17155.pdf)
  > 💡 针对将2D信息高效映射回3D高斯场景的任务，用法方程求解加权最小二乘，实现快速重光照、特征增强和语义分割。

  <details><summary>Abstract</summary>

  Gaussian Splatting has recently become one of the most popular frameworks for photorealistic 3D scene reconstruction and rendering. While current rasterizers allow for efficient mappings of 3D Gaussian splats onto 2D camera views, this work focuses on mapping 2D image information (e.g. color, neural features or segmentation masks) efficiently back onto an existing scene of Gaussian splats. This 'opposite' direction enables applications ranging from scene relighting and stylization to 3D semantic segmentation, but also introduces challenges, such as view-dependent colorization and occlusion handling. Our approach tackles these challenges using the normal equation to solve a visibility-weighted least squares problem for every Gaussian and can be implemented efficiently with existing differentiable rasterizers. We demonstrate the effectiveness of our approach on scene relighting, feature enrichment and 3D semantic segmentation tasks, achieving up to an order of magnitude speedup compared to gradient descent-based baselines.

  </details>


- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941)**  
  *Haato Watanabe, Nobuyuki Umetani*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15941) · [pdf](https://arxiv.org/pdf/2604.15941.pdf)
  > 💡 使用轻量MLP增强高斯基元建模颜色变化，配合频率感知稠密化策略，实现高频表面的高效精确重建。

  <details><summary>Abstract</summary>

  Recent years have witnessed the rapid emergence of 3D Gaussian splatting (3DGS) as a powerful approach for 3D reconstruction and novel view synthesis. Its explicit representation with Gaussian primitives enables fast training, real-time rendering, and convenient post-processing such as editing and surface reconstruction. However, 3DGS suffers from a critical drawback: the number of primitives grows drastically for scenes with high-frequency appearance details, since each primitive can represent only a single color, requiring multiple primitives for every sharp color transition. To overcome this limitation, we propose neural Gabor splatting, which augments each Gaussian primitive with a lightweight multi-layer perceptron that models a wide range of color variations within a single primitive. To further control primitive numbers, we introduce a frequency-aware densification strategy that selects mismatch primitives for pruning and cloning based on frequency energy. Our method achieves accurate reconstruction of challenging high-frequency surfaces. We demonstrate its effectiveness through extensive experiments on both standard benchmarks, such as Mip-NeRF360 and High-Frequency datasets (e.g., checkered patterns), supported by comprehensive ablation studies.

  </details>


- **[SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2604.13333)**  
  *Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13333) · [pdf](https://arxiv.org/pdf/2604.13333.pdf)
  > 💡 针对现有3DGS重光照中阴影与散射建模不足，提出四项物理分解模型，实现

  <details><summary>Abstract</summary>

  We present SSD-GS, a physically-based relighting framework built upon 3D Gaussian Splatting (3DGS) that achieves high-quality reconstruction and photorealistic relighting under novel lighting conditions. In physically-based relighting, accurately modeling light-material interactions is essential for faithful appearance reproduction. However, existing 3DGS-based relighting methods adopt coarse shading decompositions, either modeling only diffuse and specular reflections or relying on neural networks to approximate shadows and scattering. This leads to limited fidelity and poor physical interpretability, particularly for anisotropic metals and translucent materials. To address these limitations, SSD-GS decomposes reflectance into four components: diffuse, specular, shadow, and subsurface scattering. We introduce a learnable dipole-based scattering module for subsurface transport, an occlusion-aware shadow formulation that integrates visibility estimates with a refinement network, and an enhanced specular component with an anisotropic Fresnel-based model. Through progressive integration of all components during training, SSD-GS effectively disentangles lighting and material properties, even for unseen illumination conditions, as demonstrated on the challenging OLAT dataset. Experiments demonstrate superior quantitative and perceptual relighting quality compared to prior methods and pave the way for downstream tasks, including controllable light source editing and interactive scene relighting. The source code is available at: https://github.com/irisfreesiri/SSD-GS.

  </details>


- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410)**  
  *Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Jiacheng Lin, Kailun Yang, Zhiyong Li, Yaonan Wang*  
  `2026-04-09` · `cs.CV` · [abs](https://arxiv.org/abs/2604.08410) · [pdf](https://arxiv.org/pdf/2604.08410.pdf)
  > 💡 利用3DGS场景表示，通过语言解析和三角几何约束定位功能点，实现零样本可解释的灵巧

  <details><summary>Abstract</summary>

  In unstructured environments, functional dexterous grasping calls for the tight integration of semantic understanding, precise 3D functional localization, and physically interpretable execution. Modular hierarchical methods are more controllable and interpretable than end-to-end VLA approaches, but existing ones still rely on predefined affordance labels and lack the tight semantic--pose coupling needed for functional dexterous manipulation. To address this, we propose BLaDA (Bridging Language to Dexterous Actions in 3DGS fields), an interpretable zero-shot framework that grounds open-vocabulary instructions as perceptual and control constraints for functional dexterous manipulation. BLaDA establishes an interpretable reasoning chain by first parsing natural language into a structured sextuple of manipulation constraints via a Knowledge-guided Language Parsing (KLP) module. To achieve pose-consistent spatial reasoning, we introduce the Triangular Functional Point Localization (TriLocation) module, which utilizes 3D Gaussian Splatting as a continuous scene representation and identifies functional regions under triangular geometric constraints. Finally, the 3D Keypoint Grasp Matrix Transformation Execution (KGT3D+) module decodes these semantic-geometric constraints into physically plausible wrist poses and finger-level commands. Extensive experiments on complex benchmarks demonstrate that BLaDA significantly outperforms existing methods in both affordance grounding precision and the success rate of functional manipulation across diverse categories and tasks. Code will be publicly available at https://github.com/PopeyePxx/BLaDA.

  </details>


- **[ColorGradedGaussians: Palette-Based Color Grading for 3D Gaussian Splatting via View-Space Sparse Decomposition](https://arxiv.org/abs/2604.01551)**  
  *Cheng-Kang Ted Chao, Yotam Gingold*  
  `2026-04-02` · `cs.GR` · [abs](https://arxiv.org/abs/2604.01551) · [pdf](https://arxiv.org/pdf/2604.01551.pdf)
  > 💡 通过视空间稀疏分解和逆重心坐标几何损失，实现实时调色板编辑，提升3DGS场景色彩编辑质量。

  <details><summary>Abstract</summary>

  Professional color editing requires precise control over both color (hue and saturation) and lightness, ideally through separate, independent controls. We present a real-time interactive color editing framework for 3D Gaussian Splatting (3DGS) that enables palette-based recoloring, per-palette tone curves for color-aware lightness adjustment, and accurate pixel-level constraints -- capabilities unavailable in prior palette-based 3DGS methods. Existing approaches decompose colors at the primitive level, optimizing per-Gaussian palette weights before splatting. However, sparse primitive-level weights do not guarantee sparse pixel-level decompositions after alpha-blending, causing palette edits to affect unintended regions and degrading editing quality. We address this through view-space palette decomposition, splatting weights instead of colors to optimize the observable appearance of the scene. We introduce a geometric loss using inverse barycentric coordinates to enforce consistent sparsity patterns, ensuring similar colors share similar decompositions. Our approach achieves superior editing quality compared to primitive-space methods, enabling professional color grading workflows for 3DGS scenes with real-time interaction.

  </details>


- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686)**  
  *Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma*  
  `2026-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2603.23686) · [pdf](https://arxiv.org/pdf/2603.23686.pdf)
  > 💡 首次系统研究前馈式3DGS的对抗攻击，提出白盒与基于频域参数化的黑盒方法，揭示模型脆弱性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is increasingly recognized as a powerful paradigm for real-time, high-fidelity 3D reconstruction. However, its per-scene optimization pipeline limits scalability and generalization, and prevents efficient inference. Recently emerged feed-forward 3DGS models address these limitations by enabling fast reconstruction from a few input views after large-scale pretraining, without scene-specific optimization. Despite their advantages and strong potential for commercial deployment, the use of neural networks as the backbone also amplifies the risk of adversarial manipulation. In this paper, we introduce AdvSplat, the first systematic study of adversarial attacks on feed-forward 3DGS. We first employ white-box attacks to reveal fundamental vulnerabilities of this model family. We then develop two improved, practically relevant, query-efficient black-box algorithms that optimize pixel-space perturbations via a frequency-domain parameterization: one based on gradient estimation and the other gradient-free, without requiring any access to model internals. Extensive experiments across multiple datasets demonstrate that AdvSplat can significantly disrupt reconstruction results by injecting imperceptible perturbations into the input images. Our findings surface an overlooked yet urgent problem in this domain, and we hope to draw the community's attention to this emerging security and robustness challenge.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (30) · <a href="topics/compression.md">full list →</a></summary>

- **[RxGS: Receiver-Generalizable 3D Gaussian Splatting for Radio-Frequency Data Synthesis](https://arxiv.org/abs/2605.24290)**  
  *Kang Yang, Mani Srivastava*  
  `2026-05-22` · `cs.NI` · [abs](https://arxiv.org/abs/2605.24290) · [pdf](https://arxiv.org/pdf/2605.24290.pdf)
  > 💡 针对固定接收器的RF合成问题，提出两阶段3DGS框架，共享几何并条件化学习辐射，首次实现单模型泛化至任意接收器。

  <details><summary>Abstract</summary>

  Radio-frequency (RF) data synthesis predicts the received signal given transmitter and receiver positions, and is essential for wireless applications. Recent 3D Gaussian Splatting (3DGS)-based methods achieve efficient synthesis at any transmitter but only for a fixed receiver. Therefore, supporting $N$ receivers in one scene requires $N$ independent models and precludes prediction at unseen receivers. We present RxGS, which achieves receiver-generalizable synthesis within a single unified model. Our key insight is that scene geometry is receiver-independent while directional radiance is not: a first stage learns shared 3D Gaussian geometry, and a second stage freezes it and learns directional radiance conditioned on receiver position. A global conditioning branch captures shared receiver-dependent effects across the scene, while a local branch models per-scatterer variations from the receiver's geometry and occlusion. A multi-receiver CUDA rasterizer further batches rendering across all $N$ receivers. Evaluated across various RF datasets, RxGS matches or improves over per-receiver baselines with a single shared model and generalizes to receivers unseen during training within the scene, cutting training cost by up to $45\times$, inference cost by $7.6\times$, and storage by $N\times$.

  </details>


- **[AIR: Amortized Image Reconstruction Framework for Self-Supervised Feed-Forward 2D Gaussian Splatting](https://arxiv.org/abs/2605.20820)**  
  *Zhaojie Zeng, Yuesong Wang, Yawei Luo, Tao Guan*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20820) · [pdf](https://arxiv.org/pdf/2605.20820.pdf)
  > 💡 提出自监督前馈AIR框架，用阶段式残差网络和预测-优化-蒸馏策略实现2D高斯泼溅，消除逐图像优化，编码仅需160-300ms。

  <details><summary>Abstract</summary>

  2D Gaussian splatting provides an efficient explicit representation for image reconstruction, but existing methods still require costly per-image iterative optimization or rely on handcrafted priors for primitive allocation. We present AIR, a self-supervised feed-forward framework that amortizes iterative Gaussian fitting into a single network pass, eliminating per-image test-time optimization. AIR adopts a stage-wise residual architecture that progressively predicts additional Gaussian primitives from reconstruction residuals, together with an explicit Stage Control mechanism that activates new primitives only in under-reconstructed regions. A Predict--Optimize--Distill training strategy stabilizes multi-stage prediction by distilling short-horizon optimized Gaussian increments back into the predictor. The stabilized predictor is then jointly finetuned across stages and equipped with an image-adaptive quantizer for compact Gaussian storage. Experiments on Kodak and DIV2K show that AIR achieves better reconstruction quality than representative Gaussian-based baselines while reducing encoding time to 160--300\,ms. Code: https://github.com/whoiszzj/AIR.git

  </details>


- **[OP2GS: Object-Aware 3D Gaussian Splatting with Dual-Opacity Primitives](https://arxiv.org/abs/2605.20044)**  
  *Guiyu Liu, Niklas Vaara, Janne Mustaniemi, Juho Kannala, Janne Heikkilä*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20044) · [pdf](https://arxiv.org/pdf/2605.20044.pdf)
  > 💡 通过双不透明度原语分离视觉重建与实例占用，解决3DGS中标签污染问题，实现高效对象感知表示。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) provides an explicit and efficient scene representation, but its primitives lack inherent object-level identity, hindering downstream tasks such as open-vocabulary scene understanding. Existing methods typically address this by either distilling high-dimensional feature embeddings into Gaussians or by lifting 2D mask labels into 3D via heuristic refinement. However, feature-based approaches incur heavy storage and decoding overhead, while lifting-based pipelines remain vulnerable to label contamination: Gaussians necessary for appearance reconstruction often receive incorrect object labels during 2D-to-3D projection. We propose OP2GS, an object-aware Gaussian representation that augments each primitive with an explicit instance identity and a dedicated instance opacity $σ^{*}$ for object-mask rendering. The original opacity $σ$ remains responsible for visual reconstruction, while $σ^{*}$ models whether a Gaussian should contribute to a particular object mask. This dual-opacity formulation decouples visual existence from instance occupancy: mislabeled Gaussians can remain available for image rendering while becoming transparent in the object-mask branch. To learn this representation, we introduce a random object loss that optimizes the 1D instance occupancy field using the standard transmittance-based visibility of 3DGS. Semantic descriptors are then attached at the object level through multi-view aggregation, eliminating per-Gaussian feature storage. Compared with feature-training approaches, OP2GS achieves competitive open-vocabulary performance while significantly reducing computational overhead. Compared with training-free pipelines, it leverages physically consistent occupancy learning to resolve visibility ambiguities.

  </details>


- **[MMGS: 10$\times$ Compressed 3DGS through Optimal Transport Aggregation based on Multi-view Ranking](https://arxiv.org/abs/2605.19304)**  
  *Beizhen Zhao, Sicheng Yu, Ziran Yin, Dongxu Shen, Hao Wang*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.19304) · [pdf](https://arxiv.org/pdf/2605.19304.pdf)
  > 💡 针对3DGS冗余基元问题，提出多视角排序和全局最优传输聚合，实现10倍压缩与加速，保持高保真渲染。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction, it suffers from significant overhead due to massive redundant primitives. Existing compression methods typically rely on local sampling or fixed pruning thresholds, which often struggle to balance redundancy reduction with high-fidelity rendering. To address this, we propose a novel framework that formulates Gaussian optimization as a global geometric distribution matching problem. Specifically, our approach integrates three components: (1) we introduce a multi-view 3D Gaussian contribution ranking mechanism that filters primitives using geometric consistency instead of local heuristics; (2) we propose a global Optimal Transport (OT)-based aggregation algorithm that merges redundant primitives while preserving the underlying geometry; and (3) we design an OT-based densification operator that maintains the Gaussian's distributional properties for stable optimization. Our approach achieves state-of-the-art rendering quality with only \textbf{10$\%$} primitives and \textbf{10$\times$} accelerated training speeds compared to vanilla 3DGS.

  </details>


- **[Efficient Sparse-to-Dense Visual Localization via Compact Gaussian Scene Representation and Accelerated Dense Pose Estimation](https://arxiv.org/abs/2605.17777)**  
  *Zizhuo Li, Songchu Deng, Linfeng Tang, Jiayi Ma*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.17777) · [pdf](https://arxiv.org/pdf/2605.17777.pdf)
  > 💡 提出无颜色解耦特征场和密集匹配浓缩策略，消除94%冗余存储并加速19倍，实现高效内存与计算的稀疏到密集视觉定位。

  <details><summary>Abstract</summary>

  This letter presents LiteLoc, a novel and efficient localizer built on 3D Gaussian Splatting (3DGS). The previous state-of-the-art (SoTA) sparse-to-dense localizer, STDLoc, has shown remarkable localization capability but suffers from severe storage redundancy and computational latency. By revisiting its design decisions, we derive two simple yet highly effective improvements that cumulatively make LiteLoc much more efficient in both memory and computation, while also being easier to train. One key observation is that the color field, inherited directly from Feature 3DGS, is functionally useless for localization. Yet, its reconstruction of high-frequency photometric details necessitates excessive Gaussian primitives, resulting in a tightly coupled color-feature representation with significant memory overhead and sub-optimal feature field optimization. To resolve this, we propose a color-free decoupled feature field that constructs a compact Gaussian scene representation by retaining only task-essential feature attributes, thereby eliminating approximately 94% of redundant storage with no loss of localization-relevant information. We further find that the primary computational bottleneck lies in the dense Perspective-n-Point (PnP) solver, where most matches contribute saturated geometric constraints with diminishing accuracy gains. Accordingly, we propose a condensing strategy that distills dense matches into a subset of 5% representative matches, enabling a nearly 19-fold speedup in robust estimation with negligible performance drop. Extensive experiments show that LiteLoc surpasses STDLoc in multiple scenes with considerable efficiency benefits, opening up exciting prospects for latency-sensitive visual localization.

  </details>


- **[A Single Atlas is All You Need: Decoder-Side Gaussian Splatting for Immersive Video](https://arxiv.org/abs/2605.17002)**  
  *Dawid Mieloch, Stuart Perry*  
  `2026-05-16` · `cs.GR` · [abs](https://arxiv.org/abs/2605.17002) · [pdf](https://arxiv.org/pdf/2605.17002.pdf)
  > 💡 解码端3DGS替代深度估计，用压缩纹理和元数据推断场景，压缩提升质量，带宽降十倍，视图间抖动从17.2dB降至6.4dB。

  <details><summary>Abstract</summary>

  Immersive video delivery is bottlenecked by pixel-rate constraints, making the transmission of high-resolution depth maps or explicit 3D volumetric data expensive. Decoder-Side Depth Estimation (DSDE) shifts depth computation to the client, but struggles with complex geometries, inter-view flickering, and non-Lambertian reflections. Conversely, 3D Gaussian Splatting (3DGS) offers state-of-the-art view synthesis, but transmitting splats (or their projected 2D maps) incurs prohibitive bandwidth costs and is poorly aligned with standard video codecs. We propose Decoder-Side Gaussian Splatting (DSGS), a framework that natively replaces the depth-estimation stage of DSDE with feed-forward 3DGS inference, optimizing volumetric scenes entirely on the decoder side from compressed textures and metadata. A central, counterintuitive finding is that lossy compression acts as an implicit low-pass filter stabilizing feed-forward splat prediction: compressed bitstreams exceed lossless quality while shrinking tenfold. Under extreme view sparsity (one 2D atlas comprising 4 input views), DSGS achieves a +5.79 dB BD-PSNR and +0.054 BD-SSIM gain over the DSDE anchor while reducing maximum inter-view Delta IV-PSNR from 17.2 dB to 6.4 dB, minimizing the domain shift between transmitted and virtual viewports.

  </details>


- **[Smart target point control for Gaussian Splatting methods](https://arxiv.org/abs/2605.16158)**  
  *Pratik Singh Bisht, Andreas Kolb*  
  `2026-05-15` · `cs.GR` · [abs](https://arxiv.org/abs/2605.16158) · [pdf](https://arxiv.org/pdf/2605.16158.pdf)
  > 💡 针对GS方法启发式密集化导致不公平比较，提出目标点控制方案，调整超参数跟踪二次计数轨迹，实现公平评估。

  <details><summary>Abstract</summary>

  Standard Gaussian splatting methods rely on heuristic densification and pruning to adaptively allocate primitives during training, and the resulting Gaussian count strongly influences both reconstruction quality and runtime. This makes comparisons across methods fragile: improvements can stem from higher representational capacity rather than algorithmic design. A common and naive workaround for this is hard-stopping or budgeting densification/pruning once a target count is reached, which biases training because different methods hit the cap at different times, yielding non-uniform densify/prune exposure across views and uneven point distributions. We propose a target point control scheme that preserves the standard densification window and cadence, but adjusts only the existing densification and opacity-culling hyper-parameters to track a quadratic target count trajectory. This quota-governor reaches the desired count by 15k iterations without abrupt cutoffs, ensuring that all methods and views receive equal densification and pruning cycles, enabling fairer, capacity-matched evaluation.

  </details>


- **[Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors](https://arxiv.org/abs/2605.14629)**  
  *Julien Zouein, Vibhoothi Vibhoothi, François Pitié, Anil Kokaram*  
  `2026-05-14` · `eess.IV` · [abs](https://arxiv.org/abs/2605.14629) · [pdf](https://arxiv.org/pdf/2605.14629.pdf)
  > 💡 利用AV1运动向量实现高效密集匹配，生成8倍密集点云，提升3DGS重建质量和减少63%训练时间。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a prominent framework for real-time, photorealistic scene reconstruction, offering significant speed-ups over Neural Radiance Fields (NeRF). However, the fidelity of 3DGS representations remains heavily dependent on the quality of the initial point cloud. While standard Structure-from-Motion (SfM) pipelines using COLMAP provide adequate initialisation, they often suffer from high computational costs and sparsity in textureless regions, which degrades subsequent reconstruction accuracy and convergence speed. In this work, we introduce an AV1-based feature detection and matching pipeline that significantly reduces SfM processing overhead. By leveraging motion vectors inherent to the AV1 video codec, we bypass computationally expensive exhaustive matching while maintaining geometric robustness. Our pipeline produces substantially denser point clouds, with up to eight times as many points as classical SfM. We demonstrate that this enhanced initialisation directly improves 3DGS performance, yielding an 9-point increase in VMAF and a 63% average reduction in training time required to reach baseline quality. The project page: https://sigmedia.tv/AV1-3DGS.github.io/

  </details>


- **[Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600)**  
  *Lovre Antonio Budimir, Yushi Guan, Steve Ryhner, Sven Lončarić, Nandita Vijaykumar*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13600) · [pdf](https://arxiv.org/pdf/2605.13600.pdf)
  > 💡 针对3D语言高斯溅射高存储与渲染代价，提出稀疏码本提升解耦优化，实现400倍训练加速和3倍内存节省且精度持平。

  <details><summary>Abstract</summary>

  3D Language Gaussian Splatting (3DLGS) augments 3D Gaussian Splatting with language-aligned visual features for open-vocabulary 3D scene understanding. A core challenge is efficiently associating high-dimensional vision-language embeddings with millions of 3D Gaussians while preserving efficient feature rendering for text-based querying. Existing methods either store dense features directly on Gaussians, causing high storage costs and slow rendering, or learn compact representations through expensive per-scene optimization with repeated feature rasterization. No existing method simultaneously achieves fast 3D semantic reconstruction, efficient storage, and fast rendering. We propose SCOUP (Sparse COde UPlifting), which addresses all three by decoupling language representation learning from 3D Gaussian optimization. Rather than working directly in 3D, we learn sparse codebook-based representations entirely using features associated with 2D image regions, associating each region with a sparse set of codebook coefficients. We then uplift these coefficients to 3D Gaussians with our weighted sparse aggregation using Gaussian-to-pixel associations, where each Gaussian accumulates coefficients over codebook atoms across views. Top-$K$ filtering then extracts the most dominant multi-view coefficients per Gaussian, enabling efficient storage and fast rendering. Our method achieves up to $400\times$ training speedup while being $3\times$ more memory efficient during training compared to the state-of-the-art in rendering speed. Across multiple benchmarks, SCOUP matches or outperforms existing methods in open-vocabulary querying accuracy.

  </details>


- **[HarmoGS: Robust 3D Gaussian Splatting in the Wild via Conflict-Aware Gradient Harmonization](https://arxiv.org/abs/2605.13073)**  
  *Yulei Kang, Tianze Zhu, Jian-Fang Hu, Jianhuang Lai, Wei-Shi Zheng*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13073) · [pdf](https://arxiv.org/pdf/2605.13073.pdf)
  > 💡 针对野外场景中瞬态干扰和外观不一致问题，提出语义一致性掩码与冲突感知梯度协调，实现高质量渲染。

  <details><summary>Abstract</summary>

  In-the-wild 3D Gaussian Splatting remains challenging due to transient distractors and illumination-induced cross-view appearance inconsistencies. Existing methods mainly rely on image-level masking to suppress unreliable supervision, but masking alone cannot fully eliminate residual occlusions or resolve illumination-induced inconsistencies, both of which can introduce conflicting cross-view gradients. These unresolved conflicts may destabilize Gaussian optimization and lead to visible reconstruction artifacts. We propose a conflict-aware 3DGS framework that addresses this problem from both image-space supervision and gradient-level optimization. Semantic Consistency-Guided Masking learns pixel-wise consistency scores to adaptively refine prior masks and suppress unreliable supervision before gradient formation. A dual-view Conflict-Aware Gradient Harmonization strategy further reconciles view-specific gradients by mutually rotating them into an orthogonal configuration, reducing negative directional interference across views. We also introduce conflict-aware densification and pruning to stabilize Gaussian growth and remove persistently conflicting primitives. Extensive experiments on standard in-the-wild benchmarks demonstrate that our method achieves state-of-the-art rendering quality under complex transient distractors and cross-view inconsistencies.

  </details>


- **[Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization](https://arxiv.org/abs/2605.07351)**  
  *Miso Lee, Sangeek Hyun, Yerim Jeon, Jae-Pil Heo*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07351) · [pdf](https://arxiv.org/pdf/2605.07351.pdf)
  > 💡 原始GSFFs中2D-3D对应存在多对一歧义，SplitGS-Loc利用混合高斯分裂和组成权重实现精确一对一匹配，提升定位精度。

  <details><summary>Abstract</summary>

  While Gaussian Splatting-based Feature Fields (GSFFs) have shown promise for visual localization, this paper highlights that photometrically optimized GSFFs are inherently ill-suited for 2D-3D matching. The volumetric extent of each Gaussian induces many-to-one pixel-to-point mappings that destabilize PnP-based pose estimation, while photometric optimization gives rise to superfluous Gaussians devoid of multi-view consistency. To address these issues, we propose SplitGS-Loc, a localization-specialized GSFFs construction framework that disambiguates 2D-3D correspondences by exploiting Gaussian attributes. Our key design, Mixture-of-Gaussians-based splitting, decomposes each Gaussian into smaller Gaussians, replacing ambiguous many-to-one with precise one-to-one correspondences. In parallel, we exploit composition weights from GS rasterization to select Gaussians that significantly and consistently contribute across multiple views and aggregate discriminative features through strong pixel-Gaussian associations, enforcing multi-view consistency. The resulting compact yet discriminative feature fields enable stable PnP convergence, achieving state-of-the-art performance on localization benchmarks. Extensive experiments validate that SplitGS-Loc extends the utility of photometric GSFFs to accurate and efficient localization by exploiting Gaussian attributes, without per-scene training or iterative pose refinement.

  </details>


- **[High-Fidelity Surface Splatting-Based 3D Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.07254)**  
  *Nandhana Sunil, Abhirami R Iyer, Avirup Mandal*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07254) · [pdf](https://arxiv.org/pdf/2605.07254.pdf)
  > 💡 针对多视图重建中高频细节缺失，提出紧凑多项式核与随机拉普拉斯正则化，实现更精确几何和清晰渲染。

  <details><summary>Abstract</summary>

  Multi-view mesh reconstruction remains a core challenge in computer graphics and vision, especially for recovering high-frequency geometry from sparse observations. Recent methods such as 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) rely on post-processing for mesh extraction, thereby limiting joint optimization of geometry and appearance. Implicit Moving Least Squares (IMLS) instead enables direct conversion of point clouds into signed distance and texture fields, supporting end-to-end reconstruction and rendering. However, existing IMLS formulations use exponential kernels that struggle with high-frequency detail. We introduce a compact polynomial kernel with local support and greater flexibility, allowing better control over frequency content and improved geometric fidelity. To further enhance fine details, we incorporate stochastic regularization with Laplacian filtering. Together, these improve the preservation of high-frequency structure while maintaining stable optimization. Experiments show state-of-the-art performance in both surface reconstruction and rendering, yielding more accurate geometry and sharper visuals from multi-view data.

  </details>


- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736)**  
  *Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang*  
  `2026-05-03` · `cs.CV` · [abs](https://arxiv.org/abs/2605.01736) · [pdf](https://arxiv.org/pdf/2605.01736.pdf)
  > 💡 提出多尺度高斯-语言地图，整合显式几何与实例/区域语义，以双模态接口支持零样本具身导航与推理。

  <details><summary>Abstract</summary>

  Understanding the geometric and semantic structure of environments is essential for embodied navigation and reasoning. Existing semantic mapping methods trade off between explicit geometry and multi-scale semantics, and lack a native interface for large models, thus requiring additional training of feature projection for semantic alignment. To this end, we propose the multi-scale Gaussian-Language Map (GLMap), which introduces three key designs: (1) explicit geometry, (2) multi-scale semantics covering both instance and region concepts, and (3) a dual-modality interface where each semantic unit jointly stores a natural language description and a 3D Gaussian representation. The 3D Gaussians enable compact storage and fast rendering of task-relevant images via Gaussian splatting. To enable efficient incremental construction, we further propose a Gaussian Estimator that analytically derives Gaussian parameters from dense point clouds without gradient-based optimization. Experiments on ObjectNav, InstNav, and SQA tasks show that GLMap effectively enhances target navigation and contextual reasoning, while remaining compatible with large-model-based methods in a zero-shot manner. The code is available at https://github.com/sx-zhang/GLMap.

  </details>


- **[2D-SuGaR: Surface-Aware Gaussian Splatting for Geometrically Accurate Mesh Reconstruction](https://arxiv.org/abs/2605.00569)**  
  *Prajwal Gupta C. R., Divyam Sheth, Jinjoo Ha, Mirela Ostrek, Justus Thies*  
  `2026-05-01` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00569) · [pdf](https://arxiv.org/pdf/2605.00569.pdf)
  > 💡 针对2DGS对初始化敏感问题，引入单目深度和法线先验，提出深度引导初始化和聚类裁剪，实现高精度网格重建和新视角合成。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a powerful technique for generating photorealistic renderings of a scene in real-time. However, the volumetric nature of 3DGS limits its ability to accurately capture surface geometry. To address this, 2D Gaussian Splatting (2DGS) was proposed to enable view-consistent and geometrically accurate surface reconstruction from multi-view images. However, 2DGS can be sensitive to the initialization of the Gaussian primitives. Reliance on Structure-from-Motion (SfM) initializations, which can produce poor estimates on challenging image sets, may lead to subpar results. In this work, we enhance 2DGS by incorporating monocular depth and normal priors to improve both geometric accuracy and robustness. We propose a depth-guided initialization strategy for Gaussians and introduce a clustering-based technique for pruning degenerate Gaussians. We evaluate our method on the DTU dataset, where it achieves state-of-the-art results in mesh reconstruction while preserving high-quality novel view synthesis.

  </details>


- **[MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching](https://arxiv.org/abs/2604.26799)**  
  *Shuzhao Xie, Junchen Ge, Weixiang Zhang, Jiahang Liu, Chen Tang, Yunpeng Bai, Shijia Ge, Jingyan Jiang, Yuzhi Huang, Fengnian Yang, Cong Zhang, Xiaoyi Fan, Zhi Wang*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26799) · [pdf](https://arxiv.org/pdf/2604.26799.pdf)
  > 💡 提出大小感知后训练压缩方法，联合剪枝、八叉树几何

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression methods still rely on many coupled hyperparameters across pruning, transformation, quantization, and entropy coding, making it difficult to control the final compressed size and fully exploit the rate-distortion trade-off. We propose MesonGS++, a size-aware post-training codec for 3D Gaussian compression. On the codec side, MesonGS++ combines joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization with entropy coding. On the configuration side, it treats the reserve ratio and bit-width allocation as the dominant rate-distortion knobs and jointly optimizes them under a target storage budget via discrete sampling and 0--1 integer linear programming. We further propose a linear size estimator and a CUDA parallel quantization operator to accelerate the hyperparameter searching process. Extensive experiments show that MesonGS++ achieves over 34$\times$ compression while preserving rendering fidelity, outperforming state-of-the-art post-training methods and accurately meeting target size budgets. Remarkably, without any training, MesonGS++ can even surpass the PSNR of vanilla 3DGS at a 20$\times$ compression rate on the Stump scene. Our code is available at https://github.com/mmlab-sigs/mesongs_plus

  </details>


- **[Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training](https://arxiv.org/abs/2604.20046)**  
  *Yangming Zhang, Jian Xu, Chaojian Li, Kunxiong Zhu, Wei Niu, Gagan Agrawal, Yang Katie Zhao, Jian Wang, Yingyan Celine Lin, Miao Yin*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20046) · [pdf](https://arxiv.org/pdf/2604.20046.pdf)
  > 💡 针对3DGS训练内存峰值问题，提出迭代生长与剪枝的内存受限框架，以低内存实现高质量渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized novel view synthesis with high-quality rendering through continuous aggregations of millions of 3D Gaussian primitives. However, it suffers from a substantial memory footprint, particularly during training due to uncontrolled densification, posing a critical bottleneck for deployment on memory-constrained edge devices. While existing methods prune redundant Gaussians post-training, they fail to address the peak memory spikes caused by the abrupt growth of Gaussians early in the training process. To solve the training memory consumption problem, we propose a systematic memory-bounded training framework that dynamically optimizes Gaussians through iterative growth and pruning. In other words, the proposed framework alternates between incremental pruning of low-impact Gaussians and strategic growing of new primitives with an adaptive Gaussian compensation, maintaining a near-constant low memory usage while progressively refining rendering fidelity. We comprehensively evaluate the proposed training framework on various real-world datasets under strict memory constraints, showing significant improvements over existing state-of-the-art methods. Particularly, our proposed method practically enables memory-efficient 3DGS training on NVIDIA Jetson AGX Xavier, achieving similar visual quality with up to 80% lower peak training memory consumption than the original 3DGS.

  </details>


- **[OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem](https://arxiv.org/abs/2604.19127)**  
  *Byunghyun Kim*  
  `2026-04-21` · `cs.GR` · [abs](https://arxiv.org/abs/2604.19127) · [pdf](https://arxiv.org/pdf/2604.19127.pdf)
  > 💡 将UV映射重释为容量分配问题，用一维最优传输排序全局分配高斯，提升UV利用率和渲染质量。

  <details><summary>Abstract</summary>

  UV-parameterized Gaussian Splatting (UVGS) maps an unstructured set of 3D Gaussians to a regular UV tensor, enabling compact storage and explicit control of representation capacity. Existing UVGS, however, uses a deterministic spherical pro- jection to assign Gaussians to UV locations. Because this mapping ignores the global Gaussian distribution, it often leaves many UV slots empty while causing frequent collisions in dense regions. We reinterpret UV mapping as a capacity-allocation problem under a fixed UV budget and propose OT-UVGS, a lightweight, separable one-dimensional optimal-transport-inspired mapping that globally couples assignments while preserving the original UVGS representation. The method is implemented with rank-based sorting, has O(N log N) complexity for N Gaussians, and can be used as a drop-in replacement for spherical UVGS. Across 184 object-centric scenes and the Mip-NeRF dataset, OT-UVGS consistently improves peak signal-to-noise ratio (PSNR), structural similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) under the same UV resolution and per-slot capacity (K=1). These gains are accompanied by substantially better UV utilization, including higher non-empty slot ratios, fewer collisions, and higher Gaussian retention. Our results show that revisiting the mapping alone can unlock a significant fraction of the latent capacity of UVGS.

  </details>


- **[GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow](https://arxiv.org/abs/2604.15612)**  
  *Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung*  
  `2026-04-17` · `cs.RO` · [abs](https://arxiv.org/abs/2604.15612) · [pdf](https://arxiv.org/pdf/2604.15612.pdf)
  > 💡 针对单目SLAM缺乏几何线索，用光流引导高斯运动场对齐，结合归一化误差优化，提升渲染与跟踪精度。

  <details><summary>Abstract</summary>

  Gaussian splatting has recently gained traction as a compelling map representation for SLAM systems, enabling dense and photo-realistic scene modeling. However, its application to monocular SLAM remains challenging due to the lack of reliable geometric cues from monocular input. Without geometric supervision, mapping or tracking could fall in local-minima, resulting in structural degeneracies and inaccuracies. To address this challenge, we propose GaussianFlow SLAM, a monocular 3DGS-SLAM that leverages optical flow as a geometry-aware cue to guide the optimization of both the scene structure and camera poses. By encouraging the projected motion of Gaussians, termed GaussianFlow, to align with the optical flow, our method introduces consistent structural cues to regularize both map reconstruction and pose estimation. Furthermore, we introduce normalized error-based densification and pruning modules to refine inactive and unstable Gaussians, thereby contributing to improved map quality and pose accuracy. Experiments conducted on public datasets demonstrate that our method achieves superior rendering quality and tracking accuracy compared with state-of-the-art algorithms. The source code is available at: https://github.com/url-kaist/gaussianflow-slam.

  </details>


- **[GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284)**  
  *Roni Itkin, Noam Issachar, Yehonatan Keypur, Xingyu Chen, Anpei Chen, Sagie Benaim*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15284) · [pdf](https://arxiv.org/pdf/2604.15284.pdf)
  > 💡 现有前馈3DGS局部分配冗余且缺乏全局一致性；提出GlobalSplat，先学习紧凑全局潜在场景表示再解码，实现少高斯、低内存、快速推理。

  <details><summary>Abstract</summary>

  The efficient spatial allocation of primitives serves as the foundation of 3D Gaussian Splatting, as it directly dictates the synergy between representation compactness, reconstruction speed, and rendering fidelity. Previous solutions, whether based on iterative optimization or feed-forward inference, suffer from significant trade-offs between these goals, mainly due to the reliance on local, heuristic-driven allocation strategies that lack global scene awareness. Specifically, current feed-forward methods are largely pixel-aligned or voxel-aligned. By unprojecting pixels into dense, view-aligned primitives, they bake redundancy into the 3D asset. As more input views are added, the representation size increases and global consistency becomes fragile. To this end, we introduce GlobalSplat, a framework built on the principle of align first, decode later. Our approach learns a compact, global, latent scene representation that encodes multi-view input and resolves cross-view correspondences before decoding any explicit 3D geometry. Crucially, this formulation enables compact, globally consistent reconstructions without relying on pretrained pixel-prediction backbones or reusing latent features from dense baselines. Utilizing a coarse-to-fine training curriculum that gradually increases decoded capacity, GlobalSplat natively prevents representation bloat. On RealEstate10K and ACID, our model achieves competitive novel-view synthesis performance while utilizing as few as 16K Gaussians, significantly less than required by dense pipelines, obtaining a light 4MB footprint. Further, GlobalSplat enables significantly faster inference than the baselines, operating under 78 milliseconds in a single forward pass. Project page is available at https://r-itk.github.io/globalsplat/

  </details>


- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401)**  
  *Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11401) · [pdf](https://arxiv.org/pdf/2604.11401.pdf)
  > 💡 利用CityGML先验，通过双光线投射融合掩膜与2D预测，学习紧凑身份编码，提升城市语义分割精度达15.8 IoU点。

  <details><summary>Abstract</summary>

  Recent semantic 3D Gaussian Splatting (3DGS) methods primarily rely on 2D foundation models, often yielding ambiguous boundaries and limited support for structured urban semantics. While city models such as CityGML encode hierarchically organized semantics together with building geometry, these labels cannot be directly mapped to Gaussian primitives. We present GS4City, a hierarchical semantic Gaussian Splatting method that incorporates city-model priors for urban scene understanding. GS4City derives reliable image-aligned masks from Level of Detail (LoD) 3 CityGML models via two-pass raycasting, explicitly using parent-child relations to validate and recover fine-grained facade elements. It then fuses these geometry-grounded masks with foundation-model predictions to establish scene-consistent instance correspondences, and learns a compact identity encoding for each Gaussian under joint 2D identity supervision and 3D spatial regularization. Experiments on the TUM2TWIN and Gold Coast datasets show that GS4City effectively incorporates structured building semantics into Gaussian scene representations, outperforming existing 2D-driven semantic 3DGS baselines, including LangSplat and Gaga, by up to 15.8 IoU points in coarse building segmentation and 14.2 mIoU points in fine-grained semantic segmentation. By bridging structured city models and photorealistic Gaussian scene representations, GS4City enables semantically queryable and structure-aware urban reconstruction. Code is available at https://github.com/Jinyzzz/GS4City.

  </details>


- **[Naka-GS: A Bionics-inspired Dual-Branch Naka Correction and Progressive Point Pruning for Low-Light 3DGS](https://arxiv.org/abs/2604.11142)**  
  *Runyu Zhu, SiXun Dong, Zhiqiang Zhang, Qingxia Ye, Zhihua Xu*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11142) · [pdf](https://arxiv.org/pdf/2604.11142.pdf)
  > 💡 针对低光3DGS，提出仿生Naka校正网络与渐进点剪枝，提升重建质量与稳定性。

  <details><summary>Abstract</summary>

  Low-light conditions severely hinder 3D restoration and reconstruction by degrading image visibility, introducing color distortions, and contaminating geometric priors for downstream optimization. We present NAKA-GS, a bionics-inspired framework for low-light 3D Gaussian Splatting that jointly improves photometric restoration and geometric initialization. Our method starts with a Naka-guided chroma-correction network, which combines physics-prior low-light enhancement, dual-branch input modeling, frequency-decoupled correction, and mask-guided optimization to suppress bright-region chromatic artifacts and edge-structure errors. The enhanced images are then fed into a feed-forward multi-view reconstruction model to produce dense scene priors. To further improve Gaussian initialization, we introduce a lightweight Point Preprocessing Module (PPM) that performs coordinate alignment, voxel pooling, and distance-adaptive progressive pruning to remove noisy and redundant points while preserving representative structures. Without introducing heavy inference overhead, NAKA-GS improves restoration quality, training stability, and optimization efficiency for low-light 3D reconstruction. The proposed method was presented in the NTIRE 3D Restoration and Reconstruction (3DRR) Challenge, and outperformed the baseline methods by a large margin. The code is available at https://github.com/RunyuZhu/Naka-GS

  </details>


- **[A 129FPS Full HD Real-Time Accelerator for 3D Gaussian Splatting](https://arxiv.org/abs/2604.10223)**  
  *Fang-Chi Chang, Tian-Sheuan Chang*  
  `2026-04-11` · `cs.AR` · [abs](https://arxiv.org/abs/2604.10223) · [pdf](https://arxiv.org/pdf/2604.10223.pdf)
  > 💡 针对3DGS在AR/VR设备上高计算与存储成本，提出低功耗硬件加速器及压缩管道，实现129F

  <details><summary>Abstract</summary>

  Rendering large-scale, unbounded scenes on AR/VR-class devices is constrained by the computation, bandwidth, and storage cost of 3D Gaussian Splatting (3DGS). We propose a low-power, low-cost 3DGS hardware accelerator that renders full-HD images in real time, together with a hardware-friendly compression pipeline that combines iterative Gaussian pruning and fine-tuning, progressive spherical harmonics (SH) degree reduction, and vector quantization of all SH coefficients and colors. The scheme achieves a $51.6\times$ model-size reduction with a 0.743 dB PSNR loss. The accelerator uses a frame-level pipeline that integrates point-based culling and projection with tile-based sorting and rasterization, skips zero-Jacobian matrix multiplications (reducing processing elements by 63\% and computation by 53\%), and adopts comparison-free tile-based sorting with deterministic latency. Implemented in a TSMC 28-nm process at 800 MHz, the design occupies $0.66~\text{mm}^2$ with 1.1438 M gates and 120 kB SRAM, consumes 0.219 W, and delivers 1219 Mpixels/J at 267.5 Mpixels/s, enabling 1080p at 129 FPS. Overall, it is $5.98\times$ smaller in area, $5.94\times$ higher throughput, and delivers $7.5\times$ higher energy efficiency than prior 3DGS accelerators.

  </details>


- **[PointSplat: Efficient Geometry-Driven Pruning and Transformer Refinement for 3D Gaussian Splatting](https://arxiv.org/abs/2604.09903)**  
  *Anh Thuan Tran, Jana Kosecka*  
  `2026-04-10` · `cs.CV` · [abs](https://arxiv.org/abs/2604.09903) · [pdf](https://arxiv.org/pdf/2604.09903.pdf)
  > 💡 提出3DGS中几何驱动剪枝与双分支Transformer精炼框架，减少内存依赖，无需逐场景优化即可保持高渲染质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently unlocked real-time, high-fidelity novel view synthesis by representing scenes using explicit 3D primitives. However, traditional methods often require millions of Gaussians to capture complex scenes, leading to significant memory and storage demands. Recent approaches have addressed this issue through pruning and per-scene fine-tuning of Gaussian parameters, thereby reducing the model size while maintaining visual quality. These strategies typically rely on 2D images to compute important scores followed by scene-specific optimization. In this work, we introduce PointSplat, 3D geometry-driven prune-and-refine framework that bridges previously disjoint directions of gaussian pruning and transformer refinement. Our method includes two key components: (1) an efficient geometry-driven strategy that ranks Gaussians based solely on their 3D attributes, removing reliance on 2D images during pruning stage, and (2) a dual-branch encoder that separates, re-weights geometric and appearance to avoid feature imbalance. Extensive experiments on ScanNet++ and Replica across varying sparsity levels demonstrate that PointSplat consistently achieves competitive rendering quality and superior efficiency without additional per-scene optimization.

  </details>


- **[DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting](https://arxiv.org/abs/2604.06739)**  
  *Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan*  
  `2026-04-08` · `cs.CV` · [abs](https://arxiv.org/abs/2604.06739) · [pdf](https://arxiv.org/pdf/2604.06739.pdf)
  > 💡 针对稀疏视图3DGS过拟合伪影问题，提出双域观测校准框架，利用深度引导丢弃和暗通道先验提升可靠性。

  <details><summary>Abstract</summary>

  Sparse-view reconstruction with 3D Gaussian Splatting (3DGS) is fundamentally ill-posed due to insufficient geometric supervision, often leading to severe overfitting and the emergence of structural distortions and translucent haze-like artifacts. While existing approaches attempt to alleviate this issue via dropout-based regularization, they are largely heuristic and lack a unified understanding of artifact formation. In this paper, we revisit sparse-view 3DGS reconstruction from a new perspective and identify the core challenge as the unobservability of Gaussian primitive reliability. Unreliable Gaussians are insufficiently constrained during optimization and accumulate as haze-like degradations in rendered images. Motivated by this observation, we propose a unified Dual-domain Observation and Calibration (DOC-GS) framework that models and corrects Gaussian reliability through the synergy of optimization-domain inductive bias and observation-domain evidence. Specifically, in the optimization domain, we characterize Gaussian reliability by the degree to which each primitive is constrained during training, and instantiate this signal via a Continuous Depth-Guided Dropout (CDGD) strategy, where the dropout probability serves as an explicit proxy for primitive reliability. This imposes a smooth depth-aware inductive bias to suppress weakly constrained Gaussians and improve optimization stability. In the observation domain, we establish a connection between floater artifacts and atmospheric scattering, and leverage the Dark Channel Prior (DCP) as a structural consistency cue to identify and accumulate anomalous regions. Based on cross-view aggregated evidence, we further design a reliability-driven geometric pruning strategy to remove low-confidence Gaussians.

  </details>


- **[3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models](https://arxiv.org/abs/2604.05366)**  
  *Jae Joong Lee*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05366) · [pdf](https://arxiv.org/pdf/2604.05366.pdf)
  > 💡 针对3DGS和DUSt3R，利用随机旋转使参数服从Beta分布，实现免训练近最优Lloyd-Max量化，压缩数倍几乎无损。

  <details><summary>Abstract</summary>

  Every existing method for compressing 3D Gaussian Splatting, NeRF, or transformer-based 3D reconstructors requires learning a data-dependent codebook through per-scene fine-tuning. We show this is unnecessary. The parameter vectors that dominate storage in these models, 45-dimensional spherical harmonics in 3DGS and 1024-dimensional key-value vectors in DUSt3R, fall in a dimension range where a single random rotation transforms any input into coordinates with a known Beta distribution. This makes precomputed, data-independent Lloyd-Max quantization near-optimal, within a factor of 2.7 of the information-theoretic lower bound. We develop 3D, deriving (1) a dimension-dependent criterion that predicts which parameters can be quantized and at what bit-width before running any experiment, (2) norm-separation bounds connecting quantization MSE to rendering PSNR per scene, (3) an entry-grouping strategy extending rotation-based quantization to 2-dimensional hash grid features, and (4) a composable pruning-quantization pipeline with a closed-form compression ratio. On NeRF Synthetic, 3DTurboQuant compresses 3DGS by 3.5x with 0.02dB PSNR loss and DUSt3R KV caches by 7.9x with 39.7dB pointmap fidelity. No training, no codebook learning, no calibration data. Compression takes seconds. The code will be released (https://github.com/JaeLee18/3DTurboQuant)

  </details>


- **[GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields](https://arxiv.org/abs/2604.05062)**  
  *Yuhang Zhang, Mingsheng Li, Yujing Shang, Zhuoyuan Yu, Chao Yan, Jiaping Xiao, Mir Feroskhan*  
  `2026-04-06` · `cs.RO` · [abs](https://arxiv.org/abs/2604.05062) · [pdf](https://arxiv.org/pdf/2604.05062.pdf)
  > 💡 利用3DGS重建场景和对比学习提取鲁棒特征，解决单目自主飞行策略的样本效率低与sim-to-real差距，实现零样本迁移。

  <details><summary>Abstract</summary>

  Learning visuomotor policies for Autonomous Aerial Vehicles (AAVs) relying solely on monocular vision is an attractive yet highly challenging paradigm. Existing end-to-end learning approaches directly map high-dimensional RGB observations to action commands, which frequently suffer from low sample efficiency and severe sim-to-real gaps due to the visual discrepancy between simulation and physical domains. To address these long-standing challenges, we propose GaussFly, a novel framework that explicitly decouples representation learning from policy optimization through a cohesive real-to-sim-to-real paradigm. First, to achieve a high-fidelity real-to-sim transition, we reconstruct training scenes using 3D Gaussian Splatting (3DGS) augmented with explicit geometric constraints. Second, to ensure robust sim-to-real transfer, we leverage these photorealistic simulated environments and employ contrastive representation learning to extract compact, noise-resilient latent features from the rendered RGB images. By utilizing this pre-trained encoder to provide low-dimensional feature inputs, the computational burden on the visuomotor policy is significantly reduced while its resistance against visual noise is inherently enhanced. Extensive experiments in simulated and real-world environments demonstrate that GaussFly achieves superior sample efficiency and asymptotic performance compared to baselines. Crucially, it enables robust and zero-shot policy transfer to unseen real-world environments with complex textures, effectively bridging the sim-to-real gap.

  </details>


- **[SparseSplat: Towards Applicable Feed-Forward 3D Gaussian Splatting with Pixel-Unaligned Prediction](https://arxiv.org/abs/2604.03069)**  
  *Zicheng Zhang, Xiangting Meng, Ke Wu, Wenchao Ding*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03069) · [pdf](https://arxiv.org/pdf/2604.03069.pdf)
  > 💡 针对前馈3DGS高斯冗余问题，提出熵采样自适应密度与高效点云网络，仅用22%高斯达到最优渲染质量。

  <details><summary>Abstract</summary>

  Recent progress in feed-forward 3D Gaussian Splatting (3DGS) has notably improved rendering quality. However, the spatially uniform and highly redundant 3DGS map generated by previous feed-forward 3DGS methods limits their integration into downstream reconstruction tasks. We propose SparseSplat, the first feed-forward 3DGS model that adaptively adjusts Gaussian density according to scene structure and information richness of local regions, yielding highly compact 3DGS maps. To achieve this, we propose entropy-based probabilistic sampling, generating large, sparse Gaussians in textureless areas and assigning small, dense Gaussians to regions with rich information. Additionally, we designed a specialized point cloud network that efficiently encodes local context and decodes it into 3DGS attributes, addressing the receptive field mismatch between the general 3DGS optimization pipeline and feed-forward models. Extensive experimental results demonstrate that SparseSplat can achieve state-of-the-art rendering quality with only 22% of the Gaussians and maintain reasonable rendering quality with only 1.5% of the Gaussians. Project page: https://victkk.github.io/SparseSplat-page/.

  </details>


- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884)**  
  *Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01884) · [pdf](https://arxiv.org/pdf/2604.01884.pdf)
  > 💡 针对3DGS

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has demonstrated breakthrough performance in novel view synthesis and real-time rendering. Nevertheless, its practicality is constrained by the high memory cost due to a huge number of Gaussian points. Many pruning-based 3DGS variants have been proposed for memory saving, but often compromise spatial consistency and may lead to rendering artifacts. To address this issue, we propose graph-based spatial distribution optimization for compact 3D Gaussian Splatting (GS\textasciicircum2), which enhances reconstruction quality by optimizing the spatial distribution of Gaussian points. Specifically, we introduce an evidence lower bound (ELBO)-based adaptive densification strategy that automatically controls the densification process. In addition, an opacity-aware progressive pruning strategy is proposed to further reduce memory consumption by dynamically removing low-opacity Gaussian points. Furthermore, we propose a graph-based feature encoding module to adjust the spatial distribution via feature-guided point shifting. Extensive experiments validate that GS\textasciicircum2 achieves a compact Gaussian representation while delivering superior rendering quality. Compared with 3DGS, it achieves higher PSNR with only about 12.5\% Gaussian points. Furthermore, it outperforms all compared baselines in both rendering quality and memory efficiency.

  </details>


- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431)**  
  *Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan*  
  `2026-03-30` · `cs.CV` · [abs](https://arxiv.org/abs/2603.28431) · [pdf](https://arxiv.org/pdf/2603.28431.pdf)
  > 💡 针对3DGS锚点剪枝与熵编码忽视几何依赖导致结构退化，提出LG-HCC利用邻域感知剪枝和几何引导卷积实现紧凑表征，存储压缩30.85倍且保持几何完整。

  <details><summary>Abstract</summary>

  Although 3D Gaussian Splatting (3DGS) enables high-fidelity real-time rendering, its prohibitive storage overhead severely hinders practical deployment. Recent anchor-based 3DGS compression schemes reduce gaussian redundancy through some advanced context models. However, they overlook explicit geometric dependencies, leading to structural degradation and suboptimal ratedistortion performance. In this paper, we propose a Local Geometry-aware Hierarchical Context Compression framework for 3DGS(LG-HCC) that incorporates inter-anchor geometric correlations into anchor pruning and entropy coding for compact representation. Specifically, we introduce an Neighborhood-Aware Anchor Pruning (NAAP) strategy, which evaluates anchor importance via weighted neighborhood feature aggregation and then merges low-contribution anchors into salient neighbors, yielding a compact yet geometry-consistent anchor set. Moreover, we further develop a hierarchical entropy coding scheme, in which coarse-to-fine priors are exploited through a lightweight Geometry-Guided Convolution(GG-Conv) operator to enable spatially adaptive context modeling and rate-distortion optimization. Extensive experiments show that LG-HCC effectively alleviates structural preservation issues,achieving superior geometric integrity and rendering fidelity while reducing storage by up to 30.85x compared to the Scaffold-GS baseline on the Mip-NeRF360 dataset

  </details>


- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036)**  
  *Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany*  
  `2026-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2603.24036) · [pdf](https://arxiv.org/pdf/2603.24036.pdf)
  > 💡 用频域谱矩监督替代空间损失并引入频率退火，解决3DGS跟踪中梯度消失问题，实现鲁棒跟踪。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables real-time, photorealistic novel view synthesis, making it a highly attractive representation for model-based video tracking. However, leveraging the differentiability of the 3DGS renderer "in the wild" remains notoriously fragile. A fundamental bottleneck lies in the compact, local support of the Gaussian primitives. Standard photometric objectives implicitly rely on spatial overlap; if severe camera misalignment places the rendered object outside the target's local footprint, gradients strictly vanish, leaving the optimizer stranded. We introduce SpectralSplats, a robust tracking framework that resolves this "vanishing gradient" problem by shifting the optimization objective from the spatial to the frequency domain. By supervising the rendered image via a set of global complex sinusoidal features (Spectral Moments), we construct a global basin of attraction, ensuring that a valid, directional gradient toward the target exists across the entire image domain, even when pixel overlap is completely nonexistent. To harness this global basin without introducing periodic local minima associated with high frequencies, we derive a principled Frequency Annealing schedule from first principles, gracefully transitioning the optimizer from global convexity to precise spatial alignment. We demonstrate that SpectralSplats acts as a seamless, drop-in replacement for spatial losses across diverse deformation parameterizations (from MLPs to sparse control points), successfully recovering complex deformations even from severely misaligned initializations where standard appearance-based tracking catastrophically fails.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (29) · <a href="topics/rendering.md">full list →</a></summary>

- **[Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342)**  
  *Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30342) · [pdf](https://arxiv.org/pdf/2605.30342.pdf)
  > 💡 提出各向异性可见性场量化3DGS不确定度，结合贝叶斯网络实现实时主动建图，显著提升精度与效率。

  <details><summary>Abstract</summary>

  We present Gaussian Splatting Anisotropic Visibility Field (GAVIS), a novel framework for uncertainty quantification and active mapping in 3DGS. Our key insight is that regions unseen from the training views yield unreliable predictions from the 3DGS. To address this, we introduce a principled and efficient method for quantifying the visibility field in 3DGS, defined as the anisotropic visibility of each particle with respect to the training views, and represented using spherical harmonics. The resulting visibility field is integrated into a Bayesian Network-based uncertainty-aware 3DGS rasterizer, enabling real-time (200 FPS) uncertainty quantification for synthesized views. Active mapping is further performed within a maximum information gain framework building on this formulation. Extensive experiments across diverse environments demonstrate that GAVIS consistently and significantly outperforms prior approaches in both accuracy and efficiency. Moreover, beyond standalone use, our method can be applied post-hoc to improve the performance of existing approaches.

  </details>


- **[Gaussian-Voxel Duet: A Dual-Scaffolding Hybrid Representation for Fast and Accurate Monocular Surface Reconstruction](https://arxiv.org/abs/2605.26616)**  
  *Zhenhua Du, Zhen Tan, Haoyu Zhang, Dewen Hu, Shuaifeng Zhi, Peidong Liu*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26616) · [pdf](https://arxiv.org/pdf/2605.26616.pdf)
  > 💡 为平衡几何精度与效率，提出高斯-体素双支架混合表示，用稀疏体素支架约束高斯，实现快速准确的单目表面重建。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting has achieved remarkable success in photorealistic novel view synthesis, its pursuit of fast and high-fidelity 3D reconstruction has long been constrained by a trade-off between geometric accuracy and optimization efficiency. Methods specialized in image rendering converge quickly at the cost of imperfect geometry caused by superfluous primitives overfitting training views, while methods integrating neural signed-distance field (SDF) for better geometry incur prohibitive training costs. In this paper, we attempt to strike a better trade-off by tethering scaffold-anchored Gaussians to a jointly optimized sparse voxel scaffold. This hybrid Gaussian-Voxel representation explicitly confines anchored Gaussians to a narrow band around surfaces defined by voxelized SDFs, which effectively improves representation efficiency and condenses floating Gaussians without sacrificing geometry quality. An implicit surface tethering loss further pulls individual Gaussian primitives closer to SDF-induced surfaces in a mutually regularized manner for improved reconstruction accuracy. Extensive experiments on diverse real-world indoor scenes from ScanNet++, ScanNetv2, and DeepBlending datasets demonstrate that our method achieves state-of-the-art surface reconstruction quality as well as superior novel view synthesis against leading baselines, while maintaining fast training convergence and real-time rendering. Code will be available at https://github.com/duzh11/VoxelGS.

  </details>


- **[Accelerating 3D Gaussian Splatting using Tensor Cores](https://arxiv.org/abs/2605.17855)**  
  *Sheng Li, Yang Sui, Yue Wu, Zhuoran Song, Bo Yuan, Xulong Tang, Yue Dai*  
  `2026-05-18` · `cs.GR` · [abs](https://arxiv.org/abs/2605.17855) · [pdf](https://arxiv.org/pdf/2605.17855.pdf)
  > 💡 提出TensorGS，利用张量核心加速3DGS光栅化，通过张量化和跨块分组

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become a leading technique for real-time neural rendering and 3D scene reconstruction, but its rendering cost remains too high for many latency-sensitive scenarios. In particular, the rasterization stage in 3DGS dominates end-to-end rendering time, during which the renderer repeatedly evaluates each Gaussian's contribution to each covered pixel, making this stage compute-bound. At the same time, modern GPUs provide high-throughput Tensor Cores for low-precision matrix operations, yet existing 3DGS systems execute rasterization entirely on CUDA cores and leave Tensor Cores idle. We find that 3DGS rendering can be executed in FP16 with negligible quality degradation, suggesting a promising opportunity for Tensor Core acceleration. However, exploiting Tensor Cores for 3DGS is non-trivial because rasterization does not naturally match their execution model. Existing 3DGS rasterization is expressed as irregular per-pixel scalar operations, whereas Tensor Cores require dense, regular, and reuse-rich matrix workloads. Moreover, conventional tile-by-tile execution fails to exploit Gaussian reuse across neighboring tiles, resulting in repeated data loading and thus high data movement overhead. To this end, we present TensorGS, a 3DGS acceleration framework using Tensor Cores. TensorGS tensorizes the dominant rasterization computation into Tensor-Core-compatible matrix operations and introduces cross-tile grouping to improve Gaussian reuse, amortize overhead, and increase Tensor Core utilization. Experimental results show that TensorGS improves end-to-end rendering performance by 1.65$\times$ while preserving image quality.

  </details>


- **[3D Skew-Normal Splatting](https://arxiv.org/abs/2605.15010)**  
  *Xiangru Wu, Ke Fan, Yanwei Fu*  
  `2026-05-14` · `cs.CV` · [abs](https://arxiv.org/abs/2605.15010) · [pdf](https://arxiv.org/pdf/2605.15010.pdf)
  > 💡 针对对称高斯原语无法紧凑表示非对称结构的问题，提出偏斜正态原语，通过可学习偏斜参数连续插值提升重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a leading representation for real-time novel view synthesis and has been widely adopted in various downstream applications. The core strength of 3DGS lies in its efficient kernel-based scene representation, where Gaussian primitives provide favorable mathematical and computational properties. However, under a finite primitive budget, the symmetric shape of each primitive directly affects representation compactness, especially near asymmetric structures such as object boundaries and one-sided surfaces. Recent works have explored more complex kernel distributions; however, they either remain within the elliptical family or rely on hard truncation, which limits continuous shape control and introduces distributional discontinuities. In this paper, we propose Skew-Normal Splatting (SNS), which adopts the Azzalini Skew-Normal distribution as the fundamental primitive. By introducing a learnable and bounded skewness parameter, SNS can continuously interpolate between symmetric Gaussians and Half-Gaussian-like shapes, enabling flexible modeling of both sharp boundaries and interior regions. Moreover, SNS preserves analytical tractability under affine transformations and marginalization. This property allows seamless integration into existing Gaussian Splatting rasterization pipelines. Furthermore, to address the strong coupling between scale, rotation, and skewness parameters, we introduce a decoupled parameterization and a block-wise optimization strategy to enhance training stability and accuracy. Extensive experiments on standard novel-view synthesis benchmarks show that SNS consistently improves reconstruction quality over Gaussian and recent non-Gaussian kernels, with clearer benefits on sharp boundaries and thin or one-sided structures.

  </details>


- **[BlitzGS: City-Scale Gaussian Splatting at Lightning Speed](https://arxiv.org/abs/2605.13794)**  
  *Zhongtao Wang, Huishan Au, Yilong Li, Mai Su, Haojie Jin, Yisong Chen, Meng Gai, Fei Zhu, Guoping Wang*  
  `2026-05-13` · `cs.GR` · [abs](https://arxiv.org/abs/2605.13794) · [pdf](https://arxiv.org/pdf/2605.13794.pdf)
  > 💡 提出分布式3DGS框架BlitzGS，通过索引奇偶分片、重要性评分与LOD门控减少高斯数量，实现城市级场景训练速度提升一个数量级。

  <details><summary>Abstract</summary>

  We present BlitzGS, a distributed 3DGS framework that reduces active Gaussian workload for fast city-scale reconstruction. BlitzGS manages this workload at three coupled levels. At the system level, the framework shards Gaussians across GPUs by index parity rather than spatial blocks. This approach mitigates the cross-block visibility redundancy inherent in spatial partitioning. Furthermore, it distributes each rendering step through a single cross-GPU exchange that routes projected Gaussians to their tile owners. At the model level, scheduled importance-scoring passes shrink the global Gaussian population. During these passes, the framework generates a per-Gaussian visibility weight to bias density-control updates toward contributing primitives and a per-view importance mask for the view-level renderer. At the view level, BlitzGS trims each camera's active set with a distance-based LOD gate to exclude excessively fine primitives for the current frustum and the importance-based culling mask to skip Gaussians with negligible cross-view contribution. On large-scale benchmarks, BlitzGS matches the rendering quality of recent large-scale baselines while delivering an order-of-magnitude speedup, training city-scale scenes in tens of minutes. Our code is available at https: //github.com/AkierRaee/BlitzGS.

  </details>


- **[Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465)**  
  *Can Wang, Lei Liu, Wei Jiang, Dong Xu*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13465) · [pdf](https://arxiv.org/pdf/2605.13465.pdf)
  > 💡 通过Z-order策略将高斯原语组织为空间连贯序列，结合稀疏注意力机制的Transformer，实现前馈式3DGS的高效去冗余与高质量渲染。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in photorealistic novel view synthesis. However, traditional 3DGS relies on a slow, iterative optimization process, which limits its use in scenarios demanding real-time results. To overcome this bottleneck, recent feed-forward methods aim to predict Gaussian attributes directly from images, but they often struggle with the redundancy of Gaussian primitives and rendering quality. In this work, we introduce a transformer-based architecture specifically designed for feed-forward Gaussian Splatting. Our key insight is that spatial and semantic relationships among Gaussians can be effectively captured through a sparse attention mechanism, enabled by a Z-order strategy that organizes the unstructured Gaussian set into a spatially coherent sequence. Furthermore, we incorporate this Z-order strategy to adaptively suppress redundancy while preserving critical structural details. This allows the transformer to efficiently model context, compress Gaussian primitives, and predict Gaussian attributes in a single forward pass. Comprehensive experiments demonstrate that our method achieves fast and high-quality novel view synthesis with fewer Gaussian primitives.

  </details>


- **[Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis](https://arxiv.org/abs/2605.07781)**  
  *Niklas Vaara, Lam Huynh, Pekka Sangi, Miguel Bordallo López, Janne Heikkilä*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07781) · [pdf](https://arxiv.org/pdf/2605.07781.pdf)
  > 💡 针对3DGS缺乏可相交几何问题，将高斯原语嵌入光线追踪结构，实现统一可微分RF模拟与视图合成。

  <details><summary>Abstract</summary>

  Explicit neural representations such as 3D Gaussian Splatting (3DGS) enable high-fidelity and real-time novel view synthesis, yet optimize for alpha-composited optical appearance rather than ray-intersectable geometry. In contrast, radio-frequency (RF) digital twins require deterministic multi-bounce paths, where the geometry dictates trajectories and their associated attenuation and delay. We introduce a framework enabling differentiable RF propagation simulation directly within visually reconstructed neural scenes, allowing point-to-point path computation between arbitrary 3D locations while preserving high-quality visual rendering. Unlike conventional RF simulation pipelines that rely on manually constructed meshes, we embed Gaussian primitives into a hardware-accelerated ray tracing structure as the underlying spatial representation. By extracting physically meaningful channel impulse responses from visual-only reconstructions, we provide cross-modal evidence that neural reconstructions can serve as unified spatial representations for both electromagnetic propagation simulation and photorealistic view synthesis.

  </details>


- **[QuadBox: Accelerating 3D Gaussian Splatting with Geometry-Aware Boxes](https://arxiv.org/abs/2605.04844)**  
  *Xinze Li, Bohan Yang, Pengxu Chen, Yiyuan Wang, Hongcheng Luo, Wentao Cheng, Weifeng Su*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04844) · [pdf](https://arxiv.org/pdf/2605.04844.pdf)
  > 💡 使用几何感知包围盒加速3DGS渲染，通过QuadBox和QPass高效计算瓦片交集，速度提升1.85倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as an advanced technique for real-time novel view synthesis by representing scene geometry and appearance using differentiable Gaussian primitives. However, efficiently computing precise Gaussian-tile intersections remains a critical task in the rasterization pipeline. To this end, we propose QuadBox, a method that leverages four axis-aligned bounding boxes to tightly encapsulate projected Gaussians in a discrete manner. First, we derive a geometry-aware stretching factor that enables the construction of a tile-aligned QuadBox, which covers the elliptical projection and largely excludes irrelevant tiles. Second, we introduce QPass, a single-pass tile traversal algorithm that exhaustively exploits the discrete nature of QuadBox, ensuring that the tile intersection check is performed with simple interval tests. Experiments on public datasets show that our method accelerates the rendering speed of 3DGS by 1.85$\times$. Code is available at \href{https://github.com/Powertony102/QuadBox}{https://github.com/Powertony102/QuadBox}.

  </details>


- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509)**  
  *Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho*  
  `2026-05-06` · `cs.GR` · [abs](https://arxiv.org/abs/2605.04509) · [pdf](https://arxiv.org/pdf/2605.04509.pdf)
  > 💡 针对光场显示多视角渲染开销大的问题，提出CoherentRaster，通过子像素光栅化、跨视角属性重用与视角重映射，实现实时高质量合成。

  <details><summary>Abstract</summary>

  Light field displays (LFDs) require rendering an interlaced image that encodes many view-dependent observations. This multi-view requirement introduces substantial computational overhead, making real-time rendering difficult to achieve. While 3D Gaussian Splatting (3DGS) is efficient for single-view rendering on 2D displays, directly extending it to LFDs is computationally expensive. Moreover, prior accelerations either suffer from GPU inefficiency under spatially incoherent subpixel layouts or rely on computationally heavy multi-plane intermediates. In this paper, we propose CoherentRaster, a 3DGS-based light field rendering framework that performs subpixel-level rasterization. Our method employs Cross-view Coherent Attribute Reuse to eliminate redundant computation across neighboring viewpoints and applies View-coherent Remapping to restore warp-level memory efficiency degraded by the interlaced subpixel layout. Together, CoherentRaster provides an efficient pipeline for real-time, high-quality light field synthesis on consumer-grade hardware.

  </details>


- **[Beyond Heuristics: Learnable Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2605.00408)**  
  *Zhenhua Ning, Xin Li, Jun Yu, Guangming Lu, Yaowei Wang, Wenjie Pei*  
  `2026-05-01` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00408) · [pdf](https://arxiv.org/pdf/2605.00408.pdf)
  > 💡 将密度控制从启发式转化为强化学习可学习策略，设计敏感度奖励函数，实现效率和质量更优平衡。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) has demonstrated impressive real-time rendering performance, its efficacy remains constrained by a reliance on heuristic density control. Despite numerous refinements to these handcrafted rules, such methods inherently lack the flexibility to adapt to diverse scenes with complex geometries. In this paper, we propose a paradigm shift for density control from rigid heuristics to fully learnable policies. Specifically, we introduce \textbf{LeGS}, a framework that reformulates density control as a parameterized policy network optimized via Reinforcement Learning (RL). Central to our approach is the tailored effective reward function grounded in sensitivity analysis, which precisely quantifies the marginal contribution of individual Gaussians to reconstruction quality. To maintain computational tractability, we derive a closed-form solution that reduces the complexity of reward calculation from $O(N^2)$ to $O(N)$. Extensive experiments on the Mip-NeRF 360, Tanks \& Temples, and Deep Blending datasets demonstrate that \textbf{LeGS} significantly outperforms state-of-the-art methods, striking a superior balance between reconstruction quality and efficiency. The code will be released at https://github.com/AaronNZH/LeGS

  </details>


- **[Faster 3D Gaussian Splatting Convergence via Structure-Aware Densification](https://arxiv.org/abs/2604.28016)**  
  *Linjie Lyu, Ayush Tewari, Jianchun Chen, Thomas Leimkühler, Christian Theobalt*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.28016) · [pdf](https://arxiv.org/pdf/2604.28016.pdf)
  > 💡 标准密度控制忽视频率信息导致模糊或过密，提出多尺度频率分析和各向异性分裂机制，加速收敛并提升高频重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting has emerged as a powerful scene representation for real-time novel-view synthesis. However, its standard adaptive density control relies on screen-space positional gradients, which do not distinguish between geometric misplacement and frequency aliasing, often leading to either over-blurred high-frequency textures or inefficient over-densification. We present a structure-aware densification framework. Our key insight is that the decision to subdivide a Gaussian should be driven by an explicit comparison between its projected screen-space extent and the local structure of the texture it seeks to represent. We introduce a multi-scale frequency analysis combining structure tensors with Laplacian scale space analysis to estimate the dominant frequency at each pixel, enabling robust supervision across varying texture scales. Based on this analysis, we define $η$, a per-Gaussian, per-axis frequency violation metric that indicates when a primitive may be under-resolving local texture details. Unlike methods that perform isotropic splitting (e.g., splitting each Gaussian into two smaller ones with uniform shape), our approach performs anisotropic splitting. For each axis with high $η$, we compute a split factor to better resolve the local frequency content. We further introduce a multiview consistency criterion that aggregates $η$ observations across multiple views. By performing densification early and faster, we skip the lengthy iterative densification phases required by baseline methods and achieve significantly faster convergence. Experiments on standard benchmarks demonstrate that our method also achieves superior reconstruction quality, particularly in high-frequency regions.

  </details>


- **[Large-Scale Photogrammetric Documentation of St. John's Co-Cathedral: A Workflow for Cultural Heritage Preservation](https://arxiv.org/abs/2604.24316)**  
  *Matthew Kenely, Mark Bugeja, Andre Grima, Peter Pullicino, Matthew Pullicino, Dylan Seychell*  
  `2026-04-27` · `cs.GR` · [abs](https://arxiv.org/abs/2604.24316) · [pdf](https://arxiv.org/pdf/2604.24316.pdf)
  > 💡 提出大型文化遗产数字化工作流，融合多模态采集与AI去噪，初步探索高斯溅射用于复杂反射表面重建。

  <details><summary>Abstract</summary>

  We present a comprehensive methodology for the large-scale photogrammetric documentation of St. John's Co-Cathedral in Valletta, Malta, a UNESCO World Heritage site renowned for its ornate Baroque architecture and Caravaggio masterpieces. Over seven nights of evening-only data collection, we captured 99,000 images using DSLR cameras, drone photography, and LIDAR scanning to create a highly detailed 3D reconstruction comprising 25-30 billion triangles. This paper documents our complete workflow for cultural heritage preservation, addressing the unique challenges of digitizing complex baroque architectural spaces with highly reflective metallic surfaces, dark materials, intricate tapestries, and restricted access. We detail our pipeline from multi-modal data acquisition through processing, including strategic image grading and AI-assisted denoising to address low-light grain, extensive LIDAR point cloud cleanup, hybrid photogrammetric reconstruction using RealityCapture, and mesh subdivision strategies for real-time visualization engines. Our methodology combines automated workflows with necessary manual intervention to handle the scale and complexity of the project, with particular attention to reflective surface challenges characteristic of baroque heritage sites. We also present preliminary experiments with Gaussian splatting as a complementary representation technique. The resulting digital archive serves multiple preservation purposes including disaster recovery documentation, conservation analysis, virtual tourism, and scholarly research. This work provides a detailed, replicable workflow for heritage professionals undertaking similar large-scale architectural documentation projects, addressing the practical challenges of applying photogrammetric methods in complex real-world heritage scenarios.

  </details>


- **[WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182)**  
  *Yuki Fujimura, Takahiro Kushida, Kazuya Kitano, Takuya Funatomi, Yasuhiro Mukaigawa*  
  `2026-04-23` · `cs.CV` · [abs](https://arxiv.org/abs/2604.21182) · [pdf](https://arxiv.org/pdf/2604.21182.pdf)
  > 💡 从无约束图像中前馈生成3D高斯并联合学习外观嵌入，实现快速重建与可变光照下的外观控制。

  <details><summary>Abstract</summary>

  We propose WildSplatter, a feed-forward 3D Gaussian Splatting (3DGS) model for unconstrained images with unknown camera parameters and varying lighting conditions. 3DGS is an effective scene representation that enables high-quality, real-time rendering; however, it typically requires iterative optimization and multi-view images captured under consistent lighting with known camera parameters. WildSplatter is trained on unconstrained photo collections and jointly learns 3D Gaussians and appearance embeddings conditioned on input images. This design enables flexible modulation of Gaussian colors to represent significant variations in lighting and appearance. Our method reconstructs 3D Gaussians from sparse input views in under one second, while also enabling appearance control under diverse lighting conditions. Experimental results demonstrate that our approach outperforms existing pose-free 3DGS methods on challenging real-world datasets with varying illumination.

  </details>


- **[An Object-Centered Data Acquisition Method for 3D Gaussian Splatting using Mobile Phones](https://arxiv.org/abs/2604.19216)**  
  *Yuezhe Zhang, Luqian Bai, Mengting Yu, Lei Wei, Shuai Wan, Yifan Zhang*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.19216) · [pdf](https://arxiv.org/pdf/2604.19216.pdf)
  > 💡 针对手机采集3DGS困难，提出面向物体的引导式采集方法，利用球形网格和面积加权覆盖实现均匀视角，用更少图像达到更优重建质量。

  <details><summary>Abstract</summary>

  Data acquisition through mobile phones remains a challenge for 3D Gaussian Splatting (3DGS). In this work we target the object-centered scenario and enable reliable mobile acquisition by providing on-device capture guidance and recording onboard sensor signals for offline reconstruction. After the calibration step, the device orientations are aligned to a baseline frame to obtain relative poses, and the optical axis of the camera is mapped to an object-centered spherical grid for uniform viewpoint indexing. To curb polar sampling bias, we compute area-weighted spherical coverage in real-time and guide the user's motion accordingly. We compare the proposed method with RealityScan and the free-capture strategy. Our method achieves superior reconstruction quality using fewer input images compared to free capture and RealityScan. Further analysis shows that the proposed method is able to obtain more comprehensive and uniform viewpoint coverage during object-centered acquisition.

  </details>


- **[LAGS: Low-Altitude Gaussian Splatting with Groupwise Heterogeneous Graph Learning](https://arxiv.org/abs/2604.16910)**  
  *Yikun Wang, Yujie Wan, Wei Zuo, Shuai Wang, Yik-Chung Wu, Chengzhong Xu, Huseyin Arslan*  
  `2026-04-18` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16910) · [pdf](https://arxiv.org/pdf/2604.16910.pdf)
  > 💡 针对低空高斯散点重建中忽视图像多样性的资源分配问题，提出分组异构图神经网络GW-HGNN，通过双级消息传递平衡质量与成本，显著提升渲染指标并实现毫秒级推理。

  <details><summary>Abstract</summary>

  Low-altitude Gaussian splatting (LAGS) facilitates 3D scene reconstruction by aggregating aerial images from distributed drones. However, as LAGS prioritizes maximizing reconstruction quality over communication throughput, existing low-altitude resource allocation schemes become inefficient. This inefficiency stems from their failure to account for image diversity introduced by varying viewpoints. To fill this gap, we propose a groupwise heterogeneous graph neural network (GW-HGNN) for LAGS resource allocation. GW-HGNN explicitly models the non-uniform contribution of different image groups to the reconstruction process, thus automatically balancing data fidelity and transmission cost. The key insight of GW-HGNN is to transform LAGS losses and communication constraints into graph learning costs for dual-level message passing. Experiments on real-world LAGS datasets demonstrate that GW-HGNN significantly outperforms state-of-the-art benchmarks across key rendering metrics, including PSNR, SSIM, and LPIPS. Furthermore, GW-HGNN reduces computational latency by approximately 100x compared to the widely-used MOSEK solver, achieving millisecond-level inference suitable for real-time deployment.

  </details>


- **[MSGS: Multispectral 3D Gaussian Splatting](https://arxiv.org/abs/2604.13340)**  
  *Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13340) · [pdf](https://arxiv.org/pdf/2604.13340.pdf)
  > 💡 通过每波段球谐和双损失监督将3DGS扩展为多光谱

  <details><summary>Abstract</summary>

  We present a multispectral extension to 3D Gaussian Splatting (3DGS) for wavelength-aware view synthesis. Each Gaussian is augmented with spectral radiance, represented via per-band spherical harmonics, and optimized under a dual-loss supervision scheme combining RGB and multispectral signals. To improve rendering fidelity, we perform spectral-to-RGB conversion at the pixel level, allowing richer spectral cues to be retained during optimization. Our method is evaluated on both public and self-captured real-world datasets, demonstrating consistent improvements over the RGB-only 3DGS baseline in terms of image quality and spectral consistency. Notably, it excels in challenging scenes involving translucent materials and anisotropic reflections. The proposed approach maintains the compactness and real-time efficiency of 3DGS while laying the foundation for future integration with physically based shading models.

  </details>


- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942)**  
  *Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang*  
  `2026-04-14` · `cs.RO` · [abs](https://arxiv.org/abs/2604.12942) · [pdf](https://arxiv.org/pdf/2604.12942.pdf)
  > 💡 针对大规模场景实时3DGS SLAM挑战，提出多传感器紧耦合框架，并行优化与级联初始化实现实时建

  <details><summary>Abstract</summary>

  Achieving real-time Simultaneous Localization and Mapping (SLAM) based on 3D Gaussian splatting (3DGS) in large-scale real-world environments remains challenging, as existing methods still struggle to jointly achieve low-latency pose estimation, continuous 3D Gaussian reconstruction, and long-term global consistency. In this paper, we present a tightly coupled LiDAR-Inertial-Visual 3DGS-based SLAM framework for real-time pose estimation and photorealistic mapping in large-scale real-world scenes. The system executes state estimation and 3D Gaussian primitive initialization in parallel with global Gaussian optimization, enabling continuous dense mapping. To improve Gaussian initialization quality and accelerate optimization convergence, we introduce a cascaded strategy that combines feed-forward predictions with geometric priors derived from voxel-based principal component analysis. To enhance global consistency, we perform loop closure directly on the optimized global Gaussian map by estimating loop constraints through Gaussian-based Generalized Iterative Closest Point registration, followed by pose-graph optimization. We also collect challenging large-scale looped outdoor sequences with hardware-synchronized LiDAR-camera-IMU and ground-truth trajectories for realistic evaluation. Extensive experiments on both public datasets and our dataset demonstrate that the proposed method achieves a state of the art among real-time efficiency, localization accuracy, and rendering quality across diverse real-world scenes.

  </details>


- **[PDF-GS: Progressive Distractor Filtering for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2604.12580)**  
  *Kangmin Seo, MinKyu Lee, Tae-Young Kim, ByeongCheol Lee, JoonSeoung An, Jae-Pil Heo*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.12580) · [pdf](https://arxiv.org/pdf/2604.12580.pdf)
  > 💡 针对3DGS对多视角不一致干扰敏感问题，提出渐进式多阶段过滤方法，实现鲁棒高质量无干扰重建。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled impressive real-time photorealistic rendering. However, conventional training pipelines inherently assume full multi-view consistency among input images, which makes them sensitive to distractors that violate this assumption and cause visual artifacts. In this work, we revisit an underexplored aspect of 3DGS: its inherent ability to suppress inconsistent signals. Building on this insight, we propose PDF-GS (Progressive Distractor Filtering for Robust 3D Gaussian Splatting), a framework that amplifies this self-filtering property through a progressive multi-phase optimization. The progressive filtering phases gradually remove distractors by exploiting discrepancy cues, while the following reconstruction phase restores fine-grained, view-consistent details from the purified Gaussian representation. Through this iterative refinement, PDF-GS achieves robust, high-fidelity, and distractor-free reconstructions, consistently outperforming baselines across diverse datasets and challenging real-world conditions. Moreover, our approach is lightweight and easily adaptable to existing 3DGS frameworks, requiring no architectural changes or additional inference overhead, leading to a new state-of-the-art performance. The code is publicly available at https://github.com/kangrnin/PDF-GS.

  </details>


- **[Ψ-Map: Panoptic Surface Integrated Mapping Enables Real2Sim Transfer](https://arxiv.org/abs/2604.10982)**  
  *Xuan Yu, Yuxuan Xie, Changjian Jiang, Shichao Zhai, Rong Xiong, Yu Zhang, Yue Wang*  
  `2026-04-13` · `cs.RO` · [abs](https://arxiv.org/abs/2604.10982) · [pdf](https://arxiv.org/pdf/2604.10982.pdf)
  > 💡 提出几何强化、端到端全景学习与高效渲染框架，利用LiDAR平面约束和2D高斯曲面，实现高精度表面重建与全局一致全景分割，推理超40FPS。

  <details><summary>Abstract</summary>

  Open-vocabulary panoptic reconstruction is essential for advanced robotics perception and simulation. However, existing methods based on 3D Gaussian Splatting (3DGS) often struggle to simultaneously achieve geometric accuracy, coherent panoptic understanding, and real-time inference frequency in large-scale scenes. In this paper, we propose a comprehensive framework that integrates geometric reinforcement, end-to-end panoptic learning, and efficient rendering. First, to ensure physical realism in large-scale environments, we leverage LiDAR data to construct plane-constrained multimodal Gaussian Mixture Models (GMMs) and employ 2D Gaussian surfels as the map representation, enabling high-precision surface alignment and continuous geometric supervision. Building upon this, to overcome the error accumulation and cumbersome cross-frame association inherent in traditional multi-stage panoptic segmentation pipelines, we design a query-guided end-to-end learning architecture. By utilizing a local cross-attention mechanism within the view frustum, the system lifts 2D mask features directly into 3D space, achieving globally consistent panoptic understanding. Finally, addressing the computational bottlenecks caused by high-dimensional semantic features, we introduce Precise Tile Intersection and a Top-K Hard Selection strategy to optimize the rendering pipeline. Experimental results demonstrate that our system achieves superior geometric and panoptic reconstruction quality in large-scale scenes while maintaining an inference rate exceeding 40 FPS, meeting the real-time requirements of robotic control loops.

  </details>


- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337)**  
  *Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov*  
  `2026-04-08` · `cs.CV` · [abs](https://arxiv.org/abs/2604.07337) · [pdf](https://arxiv.org/pdf/2604.07337.pdf)
  > 💡 针对3DGS表面重建难题，通过可学习有向高斯及占用场公式，结合一致性损失与稠密化策略，实现高精度水

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized fast novel view synthesis, yet its opacity-based formulation makes surface extraction fundamentally difficult. Unlike implicit methods built on Signed Distance Fields or occupancy, 3DGS lacks a global geometric field, forcing existing approaches to resort to heuristics such as TSDF fusion of blended depth maps. Inspired by the Objects as Volumes framework, we derive a principled occupancy field for Gaussian Splatting and show how it can be used to extract highly accurate watertight meshes of complex scenes. Our key contribution is to introduce a learnable oriented normal at each Gaussian element and to define an adapted attenuation formulation, which leads to closed-form expressions for both the normal and occupancy fields at arbitrary locations in space. We further introduce a novel consistency loss and a dedicated densification strategy to enforce Gaussians to wrap the entire surface by closing geometric holes, ensuring a complete shell of oriented primitives. We modify the differentiable rasterizer to output depth as an isosurface of our continuous model, and introduce Primal Adaptive Meshing for Region-of-Interest meshing at arbitrary resolution. We additionally expose fundamental biases in standard surface evaluation protocols and propose two more rigorous alternatives. Overall, our method Gaussian Wrapping sets a new state-of-the-art on DTU and Tanks and Temples, producing complete, watertight meshes at a fraction of the size of concurrent work-recovering thin structures such as the notoriously elusive bicycle spokes.

  </details>


- **[Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D Gaussian Splatting under Constrained GPU Budgets](https://arxiv.org/abs/2604.07177)**  
  *Muhammad Fahim Tajwar, Arthur Wuhrlin, Bhojan Anand*  
  `2026-04-08` · `cs.GR` · [abs](https://arxiv.org/abs/2604.07177) · [pdf](https://arxiv.org/pdf/2604.07177.pdf)
  > 💡 通过模拟不同GPU能力层级，探究实时3DGS在受限预算下的性能与能耗权衡，评估边缘部署可行性。

  <details><summary>Abstract</summary>

  We investigate the feasibility of real-time 3D Gaussian Splatting (3DGS) rasterisation on edge clients with varying Gaussian splat counts and GPU computational budgets. Instead of evaluating multiple physical devices, we adopt an emulation-based approach that approximates different GPU capability tiers on a single high-end GPU. By systematically under-clocking the GPU core frequency and applying power caps, we emulate a controlled range of floating-point performance levels that approximate different GPU capability tiers. At each point in this range, we measure frame rate, runtime behaviour, and power consumption across scenes of varying complexity, pipelines, and optimisations, enabling analysis of power-performance relationships such as FPS-power curves, energy per frame, and performance per watt. This method allows us to approximate the performance envelope of a diverse class of GPUs, from embedded and mobile-class devices to high-end consumer-grade systems. Our objective is to explore the practical lower bounds of client-side 3DGS rasterisation and assess its potential for deployment in energy-constrained environments, including standalone headsets and thin clients. Through this analysis, we provide early insights into the performance-energy trade-offs that govern the viability of edge-deployed 3DGS systems.

  </details>


- **[GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending](https://arxiv.org/abs/2604.02120)**  
  *Haomin Li, Bowen Zhu, Fangxin Liu, Zongwu Wang, Xinran Liang, Li Jiang, Haibing Guan*  
  `2026-04-02` · `cs.AR` · [abs](https://arxiv.org/abs/2604.02120) · [pdf](https://arxiv.org/pdf/2604.02120.pdf)
  > 💡 针对3DGS渲染慢且缺乏GEMM操作，提出GEMM-GS将混合过程转为GEMM兼容形式以利用张量核，实现1.

  <details><summary>Abstract</summary>

  Neural Radiance Fields (NeRF) enables 3D scene reconstruction from several 2D images but incurs high rendering latency via its point-sampling design. 3D Gaussian Splatting (3DGS) improves on NeRF with explicit scene representation and an optimized pipeline yet still fails to meet practical real-time demands. Existing acceleration works overlook the evolving Tensor Cores of modern GPUs because 3DGS pipeline lacks General Matrix Multiplication (GEMM) operations. This paper proposes GEMM-GS, an acceleration approach utilizing tensor cores on GPUs via GEMM-friendly blending transformation. It equivalently reformulates the 3DGS blending process into a GEMM-compatible form to utilize Tensor Cores. A high-performance CUDA kernel is designed, integrating a three-stage double-buffered pipeline that overlaps computation and memory access. Extensive experiments show that GEMM-GS achieves $1.42\times$ speedup over vanilla 3DGS and provides an additional $1.47\times$ speedup on average when combining with existing acceleration approaches. Code is released at https://github.com/shieldforever/GEMM-GS.

  </details>


- **[LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2604.01388)**  
  *Fusang Wang, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Fabien Moutarde*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01388) · [pdf](https://arxiv.org/pdf/2604.01388.pdf)
  > 💡 针对3DGS开集场景理解的空间和语义模糊，提出稀疏体素光栅化SVRaster与AM-RADIO对齐，实现确定性特征注册并抑制渗漏，性能SOTA。

  <details><summary>Abstract</summary>

  Recent advancements in open-vocabulary 3D scene understanding heavily rely on 3D Gaussian Splatting (3DGS) to register vision-language features into 3D space. However, we identify two critical limitations in these approaches: the spatial ambiguity arising from unstructured, overlapping Gaussians which necessitates probabilistic feature registration, and the multi-level semantic ambiguity caused by pooling features over object-level masks, which dilutes fine-grained details. To address these challenges, we present a novel framework that leverages Sparse Voxel Rasterization (SVRaster) as a structured, disjoint geometry representation. By regularizing SVRaster with monocular depth and normal priors, we establish a stable geometric foundation. This enables a deterministic, confidence-aware feature registration process and suppresses the semantic bleeding artifact common in 3DGS. Furthermore, we resolve multi-level ambiguity by exploiting the emerging dense alignment properties of foundation model AM-RADIO, avoiding the computational overhead of hierarchical training methods. Our approach achieves state-of-the-art performance on Open Vocabulary 3D Object Retrieval and Point Cloud Understanding benchmarks, particularly excelling on fine-grained queries where registration methods typically fail.

  </details>


- **[DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](https://arxiv.org/abs/2604.00648)**  
  *Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.00648) · [pdf](https://arxiv.org/pdf/2604.00648.pdf)
  > 💡 鱼眼畸变导致3DGS预处理损失信息与产生漂浮物，提出原生鱼眼模型集成与跨视图联合优化，提升重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has enabled efficient 3D scene reconstruction from everyday images with real-time, high-fidelity rendering, greatly advancing VR/AR applications. Fisheye cameras, with their wider field of view (FOV), promise high-quality reconstructions from fewer inputs and have recently attracted much attention. However, since 3DGS relies on rasterization, most subsequent works involving fisheye camera inputs first undistort images before training, which introduces two problems: 1) Black borders at image edges cause information loss and negate the fisheye's large FOV advantage; 2) Undistortion's stretch-and-interpolate resampling spreads each pixel's value over a larger area, diluting detail density -- causes 3DGS overfitting these low-frequency zones, producing blur and floating artifacts. In this work, we integrate fisheye camera model into the original 3DGS framework, enabling native fisheye image input for training without preprocessing. Despite correct modeling, we observed that the reconstructed scenes still exhibit floaters at image edges: Distortion increases toward the periphery, and 3DGS's original per-iteration random-selecting-view optimization ignores the cross-view correlations of a Gaussian, leading to extreme shapes (e.g., oversized or elongated) that degrade reconstruction quality. To address this, we introduce a feature-overlap-driven cross-view joint optimization strategy that establishes consistent geometric and photometric constraints across views-a technique equally applicable to existing pinhole-camera-based pipelines. Our DirectFisheye-GS matches or surpasses state-of-the-art performance on public datasets. Project Page: https://yzxqh.github.io/DirectFisheye-GS/ .

  </details>


- **[TreeGaussian: Tree-Guided Cascaded Contrastive Learning for Hierarchical Consistent 3D Gaussian Scene Segmentation and Understanding](https://arxiv.org/abs/2604.03309)**  
  *Jingbin You, Zehao Li, Hao Jiang, Xinzhu Ma, Shuqin Gao, Honglong Zhao, Congcong Zheng, Tianlu Mao, Feng Dai, Yucheng Zhang, Zhaoqi Wang*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03309) · [pdf](https://arxiv.org/pdf/2604.03309.pdf)
  > 💡 针对3DGS难以建模层次化语义和整体-部分关系的问题，TreeGaussian用树引导级联对比学习框架实现一致分割和理解。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a real-time, differentiable representation for neural scene understanding. However, existing 3DGS-based methods struggle to represent hierarchical 3D semantic structures and capture whole-part relationships in complex scenes. Moreover, dense pairwise comparisons and inconsistent hierarchical labels from 2D priors hinder feature learning, resulting in suboptimal segmentation. To address these limitations, we introduce TreeGaussian, a tree-guided cascaded contrastive learning framework that explicitly models hierarchical semantic relationships and reduces redundancy in contrastive supervision. By constructing a multi-level object tree, TreeGaussian enables structured learning across object-part hierarchies. In addition, we propose a two-stage cascaded contrastive learning strategy that progressively refines feature representations from global to local, mitigating saturation and stabilizing training. A Consistent Segmentation Detection (CSD) mechanism and a graph-based denoising module are further introduced to align segmentation modes across views while suppressing unstable Gaussian points, enhancing segmentation consistency and quality. Extensive experiments, including open-vocabulary 3D object selection, 3D point cloud understanding, and ablation studies, demonstrate the effectiveness and robustness of our approach.

  </details>


- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725)**  
  *Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger*  
  `2026-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2603.24725) · [pdf](https://arxiv.org/pdf/2603.24725.pdf)
  > 💡 针对视图依赖场景下网格提取困难，提出自监督置信度框架动态平衡光度与几何监督，并引入颜色法线方差损失，实现高效SOTA网格提取。

  <details><summary>Abstract</summary>

  Recently, 3D Gaussian Splatting (3DGS) greatly accelerated mesh extraction from posed images due to its explicit representation and fast software rasterization. While the addition of geometric losses and other priors has improved the accuracy of extracted surfaces, mesh extraction remains difficult in scenes with abundant view-dependent effects. To resolve the resulting ambiguities, prior works rely on multi-view techniques, iterative mesh extraction, or large pre-trained models, sacrificing the inherent efficiency of 3DGS. In this work, we present a simple and efficient alternative by introducing a self-supervised confidence framework to 3DGS: within this framework, learnable confidence values dynamically balance photometric and geometric supervision. Extending our confidence-driven formulation, we introduce losses which penalize per-primitive color and normal variance and demonstrate their benefits to surface extraction. Finally, we complement the above with an improved appearance model, by decoupling the individual terms of the D-SSIM loss. Our final approach delivers state-of-the-art results for unbounded meshes while remaining highly efficient.

  </details>


- **[Accurate Point Measurement in 3DGS -- A New Alternative to Traditional Stereoscopic-View Based Measurements](https://arxiv.org/abs/2603.24716)**  
  *Deyan Deng, Rongjun Qin*  
  `2026-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2603.24716) · [pdf](https://arxiv.org/pdf/2603.24716.pdf)
  > 💡 针对3DGS几何测量未被充分利用，提出利用跨视图选点三角化，实现无需立体工作站的精确测量，精度匹敌传统方法。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized real-time rendering with its state-of-the-art novel view synthesis, but its utility for accurate geometric measurement remains underutilized. Compared to multi-view stereo (MVS) point clouds or meshes, 3DGS rendered views present superior visual quality and completeness. However, current point measurement methods still rely on demanding stereoscopic workstations or direct picking on often-incomplete and inaccurate 3D meshes. As a novel view synthesizer, 3DGS renders exact source views and smoothly interpolates in-between views. This allows users to intuitively pick congruent points across different views while operating 3DGS models. By triangulating these congruent points, one can precisely generate 3D point measurements. This approach mimics traditional stereoscopic measurement but is significantly less demanding: it requires neither a stereo workstation nor specialized operator stereoscopic capability. Furthermore, it enables multi-view intersection (more than two views) for higher measurement accuracy. We implemented a web-based application to demonstrate this proof-of-concept (PoC). Using several UAV aerial datasets, we show this PoC allows users to successfully perform highly accurate point measurements, achieving accuracy matching or exceeding traditional stereoscopic methods on standard hardware. Specifically, our approach significantly outperforms direct mesh-based measurements. Quantitatively, our method achieves RMSEs in the 1-2 cm range on well-defined points. More critically, on challenging thin structures where mesh-based RMSE was 0.062 m, our method achieved 0.037 m. On sharp corners poorly reconstructed in the mesh, our method successfully measured all points with a 0.013 m RMSE, whereas the mesh method failed entirely. Code is available at: https://github.com/GDAOSU/3dgs_measurement_tool.

  </details>


- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637)**  
  *Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao*  
  `2026-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2603.23637) · [pdf](https://arxiv.org/pdf/2603.23637.pdf)
  > 💡 针对3DGS射线追踪排序慢和近似阴影问题，提出无排序随机射线追踪，用蒙特卡洛梯度估计实现高效高质量标准与可重光照重建。

  <details><summary>Abstract</summary>

  Ray-tracing-based 3D Gaussian splatting (3DGS) methods overcome the limitations of rasterization -- rigid pinhole camera assumptions, inaccurate shadows, and lack of native reflection or refraction -- but remain slower due to the cost of sorting all intersecting Gaussians along every ray. Moreover, existing ray-tracing methods still rely on rasterization-style approximations such as shadow mapping for relightable scenes, undermining the generality that ray tracing promises. We present a differentiable, sorting-free stochastic formulation for ray-traced 3DGS -- the first framework that uses stochastic ray tracing to both reconstruct and render standard and relightable 3DGS scenes. At its core is an unbiased Monte Carlo estimator for pixel-color gradients that evaluates only a small sampled subset of Gaussians per ray, bypassing the need for sorting. For standard 3DGS, our method matches the reconstruction quality and speed of rasterization-based 3DGS while substantially outperforming sorting-based ray tracing. For relightable 3DGS, the same stochastic estimator drives per-Gaussian shading with fully ray-traced shadow rays, delivering notably higher reconstruction fidelity than prior work.

  </details>


- **[GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192)**  
  *Yan Fang, Jianfei Ge, Jiangjian Xiao*  
  `2026-03-24` · `cs.GR` · [abs](https://arxiv.org/abs/2603.23192) · [pdf](https://arxiv.org/pdf/2603.23192.pdf)
  > 💡 针对传统3DGS尺度模糊和几何一致性差，提出LiDAR度量感知分配与曲率自适应细化，实现高保真几何重建。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled real-time, photorealistic scene reconstruction. However, conventional 3DGS frameworks typically rely on sparse point clouds derived from Structure-from-Motion (SfM), which inherently suffer from scale ambiguity, limited geometric consistency, and strong view dependency due to the lack of geometric priors. In this work, a LiDAR-centric 3D Gaussian Splatting framework is proposed that explicitly incorporates metric geometric priors into the entire Gaussian optimization process. Instead of treating LiDAR data as a passive initialization source, 3DGS optimization is reformulated as a geometry-conditioned allocation and refinement problem under a fixed representational budget. Specifically, this work introduces (i) a geometry-texture-aware allocation strategy that selectively assigns Gaussian primitives to regions with high structural or appearance complexity, (ii) a curvature-adaptive refinement mechanism that dynamically guides Gaussian splitting toward geometrically complex areas during training, and (iii) a confidence-aware metric depth regularization that anchors the reconstructed geometry to absolute scale using LiDAR measurements while maintaining optimization stability. Extensive experiments on the ScanNet++ dataset and a custom real-world dataset validate the proposed approach. The results demonstrate state-of-the-art performance in metric-scale reconstruction with high geometric fidelity.

  </details>


</details>

<details><summary><b>SLAM / Localization / Mapping</b> (8) · <a href="topics/slam.md">full list →</a></summary>

- **[PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting](https://arxiv.org/abs/2605.08035)**  
  *William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp*  
  `2026-05-08` · `eess.SP` · [abs](https://arxiv.org/abs/2605.08035) · [pdf](https://arxiv.org/pdf/2605.08035.pdf)
  > 💡 提出PropSplat，用3D高斯原语无地图重建射频场，稀疏测量下精度优于现有方法。

  <details><summary>Abstract</summary>

  Building a site-specific propagation model typically requires either ray-tracing over detailed 3D maps or dense measurement campaigns. Both approaches are expensive and often infeasible for rapid deployments where geographic data is unavailable or outdated. We present PropSplat, a map-free propagation modeling method that reconstructs radio frequency (RF) fields using 3D anisotropic Gaussian primitives. Each Gaussian encodes a scalar path loss offset relative to an explicit baseline path loss model with a learnable path loss exponent. Gaussians are initialized along observed transmitter--receiver paths and optimized end-to-end to learn the propagation environment without external information like floor plans, terrain databases, or clutter data. We evaluate PropSplat against wireless radiance field methods NeRF$^2$, GSRF, and WRF-GS+ on two real-world datasets. On large-scale outdoor drive-tests spanning multiple topographical regions at six sub-6 GHz frequencies, PropSplat achieves 5.38 dB RMSE when training measurements are spaced 300m apart and outperforms WRF-GS+ (5.87 dB), GSRF (7.46 dB), and NeRF$^2$ (14.76 dB). On indoor Bluetooth Low Energy measurements, PropSplat achieves 0.19m mean localization error, an order of magnitude better than NeRF$^2$ (1.84m), while achieving near-identical received signal strength prediction accuracy. These results show that accurate site-specific propagation reconstruction is achievable from sparse RF-native measurements. The need for geographic data as a prerequisite for scalable RF environment modeling is reduced.

  </details>


- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730)**  
  *Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04730) · [pdf](https://arxiv.org/pdf/2605.04730.pdf)
  > 💡 针对3DGS中α混合导致的特征偏差，提出几何加权融合与地标采样，降低17%平移误差且训练时间仅1/10。

  <details><summary>Abstract</summary>

  Visual localization is a core technology for augmented reality and autonomous navigation. Recent methods combine the efficient rendering of 3D Gaussian Splatting (3DGS) with feature-based localization. These methods rely on direct matching between 2D query features and the 3D Gaussian feature field, but this often results in mismatches due to an inherent bias in the learned Gaussian feature. We theoretically analyze the feature learning process in 3DGS, revealing that the widely adopted $α$-blending optimization inherently introduces bias into 3D point features. This bias stems from the entanglement between individual Gaussians and their neighboring Gaussians, making the learned features unsuitable for precise matching tasks. Motivated by these findings, we propose ULF-Loc, an unbiased landmark feature framework that replaces biased feature optimization with geometry-weighted feature fusion. We further introduce keypoint-consensus landmark sampling to select reliable Gaussians and local geometric consistency verification to reject mismatches caused by rendering artifacts. On the Cambridge Landmarks dataset, ULF-Loc reduces the mean median translation error by 17\% compared to the state-of-the-art, while achieving superior efficiency with only 1/10 the training time and 1/6 the GPU memory of STDLoc.

  </details>


- **[PoInit-of-View: Poisoning Initialization of Views Transfers Across Multiple 3D Reconstruction Systems](https://arxiv.org/abs/2604.16540)**  
  *Weijie Wang, Songlong Xing, Zhengyu Zhao, Nicu Sebe, Bruno Lepri*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16540) · [pdf](https://arxiv.org/pdf/2604.16540.pdf)
  > 💡 针对SfM初始化模块制造跨视图梯度不一致，破坏关键点匹配与位姿估计，实现跨3D重建系统的高迁移性投毒攻击。

  <details><summary>Abstract</summary>

  Poisoning input views of 3D reconstruction systems has been recently studied. However, we identify that existing studies simply backpropagate adversarial gradients through the 3D reconstruction pipeline as a whole, without uncovering the new vulnerability rooted in specific modules of the 3D reconstruction pipeline. In this paper, we argue that the structure-from-motion (SfM) initialization, as the geometric core of many widely used reconstruction systems, can be targeted to achieve transferable poisoning effects across diverse 3D reconstruction systems. To this end, we propose PoInit-of-View, which optimizes adversarial perturbations to intentionally introduce cross-view gradient inconsistencies at projections of corresponding 3D points. These inconsistencies disrupt keypoint detection and feature matching, thereby corrupting pose estimation and triangulation within SfM, eventually resulting in low-quality rendered views. We also provide a theoretical analysis that connects cross-view inconsistency to correspondence collapse. Experimental results demonstrate the effectiveness of our PoInit-of-View on diverse 3D reconstruction systems and datasets, surpassing the single-view baseline by 25.1% in PSNR and 16.5% in SSIM in black-box transfer settings, such as 3DGS to NeRF.

  </details>


- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492)**  
  *Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko*  
  `2026-04-15` · `cs.RO` · [abs](https://arxiv.org/abs/2604.13492) · [pdf](https://arxiv.org/pdf/2604.13492.pdf)
  > 💡 针对雷达SLAM漂移问题，提出首个高斯溅射雷达束调整方法，联合优化位姿与场景几何，误差降低90%和80%。

  <details><summary>Abstract</summary>

  Radar is more resilient to adverse weather and lighting conditions than visual and Lidar simultaneous localization and mapping (SLAM). However, most radar SLAM pipelines still rely heavily on frame-to-frame odometry, which leads to substantial drift. While loop closure can correct long-term errors, it requires revisiting places and relies on robust place recognition. In contrast, visual odometry methods typically leverage bundle adjustment (BA) to jointly optimize poses and map within a local window. However, an equivalent BA formulation for radar has remained largely unexplored. We present the first radar BA framework enabled by Gaussian Splatting (GS), a dense and differentiable scene representation. Our method jointly optimizes radar sensor poses and scene geometry using full range-azimuth-Doppler data, bringing the benefits of multi-frame BA to radar for the first time. When integrated with an existing radar-inertial odometry frontend, our approach significantly reduces pose drift and improves robustness. Across multiple indoor scenes, our radar BA achieves substantial gains over the prior radar-inertial odometry, reducing average absolute translational and rotational errors by 90% and 80%, respectively.

  </details>


- **[LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios](https://arxiv.org/abs/2604.05402)**  
  *Xiang Zhang, Tengfei Wang, Fang Xu, Xin Wang, Zongqian Zhan*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05402) · [pdf](https://arxiv.org/pdf/2604.05402.pdf)
  > 💡 应对大规模无人机场景下3DGS定位的位姿初始化难和渲染伪影问题，提出尺度感知初始化和拉普拉斯可靠性掩码，显著提升精度与鲁棒性。

  <details><summary>Abstract</summary>

  Visual localization in large-scale UAV scenarios is a critical capability for autonomous systems, yet it remains challenging due to geometric complexity and environmental variations. While 3D Gaussian Splatting (3DGS) has emerged as a promising scene representation, existing 3DGS-based visual localization methods struggle with robust pose initialization and sensitivity to rendering artifacts in large-scale settings. To address these limitations, we propose LSGS-Loc, a novel visual localization pipeline tailored for large-scale 3DGS scenes. Specifically, we introduce a scale-aware pose initialization strategy that combines scene-agnostic relative pose estimation with explicit 3DGS scale constraints, enabling geometrically grounded localization without scene-specific training. Furthermore, in the pose refinement, to mitigate the impact of reconstruction artifacts such as blur and floaters, we develop a Laplacian-based reliability masking mechanism that guides photometric refinement toward high-quality regions. Extensive experiments on large-scale UAV benchmarks demonstrate that our method achieves state-of-the-art accuracy and robustness for unordered image queries, significantly outperforming existing 3DGS-based approaches. Code is available at: https://github.com/xzhang-z/LSGS-Loc

  </details>


- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192)**  
  *Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou*  
  `2026-03-31` · `cs.RO` · [abs](https://arxiv.org/abs/2603.29192) · [pdf](https://arxiv.org/pdf/2603.29192.pdf)
  > 💡 针对机器人策略新视角泛化差的问题，提出GenSplat，利用前馈3DGS和3D先验蒸馏生成合成视图增强训练，提升鲁棒性。

  <details><summary>Abstract</summary>

  Prevailing 2D-centric visuomotor policies exhibit a pronounced deficiency in novel view generalization, as their reliance on static observations hinders consistent action mapping across unseen views. In response, we introduce GenSplat, a feed-forward 3D Gaussian Splatting framework that facilitates view-generalized policy learning through novel view rendering. GenSplat employs a permutation-equivariant architecture to reconstruct high-fidelity 3D scenes from sparse, uncalibrated inputs in a single forward pass. To ensure structural integrity, we design a 3D-prior distillation strategy that regularizes the 3DGS optimization, preventing the geometric collapse typical of purely photometric supervision. By rendering diverse synthetic views from these stable 3D representations, we systematically augment the observational manifold during training. This augmentation forces the policy to ground its decisions in underlying 3D structures, thereby ensuring robust execution under severe spatial perturbations where baselines severely degrade.

  </details>


- **[Unblur-SLAM: Dense Neural SLAM for Blurry Inputs](https://arxiv.org/abs/2603.26810)**  
  *Qi Zhang, Denis Rozumny, Francesco Girlanda, Sezer Karaoglu, Marc Pollefeys, Theo Gevers, Martin R. Oswald*  
  `2026-03-26` · `cs.CV` · [abs](https://arxiv.org/abs/2603.26810) · [pdf](https://arxiv.org/pdf/2603.26810.pdf)
  > 💡 使用前馈去模糊与3DGS模糊建模，从模糊输入实现锐利SLAM重建，姿态与几何纹理

  <details><summary>Abstract</summary>

  We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in the input image. As a first stage, our method uses a feed-forward image deblurring model for which we propose a suitable training scheme that can improve both tracking and mapping modules. Frames that are successfully deblurred by the feed-forward network obtain refined poses and depth through local-global multi-view optimization and loop closure. Frames that fail the first stage deblurring are directly modeled through the global 3DGS representation and an additional blur network to model multiple blurred sub-frames and simulate the blur formation process in 3D space, thereby learning sharp details and refined sub-frame poses. Experiments on several real-world datasets demonstrate consistent improvements in both pose estimation and sharp reconstruction results of geometry and texture.

  </details>


- **[Pose-Free Omnidirectional Gaussian Splatting for 360-Degree Videos with Consistent Depth Priors](https://arxiv.org/abs/2603.23324)**  
  *Chuanqing Zhuang, Xin Lu, Zehui Deng, Zhengda Lu, Yiqun Wang, Junqi Diao, Jun Xiao*  
  `2026-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2603.23324) · [pdf](https://arxiv.org/pdf/2603.23324.pdf)
  > 💡 针对无姿态360度视频，提出PFGS360，用球面一致性姿态估计和深度内点感知密集化模块，实现高效重建及逼真新视角合成。

  <details><summary>Abstract</summary>

  Omnidirectional 3D Gaussian Splatting with panoramas is a key technique for 3D scene representation, and existing methods typically rely on slow SfM to provide camera poses and sparse points priors. In this work, we propose a pose-free omnidirectional 3DGS method, named PFGS360, that reconstructs 3D Gaussians from unposed omnidirectional videos. To achieve accurate camera pose estimation, we first construct a spherical consistency-aware pose estimation module, which recovers poses by establishing consistent 2D-3D correspondences between the reconstructed Gaussians and the unposed images using Gaussians' internal depth priors. Besides, to enhance the fidelity of novel view synthesis, we introduce a depth-inlier-aware densification module to extract depth inliers and Gaussian outliers with consistent monocular depth priors, enabling efficient Gaussian densification and achieving photorealistic novel view synthesis. The experiments show significant outperformance over existing pose-free and pose-aware 3DGS methods on both real-world and synthetic 360-degree videos. Code is available at https://github.com/zcq15/PFGS360.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (11) · <a href="topics/driving.md">full list →</a></summary>

- **[Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328)**  
  *Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30328) · [pdf](https://arxiv.org/pdf/2605.30328.pdf)
  > 💡 结合深度估计的单模态热红外高斯泼溅方法，显著提升渲染质量并将训练时间缩减55%。

  <details><summary>Abstract</summary>

  Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like thermal or depth can enable additional information on the environment. Lately, novel view synthesis methods like 3D Gaussian Splatting have started using multiple modalities to further boost their performance. But fusing or combining multimodal data can make the process slower and can bring in additional challenges. Therefore, our project aims to use single modality based on thermal infrared domain, by removing the reliance on visible light as much as possible. This single modality can be expected to be faster as it does not rely on multimodal data. We propose a method, Thermal-to-Depth Gaussian Splatting (TDg), that uses only thermal images and depth estimation in its architecture to derive the radiance fields. Our TDg method outperforms the MSMG (Multiple Single-Modal Gaussians) baseline in most cases on our test datasets, RGBT-Scenes and ThermalMix. On average, the rendering quality metrics such as learned perceptual image patch similarity (LPIPS), structural similarity index measure (SSIM), and peak signal-to-noise ratio (PSNR) of TDg are 1.12%, 0.034%, and 0.01% better than the baseline MSMG values. It also reduces the training time significantly, by 12 mins 47 secs (55% improvement). Overall, our method is successful in deriving these thermal radiance fields, which can ultimately have several applications, such as identifying heat sources critical in surveillance, search or rescue operations, and industrial inspections where temperature is widely used to monitor machines.

  </details>


- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310)**  
  *Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30310) · [pdf](https://arxiv.org/pdf/2605.30310.pdf)
  > 💡 针对城市尺度多视图图像重建仿真就绪3D网格

  <details><summary>Abstract</summary>

  City-scale 3D surface reconstruction from multiview images for downstream 3D simulation, poses highly challenging problems due to the scale and complexity of urban scenes. Existing city-scale 3D reconstruction methods based on NeRF, Gaussian Splatting etc. often fail to recover 3D meshes ready for simulation due to incomplete/missing geometry and irregular, noisy surfaces. Scaling existing small-scale 3D reconstruction methods to arbitrarily large urban scenes is highly infeasible due to their computational complexity. We present City-Mesh3R, a scalable framework for reconstructing watertight surface meshes directly from large unordered image collections. Unlike recent methods which use global sparse SfM point-cloud initialization followed by a distributed 3D dense reconstruction of large-scale scenes, our method follows an end-to-end images-to-mesh 3D reconstruction approach using a divide-and-conquer strategy. The sparse city map is reconstructed via topological image clustering, cluster-wise independent sparse SfM and map merging, without need for exhaustive image feature matching. Then this map is partitioned spatially to perform geometry-aware camera selection, followed by dense surface reconstruction and surface refinement using curvature-aware adaptive vertex density remeshing. These partition meshes are then stitched together to produce the global mesh of the city. The proposed end-to-end framework is evaluated on city-scale reconstruction datasets. As demonstrated by our qualitative and quantitative results, our proposed method yields high-fidelity watertight 3D meshes with regular geometry, capturing fine surface details, and is suitable for scaling to arbitrarily large scenes owing to the end-to-end processing in a distributed setting.

  </details>


- **[3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](https://arxiv.org/abs/2605.26500)**  
  *Jianzhe Gao, Rui Liu, Wenguan Wang*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26500) · [pdf](https://arxiv.org/pdf/2605.26500.pdf)
  > 💡 针对VLN场景理解不足，提出3D高斯地图与开放集语义分组及多级动作预测，提升导航泛化能力。

  <details><summary>Abstract</summary>

  Vision-language navigation (VLN) requires an agent to traverse complex 3D environments based on natural language instructions, necessitating a thorough scene understanding. While existing works equip agents with various scene representations to enhance spatial awareness, they often neglect the complex 3D geometry and rich semantics in VLN scenarios, limiting the ability to generalize across diverse and unseen environments. To address these challenges, this work proposes a 3D Gaussian Map that represents the environment as a set of differentiable 3D Gaussians and accordingly develops a navigation strategy for VLN. Specifically, Egocentric Scene Map is constructed online by initializing 3D Gaussians from sparse pseudo-lidar point clouds, providing informative geometric priors for scene understanding. Each Gaussian primitive is further enriched through Open-Set Semantic Grouping operation, which groups 3D Gaussians based on their membership in object instances or stuff categories within the open world, resulting in a unified 3D Gaussian Map. Building on this map, Multi-Level Action Prediction strategy, which combines spatial-semantic cues at multiple granularities, is designed to assist agents in decision-making. Extensive experiments conducted on three public benchmarks (i.e., R2R, R4R, and REVERIE) validate the effectiveness of our method.

  </details>


- **[PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11520)**  
  *Yixiao Song, Qingyong Li, Wen Wang, Zhicheng Yan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11520) · [pdf](https://arxiv.org/pdf/2605.11520.pdf)
  > 💡 用3D高斯溅射桥接离散点云与连续图像的域差距，结合SAM与对比学习实现无监督分割，性能达先进水平。

  <details><summary>Abstract</summary>

  Unsupervised point cloud segmentation is critical for embodied artificial intelligence and autonomous driving, as it mitigates the prohibitive cost of dense point-level annotations required by fully supervised methods. While integrating 2D pre-trained models such as the Segment Anything Model (SAM) to supplement semantic information is a natural choice, this approach faces a fundamental mismatch between discrete 3D points and continuous 2D images. This mismatch leads to inevitable projection overlap and complex modality alignment, resulting in compromised semantic consistency across 2D-3D transfer. To address these limitations, this paper proposes PointGS, a simple yet effective pipeline for unsupervised 3D point cloud segmentation. PointGS leverages 3D Gaussian Splatting as a unified intermediate representation to bridge the discrete-continuous domain gap. Input sparse point clouds are first reconstructed into dense 3D Gaussian spaces via multi-view observations, filling spatial gaps and encoding occlusion relationships to eliminate projection-induced semantic conflation. Multi-view dense images are rendered from the Gaussian space, with 2D semantic masks extracted via SAM, and semantics are distilled to 3D Gaussian primitives through contrastive learning to ensure consistent semantic assignments across different views. The Gaussian space is aligned with the original point cloud via two-step registration, and point semantics are assigned through nearest-neighbor search on labeled Gaussians. Experiments demonstrate that PointGS outperforms state-of-the-art unsupervised methods, achieving +0.9% mIoU on ScanNet-V2 and +2.8% mIoU on S3DIS.

  </details>


- **[UAV-Assisted Scan-to-Simulation for Landslides Using Physics-Informed Gaussian Splatting](https://arxiv.org/abs/2605.10715)**  
  *Zhenyu Liang, Jack C. P. Cheng*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10715) · [pdf](https://arxiv.org/pdf/2605.10715.pdf)
  > 💡 通过无人机倾斜摄影与3DGS重建结合MPM，实现滑坡场景的逼真视觉重建与物理模拟。

  <details><summary>Abstract</summary>

  Landslide monitoring and simulation play an important role in urban safety assessment and disaster prevention. Existing landslide simulation pipelines typically rely on digital elevation model and mesh-based representations, which are suitable for geometric analysis, but often lack visual realism. This limitation reduces their effectiveness in interactive applications, hazard communication, and public education. In this paper, we propose a UAV-based scan-to-simulation framework that bridges photorealistic scene capture and physics-based landslide simulation through 3DGS. Specifically, our pipeline includes four stages: (1) UAV-based acquisition of slope imagery, (2) reconstruction of a low-anisotropy 3DGS scene representation, (3) volumetric conversion of the target simulation region by filling the interior of the surface-based model, and (4) integration with the Material Point Method (MPM) for landslide simulation. We validate the proposed framework on a real landslide site in Hong Kong that experienced a severe landslide event. The results show that our method supports both realistic visual reconstruction and effective simulation.

  </details>


- **[GSDrive: Reinforcing Driving Policies by Multi-mode Future Trajectory Probing with 3D Gaussian Splatting Environment](https://arxiv.org/abs/2604.28111)**  
  *Ziang Guo, Chen Min, Xuefeng Zhang, Yixiao Zhou, Shuo Wang, Sifa Zheng, Dzmitry Tsetserukou, Zufeng Zhang*  
  `2026-04-30` · `cs.RO` · [abs](https://arxiv.org/abs/2604.28111) · [pdf](https://arxiv.org/pdf/2604.28111.pdf)
  > 💡 端到端自动驾驶中强化学习奖励稀疏，采用3DGS环境进行多模态未来轨迹探测与奖励塑形，结合IL-RL循环提升策略性能。

  <details><summary>Abstract</summary>

  End-to-end (E2E) autonomous driving aims to directly map sensory observations to driving actions, but its real-world deployment is hindered by evolving data distributions and the high cost of continual annotation. While combining imitation learning (IL) and reinforcement learning (RL) is a common strategy for policy improvement, conventional RL training relies on delayed, event-based rewards, where policies learn only from catastrophic outcomes such as collisions, leading to premature convergence to suboptimal behaviors. To address these limitations, we propose GSDrive, a framework that uses a differentiable 3D Gaussian Splatting (3DGS) environment for future-aware trajectory probing and reward shaping in E2E driving. GSDrive first learns a multi-mode trajectory probe via IL and then uses RL to evaluate multiple candidate futures in the 3DGS environment, converting their simulated returns into dense shaping rewards for policy optimization. This yields a cyclic hybrid IL-RL training loop, where IL supplies structured future priors and RL provides interactive feedback for iterative refinement. Evaluated on the reconstructed nuScenes dataset, our method outperforms other simulation-based RL approaches in closed-loop experiments. Code is available at https://github.com/ZionGo6/GSDrive.

  </details>


- **[Two-View Accumulation as the Primary Training Lever for Hybrid-Capture Gaussian Splatting: A Variance-Decomposition View of When Gradient Surgery Helps](https://arxiv.org/abs/2605.00052)**  
  *Sungjun Cho*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00052) · [pdf](https://arxiv.org/pdf/2605.00052.pdf)
  > 💡 混合捕捉3DGS中，每步两视图累积训练即可显著提升性能，配对方式无关，方差分解揭示其主导效应。

  <details><summary>Abstract</summary>

  Hybrid-capture novel view synthesis combines images at substantially different camera distances (e.g., aerial drone and ground-level views). Standard 3D Gaussian Splatting (3DGS), trained for 30K iterations with one rendered view per optimizer step, under-fits the minority regime by 1-3 dB on five hybrid-capture benchmarks. We isolate the lever that closes this gap. Among compute-matched alternatives -- vanilla 60K iterations, magnitude corrections (GradNorm), direction-aware near/far gradient surgery, projective preconditioning, confidence-gated sample-level surgery, and a random two-view-per-step control -- the simplest structural change wins: rendering two views per optimizer step. The pairing rule (geometry-defined near/far, random, or active loss-disparity) does not change PSNR beyond seed variance on any of the five scenes; the structural change of having two views per step does. We propose a variance-decomposition framework that predicts and explains this finding: under bimodal camera regimes, between-regime gradient variance turns out to be small relative to within-regime variance in 3DGS, so structured and random pairings are variance-equivalent in expectation, and the variance halving from two-view accumulation itself is the dominant effect. We verify the framework on five scenes whose camera-altitude bimodality coefficients span [0.55, 1.00], and we report the negative result that direction-aware projection, magnitude correction, confidence gating, and an active loss-disparity pairing all fall within seed variance of random two-view pairing. The two-view structural lever transfers cleanly to the Scaffold-GS and Pixel-GS backbones. We position this work as an honest characterization of which training-side axes do and do not move PSNR for hybrid-capture 3DGS, together with the framework that explains why.

  </details>


- **[EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors](https://arxiv.org/abs/2604.26238)**  
  *Rui Song, Tianhui Cai, Markus Gross, Yun Zhang, Walter Zimmer, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26238) · [pdf](https://arxiv.org/pdf/2604.26238.pdf)
  > 💡 将部分几何先验建模为连续能量场提供软引导，既提升光度质量又增强几何稳定性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and non-convex optimization problem. Recent works commonly incorporate geometric priors, such as LiDAR measurements, either for initialization or as training constraints, with the goal of improving photometric reconstruction quality. However, in large-scale outdoor scenarios, such geometric supervision is often spatially incomplete and uneven, which limits its effectiveness as a reliable prior and can even be detrimental to the final reconstruction. To address this challenge, we model partially observable geometry as a continuous energy field induced by geometric evidence and propose EnerGS. Rather than enforcing geometry as a hard constraint, EnerGS provides a soft geometric guidance for the optimization of Gaussian primitives, allowing geometric information to steer the optimization process without directly restricting the solution space. Extensive experiments on large-scale outdoor scenes demonstrate that, under both sparse multi-view and monocular settings, EnerGS consistently improves photometric quality and geometric stability, while effectively mitigating overfitting during 3DGS training.

  </details>


- **[AdaGScale: Viewpoint-Adaptive Gaussian Scaling in 3D Gaussian Splatting to Reduce Gaussian-Tile Pairs](https://arxiv.org/abs/2604.18980)**  
  *Joongho Jo, Hyerin Lim, Hanjun Choi, Jongsun Park*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18980) · [pdf](https://arxiv.org/pdf/2604.18980.pdf)
  > 💡 提出AdaGScale，通过估计高斯外围颜色贡献自适应缩放尺寸，减少高斯-瓦片对，实现13.8倍加速且仅降0.5dB PSNR。

  <details><summary>Abstract</summary>

  Reducing the number of Gaussian-tile pairs is one of the most promising approaches to improve 3D Gaussian Splatting (3D-GS) rendering speed on GPUs. However, the importance difference existing among Gaussian-tile pairs has never been considered in the previous works. In this paper, we propose AdaGScale, a novel viewpoint-adaptive Gaussian scaling technique for reducing the number of Gaussian-tile pairs. AdaGScale is based on the observation that the peripheral tiles located far from Gaussian center contribute negligibly to pixel color accumulation. This suggests an opportunity for reducing the number of Gaussian-tile pairs based on color contribution. AdaGScale efficiently estimates the color contribution in the peripheral region of each Gaussian during a preprocessing stage and adaptively scales its size based on the peripheral score. As a result, Gaussians with lower importance intersect with fewer tiles during the intersection test, which improves rendering speed while maintaining image quality. The adjusted size is used only for tile intersection test, and the original size is retained during color accumulation to preserve visual fidelity. Experimental results show that AdaGScale achieves a geometric mean speedup of 13.8x over original 3D-GS on a GPU, with only about 0.5 dB degradation in PSNR on city-scale scenes.

  </details>


- **[Efficient Transceiver Design for Aerial Image Transmission and Large-scale Scene Reconstruction](https://arxiv.org/abs/2604.11098)**  
  *Zeyi Ren, Jialin Dong, Wei Zuo, Yikun Wang, Bingyang Cheng, Sheng Zhou, Zhisheng Niu*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11098) · [pdf](https://arxiv.org/pdf/2604.11098.pdf)
  > 💡 针对低空大规模3D场景重建，提出融合3DGS渲染损失的端到端收发机，以稀疏导频降低开销并提升重建质量。

  <details><summary>Abstract</summary>

  Large-scale three-dimensional (3D) scene reconstruction in low-altitude intelligent networks (LAIN) demands highly efficient wireless image transmission. However, existing schemes struggle to balance severe pilot overhead with the transmission accuracy required to maintain reconstruction fidelity. To strike a balance between efficiency and reliability, this paper proposes a novel deep learning-based end-to-end (E2E) transceiver design that integrates 3D Gaussian Splatting (3DGS) directly into the training process. By jointly optimizing the communication modules via the combined 3DGS rendering loss, our approach explicitly improves scene recovery quality. Furthermore, this task-driven framework enables the use of a sparse pilot scheme, significantly reducing transmission overhead while maintaining robust image recovery under low-altitude channel conditions. Extensive experiments on real-world aerial image datasets demonstrate that the proposed E2E design significantly outperforms existing baselines, delivering superior transmission performance and accurate 3D scene reconstructions.

  </details>


- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605)**  
  *Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01605) · [pdf](https://arxiv.org/pdf/2604.01605.pdf)
  > 💡 针对分布式多智能体三维重建问题，提出联邦3DGS框架，固定几何只更新外观，可见性加权聚合，效果接近集中式训练。

  <details><summary>Abstract</summary>

  We present F3DGS, a federated 3D Gaussian Splatting framework for decentralized multi-agent 3D reconstruction. Existing 3DGS pipelines assume centralized access to all observations, which limits their applicability in distributed robotic settings where agents operate independently, and centralized data aggregation may be restricted. Directly extending centralized training to multi-agent systems introduces communication overhead and geometric inconsistency. F3DGS first constructs a shared geometric scaffold by registering locally merged LiDAR point clouds from multiple clients to initialize a global 3DGS model. During federated optimization, Gaussian positions are fixed to preserve geometric alignment, while each client updates only appearance-related attributes, including covariance, opacity, and spherical harmonic coefficients. The server aggregates these updates using visibility-aware aggregation, weighting each client's contribution by how frequently it observed each Gaussian, resolving the partial-observability challenge inherent to multi-agent exploration. To evaluate decentralized reconstruction, we collect a multi-sequence indoor dataset with synchronized LiDAR, RGB, and IMU measurements. Experiments show that F3DGS achieves reconstruction quality comparable to centralized training while enabling distributed optimization across agents. The dataset, development kit, and source code will be publicly released.

  </details>


</details>

<details><summary><b>Medical / Surgical</b> (2) · <a href="topics/medical.md">full list →</a></summary>

- **[Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction](https://arxiv.org/abs/2604.27552)**  
  *Jian Lin, Jiancheng Fang, Shaoyu Wang, Changan Lai, Yikun Zhang, Yang Chen, Qiegen Liu*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.27552) · [pdf](https://arxiv.org/pdf/2604.27552.pdf)
  > 💡 针对超稀疏视角CBCT中3DGS高频细节丢失问题，提出融合小波变换的

  <details><summary>Abstract</summary>

  While 3D Gaussian splatting (3DGS) offers explicit and efficient scene representations for cone-beam computed tomography reconstruction, conventional photometric optimization inherently suffers from spectral bias under ultra sparse-view conditions, leading to over-smoothing and a loss of high-frequency anatomical details. Since wavelet transforms provide rich high-frequency information and have been widely utilized to enhance sparse reconstruction, this work integrates wavelet multi-resolution analysis with 3DGS. To circumvent the mathematical mismatch between the strict non-negativity of physical X-ray attenuation and the bipolar nature of high-frequency wavelet coefficients, we propose Residual Gaussian Splatting (RGS). Methodologically, we introduce a spectrally-decoupled Gaussian representation that stratifies the volumetric field into a geometric base component and a residual detail component. This decomposition systematically transforms explicit high-frequency fitting into a physically consistent, implicit residual compensation task. Furthermore, we devise a spectral-spatial collaborative optimization strategy to coordinate the interplay between geometric anchoring and texture refinement, effectively preventing spectral crosstalk. Extensive experiments on clinical datasets demonstrate that RGS enables the reconstructed images to capture highly refined geometric textures. It successfully resolves the trade-off between artifact suppression and detail preservation, yielding superior visual fidelity in complex trabecular and vascular structures compared to existing neural rendering baselines.

  </details>


- **[Multivariate Gaussian NeRF for Wide Field-of-View Ultrasound Reconstruction](https://arxiv.org/abs/2604.24187)**  
  *Patris Valera, Magdalena Wysocki, Felix Duelmer, Mohammad Farid Azampour, Sebastian Herz, Stefan Wörz, Nassir Navab*  
  `2026-04-27` · `cs.CV` · [abs](https://arxiv.org/abs/2604.24187) · [pdf](https://arxiv.org/pdf/2604.24187.pdf)
  > 💡 针对凸探头超声宽视野重建的伪影和混叠，采用多元高斯NeRF建模光束几何与各向异性高斯，实现抗混叠连续神经表示及高质量新视角合成。

  <details><summary>Abstract</summary>

  Wide Field-of-View (WFoV) reconstruction enhances 3D ultrasound imaging by providing valuable anatomical context for segmentation models and visualization. Clinical ultrasound volumes are predominantly acquired using convex probes, which generate expanding, diverging acoustic beams to maximize anatomical coverage. Stitching these sweeps together traditionally introduces significant compounding artifacts and aliasing due to depth-dependent resolution changes. Here, we introduce Ultra-Wide-NeRF, a Multivariate 3D Gaussian (MVG) NeRF-based method for WFoV ultrasound reconstruction. By explicitly modeling the complex beam geometry using distance-dependent convex volumetric sampling and anisotropic 3D Gaussians, our method inherently mitigates these compounding artifacts and provides anti-aliasing. Beyond simply reconstructing a static 3D grid, our NeRF-based approach yields a continuous neural representation of the tissue, enabling the synthesis of high-fidelity novel views from arbitrary virtual trajectories. We validate Ultra-Wide-NeRF for intracardiac echocardiography on phantom and porcine datasets, demonstrating that our method expands the spatial context important in intraoperative navigation. Code will be open-sourced upon publication.

  </details>


</details>

<details><summary><b>Relighting / Material / BRDF</b> (2) · <a href="topics/relighting.md">full list →</a></summary>

- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975)**  
  *Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang*  
  `2026-05-25` · `cs.GR` · [abs](https://arxiv.org/abs/2605.25975) · [pdf](https://arxiv.org/pdf/2605.25975.pdf)
  > 💡 基于LRM和IDM，用潜插值几何合成与先验蒸馏，从稀疏视角高效生成可重照明的3D高斯资产。

  <details><summary>Abstract</summary>

  Capturing relightable 3D assets from real-world objects is a widely researched problem. Several per-scene optimization-based methods, based on 3D Gaussian splatting (3DGS), support relighting; however, they usually require dense input views, and their overfitting nature makes it difficult to generalize across scenes. Unlike per-scene optimization methods, generalized feed-forward models can directly reconstruct Gaussians from sparse input views. However, the resulting assets have baked-in illumination and cannot be easily used for relighting. In this paper, we present F-RNG, a feed-forward framework that directly generates relightable 3DGS assets from sparse-view inputs. Training such a model from scratch can require massive data and computing resources, and it is especially challenging to generate relightable assets in a feed-forward manner with acceptable cost. We develop F-RNG upon an existing large reconstruction model (LRM) to extract relightable representations, while also utilizing priors from an intrinsic decomposition model (IDM). Specifically, we first introduce a latent-interpolated fine-grained geometry synthesis to enhance the LRM's geometry representation. Second, we propose a prior-guided relightable appearance distillation to extract relightable neural representations by incorporating IDM priors. Finally, a universal neural renderer enables flexible and high-fidelity relighting. F-RNG requires neither re-training nor fine-tuning of the underlying LRMs, thus can automatically benefit from better LRMs and IDMs in the future. With only small networks that can be trained with affordable data and computational resources, F-RNG avoids the repetitive inference of large models under different light conditions. By comparison to the state-of-the-art LRM-based relighting method, F-RNG achieves ~25x faster relighting, as well as superior quality (~+2.0 dB).

  </details>


- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177)**  
  *Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen*  
  `2026-04-30` · `cs.GR` · [abs](https://arxiv.org/abs/2605.00177) · [pdf](https://arxiv.org/pdf/2605.00177.pdf)
  > 💡 集成物理燃烧模拟与3DGS，结合大模型推理材料，实现无需手动调参的真实可控火焰合成。

  <details><summary>Abstract</summary>

  We consider the problem of synthesizing photorealistic, physically plausible combustion effects in in-the-wild 3D scenes. Traditional CFD and graphics pipelines can produce realistic fire effects but rely on handcrafted geometry, expert-tuned parameters, and labor-intensive workflows, limiting their scalability to the real world. Recent scene modeling advances like 3D Gaussian Splatting (3DGS) enable high-fidelity real-world scene reconstruction, yet lack physical grounding for combustion. To bridge this gap, we propose FieryGS, a physically-based framework that integrates physically-accurate and user-controllable combustion simulation and rendering within the 3DGS pipeline, enabling realistic fire synthesis for real scenes. Our approach tightly couples three key modules: (1) multimodal large-language-model-based physical material reasoning, (2) efficient volumetric combustion simulation, and (3) a unified renderer for fire and 3DGS. By unifying reconstruction, physical reasoning, simulation, and rendering, FieryGS removes manual tuning and automatically generates realistic, controllable fire dynamics consistent with scene geometry and materials. Our framework supports complex combustion phenomena -- including flame propagation, smoke dispersion, and surface carbonization -- with precise user control over fire intensity, airflow, ignition location and other combustion parameters. Evaluated on diverse indoor and outdoor scenes, FieryGS outperforms all comparative baselines in visual realism, physical fidelity, and controllability. Project page can be found at https://pku-vcl-geometry.github.io/FieryGS/.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (11) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[ArtSplat: Feed-Forward Articulated 3D Gaussian Splatting from Sparse Multi-State Uncalibrated Views](https://arxiv.org/abs/2605.24304)**  
  *Inseo Lee, Yoonji Kim, Eugene Sohn, Jiwoong Lee, Jungmin You, Joonseok Lee, Jin-Hwa Kim*  
  `2026-05-23` · `cs.CV` · [abs](https://arxiv.org/abs/2605.24304) · [pdf](https://arxiv.org/pdf/2605.24304.pdf)
  > 💡 针对稀疏多状态未标定视图关节物体重建，提出ArtSplat前馈框架，利用每像素关节图和跨状态注意力，实现快速几何与关节参数联合估计。

  <details><summary>Abstract</summary>

  Articulated object reconstruction from sparse-view images is an ill-posed problem that requires simultaneous inference of geometry and underlying articulation structure. Existing methods for articulated object reconstruction based on NeRF and 3D Gaussian Splatting (3DGS) typically rely on dense views or strong priors (e.g., depth maps, joint types, predefined number of joints) and require costly per-object optimization. In this paper, we propose ArtSplat, the first feed-forward framework for articulated 3D Gaussian Splatting. It reconstructs both geometry and joint parameters from sparse multi-view images across multiple articulation states in a single forward pass. To address the challenges of single-pass articulated reconstruction, we introduce a per-pixel joint map representation that enables the integration of joint parameter estimation into the feed-forward pipeline. We further propose a Cross-State Attention (CSA) mechanism with state tokens, which effectively captures discrete motion across input states. Experiments on 68 articulated objects from PartNet-Mobility, including both single- and multi-joint configurations, demonstrate that ArtSplat achieves competitive performance in both geometry and joint estimation, while being over 400 times faster than baselines.

  </details>


- **[LangFlash: Feed-forward 3D Language Gaussian Splatting from Sparse Unposed Images](https://arxiv.org/abs/2605.23287)**  
  *Yilong Liu, Wanhua Li, Chen Zhu-Tian, Hanspeter Pfister*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23287) · [pdf](https://arxiv.org/pdf/2605.23287.pdf)
  > 💡 提出前馈框架LangFlash，从稀疏无位姿图像直接预测三维高斯语义场，实现低延迟重建和一致语义理解。

  <details><summary>Abstract</summary>

  We present LangFlash, a feed-forward framework for 3D Language Gaussian Splatting that reconstructs 3D scenes parameterized by Gaussian primitives enriched with language-aligned semantic features from sparse unposed multi-view images. Unlike optimization-based 3D methods, LangFlash directly predicts the geometry and semantics in a single forward pass, enabling low-latency 3D reconstruction and language-consistent scene understanding. To support large-scale training, we enriched the RealEstate10k dataset with coherent and dense semantic information for 3D semantic supervision. Furthermore, we propose a sparse semantic encoding scheme that combines a global semantic dictionary with locally varying per-primitive weights, preserving high-level linguistic information, while reducing representation complexity. Experimental results show that LangFlash achieves superior novel view synthesis and semantic consistency compared with previous methods. This study establishes a new paradigm for pose-free, language-grounded 3D scene reconstruction, advancing generalizable 3D vision and multimodal scene understanding. Demo is available at https://liylo.github.io/langflash.github.io/.

  </details>


- **[PairDropGS: Paired Dropout-Induced Consistency Regularization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.12072)**  
  *Hantang Li, Qiang Zhu, Xiandong Meng, Xingtao Wang, Debin Zhao, Xiaopeng Fan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12072) · [pdf](https://arxiv.org/pdf/2605.12072.pdf)
  > 💡 现有dropout方法忽略不一致性导致不稳定；提出成对dropout一致性正则化，约束低频结构，提升稀疏视图3DGS重建质量与训练稳定性。

  <details><summary>Abstract</summary>

  Dropout-based sparse-view 3D Gaussian Splatting (3DGS) methods alleviate overfitting by randomly suppressing Gaussian primitives during training. Existing methods mainly focus on designing increasingly sophisticated dropout strategies, while they overlook the resulting inconsistencies among different dropped Gaussian subsets. This oversight often leads to unstable reconstruction and suboptimal Gaussian representation learning.In this paper, we revisit dropout-based sparse-view 3DGS from a consistency regularization perspective and propose PairDropGS, a Paired Dropout-induced Consistency Regularization framework for sparse-view Gaussian splatting. Specifically, PairDropGS first constructs a pair of the dropped Gaussian subsets from a shared Gaussian field and designs a low-frequency consistency regularization to constrain their low-frequency rendered structures. This design encourages the shared Gaussian field to preserve stable scene layout and coarse geometry under different random dropouts, while avoiding excessive constraints on ambiguous high-frequency details. Moreover, we introduce a progressive consistency scheduling strategy to gradually strengthen the consistency regularization during training for stability and robustness of reconstruction. Extensive experiments on widely-used sparse-view benchmarks demonstrate that PairDropGS achieves superior training stability, significantly outperforms existing dropout-based 3DGS methods in reconstruction quality, while exhibiting the simplicity and plug-and-play nature for improving dropout-based optimization.

  </details>


- **[AdaptSplat: Adapting Vision Foundation Models for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.10239)**  
  *Mingwei Xing, Xinliang Wang, Yifeng Shi*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10239) · [pdf](https://arxiv.org/pdf/2605.10239.pdf)
  > 💡 针对前馈3DGS跨域泛化差和高频保真不足，提出仅1.5M参数的频率保持适配器FPA，利用浅层高频先验提升性能。

  <details><summary>Abstract</summary>

  This work explores a simple yet powerful lightweight adapter design for feed-forward 3D Gaussian Splatting (3DGS). Existing methods typically apply complex, architecture-specific designs on top of the generic pipeline of image feature extraction $\rightarrow$ multi-view interaction $\rightarrow$ feature decoding. However, constrained by the scale bottleneck of 3D training data and the low-pass filtering effect of deep networks, these methods still fall short in cross-domain generalization and high-frequency geometric fidelity. To address these problems, we propose AdaptSplat, which demonstrates that without complex component engineering, introducing a single adapter of only 1.5M parameters into the generic architecture is sufficient to achieve superior performance. Specifically, we design a lightweight Frequency-Preserving Adapter (FPA) that extracts direction-aware high-frequency structural priors from the shallow features of a powerful vision foundation model backbone, and seamlessly integrates them into the generic pipeline via high-frequency positional encodings and adaptive residual modulation. This effectively compensates for the high-frequency attenuation caused by over-smoothing in deep features, improving the fitting accuracy of Gaussian primitives on complex surfaces and sharp boundaries. Extensive experiments demonstrate that AdaptSplat achieves state-of-the-art feed-forward reconstruction performance on multiple standard benchmarks, with stable generalization across domains. Code available at: https://github.com/xmw666/AdaptSplat.

  </details>


- **[SplatWeaver: Learning to Allocate Gaussian Primitives for Generalizable Novel View Synthesis](https://arxiv.org/abs/2605.07287)**  
  *Yecong Wan, Fan Li, Mingwen Shao, Wangmeng Zuo*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07287) · [pdf](https://arxiv.org/pdf/2605.07287.pdf)
  > 💡 针对固定高斯原语分配忽略空间复杂度问题，提出动态分配的SplatWeaver，通过专家与路由实现区域自适应，

  <details><summary>Abstract</summary>

  Generalizable novel view synthesis aims to render unseen views from uncalibrated input images without requiring per-scene optimization. Recent feed-forward approaches based on 3D Gaussian Splatting have achieved promising efficiency and rendering quality. However, most of them assign a fixed number of Gaussians to each pixel or voxel, ignoring the spatially varying complexity of real-world scenes. Such uniform allocation often wastes Gaussian primitives in smooth regions while providing insufficient capacity for fine structures, complex geometry, and high-frequency details. This motivates us to predict region-dependent primitive cardinalities rather than impose a fixed primitive budget everywhere, enabling a more expressive 3D scene representation. Therefore, we propose SplatWeaver, a generalizable novel view synthesis framework that is able to dynamically allocate Gaussian primitives over different regions in a feed-forward manner. Specifically, SplatWeaver introduces cardinality Gaussian experts and a pixel-level routing scheme, wherein each expert specializes in producing a specific number of primitives from 0 to M, and the routing scheme coordinates these experts to adaptively determine how many Gaussian primitives should be allocated to each spatial location. Moreover, SplatWeaver incorporates a high-frequency prior with attendant guidance module and routing regularization to stabilize expert selection and promote complexity-aware allocation. By leveraging high-frequency cues, the routing process is encouraged to assign more Gaussian primitives to fine structures and textured regions, while suppressing redundancy in smooth areas. Extensive experiments across diverse scenarios show that SplatWeaver consistently outperforms state-of-the-art methods, delivering more faithful novel-view renderings with fewer Gaussian primitives. Project Page: https://yecongwan.github.io/SplatWeaver/

  </details>


- **[SatSurfGS: Generalizable 2D Gaussian Splatting for Sparse-View Satellite Surface Reconstruction](https://arxiv.org/abs/2605.07181)**  
  *Min Chen, Wei Guo, Bin Wang, Wen Li, Tong Fang, Jinbo Zhang, Junqi Zhao, Hong Kuang, Han Hu, Xuming Ge, Qing Zhu, Bo Xu*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07181) · [pdf](https://arxiv.org/pdf/2605.07181.pdf)
  > 💡 针对稀疏视图卫星表面重建中多视角匹配空间异质问题，提出基于2DGS的可泛化方法，通过粗到细属性预测和三级局部几何可靠性建模提升重建精度与效率。

  <details><summary>Abstract</summary>

  Sparse-view satellite image surface reconstruction remains highly challenging, fundamentally because the reliability of multi-view matching under satellite imaging conditions is strongly spatially heterogeneous. Affected by large photometric differences, weak textures, and repetitive textures, multi-view geometric constraints are often sparse, unevenly distributed, and locally unreliable. Although 2D Gaussian Splatting (2DGS) is more suitable than 3D Gaussian Splatting (3DGS) for the explicit representation of continuous surfaces, research on generalizable feed-forward 2DGS frameworks for sparse-view satellite surface reconstruction is still lacking. To address this issue, we propose SatSurfGS, a generalizable sparse-view surface reconstruction method for satellite imagery based on 2DGS. The proposed method builds a coarse-to-fine Gaussian attribute prediction framework and explicitly models local geometric reliability at three levels: feature learning, Gaussian parameter estimation, and training optimization. Specifically, we propose a confidence-aware monocular multi-view feature fusion module to adaptively integrate monocular priors and multi-view matching features according to local confidence; a cross-stage self-consistency residual guidance module to stabilize stage-wise Gaussian parameter refinement using the residual between the rendered height map from the previous stage and the current-stage MVS height map, together with confidence information; and a confidence bidirectional routing loss to achieve differentiated allocation of geometric and appearance supervision. Experiments on satellite datasets show that the proposed method achieves improved rendering quality, surface reconstruction accuracy, cross-dataset generalization, and inference efficiency compared with representative generalizable baselines and competitive per-scene optimization methods.

  </details>


- **[VVGT: Visual Volume-Grounded Transformer](https://arxiv.org/abs/2604.12217)**  
  *Yuxuan Wang, Qibiao Li, Youcheng Cai*  
  `2026-04-14` · `cs.GR` · [abs](https://arxiv.org/abs/2604.12217) · [pdf](https://arxiv.org/pdf/2604.12217.pdf)
  > 💡 现有体可视化可扩展性差，提出前馈双Transformer网络VVGT，用体几何强制机制将体数据映射为3DGS，实现快速高质量免逐场景优化。

  <details><summary>Abstract</summary>

  Volumetric visualization has long been dominated by Direct Volume Rendering (DVR), which operates on dense voxel grids and suffers from limited scalability as resolution and interactivity demands increase. Recent advances in 3D Gaussian Splatting (3DGS) offer a representation-centric alternative; however, existing volumetric extensions still depend on costly per-scene optimization, limiting scalability and interactivity. We present VVGT (Visual Volume-Grounded Transformer), a feed-forward, representation-first framework that directly maps volumetric data to a 3D Gaussian Splatting representation, advancing a new paradigm for volumetric visualization beyond DVR. Unlike prior feed-forward 3DGS methods designed for surface-centric reconstruction, VVGT explicitly accounts for volumetric rendering, where each pixel aggregates contributions along a ray. VVGT employs a dual-transformer network and introduces Volume Geometry Forcing, an epipolar cross-attention mechanism that integrates multi-view observations into distributed 3D Gaussian primitives without surface assumptions. This design eliminates per-scene optimization while enabling accurate volumetric representations. Extensive experiments show that VVGT achieves high-quality visualization with orders-of-magnitude faster conversion, improved geometric consistency, and strong zero-shot generalization across diverse datasets, enabling truly interactive and scalable volumetric visualization. The code will be publicly released upon acceptance.

  </details>


- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370)**  
  *Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan*  
  `2026-04-09` · `cs.CV` · [abs](https://arxiv.org/abs/2604.08370) · [pdf](https://arxiv.org/pdf/2604.08370.pdf)
  > 💡 针对稀疏视图表面重建，提出基于奈奎斯特采样定理的前馈框架，高效生成可泛化高斯surfel表示，实现快速精确重建。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has demonstrated impressive performance in 3D scene reconstruction. Beyond novel view synthesis, it shows great potential for multi-view surface reconstruction. Existing methods employ optimization-based reconstruction pipelines that achieve precise and complete surface extractions. However, these approaches typically require dense input views and high time consumption for per-scene optimization. To address these limitations, we propose SurfelSplat, a feed-forward framework that generates efficient and generalizable pixel-aligned Gaussian surfel representations from sparse-view images. We observe that conventional feed-forward structures struggle to recover accurate geometric attributes of Gaussian surfels because the spatial frequency of pixel-aligned primitives exceeds Nyquist sampling rates. Therefore, we propose a cross-view feature aggregation module based on the Nyquist sampling theorem. Specifically, we first adapt the geometric forms of Gaussian surfels with spatial sampling rate-guided low-pass filters. We then project the filtered surfels across all input views to obtain cross-view feature correlations. By processing these correlations through a specially designed feature fusion network, we can finally regress Gaussian surfels with precise geometry. Extensive experiments on DTU reconstruction benchmarks demonstrate that our model achieves comparable results with state-of-the-art methods, and predict Gaussian surfels within 1 second, offering a 100x speedup without costly per-scene training.

  </details>


- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693)**  
  *Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu*  
  `2026-04-06` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04693) · [pdf](https://arxiv.org/pdf/2604.04693.pdf)
  > 💡 针对ADF-STEM稀疏视角重建伪影问题，提出DenZa-Gaussian，用标量场denza建模散射，引入γ和傅里叶损失实现高保真重建。

  <details><summary>Abstract</summary>

  Analytical Dark Field Scanning Transmission Electron Microscopy (ADF-STEM) tomography reconstructs nanoscale materials in 3D by integrating multi-view tilt-series images, enabling precise analysis of their structural and compositional features. Although integrating more tilt views improves 3D reconstruction, it requires extended electron exposure that risks damaging dose-sensitive materials and introduces drift and misalignment, making it difficult to balance reconstruction fidelity with sample preservation. In practice, sparse-view acquisition is frequently required, yet conventional ADF-STEM methods degrade under limited views, exhibiting artifacts and reduced structural fidelity. To resolve these issues, in this paper, we adapt 3D GS to this domain with three key components. We first model the local scattering strength as a learnable scalar field, denza, to address the mismatch between 3DGS and ADF-STEM imaging physics. Then we introduce a coefficient $γ$ to stabilize scattering across tilt angles, ensuring consistent denza via scattering view normalization. Finally, We incorporate a loss function that includes a 2D Fourier amplitude term to suppress missing wedge artifacts in sparse-view reconstruction. Experiments on 45-view and 15-view tilt series show that DenZa-Gaussian produces high-fidelity reconstructions and 2D projections that align more closely with original tilts, demonstrating superior robustness under sparse-view conditions.

  </details>


- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030)**  
  *Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01030) · [pdf](https://arxiv.org/pdf/2604.01030.pdf)
  > 💡 通过可微优化层和不确定性模型，将前馈预测与测试时优化结合，提升3DGS渲染质量与鲁棒性。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) present two main directions: feed-forward models offer fast inference in sparse-view settings, while per-scene optimization yields high-quality renderings but is computationally expensive. To combine the benefits of both, we introduce Diff3R, a novel framework that explicitly bridges feed-forward prediction and test-time optimization. By incorporating a differentiable 3DGS optimization layer directly into the training loop, our network learns to predict an optimal initialization for test-time optimization rather than a conventional zero-shot result. To overcome the computational cost of backpropagating through the optimization steps, we propose computing gradients via the Implicit Function Theorem and a scalable, matrix-free PCG solver tailored for 3DGS optimization. Additionally, we incorporate a data-driven uncertainty model into the optimization process by adaptively controlling how much the parameters are allowed to change during optimization. This approach effectively mitigates overfitting in under-constrained regions and increases robustness against input outliers. Since our proposed optimization layer is model-agnostic, we show that it can be seamlessly integrated into existing feed-forward 3DGS architectures for both pose-given and pose-free methods, providing improvements for test-time optimization.

  </details>


- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394)**  
  *Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2603.29394) · [pdf](https://arxiv.org/pdf/2603.29394.pdf)
  > 💡 前馈3DGS在变分辨率下产生锯齿，AA-Splat通过OBBL双组件实现抗锯齿，PSNR提升5.4~7.5dB。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting (FF-3DGS) emerges as a fast and robust solution for sparse-view 3D reconstruction and novel view synthesis (NVS). However, existing FF-3DGS methods are built on incorrect screen-space dilation filters, causing severe rendering artifacts when rendering at out-of-distribution sampling rates. We firstly propose an FF-3DGS model, called AA-Splat, to enable robust anti-aliased rendering at any resolution. AA-Splat utilizes an opacity-balanced band-limiting (OBBL) design, which combines two components: a 3D band-limiting post-filter integrates multi-view maximal frequency bounds into the feed-forward reconstruction pipeline, effectively band-limiting the resulting 3D scene representations and eliminating degenerate Gaussians; an Opacity Balancing (OB) to seamlessly integrate all pixel-aligned Gaussian primitives into the rendering process, compensating for the increased overlap between expanded Gaussian primitives. AA-Splat demonstrates drastic improvements with average 5.4$\sim$7.5dB PSNR gains on NVS performance over a state-of-the-art (SOTA) baseline, DepthSplat, at all resolutions, between $4\times$ and $1/4\times$. Code will be made available.

  </details>


</details>

<details><summary><b>Semantic / Scene Understanding</b> (9) · <a href="topics/semantic.md">full list →</a></summary>

- **[Comparative evaluation of photogrammetric reconstruction methods and 3D Gaussian Splatting for road surface roughness analysis](https://arxiv.org/abs/2605.29452)**  
  *Marouane Elmegdar, Teng Xiao*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29452) · [pdf](https://arxiv.org/pdf/2605.29452.pdf)
  > 💡 比较COLMAP等四种重建法评估路面粗糙度，3DGS噪声大但可捕获不规则，开源管道适于低成本监测。

  <details><summary>Abstract</summary>

  Image-based 3D reconstruction offers a low-cost alternative to traditional sensor-based techniques for road surface assessment. This study compares four reconstruction pipelines--COLMAP, Meshroom, Metashape, and 3D Gaussian Splatting (3DGS)--to evaluate their ability to estimate road surface roughness from smartphone imagery. All point clouds were processed in CloudCompare using a consistent workflow involving orientation alignment, segmentation, normal estimation, and roughness computation at neighborhood radiuses of 0.2, 0.4, and 0.6 model units. The results show that COLMAP provides the highest sensitivity to micro-texture, while Meshroom yields balanced reconstructions with moderate roughness variation. Metashape produces the smoothest geometry due to its internal filtering, and 3DGS captures visible irregularities but exhibits higher noise and lower density. The comparison demonstrates that open-source pipelines are viable for relative roughness evaluation, offering a practical approach for low-cost pavement monitoring.

  </details>


- **[Uncertainty-Aware Gaussian Map for Vision-Language Navigation](https://arxiv.org/abs/2605.26503)**  
  *Jianzhe Gao, Rui Liu, Yuxuan Xu, Tongtong Cao, Yingxue Zhang, Zhanguang Zhang, Sida Peng, Yi Yang, Wenguan Wang*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26503) · [pdf](https://arxiv.org/pdf/2605.26503.pdf)
  > 💡 提出感知不确定性（几何、语义、外观）问题，通过语义高斯地图建模并扩展为3D价值地图，提升视觉语言导航可靠性。

  <details><summary>Abstract</summary>

  Vision-Language Navigation (VLN) requires an agent to navigate 3D environments following natural language instructions. During navigation, existing agents commonly encounter perceptual uncertainty, such as insufficient evidence for reliable grounding or ambiguity in interpreting spatial cues, yet they typically ignore such information when predicting actions. In this work, we explicitly model three forms of perceptual uncertainty (i.e., geometric, semantic, and appearance uncertainty) and integrate them into the agent's observation space to enable informed decision-making. Concretely, our agent first constructs a Semantic Gaussian Map (SGM), composed of differentiable 3D Gaussian primitives initialized from panoramic observations, that encodes both the geometric structure and semantic content of the environment. On top of SGM, geometric uncertainty is estimated through variational perturbations of Gaussian position and scale to assess structural reliability; semantic uncertainty is captured by perturbing Gaussian semantic attributes to reveal ambiguous interpretations; and appearance uncertainty is characterized by Fisher Information, which measures the sensitivity of rendered observations to Gaussian-level variations. These uncertainties are incorporated into SGM, extending it into a unified 3D Value Map, which grounds them as affordances and constraints that support reliable navigation. Comprehensive evaluations across multiple VLN benchmarks show the effectiveness of our agent.

  </details>


- **[Uncovering and Shaping the Latent Representation of 3D Scene Topology in Vision-Language Models](https://arxiv.org/abs/2605.07148)**  
  *Haoming Wang, Wei Gao*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07148) · [pdf](https://arxiv.org/pdf/2605.07148.pdf)
  > 💡 通过跨场景线性特征提取分离被语义掩盖的3D场景拓扑潜表征，并引入Dirichlet能量正则化提升VLM空间推理达12.1%。

  <details><summary>Abstract</summary>

  Decades of cognitive science establish that humans navigate environments by forming cognitive maps, defined as allocentric and topology-preserving representations of 3D space. While modern Vision-Language Models (VLMs) demonstrate emergent spatial reasoning from 2D egocentric inputs, it remains unclear whether they construct an analogous 3D internal representation. In this paper, we demonstrate that current VLMs do possess a latent topological map of 3D scenes, but it is heavily overshadowed by non-geometric visual semantics, such as color and shape. By isolating this spatial subspace through cross-scene linear feature extraction, we extract a clean spatial subspace that causally controls the model's spatial outputs. We mathematically shape this latent representation and prove its correspondence to the Laplacian eigenmaps of the scene's 3D Gaussian-kernel graph, converging to the physical 3D space in the continuous limit. Motivated by this geometric identification, we further introduce a mathematically principled latent regularization method for VLMs, based on Dirichlet energy. Applying this single-term regularizer to a minimal 500-step supervised VLM fine-tuning (SFT) on simple synthetic data yields significant improvements on real-world spatial benchmarks, outperforming standard SFT and competitive baselines by up to 12.1\% in spatial tasks involving scene topology understanding. Source code is available at https://github.com/pittisl/vlm-latent-shaping

  </details>


- **[OpenGaFF: Open-Vocabulary Gaussian Feature Field with Codebook Attention](https://arxiv.org/abs/2605.06088)**  
  *Kunyi Li, Michael Niemeyer, Sen Wang, Stefano Gasperini, Nassir Navab, Federico Tombari*  
  `2026-05-07` · `cs.CV` · [abs](https://arxiv.org/abs/2605.06088) · [pdf](https://arxiv.org/pdf/2605.06088.pdf)
  > 💡 通过高斯特征场和码本注意力增强几何-语义耦合，实现开放词汇3D场景中一致且可解释的语义分割。

  <details><summary>Abstract</summary>

  Understanding open-vocabulary 3D scenes with Gaussian-based representations remains challenging due to fragmented and spatially inconsistent semantic predictions across multi-view observations. In this paper, we present OpenGaFF, a novel framework for open-vocabulary 3D scene understanding built upon 3D Gaussian Splatting. At the core of our method is a Gaussian Feature Field that models semantics as a continuous function of Gaussian geometry and appearance. By explicitly conditioning semantic predictions on geometric structure, this formulation strengthens the coupling between geometry and semantics, leading to improved spatial coherence across similar structures in 3D space. To further enforce object-level semantic consistency, we introduce a structured codebook that serves as a set of shared semantic primitives. Furthermore, a codebook-guided attention mechanism is proposed to retrieve language features via similarity matching between query embeddings and learned codebook entries, enabling robust open-vocabulary reasoning while reducing intra-object feature variance. Extensive experiments on standard 2D and 3D open-vocabulary benchmarks demonstrate that our method consistently outperforms prior approaches, achieving improved segmentation quality, stronger 3D semantic consistency and a semantically interpretable codebook that provides insight into the learned representation.

  </details>


- **[Ilov3Splat: Instance-Level Open-Vocabulary 3D Scene Understanding in Gaussian Splatting](https://arxiv.org/abs/2605.04506)**  
  *Binh Long Nguyen, Kien Nguyen, Sridha Sridharan, Clinton Fookes, Peyman Moghadam*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04506) · [pdf](https://arxiv.org/pdf/2605.04506.pdf)
  > 💡 用多分辨率哈希嵌入增强Gaussian splats的CLIP特征和实例特征场，实现无需标注的开放词汇实例分割。

  <details><summary>Abstract</summary>

  We introduce Ilov3Splat, a novel framework for instance-level open-vocabulary 3D scene understanding built on 3D Gaussian Splatting (3D-GS). Most prior work depends on 2D rendering-based matching or point-level semantic association, which undermines cross-view consistency, lacks coherent instance-level reasoning, and limits precision in downstream 3D tasks. To address these limitations, our method jointly optimizes scene geometry and semantic representations by augmenting Gaussian splats with view-consistent feature fields. Specifically, we leverage multi-resolution hash embedding to efficiently encode language-aligned CLIP features, enabling dense and coherent language grounding in 3D space. We further train an instance feature field using contrastive loss over SAM masks, supporting fine-grained object distinction across views. At inference time, CLIP-encoded queries are matched against the learned features, followed by two-stage 3D clustering to retrieve relevant Gaussian groups. This enables our framework to identify arbitrary objects in 3D scenes based on natural language descriptions, without requiring category supervision or manual annotations. Experiments on standard benchmarks demonstrate that Ilov3Splat outperforms prior open-vocabulary 3D-GS methods in both object selection and instance segmentation, offering a flexible and accurate solution for language-driven 3D scene understanding. Project page: https://csiro-robotics.github.io/Ilov3Splat.

  </details>


- **[NRGS: Neural Regularization for Robust 3D Semantic Gaussian Splatting](https://arxiv.org/abs/2604.22439)**  
  *Zaiyan Yang, Xinpeng Liu, Heng Guo, Jinglei Shi, Zhanyu Ma, Fumio Okura*  
  `2026-04-24` · `cs.CV` · [abs](https://arxiv.org/abs/2604.22439) · [pdf](https://arxiv.org/pdf/2604.22439.pdf)
  > 💡 针对多视图不一致特征导致的3D语义场噪声，提出方差感知条件MLP直接校正高斯语义，提升鲁棒性和精度。

  <details><summary>Abstract</summary>

  We propose a neural regularization method that refines the noisy 3D semantic field produced by lifting multi-view inconsistent 2D features, in order to obtain an accurate and robust 3D semantic Gaussian Splatting. The 2D features extracted from vision foundation models suffer from multi-view inconsistency due to a lack of cross-view constraints. Lifting these inconsistent features directly into 3D Gaussians results in a noisy semantic field, which degrades the performance of downstream tasks. Previous methods either focus on obtaining consistent multi-view features in the preprocessing stage or aim to mitigate noise through improved optimization strategies, often at the cost of increased preprocessing time or expensive computational overhead. In contrast, we introduce a variance-aware conditional MLP that operates directly on the 3D Gaussians, leveraging their geometric and appearance attributes to correct semantic errors in 3D space. Experiments on different datasets show that our method enhances the accuracy of lifted semantics, providing an efficient and effective approach to robust 3D semantic Gaussian Splatting.

  </details>


- **[NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706)**  
  *Yi He, Tao Wang, Yi Jin, Congyan Lang, Yidong Li, Haibin Ling*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.14706) · [pdf](https://arxiv.org/pdf/2604.14706.pdf)
  > 💡 利用掩码方差识别边界模糊高斯，通过RBF插值与多分辨率哈希编码构建连续特征场并联合NeRF优化，显著提升3DGS分割边界精度。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled highly efficient and photorealistic novel view synthesis. However, segmenting objects accurately in 3DGS remains challenging due to the discrete nature of Gaussian representations, which often leads to aliasing and artifacts at object boundaries. In this paper, we introduce NG-GS, a novel framework for high-quality object segmentation in 3DGS that explicitly addresses boundary discretization. Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis. We then apply radial basis function (RBF) interpolation to construct a spatially continuous feature field, enhanced by multi-resolution hash encoding for efficient multi-scale representation. A joint optimization strategy aligns 3DGS with a lightweight NeRF module through alignment and spatial continuity losses, ensuring smooth and consistent segmentation boundaries. Extensive experiments on NVOS, LERF-OVS, and ScanNet benchmarks demonstrate that our method achieves state-of-the-art performance, with significant gains in boundary mIoU. Code is available at https://github.com/BJTU-KD3D/NG-GS.

  </details>


- **[Scene-Agnostic Object-Centric Representation Learning for 3D Gaussian Splatting](https://arxiv.org/abs/2604.09045)**  
  *Tsuheng Hsu, Guiyu Liu, Juho Kannala, Janne Heikkilä*  
  `2026-04-10` · `cs.CV` · [abs](https://arxiv.org/abs/2604.09045) · [pdf](https://arxiv.org/pdf/2604.09045.pdf)
  > 💡 提出场景无关的物体编码本，将物体中心学习引入3DGS，解决场景依赖问题并提升跨场景泛化能力。

  <details><summary>Abstract</summary>

  Recent works on 3D scene understanding leverage 2D masks from visual foundation models (VFMs) to supervise radiance fields, enabling instance-level 3D segmentation. However, the supervision signals from foundation models are not fundamentally object-centric and often require additional mask pre/post-processing or specialized training and loss design to resolve mask identity conflicts across views. The learned identity of the 3D scene is scene-dependent, limiting generalizability across scenes. Therefore, we propose a dataset-level, object-centric supervision scheme to learn object representations in 3D Gaussian Splatting (3DGS). Building on a pre-trained slot attention-based Global Object Centric Learning (GOCL) module, we learn a scene-agnostic object codebook that provides consistent, identity-anchored representations across views and scenes. By coupling the codebook with the module's unsupervised object masks, we can directly supervise the identity features of 3D Gaussians without additional mask pre-/post-processing or explicit multi-view alignment. The learned scene-agnostic codebook enables object supervision and identification without per-scene fine-tuning or retraining. Our method thus introduces unsupervised object-centric learning (OCL) into 3DGS, yielding more structured representations and better generalization for downstream tasks such as robotic interaction, scene understanding, and cross-scene generalization.

  </details>


- **[Indoor Asset Detection in Large Scale 360° Drone-Captured Imagery via 3D Gaussian Splatting](https://arxiv.org/abs/2604.05316)**  
  *Monica Tang, Avideh Zakhor*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05316) · [pdf](https://arxiv.org/pdf/2604.05316.pdf)
  > 💡 针对无人机360°图像重建的3DGS场景，提出3D物体码本结合语义与空间信息进行多视角掩码关联，检测性能提升显著。

  <details><summary>Abstract</summary>

  We present an approach for object-level detection and segmentation of target indoor assets in 3D Gaussian Splatting (3DGS) scenes, reconstructed from 360° drone-captured imagery. We introduce a 3D object codebook that jointly leverages mask semantics and spatial information of their corresponding Gaussian primitives to guide multi-view mask association and indoor asset detection. By integrating 2D object detection and segmentation models with semantically and spatially constrained merging procedures, our method aggregates masks from multiple views into coherent 3D object instances. Experiments on two large indoor scenes demonstrate reliable multi-view mask consistency, improving F1 score by 65% over state-of-the-art baselines, and accurate object-level 3D indoor asset detection, achieving an 11% mAP gain over baseline methods.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (20) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[DVSM: Decoder-only View Synthesis Model Done Right](https://arxiv.org/abs/2605.29891)**  
  *Cheng Sun, Jaesung Choe, Min-Hung Chen, Ryo Hachiuma, Yu-Chiang Frank Wang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29891) · [pdf](https://arxiv.org/pdf/2605.29891.pdf)
  > 💡 纯解码器架构以KV-cache隐式表示场景，权重共享与基础先验提升效率，在视图合成中超越编码器-解码器及3D

  <details><summary>Abstract</summary>

  Recent Large View Synthesis Models (LVSMs) advocate an encoder-decoder architecture that separates reconstruction and rendering into distinct networks. We re-examine this design. Through controlled experiments, we show that a decoder-only architecture, which represents scenes implicitly as a KV-cache, outperforms encoder-decoder variants while using fewer parameters at identical rendering complexity. Further analysis shows that sharing weights between the color-input reconstruction network and the camera-only rendering network better aligns their features at the same viewpoint, facilitating image synthesis. Building on this finding, our model, dubbed DVSM, further incorporates foundation model priors and stage-wise patch sizing for an improved efficiency-quality tradeoff. Our results establish a new state of the art for novel-view synthesis across multiple benchmarks, in some cases even outperforming per-scene-optimized 3DGS under dense input views.

  </details>


- **[Depth Peeling for High-Fidelity Gaussian-Enhanced Surfel Rendering](https://arxiv.org/abs/2605.25345)**  
  *Keyang Ye, Hongzhi Wu, Kun Zhou*  
  `2026-05-25` · `cs.GR` · [abs](https://arxiv.org/abs/2605.25345) · [pdf](https://arxiv.org/pdf/2605.25345.pdf)
  > 💡 用半透明边界和深度剥离排序解决高斯增强表面混叠伪影，实现高质量可微渲染与重建。

  <details><summary>Abstract</summary>

  Novel view synthesis has been significantly advanced by NeRFs and 3D Gaussian Splatting (3DGS), which require ordering volumetric samples or primitives for correct color blending. While the recent Gaussian-Enhanced Surfels (GES) enable high-performance, sort-free rendering, they suffer from aliasing artifacts and suboptimal reconstruction. To address these limitations, we propose DP-GES, a novel representation that augments opaque surfels with semi-transparent boundaries and leverages Depth Peeling to establish accurate per-pixel ordering. This design enables sort-free Gaussian splatting with correct transmittance modulation, effectively eliminating aliasing and popping artifacts while facilitating a fully differentiable joint optimization. Extensive experiments demonstrate that our method achieves superior reconstruction quality and compares favorably against state-of-the-art techniques across a wide range of scenes.

  </details>


- **[ConFi-GS Confidence-Guided High-Frequency Injection for 3D Gaussian Splatting Super-Resolution](https://arxiv.org/abs/2605.24964)**  
  *Jiaxiang Li, Zongtan Zhou, Zhen Tan, Yadong Liu, Dewen Hu*  
  `2026-05-24` · `cs.CV` · [abs](https://arxiv.org/abs/2605.24964) · [pdf](https://arxiv.org/pdf/2605.24964.pdf)
  > 💡 针对低分辨率3DGS重建细节模糊问题，提出可靠性感知频率建模，通过细节注入图引导空间选择性监督与频率正则化，提升质量并抑制不一致细节。

  <details><summary>Abstract</summary>

  Reconstructing high-quality 3D scenes from low-resolution multi-view images remains challenging for 3D Gaussian Splatting (3DGS), because insufficient high-frequency observations often lead to blurred textures, weak boundaries, and view-inconsistent details. Existing approaches either apply super-resolution guidance uniformly or localize enhancement regions based mainly on geometric sampling. However, they typically do not distinguish between two fundamentally different questions: where additional detail is needed, and whether the corresponding candidate high-frequency content is reliable enough to be internalized into a multi-view consistent 3D representation. In this paper, we propose a reliability-aware frequency modeling framework for low-resolution 3DGS reconstruction. The framework first estimates a geometry-guided detail-demand prior to locate regions that are likely under-detailed under low-resolution supervision. It then computes a frequency-aware reliability map to determine whether candidate high-frequency details are structurally supported, spectrally unresolved, and cross-view stable. Combining these signals yields a detail-injection map that guides where super-resolved details should be introduced during optimization. Based on this map, we design a unified optimization scheme comprising spatially selective supervision, coarse-to-fine frequency regularization, and reliability-aware Gaussian densification. This scheme controls where reliable details are injected, when high-frequency supervision is activated, and how unresolved yet reliable details are internalized into the Gaussian representation. Experiments on multiple benchmarks show improved fidelity and perceptual quality while suppressing unstable or view-inconsistent details.

  </details>


- **[Transcoding a 3D Gaussian Splatting Model from a Plenoptic Point Cloud or Mesh without the Original Multi-view Images](https://arxiv.org/abs/2605.21051)**  
  *Maja Krivokuća, Riad Bendouro, Neus Sabater*  
  `2026-05-20` · `eess.IV` · [abs](https://arxiv.org/abs/2605.21051) · [pdf](https://arxiv.org/pdf/2605.21051.pdf)
  > 💡 提出从光场点云或网格转码为3DGS的端到端管道，自定义初始化引导学习，实现高视觉质量、更少高斯和快速收敛。

  <details><summary>Abstract</summary>

  In this paper, we propose an end-to-end transcoding pipeline, to create 3D Gaussian splatting (3DGS) models from existing 3D plenoptic point cloud or mesh models, when the original multi-view images of the captured 3D object or scene are not available. We also propose a custom initialisation to guide the 3DGS model learning, with constraints to ensure that the final 3DGS model aligns closely with the input point cloud or mesh surface. Tests on a high-quality, standard plenoptic point cloud dataset show that our pipeline produces 3DGS models of high visual quality, with many fewer splats than points in the original dense point clouds. Additionally, our custom initialisation leads to much faster convergence and cleaner surface representation than when starting from the default SfM-based initialisation that is typically used for 3DGS model learning.

  </details>


- **[Topo-GS: Continuous Volumetric Embedding of High-Dimensional Data via Topological Gaussian Splatting](https://arxiv.org/abs/2605.17011)**  
  *João Paulo Gois, Luis Gustavo Nonato*  
  `2026-05-16` · `cs.GR` · [abs](https://arxiv.org/abs/2605.17011) · [pdf](https://arxiv.org/pdf/2605.17011.pdf)
  > 💡 将3DGS用于高维投影，通过局部几何约束和拓扑感知策略生成连续体积表示，避免离散点云遮挡与间断。

  <details><summary>Abstract</summary>

  Dimensionality reduction algorithms map high-dimensional data into visualizable 2D or 3D spaces, but traditionally rely on a discrete point-cloud paradigm. This discrete abstraction is susceptible to visual occlusion and artificial discontinuities, often failing to represent the continuous density of the underlying manifold. To address these limitations, we introduce Topo-GS, a framework that repurposes 3D Gaussian Splatting (3DGS) to cast multidimensional projection as a meshless volumetric reconstruction process. Instead of standard photometric losses, Topo-GS is driven by local geometric constraints. By solving orthogonal Procrustes targets, the optimization enforces an As-Rigid-As-Possible prior while explicitly aligning the spatial covariance of each Gaussian to the local tangent space. Recognizing that unrolling data of varying intrinsic dimensionalities requires distinct spatial treatments, we utilize a topology-aware strategy that tailors the loss formulation to preserve either continuous 1D trajectories or cohesive 2D surfaces. Quantitative and visual evaluations demonstrate that Topo-GS successfully transforms discrete scatter plots into continuous volumetric representations, where inherent projection distortions explicitly manifest as observable geometric variations, while preserving local topological fidelity comparable to discrete baselines.

  </details>


- **[Learn2Splat: Extending the Horizon of Learned 3DGS Optimization](https://arxiv.org/abs/2605.15760)**  
  *Naama Pearl, Stefano Esposito, Haofei Xu, Amit Peleg, Patricia Gschossmann, Lorenzo Porzi, Peter Kontschieder, Gerard Pons-Moll, Andreas Geiger*  
  `2026-05-15` · `cs.CV` · [abs](https://arxiv.org/abs/2605.15760) · [pdf](https://arxiv.org/pdf/2605.15760.pdf)
  > 💡 提出元学习优化器Learn2Splat，以检查点缓冲和展开策略扩展优化

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) optimization is most commonly performed using standard optimizers (Adam, SGD). While stable across diverse scenes, standard optimizers are general-purpose and not tailored to the structure of the problem. In particular, they produce independent parameter updates that do not capture the structural and spatial relationships within a scene, leading to inefficient optimization and slow convergence. Recent works introduced learned optimizers that predict correlated updates informed by inter-parameter and inter-Gaussian dependencies. However, these methods are trained for a fixed number of optimization iterations and rely on manually scheduled learning rates to avoid degradation. In this paper, we introduce a learned optimizer for 3DGS that avoids degradation over extended optimization horizons without auxiliary mechanisms. To enable this, we propose a meta-learning scheme that extends the optimization horizon via a checkpoint buffer and an optimizer rollout strategy, combined with an architecture that encodes gradient scale information in its latent states. Results show improved early novel view synthesis quality while remaining stable over long horizons, with zero-shot generalization to unseen reconstruction settings. To support our findings, we introduce the first unified framework for training and evaluating both learned and conventional optimizers across sparse and dense view settings. Code and models will be released publicly. Our project page is available at https://naamapearl.github.io/learn2splat .

  </details>


- **[FLUIDSPLAT: Reconstructing Physical Fields from Sparse Sensors via Gaussian Primitives](https://arxiv.org/abs/2605.18866)**  
  *Huaxi Huang, Meng Li, Zhengqing Gao, Xi Zhou, Xiaoshui Huang, Xiao Sun*  
  `2026-05-15` · `cs.LG` · [abs](https://arxiv.org/abs/2605.18866) · [pdf](https://arxiv.org/pdf/2605.18866.pdf)
  > 💡 基于3DGS提出各向异性高斯基元结合状态残差解码器，从稀疏传感器重建流场，理论指导基元数量平衡，误差降低11-28%。

  <details><summary>Abstract</summary>

  Reconstructing continuous flow fields from sparse surface-mounted sensors is central to aerodynamic design, flow control, and digital-twin instrumentation. Existing neural methods for this task typically encode sensor readings into implicit latent codes with little spatial interpretability and limited formal guidance on how representational capacity should scale with observation count. Inspired by 3D Gaussian Splatting, we introduce FLUIDSPLAT, a sensor-conditioned model that predicts K anisotropic Gaussian primitives forming a partition-of-unity scaffold, a spatially explicit and interpretable intermediate representation of the flow. For an idealized Gaussian primitive estimator, we prove an $O(K^{-s/d})$ approximation rate for fields with Sobolev smoothness $s$; incorporating $N$ noisy observations yields a squared-risk decomposition with bias $O(K^{-2s/d})$ and variance $O(σ^{2}K/N)$.Balancing the two yields $K^{*}\!\sim\!(N/σ^{2})^{d/(2s+d)}$: primitive count cannot grow freely under sparse sensing, revealing a variance bottleneck that motivates complementing the scaffold with a state-conditioned residual decoder. Across four benchmarks spanning 2D and 3D, FLUIDSPLAT achieves 11-28% error reduction over several strong baselines on cylinder flow, AirfRANS, FlowBench LDC-3D, and PhySense-Car 3D benchmarks.

  </details>


- **[GeoGS-CE: Learning Delay--Beam Channel Priors with 3D Gaussians for High-Mobility Scenarios](https://arxiv.org/abs/2605.16094)**  
  *Yumeng Zhang, Jiajia Guo, Chaozheng Wen, Chenghong Bian, Jun Zhang*  
  `2026-05-15` · `cs.IT` · [abs](https://arxiv.org/abs/2605.16094) · [pdf](https://arxiv.org/pdf/2605.16094.pdf)
  > 💡 使用3D高斯建模几何散射先验，结合可微渲染预测功率谱，提升高移动场景稀疏导频信道估计精度。

  <details><summary>Abstract</summary>

  Wideband channel estimation (CE) in high-mobility scenarios remains challenging because channel responses vary rapidly, while practical systems can allocate only sparse pilots to accommodate dense users. Fortunately, many high-mobility environments, such as high-speed railways, exhibit scheduled trajectories, predictable velocities, and a limited number of dominant propagation paths. These properties induce a delay--beam power spectrum that is more stable than the instantaneous complex channel frequency response (CFR), less sensitive to the random phase coherence, and rich in geometric information. To exploit such environmental properties, we propose GeoGS-CE, a two-stage channel estimation framework for sparse-pilot high-mobility scenarios. In the offline stage, GeoGS-CE jointly models: 1) a scene-level 3D Gaussian representation that captures the non-line-of-sight (NLoS) geometric scattering support, and 2) a leakage-aware differentiable wireless rendering process that maps the NLoS Gaussians, together with an explicit virtual line-of-sight (LoS) component, to the measured delay--beam power spectrum, while accounting for practical OFDM delay and array leakage effects. In the online stage, the delay--beam power spectrum is predicted for each user location and used as a strong covariance prior, enabling accurate full-band and full-array CFR reconstruction and tracking through a linear MMSE estimator. Simulations based on channels generated from a segment of the Guangshen high-speed railway show that the proposed geometric prior substantially improves CFR reconstruction over pilot-only and non-geometric baselines.

  </details>


- **[Revisiting Photometric Ambiguity for Accurate Gaussian-Splatting Surface Reconstruction](https://arxiv.org/abs/2605.12494)**  
  *Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Xiaohan Yu, Lin Gu, Gim Hee Lee*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12494) · [pdf](https://arxiv.org/pdf/2605.12494.pdf)
  > 💡 针对光度歧义导致表面重建不准确的问题，利用高斯溅射自指示潜力，提出光度去歧义与歧义指示模块实现鲁棒高精度重建。

  <details><summary>Abstract</summary>

  Surface reconstruction with differentiable rendering has achieved impressive performance in recent years, yet the pervasive photometric ambiguities have strictly bottlenecked existing approaches. This paper presents AmbiSuR, a framework that explores an intrinsic solution upon Gaussian Splatting for the photometric ambiguity-robust surface 3D reconstruction with high performance. Starting by revisiting the foundation, our investigation uncovers two built-in primitive-wise ambiguities in representation, while revealing an intrinsic potential for ambiguity self-indication in Gaussian Splatting. Stemming from these, a photometric disambiguation is first introduced, constraining ill-posed geometry solution for definite surface formation. Then, we propose an ambiguity indication module that unleashes the self-indication potential to identify and further guide correcting underconstrained reconstructions. Extensive experiments demonstrate our superior surface reconstructions compared to existing methods across various challenging scenarios, excelling in broad compatibility. Project: https://fictionarry.github.io/AmbiSuR-Proj/ .

  </details>


- **[XFreq-GS: Cross-Frequency Wireless Radiation Field Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11432)**  
  *Sheng Wang, Hengtao He, Chaozheng Wen, Jingwen Tong, Xinyu Li, Xiao Li, Jun Zhang, Shi Jin*  
  `2026-05-12` · `eess.SP` · [abs](https://arxiv.org/abs/2605.11432) · [pdf](https://arxiv.org/pdf/2605.11432.pdf)
  > 💡 现有3DGS方法仅支持单频，利用共享几何与频率自适应射频属性的高斯原语重建跨频率无线辐射场，性能优于现有方法。

  <details><summary>Abstract</summary>

  Channel modeling is fundamental to the analysis, design, and optimization of wireless communication systems, which, however, accurate wireless channel modeling remains challenging, especially given the increasingly complex wireless environments. As an emerging paradigm, 3D Gaussian Splatting (3DGS)-based channel modeling methods achieve accurate wireless radiation field (WRF) reconstruction and high-fidelity spatial spectrum synthesis. However, existing works only consider a single carrier frequency and fail to adapt to wide-range cross-frequency channels. To address this challenge, we propose XFreq-GS, a cross-frequency Gaussian splatting framework for WRF reconstruction. It employs 3D Gaussian primitives with shared geometry and frequency-adaptive radio frequency (RF) attributes to reconstruct cross-frequency WRF, and synthesizes power angular spectrum (PAS) maps for wireless channel modeling. Experiments show that XFreq-GS outperforms state-of-the-art 3DGS-based methods in PAS synthesis and achieves superior cross-frequency generalization. Code is available at https://github.com/KINGAZ1019/XFreq-GS.

  </details>


- **[TransmissiveGS: Residual-Guided Disentangled Gaussian Splatting for Transmissive Scene Reconstruction and Rendering](https://arxiv.org/abs/2605.10705)**  
  *Zhenyu Liang, Xiao Zhang, Tianchao Li, Jack C. P. Cheng, Chi-Keung Tang*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10705) · [pdf](https://arxiv.org/pdf/2605.10705.pdf)
  > 💡 针对透射场景反射与透射纠缠问题，提出双高斯表示与残差引导解耦框架，实现高质量重建与渲染。

  <details><summary>Abstract</summary>

  Transmissive scenes are ubiquitous in daily life, yet reconstructing and rendering them remains highly challenging due to the inherent entanglement between near-field reflections from the surrounding environment on the transmissive surface, and the transmitted content of the scene behind it. This coupling gives rise to dual surface geometries and dual radiance components within each observation, posing ambiguities for standard methods. We present TransmissiveGS, a novel framework for disentangled reconstruction and rendering of transmissive scenes. Specifically, we model the scene with a dual-Gaussian representation and introduce a deferred shading function to jointly render the two Gaussian components. To separate reflection and transmission, we exploit the inherent multi-view inconsistency of reflections and leverage the residuals from reconstructing multi-view consistent content as cues for disentangled geometry and appearance modeling. We further propose a reflection light field that enables high-fidelity estimation of near-field reflections. During training, we introduce a high-frequency regularization to preserve fine details. We also contribute a new synthetic dataset for evaluating transmissive surface reconstruction. Experiments on both synthetic and real-world scenes demonstrate that TransmissiveGS consistently outperforms prior Gaussian Splatting-based methods in both reconstruction and rendering quality for transmissive scenes.

  </details>


- **[From Pixels to Primitives: Scene Change Detection in 3D Gaussian Splatting](https://arxiv.org/abs/2605.07203)**  
  *Chamuditha Jayanga Galappaththige, Jason Lai, Timothy Patten, Donald Dansereau, Niko Suenderhauf, Dimity Miller*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07203) · [pdf](https://arxiv.org/pdf/2605.07203.pdf)
  > 💡 针对高斯泼溅场景变化检测中像素比对局限，提出直接利用高斯原语属性，通过各向异性漂移模型和可观测性项实现多视图一致且区分几何外观变化

  <details><summary>Abstract</summary>

  Scene change detection methods built on Gaussian splatting universally follow a render-then-compare paradigm: the pre-change scene is rendered into 2D and compared against post-change images via pixel or feature residuals. This change detection problem with Gaussian Splatting has been treated as a question about pixels; we treat it as a question about primitives. We provide direct evidence that native primitive attributes alone -- position, anisotropic covariance, and color -- carry sufficient signal for scene change detection. What makes primitive-space comparison hard is the under-constrained nature of Gaussian splatting representation: independent optimizations yield primitive solutions whose count, positions, shapes, and colors differ even where nothing has changed. We address this challenge with anisotropic models of geometric and photometric drift, complemented by a per-primitive observability term that reflects the extent to which each Gaussian is constrained by the camera geometry. Operating directly on primitives gives our method, GD-DIFF, two properties that distinguish it from render-then-compare methods. First, change maps are multi-view consistent by construction, where prior work had to learn this through an additional optimization objective. Second, geometric and appearance changes are scored separately, identifying not just where but what kind of change occurred, distinguishing structural changes (e.g., an added object) from surface-level ones (e.g., a color change) without supervision or external model dependencies. On real-world benchmarks, GS-DIFF surpasses the prior state-of-the-art approach by $\sim$17% in mean Intersection over Union.

  </details>


- **[AdpSplit: Error-Driven Adaptive Splitting for Faster Geometry Discovery in 3D Gaussian Splatting](https://arxiv.org/abs/2605.06876)**  
  *Yongjae Lee, Jingxing Li, Abhay Kumar Yadav, Rama Chellappa, Deliang Fan*  
  `2026-05-07` · `cs.CV` · [abs](https://arxiv.org/abs/2605.06876) · [pdf](https://arxiv.org/pdf/2605.06876.pdf)
  > 💡 针对3DGS固定分裂导致密集化慢的问题，提出误差驱动自适应分裂算子，根据像素误差统计确定子节点，减少训练时间9.2%-22.3%且保持质量。

  <details><summary>Abstract</summary>

  Adaptive density control in 3D Gaussian Splatting (3DGS) repeatedly grows the Gaussian population through fixed-cardinality random splitting to discover useful scene structure. However, in vanilla 3DGS, its binary split operator requires many densification rounds to expose fine details, making it a bottleneck for efficient training schedules with fewer iterations. We introduce AdpSplit, an error-driven adaptive split operator that determines the number of split children and initializes the child parameters from L1-pixel-error region statistics, enabling fewer densification iterations, thus reduced training time, while preserving the rendering quality of full-schedule training. Across the MipNeRF360, Deep-Blending, and Tanks&Temples datasets, AdpSplit reduces the training time of multiple accelerated 3DGS pipelines by 9.2%-22.3% as a simple drop-in replacement for the standard split operator. With FastGS, AdpSplit matches the full-schedule PSNR on MipNeRF360 while reducing training time by 16.4%, corresponding to a 12.6x acceleration over vanilla 3DGS.

  </details>


- **[Softmax-GS: Generalized Gaussians Learning When to Blend or Bound](https://arxiv.org/abs/2604.27437)**  
  *Chen Ziwen, Peng Wang, Hao Tan, Zexiang Xu, Li Fuxin*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.27437) · [pdf](https://arxiv.org/pdf/2604.27437.pdf)
  > 💡 提出Softmax-GS，用softmax竞争和可学习参数解决高斯重叠导致的视图不一致与边界模糊问题，实现SOTA。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3D GS) is widely adopted for novel view synthesis due to its high training and rendering efficiency. However, its efficiency relies on the key assumption that Gaussians do not overlap in the 3D space, which leads to noticeable artifacts and view inconsistencies. In addition, the inherently diffuse boundaries of Gaussians hinder accurate reconstruction of sharp object edges. We propose Softmax-GS, a unified solution that addresses both the view-inconsistency and the diffuse-boundary problem by enforcing a softmax-based competition in overlapping regions between two Gaussians. With learnable parameters controlling the strength of the competition, it enables a continuous spectrum from smooth color blending to crisp, well-defined boundaries. Our formulation explicitly preserves order invariance for any two overlapping Gaussians and ensures that the output transmittance remains unchanged irrespective of the extent of overlapping, preventing undesirable discontinuities in the rendered output. Ablation experiments on simple geometries demonstrate the effectiveness of each component of Softmax-GS, and evaluations on real-world benchmarks show that it achieves state-of-the-art performance, improving both reconstruction quality and parameter efficiency.

  </details>


- **[PAGaS: Pixel-Aligned 1DoF Gaussian Splatting for Depth Refinement](https://arxiv.org/abs/2604.22129)**  
  *David Recasens, Robert Maier, Aljaz Bozic, Stephane Grabli, Javier Civera, Tony Tung, Edmond Boyer*  
  `2026-04-24` · `cs.CV` · [abs](https://arxiv.org/abs/2604.22129) · [pdf](https://arxiv.org/pdf/2604.22129.pdf)
  > 💡 为多视图立体深度任务提出像素对齐一自由度高斯，限制位置大小仅优化深度，生成高细节深度图。

  <details><summary>Abstract</summary>

  Gaussian Splatting (GS) has emerged as an efficient approach for high-quality novel view synthesis. While early GS variants struggled to accurately model the scene's geometry, recent advancements constraining the Gaussians' spread and shapes, such as 2D Gaussian Splatting, have significantly improved geometric fidelity. In this paper, we present Pixel-Aligned 1DoF Gaussian Splatting (PAGaS) that adapts the GS representation from novel view synthesis to the multi-view stereo depth task. Our key contribution is modeling a pixel's depth using one-degree-of-freedom (1DoF) Gaussians that remain tightly constrained during optimization. Unlike existing approaches, our Gaussians' positions and sizes are restricted by the back-projected pixel volumes, leaving depth as the sole degree of freedom to optimize. PAGaS produces highly detailed depths, as illustrated in Figure 1. We quantitatively validate these improvements on top of reference geometric and learning-based multi-view stereo baselines on challenging 3D reconstruction benchmarks. Code: davidrecasens.github.io/pagas

  </details>


- **[You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes](https://arxiv.org/abs/2604.21400)**  
  *Jinrang Jia, Zhenjia Li, Yifeng Shi*  
  `2026-04-23` · `cs.CV` · [abs](https://arxiv.org/abs/2604.21400) · [pdf](https://arxiv.org/pdf/2604.21400.pdf)
  > 💡 针对3DGS工业部署中资源不可控与数据污染问题，提出YOGO实现确定性预算均衡，并发布超密集

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized neural rendering, yet existing methods remain predominantly research prototypes ill-suited for production-level deployment. We identify a critical "Industry-Academia Gap" hindering real-world application: unpredictable resource consumption from heuristic Gaussian growth, the "sparsity shield" of current benchmarks that rewards hallucination over physical fidelity, and severe multi-sensor data pollution. To bridge this gap, we propose YOGO (You Only Gaussian Once), a system-level framework that reformulates the stochastic growth process into a deterministic, budget-aware equilibrium. YOGO integrates a novel budget controller for hardware-constrained resource allocation and an availability-registration protocol for robust multi-sensor fusion. To push the boundaries of reconstruction fidelity, we introduce Immersion v1.0, the first ultra-dense indoor dataset specifically designed to break the "sparsity shield." By providing saturated viewpoint coverage, Immersion v1.0 forces algorithms to focus on extreme physical fidelity rather than viewpoint interpolation, and enables the community to focus on the upper limits of high-fidelity reconstruction. Extensive experiments demonstrate that YOGO achieves state-of-the-art visual quality while maintaining a strictly deterministic profile, establishing a new standard for production-grade 3DGS. To facilitate reproducibility, part scenes of Immersion v1.0 dataset and source code of YOGO has been publicly released. The project link is https://jjrcn.github.io/yogo-project-home/

  </details>


- **[Planar Gaussian Splatting with Bilinear Spatial Transformer for Wireless Radiance Field Reconstruction](https://arxiv.org/abs/2604.25945)**  
  *Jinghan Zhang, Xitao Gong, Qi Wang, Richard A. Stirling-Gallacher, Giuseppe Caire*  
  `2026-04-17` · `eess.SP` · [abs](https://arxiv.org/abs/2604.25945) · [pdf](https://arxiv.org/pdf/2604.25945.pdf)
  > 💡 用平面高斯和双线性空间变换器可解释地重建无线辐射场，在空间频谱合成任务上精度超越现有方法。

  <details><summary>Abstract</summary>

  Wireless radiance field (WRF) reconstruction aims to learn a continuous, queryable representation of radio frequency characteristics over 3D space and direction, from which specific quantities, such as the spatial power spectrum (SPS) at a receiver given a transmitter position, can be predicted. While Gaussian splatting (GS)-based method has surpassed Neural Radiance Fields (NeRF)-based method for this task, existing adaptations largely transplant vision pipelines, limiting physical interpretability and accuracy. We introduce BiSplat-WRF, a planar GS framework that retains the expressiveness of 3D GS while removing unnecessary projections and incorporating global EM coupling and mutual scattering among primitives. Each primitive is a 2D planar Gaussian with 3D coordinates, rendered directly on the angular domain of the SPS. A bilinear spatial transformer (BST) aggregates inter-primitive relations on an angular grid and, via attention, captures long-range electromagnetic dependencies, thereby enforcing globally aware EM interactions that reflect the complex physics of the wireless environment. On spatial spectrum synthesis task, BiSplat-WRF surpasses NeRF-based and prior GS-based baselines with respect to the Structural Similarity Index (SSIM); comprehensive ablation studies validate the contribution of BST. We also provide a larger BiSplat-WRF+ variant that further increases SSIM at a higher computation cost, serving as a strong reference for future studies.

  </details>


- **[AudioGS: Spectrogram-Based Audio Gaussian Splatting for Sound Field Reconstruction](https://arxiv.org/abs/2604.08967)**  
  *Chunhao Bi, Houqiang Zhong, Zhixin Xu, Li Song, Zhengxue Cheng*  
  `2026-04-10` · `cs.SD` · [abs](https://arxiv.org/abs/2604.08967) · [pdf](https://arxiv.org/pdf/2604.08967.pdf)
  > 💡 提出无需视觉先验的AudioGS框架，用频谱图定义音频高斯并编码声场，实现双耳音频重建，在MAG和DPAM指标上显著超越现有方法。

  <details><summary>Abstract</summary>

  Spatial audio is fundamental to immersive virtual experiences, yet synthesizing high-fidelity binaural audio from sparse observations remains a significant challenge. Existing methods typically rely on implicit neural representations conditioned on visual priors, which often struggle to capture fine-grained acoustic structures. Inspired by 3D Gaussian Splatting (3DGS), we introduce AudioGS, a novel visual-free framework that explicitly encodes the sound field as a set of Audio Gaussians based on spectrograms. AudioGS associates each time-frequency bin with an Audio Gaussian equipped with dual Spherical Harmonic (SH) coefficients and a decay coefficient. For a target pose, we render binaural audio by evaluating the SH field to capture directionality, incorporating geometry-guided distance attenuation and phase correction, and reconstructing the waveform. Experiments on the Replay-NVAS dataset demonstrate that AudioGS successfully captures complex spatial cues and outperforms state-of-the-art visual-dependent baselines. Specifically, AudioGS reduces the magnitude reconstruction error (MAG) by over 14% and reduces the perceptual quality metric (DPAM) by approximately 25% compared to the best performing visual-guided method.

  </details>


- **[SparseOIT: Improving Order-Independent Transparency 3DGS via Active Set Method](https://arxiv.org/abs/2605.13855)**  
  *Wentao Yang, Fanzhen Kong, Zejian Kang, Xiangru Huang*  
  `2026-04-07` · `cs.GR` · [abs](https://arxiv.org/abs/2605.13855) · [pdf](https://arxiv.org/pdf/2605.13855.pdf)
  > 💡 针对OIT渲染中变量稀疏依赖问题，提出基于活跃集方法的SparseOIT，加速3DGS透明物体重建并提升性能。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has received tremendous popularity over the past few years due to its photorealistic visual appearance. However, 3DGS uses volumetric rendering that is not suitable for objects with non-lambertian or transparent materials. To remedy this issue, a family of Order-Independent Transparency (OIT) rendering methods propose to remove or modify the depth sorting step in the 3DGS rendering equation. However, the potential of OIT-based method is still underexplored. In this paper, we observe that the OIT modifications to the rendering equation significantly reduce the inter-independence among individual gaussian splats, resulting in very sparse variable dependencies that can be harnessed by specific optimization techniques such as active set method. To this end, we propose SparseOIT, an OIT-based 3DGS reconstruction algorithm that maintains an active set of gaussian splats and enjoys an acceleration ratio that is proportional to the potential sparsity. SparseOIT is designed by jointly considering the OIT rendering equation, the reconstruction algorithm and the geometric regularization. Through extensive experiments, we demonstrate that SparseOIT outperforms existing methods in the OIT-family by a large margin and also achieves comparable performance to the state-of-the-art 3DGS reconstruction methods based on volumetric rendering. Project page:

  </details>


- **[SmokeGS-R: Physics-Guided Pseudo-Clean 3DGS for Real-World Multi-View Smoke Restoration](https://arxiv.org/abs/2604.05301)**  
  *Xueming Fu, Lixia Han*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05301) · [pdf](https://arxiv.org/pdf/2604.05301.pdf)
  > 💡 针对真实烟雾场景辐射衰减与外观不一致，提出物理引导伪清洁3DGS解耦几何与外观，领先基线+3.68dB PSNR。

  <details><summary>Abstract</summary>

  Real-world smoke simultaneously attenuates scene radiance, adds airlight, and destabilizes multi-view appearance consistency, making robust 3D reconstruction particularly difficult. We present \textbf{SmokeGS-R}, a practical pipeline developed for the NTIRE 2026 3D Restoration and Reconstruction Track 2 challenge. The key idea is to decouple geometry recovery from appearance correction: we generate physics-guided pseudo-clean supervision with a refined dark channel prior and guided filtering, train a sharp clean-only 3D Gaussian Splatting source model, and then harmonize its renderings with a donor ensemble using geometric-mean reference aggregation, LAB-space Reinhard transfer, and light Gaussian smoothing. On the official challenge testing leaderboard, the final submission achieved \mbox{PSNR $=15.217$} and \mbox{SSIM $=0.666$}. After the public release of RealX3D, we re-evaluated the same frozen result on the seven released challenge scenes without retraining and obtained \mbox{PSNR $=15.209$}, \mbox{SSIM $=0.644$}, and \mbox{LPIPS $=0.551$}, outperforming the strongest official baseline average on the same scenes by $+3.68$ dB PSNR. These results suggest that a geometry-first reconstruction strategy combined with stable post-render appearance harmonization is an effective recipe for real-world multi-view smoke restoration. The code is available at https://github.com/windrise/3drr_Track2_SmokeGS-R.

  </details>


</details>

<details><summary><b>Others</b> (7) · <a href="topics/others.md">full list →</a></summary>

- **[OctCGS: Octree-Contextual Gaussian Splatting with Explicit Multi-Order Propagation Modeling for Channel Knowledge Map Construction](https://arxiv.org/abs/2605.22961)**  
  *Jinghan Zhang, Xitao Gong, Qi Wang, Richard A. Stirling-Gallacher, Giuseppe Caire*  
  `2026-05-21` · `eess.SP` · [abs](https://arxiv.org/abs/2605.22961) · [pdf](https://arxiv.org/pdf/2605.22961.pdf)
  > 💡 八叉树上下文高斯溅射联合建模多阶传播，实现信道知识图构建，降低误差达0.88 dB MAE。

  <details><summary>Abstract</summary>

  Channel knowledge maps (CKMs) learn the relation between transmitter (Tx) and receiver (Rx) positions and channel knowledge to support environment-aware wireless communications. Implicit neural methods can model continuous channel variation but often incur high training and inference cost, while existing Gaussian-splatting-based CKM methods improve efficiency yet still compress wireless multipath interactions into aggregated scattering representations. Consequently, explicit modeling of multi-bounce wireless propagation remains absent from CKM construction. We propose OctCGS, an octree-contextual Gaussian splatting framework that explicitly models the order of bounce jointly over Tx/Rx positions and carrier frequencies. OctCGS partitions the environment into a multi-resolution octree and anchors one Gaussian primitive to each leaf node. Rather than having each Gaussian independently encode all multi-path propagations, it models complex electromagnetic interactions among scatterers through tree attention over the octree hierarchy with controlled complexity. Experiments on simulated benchmarks show that OctCGS achieves a 2.99 dB channel-gain mean absolute error (MAE) and 0.065 channel gain normalized mean absolute error (NMAE), outperforming the strongest baseline by 0.88 dB MAE and 0.021 NMAE.

  </details>


- **[Conflict-Aware Active Perception and Control in 3D Gaussian Splatting Fields via Control Barrier Functions](https://arxiv.org/abs/2605.20566)**  
  *Amirhossein Mollaei Khass, Athanasios Cosse, Vivek Pandey, Nader Motee*  
  `2026-05-19` · `cs.RO` · [abs](https://arxiv.org/abs/2605.20566) · [pdf](https://arxiv.org/pdf/2605.20566.pdf)
  > 💡 在3DGS场中采用控制障碍函数与风险感知信息增益，通过二次规划平衡冲突的安全与感知目标，提升安全性和信息采集效率

  <details><summary>Abstract</summary>

  Active perception in uncertain environments requires robots to navigate safely while acquiring informative observations to reduce map uncertainty. These objectives inherently conflict, as informative viewpoints often lie near uncertain regions with higher collision risk. To address this challenge, we develop a conflict-aware active perception and control framework for robotic systems operating in environments represented by 3D Gaussian Splatting (3DGS). Safety is enforced using a Control Barrier Function (CBF) derived from an Average Value-at-Risk AV@R collision-risk metric that accounts for geometric uncertainty and guarantees forward invariance of a safe set. To improve perception, we propose a risk-aware Expected Information Gain (EIG) formulation for selecting the next-best-view and introduce perception barrier functions that align the camera orientation with the local information-ascent direction. To obtain a tractable formulation for these conflicting safety and perception objectives, we propose a unified safety-critical, perception-aware quadratic program that enforces safety as a hard constraint while relaxing perception constraints through slack variables. Simulation results demonstrate that the proposed method improves both safety and information acquisition compared to existing 3DGS-based approaches.

  </details>


- **[A Geometric Algebra-Informed 3DGS Framework for Wireless Channel Prediction](https://arxiv.org/abs/2605.19065)**  
  *Jingzhou Shen, Tianya Zhao, Xuyu Wang*  
  `2026-05-18` · `cs.NI` · [abs](https://arxiv.org/abs/2605.19065) · [pdf](https://arxiv.org/pdf/2605.19065.pdf)
  > 💡 采用几何代数注意力机制与3D高斯泼溅，显式建模射线-物体交互，实现高精度无线信道预测。

  <details><summary>Abstract</summary>

  In this paper, we introduce Geometric Algebra-Informed 3D Gaussian Splatting (GAI-GS), a framework for wireless modeling that couples 3D Gaussian splatting with a geometric algebra-based attention mechanism to explicitly model ray-object interactions in complex propagation environments. GAI-GS encodes joint spatial-electromagnetic (EM) relations into token representations, enabling scene-level aggregation within a unified, end-to-end neural architecture. This design grounds wireless ray propagation in electromagnetic principles, allowing token interactions to model key effects such as multipath, attenuation, and reflection/diffraction. Through extensive evaluations on multiple real-world indoor datasets, GAI-GS consistently surpasses current baselines across various wireless tasks.

  </details>


- **[ReorgGS: Equivalent Distribution Reorganization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.08739)**  
  *Luchao Wang, Kaimin Liao, Qian Ren, Hua Wang, Zhi Chen, Yaohua Tang*  
  `2026-05-09` · `cs.CV` · [abs](https://arxiv.org/abs/2605.08739) · [pdf](https://arxiv.org/pdf/2605.08739.pdf)
  > 💡 针对3DGS参数化退化问题，通过等价分布重组重采样中心与协方差，改善梯度可访问性并抑制漂浮物，提升拟合质量。

  <details><summary>Abstract</summary>

  A converged 3D Gaussian Splatting (3DGS) model may approximate the target scene while remaining poorly parameterized for further optimization. We identify this failure mode as \emph{parameterization degeneration}: high-opacity floaters attenuate gradients to true surfaces through alpha compositing, and redundant overlapping clusters create strongly coupled parameter blocks with nearly collinear Jacobian responses. These effects explain why continued optimization can plateau even when the model still contains removable artifacts. We propose ReorgGS, an equivalent distribution reorganization method for converged 3DGS models. ReorgGS treats the existing Gaussian set as an empirical probability field, resamples centers from it, estimates local anisotropic covariances with kNN, initializes low opacity, and continues optimization with the original 3DGS renderer and loss. Unlike opacity reset, which only rescales opacity on the old overlap graph, ReorgGS rebuilds centers, covariances, and visibility structure, thereby changing the graph itself. Our analysis shows that distributional equivalence is not optimization equivalence. The reorganized model preserves scene support while improving gradient accessibility under alpha compositing and reducing opacity-weighted overlap, thereby weakening local parameter coupling during subsequent optimization. Under the same additional optimization budget, ReorgGS improves fitting quality at a fixed Gaussian count, suppresses persistent floaters, and reduces rendering overhead from redundant overlap.

  </details>


- **[VkSplat: High-Performance 3DGS Training in Vulkan Compute](https://arxiv.org/abs/2605.00219)**  
  *Jingxiang Chen, Mohamed Ibrahim, Yang Liu*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00219) · [pdf](https://arxiv.org/pdf/2605.00219.pdf)
  > 💡 使用Vulkan计算管线优化3DGS训练，实现3.3倍加速和33%显存降低，并兼容多厂商GPU。

  <details><summary>Abstract</summary>

  We present VkSplat, a high-performance, cross-vendor 3D Gaussian Splatting (3DGS) training pipeline implemented fully in Vulkan compute, addressing performance and compatibility limitation of existing training pipelines. With various optimizations, we achieve $3.3\times$ speed and $33\%$ VRAM reduction over CUDA+PyTorch baseline, maintaining quality, and demonstrating compatibility across GPU vendors. To the best of our knowledge, this is the first fully-Vulkan-based 3DGS training pipeline that achieves state-of-the-art performance. Code: \href{https://github.com/harry7557558/vksplat}{https://github.com/harry7557558/vksplat}

  </details>


- **[GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds](https://arxiv.org/abs/2604.20155)**  
  *Ao Gao, Jingyu Gong, Xin Tan, Zhizhong Zhang, Lizhuang Ma, Yuan Xie*  
  `2026-04-22` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20155) · [pdf](https://arxiv.org/pdf/2604.20155.pdf)
  > 💡 提出无蒸馏插件GSCompleter，以生成-注册替代修复-蒸馏，实现快速度量感知的3DGS补全，提升质量和效率。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized high-fidelity neural rendering with its explicit representation and efficiency. However, reconstructing scenes from sparse viewpoints suffers from severe geometric voids and floaters due to limited coverage. Current scene completion methods typically rely on an iterative "Repair-then-Distill" paradigm, which is computationally intensive, prone to unstable optimization, and susceptible to overfitting. To address these limitations, we propose GSCompleter, a distillation-free plugin that shifts scene completion to a stable "Generate-then-Register" workflow. Specifically, GSCompleter synthesizes visually plausible 2D reference images and explicitly lifts them into 3D Gaussian primitives with a consistent metric scale via a robust Stereo-Anchor View Selection mechanism. These newly generated primitives are then seamlessly integrated into the global scene using a novel Ray-Constrained Registration strategy. By replacing unstable distillation with rapid geometric registration, GSCompleter exhibits superior 3DGS completion performance across three benchmarks, enhancing both quality and efficiency over various baselines and achieving new state-of-the-art (SOTA) results.

  </details>


- **[GeGS-PCR: Effective and Robust 3D Point Cloud Registration with Two-Stage Color-Enhanced Geometric-3DGS Fusion](https://arxiv.org/abs/2604.17721)**  
  *Jiayi Tian, Haiduo Huang, Tian Xia, Wenzhe Zhao, Pengju Ren*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17721) · [pdf](https://arxiv.org/pdf/2604.17721.pdf)
  > 💡 针对低重叠点云注册难题，融合几何、颜色

  <details><summary>Abstract</summary>

  We address the challenge of point cloud registration using color information, where traditional methods relying solely on geometric features often struggle in low-overlap and incomplete scenarios. To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration. Our approach incorporates a dedicated color encoder that enhances color features by extracting multi-level geometric and color data from the original point cloud. We introduce the \textbf{Ge}ometric-3D\textbf{GS} module, which encodes the local neighborhood information of colored superpoints to ensure a globally invariant geometric-color context. Leveraging LORA optimization, we maintain high performance while preserving the expressiveness of 3DGS. Additionally, fast differentiable rendering is utilized to refine the registration process, leading to improved convergence. To further enhance performance, we propose a joint photometric loss that exploits both geometric and color features. This enables strong performance in challenging conditions with extremely low point cloud overlap. We validate our method by colorizing the Kitti dataset as ColorKitti and testing on both Color3DMatch and Color3DLoMatch datasets. Our method achieves state-of-the-art performance with \textit{Registration Recall} at 99.9\%, \textit{Relative Rotation Error} as low as 0.013, and \textit{Relative Translation Error} as low as 0.024, improving precision by at least a factor of 2.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
