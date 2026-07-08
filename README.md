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
| 1 | **Survey & Benchmark** | 79 | **+1** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 273 | **+1** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 42 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 64 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 37 | **+1** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 37 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 55 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 16 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 7 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 20 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | **+1** | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 26 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-08 (UTC) — 5 new paper(s)

<details><summary><b>Survey & Benchmark</b> (1) · <a href="topics/survey.md">full list →</a></summary>

- **[APVI-SLAM: Real-Time Acoustic-Pressure-Visual-Inertial Localization and Photorealistic Mapping System in Complex Underwater Environment](https://arxiv.org/abs/2607.06222)**  
  *Hanwen Zhang, Yipeng Zhu, Xiaopeng Guo, Huajian Huang, Sai-Kit Yeung*  
  `2026-07-07` · `cs.RO` · [abs](https://arxiv.org/abs/2607.06222) · [pdf](https://arxiv.org/pdf/2607.06222.pdf)
  > 💡 水下视觉惯性SLAM面临特征退化，提出可靠性感知定位与四叉树引导3D高斯映射，实现实时高精度定位和逼真重建。

  <details><summary>Abstract</summary>

  Extreme subsea environments often cause severe feature de-gradation and estimator divergence in underwater visual-inertial SLAM. Although sensors like Doppler Velocity Logs (DVL) and pressure gauges provide auxiliary constraints, robust multi-sensor fusion during intermittent visual failure remains challenging. To address this, we present APVI-SLAM, a real-time multi-sensor fusion SLAM system that achieves both accurate underwater localization and photorealistic mapping. Our approach introduces a reliability-aware localization framework that dynamically reweights sensor estimators and employs a sliding-window freezing strategy to recover from tracking failures, substantially enhancing system robustness. Furthermore, for high-fidelity scenes reconstruction, we propose an efficient quadtree-guided mapping module that facilitates incremental water-medium modeling and 3D Gaussian optimization. Recognizing the lack of benchmark for underwater mapping evaluation, we also contribute a coral reef surveying dataset with synchronized multi-modality data. Extensive experiments on public and our proposed benchmarks demonstrate that APVI-SLAM achieves state-of-the-art localization and reconstruction quality at real-time speeds.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (1) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238)**  
  *Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren*  
  `2026-07-07` · `cs.CV` · [abs](https://arxiv.org/abs/2607.06238) · [pdf](https://arxiv.org/pdf/2607.06238.pdf)
  > 💡 针对MRI超分辨忽略分辨率-SNR物理耦合，提出物理感知重建方法，结合

  <details><summary>Abstract</summary>

  Magnetic resonance imaging (MRI) super-resolution is vital for improving diagnostic accessibility, yet most methods treat it as a deterministic mapping from a fixed low-resolution input to a high-resolution target. This overlooks a key property of MRI acquisition physics: spatial resolution and signal-to-noise ratio (SNR) are inherently coupled, making any given low-resolution scan merely one of many possible realizations under varying acquisition trade-offs. We rethink MRI super-resolution as a physics-aware reconstruction problem, in which the goal is to identify the optimal resolution-SNR configuration and then super-resolve it to obtain high-quality MRI results. A key implication of this formulation is that MRI resolution becomes dynamic rather than fixed. To handle such resolution-heterogeneous inputs, we adapt 2D Gaussian Splatting (2D GS) to MRI by formulating reconstruction as a coordinate-based, resolution-agnostic rendering problem. To further enhance fidelity, we introduce three innovations: (1) a prior-aware Gaussian representation that combines an Anatomical Structure Prior for tissue-specific kernel initialization with an Imaging System Prior that captures hardware characteristics via a covariance dictionary; (2) a physics-constrained signal modeling scheme that predicts intrinsic tissue parameters (proton density rho and effective relaxation rate R2) and synthesizes intensities through governing physical equations, ensuring biophysically plausible contrast; and (3) a meta-learning framework that alleviates paired-data scarcity by pretraining on simulated data and adapting to real-world conditions. Extensive experiments on dynamic-resolution datasets and standard benchmarks demonstrate that our method achieves state-of-the-art performance, highlighting its strong potential for clinical deployment.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522)**  
  *Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang*  
  `2026-07-06` · `cs.CV` · [abs](https://arxiv.org/abs/2607.05522) · [pdf](https://arxiv.org/pdf/2607.05522.pdf)
  > 💡 提出渲染感知贝叶斯3DGS框架，用Normal-Inverse-Wishart后验实现不确定性量化与自适应复杂度控制，在主动视图选择任务中PSNR提升0.453dB。

  <details><summary>Abstract</summary>

  3D Gaussian splatting (3DGS) is a strong representation for real-time novel-view synthesis, but its standard training pipeline relies on point estimates and hand-tuned heuristics, providing no native uncertainty or principled complexity control. This is most limiting under sparse views or fixed acquisition budgets, where a model must identify weakly supported geometry and select informative views. We introduce a rendering-aware Bayesian 3DGS framework that tracks Gaussian geometry with a Normal-Inverse-Wishart posterior over means and covariances using renderer-derived surrogate summaries. An optional Dirichlet-process extension adds a probabilistic component-usage signal, and the training schedule makes the closed-form versus approximate inference boundary explicit. Re-rendering posterior geometry samples yields native predictive uncertainty for interval calibration and active view selection. In a fixed-budget 16-to-32 active-view task, native NIW acquisition improves PSNR by +0.453 dB and LPIPS by -0.0146 over a scoring-only 3-member standard-ensemble baseline, winning 29/39 scene-seed pairs and 10/13 scene means; it also improves over PPU-style (+0.355 dB) and NIW-proxy (+0.401 dB) acquisition. NIW native intervals reduce 95% coverage error by about 17x relative to a shared proxy (0.046 vs. 0.796) and are about 10x closer to nominal coverage than a 3-member deep ensemble (0.047 vs. 0.454) at roughly one-third the training cost. As a reconstruction compatibility check, paired NIW-vs-standard analysis over 39 scene-seed runs yields +0.030 dB PSNR with 1.6% additional training time. These results position Bayesian 3DGS as a practical probabilistic scene representation for decision-facing tasks such as active view selection.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (1) · <a href="topics/editing.md">full list →</a></summary>

- **[SSA-3DGS: Unsupervised Removal of Screen-Space Artifacts for 3D Gaussian Splatting](https://arxiv.org/abs/2607.05598)**  
  *Kristof Overdulve, Lode Jorissen, Nick Michiels*  
  `2026-07-06` · `cs.GR` · [abs](https://arxiv.org/abs/2607.05598) · [pdf](https://arxiv.org/pdf/2607.05598.pdf)
  > 💡 提出SSA-3DGS无监督框架，通过联合优化3D场景与可学习2D覆盖层消除屏幕空间伪影，有效提升重建保真度。

  <details><summary>Abstract</summary>

  Novel View Synthesis (NVS) methods, such as 3D Gaussian Splatting (3DGS), rely heavily on the assumption of clean, multi-view consistent, posed input images. Real-world captures can violate this assumption due to screen-space artifacts-static occlusions fixed to the 2D image plane rather than to the 3D world. Common examples include physical sensor defects, environmental obstructions (such as rain or mud on the lens enclosure), capture obstructions (such as a thumb over the camera sensor or a dashboard visible in dashcam footage), and digital overlays (such as watermarks or UI elements). When present, they are erroneously baked into the 3D geometry as "floaters" or near-camera artifacts, degrading the quality of novel-view rendering. In this work, we propose SSA-3DGS, an unsupervised framework that jointly optimizes a 3D scene and a learnable 2D overlay to recover a clean 3D scene and the corrupting artifacts. By exploiting geometric consensus across views, our method effectively disentangles static artifacts from the 3D scene geometry without supervision or manual input. Across diverse synthetic corruptions and a self-captured real-world dataset, SSA-3DGS improves reconstruction fidelity by up to 9 dB PSNR over 3DGS trained on the same corrupted inputs, while faithfully preserving the corrupting artifact.

  </details>


</details>

<details><summary><b>Semantic / Scene Understanding</b> (1) · <a href="topics/semantic.md">full list →</a></summary>

- **[GaussFusion: Towards Multimodal 3D Gaussian Pretraining](https://arxiv.org/abs/2607.05906)**  
  *Zhixuan You, Jihua Zhu, Yiding Sun, Zihao Guo, Haozhe Cheng, Dongxu Zhang, Lin Chen, Hainan Luo*  
  `2026-07-07` · `cs.CV` · [abs](https://arxiv.org/abs/2607.05906) · [pdf](https://arxiv.org/pdf/2607.05906.pdf)
  > 💡 针对3D高斯预训练缺乏语义监督，提出跨模态对齐和显著性引导掩码，提升表征可迁移性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting provides an explicit representation that jointly models geometry and appearance, serving as a scalable foundation for 3D representation learning. Existing pre-training methods for Gaussian representations, such as masked Gaussian reconstruction, primarily capture local structures but offer limited semantic supervision. In this paper, we propose GaussFusion, a multimodal pre-training framework for 3D Gaussian representations. GaussFusion integrates image and text supervision into masked Gaussian modeling through cross-modal semantic alignment, enabling the Gaussian encoder to learn both visual and language-level semantic information during pre-training. To better adapt masked modeling to the non-uniform distribution of Gaussian primitives, we further propose Gaussian Salience-guided Multi-scale Hole Masking (GSHM). GSHM constructs spatially continuous masked regions based on Gaussian salience. By applying hole masks at multiple scales, GSHM encourages the encoder to capture both fine-grained local patterns and broader structural dependencies. Extensive experiments on downstream tasks demonstrate that GaussFusion improves the transferability of Gaussian representations. Notably, GaussFusion outperforms Gaussian-MAE on ModelNet40 and ScanObjectNN (PB-T50-RS) by 0.61\% and 3.85\%, respectively.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
