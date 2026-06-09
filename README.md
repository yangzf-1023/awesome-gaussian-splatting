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
| 1 | **Survey & Benchmark** | 58 | **+1** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 230 | **+1** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 30 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 45 | **+2** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 22 | **+2** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 32 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 34 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 10 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 12 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 2 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 13 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 21 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-09 (UTC) — 8 new paper(s)

<details><summary><b>Survey & Benchmark</b> (1) · <a href="topics/survey.md">full list →</a></summary>

- **[REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance](https://arxiv.org/abs/2606.09074)**  
  *Zhang Chen, Shuai Wan, Mengting Yu, Fuzheng Yang, Junhui Hou*  
  `2026-06-08` · `cs.CV` · [abs](https://arxiv.org/abs/2606.09074) · [pdf](https://arxiv.org/pdf/2606.09074.pdf)
  > 💡 针对3DGS剪枝效率低的问题，提出基于无渲染Hessian场的重要性度量，实现3000倍加速且保持

  <details><summary>Abstract</summary>

  Existing pruning methods for 3D Gaussian splatting (3DGS) suffer from either severe quality degradation or prohibitive computational overhead. In this paper, we propose REFINE, a highly accelerated 3DGS pruning framework centered on a novel rendering-free primitive importance metric. Our approach leverages an analytically approximated, rendering-aware Hessian field to quantify the expected perceptual error induced by the removal of individual primitives. By modeling the joint modulation of visibility, projection geometry and the content adaptive hyperparameter, we entirely bypass costly forward rendering passes and derive an anisotropic perceptual weight field that serves as a high-fidelity proxy for primitive importance. Extensive experiments across multiple benchmark datasets demonstrate that REFINE maintains highly competitive rendering quality while achieving an unprecedented $3,000\times$ reduction in pruning-related computational complexity compared to state-of-the-art pruning methods.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (1) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Liquid Neural Networks as a Drop-in Continuous-Time Deformation Field for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.07670)**  
  *Mingzhao Li, Arghya Pal, Guan Yuan Tan*  
  `2026-06-04` · `cs.CV` · [abs](https://arxiv.org/abs/2606.07670) · [pdf](https://arxiv.org/pdf/2606.07670.pdf)
  > 💡 用液态神经网络替代MLP变形场，实现显式连续时间平滑动态场景重建。

  <details><summary>Abstract</summary>

  Deformable 3D Gaussian Splatting (D-3DGS) re-constructs dynamic scenes from monocular video by deforming a canonical set of 3D Gaussians through a positional-encoded MLP of frame time t. Although fitted to a continuous variable, the MLP couples no two values of t in its architecture and effectively predicts discrete per-frame offsets, leaving temporal smoothness to emerge only as a byproduct of optimisation. We redesign the deformation field as a stack of Closed-form Continuous-time (CfC) cells, a Liquid Neural Network (LNN), that is the closed-form solution of the Liquid Time-constant ODE while preserving every other part of the D-3DGS pipeline. Each cell exposes a sigmoidal time gate that interpolates between two candidate hidden states, baking a learned smooth response to t into the loss landscape without invoking any numerical solver. On the eight D-NeRF and seven NeRF-DS scenes the liquid field matches or exceeds the MLP baseline in aggregate, with its largest gains concentrated on the scenes with the most high-frequency articulated motion. The result is a near-zero-friction architectural design that turns the discrete MLP deformation field into an explicit continuous-time function of t.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[Wispy to Voluminous: Prior-free Multi-view Capture of Strand-level Facial Hair](https://arxiv.org/abs/2606.08041)**  
  *Jaeseong Lee, Giljoo Nam, Adrian Jarabo, Carlos Aliaga*  
  `2026-06-06` · `cs.GR` · [abs](https://arxiv.org/abs/2606.08041) · [pdf](https://arxiv.org/pdf/2606.08041.pdf)
  > 💡 将多视图图像的无结构3

  <details><summary>Abstract</summary>

  Facial hair is a defining trait of personal identity, yet remains a critical bottleneck for digital avatars. Recent volumetric methods achieve photorealism but bake hair into the underlying face geometry, preventing editability and failing to resolve sparse, strand-like structures. Meanwhile, scalp-hair reconstruction methods target dense hair volumes and do not transfer to the sparse, spatially-varying nature of facial hair. We present a pipeline that automatically reconstructs facial hair -- beard, mustache, lashes, and brows -- from multi-view images, converting an unstructured 3D Gaussian representation into an explicit curve-based strand representation. We resolve geometric ambiguities in four stages: (i) optimizing 3D Gaussians constrained by tracked head geometry to enforce early ray termination and suppress sub-surface noise; (ii) tracing continuous strands robust to frequent crossings and extreme curvature; (iii) grounding strands to the surface and resolving root-tip ambiguity via a physically-motivated prior; and (iv) refining the reconstruction through opacity-driven density control under photometric optimization. To our knowledge, this is the first method to reconstruct high-fidelity facial hair strands from a 3D Gaussian representation. The recovered strands faithfully preserve the orientation and sparsity patterns characteristic of facial hair, and yield assets immediately suitable for downstream production tasks, including facial animation and physical simulation, geometric grooming and transfer, appearance editing, and physics-based rendering.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (2) · <a href="topics/generation.md">full list →</a></summary>

- **[Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/abs/2606.09034)**  
  *Mizuki Morikawa, Yuta Shimizu, Chunyu Li, Yusuke Monno, Masatoshi Okutomi*  
  `2026-06-08` · `cs.CV` · [abs](https://arxiv.org/abs/2606.09034) · [pdf](https://arxiv.org/pdf/2606.09034.pdf)
  > 💡 利用街景NeRF渲染图像辅助3DGS训练，移除瞬态物体并添加鸟瞰视图，结合扩散增强，兼顾渲染速度与质量。

  <details><summary>Abstract</summary>

  Neural radiance field (NeRF) and 3D Gaussian splatting (3DGS) are two mainstream approaches for novel view synthesis. They often show complementary performance, i.e., 3DGS demonstrating faster rendering speed and NeRF demonstrating higher rendering quality. Motivated by this, we propose leveraging NeRF-rendered images for 3DGS. Specifically, we target street scenes and utilize a pre-trained street-specific NeRF method to produce training images for a target 3DGS method. In our 3DGS training, NeRF-rendered images are used to remove transient objects in street-level input views and to generate bird's-eye views as additional views, inheriting the higher-quality rendering of NeRF into 3DGS. We further incorporate a diffusion-based image enhancement to improve the image quality of the additional views. Experimental results on one synthetic and two real datasets demonstrate that our proposed method improves street-scene rendering while preserving the speed of 3DGS and the quality of NeRF.

  </details>


- **[LEGS: Laplacian-Enhanced Gaussian Splatting with a Nonlinear Weighted Loss](https://arxiv.org/abs/2606.07932)**  
  *Yongfei Guo, Qizhou Huo, Xuan Sun, Yuanhao Gong*  
  `2026-06-06` · `cs.CV` · [abs](https://arxiv.org/abs/2606.07932) · [pdf](https://arxiv.org/pdf/2606.07932.pdf)
  > 💡 用二阶拉普拉斯非线性加权损失替代一阶梯度，增强高斯溅射的结构感知，渲染质量提升达1.68dB。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become an efficient explicit representation for radiance field reconstruction and real-time novel view synthesis. However, its standard photometric loss treats flat and structure-rich regions similarly, which may limit the recovery of sharp contours and fine details. Edge-Guided Gaussian Splatting (EGGS) improves structure awareness through edge-guided weighting, but mainly relies on first-order gradient responses and linear weighting. In this paper, we propose LEGS, a Laplacian-Enhanced Gaussian Splatting method with a nonlinearly weighted loss. LEGS replaces first-order gradient guidance with second-order Laplacian structural guidance and maps the normalized Laplacian response into pixel-wise weights through nonlinear response-to-weight functions. The proposed loss improves structure-aware Gaussian optimization while keeping the original 3DGS rendering pipeline unchanged. Experiments on the full Tanks\&Temples and Mip-NeRF360 datasets show that LEGS improves peak signal-to-noise ratio (PSNR) by up to 1.68 dB over 3DGS and up to 0.52 dB over EGGS. Incorporating the proposed second-order nonlinear weighting strategy into FastGS and FasterGS further improves PSNR by up to 1.69 dB, demonstrating its effectiveness as a general loss-level extension for Gaussian Splatting pipelines with potential applications in AR/VR, immersive visualization, and real-time 3D content generation.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (2) · <a href="topics/editing.md">full list →</a></summary>

- **[MaterialClusterGS: Palette-Based Material Decomposition and Physically-Based Relighting with 2D Gaussian Splatting](https://arxiv.org/abs/2606.09018)**  
  *Hao Zhang, Ang Li, Boyan Du, Junke Zhu, Fei Zhu, Meng Gai, Zhangjin Huang, Guoping Wang, Sheng Li*  
  `2026-06-08` · `cs.GR` · [abs](https://arxiv.org/abs/2606.09018) · [pdf](https://arxiv.org/pdf/2606.09018.pdf)
  > 💡 用调色板基材质分解和连续空间材质场解决高斯逆渲染材质欠约束问题，实现物理可重光照与编辑。

  <details><summary>Abstract</summary>

  We present MaterialClusterGS, a palette-based material decomposition framework for 2D Gaussian Splatting that enables physically based relighting and material editing. Existing Gaussian inverse rendering methods typically assign independent BRDF parameters to individual primitives. While flexible, this local fitting strategy makes material recovery highly under-constrained: shadows, indirect illumination, geometric errors, and visibility residuals can be absorbed into thousands of slightly different local material estimates. Meanwhile, recent palette-based appearance methods operate solely in RGB space without modeling physical materials or illumination. To bridge this gap, we represent scene materials using a compact global palette of shared BRDF prototypes assigned via a continuous spatial material field. Without shared material structure, editing one region does not propagate consistently to others of the same material, making per-primitive decompositions impractical for editing. We jointly optimize the material field, palette prototypes, and environment lighting under a physically based rendering objective. The resulting framework recovers compact, spatially coherent attributes directly usable for material editing, relighting, and transfer.

  </details>


- **[GraspFoM: Towards Reconstruction-Driven Robotic Grasping with 3D Foundation Priors](https://arxiv.org/abs/2606.08440)**  
  *Dongli Wu, Xiaobao Wei, Hao Wang, Qiaochu Dong, Ying Li, Qingpo Wuwu, Ming Lu, Wufan Zhao*  
  `2026-06-07` · `cs.RO` · [abs](https://arxiv.org/abs/2606.08440) · [pdf](https://arxiv.org/pdf/2606.08440.pdf)
  > 💡 利用SAM

  <details><summary>Abstract</summary>

  Robotic grasping is a fundamental capability in robotic manipulation. Yet grasping remains challenging under partial observations. Reliable grasping depends on both local contact cues and object-level 3D structure. Existing geometry-aware grasping methods recognize the value of reconstruction, but they typically treat geometry as an intermediate prediction rather than a reusable object prior for grasping. In this paper, we present GraspFoM, a unified framework that leverages 3D foundation priors (SAM3D) to build a shared 3D object latent for both reconstruction and grasp pose prediction. Built on this shared object latent, we introduce an anchor-initialized truncated pose-reasoning diffuser that predicts continuous and multimodal grasp poses without directly relying on discrete grasp candidates. We further investigate the interaction between reconstruction and grasping through a reconstruction-aware scorer and a residual latent updater. Reconstruction provides grounded geometric cues, while grasp supervision refines the shared object latent toward grasp-relevant affordances. GraspFoM jointly predicts grasp poses and reconstructs high-fidelity 3D assets in mesh and 3DGS forms. Comprehensive experiments demonstrate that GraspFoM achieves state-of-the-art results on both reconstruction and grasping. Notably, these improvements require only a small number of additional trainable parameters. Component-wise ablation studies also demonstrate the contribution of each component.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606)**  
  *Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li*  
  `2026-06-08` · `cs.GR` · [abs](https://arxiv.org/abs/2606.09606) · [pdf](https://arxiv.org/pdf/2606.09606.pdf)
  > 💡 现有逆渲染因管线不匹配忽略间接光照，提出无splatting的路径追踪框架，用路径空间等价模型统一前后向传播，实现全局光照下材质优化与高质量渲染。

  <details><summary>Abstract</summary>

  Ray tracing enables 3D Gaussian fields to serve as a representation for physically based light transport. Faithful inverse rendering requires forward rendering and backward optimization to be defined within a consistent light-transport pipeline. Existing inverse rendering methods estimate G-buffers via splatting and optimize materials in screen space, tying the recovered properties to a rasterization-based pipeline. This pipeline mismatch, together with simplified rendering equations that neglect indirect illumination, often leads to inconsistent shading, visible artifacts, and inaccurate material-lighting estimation under path-traced rendering. Therefore, we propose a splatting-free path-traced inverse rendering framework for 3D Gaussian fields, where forward light transport and backward gradient propagation are defined within a unified ray-tracing pipeline. Our key idea is to define a path-space equivalent interaction model for overlapping Gaussian primitives, under which Monte-Carlo-based path tracing is unbiased for the induced light-transport integral, while pathwise gradients are replayed over the same ray-traced interactions rather than splatting-derived screen-space buffers. The framework optimizes materials and a compact Spherical-Gaussian environment under the full rendering equation with ray-traced visibility and multi-bounce light transport. Extensive experiments demonstrate competitive material inversion and improved path-traced rendering quality, producing more plausible shadows, reflections, and relighting results under global illumination.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
