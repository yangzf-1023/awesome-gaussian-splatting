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
| 2 | **Dynamic / 4D / Streaming** | 279 | **+1** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 44 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 71 | **+2** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 37 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 39 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 57 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 17 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 8 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 23 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 27 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 10 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-15 (UTC) — 5 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (1) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements](https://arxiv.org/abs/2607.12362)**  
  *Seung-gyeom Kim, Areum Kim, Yongjae Yoo, Sukmin Yun*  
  `2026-07-14` · `cs.CV` · [abs](https://arxiv.org/abs/2607.12362) · [pdf](https://arxiv.org/pdf/2607.12362.pdf)
  > 💡 利用时空位置隐式网络预测高斯属性，解决大帧间位移下快速运动的4DGS重建失败问题，显著提升保真度。

  <details><summary>Abstract</summary>

  Recent 4D Gaussian Splatting (4DGS) methods often fail under fast motion with large inter-frame displacements, where Gaussian attributes are poorly learned during training, and fast-moving objects are often lost from the reconstruction. In this work, we introduce Spatiotemporal Position Implicit Network for 4DGS, coined SPIN-4DGS, which learns Gaussian attributes from explicitly collected spatiotemporal positions rather than modeling temporal displacements, thereby enabling more faithful splatting under fast motions with large inter-frame displacements. To avoid the heavy memory overhead of explicitly optimizing attributes across all spatiotemporal positions, we instead predict them with a lightweight feed-forward network trained under a rasterization-based reconstruction loss. Consequently, SPIN-4DGS learns shared representations across Gaussians, effectively capturing spatiotemporal consistency and enabling stable high-quality Gaussian splatting even under challenging motions. Across extensive experiments, SPIN-4DGS consistently achieves higher fidelity under large displacements, with clear improvements in PSNR and SSIM on challenging sports scenes from the CMU Panoptic dataset. For example, SPIN-4DGS notably outperforms the strongest baseline, D3DGS, by achieving +1.83 higher PSNR on the Basketball scene.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356)**  
  *Mohan Liu, Zhihao Gu, Xuanyu Chen, Haitian Zhang, Kaimin Mao, Yan Wu, Wei-Yun Yau, Lin Wang*  
  `2026-07-14` · `cs.RO` · [abs](https://arxiv.org/abs/2607.12356) · [pdf](https://arxiv.org/pdf/2607.12356.pdf)
  > 💡 将多视角视觉语言特征提升为3D高斯基元，构建几何语义认知表示，用Merge-then-Query压缩99%token，提升机器人操控成功率22.8%。

  <details><summary>Abstract</summary>

  Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. While recent efforts incorporate explicit 3D cues, such as depth maps or point clouds, to improve geometric awareness, they primarily capture low-level structures and lack high-level semantic grounding in 3D space. In human cognition, interaction with the physical world relies on a 3D semantic cognitive map - an internal mental model that integrates spatial layouts with semantic context to enable persistent, viewpoint-invariant reasoning. In light of this, we present VistaVLA, a novel two-stage framework that constructs a geometry- and semantics-aware 3D cognitive representation from 3D Gaussian primitives and grounds it as compact context tokens for VLA policy learning. Specifically, VistaVLA lifts multi-view vision-language features into 3D Gaussian primitives, forming geometry-anchored semantic tokens that align view-consistent spatial grounding with 2D visual feature spaces. To make this 3D representation computationally tractable for effective VLA control, we introduce Merge-then-Query (MtQ), a token summarization mechanism. MtQ compresses dense Gaussian primitives into a highly compact set of spatially informative tokens, achieving a 99% token reduction while preserving action-relevant 3D layouts and semantic context. Extensive evaluations in both simulated and real-world environments demonstrate the effectiveness of VistaVLA. Notably, in real-world scenarios, VistaVLA improves success rates by 22.8% across seven real-world tasks and by 30.0% over the VLA-Adapter baseline on challenging out-of-distribution tasks.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (2) · <a href="topics/generation.md">full list →</a></summary>

- **[ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting](https://arxiv.org/abs/2607.12785)**  
  *Cheng-Tai Hsieh, Jiwei Shan, Han Fang, Jianshu Hu, Tao Ni, Lijun Han, Yutong Ban, Shing Shin Cheng, Hesheng Wang*  
  `2026-07-14` · `cs.CV` · [abs](https://arxiv.org/abs/2607.12785) · [pdf](https://arxiv.org/pdf/2607.12785.pdf)
  > 💡 通过扩散引导的3D高斯泼溅和不确定性采样，有效减少内窥镜视野外推伪影，实现SOTA新视角合成。

  <details><summary>Abstract</summary>

  Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating beyond the training trajectory.In this work, we propose ExtraGS, a framework for enhancing endoscopic view extrapolation via diffusion-guided 3D Gaussian Splatting. Starting from an initial reconstruction, we introduce an uncertainty-guided virtual camera sampling strategy to actively explore blind spots and maximize information gain. The rendered views from these sampled locations are refined using a diffusion model to recover plausible anatomical structures, producing pseudo observations that guide further optimization. To prevent the generated content from degrading reliable regions, we adopt a confidence-weighted fine-tuning strategy when incorporating these pseudo observations.Extensive experiments on multiple public endoscopic datasets demonstrate that ExtraGS significantly reduces extrapolation artifacts and achieves state-of-the-art performance in endoscopic novel view synthesis.

  </details>


- **[GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR](https://arxiv.org/abs/2607.12641)**  
  *Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu*  
  `2026-07-14` · `cs.MM` · [abs](https://arxiv.org/abs/2607.12641) · [pdf](https://arxiv.org/pdf/2607.12641.pdf)
  > 💡 提出几何感知跨层框架GeoFovea-GS，用注视点失真度量和信息价值调度优化无线VR渲染传输，降低带宽并提升质量。

  <details><summary>Abstract</summary>

  Wireless aerial virtual reality (VR) aims to provide immersive access to large-scale scenes, but high-resolution view generation and delivery are jointly constrained by limited bandwidth, latency, and power. 3D Gaussian Splatting (3DGS) can reduce the payload by rendering views from compact pose information, yet its geometry errors may cause severe VR quality degradation. Existing channel-aware or pixel-level resource allocation schemes fail to capture such geometry-sensitive distortion. To address this issue, this paper proposes GeoFovea-GS as a geometry-aware cross-layer framework for communication-efficient wireless aerial VR. A foveated geometry-aware distortion metric is developed to characterize photometric rendering error, geometric inconsistency, and view-dependent perceptual importance in a unified form. Based on this metric, the joint selection of pose-only 3DGS rendering and image/tile correction transmission is formulated as a cross-layer optimization problem under wireless constraints. A lightweight value-of-information scheduler is further developed to allocate communication resources to regions that are both geometry-critical and perceptually important. Experiments on real-world 3DGS scenes demonstrate that GeoFovea-GS achieves superior immersive rendering quality with substantially reduced transmission cost.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[SpeedyGS: Content-Aware 3D Gaussian Splatting Compression via Two-Stage Optimization](https://arxiv.org/abs/2607.12656)**  
  *Junteng Zhang, Tong Chen, Yuxin Zhao, Yibo Shi, Jing Wang, Zhan Ma*  
  `2026-07-14` · `eess.SP` · [abs](https://arxiv.org/abs/2607.12656) · [pdf](https://arxiv.org/pdf/2607.12656.pdf)
  > 💡 针对3DGS解码慢问题，提出内容感知两阶段优化，联合自适应量化剪枝与率代理，结合稀疏八叉树令牌和局部自回归熵编码，实现160倍压缩及9倍优化加速。

  <details><summary>Abstract</summary>

  Recent progress in compressing large-scale 3D Gaussian Splatting (3DGS) data has substantially reduced storage footprint, network transmission bandwidth, and memory traffic to GPU caches before rendering. Yet decoding with advanced 3DGS codecs still takes seconds, making them unsuitable for interactive applications. To systematically address this challenge, we propose SpeedyGS, a Content-Aware 3DGS Compressor that separately optimizes the structural formation and statistical coding. First, in structural formation, we jointly optimize adaptive quantization and pruning under a unified rate-distortion objective, where the rate term is replaced by a lightweight rate proxy that estimates entropy coding cost of the next stage, thereby efficiently regulating Gaussian density and precision to yield a compact scene representation. Then, in the statistical coding phase, Gaussian geometry is converted into sparse octree tokens and subsequently undergoes multi-stage coding, while Gaussian attributes are serialized into a 1D token stream for entropy coding via a complexity-controllable local autoregressive model. SpeedyGS achieves a favorable balance among optimization efficiency, compression performance, decoding latency, and rendering speed. Compared to vanilla 3DGS, SpeedyGS achieves up to 160$\times$ model size reduction with negligible quality degradation across common datasets. Compared to state-of-the-art compression methods, it also offers significantly faster decoding and accelerates optimization by 9$\times$ on consumer-grade hardware. To further reduce decoding overhead, the statistical coding stage also supports channel-wise, fixed-length coding for Gaussian as a simpler alternative, enabling SpeedyGS to better adapt to the underlying application and reduce decoding latency to nearly zero.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
