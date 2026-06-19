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
| 2 | **Dynamic / 4D / Streaming** | 242 | — | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 32 | **+1** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 49 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 23 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 32 | — | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 40 | **+1** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 13 | **+1** | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 15 | **+1** | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 2 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 5 | **+1** | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 15 | **+1** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 9 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 23 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 9 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-06-19 (UTC) — 6 new paper(s)

<details><summary><b>Avatar / Human / Face</b> (1) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies](https://arxiv.org/abs/2606.19586)**  
  *Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song*  
  `2026-06-17` · `cs.RO` · [abs](https://arxiv.org/abs/2606.19586) · [pdf](https://arxiv.org/pdf/2606.19586.pdf)
  > 💡 针对操作任务中观测分布外导致失败的问题，提出基于高斯散射和轨迹优化的鱼眼视图动作增强框架，提升成功率。

  <details><summary>Abstract</summary>

  Visuomotor policies for manipulation have demonstrated remarkable potential in modeling complex robotic behaviors, yet minor alterations in the robot's initial configuration and unseen obstacles easily lead to out-of-distribution observations. Without extensive data collection effort, these result in catastrophic execution failures. In this work, we introduce an effective data augmentation framework that generates visually realistic fisheye image sequences and corresponding physically feasible action trajectories from real-world eye-in-hand demonstrations, captured with a portable parallel gripper with a single fisheye camera. We introduce a novel Gaussian Splatting formulation, adapted to wide FoV fisheye cameras, to reconstruct and edit the 3D scene with unseen objects. We utilize trajectory optimization to generate smooth, collision-free, view-rendering-friendly action trajectories and render visual observations from corresponding novel views. Comprehensive experiments in simulation and the real world show that our augmentation framework improves the success rate for various manipulation tasks in both the same scene and the augmented scene with obstacles requiring collision avoidance.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (1) · <a href="topics/rendering.md">full list →</a></summary>

- **[LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping](https://arxiv.org/abs/2606.20424)**  
  *Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui*  
  `2026-06-18` · `cs.RO` · [abs](https://arxiv.org/abs/2606.20424) · [pdf](https://arxiv.org/pdf/2606.20424.pdf)
  > 💡 针对光照变化场景，LIT-GS通过LiDAR平面约束和热-LiDAR关联优化位姿与结构，提升几何与渲染质量。

  <details><summary>Abstract</summary>

  Gaussian Splatting has enabled real-time neural rendering, yet existing LiDAR-inertial-visual (LIV) Gaussian mapping pipelines remain fragile under illumination changes and texture-deficient scenes due to their reliance on RGB photometric cues. We present LIT-GS, a LiDAR-inertial-thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization. Specifically, we exploit LIV visual map points as confidence-aware cross-modal anchors to establish reliable thermal-LiDAR associations, and incorporate weighted LiDAR point-to-plane residuals into bundle adjustment to jointly refine camera poses and 3D points under weak thermal supervision. Building on the refined structure, we further introduce a LiDAR-plane-regularized differentiable splatting objective that constrains rendered 3D points to align with locally observed planes, mitigating surface thickening and structural drift in low-contrast thermal imagery. Experiments on proprietary sequences and public datasets demonstrate that LIT-GS consistently improves geometric accuracy and rendering quality over state-of-the-art LIV-based Gaussian Splatting baselines, particularly in challenging lighting conditions.

  </details>


</details>

<details><summary><b>SLAM / Localization / Mapping</b> (1) · <a href="topics/slam.md">full list →</a></summary>

- **[MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM](https://arxiv.org/abs/2606.19874)**  
  *Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang*  
  `2026-06-18` · `cs.RO` · [abs](https://arxiv.org/abs/2606.19874) · [pdf](https://arxiv.org/pdf/2606.19874.pdf)
  > 💡 提出MMD-SLAM，利用Atlanta World假设增强

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has significantly boosted novel view synthesis and high-fidelity scene reconstruction, expanding the potential of 3DGS-based Visual Simultaneous Localization and Mapping (SLAM) methods. However, most existing systems fail to fully exploit the underlying structural information, which limits rendering quality and often leads to inconsistent maps. To address these limitations, we propose MMD-SLAM, a structure-enhanced Visual SLAM framework that leverages the Atlanta World (AW) assumption to guide a Multi-Meta Gaussian representation for photorealistic mapping. First, we introduce a point-line fusion strategy for pose optimization, where 3D line segments are incorporated to improve tracking robustness and provide additional constraints for mapping. Second, we design a Multi-Meta Gaussian representation with dominant directions, explicitly encoding structural priors from the AW hypothesis. Finally, we propose a Gaussian evolution strategy that adapts to scene geometry and incorporates structural cues into global optimization. Extensive experiments demonstrate that these innovations enable MMD-SLAM to achieve state-of-the-art performance in both tracking accuracy and mapping quality. e.g., our method achieves a 48.56% reduction in ATE RMSE on ScanNet and a 5.71% improvement in PSNR on Replica, compared with MonoGS.

  </details>


</details>

<details><summary><b>Autonomous Driving / Outdoor</b> (1) · <a href="topics/driving.md">full list →</a></summary>

- **[Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration](https://arxiv.org/abs/2606.20103)**  
  *Kyoleen Kwak, Daeho Kim, Jeong Woon Lee, Hyoseok Hwang*  
  `2026-06-18` · `cs.CV` · [abs](https://arxiv.org/abs/2606.20103) · [pdf](https://arxiv.org/pdf/2606.20103.pdf)
  > 💡 针对3DGS标定中几何漂移问题，提出多视图LiDAR深度监督并阻断光度梯度以保留度量几何，提升标定精度。

  <details><summary>Abstract</summary>

  Accurate LiDAR-camera calibration is essential for robust multi-modal perception. Targetless approaches avoid manual setup but remain limited by the scarcity of discriminative cross-modal features. Recent methods address this by reconstructing the scene within a differentiable model, enabling extrinsic optimization through dense photometric supervision. Among these, 3D Gaussian Splatting (3DGS) has been widely adopted as a geometric proxy that bridges LiDAR and camera within a single differentiable framework. However, since 3DGS was originally designed for novel view synthesis, existing methods tend to prioritize rendering quality, causing the proxy geometry to drift from the true LiDAR structure. We propose a framework that preserves the metric geometry of the Gaussian proxy by aggregating multi-view LiDAR observations for dense depth supervision and blocking photometric gradients from updating the Gaussian spatial parameters. We validate our method on public driving datasets, where it consistently outperforms existing targetless methods in calibration accuracy.

  </details>


</details>

<details><summary><b>Relighting / Material / BRDF</b> (1) · <a href="topics/relighting.md">full list →</a></summary>

- **[Building Drift: Documenting On-Site Construction Adaptations Across Material Lifecycles](https://arxiv.org/abs/2606.19609)**  
  *Ritik Batra, Martin Tamke, Tom Svilans, Jan Hüls, Amritansh Kwatra, Steven J. Jackson, Thijs Roumen, Mette Ramsgaard Thomsen*  
  `2026-06-17` · `cs.HC` · [abs](https://arxiv.org/abs/2606.19609) · [pdf](https://arxiv.org/pdf/2606.19609.pdf)
  > 💡 提出建筑漂移概念和分类法，用Pentimento工具结合视频与3D高斯泼溅记录现场适应，促进回收材料循环利用。

  <details><summary>Abstract</summary>

  In a circular economy for construction, reclaimed materials carry prior lives of use and go on to have post-lives in future buildings. Yet working with such materials introduces unpredictability that requires on-site improvisation, making their reuse challenging to document and scale across building lifetimes. Without documentation, the on-site adaptations that make construction with reclaimed materials possible leave collaborators, evaluators, and inheritors without the information they need to continue, assess, and reuse materials. We call the collective deviation of the physical state from the digital model through these adaptations "building drift." Through a case study, ReShelter, a reclaimed timber pavilion constructed in the forest, we develop a taxonomy for building drift that characterizes the collective deviation across building lifetimes: Tending the Site, Foraging for Fit, Interpreting the Material, Marking Measurements, and Coordinating Across Communities. To put our taxonomy for building drift into practice, we present Pentimento, a documentation tool that leverages video documentation and 3D Gaussian Splatting to spatially, temporally, and semantically represent on-site adaptations in relation to the designed model. Pentimento enables each stakeholder to navigate material histories in ways that reduce barriers to material reuse. Together, these contributions open pathways towards computational tools that support the on-site improvisation essential to construction with reclaimed materials, enabling more sustainable cycles of recovery, repair, and reuse.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (1) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[VisDom: Sparse Novel View Synthesis with Visible Domain Constraint](https://arxiv.org/abs/2606.20531)**  
  *Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers*  
  `2026-06-18` · `cs.CV` · [abs](https://arxiv.org/abs/2606.20531) · [pdf](https://arxiv.org/pdf/2606.20531.pdf)
  > 💡 针对稀疏视图新视图合成中过拟合与几何模糊，提出可见域约束，基于多视图可见性过滤，提升NeRF/GS重建质量。

  <details><summary>Abstract</summary>

  Sparse novel view synthesis (NVS) remains challenging due to the ambiguity of recovering 3D geometry from few input views. While NeRF- and Gaussian Splatting (GS)-based methods perform well with dense supervision, they often overfit in sparse settings, producing floating artifacts and inconsistent geometry. Silhouette consistency is commonly used as a regularizer, but it remains insufficient, as silhouette-consistent regions can extend beyond the true object geometry. We introduce VisDom, a learning-free geometric constraint that augments classical carving-based visual hull reconstruction by enforcing a minimum multi-view visibility requirement. Specifically, we define a visible domain as the subset of 3D space observed by at least $K$ views and use it as an additional filtering criterion on top of standard silhouette-based reconstruction. This provides a stronger spatial prior in sparse-view settings. We integrate VisDom into both implicit (NeRF) and explicit (GS) pipelines by restricting volumetric sampling and guiding Gaussian placement during optimization. Experiments on three challenging datasets show consistent improvements in sparse-view NVS, enabling high-quality object-centric reconstruction from as few as four input images. Our method is domain-agnostic, requires only silhouettes, and introduces no learned parameters, making it a simple complement to existing approaches. Applying VisDom on top of GaussianObject further improves performance on Omni3D and MipNeRF360, while matching or surpassing it at 22 $\times$ lower training cost.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
