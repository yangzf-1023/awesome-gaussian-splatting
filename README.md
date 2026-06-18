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
| 1 | **Survey & Benchmark** | 62 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 242 | **+4** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 31 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 49 | **+3** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 23 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 32 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 39 | **+2** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 12 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 14 | **+1** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 4 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 14 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 23 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | **+2** | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-18 (UTC) — 13 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (4) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos](https://arxiv.org/abs/2606.19156)**  
  *Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon*  
  `2026-06-17` · `cs.CV` · [abs](https://arxiv.org/abs/2606.19156) · [pdf](https://arxiv.org/pdf/2606.19156.pdf)
  > 💡 首个前馈框架通过网格引导和时间卷积从第一视角视频重建动态4D手部，实现快速推理与强泛化。

  <details><summary>Abstract</summary>

  Dynamic 3D hand reconstruction from egocentric videos is essential for next-generation computing platforms such as AR/VR and AI glasses. Despite its importance, most prior works focus either on multi-view 3D hand reconstruction or on 4D human body reconstruction. Egocentric 4D hand reconstruction remains challenging due to fast head motion, rapid hand dynamics, severe occlusions, and inherent ambiguity from single-view observations. To address these challenges, we introduce Hand-4DGS, the first feed-forward framework for reconstructing dynamic 4D hands directly from egocentric videos, enabling both fast (~60 FPS) inference and strong generalization. Our approach incorporates a mesh-guided representation for structural priors and temporal convolutions to model dynamic motion. We evaluate our framework on two challenging egocentric datasets, H2O and ARCTIC, and demonstrate significant improvements over baselines. Our method benefits from the generalization capability of feed-forward networks and effective 2D image supervision through Gaussian splatting, without requiring expensive 3D hand pose ground-truth annotations.

  </details>


- **[Intrinsic 4D Gaussian Segmentation from Scene Cues](https://arxiv.org/abs/2606.18623)**  
  *Hasan Yazar, Mohamed Rayan Barhdadi, Erchin Serpedin, Mehmet Tuncel, Hasan Kurban*  
  `2026-06-17` · `cs.CV` · [abs](https://arxiv.org/abs/2606.18623) · [pdf](https://arxiv.org/pdf/2606.18623.pdf)
  > 💡 利用高斯原语自身的外观、形变轨迹等线索构建亲和图并进行社区检测，实现无需掩码和训练的4D高斯分割，速度提升12.5倍且精度与监督方法相当。

  <details><summary>Abstract</summary>

  Dynamic 4D Gaussian Splatting reconstructs deforming scenes with high fidelity and is increasingly adopted as a representation for dynamic 3D scenes. Putting such a scene to use, for editing, manipulation or motion analysis, first requires segmenting it: grouping the Gaussian primitives into coherent objects. Current pipelines obtain this grouping by importing 2D masks from foundation models such as SAM and lifting or distilling them into the Gaussian representation. In dynamic scenes these masks must be generated across many frames and views, which is costly, and the resulting segmentation can depend strongly on the quality and consistency of those external masks. We ask how much object-level structure can instead be recovered from the Gaussians themselves, and propose Intrinsic-GS, a training-free, mask-free method that builds a sparse affinity graph over Gaussian primitives from appearance, orientation, scale, deformation-trajectory and non-learned rendered-boundary cues. The graph is partitioned with Leiden community detection, requiring no foundation model and no learned feature field. On the standard 4D Gaussian segmentation benchmarks, Neu3D and HyperNeRF, Intrinsic-GS recovers substantial object structure without mask supervision, reaching 0.746 mIoU on Neu3D and 0.575 on HyperNeRF; on Neu3D, a geometry-only variant reaches 0.902 mIoU, matching SAM-supervised TRASE. On HyperNeRF, Intrinsic-GS runs 12.5x faster than the mask-generation and feature-rendering stages used by mask-supervised pipelines. These results suggest that much of the segmentation signal is already encoded in the Gaussians themselves, offering a fast, mask-free direction for 3D and 4D Gaussian segmentation that may also point toward more generalizable, robust segmentation in settings where external masks are unreliable or expensive.

  </details>


- **[Edit3DGS: Unified Framework for Dynamic Head Editing via 2D Instruction-Guided Diffusion and 3D Gaussian Splatting](https://arxiv.org/abs/2606.17432)**  
  *Duy-Dat Tran, Trung-Nghia Le*  
  `2026-06-16` · `cs.GR` · [abs](https://arxiv.org/abs/2606.17432) · [pdf](https://arxiv.org/pdf/2606.17432.pdf)
  > 💡 利用2D指令扩散与3D高斯泼溅，实现动态头部编辑的统一框架，支持时域一致的高保真编辑。

  <details><summary>Abstract</summary>

  We present Edit3DGS, a unified framework for dynamic 3D head editing that integrates 2D instruction-guided diffusion with 3D Gaussian splatting. Unlike prior approaches that separately address frame-based edits or static 3D reconstruction, our method couples semantic controllability in the image domain with photorealistic, temporally consistent 3D representations. Given an input video, editable facial regions are masked and modified using a text-conditioned diffusion model to support fine-grained operations such as expression transformation, attribute modification, and appearance refinement. The edited frames are then aggregated through 3D Gaussian splatting to produce a coherent, high-fidelity avatar that preserves both identity and motion dynamics. To enforce consistency, Edit3DGS incorporates multi-view batch editing and lightweight inpainting strategies that recover lost expressions across timesteps. Experimental results demonstrate that our framework enables controllable, artifact-free head editing with smooth temporal transitions, offering practical applications in virtual avatars, immersive communication, film production, and interactive media.

  </details>


- **[Renderable Partial Representations for Dynamic Gaussian Splatting under Incomplete Delivery](https://arxiv.org/abs/2606.17212)**  
  *Faruk Alpay, Levent Sarioglu, Yaser Hadri*  
  `2026-06-15` · `cs.GR` · [abs](https://arxiv.org/abs/2606.17212) · [pdf](https://arxiv.org/pdf/2606.17212.pdf)
  > 💡 动态高斯溅射面临部分传输不可渲染问题，提出时空聚类与反事实效用层优化可渲染部分表示，显著改善质量退化。

  <details><summary>Abstract</summary>

  Dynamic Gaussian compression is normally optimized for complete files or complete progressive prefixes, but interactive rendering encounters partial representations: some spatiotemporal regions are present, others missing, and late refinements cannot affect the displayed frame. We study dynamic Gaussian representations whose incomplete delivery states remain directly renderable and whose degradation is optimized in image space. Gaussian primitives are organized into independently addressable spatiotemporal clusters with a base level and three refinements; training samples partial dependency graphs, renders many counterfactual states in one GPU batch, and minimizes expected distortion, tail distortion, temporal inconsistency, rate, and prefix regressions. A counterfactual utility layer measures the marginal render contribution of each completion group across valid receiver contexts. The same graph admits a concrete delivery realization with MTU-bounded entropy-coded chunks, deadline-aware scheduling, and receiver-side dependency closure. On held-out views, the finest refinement has negative mean marginal utility in 3/32 D-NeRF bouncingballs, 49/64 HyperNeRF broom2, and 28/64 HyperNeRF chicken clusters; its lower-tail utility is negative in 21/32, 61/64, and 42/64 clusters, respectively. On broom2, render-utility ordering removes both PSNR regressions produced by nominal layer order at matched byte budgets; on chicken, utilities measured on disjoint training cameras improve held-out PSNR by 3.03 dB at the lowest matched budget. These scoped results show why nominal refinement order cannot substitute for render-conditioned utility: the formulation treats network delivery as a distribution over renderable scene states rather than as an external wrapper around a graphics codec.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement](https://arxiv.org/abs/2606.17998)**  
  *Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17998) · [pdf](https://arxiv.org/pdf/2606.17998.pdf)
  > 💡 针对低光增强中光照建模与效率瓶颈，提出基于2D

  <details><summary>Abstract</summary>

  Existing low-light image enhancement methods often face a bottleneck between the representation capacity of illumination-field modeling and computational complexity. To address this issue, this paper proposes an Adaptive Illumination Gaussian Splatting Network (AIGS-Net), an ultra-lightweight architecture for fast low-light enhancement. Unlike conventional static priors, AIGS-Net constructs an input-adaptive 2D Gaussian Splatting illumination field. The opacity of Gaussian basis functions is dynamically modulated by relative luminance statistics of the input image, and spatially varying illumination compensation is rendered through ordered alpha compositing. To guide adaptive illumination compensation efficiently, a zero-parameter nonlinear multiscale contextual encoding module is introduced to extract low-frequency structures and local contrast cues without additional convolutional weights. To suppress noise amplification and sensor-induced color bias, AIGS-Net integrates noise-mask estimation, locked single-channel Gamma mapping, cross-channel consistency regularization, and target color-alignment constraints. Experiments on LOL and LSRW benchmarks show that AIGS-Net improves detail recovery and color fidelity while requiring only approximately 40 learnable parameters, achieving an effective trade-off between enhancement quality and extreme inference efficiency.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (3) · <a href="topics/generation.md">full list →</a></summary>

- **[FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity](https://arxiv.org/abs/2606.19019)**  
  *Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer*  
  `2026-06-17` · `cs.CV` · [abs](https://arxiv.org/abs/2606.19019) · [pdf](https://arxiv.org/pdf/2606.19019.pdf)
  > 💡 针对稀疏视图重建中生成先验与观测一致性矛盾，提出双空间引导流匹配和3DGS细化，实现高

  <details><summary>Abstract</summary>

  Recovering complete 3D representations of objects from few casual image captures remains a significant challenge. Recent 3D generative models, particularly those based on Flow-Matching (FM), can synthesize high-quality textured assets; however, they often suffer from ''synthetic bias'' where learned priors override observational evidence, alongside a lack of alignment with the observed instance. Conversely, optimization-based methods like 3D Gaussian Splatting (3DGS) provide high fidelity on visible surfaces but fail to reason about unobserved geometry. In this paper, we present FlowObject, a framework that reformulates sparse-view 3D reconstruction as a training-free, guided inverse problem. Our approach applies a dual-space guidance strategy to steer the Ordinary Differential Equation (ODE) trajectory of a flow-matching model, enabling the completion of unseen regions through learned generative priors while enforcing strict consistency with real-world observations. By integrating a 3DGS refinement stage, FlowObject further bridges the gap between ''synthetic-looking'' generative outputs and photorealistic reconstructions. Comprehensive benchmarks on synthetic and real-world datasets demonstrate that current state-of-the-art methods often struggle to achieve geometric completeness and observational consistency simultaneously, especially under severe occlusions. In contrast, our method significantly outperforms state-of-the-art generative models and optimization-based frameworks in both geometric completeness and view-dependent appearance fidelity.

  </details>


- **[Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734)**  
  *Ye Xue, Yiheng Wang, Xinhua Shao, Qi Yan, Shutao Zhang, Tsung-Hui Chang*  
  `2026-06-17` · `eess.SP` · [abs](https://arxiv.org/abs/2606.18734) · [pdf](https://arxiv.org/pdf/2606.18734.pdf)
  > 💡 用切线高斯泼溅外推无线信道角度功率谱，结合点云几何实现未测量网格的准确预测，性能更优。

  <details><summary>Abstract</summary>

  Accurate, site-specific channel information is crucial for optimizing next-generation wireless networks. Among various approaches, localized statistical channel modeling (LSCM), which models the channel multipath angular power spectrum (APS) from the reference signal received power (RSRP) measurement, has emerged as a state-of-the-art method tailored for efficient network optimization. However, despite its effectiveness, LSCM cannot predict APS at the vast majority of locations where no measurements are available, which significantly restricts its applicability in large-scale, real-world scenarios. To address this challenge, we present \emph{point-cloud-assisted tangent Gaussian splatting} (PC-TGS), the first framework to \emph{extrapolate} APS to unmeasured outdoor grids by integrating sparse radio measurements with dense LiDAR-based geometry. PC-TGS represents environmental scatterers as anisotropic 3D Gaussians, initialized and refined through a relaxed-mean reparameterization of the raw point cloud. A tangent-plane projection accurately maps each Gaussian into the local angular domain, while a depth-aware electromagnetic splatting process aggregates their contributions. To ensure practical deployment, we derive a closed-form Gaussian-weighted average (GWA) for APS bin integration and provide a provable error bound. { Evaluations on a LiDAR-scanned city-scale dataset (5M points, 6,310 RSRP samples) demonstrate that PC-TGS achieves better APS and RSRP prediction performance compared to state-of-the-art baselines and faster inference time for APS extrapolation task. These results highlight the potential of PC-TGS to enable geometry-aware and data-efficient channel prediction in large-scale wireless digital twins.

  </details>


- **[GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments](https://arxiv.org/abs/2606.17520)**  
  *Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang*  
  `2026-06-16` · `cs.RO` · [abs](https://arxiv.org/abs/2606.17520) · [pdf](https://arxiv.org/pdf/2606.17520.pdf)
  > 💡 提出基于3DGS的自动化系统GASE，利用全景相机阵列和位姿策略高效构建仿真环境，分割精度提升10%以上并实现最优修补。

  <details><summary>Abstract</summary>

  Training embodied agents in the real world requires skilled operators and expensive hardware. Simulation environments offer a compelling alternative by enabling large-scale, cost-effective data augmentation. Consequently, rapidly constructing high-fidelity simulation scenes with a minimal sim-to-real gap has become a critical objective in robot learning. While reconstruction-based methods provide superior visual quality, current workflows are hindered by inefficient data acquisition and subpar foreground object extraction. We thus propose GASE, a highly automated system for simulation scene construction. GASE leverages multi-view video streams from panoramic camera arrays to enable rapid environment scanning. To ensure high-quality asset generation, our pipeline introduces a camera-pose-based strategy that robustly extracts objects across frames in the 2D domain, followed by high-fidelity scene inpainting. Foreground objects and the static background are then reconstructed independently and seamlessly imported into physics simulators for policy training. Extensive experiments demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation accuracy by over 10\% while achieving state-of-the-art inpainting quality. Furthermore, real-robot deployments across manipulation and navigation tasks maintains a performance gap of less than 10\% compared to policies trained purely on real-world data. These results confirm that GASE provides an efficient and highly effective solution for bridging the sim-to-real gap. Code will be released.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (2) · <a href="topics/rendering.md">full list →</a></summary>

- **[Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale Scene Reconstruction via Pixel-level Communication](https://arxiv.org/abs/2606.18588)**  
  *Wenqi Jia, Zhewen Hu, Ying Huang, Yu Gong, Stavros Kalafatis, Yuke Wang, Wei Niu, Chengming Zhang, Ang Li, Sheng Di, Yuede Ji, Bo Fang, Miao Yin*  
  `2026-06-17` · `cs.DC` · [abs](https://arxiv.org/abs/2606.18588) · [pdf](https://arxiv.org/pdf/2606.18588.pdf)
  > 💡 分布式训练3DGS通信成本高，提出Splaxel，通过像素级局部渲染与全局组合减少交换，实现7.6倍加速并保持高质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables high-fidelity and real-time 3D scene reconstruction, but scaling training to large-scale scenes requires optimizing hundreds of millions of Gaussians across multiple GPUs. Existing distributed approaches either partition scenes into isolated regions, causing global inconsistency, or rely on global Gaussian-level exchanges, which lead to substantial growth in inter-GPU communication and quickly dominate iteration time. We propose Splaxel, a communication-efficient distributed 3DGS training framework based on pixel-level local rendering and global composition. Instead of synchronizing Gaussians, each GPU renders its local subset and exchanges only partial pixel values, maintaining mathematical consistency while keeping communication cost stable as the scene size increases. Splaxel further reduces pixel-level redundancy through geometric and transmittance visibility prediction and improves GPU utilization via conflict-free camera-view consolidation. Evaluated on large-scale datasets with up to 120M Gaussians, Splaxel achieves up to 7.6$\times$ speedup over the state-of-the-art distributed 3DGS framework while preserving high reconstruction quality.

  </details>


- **[MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization](https://arxiv.org/abs/2606.17935)**  
  *Guo Pu, Yixuan Han, Haofeng Li, Yao Zhang, Hui Zhou, Zhouhui Lian*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17935) · [pdf](https://arxiv.org/pdf/2606.17935.pdf)
  > 💡 通过全局Sim(3)优化和颜色残差学习，实现鲁棒高效的在线单目体素化3DGS重建，提升姿态精度与渲染质量。

  <details><summary>Abstract</summary>

  Online 3D reconstruction from monocular image sequences is a challenging and ongoing research topic. 3D Gaussian Splatting (3DGS), leveraging its high-quality real-time rendering capability, empowers online 3D reconstruction to represent dense scenes with enhanced expressiveness, and thus holds great promise for a wide range of applications such as robotics and AR/VR. However, existing online 3DGS methods still suffer from some key challenges: fragile camera pose estimation due to the lack of global optimization, and low optimization efficiency in large-scale or long-sequence scenarios. To address these issues, we propose a robust and efficient online voxelized 3DGS reconstruction framework integrated with global $\text{Sim}(3)$ optimization, which enables reliable camera tracking and efficient global loop closure for both camera poses and voxelized 3DGS. To accelerate the convergence of the voxelized 3DGS, we further introduce a color residual learning strategy, which not only boosts optimization speed but also enhances rendering quality. Extensive experiments on diverse indoor and outdoor datasets demonstrate that our method achieves state-of-the-art performance in both camera pose estimation accuracy and rendering quality, while retaining real-time efficiency. Additionally, we develop and deploy a real-world UAV-based active reconstruction system grounded on our proposed method, validating its robustness and generalizability for practical online 3D reconstruction tasks. Our code and data are available at https://github.com/TrickyGo/MoonSplat.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (1) · <a href="topics/driving.md">full list →</a></summary>

- **[TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations](https://arxiv.org/abs/2606.17386)**  
  *Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17386) · [pdf](https://arxiv.org/pdf/2606.17386.pdf)
  > 💡 提出无需专家演示的端到端驾驶方法，通过自对弈预训练与视觉骨干对齐，降低采集和渲染成本并达到SOTA。

  <details><summary>Abstract</summary>

  End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all stages: collecting and labeling millions of driving frames is costly, and closed-loop RL on images is bottlenecked by the per-step cost of photorealistic rendering plus a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: millions of rollout steps per second, and a state distribution naturally rich in collisions, near-misses, and recoveries that no driving log contains. Our approach exploits this asymmetry by decoupling learning to drive from learning to see. We pretrain a single policy by self-play, then align its latent space with a pretrained vision backbone, through the action KL divergence and a batch-relational low-rank structural loss. The action target comes from the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. On photorealistic 3D Gaussian splatting closed-loop scenarios, the resulting end-to-end policy matches or exceeds prior end-to-end methods.

  </details>


</details>

<details><summary><b>Others</b> (2) · <a href="topics/others.md">full list →</a></summary>

- **[Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement](https://arxiv.org/abs/2606.17985)**  
  *Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17985) · [pdf](https://arxiv.org/pdf/2606.17985.pdf)
  > 💡 针对非均匀光照下曝光失衡与色偏问题，提出高斯光场散射驱动的视觉Transformer，用各向异性高斯基嵌入物理先验，实现SOTA无监督

  <details><summary>Abstract</summary>

  Existing unsupervised low-light image enhancement methods often encounter local exposure imbalance and color distortion under complex non-uniform illumination. In addition, most Vision Transformers lack an explicit mechanism for modeling the physical priors of illumination degradation. To address these limitations, we propose GLFS, a Gaussian light field splatting-based Vision Transformer that integrates continuous physical illumination modeling from Gaussian splatting into the Transformer architecture. In GLFS, scene illumination is represented by a superposition of anisotropic Gaussian basis functions. Physics-guided biases are introduced into self-attention to adaptively infer a spatial gain field, enabling accurate and uniform restoration under complex illumination. To reduce color bias and structural degradation during enhancement, a color-vector angular loss and a luminance-edge loss are further developed. These losses enforce hue consistency and improve the structural fidelity of local details. Extensive ablation studies and quantitative evaluations show that GLFS provides clear advantages in illumination correction and detail preservation. It achieves state-of-the-art performance and offers a new representation paradigm for low-light image enhancement.

  </details>


- **[GSPan: A Continuous Gaussian Primitive Representation for Arbitrary-Scale Pansharpening](https://arxiv.org/abs/2606.17722)**  
  *Fangyi Li, Xiaoyuan Yang, Yixiao Li, Zongyang Sui, Kangqing Shen, Gemine Vivone*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17722) · [pdf](https://arxiv.org/pdf/2606.17722.pdf)
  > 💡 提出用二维高斯溅射连续表示残差细节，结合双流层次交互与空间-光谱注意力，实现无需重训的任意尺度全色锐化并加速推理。

  <details><summary>Abstract</summary>

  Pansharpening aims to generate high-resolution multispectral (HRMS) images by fusing low-resolution multispectral (LRMS) and panchromatic (PAN) observations. Most existing deep learning methods treat pansharpening as fixed-grid prediction, which limits scale adaptation. To address this, we propose GSPan, a framework that introduces 2D Gaussian Splatting (GS) into pansharpening. Instead of directly predicting pixels, GSPan represents band-wise residual details as continuous and learnable 2D Gaussian primitives. We design a Dual-Stream Hierarchical Interaction (DSHI) architecture with a Spatial-Spectral Interactive Attention (SSIA) module to estimate these primitives from complementary PAN and MS observations. The predicted primitives are rendered as a residual detail field and injected into the upsampled MS image. This continuous representation allows GSPan to render fused images on arbitrary target sampling grids without scale-specific retraining. It further enables a Scale-Decoupled Asymmetric Inference (SDAI) strategy, which estimates primitives at a reduced resolution and renders the fused image at the target resolution for efficient large-scene pansharpening. Experiments on QuickBird, GaoFen-2, WorldView-3, and WorldView-3-4K datasets show that GSPan delivers state-of-the-art fusion performance. Moreover, SDAI markedly accelerates inference, achieving a favorable trade-off between computational efficiency and fusion quality. Our results demonstrate the potential of continuous Gaussian residual representations as a flexible and scale-decoupled alternative to fixed-grid prediction.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
