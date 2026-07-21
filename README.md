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
| 1 | **Survey & Benchmark** | 84 | **+3** | [topics/survey.md](topics/survey.md) |
| 2 | **Dynamic / 4D / Streaming** | 288 | **+2** | [topics/dynamic-4d.md](topics/dynamic-4d.md) |
| 3 | **Avatar / Human / Face** | 47 | — | [topics/avatar-human.md](topics/avatar-human.md) |
| 4 | **Generation / Diffusion** | 73 | **+1** | [topics/generation.md](topics/generation.md) |
| 5 | **Editing / Stylization / Watermark** | 38 | **+1** | [topics/editing.md](topics/editing.md) |
| 6 | **Compression / Compact / Efficient Storage** | 45 | **+4** | [topics/compression.md](topics/compression.md) |
| 7 | **Rendering / Acceleration / Mobile** | 62 | **+2** | [topics/rendering.md](topics/rendering.md) |
| 8 | **SLAM / Localization / Mapping** | 18 | **+1** | [topics/slam.md](topics/slam.md) |
| 9 | **Autonomous Driving / Outdoor** | 18 | — | [topics/driving.md](topics/driving.md) |
| 10 | **Medical / Surgical** | 4 | — | [topics/medical.md](topics/medical.md) |
| 11 | **Relighting / Material / BRDF** | 8 | — | [topics/relighting.md](topics/relighting.md) |
| 12 | **Sparse-View / Few-shot / Generalizable** | 24 | **+1** | [topics/sparse-view.md](topics/sparse-view.md) |
| 13 | **Semantic / Scene Understanding** | 15 | — | [topics/semantic.md](topics/semantic.md) |
| 14 | **Reconstruction / Geometry** | 28 | — | [topics/reconstruction.md](topics/reconstruction.md) |
| 15 | **Others** | 10 | — | [topics/others.md](topics/others.md) |
<!-- TOPIC-INDEX-END -->

## Latest update

Only the most recent crawl day is shown inline. Day-by-day history older than 30 days is rotated into [`papers/YYYY-MM.md`](papers/); the canonical view of each sub-topic lives in [`topics/`](topics/).

<!-- LATEST-START -->

### 2026-07-21 (UTC) — 15 new paper(s)

<details><summary><b>Survey & Benchmark</b> (3) · <a href="topics/survey.md">full list →</a></summary>

