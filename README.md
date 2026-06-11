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
| 1 | **Survey & Benchmark** | 59 | — | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 234 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 30 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 46 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 23 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 32 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 35 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 10 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 13 | **+1** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 3 | **+1** | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 13 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 22 | **+1** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 7 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-11 (UTC) — 6 new paper(s)

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Scene-Adaptive Nonlinear Tone Curves for Pseudo Ground-Truth Generation in Low-Light 3D Gaussian Splatting](https://arxiv.org/abs/2606.11841)**  
  *Mingzhe Lyu, Jinqiang Cui, Hong Zhang*  
  `2026-06-10` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11841) · [pdf](https://arxiv.org/pdf/2606.11841.pdf)
  > 💡 低光3DGS伪GT生成中线性增益受限，提出场景自适应非线性色调曲线（ASE/AP3），PSNR提升高达4.34dB。

  <details><summary>Abstract</summary>

  Low-light novel view synthesis is challenging because dark multi-view images contain noise, weak structural detail, and compressed dynamic range. Recent 3D Gaussian Splatting (3DGS) methods address these challenges by generating pseudo ground-truth (pseudo-GT) images as supervision targets when paired normal-light references are unavailable. Existing pseudo-GT methods apply a uniform linear gain to all pixels, which clips bright regions while providing insufficient enhancement in dark regions, limiting reconstruction quality. We observe that nonlinear tone mappings, long established in 2D low-light enhancement, have not been explored for pseudo-GT generation in 3D reconstruction. Accordingly, we propose a scene-adaptive nonlinear tone-curve framework that replaces linear pseudo-GT with nonlinear alternatives. The framework introduces percentile-based normalisation for scene-agnostic curve application, a scene-adaptive offset for automatic black-level adjustment, and two complementary curves: Adaptive SoftExp (ASE), a bounded exponential curve, and Adaptive Poly3 (AP3), a data-driven cubic polynomial. The module changes only the pseudo-GT computation and leaves the 3DGS backbone unchanged. Experiments on three benchmarks covering 21 scenes show that both curves consistently outperform the linear baseline with PSNR improvements up to +4.34 dB on LOM and +3.25 dB on RealX3D. Both curves achieve similar performance despite their different mathematical forms, suggesting the improvement is curve-agnostic. Code is available at https://github.com/lvmingzhe/adaptiveToneCurve

  </details>


- **[TRON: Tracing Rays to Orchestrate a Neural Renderer for 3D Gaussian Reconstructions](https://arxiv.org/abs/2606.11314)**  
  *Or Perel, Hassan Abu Alhaija, Zian Wang, Jacob Munkberg, Matan Atzmon, Sanja Fidler, Masha Shugrina*  
  `2026-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11314) · [pdf](https://arxiv.org/pdf/2606.11314.pdf)
  > 💡 结合3D高斯光线追踪与神经渲染，利用逆渲染先验和辐射引导，实现逼真可控的重光照与编辑。

  <details><summary>Abstract</summary>

  We introduce TRON, a rendering framework that combines 3D Gaussian ray tracing with neural rendering to enable realistic and controllable rendering of real-world 3D scenes under novel lighting, dynamic object motion, object insertion, and material editing. Prior approaches that rely solely on physically based rendering (PBR) of Gaussian representations struggle to achieve realistic relighting due to imperfections in reconstructed geometry, material estimates, and light transport estimation. At the same time, neural rendering methods often lack an explicit scene representation, limiting their ability to support interactive editing with fine-grained manipulation. TRON bridges these two paradigms. We use intrinsic decomposition priors from a learned inverse rendering model to regularize the material properties of a Gaussian field, and repurpose a ray tracer to provide radiometric guidance rather than final pixels. By treating this output as a structured 3D scaffold, we empower a lightweight neural renderer to bridge the domain gap between shading-model constrained estimates and photorealistic output. Our key insight is that the combination of explicit 3D knowledge with robust material priors provides speed and controllability, while neural rendering enables the synthesis of photorealistic images. To support real-world scenarios, we train our neural renderer with a multi-stage strategy consisting of large-scale pretraining and targeted fine-tuning on a newly constructed dataset of 2.1M rendered synthetic and real-world frames from 3D reconstructions. TRON outperforms Gaussian-based relighting methods in realism, and prior neural renderers in editability and speed. To the best of our knowledge, TRON is the first method to enable practical interactive applications in captured 3D environments, offering realistic appearance under dynamic geometric, lighting and material conditions.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[Seeing What Matters: Perceptual Wrapper with Common Randomness for 3D Gaussian Splatting](https://arxiv.org/abs/2606.11782)**  
  *He-Bi Yang, Jing-Zhong Chen, Yen-Kuan Ho, Sang NguyenQuang, Fan-Yi Hsu, Yun-Yu Lee, Jui-Chiu Chiang, Wen-Hsiao Peng*  
  `2026-06-10` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11782) · [pdf](https://arxiv.org/pdf/2606.11782.pdf)
  > 💡 针对3DGS高频纹理缺失问题，提出伪随机噪声驱动的2D感知包装器，以Wasserstein损失学习局部特征统计，提升感知质量并显著压缩模型体积。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) achieves impressive real-time rendering, it frequently struggles to synthesize high-frequency textures, a limitation heavily exacerbated in memory-constrained and rate-distortion-optimized (RDO) pipelines. To address this, we propose a versatile 2D perceptual wrapper that enhances the rendered outputs of existing 3DGS representations in a content- and view-dependent manner. Our method leverages a lightweight synthesis network conditioned on pseudo-random Gaussian noise to synthesize perceptually plausible textures. Supervised by Wasserstein Distortion, the network learns to match local feature statistics rather than strictly enforcing pixel-wise reconstruction fidelity, effectively mitigating the blurriness inherent in standard frameworks. We demonstrate the broad applicability of our plug-and-play approach across vanilla, memory-constrained, and RDO 3DGS methods. Comprehensive subjective and objective experiments confirm that our method significantly improves over existing baselines, yielding superior perceptual quality at sharply reduced file or model sizes.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (1) · <a href="topics/driving.md">full list →</a></summary>

- **[A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting](https://arxiv.org/abs/2606.11390)**  
  *Matthew Cong, Francis Williams, Jonathan Swartz, Mark Harris, Sanja Fidler, Ken Museth*  
  `2026-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11390) · [pdf](https://arxiv.org/pdf/2606.11390.pdf)
  > 💡 提出多GPU高斯溅射方法，利用CUDA统一内存和NVLink在算子级别隐藏通信，实现城市场景超10亿高斯块重建，规模提升25倍以上。

  <details><summary>Abstract</summary>

  Gaussian splatting methods have become increasingly popular for neural reconstruction of the real world. However, they are often limited in scale and resolution due to compute and memory constraints. We present a multi-GPU Gaussian splatting approach that scales reconstruction to higher resolutions and larger scenes while abstracting away the code complexity typically associated with distributing a model. To accomplish this, we propose a PyTorch backend that distributes the Gaussian parameters and splatting operators across GPUs via CUDA unified memory and NVLink. Because distribution occurs at the operator level, the model code requires no explicit cross-device communication. More broadly, the backend exposes multiple GPUs as an aggregate PyTorch device and supports other PyTorch operators. We demonstrate city-scale reconstructions with street-level detail consisting of over 1 billion Gaussian splats, more than 25 times as many as the current state of the art.

  </details>


</details>

<details><summary><b>Relighting / Material / BRDF</b> (1) · <a href="topics/relighting.md">full list →</a></summary>

- **[Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Collection](https://arxiv.org/abs/2606.11894)**  
  *Yuto Furutani, Takashi Otonari, Kaede Shiohara, Toshihiko Yamasaki*  
  `2026-06-10` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11894) · [pdf](https://arxiv.org/pdf/2606.11894.pdf)
  > 💡 针对前馈3DGS在复杂光照和瞬态物体场景中的困难，提出WildCity数据集及模型学习跨视角外观一致性并去除瞬态内容。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting (3DGS) removes the need for time-consuming per-scene optimization required by traditional 3DGS. However, existing feed-forward approaches struggle with real-world photo collections that include diverse lighting conditions and transient objects. In this paper, we present Wild3R, a feed-forward approach for unconstrained sparse photo collections. The main bottleneck is the lack of training data that provides multiple viewpoints, a variety of illuminations, and transient variations necessary for learning robust scene representations. To address this, we introduce the WildCity dataset, which comprises 200 scenes, 170 lighting conditions, and transient objects, resulting in 337,500 images in total. By leveraging the dataset, our model learns appearance consistency across viewpoints conditioned on reference views, while removing transient content. Extensive experiments demonstrate that our method outperforms existing feed-forward approaches and achieves results competitive with prior per-scene optimization-based methods.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (1) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[XPR: An Extensible Cross-Platform Point-Based Differentiable Renderer](https://arxiv.org/abs/2606.11529)**  
  *Steve Rhyner, Sankeerth Durvasula, Aleksandr Kovalev, Hansel Jia, Adrian Zhao, Mrutunjayya Mrutunjayya, Nilesh Ahuja, Selvakumar Panneer, Christina Giannoula, Nandita Vijaykumar*  
  `2026-06-10` · `cs.GR` · [abs](https://arxiv.org/abs/2606.11529) · [pdf](https://arxiv.org/pdf/2606.11529.pdf)
  > 💡 针对点基可微渲染开发困难，提出XPR框架，用高层接口分离逻辑，跨平台编译支持多种

  <details><summary>Abstract</summary>

  Point-based differentiable rendering underpins modern 3D reconstruction, novel-view synthesis, and learning-based graphics pipelines, but developing new rendering methods often requires extensive low-level implementation, hardware-specific kernels, and manually written backward passes. This limits rapid prototyping, reproducibility, exploration, and deployment, especially across diverse hardware platforms. This paper presents XPR, an extensible cross-platform framework for point-based differentiable rendering. XPR introduces a high-level programming interface that separates method-specific logic from the shared rendering pipeline, allowing users to implement new methods in a few lines of code. Its pipeline decomposes rendering into modular, statically shaped parallel operations that can be lowered by a cross-platform compiler to GPUs, TPUs, CPUs, and other ML accelerators. We demonstrate implementations of 3DGS, 3DGUT, and LinPrim, with only a few 100s lines of Python code, each of which can be compiled to a range of hardware platforms with the XLA compiler. These results show that XPR enables fast experimentation and portable execution for emerging point-based differentiable rendering systems.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
