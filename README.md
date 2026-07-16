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
| 1 | **Survey & Benchmark** | 81 | **+1** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 281 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 46 | **+2** | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 71 | — | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 37 | — | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 40 | **+1** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 57 | — | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 17 | — | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 8 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 23 | — | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 28 | **+1** | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 10 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-16 (UTC) — 7 new paper(s)

<details><summary><b>Survey & Benchmark</b> (1) · <a href="topics/survey.md">full list →</a></summary>

- **[Calibrated Closed-Form Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682)**  
  *Chulin Zhao, Yiran Xu, Shu Liu*  
  `2026-07-15` · `cs.CV` · [abs](https://arxiv.org/abs/2607.13682) · [pdf](https://arxiv.org/pdf/2607.13682.pdf)
  > 💡 利用辐射高斯泼溅的线性属性导出闭式变分方差，首次系统校准表明不确定性可准确排序稀疏视图CT重建误差。

  <details><summary>Abstract</summary>

  Radiative Gaussian splatting has made sparse-view CT reconstruction fast, but existing methods output point estimates with no notion of where the reconstruction can be trusted. We exploit a property of transmissive X-ray imaging that RGB splatting cannot claim -- projection and voxelization are strictly linear in the per-Gaussian densities -- to equip radiative Gaussians with a variational density posterior whose predictive variance propagates in closed form, exactly, in a single forward pass, in both volume space ($σ^2(x)=\sum_i g_i(x)^2 s_i^2$) and projection space ($\mathrm{Var}[I_p]=\sum_i w_{i,p}^2 s_i^2$). We present the first systematic calibration study for Gaussian-splatting CT (Spearman / AUSE / ECE with temperature scaling), showing that the resulting per-voxel uncertainty ranks true reconstruction error on 14 of 15 scenes of the official benchmark across three view budgets -- 9 of 15 additionally meeting our magnitude-calibration target after a single temperature -- while the perturbation-ensemble heuristic of concurrent work, transplanted to voxel space under the same protocol on our development scenes, does not (rank correlation as low as $-0.08$). We then dissect why uncalibrated acquisition scores can nevertheless select acceptable views, identifying three regimes -- flat (isotropic, balanced), pathological (degenerate coverage), and anisotropic -- and showing, in controlled single-scene testbeds, that principled uncertainty earns a measurable premium only in the last, motivating a coverage-gated, maturity-scheduled acquisition policy; the same calibrated posterior further points toward a dose-adaptive stopping rule, whose experimental validation we leave to future work.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](https://arxiv.org/abs/2607.13451)**  
  *Shivansh Patel, Kaifeng Zhang, Sanjay Pokkali, Svetlana Lazebnik, Yunzhu Li*  
  `2026-07-15` · `cs.RO` · [abs](https://arxiv.org/abs/2607.13451) · [pdf](https://arxiv.org/pdf/2607.13451.pdf)
  > 💡 结合可优化弹簧质点模型与残差修正网络，使用滑动窗口Transformer实现更精确的可变形物体模拟。

  <details><summary>Abstract</summary>

  Simulating deformable objects is essential for a wide range of robotic manipulation applications, yet accurately predicting their dynamics remains challenging. We propose Physics-Guided Residual Dynamics (PGRD), a hybrid simulation framework that combines the advantages of physics-based and learning-based approaches. Specifically, PGRD combines an optimizable spring-mass simulator as a backbone with a learned neural network that predicts residual corrections to the physics-based predictions. We adopt a velocity-based formulation to ensure stable simulation and a sliding-window transformer architecture to capture temporal dependencies. We show that PGRD produces more accurate results than both purely physics-based and learning-based methods on a set of diverse real-world deformable objects. We further demonstrate the utility of PGRD in two applications: manipulation planning via Model Predictive Control, including a language-conditioned setting with a generated goal image; and interactive simulation via action-conditioned video prediction by 3D Gaussian Splatting.

  </details>


- **[A 3DGS-Driven Dynamic Viewpoint and Vibrotactile Framework for Subsea Teleoperation Validated via fNIRS](https://arxiv.org/abs/2607.13067)**  
  *Fang Xu, Tianyu Zhou, Ruitong Tian, Md Jahidul Islam, Jing Du*  
  `2026-07-10` · `cs.RO` · [abs](https://arxiv.org/abs/2607.13067) · [pdf](https://arxiv.org/pdf/2607.13067.pdf)
  > 💡 提出结合3DGS动态视点和振动触觉的多模态框架，有效改善水下远程操作在不同延迟下的性能。

  <details><summary>Abstract</summary>

  Teleoperating remotely operated vehicles (ROVs) in flooded, cluttered infrastructure is fundamentally limited by narrow 2D egocentric views and subsea communication latency. We present a multimodal teleoperation architecture built on a ROS-Unity framework that decouples proactive spatial planning from reactive boundary avoidance. The system replaces static camera feeds with a Dynamic Adaptive Viewpoint System (DAVS), which uses continuous optimization and real-time 3D Gaussian Splatting (3DGS) to synthesize an occlusion-free exocentric viewpoint from onboard state estimation. To further reduce sensory workload, a torso-mounted vibrotactile suit maps local obstacle clearance to intuitive haptic proximity cues. The architecture was evaluated in a controlled human-subject study (N = 30) using a BlueROV2 navigating a complex simulated underwater facility. A 3 x 4 repeated-measures design compared three interaction modalities (Egocentric, Haptic, Exocentric) under four communication delays (0.0-1.0 s). Performance was quantified using behavioral measures and functional near-infrared spectroscopy (fNIRS) to assess task-evoked prefrontal activation. Results show that reactive haptic feedback improves path adherence under minimal delay, whereas the 3DGS-driven exocentric visualization provides superior resilience under severe latency (0.5-1.0 s), significantly outperforming the other modalities. fNIRS further revealed a cognitive disengagement effect: increasing latency during conventional egocentric teleoperation overloaded working memory and reduced prefrontal activation, whereas the proactive spatial context provided by DAVS sustained executive control. These findings demonstrate that spatially grounded, multimodal assistance can substantially improve operator performance and cognitive endurance during latency-degraded underwater teleoperation.

  </details>


</details>

<details><summary><b>Avatar / Human / Face</b> (2) · <a href="topics/avatar-human.md">full list →</a></summary>

- **[T3HG-Editor: Text-driven 3D Human Garment Editing with Body Priors Embedded in SMPL-X](https://arxiv.org/abs/2607.13654)**  
  *Shaoru Sun, Xingtao Wang, Zihan Ma, Wenrui Li, Jiantao Zhou, Debin Zhao, Xiaopeng Fan*  
  `2026-07-15` · `cs.CV` · [abs](https://arxiv.org/abs/2607.13654) · [pdf](https://arxiv.org/pdf/2607.13654.pdf)
  > 💡 利用SMPL-X先验播种高斯、聚合跨视图令牌并裁剪溢出高斯，实现高保真且一致的文本驱动3D服装编辑。

  <details><summary>Abstract</summary>

  While 3D Gaussian Editing (3DGE) has seen substantial progress, text-driven 3D human garment editing remains largely underexplored. Existing 3DGE works typically follow a paradigm that applies 2D editing techniques to multi-view rendered images and updates 3D Gaussians based on the modified images. Extending such methods to 3D human garment editing suffers from low-fidelity outcomes, caused by introduced distortions and garment inconsistencies. A promising breakthrough opportunity arises from the SMPL eXpressive (SMPL-X) model that embodies rich prior information for virtual humans. Motivated by this insight, we propose a text-driven 3D human garment editor termed T3HG-Editor, which delivers high-fidelity and garment consistent results by leveraging geometry and joint priors embedded in SMPL-X. Specifically, T3HG-Editor contains three stages, namely obtainment of editable Gaussians, garment consistent editing, and Gaussian updating with overflow pruning. The obtainment of editable Gaussians begins with seeding Gaussians along SMPL-X normals to generate sufficient near surface Gaussians, followed by a 2D mask constraint that precisely localizes the target Gaussians to be edited. The garment consistent editing aggregates tokens corresponding to the same SMPL-X vertex across multiple views and propagates them to their original views, enforcing garment consistency without requiring additional training. Gaussian updating with overflow pruning employs a Signed Distance Function (SDF) defined on SMPL-X to construct a human distance field, which is then integrated with a 2D semantic mask to prune overflowing Gaussians, thus preventing contamination of non-target regions. Experiments on multiple subjects and diverse garment types demonstrate that T3HG-Editor outperforms state-of-the-art methods in both editing quality and garment consistency.

  </details>


- **[Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation](https://arxiv.org/abs/2607.13154)**  
  *Lingxiao Guo, Huanyu Li, Guanya Shi*  
  `2026-07-14` · `cs.RO` · [abs](https://arxiv.org/abs/2607.13154) · [pdf](https://arxiv.org/pdf/2607.13154.pdf)
  > 💡 从单一RGBD演示重建高斯泼溅背景与轨迹，通过合成数据引擎生成多样化数据，实现开放世界移动操控的泛化。

  <details><summary>Abstract</summary>

  Learning open-world mobile manipulation policies requires vast data to achieve spatial generalization, long-horizon robustness, and scene generalization. Current prevailing data collection paradigms, teleoperation and UMI, demand prohibitive human effort and cost at scale. To scale beyond the limits of manual data collection, we seek to maximize the value of each human demonstration by scalable data generation. To this end, we introduce WANDA: learning open-World mobile mANipulation from one demonstration via a synthetic DAta engine. WANDA first reconstructs background Gaussian splats and robot-object interaction trajectories from source RGBD observations, as a world substrate for later planning and rendering. It then rearranges contact-rich robot-object interaction segments into extensive spatial configurations, utilizing whole-body motion planning to chain them into new trajectories. To enhance long-horizon robustness, it applies Corrective State Expansion to increase the robot and object state diversity at different stages of mobile manipulation. To unlock cross-environment generalization, trajectories are synthesized on diverse generated 3D worlds from everyday photos. Furthermore, we synthesize photo-realistic observations by compositing rendered robot and object meshes with Gaussian splatting backgrounds. We evaluate our approach on extensive simulation and real-world tasks in various scenes. Experiments show that policies trained with WANDA achieve long-horizon robustness, broad spatial generalization and cross-environment generalization from one real demonstration. Moreover, WANDA naturally supports cross-embodiment data generation, validated by zero-shot deployment on another mobile manipulator with a distinct morphology.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (1) · <a href="topics/compression.md">full list →</a></summary>

- **[Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808)**  
  *Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann*  
  `2026-07-15` · `cs.CV` · [abs](https://arxiv.org/abs/2607.13808) · [pdf](https://arxiv.org/pdf/2607.13808.pdf)
  > 💡 针对3DGS外观参数化开销大，提出解耦辐射表示结合空间hash网格烘焙纹理贴图，实现5倍加速的实时4K渲染。

  <details><summary>Abstract</summary>

  Recent extensions of 3D Gaussian Splatting (3DGS) capture fine color details using hash-grid-based appearance parameterization but incur high computational cost during fragment rendering. We introduce a decoupled radiance representation that models low-frequency geometry and view dependent appearance features with 2D surfels while representing high-frequency textures via a view-independent spatial hash grid that is baked into a compact texture atlas. By including sparsity-enhancing optimizations that penalize semi-transparency and per-primitive falloff, our method aggressively prunes insignificant surfels and achieves significantly faster and sparser reconstructions than prior work. Exploiting geometric sparsity and efficient GPU texture mapping, our approach achieves up to a fivefold speedup over 3DGS while preserving state-of-the-art visual fidelity, enabling real-time 4K rendering at 60 FPS on consumer hardware.

  </details>


</details>

<details><summary><b>Reconstruction / Geometry</b> (1) · <a href="topics/reconstruction.md">full list →</a></summary>

- **[COLMAR: Cooperative View Policy Learning for Multi-Agent Active 3D Reconstruction](https://arxiv.org/abs/2607.13524)**  
  *Phu Pham, Damon Conover, Aniket Bera*  
  `2026-07-15` · `cs.RO` · [abs](https://arxiv.org/abs/2607.13524) · [pdf](https://arxiv.org/pdf/2607.13524.pdf)
  > 💡 通过共享策略优化和重建感知目标，COLMAR解决了多智能体主动3D重建中的冗余观测问题，精度提升54%，覆盖率提升49%。

  <details><summary>Abstract</summary>

  Active 3D reconstruction requires selecting informative viewpoints under limited sensing budgets. In multi-agent settings, coordination inefficiencies such as redundant observations and spatial clustering can significantly reduce reconstruction quality. We present COLMAR, a cooperative view policy learning framework for multi-agent active 3D reconstruction. COLMAR formulates viewpoint allocation as a shared policy optimization over map-centric observations and introduces a reconstruction-aware objective that promotes overlap-aware coverage, team-level discovery, and collision-safe exploration. Dense feedback derived from incremental reconstruction updates aligns exploration behavior with downstream geometric quality. The policy is trained using parameter-sharing Proximal Policy Optimization (PPO) with independent per-agent action selection at deployment, conditioned on a fused team map and without inter-agent message passing for decision making. Selected viewpoints are then reconstructed with 3D Gaussian Splatting (3DGS) for high-fidelity photometric evaluation. Experiments on GLEAM and Replica demonstrate consistent improvements over heuristic and non-cooperative baselines, achieving up to 54% higher reconstruction accuracy and 49% greater coverage under matched sensing budgets.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