- **[CaT-GS: Efficient 3DGS Rendering for Large Scale Scenes via Inter-frame Caching and Tile Scheduling](https://arxiv.org/abs/2607.17842)**  
  *Tingjia Zhang, Bo Chen, Shengzhong Liu, Fan Wu, Guihai Chen*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.17842) · [pdf](https://arxiv.org/pdf/2607.17842.pdf)
  > 💡 针对大规模3DGS渲染中冗余计算与负载不均，提出跨帧缓存与瓦片调度方法，实现10倍加速。

  <details><summary>Abstract</summary>

  Recent breakthroughs in 3D Gaussian Splatting (3DGS) have advanced neural rendering with high fidelity and speed. However, its performance degrades significantly in large-scale scenes due to the computational burden of tile-based rasterization. Existing optimization efforts either require costly scene re-training or focus on narrow aspects of the pipeline, overlooking critical inefficiencies in real-world deployments. Through a comprehensive analysis, we identify three primary sources of redundancy and low GPU utilization: redundant inter-frame pre-processing, viewpoint-based occlusion redundancy, and severe tile-level load imbalance. To address these issues, we propose CaT-GS, a novel and efficient 3DGS rendering pipeline. CaT-GS introduces a speculative multi-frame preprocessing method to eliminate redundant computations across consecutive frames, and an inter-frame caching mechanism to eliminate viewpoint redundant rendering stages. Furthermore, it refactors rasterization tasks with a dedicated kernel to mitigate tile load imbalance, significantly boosting GPU utilization. Extensive experiments demonstrate that CaT-GS achieves a speedup of up to 10 times over the original 3DGS and up to 70% over previous state-of-the-art methods, establishing a new benchmark for high-fidelity, real-time rendering of large-scale scenes.

  </details>


- **[Does Robust VIO Need More Learning? Geometry-Verified Visual Measurements under Distribution Shift](https://arxiv.org/abs/2607.17956)**  
  *Yangyang Ning, Shu Liang, Quanbo Ge, Tianchen Deng, Yuhua Qi, Shenghai Yuan*  
  `2026-07-20` · `cs.RO` · [abs](https://arxiv.org/abs/2607.17956) · [pdf](https://arxiv.org/pdf/2607.17956.pdf)
  > 💡 针对分布偏移下VIO鲁棒性，提出最小学习框架，

  <details><summary>Abstract</summary>

  Learning is increasingly introduced into visual-inertial odometry (VIO), ranging from learned feature front-ends to learning-dominant motion and geometry estimation. However, learning more of the pipeline does not necessarily improve robustness when deployment conditions differ from the training distribution. This work asks whether robust VIO under distribution shift truly requires deeper learned estimation, or whether learning can be confined to visual measurement generation. We propose a minimal-learning stereo VIO framework in which SEA-RAFT is used only to propose dense stereo correspondences and predict their uncertainty, while temporal tracking, geometric verification, and state estimation remain explicit. Dense flow is sampled at sparse feature locations, filtered using predicted uncertainty and stereo epipolar consistency, and incorporated into a sliding-window stereo-inertial estimator through uncertainty-weighted reprojection factors. The same uncertainty is further propagated through stereo triangulation for downstream anisotropic 3D Gaussian mapping. Experiments on EuRoC, VIODE, and 4Seasons demonstrate accurate and stable estimation under motion blur, dynamic scenes, illumination changes, and large indoor-to-outdoor distribution shifts. Ablations show that learned flow alone is insufficient: the gains arise from combining learned correspondence proposals with geometric verification and uncertainty-aware weighting. These results suggest that, for OOD-robust VIO, carefully integrated learned visual measurements can be more effective than learning a larger fraction of the estimation pipeline. Code and configs for the benchmark will be open-source upon acceptance. A supplementary video is available at https://drive.google.com/file/d/1EVRhOkhanmNXHbQS1Vr80FoEIAYOYOV2/view

  </details>


- **[GEAR: Reconstruction of Classical Paintings via Geometry Grounding and Appearance Restitution](https://arxiv.org/abs/2607.17519)**  
  *Qinyu Zhang, Xinda Liu, Yunchen Li, Yunzhuo Liu, Chenxi Hu, Kang Li, Guohua Geng*  
  `2026-07-20` · `cs.MM` · [abs](https://arxiv.org/abs/2607.17519) · [pdf](https://arxiv.org/pdf/2607.17519.pdf)
  > 💡 针对单幅古典绘画缺乏3D线索，提出无训练两阶段GeAR框架进行几何基础化与外观恢复，生成逼真3D场景，并构建HeriArch基准。

  <details><summary>Abstract</summary>

  Classical paintings preserve rich spatial, cultural, and historical content, making their reconstruction as explorable 3D scenes valuable for digital preservation, immersive exhibition, and cultural engagement. Yet, unlike photographs, they often depict scenes in a single-view, stylized manner, with weak perspective, lighting, and depth cues. Existing 3D reconstruction methods are largely built on natural-image priors, making it difficult to recover geometrically plausible and visually faithful 3D representations from such inputs. To address this challenge, we introduce Classical Painting-to-3D (CP3D), a new task that aims to recover a 3D representation from a single classical painting while jointly ensuring geometric plausibility, appearance fidelity to the source artwork, and plausible novel-view synthesis. We further propose GeAR, a training-free two-stage framework for Geometry Grounding and Appearance Restitution. GeAR first converts the input painting into a geometry-grounded representation with more coherent shading and illumination cues, improving the stability of 3D Gaussian reconstruction. It then restores artwork-faithful appearance across views under spatial constraints and multi-view consistency, recovering the painterly textures and details weakened during grounding. In addition, we construct HeriArch, a curated benchmark of 10,160 high-resolution classical artworks for systematic evaluation of CP3D. Extensive experiments and user studies show that GeAR consistently outperforms strong baselines in geometric plausibility, appearance fidelity, and human preference. Code and dataset will be released publicly.

  </details>


</details>

<details><summary><b>Dynamic / 4D / Streaming</b> (2) · <a href="topics/dynamic-4d.md">full list →</a></summary>

- **[Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based Error Concealment](https://arxiv.org/abs/2607.17916)**  
  *Yuxuan Tao, Xuerui Ma, Hao Zhang, Chunhua Peng*  
  `2026-07-20` · `cs.GR` · [abs](https://arxiv.org/abs/2607.17916) · [pdf](https://arxiv.org/pdf/2607.17916.pdf)
  > 💡 提出原子包装和GNN误差隐藏框架，在20%丢包下将3DGS渲染PSNR下降限制至约3dB。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) and recent compression schemes such as HAC++ enable high-fidelity real-time neural rendering, but their bitstreams are fragile under packet loss during network streaming. Existing compression methods often separate correlated anchor attributes into independent streams, so losing one packet can create attribute-inconsistent broken anchors and severe rendering artifacts. We propose a packet-loss robust 3DGS transmission and error concealment framework. On the encoder side, anchor-level atomic packaging jointly encapsulates all attributes of each anchor, converting corrupted-attribute failures into clean missing-anchor erasures. Stratified random grouping further disperses packet losses across the spatial domain to avoid large contiguous voids. On the decoder side, we formulate recovery as prior-aware attribute inpainting. A Context-Aware Residual Interpolation (CARI) branch uses hash-grid prior predictions and neighboring residuals to build a robust baseline, while a lightweight two-layer graph neural network with cross-attention over hash-grid priors refines high-frequency attribute residuals. Attribute-wise confidence control falls back to interpolation when learned predictions are unreliable. Experiments under 20 percent random packet loss on BungeeNeRF, Mip-NeRF 360, and Tanks and Temples show that the proposed method substantially improves over no-concealment transmission and limits average PSNR degradation to about 3 dB relative to the lossless HAC++ reference.

  </details>


- **[OmniStyle-INR: Universal and Multimodal Style Transfer for INRs](https://arxiv.org/abs/2607.16362)**  
  *Rafał Kajca, Michał Miziołek, Kornel Howil, Rafał Tobiasz, Przemysław Spurek*  
  `2026-07-17` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16362) · [pdf](https://arxiv.org/pdf/2607.16362.pdf)
  > 💡 针对高斯溅射在连续域

  <details><summary>Abstract</summary>

  Style transfer remains a fundamental and highly important task across various data modalities, enabling creative manipulation conditioned by both reference images and textual descriptions. Recently, methods utilizing Gaussian Splatting have emerged as a unified representation for 2D images, video, 3D scenes, and 4D dynamics. However, representing videos and 2D images with Gaussian Splatting is structurally sub-optimal for dense continuous domains. The number of required Gaussians often approaches the total number of pixels, raising questions about the actual utility of such a representation for these specific modalities. In contrast, Implicit Neural Representations have established themselves as a much more popular and natural choice across all these data domains. Implicit Neural Representations naturally provide significant advantages, including data compression, inherent capabilities for super resolution, and seamless integration with deep generative models. To this end, we introduce OmniStyle-INR, a novel framework that leverages network-based continuous representations as a truly universal domain. Our approach successfully performs high-quality style transfer across all visual modalities, guided seamlessly by both text prompts and visual exemplars.

  </details>


</details>

<details><summary><b>Generation / Diffusion</b> (1) · <a href="topics/generation.md">full list →</a></summary>

- **[FillGauss: Fine-Grained Filling-Aware Impact Sound Generation for 3D Gaussian Splatting](https://arxiv.org/abs/2607.17773)**  
  *Chen Yang, Ganye Wen, Bin Huang, Jiayi Lyu, Zehai Niu, Linlin Shen, Jinbao Wang*  
  `2026-07-20` · `cs.MM` · [abs](https://arxiv.org/abs/2607.17773) · [pdf](https://arxiv.org/pdf/2607.17773.pdf)
  > 💡 针对忽略内部填充状态导致声学失真的问题，提出FillGauss框架，融合3DGS几何特征与潜扩散生成高保真冲击声。

  <details><summary>Abstract</summary>

  Synthesizing physically plausible impact sounds from visual observations remains a great challenge in multi-modal AI. Existing 3D-aware audio generation methods primarily model the surface geometry of hollow rigid bodies. However, they fundamentally overlook internal filling states, a critical physical factor that drastically modulates acoustic resonance and damping. To address this issue, we have defined a new task called Fine-Grained Filling-Aware Impact Sound Generation. As a foundational step, we first introduce the fine-grained fill-aware dataset (FillImpact), a pioneering multi-modal collection comprising over 5,000 rigorous acoustic recordings from 88 diverse real-world objects. It captures impact interactions with varying internal contents (i.e., water, rice), a continuous range of fill levels, and distinct striker materials. Furthermore, comprehensive acoustic analysis confirms that the collected data closely aligns with established physical laws governing acoustic resonance and damping, indicating its suitability for physically grounded modeling. Building on this dataset, we propose a novel generative framework (FillGauss) that integrates 3D Gaussian Splatting (3DGS) with internal state conditioning for sound generation. By fusing 3DGS geometric features, precise 3D spatial strike coordinates, and fine-grained textual physical conditions within a latent diffusion architecture, FillGauss enables position-aware, striker-aware, and filling-aware audio generation. Extensive experiments demonstrate that our approach could generate high-fidelity impact sounds that adhere to underlying physical principles, establishing a new state-of-the-art for physically grounded cross-modal audio generation.

  </details>


</details>

<details><summary><b>Editing / Stylization / Watermark</b> (1) · <a href="topics/editing.md">full list →</a></summary>

- **[FF-ProCams: Feed-Forward Gaussian Splatting for Projector-Camera System](https://arxiv.org/abs/2607.17803)**  
  *Ziyao Wang, Yuqi Li, Wenxing Zheng, Jiaying Chen, Chong Wang*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.17803) · [pdf](https://arxiv.org/pdf/2607.17803.pdf)
  > 💡 提出前馈高斯泼溅框架FF-ProCams，用混合编码器预测可重照明高斯体，实现投影仪-相机系统的高效

  <details><summary>Abstract</summary>

  Projector-camera (ProCams) systems achieve active scene perception and controllable appearance manipulation via structured illumination, serving as a core infrastructure for spatial augmented reality, projection mapping, and surface reflectance acquisition. Existing inverse-rendering methods for ProCams deliver high-fidelity results but rely on time-consuming per-scene optimization, while mainstream feed-forward 3D reconstruction models produce baked appearance that cannot adapt to spatially varying projector illumination. To resolve this accuracy-efficiency trade-off, we propose FF-ProCams, a Feed-Forward 3D Gaussian inverse-rendering framework for ProCams. A hybrid Mamba2-Transformer encoder aggregates cross-view geometric and photometric cues from sparse multi-view observations, and lightweight heads predict a relightable Gaussian representation in a single forward pass. We further design a projector-aware differentiable renderer to synthesize camera observations under arbitrary active illumination and ProCams poses. To enable feed-forward training, we construct a large-scale synthetic ProCams dataset covering diverse object geometries and surface materials. Experiments show FF-ProCams achieves high-fidelity projector-aware rendering, generalizes to unseen patterns, and supports novel projector-camera poses. Using only 8 input views, it outperforms optimization-based baselines with 297 views while reducing test-time reconstruction to 0.13 seconds (a three-to-five-order-of-magnitude speedup). The code and data are available at https://github.com/CPREgroup/FF-ProCams/.

  </details>


</details>

<details><summary><b>Compression / Compact / Efficient Storage</b> (4) · <a href="topics/compression.md">full list →</a></summary>

- **[QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2607.18067)**  
  *Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.18067) · [pdf](https://arxiv.org/pdf/2607.18067.pdf)
  > 💡 利用量子启发非正交函数压缩，通过重叠矩阵和密度矩阵选择子空间，减少高斯数量71.7%，提升渲染速度34.3%。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves high-quality real-time rendering by representing a scene with a large collection of anisotropic Gaussian primitives. However, complex scenes often require millions of Gaussians, resulting in substantial storage and rendering costs. Existing compression methods mainly reduce redundancy through primitive-wise pruning, attribute quantization, clustering, or neural coding, while redundancy caused by strongly overlapping and non-orthogonal Gaussian basis functions remains largely unexplored. We present QIRF, a quantum-inspired non-orthogonal function-space compression method for 3D Gaussian Splatting. QIRF models neighboring Gaussian primitives as a local non-orthogonal basis and formulates primitive reduction as a subspace-aware selection problem. Specifically, an analytic Gaussian overlap matrix and a radiance-response density matrix are constructed to characterize functional redundancy and rendering relevance. Generalized eigendecomposition is then used to identify the dominant local subspace and select representative Gaussian primitives. An RRDM-based response model and detail-aware safeguarding further preserve visually important high-frequency structures under aggressive pruning. Experiments on 13 scenes from Mip-NeRF 360, Tanks and Temples, and Deep Blending show that QIRF reduces the Gaussian count and raw PLY storage by 71.7 percent on average, corresponding to approximately 3.54 times compression, while maintaining reconstruction quality comparable to 3DGS and achieving a marginal average PSNR improvement of 0.10 dB. QIRF also improves the average rendering speed over 3DGS by 34.3 percent. These results suggest that non-orthogonal function-space redundancy is an important yet underexplored source of representational redundancy in explicit Gaussian radiance fields.

  </details>


- **[TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting](https://arxiv.org/abs/2607.16838)**  
  *Shanshan Pan, Jiale Chen, Yilin Liu, Hui Huang*  
  `2026-07-18` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16838) · [pdf](https://arxiv.org/pdf/2607.16838.pdf)
  > 💡 针对3DGS平面重建缺乏拓扑连接导致碎片化问题，TopoGS通过引入平面与拓扑约束及全局2D拓扑关系，生成连贯精准的3D场景。

  <details><summary>Abstract</summary>

  Extracting structured, parametric 3D representations from raw images remains a fundamental challenge in computer vision and graphics. While recent advancements in the 3D Gaussian Splatting (3DGS) pipeline integrate planar primitives to yield compact and editable geometry, these approaches typically treat planes as isolated, discrete sets. This lack of topological connectivity hinders robust geometric reasoning, leading to fragmented reconstructions and misaligned boundaries that fall short of the precision for rigorous spatial analysis and professional design workflows. To address this, we introduce TopoGS, the first 3DGS framework to explicitly integrate both planar and topological constraints for coherent 3D reconstruction. Specifically, we extract global 2D topological relationships from multi-view image segmentations and anchor Gaussian primitives to these structural elements. This formulation enables the joint optimization of plane parameters, rendering fidelity, and topological adjacency. By enforcing strict multi-view consistency alongside these topological constraints, our method significantly mitigates geometric misalignments and produces connected, structured 3D models. Extensive evaluations on the ScanNet++ dataset demonstrate that TopoGS achieves state-of-the-art performance, providing a highly robust solution for generating accurate, topologically sound, and visually faithful scene representations.

  </details>


- **[SPARE-GS: Structural Parsimony and Resource Efficiency for 3D Gaussian Splatting](https://arxiv.org/abs/2607.16624)**  
  *Zhang Chen, Shuai Wan, Fuzheng Yang, Jiazhi Xia, Weiyao Lin, Junhui Hou*  
  `2026-07-18` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16624) · [pdf](https://arxiv.org/pdf/2607.16624.pdf)
  > 💡 针对3DGS原语过多问题，提出全局预算约束优化框架，动态调整原语分布，降低高斯数和训练时间并提升质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves high-fidelity novel view synthesis in real-time; however its training efficiency and representation compactness are hindered by excessive primitive proliferation. To address this challenge, we formulate the structural evolution of 3DGS as a global budget-constrained optimization problem and derive an optimality condition, which requires the marginal utility of structural resources to be balanced across spatial regions under a finite primitive budget. Based on this formulation, we propose SPARE-GS, a general plug-and-play framework that dynamically aligns the distribution of 3D Gaussian primitives with regional representational demand. SPARE-GS estimates capacity-normalized regional demand, assigns adaptive target quotas, and uses regional budget deviations to coordinate densification, pruning and adaptive termination toward a more balanced structural allocation. Extensive experiments across standard, accelerated, and structure-enhanced 3DGS pipelines demonstrate that SPARE-GS reduces the Gaussian count and training time by an average of 30.38% and 23.81%, respectively, while improving the average PSNR. Moreover, the resulting compact representations reduce downstream processing time and improve the rate-distortion performance of diverse compression and pruning methods, demonstrating the broad applicability of global structural budget regulation.

  </details>


- **[SaaF: Scene-Specific Ambiguity-Aware 3D Language Fields towards Interactive Real-World Object Retrieval](https://arxiv.org/abs/2607.16309)**  
  *Yuga Yano, Daiju Kanaoka, Hakaru Tamukoh, Yasutomo Kawanishi*  
  `2026-07-14` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16309) · [pdf](https://arxiv.org/pdf/2607.16309.pdf)
  > 💡 针对3D语言场特征压缩和查询歧义问题，提出度量学习构建判别性且模糊感知的统一特征空间，提升交互式物体检索准确率。

  <details><summary>Abstract</summary>

  We propose Scene-specific Ambiguity-aware 3D Language Fields (SaaF), a novel Gaussian Splatting-based 3D language field designed for interactive object retrieval in a given real-world scene. Interactive object retrieval using natural language is a crucial capability for service robots operating in complex real-world environments. While recent 3D language field methods for object retrieval establish associations between rendered pixels and autoencoder-compressed CLIP features, they suffer from two limitations: (1) reduced discriminability among similar objects due to feature compression, and (2) poor handling of ambiguous queries, often resulting in unstable or incorrect retrieval. To address these limitations, SaaF introduces a metric learning strategy to construct a unified feature space that is both instance-discriminative and ambiguity-aware. (i) To enhance instance-level visual discrimination, SaaF employs metric learning that pulls image features from multiple viewpoints of the same object closer together in the feature space. (ii) To establish ambiguity awareness, the model jointly trains on multiple text labels generated by the proposed method from each tracked object image sequence, including ambiguous descriptions, to learn the semantic relationships between ambiguous and specific features in a target scene. This feature space enables fine-grained visual understanding while allowing the system to estimate query ambiguity and interactively request clarification when needed. Experimental results demonstrate that SaaF not only improves retrieval accuracy over previous methods but also robustly detects and handles ambiguity in the user text queries under open-vocabulary settings.

  </details>


</details>

<details><summary><b>Rendering / Acceleration / Mobile</b> (2) · <a href="topics/rendering.md">full list →</a></summary>

- **[Exploration Matters for Escaping the Blur Trap in 3D Gaussian Splatting](https://arxiv.org/abs/2607.17965)**  
  *Chengbo Wang, Guozheng Ma, Jinhong Wu, Tie Ji, Yizhen Lao*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.17965) · [pdf](https://arxiv.org/pdf/2607.17965.pdf)
  > 💡 指出3DGS优化中的模糊陷阱问题，提出随机播种和随机分裂两种探索策略，成功逃离局部最优，提升渲染质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) employs Gaussian primitives for explicit scene representation, facilitating real-time, high-fidelity reconstruction and novel view synthesis of complex scenes. However, the explicit modeling inherent in 3DGS introduces a gradient bias during optimization, rendering its non-convex optimization process highly susceptible to convergence toward local suboptimal solutions. This constitutes a fundamental limitation in 3DGS optimization, which we term the Blur Trap. To address this limitation, we integrate simple explicit exploration into the 3DGS optimization framework. First, through rigorous mathematical analysis of the 3DGS optimization formulation, we identify the underlying optimization bias responsible for the Blur Trap and categorize it into two distinct subtypes: the Far-Side Blur Trap and the Near-Side Blur Trap. Subsequently, we propose two highly straightforward exploration strategies (Random Seeding and Random Splitting) to mitigate the far-side and near-side blur traps, respectively. Experimental validation demonstrates that the incorporation of these exploration operators effectively and complementarily overcome the Blur Trap, achieving high-quality rendering performance across multiple datasets. Project page: https://chengbo-wang.github.io/ExploreGS/

  </details>


- **[Locality-Aware Density Control for Efficient Gaussian-based Image Representation](https://arxiv.org/abs/2607.17896)**  
  *Jiacong Chen, Qingyu Mao, Xiandong Meng, Shuai Liu, Chao Li, Fanyang Meng, Youneng Bao, Yongsheng Liang*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.17896) · [pdf](https://arxiv.org/pdf/2607.17896.pdf)
  > 💡 针对2DGS中高斯容量分配效率低的问题，提出LocoADC框架，通过区域致密化与相似合并策略，显著提升图像重建质量。

  <details><summary>Abstract</summary>

  2D Gaussian Splatting is an attractive direction for image representation due to its explicit formulation, fast rasterization, and favorable decoding efficiency. The representation quality of this paradigm depends on the proper allocation of Gaussian capacity to the demanding regions. However, existing methods fail to allocate Gaussian capacity efficiently during optimization: under-reconstructed content is often refined in a fragmented pixel-wise manner, while neighboring optimized Gaussians with similar attributes are redundantly retained. This inefficiency motivates the need for a density control framework that jointly addresses insufficient allocation in under-reconstructed regions and redundant allocation in over-reconstructed regions. Our key insight is that this framework should exploit two complementary forms of locality: the local continuity of reconstruction errors in image space for improved Gaussian allocation, and the local similarity of neighboring Gaussians in Gaussian space for redundant elimination. Based on this insight, we propose Locality-Aware Density Control (LocoADC), a plug-and-play framework that improves Gaussian capacity utilization through Region-wise Gaussian Densification (RGD) and Similarity-Driven Gaussian Merging (SDGM) strategies, together with a local color consistency constraint for more reliable merging. Extensive experiments on diverse datasets show that LocoADC consistently improves multiple baselines by enabling more effective local Gaussian allocation, including a 2.93 dB PSNR gain over GI on the CLIC dataset under the same 30k Gaussian budget. Code is available at: \textit{https://github.com/ChenJiaCong-1005/LocoADC}.

  </details>


</details>

<details><summary><b>SLAM / Localization / Mapping</b> (1) · <a href="topics/slam.md">full list →</a></summary>

- **[Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926)**  
  *Hyeonjoong Jang, Dongyoung Choi, Donggun Kim, Woohyun Kang, Min H. Kim*  
  `2026-07-18` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16926) · [pdf](https://arxiv.org/pdf/2607.16926.pdf)
  > 💡 针对极端运动模糊，提出结合高斯泼溅与光流ICP的RGB-D重建方法，实现高质量3D场景重建。

  <details><summary>Abstract</summary>

  We propose a splat-based 3D scene reconstruction method from RGB-D input that effectively handles extreme motion blur, a frequent challenge in low-light environments. Under dim illumination, RGB frames often suffer from severe motion blur due to extended exposure times, causing traditional camera pose estimation methods, such as COLMAP, to fail. This results in inaccurate camera pose and blurry color input, compromising the quality of 3D reconstructions. Although recent 3D reconstruction techniques like Neural Radiance Fields and Gaussian Splatting have demonstrated impressive results, they rely on accurate camera trajectory estimation, which becomes challenging under fast motion or poor lighting conditions. Furthermore, rapid camera movement and the limited field of view of depth sensors reduce point cloud overlap, limiting the effectiveness of pose estimation with the ICP algorithm. To address these issues, we introduce a method that combines camera pose estimation and image deblurring using a Gaussian Splatting framework, leveraging both 3D Gaussian splats and depth inputs for enhanced scene representation. Our method first aligns consecutive RGB-D frames through optical flow and ICP, then refines camera poses and 3D geometry by adjusting Gaussian positions for optimal depth alignment. To handle motion blur, we model camera movement during exposure and deblur images by comparing the input with a series of sharp, rendered frames. Experiments on a new RGB-D dataset with extreme motion blur show that our method outperforms existing approaches, enabling high-quality reconstructions even in challenging conditions. This approach has broad implications for 3D mapping applications in robotics, autonomous navigation, and augmented reality. Both code and dataset are publicly available on https://github.com/KAIST-VCLAB/gs-extreme-motion-blur.

  </details>


</details>

<details><summary><b>Sparse-View / Few-shot / Generalizable</b> (1) · <a href="topics/sparse-view.md">full list →</a></summary>

- **[Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://arxiv.org/abs/2607.16946)**  
  *Nicole Feng, Ioannis Gkioulekas, Keenan Crane*  
  `2026-07-18` · `cs.GR` · [abs](https://arxiv.org/abs/2607.16946) · [pdf](https://arxiv.org/pdf/2607.16946.pdf)
  > 💡 通过局部圆环拟合点云并利用预训练网络预测曲率参数，实现快速点态有符号距离计算，无需全局优化或离散化。

  <details><summary>Abstract</summary>

  We describe a method for computing signed distance to point clouds that allows fast pointwise evaluation at arbitrary spatial resolution. As input, our method takes a point cloud with normals; as output, it provides an analytical parameterization that allows queries of signed distance to the approximate underlying surface at arbitrary points - simultaneously providing reconstruction and distance. Our key idea is to reconstruct shapes by locally fitting point clouds with tori, which have closed-form signed distance functions. Tori are fitted in a feed-forward manner, using a pre-trained network to output per-point curvature and shift parameters. Importantly, our method does not require costly global optimization or spatial discretization, and is easily parallelizable. Underlying our method is a new theory that unifies signed distance with the classic reconstruction methods of winding numbers and Poisson surface reconstruction. We use our method to compute signed distance to point clouds arising from photogrammetry, meshes, 3D Gaussians, and neural implicits. Our method allows point clouds to be used directly in applications, without explicit surface reconstruction: as examples, we take offsets of point clouds, apply morphological and Boolean operations, and directly visualize offset surfaces using sphere tracing.

  </details>


</details>
<!-- LATEST-END -->
<!-- AUTO-GENERATED-END -->
