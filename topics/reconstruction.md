# Reconstruction / Geometry

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---

## 2026-05-30

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

