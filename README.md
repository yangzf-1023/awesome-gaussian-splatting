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
| 1 | **Survey & Benchmark** | 80 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 278 | **+1** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 43 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 69 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 37 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 38 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 57 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 17 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 8 | **+1** | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 23 | **+3** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 27 | **+1** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 10 | **+1** | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-14 (UTC) — 11 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (1) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Grassmannian Splatting I: Moving rank-2 Spacetime Surfels for Dynamic Scene Rendering](https://arxiv.org/abs/2607.10489)**  
  *Aaron Maurice Berman, Shantanu Dave*  
  `2026-07-11` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10489) · [pdf](https://arxiv.org/pdf/2607.10489.pdf)
  > 💡 用Grassmannian流形参数化秩2时空表面元，实现闭式运动，无需变形场

  <details><summary>Abstract</summary>

  We introduce Grassmannian splatting, a dynamic scene representation whose primitives are Gaussians supported on 3-planes in spacetime $\R^4$: generically, spatial 2-planes in uniform translation along their normals. Each primitive carries a unit normal $n \in \mathbb S^3/\{\pm 1\} \cong \mathrm{Gr}(3,4)$ and an unconstrained factor $L \in \mathbb R^{4 \times 3}$, with covariance \[ Σ_{4\mathrm{D}} = (P_n L)(P_n L)^T, \qquad P_n = I - n n^T. \] For generic $L$ and $n \neq \pm e_0$, conditioning on time returns a rank-2 surfel at every frame. The normal of the disk and its velocity along that normal are read off from $n$; the disk shape and the tangential drift of its center are set by $L$. Existing native 4D Gaussian splatting methods [\it{Yang et. al. 2023,Duan et. al. 2024}] slice full-rank spacetime covariances, so their per-frame primitive is a volumetric ellipsoid; since conditioning lowers rank by exactly one, a rank-2 surfel in the slice requires a rank-3 spacetime covariance, and the parameterization above realizes exactly these. The motion model is closed form, i.e. no deformation field is learned, and no custom CUDA is required: the conditioned disk feeds a standard 3DGS rasterizer through its precomputed-covariance interface. A soft clamp in the Schur denominator regularizes the static orientation and continuously bridges rank-3 static and rank-2 dynamic behavior, so static and moving primitives form a single continuous family. On the 17 HyperNeRF scenes of MonoDyGauBench, training is fastest among all compared methods (4.9 to 5.6 times faster than the strongest quality baselines), while ranking second in PSNR, MS-SSIM, and LPIPS. Code: https://github.com/PaulCelanCoding/grassmannian-splatting

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[SyncSpace: Layout-Conditioned 3D Gaussian Splatting for Space Reskinning in Mixed Reality](https://arxiv.org/abs/2607.10050)**  
  *Qinchuan Zhang, Weibo Xu, Yunge Wen*  
  `2026-07-11` · `cs.HC` · [abs](https://arxiv.org/abs/2607.10050) · [pdf](https://arxiv.org/pdf/2607.10050.pdf)
  > 💡 先提取布局几何先验生成3DGS场景，再配准到物理空间，实现混合现实中布局保留的多风格空间重绘。

  <details><summary>Abstract</summary>

  We present SyncSpace, a system that achieves both spatial alignment and visual consistency between a generated 3DGS world and physical space. We first scan the space via depth sensing to extract 3D bounding boxes, which we render into a layout-only panorama and feed as a geometric prior to a generative world model, producing a Gaussian splat scene in which objects are re-semantized to fit a target style without per-object control. We then align the generated scene to physical space with a coarse-to-fine registration algorithm, refined manually via pinch gestures when automatic registration does not converge. We demonstrate a hand-tracked engulfment interaction in which the virtual world rises to replace the physical space, and show a single space reskinned into multiple stylistically distinct worlds with its layout preserved.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673)**  
  *Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.11673) · [pdf](https://arxiv.org/pdf/2607.11673.pdf)
  > 💡 提出SGP统一多模态输入，通过全景视频生成与3DGS重建，实现从文本/图像/视频到高保真可探索3D世界。

  <details><summary>Abstract</summary>

  We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds. At the heart of our framework is a unified Spatial Generative Primitive (SGP), a compact tuple of a high-quality panorama and a spatial point cloud that delivers an efficient description of any 3D space. Multimodal inputs are first lifted into this primitive; a 3D-consistent panoramic video generator then explores the primitive along a planned trajectory; finally, our panoramic video reconstruction engine converts the generated video into a clean, photorealistic 3D Gaussian Splatting (3DGS) world. This pipeline covers two regimes: rich inputs (multi-view sets, casual video) are lifted into the SGP through a geometry-rigorous recovery that mirrors the observed scene, while a single image or sentence is completed generatively into a creative world. The result is one low-barrier engine for general 3D content creation that further anchors generated worlds to geographic points of interest, enabling map-native spatial exploration at consumer scale. Experiments show that ABot-3DWorld 0 sets the state of the art among open-source methods and demonstrates stronger scene fidelity than Marble under rich multimodal inputs.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[CoSAG: Compact Semantic Anchor Gaussians via Training-Free Rate-Distortion Coding](https://arxiv.org/abs/2607.10237)**  
  *Yuang Jia, Jinlong Wang, Junhong Lin, Ruiting Dai, Wei Gao*  
  `2026-07-11` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10237) · [pdf](https://arxiv.org/pdf/2607.10237.pdf)
  > 💡 通过空间锚点与无训练率失真编码压缩开放词汇3D高斯场，存储减少37-76倍且精度更优

  <details><summary>Abstract</summary>

  Open-vocabulary 3D scene understanding is commonly achieved by embedding 2D vision-language features such as CLIP into a 3D Gaussian Splatting scene, turning it into a text-queryable semantic field. However, attaching a high-dimensional feature to each of millions of Gaussians inflates a single scene to gigabytes, which makes storage and deployment the real bottleneck of these fields. Existing compact methods each learn and ship a per-scene codec, an autoencoder, a quantized codebook, or a distilled feature field, entangling field construction with field storage and never compressing the per-Gaussian assignment that holds the bulk of the cost. We argue that construction and storage should be decoupled, and that storage is a rate-distortion problem over the per-Gaussian binding to a small anchor table, a structure no prior open-vocabulary method compresses. We present CoSAG, which constructs the field without any per-scene training through a closed-form transmittance-weighted lift, spatially grounded semantic anchors, and multi-view denoising, and stores it with a spatially predictive entropy coder that ships no decoder. Because the anchors are spatially grounded, the binding is predictable and therefore highly compressible. The transmittance-weighted lift and multi-view denoising yield a clean, view-consistent assignment, so the entropy coder spends almost no rate on correcting noise and instead codes only the residual against its spatial prediction. CoSAG reaches sub-megabyte storage while matching or exceeding the state of the art across the 2D-rendered, 3D-selection, and dense-LSeg protocols, reducing field size by 37 to 76x relative to LangSplatV2 at higher accuracy.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](https://arxiv.org/abs/2607.11184)**  
  *Ruilan Gao, Letian Jin, Yu Zhang*  
  `2026-07-13` · `cs.RO` · [abs](https://arxiv.org/abs/2607.11184) · [pdf](https://arxiv.org/pdf/2607.11184.pdf)
  > 💡 针对单目重建，结合高斯泼溅与几何先验，通过采样原语和联合优化实现高精度实时SL

  <details><summary>Abstract</summary>

  SLAM methods based on 3D Gaussian Splatting (3DGS) have demonstrated impressive tracking and mapping performance, but typically require additional geometric information from external depth sensors. Meanwhile, recent SLAM systems that leverage geometric priors from pre-trained feed-forward models enable real-time dense reconstruction, yet often discard original RGB information during optimization, thus degrading overall reconstruction quality. We present GeoGS-SLAM, an online monocular dense reconstruction system that combines the 3DGS-based map representation with learned geometric priors. Given uncalibrated RGB input, we first employ a feed-forward visual geometry model to predict camera and scene priors. The Gaussian scene map is then expanded by directly sampling Gaussian primitives from both RGB input and geometric priors. Camera poses and the scene map are jointly optimized through a coarse-to-fine strategy that minimizes both photometric and geometric losses. To ensure global consistency, we further incorporate online loop closure detection and pose graph optimization. Extensive experiments across indoor and outdoor benchmarks demonstrate that GeoGS-SLAM achieves superior rendering quality and tracking accuracy compared to state-of-the-art methods while maintaining online real-time performance. Project page: https://rlgao.github.io/geogs_slam.

  </details>


</details>

<details><summary><b>Relighting / Material / BRDF</b> (1) · <a href="topics/relighting.md">full list →</a></summary>

- **[SalientGS: Unified SfM-to-3DGS with Importance-Guided MCMC Gaussian Allocation](https://arxiv.org/abs/2607.11285)**  
  *Tianyu Xiong, Rui Li, Suning Ge, Jiaqi Yang*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.11285) · [pdf](https://arxiv.org/pdf/2607.11285.pdf)
  > 💡 提出统一SfM到3DGS流水线，用重要性引导MCMC高斯分配重新分配容量到欠拟合区域，实现快速高质量重建。

  <details><summary>Abstract</summary>

  Reconstructing 3D scenes from unordered images remains bottlenecked by expensive Structure-from-Motion (SfM) preprocessing and frozen pose interfaces. We present SalientGS, a unified SfM-to-3D Gaussian Splatting (3DGS) pipeline. Its central contribution is importance-guided Markov Chain Monte Carlo (MCMC) Gaussian allocation, which aggregates multi-view residuals into per-Gaussian underfit and redundancy signals. These signals define a smooth importance-weighted sampling distribution that biases both birth and relocation toward underfit regions. This reallocates capacity from well-fit areas without altering the underlying stochastic gradient Langevin dynamics (SGLD). SalientGS achieves end-to-end reconstruction in 15 minutes with state-of-the-art perceptual quality. The supplementary material provides dedicated sections for Per-Scene Qualitative Comparisons and Per-Image Learned Perceptual Image Patch Similarity (LPIPS) Analysis, including failure cases. Code and evaluation scripts are available at https://github.com/Six-Bit-TX/SalientGS.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (3) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[HyperGS: Fast and Generalizable Gaussian Video Representation](https://arxiv.org/abs/2607.11500)**  
  *Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.11500) · [pdf](https://arxiv.org/pdf/2607.11500.pdf)
  > 💡 现有高斯视频表示依赖逐视频优化，HyperGS用分解时空Transformer和前馈预测实现零样本泛化，编码速度提升数万倍。

  <details><summary>Abstract</summary>

  Gaussian Splatting has emerged as an effective representation for video, but existing methods rely on per-video optimization. This leads to slow encoding and limits generalization across videos. To amortize this optimization, we propose HyperGS, a feedforward, optimization-free approach that directly predicts Gaussian representations from any video in a single forward pass, speeding up encoding and decoding by orders of magnitude while generalizing to out-of-distribution videos at higher resolutions. In HyperGS, we design a factorized spatiotemporal Transformer to extract tokens from video, and a learnable query-based Transformer to obtain 8-parameter Gaussian representations for each video frame. We find that naively predicting Gaussians across diverse videos induces a needle-like degeneration that collapses training, and address this with a rank-based geometric regularizer whose strength adapts dynamically to stabilize optimization. HyperGS achieves encoding at $10^4$--$10^5\times$ the speed of per-video Gaussian optimization at matched reconstruction quality while generalizing zero-shot to $720p$ video, enabling higher-resolution rendering without re-encoding. HyperGS improves PSNR by +2.9--3.1 dB over the prior video encoders on K400, SSv2, and UCF101 at a smaller video representation size. By predicting explicit 2D Gaussians in a single forward pass, HyperGS combines the fast, flexible rendering of Gaussian Splatting with the speed and generalization of feedforward prediction, advancing Gaussians as a practical direction for fast and generalizable video representation.

  </details>


- **[AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling](https://arxiv.org/abs/2607.10995)**  
  *Yingji Zhong, Dave Zhenyu Chen, Fuzhao Ou, Youyu Chen, Zhihao Li, Lanqing Hong, Dan Xu*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10995) · [pdf](https://arxiv.org/pdf/2607.10995.pdf)
  > 💡 针对长序列3DGS冗余计算，提出不对称架构解耦几何与外观，粗粒度几何与细粒度外观分支交互，大幅提升效率。

  <details><summary>Abstract</summary>

  Recent generalizable 3D Gaussian Splatting models have advanced long-sequence novel view synthesis (NVS), but at the cost of substantial redundant computation. We identify that the redundancy can be mitigated based on two observations: (i) high-precision geometry is not strictly required for high-quality NVS; (ii) appearance learning is generally easier than geometry recovery. Motivated by these insights, we propose an asymmetric architecture that decouples geometry and appearance modeling. The geometry branch processes coarse-grained tokens with most of the parameters for multi-view reconstruction, while the appearance branch operates on fine-grained tokens to capture details using significantly fewer parameters. The two branches interact through bilateral connections, enabling mutual guidance for their respective tasks. This task-aware asymmetry reduces the computational redundancy and allocates the computation more judiciously, thereby increasing parameter efficiency and enabling smaller models to achieve strong performance. On 32-view 960P inputs, our model matches optimization-based methods while delivering nearly 800x speedup, and surpasses the zero-shot performance of state-of-the-art generalizable models with markedly fewer parameters and reduced training/inference overhead, achieving an overall efficiency improvement.

  </details>


- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792)**  
  *Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia*  
  `2026-07-12` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10792) · [pdf](https://arxiv.org/pdf/2607.10792.pdf)
  > 💡 针对稀疏视图几何伪影，提出基于语义对应和多属性一致性损失的MAC-Splat框架，在ScanNet++上PSNR提升超4.5dB。

  <details><summary>Abstract</summary>

  Reconstructing high-fidelity 3D scenes from sparse-views remains a central problem in generalizable neural rendering. Existing generalizable 3D Gaussian Splatting (3DGS) methods often exhibit geometric artifacts in sparse-view settings, since supervision based solely on 2D photometric losses cannot resolve depth and correspondence ambiguities. To address this issue, we propose MAC-Splat, a training framework built around direct 3D consistency supervision. MAC-Splat builds on the MASt3R geometric backbone and a frozen DINOv3 encoder to obtain semantically informed 2D correspondences, which serve as geometric anchors for 3D supervision. Using these anchors, we define the Multi-Attribute Consistency (MAC) loss. This objective jointly regularizes the 3D attributes of matched Gaussians, including their position, shape, and appearance, by enforcing agreement in a common world coordinate frame. The formulation is robust to outliers and respects the geometry of covariance matrices, which leads to stable training under sparse-view conditions. Experiments on ScanNet++ show that MAC-Splat outperforms strong baselines, with particularly large gains under different overlap regimes. In particular, it improves average PSNR over Splatt3R by more than 4.5 dB, reduces LPIPS, and maintains performance as the camera pose gap increases. These results indicate that a direct, multi-attribute 3D consistency objective, when combined with high-quality correspondences, is effective for addressing the ill-posed sparse-view reconstruction problem.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (1) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[Incremental Online Scene Reconstruction by 3D Gaussian Triangulation](https://arxiv.org/abs/2607.10690)**  
  *Yanjin Zhu, Shaofan Liu, Jianke Zhu*  
  `2026-07-12` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10690) · [pdf](https://arxiv.org/pdf/2607.10690.pdf)
  > 💡 提出在线三角化3D高斯框架，直接提取网格并通过平面约束优化，实现高质量渲染与增量表面重建，降低存储开销。

  <details><summary>Abstract</summary>

  Incremental scene reconstruction is essential for real-world applications. Although 3D Gaussian Splatting shows strong potential, most existing approaches require offline conversion of the optimized Gaussians into an intermediate implicit field for explicit mesh extraction, which hinders seamless integration with downstream tasks. To address this limitation, we propose a novel online framework that incrementally reconstructs and updates high-fidelity explicit meshes by directly triangulating a dense geometric Gaussian representation, which supports both high-quality rendering and incremental surface reconstruction. Moreover, we present a direct meshing algorithm that efficiently extracts and updates the mesh from the Gaussian set. To ensure mesh accuracy, we enforce a plane-based pulling constraint that dynamically aligns 3D Gaussian primitives to the approximated local surface. Furthermore, our framework significantly reduces memory and computational overhead during long-sequence processing by dynamically freezing fully optimized historical regions. Experiments on public datasets demonstrate that our method outperforms conventional Gaussian-based methods on both rendering quality and reconstruction accuracy.

  </details>


</details>

<details><summary><b>Others</b> (1) · <a href="topics/others.md">full list →</a></summary>

- **[DP-Splat: Bayesian Nonparametric Complexity Control for Gaussian Splatting](https://arxiv.org/abs/2607.10912)**  
  *Aqi Dong*  
  `2026-07-12` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10912) · [pdf](https://arxiv.org/pdf/2607.10912.pdf)
  > 💡 用截断棍棒狄利克雷过程替代固定混合权重，实现高斯溅射组件数量自适应，理论保证单调性和截断误差，性能匹配且组件减少5.9-7.6倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting represents scenes as finite mixtures of anisotropic Gaussians whose number of components $K$ is set by heuristic density control or user caps. Variational Bayes Gaussian Splatting (VBGS) recast splat fitting as conjugate variational inference, but $K$ remains fixed. We replace the finite symmetric Dirichlet over mixture weights with a truncated stick-breaking Dirichlet-process prior -- and, as a theory-backed alternative, a sparse overfitted finite Dirichlet -- so that the number of occupied components adapts to the data while every update remains a closed-form coordinate-ascent step; a natural-gradient stochastic variant makes the per-step cost independent of the number of points. We give an exact monotonicity guarantee, a rigorous truncation-error bound correcting an anti-conservative large-$α$ approximation in common use, and an honest account of what the fitted number of components estimates. Empirically: (i) the effective complexity $\hat{K}$ adapts to scene complexity and recovers the true $K$ within $\pm 1$ on well-separated synthetic data with regime-appropriate concentration; (ii) a deconfounded comparison shows the DP prior's contribution is complexity selection, not per-component efficiency -- converged DP fits exceed single-pass fixed-$K$ VBGS by +2.7 dB at matched budgets yet tie an equally converged fixed-$K$ baseline, and on 3D scenes DP-Splat matches or exceeds VBGS's held-out color prediction with 5.9-7.6x fewer components; (iii) the posterior-predictive color variance is well calibrated on model-matched synthetic data; and (iv) the ordering suggested by exact-posterior asymptotics reverses under mean-field coordinate ascent: the DP prior resists over-splitting while the sparse finite mixture saturates its truncation, a gap between variational practice and posterior asymptotics documented across three orders of magnitude in $N$.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
