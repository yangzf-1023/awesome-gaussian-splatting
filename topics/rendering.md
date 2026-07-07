# Rendering / Acceleration / Mobile

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---














## 2026-07-07

- **[Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209)**  
  *Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård*  
  `2026-07-03` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03209) · [pdf](https://arxiv.org/pdf/2607.03209.pdf)
  > 💡 利用3D基础模型初始化位姿和点云，联合深度引导优化与MLP位姿细化，实现无SfM的3分钟高质量3DGS重建。

  <details><summary>Abstract</summary>

  This paper introduces a fast method for high-quality 3D Gaussian Splatting (3DGS) reconstruction without traditional Structure-from-Motion (SfM). The proposed approach leverages 3D Foundation Models (3DFMs) for camera pose and point-cloud initialization, then jointly optimizes both camera poses and Gaussian primitives using a depth-guided loss function. This enables fast convergence even from rough initialization with as few as 50-60 input views. To further improve reconstruction quality in sparse-view scenarios, an MLP-based pose refinement module is introduced alongside depth-guided supervision from the foundation model. Extensive experiments on Mip-NeRF 360, Tanks and Temples, and RobustNeRF demonstrate that the proposed method achieves competitive reconstruction quality (23.61 dB PSNR, 0.19 LPIPS) while reducing training time to approximately three minutes per scene. The proposed method produces ready-to-use 3DGS models at a fraction of the time required by existing pipelines, making it suitable for near real-time applications in robotics, VR, and autonomous navigation.

  </details>

## 2026-07-02

- **[FastBridge: Closing the Model-Based Realization Gap in Safety Filters on 3D Gaussian Splatting for Fast Quadrotor Flight](https://arxiv.org/abs/2607.01200)**  
  *Tscholl Dario, Nakka Yashwanth Kumar, Gunter Brian*  
  `2026-07-01` · `cs.RO` · [abs](https://arxiv.org/abs/2607.01200) · [pdf](https://arxiv.org/pdf/2607.01200.pdf)
  > 💡 针对3DGS安全滤波器忽略执行器限制问题，提出全四旋翼动力学的执行器感知碰撞锥CBF，降低急动度47%、加速2.25倍。

  <details><summary>Abstract</summary>

  Fast quadrotor flight requires safe obstacle avoidance under tight onboard compute limits. While 3D Gaussian Splatting (3DGS) provides a continuous, geometry-aware scene representation for perception-driven navigation, existing 3DGS safety filters use reduced-order models such as single- and double-integrators that ignore actuator limits and assume commanded accelerations are realized instantaneously. Building on an analytic collision cone barrier for 3DGS, we introduce a nonlinear, actuator-aware safety filter enforced through the full quadrotor dynamics. We derive a high-relative-degree collision cone exponential CBF and a backup CBF that preserves QP feasibility under input constraints using a forward-simulated backup policy. Compared with a state-of-the-art 3DGS safety filter, our approach reduces trajectory jerk by 47% and runs 2.25 times faster. We validate the method in simulation and on hardware for real-time navigation in cluttered, perception-derived environments.

  </details>

## 2026-07-01

- **[AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556)**  
  *Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath, Michael Niemeyer, Keisuke Tateno*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.31556) · [pdf](https://arxiv.org/pdf/2606.31556.pdf)
  > 💡 利用辐射场合成新视图辅助高斯溅射优化，解决稀疏视图下初始几何敏感问题，提升重建质量并保持实时渲染。

  <details><summary>Abstract</summary>

  Generating high-quality novel views at real-time frame rates remains a central challenge in 3D vision, particularly in sparse-view scenarios. Neural radiance fields have demonstrated robust reconstruction from limited observations, but their reliance on volumetric rendering leads to high computational cost and slow inference. In contrast, Gaussian Splatting methods achieve real-time rendering through rasterization, but their optimization is highly sensitive to the quality of the initial geometry. This sensitivity becomes especially problematic in sparse-view settings, where limited observations often lead to incomplete or noisy point-cloud reconstructions. In this work, we present AugSplat, a simple framework for improving Gaussian Splatting in sparse-view regimes using radiance-field-based view augmentation. We first train a radiance field on the sparse input views and use it to synthesize additional images from nearby novel viewpoints, increasing the effective view-space coverage available for supervision. These synthetic views are then used as auxiliary supervision during Gaussian Splatting optimization. We study two variants: Staged AugSplat, which uses synthetic views for an initial optimization phase before switching to real images, and Dual AugSplat, which jointly trains on real and synthetic views with a decaying synthetic loss weight. Experiments on sparse-view mip-NeRF 360 scenes show that AugSplat improves reconstruction quality over standard Gaussian Splatting. Staged AugSplat achieves the strongest average performance, while Dual AugSplat provides a closely performing formulation that keeps real-image supervision active throughout training, and both variants preserve real-time rendering at inference.

  </details>

- **[GRay: Ray Tracing 3D Gaussians Near the Speed of Splats](https://arxiv.org/abs/2606.30869)**  
  *Yohan Poirier-Ginter, Jean-François Lalonde, George Drettakis*  
  `2026-06-29` · `cs.GR` · [abs](https://arxiv.org/abs/2606.30869) · [pdf](https://arxiv.org/pdf/2606.30869.pdf)
  > 💡 利用射线追踪仅相交评估的对数缩放特性，通过密集初始化加速，实现接近光栅化速度的3D高斯射线追踪。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a popular representation for radiance field reconstruction, distinguished by the rendering speed of its rasterization-based renderer. While 3D Gaussians can also be ray traced, this approach has so far been slower, with 3D Gaussian Ray Tracing (3DGRT) taking nearly one order of magnitude longer to optimize. To address this, we present GRay, a fast ray tracer for 3D Gaussians designed to close this performance gap and match 3DGS's speed. Our method leverages the algorithmic difference between both approaches: unlike rasterization, ray tracing evaluates only Gaussians that are actually intersected by a ray, leading to potentially logarithmic--rather than linear--scaling in the number of primitives. This property allows ray tracing to better exploit dense scenes composed of numerous tiny Gaussians, a configuration which has largely been overlooked. Notably, we show that dense initialization--which creates many small Gaussians--slows down rasterization, but instead speeds up ray tracing. Designed to leverage this effect, GRay renders nearly 4x faster and optimizes nearly 10x faster than 3DGRT while maintaining similar quality, and has competitive speed with 3DGS albeit at somewhat lower quality. Code is available at https://repo-sam.inria.fr/nerphys/gray.

  </details>

- **[GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809)**  
  *Annika Thomas, Mason Peterson, Jonathan P. How*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30809) · [pdf](https://arxiv.org/pdf/2606.30809.pdf)
  > 💡 现有3DGS均匀分配容量浪费资源，GaussLite提出任务驱动的稀疏化映射，通过LLM解析和开放词汇检测按需分配密度，在资源受限硬件上实时重建，ROI PSNR提升超2.7dB。

  <details><summary>Abstract</summary>

  Existing 3D Gaussian Splatting (3DGS) systems distribute representation capacity uniformly across a scene, ignoring the fact that many downstream robotic tasks engage only a fraction of the reconstructed geometry. This causes valuable onboard compute to be allocated towards optimizing irrelevant parts of the scene, either limiting online capacity or under-optimizing the most relevant parts of the scene. We introduce GaussLite, a task-driven 3DGS mapping system that conditions its representation density on a natural-language task specification. Given a posed RGB-D stream and a task such as "prepare to pick up the object on the desk," GaussLite uses a one-shot LLM parser to extract target and anchor objects, which are grounded per-frame by an open-vocabulary detector and segmented to produce per-pixel relevance masks in real time. The mapper allocates seeding density, gradient flow and scaling by task relevance. At matched Gaussian budget and real-time mapping at 4 Hz on resource-constrained hardware, GaussLite outperforms baselines on ROI PSNR on the Replica Dataset by an average +2.72 dB and on a real-hardware demonstration in indoor and outdoor settings by +2.23 dB. We further show that two task-specialized agents' maps can be fused into a single shared map via per-voxel voting on active-optimization counts in real time, outperforming concatenation by +3.42 dB while only sharing an average 7.08% of the map.

  </details>

## 2026-06-30

- **[StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors](https://arxiv.org/abs/2606.30545)**  
  *Wenhao Yuan, Yiyuan Ge, Deli Cai*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30545) · [pdf](https://arxiv.org/pdf/2606.30545.pdf)
  > 💡 针对稀疏视图下3DGS过拟合与几何缺陷，引入立体先

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has achieved remarkable success in real-time novel view synthesis, yet it suffers from severe overfitting under sparse-view settings due to insufficient geometric constraints. While recent methods introduce monocular depth priors to mitigate this, they inherently struggle with scale ambiguity and cross-view inconsistency, leading to defective geometry. In this paper, we propose StereoGS, a novel sparse-view 3DGS framework that integrates stereo priors to establish reliable binocular consistency. Unlike scale-agnostic monocular constraints, StereoGS introduces a Stereo Depth Regularization by constructing virtual stereo pairs during optimization and leveraging a foundation stereo model to enforce absolute scale and binocular-consistent structures. To further suppress overfitting and eliminate redundant primitives, we design a Gradient-Aware Opacity Decay strategy that dynamically penalizes Gaussians based on their relative opacity gradient magnitudes. Combined with a Consistency-Aware Dense Initialization using zero-shot multi-view depth estimation, StereoGS effectively anchors primitives to accurate scene surfaces. Extensive experiments on LLFF, DTU, Mip-NeRF360, and Blender datasets demonstrate that StereoGS achieves state-of-the-art performance in sparse-view settings without incurring any additional inference overhead. Project Page: https://stringerywh00.github.io/StereoGS_project_page/

  </details>

- **[UniTriSplat: A Unified 3D Gaussian Splatting Framework with Uniform Spherical Rasterization for Universal Cameras](https://arxiv.org/abs/2606.29794)**  
  *Yipeng Zhu, Huajian Huang, Tristan Braud, Sai-Kit Yeung*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29794) · [pdf](https://arxiv.org/pdf/2606.29794.pdf)
  > 💡 针对不同相机模型采样不一致问题，提出基于HEALPix球面均匀光栅化的统一3DGS框架，提升跨相机泛化与重建质量。

  <details><summary>Abstract</summary>

  Existing 3D Gaussian Splatting (3DGS) frameworks rely on camera-specific rasterization, suffering from inconsistent solid-angle sampling and degraded performance across heterogeneous camera models (e.g., perspective, fisheye, omnidirectional). To address this limitation, we propose UniTriSplat, a unified 3DGS framework for universal cameras that reformulates Gaussian splatting on the unit sphere via HEALPix discretization. Leveraging the equal-area property of HEALPix, we construct a spherical sampling grid aligned with the angular resolution of input images. We derive the forward rendering and gradient propagation of Gaussians directly in the spherical radian domain, yielding uniform optimization behavior from narrow-FoV images to full 360-degree panoramas. To enhance perceptual reconstruction quality, we additionally introduce a HEALPix-aware SSIM loss that respects spherical neighborhood structure. Extensive experiments across diverse camera models demonstrate that UniTriSplat consistently improves cross-camera generalization while preserving geometric fidelity and rendering quality.

  </details>

- **[MyGO-Splat: Multi-Objective Closed-Loop Geometric Feedback for RGB-Only Gaussian SLAM](https://arxiv.org/abs/2606.29738)**  
  *Fan Zhu, Ziyu Chen, Zhenjun Zhao, Zhisong Xu, Hui Zhu, Mingrui Li, Chunmao Jiang, Javier Civera*  
  `2026-06-29` · `cs.RO` · [abs](https://arxiv.org/abs/2606.29738) · [pdf](https://arxiv.org/pdf/2606.29738.pdf)
  > 💡 单目SLAM尺度模糊且缺少几何自校正，MyGO-Splat通过闭环Gaussian光栅化深度与法线及尺度自适应对齐，提升尺度稳定性，性能媲美RGB-D。

  <details><summary>Abstract</summary>

  Real-time monocular Simultaneous Localization and Mapping (SLAM) fundamentally suffers from scale ambiguity and a lack of geometric self-correction. While 3D Gaussian Splatting (3DGS) enables high-fidelity rendering, existing RGB-only systems remain open-loop because depth priors are injected into mapping but refined geometry cannot effectively regulate tracking drift. We present MyGO-Splat, a closed-loop Gaussian SLAM framework that analytically rasterizes Gaussian primitives into pixel-wise depth and surface normals, allowing the map to actively supervise camera pose optimization. To bridge monocular priors and scale consistency, our framework introduces scale-aware adaptive alignment that projects foundation-model depth estimates into the globally optimized Gaussian space, forming a self-correcting cycle for scale feedback. Extensive evaluations show that this closed-loop design improves scale stability and appearance-geometry consistency, achieving performance comparable to RGB-D methods while using only monocular input.

  </details>

- **[Resonant Brane Splatting for Arbitrary-Scale Super-Resolution](https://arxiv.org/abs/2606.29453)**  
  *Giulio Federico, Giuseppe Amato, Claudio Gennaro, Fabio Carrara, Marco Di Benedetto*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29453) · [pdf](https://arxiv.org/pdf/2606.29453.pdf)
  > 💡 针对高斯平滑导致的稀疏性问题，RBS引入带高斯-埃尔

  <details><summary>Abstract</summary>

  Arbitrary-Scale Super-Resolution (ASR) reconstructs images at continuous magnification factors. Recent methods accelerate inference by replacing computationally heavy implicit neural decoders with explicit 2D Gaussian Splatting (GS). However, since standard Gaussians are smooth low-pass primitives, modeling edges and fine textures requires multiple overlapping, well-aligned splats, which creates severe bottlenecks during rasterization. To address this, we introduce Resonant Brane Splatting (RBS), a feed-forward ASR framework. RBS replaces flat Gaussians with Branes: expressive primitives that emit spatially varying colors to natively model local contrast and complex textures within a single footprint. We achieve this by augmenting the standard Gaussian envelope with internal Gaussian-Hermite modes, assigning a distinct color coefficient to each. The zero-order mode recovers standard GS, while higher-order modes capture high frequencies. We predict Brane parameters directly from low-resolution features. Because Branes provide a mathematically richer formulation than simple Gaussians, far fewer primitives need to overlap to reconstruct a given target pixel. To exploit this, we introduce an efficient fully differentiable rasterizer with a precise culling strategy based on the classical quantum turning point. This allows us to safely skip negligible regions, drastically reducing the rendering overhead. Experiments on standard ASR benchmarks show that RBS improves reconstruction quality over implicit and GS baselines, while achieving superior speed-quality trade-off than prior GS methods.

  </details>

## 2026-06-26

- **[Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction](https://arxiv.org/abs/2606.26985)**  
  *Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung*  
  `2026-06-25` · `cs.GR` · [abs](https://arxiv.org/abs/2606.26985) · [pdf](https://arxiv.org/pdf/2606.26985.pdf)
  > 💡 提出Vis4GS多视图可视分析工具，连接3DGS伪影与高斯属性及优化历史，实现原始级诊断。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) supports fast training and real-time rendering, but its optimization process remains difficult to interpret. Existing viewers mainly expose the final reconstructed scene and offer limited support for explaining how Gaussian properties contribute to visible artifacts or evolve during training. We present Vis4GS, a multi-view visual analytics tool for primitive-level diagnosis of 3DGS reconstruction artifacts. Built on the original 3DGS viewer and training framework, Vis4GS links rendered artifacts to Gaussian properties, View Coverage, training progress, and Gaussian genealogy through four linked views: an interactive Gaussian analysis view, a property timeline view, a Gaussian densification tree view, and a log and control panel. The system supports Gaussian selection, blur and needle-like artifact scoring, View Coverage analysis, and multiscale genealogy exploration of clone, split, prune, and clone-split events. By connecting scene-level artifacts with primitive-level evidence and optimization history, Vis4GS enables a structured workflow for diagnosing reconstruction failures beyond final-image inspection and global metrics. A user study also shows that Vis4GS provides stronger support for usability and artifact understanding than the original 3DGS viewer.

  </details>

## 2026-06-24

- **[Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353)**  
  *Hojun Choi, Seulbin Hwang, Dae Jung Kim, Kisung Kim, Hyunjung Shim, Jinhan Lee*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24353) · [pdf](https://arxiv.org/pdf/2606.24353.pdf)
  > 💡 开放词汇BEV分割存在3D几何不一致，提出基于高斯泼溅和几何约束的OVBEVSeg，实现SOTA性能并提升效率。

  <details><summary>Abstract</summary>

  Bird's-eye view (BEV) perception fuses multi-camera images into a unified top-down representation for autonomous driving. Despite recent progress, state-of-the-art methods remain confined to closed-set scenarios, making them vulnerable to unpredictable real-world environments. In this work, we introduce open-vocabulary BEV segmentation (OVBS), which leverages vision-language models (VLMs) to recognize categories beyond the training set while maintaining precise BEV perception and real-time efficiency. A key challenge in OVBS lies in the 3D geometric inconsistency inherent in the ill-posed lifting of 2D VLM semantics into BEV. To address this, we propose OVBEVSeg, a geometry-aware OVBS framework that enhances efficient Gaussian splatting (GS)-based unprojection by leveraging robust 3D geometric constraints across three progressive stages: (1) 2D-to-BEV pseudo-labeling via reliable 3D projection for OV generalization; (2) joint 2D-BEV per-scene optimization with BEV structural constraints for 3D geometric consistency; and (3) 3D geometric distillation for online efficiency. On the nuScenes dataset, OVBEVSeg achieves state-of-the-art performance, outperforming closed-set methods by 15.3 mIoU on unseen categories. Remarkably, even with no novel-class ground-truth labels, it remains competitive with self- and semi-supervised baselines trained with up to 40% of ground-truth annotations. Furthermore, it achieves 2.5x faster inference with only 0.22x the memory consumption of projection-based methods. Project page: https://hchoi256.github.io/projects/ovbevseg/.

  </details>

## 2026-06-23

- **[Learning Stable Canonical Worlds for Novel View Synthesis and Beyond](https://arxiv.org/abs/2606.23027)**  
  *Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23027) · [pdf](https://arxiv.org/pdf/2606.23027.pdf)
  > 💡 前馈高斯泼溅在视图增多时易积累噪声，通过不确定性感知融合构建规范潜在世界，新视图合成PSNR提升2.5dB，语义分割准确率提升11%。

  <details><summary>Abstract</summary>

  Feed-forward Gaussian splatting (FFGS) facilitates real-time novel view synthesis, yet current methods often remain tied to view-dependent predictions. As more input views are added, they may accumulate noisy or redundant evidence instead of converging to a stable scene representation. In this paper, we introduce CanonicalGS, a feed-forward pipeline that maps cluttered multi-view observations into a stable, scene-centric representation. CanonicalGS first extracts view-centric evidence from depth, semantic features, and uncertainty estimates, and then aggregates this evidence in a canonical latent world using uncertainty-aware fusion. By emphasizing reliable observations while suppressing uncertain or redundant ones, CanonicalGS produces representations that scale more effectively for novel view synthesis and transfer to downstream visual perception tasks. Experiments show up to a $2.5$ dB improvement in peak signal-to-noise ratio for synthesizing novel views and an $11\%$ gain in semantic segmentation accuracy.

  </details>

- **[Mesh2GS: White-Box 3DGS Construction via Plenoptic Sampling](https://arxiv.org/abs/2606.21898)**  
  *Haoran Zhu, Youcheng Cai, Huangsheng Du, Jingyang Meng, Ligang Liu*  
  `2026-06-20` · `cs.GR` · [abs](https://arxiv.org/abs/2606.21898) · [pdf](https://arxiv.org/pdf/2606.21898.pdf)
  > 💡 针对网格转3DGS问题，提出基于全光采样理论的白盒框架，通过最小采样率推导和反照率-着色分解更新实现奈奎斯特级全局光照渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a promising method for high-quality, real-time 3D reconstruction. To associate 3DGS with mesh representations, existing methods primarily focus on 3DGS-to-mesh reconstruction from multi-view images. In contrast, the problem of converting a mesh into 3DGS has received comparatively less attention. Instead of relying on heuristic strategies that bind 3D Gaussians to the mesh, we propose a novel white-box 3DGS construction framework, termed Mesh2GS, which generates 3DGS directly from mesh geometry based on plenoptic sampling theory, achieving Nyquist-level performance for high-quality global illumination rendering. Firstly, we propose a plenoptic sampling guided 3DGS construction strategy that theoretically derives the minimum sampling rate of the sampled views and the distribution of 3D Gaussians. Second, we propose a novel 3DGS update procedure with albedo--shading decomposition for efficient global-illumination capture. Finally, we introduce a neural illumination enhancement module to handle non-Lambertian effects. Experimental results demonstrate that our method surpasses state-of-the-art baselines and is practically effective for both real-time shared rendering and non-Lambertian effects capturing specular highlights. The project code will be released upon acceptance.

  </details>

- **[Single-Event Upsets in 3D Gaussian Splatting Rendering: Bit-Level Criticality, Spatial Extent, and a Parallel Support Guard](https://arxiv.org/abs/2606.21791)**  
  *Faruk Alpay, Baris Basaran*  
  `2026-06-19` · `cs.GR` · [abs](https://arxiv.org/abs/2606.21791) · [pdf](https://arxiv.org/pdf/2606.21791.pdf)
  > 💡 分析3DGS渲染中单比特翻转的位

  <details><summary>Abstract</summary>

  Three-dimensional Gaussian splatting is a standard real-time scene representation increasingly deployed on hardware exposed to transient faults, such as spaceborne processors and robotic edge devices where silent data corruption occurs. A trained model is a large array of floating-point parameters in GPU memory, where a single-event upset corresponds to a single flipped bit. This paper measures these effects and constructs a defense. A GPU-resident parallel fault-injection engine applies over 3.8 million controlled single-bit upsets across four scenes, six fields, all bit positions, and three numeric formats (fp32, fp16, bf16), using 5.3 GPU-hours. The effect is highly concentrated: most upsets leave the image perceptually unchanged due to high redundancy, but a small set of high-order bits principally the logarithmic scale's sign bit enlarge a single primitive to cover up to 75.7% of the frame. A closed-form perturbation bound derived from the IEEE-754 layout and pipeline activations predicts this per-bit ordering. This concentration motivates a support guard: a per-primitive clamp of each parameter to the coordinate box observed during training, costing 76 us per frame. Over 768,000 guarded upsets, the worst corruption footprint is restricted to 11.68% of the frame. We prove the guard leaves clean models unchanged and prevents frame-covering corruption. Under an accumulated dose of 20,000 simultaneous upsets, the unguarded renderer degrades to 10.6 dB, whereas the guarded renderer remains at 21.8 dB. The corruption footprint also dictates the number of tile/compositing nodes contaminated in distributed renderers, where the per-node guard contains it.

  </details>

- **[Spectral GS-SLAM: Observability-Aware, Degeneracy-Robust Tracking for Real-Time 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2606.21258)**  
  *Edward Beng Wai Tan, Siew-Kei Lam, Dongshuo Zhang*  
  `2026-06-19` · `cs.RO` · [abs](https://arxiv.org/abs/2606.21258) · [pdf](https://arxiv.org/pdf/2606.21258.pdf)
  > 💡 针对纹理缺失或几何退化场景中跟踪易失效问题，提出结合ICP与特征约束并引入高斯感知平面性加权的实时鲁棒SLAM方法。

  <details><summary>Abstract</summary>

  Recent 3DGS-SLAM systems enable real-time operation by leveraging conventional feature matching or ICP-based tracking, thereby avoiding the heavy dense photometric optimization used in earlier approaches. However, feature matching remains prone to failure in textureless environments, while ICP-based tracking struggles in structureless or geometrically degenerate scenes due to ill-conditioned optimization. To address this issue, we propose Spectral GS-SLAM, an efficient yet robust tracking framework that integrates ICP with complementary feature-based constraints. Our method mitigates numerical instability by adaptively compensating under-constrained directions in degenerate scenarios, without interfering with the shared Gaussian representation used for mapping. We further introduce a Gaussian-aware planarity weighting mechanism that exploits the intrinsic covariance structure of 3D Gaussians to characterize scene geometry and guide information fusion. Extensive evaluations on challenging TUM RGB-D sequences demonstrate that Spectral GS-SLAM achieves real-time performance (40.14 FPS) while maintaining consistent tracking in both structureless and featureless environments. The proposed method preserves trajectory integrity in degenerate scenes while maintaining competitive performance in non-adverse conditions.

  </details>

## 2026-06-19

- **[LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping](https://arxiv.org/abs/2606.20424)**  
  *Shikuan Shi, Chunran Zheng, Jiaming Xu, Tianyong Ye, Tao Yu, Yukang Cui*  
  `2026-06-18` · `cs.RO` · [abs](https://arxiv.org/abs/2606.20424) · [pdf](https://arxiv.org/pdf/2606.20424.pdf)
  > 💡 针对光照变化场景，LIT-GS通过LiDAR平面约束和热-LiDAR关联优化位姿与结构，提升几何与渲染质量。

  <details><summary>Abstract</summary>

  Gaussian Splatting has enabled real-time neural rendering, yet existing LiDAR-inertial-visual (LIV) Gaussian mapping pipelines remain fragile under illumination changes and texture-deficient scenes due to their reliance on RGB photometric cues. We present LIT-GS, a LiDAR-inertial-thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization. Specifically, we exploit LIV visual map points as confidence-aware cross-modal anchors to establish reliable thermal-LiDAR associations, and incorporate weighted LiDAR point-to-plane residuals into bundle adjustment to jointly refine camera poses and 3D points under weak thermal supervision. Building on the refined structure, we further introduce a LiDAR-plane-regularized differentiable splatting objective that constrains rendered 3D points to align with locally observed planes, mitigating surface thickening and structural drift in low-contrast thermal imagery. Experiments on proprietary sequences and public datasets demonstrate that LIT-GS consistently improves geometric accuracy and rendering quality over state-of-the-art LIV-based Gaussian Splatting baselines, particularly in challenging lighting conditions.

  </details>

## 2026-06-18

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

## 2026-06-16

- **[Local-GS: Accelerating 3D Gaussian Splatting via Tile-Local Warp Coherence](https://arxiv.org/abs/2606.16566)**  
  *Yang Luo, Yan Gong, Yongsheng Gao, Jie Zhao, Xinyu Zhang, Huaping Liu*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16566) · [pdf](https://arxiv.org/pdf/2606.16566.pdf)
  > 💡 针对3DGS翘曲分歧致GPU低效，提出基于瓦片局部

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has significantly advanced real-time novel view synthesis by representing scenes as dense collections of anisotropic 3D Gaussian primitives. However, the irregular spatial distribution of Gaussians often leads to poor GPU utilization, as warp divergence and redundant computation degrade rendering performance. To address this, we present Local-GS, a warp-coherent rendering paradigm that, organizes Gaussian primitives with respect to SIMT (Single Instruction, Multiple Threads) execution boundaries rather than scene geometry. Specifically, we propose three warp-coherent stages: a hoisting stage that precomputes shared parameters at tile level, a culling stage that discards warps with no contribution, and a blending stage that replaces per-pixel branching with a uniform instruction stream. Across extensive benchmarks on multiple datasets, Local-GS improves efficiency without compromising quality. As a plug-and-play optimization, it provides additional performance gains to all tested baselines, culminating in a $7.76\times$ speedup on Deep Blending scenes.

  </details>

- **[PolyMerge: Compressing 3D Gaussian Splats with Polytope Coverings for Provably Safe Resource-Constrained Navigation](https://arxiv.org/abs/2606.16232)**  
  *Jihoon Hong, Chih-Yuan Chiu, Sara Fridovich-Keil, Glen Chou*  
  `2026-06-15` · `cs.RO` · [abs](https://arxiv.org/abs/2606.16232) · [pdf](https://arxiv.org/pdf/2606.16232.pdf)
  > 💡 将3DGS模型转化为凸多面体覆盖，压缩并保证安全，实现资源受限下的实时避障导航。

  <details><summary>Abstract</summary>

  Obstacle avoidance is essential for safe navigation and motion planning. Recent radiance field reconstruction methods enable object detection and modeling with high fidelity, but remain too memory- and compute-intensive for on-board perception-based path planning. To address these limitations, we propose PolyMerge to convert a large, photorealistic 3D Gaussian Splatting (3DGS) model of a scene into a lightweight representation of convex polytopes whose union provably over-approximates all obstacles in the original 3DGS model. PolyMerge tunes the polytope count to trade off conservativeness and compute cost, and integrates with control barrier functions (CBFs) to plan collision-free paths. We showcase PolyMerge in simulation and hardware experiments on a Crazyflie drone, which uses PolyMerge to compute and follow safe trajectories in real time under severe onboard compute constraints, outperforming baselines in speed while guaranteeing safety. For our code and videos, visit https://athlon76.github.io/PolyMerge-website/.

  </details>

## 2026-06-11

- **[Seeing What Matters: Perceptual Wrapper with Common Randomness for 3D Gaussian Splatting](https://arxiv.org/abs/2606.11782)**  
  *He-Bi Yang, Jing-Zhong Chen, Yen-Kuan Ho, Sang NguyenQuang, Fan-Yi Hsu, Yun-Yu Lee, Jui-Chiu Chiang, Wen-Hsiao Peng*  
  `2026-06-10` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11782) · [pdf](https://arxiv.org/pdf/2606.11782.pdf)
  > 💡 针对3DGS高频纹理缺失问题，提出伪随机噪声驱动的2D感知包装器，以Wasserstein损失学习局部特征统计，提升感知质量并显著压缩模型体积。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) achieves impressive real-time rendering, it frequently struggles to synthesize high-frequency textures, a limitation heavily exacerbated in memory-constrained and rate-distortion-optimized (RDO) pipelines. To address this, we propose a versatile 2D perceptual wrapper that enhances the rendered outputs of existing 3DGS representations in a content- and view-dependent manner. Our method leverages a lightweight synthesis network conditioned on pseudo-random Gaussian noise to synthesize perceptually plausible textures. Supervised by Wasserstein Distortion, the network learns to match local feature statistics rather than strictly enforcing pixel-wise reconstruction fidelity, effectively mitigating the blurriness inherent in standard frameworks. We demonstrate the broad applicability of our plug-and-play approach across vanilla, memory-constrained, and RDO 3DGS methods. Comprehensive subjective and objective experiments confirm that our method significantly improves over existing baselines, yielding superior perceptual quality at sharply reduced file or model sizes.

  </details>

## 2026-06-06

- **[KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120)**  
  *Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa, Aniket Roy*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03120) · [pdf](https://arxiv.org/pdf/2606.03120.pdf)
  > 💡 KC-3DGS用峰度约束的小波域监督弥补标准3DGS高频细节缺失，提升感知质量与稀疏视图性能。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables real-time novel view synthesis by representing scenes as collections of anisotropic Gaussians optimized via differentiable rasterization. However, standard pixel-space losses (L1, SSIM) constrain only aggregate reconstruction error, permitting the optimization to redistribute error across frequency scales. This leads to oversmoothing and structural artifacts, particularly in sparse-view settings where supervision is limited. We propose KC-3DGS, which augments 3DGS training with wavelet-domain supervision based on natural image statistics. Our method combines three components: (1) a multi-scale wavelet coefficient alignment loss that explicitly penalizes missing high-frequency detail, (2) a supervised kurtosis concentration loss that encourages rendered images to match the heavy-tailed frequency statistics of ground-truth images, and (3) a cross-band covariance penalty that promotes frequency specialization. We provide theoretical analysis showing that pixel-space losses admit a family of indistinguishable perturbations under wavelet redistribution, and that our joint objective excludes degenerate solutions. Experiments across MipNeRF360, Tanks&Temples, MVImgNet, DeepBlending, and WRIVA-ULTRRA demonstrate consistent improvements in perceptual quality. On the challenging WRIVA-ULTRRA outdoor dataset, KC-3DGS achieves a 9.48% improvement in DreamSim while also improving PSNR, SSIM, and LPIPS. In sparse-view settings with only 12 training images, our method improves PSNR by up to 0.5 dB on MipNeRF360 while maintaining perceptual quality. The approach integrates seamlessly into existing 3DGS pipelines as a plug-and-play regularization strategy.

  </details>

- **[RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261)**  
  *Chengyang Yao, Cunhua Pan, Jiaming Zeng, Yuquan Sun, Haoyang Weng, Haojian Wang, Hong Ren, Jiangzhou Wang*  
  `2026-05-31` · `eess.IV` · [abs](https://arxiv.org/abs/2606.01261) · [pdf](https://arxiv.org/pdf/2606.01261.pdf)
  > 💡 面向28GHz室内射线追踪，联合RGB-LiDAR与3DGS构建RF数字孪生，语义分割赋予材质属性，有效路径从742降至52。

  <details><summary>Abstract</summary>

  Real-scene indoor millimeter-wave simulation requires efficient modeling of radio frequency (RF)-computable geometry and electromagnetic material properties. To address the low efficiency of manual scene modeling, the limited RF adaptability of visually reconstructed meshes, and the lack of material binding in 28 GHz ray-tracing simulation, RFDT-Channel is developed as an RF digital twin scene construction workflow based on red-green-blue (RGB) images and light detection and ranging (LiDAR) point clouds. Indoor videos and point clouds are collected by a Jetson Orin platform with LiDAR and GMSL cameras. An initial triangular mesh is generated through COLMAP, 3D Gaussian Splatting, and SuGaR. The LiDAR point cloud then provides geometric and scale references for RF-oriented regularization in Blender, including alignment, wall solidification, door/window opening construction, and topology repair. OpenScene semantic segmentation maps major indoor structures to concrete, glass, wood, and metal materials, and Sionna RT performs 28 GHz ray tracing. Under a fixed transmitter-receiver deployment, the generated channel impulse response (CIR), channel frequency response (CFR), and Radio Map results show that material binding mainly changes weak reflection, transmission, and scattering paths, reducing the number of effective paths from about 742 to about 52 while keeping the dominant path amplitude nearly unchanged.

  </details>

- **[Directed Distance Fields for Constant-Time Ray Queries on Gaussian Splatting](https://arxiv.org/abs/2606.00817)**  
  *Subhankar MIshra*  
  `2026-05-30` · `cs.GR` · [abs](https://arxiv.org/abs/2606.00817) · [pdf](https://arxiv.org/pdf/2606.00817.pdf)
  > 💡 针对3DGS无法追踪次光线，提出定向距离场(DDF)实现快速恒定时间射线查询，无需网格且内存不随

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) renders new views of a scene in real time. Like every rasterizer, it answers only primary rays, the rays from the camera through the image. It cannot trace the secondary rays that shadows, ambient occlusion, and global illumination need. We turn a trained 3DGS scene into a ray oracle by distilling a Directed Distance Function (DDF). The DDF is a small neural field. It takes a ray, given by an origin and a direction, and returns the distance to the first surface and whether the ray hits anything. Each query is one forward pass. The field is 52~MB, and its size does not depend on the number of Gaussians, so its cost and memory stay flat as the scene grows. We make three points. First, we study what supervision a DDF needs. Depth rendered from the Gaussians is too blurry to teach thin parts, while clean distance supervision recovers them. Second, we measure speed. The DDF is 26 to 72 times faster than sphere tracing an equivalent signed distance field, and unlike a bounding volume hierarchy built over the Gaussians, even on dedicated RT-core hardware, its query time and memory do not grow with the scene. Third, we show a pipeline that needs no mesh: images give a 3DGS scene, a neural surface gives clean distances, and the DDF learns from them. We use the DDF as a secondary-ray oracle for global illumination. It reproduces reference ray-traced shadows at 30.3~dB and ambient occlusion at 21.3~dB across 142 objects, and on real captured scenes. Our codes are available at https://github.com/smlab-niser/ddf-gs.

  </details>

- **[HiGS: A Hierarchical Rendering Architecture for Real-Time 3D Gaussian Splatting](https://arxiv.org/abs/2606.00352)**  
  *Dawid Pająk, Martin Bisson, Rodolfo Lima*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00352) · [pdf](https://arxiv.org/pdf/2606.00352.pdf)
  > 💡 3DGS中分区与光栅化对瓦片大小需求矛盾，提出分层渲染架构HiGS，宏块分区精细光栅化，加速达15.8倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become the standard for real-time novel view synthesis on commodity GPUs. Its pipeline ties spatial partitioning and rasterization to one tile size, yet the two pull in opposite directions: partitioning, which bins and depth-sorts gaussians, grows cheaper with larger tiles, while rasterization gets cheaper with smaller ones. Prior acceleration work reduces the cost of individual stages but keeps both locked to that single scale, where a few dense tiles dominate frame time. We present Hierarchically Tiled Gaussian Splatting (HiGS), which gives each its own scale: partitioning runs over coarse macro-tiles, while rasterization runs over the fine render tiles within them. Rasterization work is then issued in proportion to the gaussians in each macro-tile rather than per tile, so dense regions spread across many parallel units instead of serializing through one. Across tested scenes, HiGS renders up to 15.8x faster than the original 3DGS and outperforms every other rasterizer we evaluate, while preserving exact front-to-back alpha compositing.

  </details>

## 2026-06-01

- **[LiftNav: Path Planning via Semantic Lifting in TSDF-Guided Gaussian Splatting](https://arxiv.org/abs/2605.31376)**  
  *Hannah Schieber, Dominik Frischmann, Victor Schaack, Angela P. Schoellig, Daniel Roth*  
  `2026-05-29` · `cs.RO` · [abs](https://arxiv.org/abs/2605.31376) · [pdf](https://arxiv.org/pdf/2605.31376.pdf)
  > 💡 针对未知室内环境语义导航难题，提出TSDF引导高斯泼溅的混合框架，结合YOLO检测

  <details><summary>Abstract</summary>

  Autonomous robots in unknown indoor environments require both reliable collision avoidance and object-level understanding. Classical representations such as TSDF support safe planning but lack semantics, while photorealistic methods like Gaussian Splatting (GS) provide rich appearance yet suffer from soft geometry, limiting precise obstacle avoidance. We present LiftNav, a hybrid navigation framework built on GSFusion's TSDF+GS dual map, augmented with a real-time pipeline of YOLO-based detection, TSDF-based 3D lifting, and B-spline trajectory optimization. This design enables flexible semantic navigation without dense 3D embeddings. We further introduce a hinge-loss-based collision penalty that improves trajectory smoothness and safety. We evaluate our approach in a simulation using the Replica dataset. Compared against a state-of-the-art radiance field baseline we show a 100% feasibility rate and shorter trajectories.

  </details>

## 2026-05-30

- **[Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342)**  
  *Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30342) · [pdf](https://arxiv.org/pdf/2605.30342.pdf)
  > 💡 提出各向异性可见性场量化3DGS不确定度，结合贝叶斯网络实现实时主动建图，显著提升精度与效率。

  <details><summary>Abstract</summary>

  We present Gaussian Splatting Anisotropic Visibility Field (GAVIS), a novel framework for uncertainty quantification and active mapping in 3DGS. Our key insight is that regions unseen from the training views yield unreliable predictions from the 3DGS. To address this, we introduce a principled and efficient method for quantifying the visibility field in 3DGS, defined as the anisotropic visibility of each particle with respect to the training views, and represented using spherical harmonics. The resulting visibility field is integrated into a Bayesian Network-based uncertainty-aware 3DGS rasterizer, enabling real-time (200 FPS) uncertainty quantification for synthesized views. Active mapping is further performed within a maximum information gain framework building on this formulation. Extensive experiments across diverse environments demonstrate that GAVIS consistently and significantly outperforms prior approaches in both accuracy and efficiency. Moreover, beyond standalone use, our method can be applied post-hoc to improve the performance of existing approaches.

  </details>

- **[Gaussian-Voxel Duet: A Dual-Scaffolding Hybrid Representation for Fast and Accurate Monocular Surface Reconstruction](https://arxiv.org/abs/2605.26616)**  
  *Zhenhua Du, Zhen Tan, Haoyu Zhang, Dewen Hu, Shuaifeng Zhi, Peidong Liu*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26616) · [pdf](https://arxiv.org/pdf/2605.26616.pdf)
  > 💡 为平衡几何精度与效率，提出高斯-体素双支架混合表示，用稀疏体素支架约束高斯，实现快速准确的单目表面重建。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting has achieved remarkable success in photorealistic novel view synthesis, its pursuit of fast and high-fidelity 3D reconstruction has long been constrained by a trade-off between geometric accuracy and optimization efficiency. Methods specialized in image rendering converge quickly at the cost of imperfect geometry caused by superfluous primitives overfitting training views, while methods integrating neural signed-distance field (SDF) for better geometry incur prohibitive training costs. In this paper, we attempt to strike a better trade-off by tethering scaffold-anchored Gaussians to a jointly optimized sparse voxel scaffold. This hybrid Gaussian-Voxel representation explicitly confines anchored Gaussians to a narrow band around surfaces defined by voxelized SDFs, which effectively improves representation efficiency and condenses floating Gaussians without sacrificing geometry quality. An implicit surface tethering loss further pulls individual Gaussian primitives closer to SDF-induced surfaces in a mutually regularized manner for improved reconstruction accuracy. Extensive experiments on diverse real-world indoor scenes from ScanNet++, ScanNetv2, and DeepBlending datasets demonstrate that our method achieves state-of-the-art surface reconstruction quality as well as superior novel view synthesis against leading baselines, while maintaining fast training convergence and real-time rendering. Code will be available at https://github.com/duzh11/VoxelGS.

  </details>

- **[Accelerating 3D Gaussian Splatting using Tensor Cores](https://arxiv.org/abs/2605.17855)**  
  *Sheng Li, Yang Sui, Yue Wu, Zhuoran Song, Bo Yuan, Xulong Tang, Yue Dai*  
  `2026-05-18` · `cs.GR` · [abs](https://arxiv.org/abs/2605.17855) · [pdf](https://arxiv.org/pdf/2605.17855.pdf)
  > 💡 提出TensorGS，利用张量核心加速3DGS光栅化，通过张量化和跨块分组

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become a leading technique for real-time neural rendering and 3D scene reconstruction, but its rendering cost remains too high for many latency-sensitive scenarios. In particular, the rasterization stage in 3DGS dominates end-to-end rendering time, during which the renderer repeatedly evaluates each Gaussian's contribution to each covered pixel, making this stage compute-bound. At the same time, modern GPUs provide high-throughput Tensor Cores for low-precision matrix operations, yet existing 3DGS systems execute rasterization entirely on CUDA cores and leave Tensor Cores idle. We find that 3DGS rendering can be executed in FP16 with negligible quality degradation, suggesting a promising opportunity for Tensor Core acceleration. However, exploiting Tensor Cores for 3DGS is non-trivial because rasterization does not naturally match their execution model. Existing 3DGS rasterization is expressed as irregular per-pixel scalar operations, whereas Tensor Cores require dense, regular, and reuse-rich matrix workloads. Moreover, conventional tile-by-tile execution fails to exploit Gaussian reuse across neighboring tiles, resulting in repeated data loading and thus high data movement overhead. To this end, we present TensorGS, a 3DGS acceleration framework using Tensor Cores. TensorGS tensorizes the dominant rasterization computation into Tensor-Core-compatible matrix operations and introduces cross-tile grouping to improve Gaussian reuse, amortize overhead, and increase Tensor Core utilization. Experimental results show that TensorGS improves end-to-end rendering performance by 1.65$\times$ while preserving image quality.

  </details>

- **[3D Skew-Normal Splatting](https://arxiv.org/abs/2605.15010)**  
  *Xiangru Wu, Ke Fan, Yanwei Fu*  
  `2026-05-14` · `cs.CV` · [abs](https://arxiv.org/abs/2605.15010) · [pdf](https://arxiv.org/pdf/2605.15010.pdf)
  > 💡 针对对称高斯原语无法紧凑表示非对称结构的问题，提出偏斜正态原语，通过可学习偏斜参数连续插值提升重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a leading representation for real-time novel view synthesis and has been widely adopted in various downstream applications. The core strength of 3DGS lies in its efficient kernel-based scene representation, where Gaussian primitives provide favorable mathematical and computational properties. However, under a finite primitive budget, the symmetric shape of each primitive directly affects representation compactness, especially near asymmetric structures such as object boundaries and one-sided surfaces. Recent works have explored more complex kernel distributions; however, they either remain within the elliptical family or rely on hard truncation, which limits continuous shape control and introduces distributional discontinuities. In this paper, we propose Skew-Normal Splatting (SNS), which adopts the Azzalini Skew-Normal distribution as the fundamental primitive. By introducing a learnable and bounded skewness parameter, SNS can continuously interpolate between symmetric Gaussians and Half-Gaussian-like shapes, enabling flexible modeling of both sharp boundaries and interior regions. Moreover, SNS preserves analytical tractability under affine transformations and marginalization. This property allows seamless integration into existing Gaussian Splatting rasterization pipelines. Furthermore, to address the strong coupling between scale, rotation, and skewness parameters, we introduce a decoupled parameterization and a block-wise optimization strategy to enhance training stability and accuracy. Extensive experiments on standard novel-view synthesis benchmarks show that SNS consistently improves reconstruction quality over Gaussian and recent non-Gaussian kernels, with clearer benefits on sharp boundaries and thin or one-sided structures.

  </details>

- **[BlitzGS: City-Scale Gaussian Splatting at Lightning Speed](https://arxiv.org/abs/2605.13794)**  
  *Zhongtao Wang, Huishan Au, Yilong Li, Mai Su, Haojie Jin, Yisong Chen, Meng Gai, Fei Zhu, Guoping Wang*  
  `2026-05-13` · `cs.GR` · [abs](https://arxiv.org/abs/2605.13794) · [pdf](https://arxiv.org/pdf/2605.13794.pdf)
  > 💡 提出分布式3DGS框架BlitzGS，通过索引奇偶分片、重要性评分与LOD门控减少高斯数量，实现城市级场景训练速度提升一个数量级。

  <details><summary>Abstract</summary>

  We present BlitzGS, a distributed 3DGS framework that reduces active Gaussian workload for fast city-scale reconstruction. BlitzGS manages this workload at three coupled levels. At the system level, the framework shards Gaussians across GPUs by index parity rather than spatial blocks. This approach mitigates the cross-block visibility redundancy inherent in spatial partitioning. Furthermore, it distributes each rendering step through a single cross-GPU exchange that routes projected Gaussians to their tile owners. At the model level, scheduled importance-scoring passes shrink the global Gaussian population. During these passes, the framework generates a per-Gaussian visibility weight to bias density-control updates toward contributing primitives and a per-view importance mask for the view-level renderer. At the view level, BlitzGS trims each camera's active set with a distance-based LOD gate to exclude excessively fine primitives for the current frustum and the importance-based culling mask to skip Gaussians with negligible cross-view contribution. On large-scale benchmarks, BlitzGS matches the rendering quality of recent large-scale baselines while delivering an order-of-magnitude speedup, training city-scale scenes in tens of minutes. Our code is available at https: //github.com/AkierRaee/BlitzGS.

  </details>

- **[Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465)**  
  *Can Wang, Lei Liu, Wei Jiang, Dong Xu*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13465) · [pdf](https://arxiv.org/pdf/2605.13465.pdf)
  > 💡 通过Z-order策略将高斯原语组织为空间连贯序列，结合稀疏注意力机制的Transformer，实现前馈式3DGS的高效去冗余与高质量渲染。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in photorealistic novel view synthesis. However, traditional 3DGS relies on a slow, iterative optimization process, which limits its use in scenarios demanding real-time results. To overcome this bottleneck, recent feed-forward methods aim to predict Gaussian attributes directly from images, but they often struggle with the redundancy of Gaussian primitives and rendering quality. In this work, we introduce a transformer-based architecture specifically designed for feed-forward Gaussian Splatting. Our key insight is that spatial and semantic relationships among Gaussians can be effectively captured through a sparse attention mechanism, enabled by a Z-order strategy that organizes the unstructured Gaussian set into a spatially coherent sequence. Furthermore, we incorporate this Z-order strategy to adaptively suppress redundancy while preserving critical structural details. This allows the transformer to efficiently model context, compress Gaussian primitives, and predict Gaussian attributes in a single forward pass. Comprehensive experiments demonstrate that our method achieves fast and high-quality novel view synthesis with fewer Gaussian primitives.

  </details>

- **[Differentiable Ray Tracing with Gaussians for Unified Radio Propagation Simulation and View Synthesis](https://arxiv.org/abs/2605.07781)**  
  *Niklas Vaara, Lam Huynh, Pekka Sangi, Miguel Bordallo López, Janne Heikkilä*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07781) · [pdf](https://arxiv.org/pdf/2605.07781.pdf)
  > 💡 针对3DGS缺乏可相交几何问题，将高斯原语嵌入光线追踪结构，实现统一可微分RF模拟与视图合成。

  <details><summary>Abstract</summary>

  Explicit neural representations such as 3D Gaussian Splatting (3DGS) enable high-fidelity and real-time novel view synthesis, yet optimize for alpha-composited optical appearance rather than ray-intersectable geometry. In contrast, radio-frequency (RF) digital twins require deterministic multi-bounce paths, where the geometry dictates trajectories and their associated attenuation and delay. We introduce a framework enabling differentiable RF propagation simulation directly within visually reconstructed neural scenes, allowing point-to-point path computation between arbitrary 3D locations while preserving high-quality visual rendering. Unlike conventional RF simulation pipelines that rely on manually constructed meshes, we embed Gaussian primitives into a hardware-accelerated ray tracing structure as the underlying spatial representation. By extracting physically meaningful channel impulse responses from visual-only reconstructions, we provide cross-modal evidence that neural reconstructions can serve as unified spatial representations for both electromagnetic propagation simulation and photorealistic view synthesis.

  </details>

- **[QuadBox: Accelerating 3D Gaussian Splatting with Geometry-Aware Boxes](https://arxiv.org/abs/2605.04844)**  
  *Xinze Li, Bohan Yang, Pengxu Chen, Yiyuan Wang, Hongcheng Luo, Wentao Cheng, Weifeng Su*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04844) · [pdf](https://arxiv.org/pdf/2605.04844.pdf)
  > 💡 使用几何感知包围盒加速3DGS渲染，通过QuadBox和QPass高效计算瓦片交集，速度提升1.85倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as an advanced technique for real-time novel view synthesis by representing scene geometry and appearance using differentiable Gaussian primitives. However, efficiently computing precise Gaussian-tile intersections remains a critical task in the rasterization pipeline. To this end, we propose QuadBox, a method that leverages four axis-aligned bounding boxes to tightly encapsulate projected Gaussians in a discrete manner. First, we derive a geometry-aware stretching factor that enables the construction of a tile-aligned QuadBox, which covers the elliptical projection and largely excludes irrelevant tiles. Second, we introduce QPass, a single-pass tile traversal algorithm that exhaustively exploits the discrete nature of QuadBox, ensuring that the tile intersection check is performed with simple interval tests. Experiments on public datasets show that our method accelerates the rendering speed of 3DGS by 1.85$\times$. Code is available at \href{https://github.com/Powertony102/QuadBox}{https://github.com/Powertony102/QuadBox}.

  </details>

- **[CoherentRaster: Efficient 3D Gaussian Splatting for Light Field Displays](https://arxiv.org/abs/2605.04509)**  
  *Gyujin Sim, Seungjoo Shin, Hosung Jeon, Gwangsoon Lee, Hyon-Gon Choo, Sunghyun Cho*  
  `2026-05-06` · `cs.GR` · [abs](https://arxiv.org/abs/2605.04509) · [pdf](https://arxiv.org/pdf/2605.04509.pdf)
  > 💡 针对光场显示多视角渲染开销大的问题，提出CoherentRaster，通过子像素光栅化、跨视角属性重用与视角重映射，实现实时高质量合成。

  <details><summary>Abstract</summary>

  Light field displays (LFDs) require rendering an interlaced image that encodes many view-dependent observations. This multi-view requirement introduces substantial computational overhead, making real-time rendering difficult to achieve. While 3D Gaussian Splatting (3DGS) is efficient for single-view rendering on 2D displays, directly extending it to LFDs is computationally expensive. Moreover, prior accelerations either suffer from GPU inefficiency under spatially incoherent subpixel layouts or rely on computationally heavy multi-plane intermediates. In this paper, we propose CoherentRaster, a 3DGS-based light field rendering framework that performs subpixel-level rasterization. Our method employs Cross-view Coherent Attribute Reuse to eliminate redundant computation across neighboring viewpoints and applies View-coherent Remapping to restore warp-level memory efficiency degraded by the interlaced subpixel layout. Together, CoherentRaster provides an efficient pipeline for real-time, high-quality light field synthesis on consumer-grade hardware.

  </details>

- **[Beyond Heuristics: Learnable Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2605.00408)**  
  *Zhenhua Ning, Xin Li, Jun Yu, Guangming Lu, Yaowei Wang, Wenjie Pei*  
  `2026-05-01` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00408) · [pdf](https://arxiv.org/pdf/2605.00408.pdf)
  > 💡 将密度控制从启发式转化为强化学习可学习策略，设计敏感度奖励函数，实现效率和质量更优平衡。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) has demonstrated impressive real-time rendering performance, its efficacy remains constrained by a reliance on heuristic density control. Despite numerous refinements to these handcrafted rules, such methods inherently lack the flexibility to adapt to diverse scenes with complex geometries. In this paper, we propose a paradigm shift for density control from rigid heuristics to fully learnable policies. Specifically, we introduce \textbf{LeGS}, a framework that reformulates density control as a parameterized policy network optimized via Reinforcement Learning (RL). Central to our approach is the tailored effective reward function grounded in sensitivity analysis, which precisely quantifies the marginal contribution of individual Gaussians to reconstruction quality. To maintain computational tractability, we derive a closed-form solution that reduces the complexity of reward calculation from $O(N^2)$ to $O(N)$. Extensive experiments on the Mip-NeRF 360, Tanks \& Temples, and Deep Blending datasets demonstrate that \textbf{LeGS} significantly outperforms state-of-the-art methods, striking a superior balance between reconstruction quality and efficiency. The code will be released at https://github.com/AaronNZH/LeGS

  </details>

- **[Faster 3D Gaussian Splatting Convergence via Structure-Aware Densification](https://arxiv.org/abs/2604.28016)**  
  *Linjie Lyu, Ayush Tewari, Jianchun Chen, Thomas Leimkühler, Christian Theobalt*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.28016) · [pdf](https://arxiv.org/pdf/2604.28016.pdf)
  > 💡 标准密度控制忽视频率信息导致模糊或过密，提出多尺度频率分析和各向异性分裂机制，加速收敛并提升高频重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting has emerged as a powerful scene representation for real-time novel-view synthesis. However, its standard adaptive density control relies on screen-space positional gradients, which do not distinguish between geometric misplacement and frequency aliasing, often leading to either over-blurred high-frequency textures or inefficient over-densification. We present a structure-aware densification framework. Our key insight is that the decision to subdivide a Gaussian should be driven by an explicit comparison between its projected screen-space extent and the local structure of the texture it seeks to represent. We introduce a multi-scale frequency analysis combining structure tensors with Laplacian scale space analysis to estimate the dominant frequency at each pixel, enabling robust supervision across varying texture scales. Based on this analysis, we define $η$, a per-Gaussian, per-axis frequency violation metric that indicates when a primitive may be under-resolving local texture details. Unlike methods that perform isotropic splitting (e.g., splitting each Gaussian into two smaller ones with uniform shape), our approach performs anisotropic splitting. For each axis with high $η$, we compute a split factor to better resolve the local frequency content. We further introduce a multiview consistency criterion that aggregates $η$ observations across multiple views. By performing densification early and faster, we skip the lengthy iterative densification phases required by baseline methods and achieve significantly faster convergence. Experiments on standard benchmarks demonstrate that our method also achieves superior reconstruction quality, particularly in high-frequency regions.

  </details>

- **[Large-Scale Photogrammetric Documentation of St. John's Co-Cathedral: A Workflow for Cultural Heritage Preservation](https://arxiv.org/abs/2604.24316)**  
  *Matthew Kenely, Mark Bugeja, Andre Grima, Peter Pullicino, Matthew Pullicino, Dylan Seychell*  
  `2026-04-27` · `cs.GR` · [abs](https://arxiv.org/abs/2604.24316) · [pdf](https://arxiv.org/pdf/2604.24316.pdf)
  > 💡 提出大型文化遗产数字化工作流，融合多模态采集与AI去噪，初步探索高斯溅射用于复杂反射表面重建。

  <details><summary>Abstract</summary>

  We present a comprehensive methodology for the large-scale photogrammetric documentation of St. John's Co-Cathedral in Valletta, Malta, a UNESCO World Heritage site renowned for its ornate Baroque architecture and Caravaggio masterpieces. Over seven nights of evening-only data collection, we captured 99,000 images using DSLR cameras, drone photography, and LIDAR scanning to create a highly detailed 3D reconstruction comprising 25-30 billion triangles. This paper documents our complete workflow for cultural heritage preservation, addressing the unique challenges of digitizing complex baroque architectural spaces with highly reflective metallic surfaces, dark materials, intricate tapestries, and restricted access. We detail our pipeline from multi-modal data acquisition through processing, including strategic image grading and AI-assisted denoising to address low-light grain, extensive LIDAR point cloud cleanup, hybrid photogrammetric reconstruction using RealityCapture, and mesh subdivision strategies for real-time visualization engines. Our methodology combines automated workflows with necessary manual intervention to handle the scale and complexity of the project, with particular attention to reflective surface challenges characteristic of baroque heritage sites. We also present preliminary experiments with Gaussian splatting as a complementary representation technique. The resulting digital archive serves multiple preservation purposes including disaster recovery documentation, conservation analysis, virtual tourism, and scholarly research. This work provides a detailed, replicable workflow for heritage professionals undertaking similar large-scale architectural documentation projects, addressing the practical challenges of applying photogrammetric methods in complex real-world heritage scenarios.

  </details>

- **[WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images](https://arxiv.org/abs/2604.21182)**  
  *Yuki Fujimura, Takahiro Kushida, Kazuya Kitano, Takuya Funatomi, Yasuhiro Mukaigawa*  
  `2026-04-23` · `cs.CV` · [abs](https://arxiv.org/abs/2604.21182) · [pdf](https://arxiv.org/pdf/2604.21182.pdf)
  > 💡 从无约束图像中前馈生成3D高斯并联合学习外观嵌入，实现快速重建与可变光照下的外观控制。

  <details><summary>Abstract</summary>

  We propose WildSplatter, a feed-forward 3D Gaussian Splatting (3DGS) model for unconstrained images with unknown camera parameters and varying lighting conditions. 3DGS is an effective scene representation that enables high-quality, real-time rendering; however, it typically requires iterative optimization and multi-view images captured under consistent lighting with known camera parameters. WildSplatter is trained on unconstrained photo collections and jointly learns 3D Gaussians and appearance embeddings conditioned on input images. This design enables flexible modulation of Gaussian colors to represent significant variations in lighting and appearance. Our method reconstructs 3D Gaussians from sparse input views in under one second, while also enabling appearance control under diverse lighting conditions. Experimental results demonstrate that our approach outperforms existing pose-free 3DGS methods on challenging real-world datasets with varying illumination.

  </details>

- **[An Object-Centered Data Acquisition Method for 3D Gaussian Splatting using Mobile Phones](https://arxiv.org/abs/2604.19216)**  
  *Yuezhe Zhang, Luqian Bai, Mengting Yu, Lei Wei, Shuai Wan, Yifan Zhang*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.19216) · [pdf](https://arxiv.org/pdf/2604.19216.pdf)
  > 💡 针对手机采集3DGS困难，提出面向物体的引导式采集方法，利用球形网格和面积加权覆盖实现均匀视角，用更少图像达到更优重建质量。

  <details><summary>Abstract</summary>

  Data acquisition through mobile phones remains a challenge for 3D Gaussian Splatting (3DGS). In this work we target the object-centered scenario and enable reliable mobile acquisition by providing on-device capture guidance and recording onboard sensor signals for offline reconstruction. After the calibration step, the device orientations are aligned to a baseline frame to obtain relative poses, and the optical axis of the camera is mapped to an object-centered spherical grid for uniform viewpoint indexing. To curb polar sampling bias, we compute area-weighted spherical coverage in real-time and guide the user's motion accordingly. We compare the proposed method with RealityScan and the free-capture strategy. Our method achieves superior reconstruction quality using fewer input images compared to free capture and RealityScan. Further analysis shows that the proposed method is able to obtain more comprehensive and uniform viewpoint coverage during object-centered acquisition.

  </details>

- **[LAGS: Low-Altitude Gaussian Splatting with Groupwise Heterogeneous Graph Learning](https://arxiv.org/abs/2604.16910)**  
  *Yikun Wang, Yujie Wan, Wei Zuo, Shuai Wang, Yik-Chung Wu, Chengzhong Xu, Huseyin Arslan*  
  `2026-04-18` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16910) · [pdf](https://arxiv.org/pdf/2604.16910.pdf)
  > 💡 针对低空高斯散点重建中忽视图像多样性的资源分配问题，提出分组异构图神经网络GW-HGNN，通过双级消息传递平衡质量与成本，显著提升渲染指标并实现毫秒级推理。

  <details><summary>Abstract</summary>

  Low-altitude Gaussian splatting (LAGS) facilitates 3D scene reconstruction by aggregating aerial images from distributed drones. However, as LAGS prioritizes maximizing reconstruction quality over communication throughput, existing low-altitude resource allocation schemes become inefficient. This inefficiency stems from their failure to account for image diversity introduced by varying viewpoints. To fill this gap, we propose a groupwise heterogeneous graph neural network (GW-HGNN) for LAGS resource allocation. GW-HGNN explicitly models the non-uniform contribution of different image groups to the reconstruction process, thus automatically balancing data fidelity and transmission cost. The key insight of GW-HGNN is to transform LAGS losses and communication constraints into graph learning costs for dual-level message passing. Experiments on real-world LAGS datasets demonstrate that GW-HGNN significantly outperforms state-of-the-art benchmarks across key rendering metrics, including PSNR, SSIM, and LPIPS. Furthermore, GW-HGNN reduces computational latency by approximately 100x compared to the widely-used MOSEK solver, achieving millisecond-level inference suitable for real-time deployment.

  </details>

- **[MSGS: Multispectral 3D Gaussian Splatting](https://arxiv.org/abs/2604.13340)**  
  *Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13340) · [pdf](https://arxiv.org/pdf/2604.13340.pdf)
  > 💡 通过每波段球谐和双损失监督将3DGS扩展为多光谱

  <details><summary>Abstract</summary>

  We present a multispectral extension to 3D Gaussian Splatting (3DGS) for wavelength-aware view synthesis. Each Gaussian is augmented with spectral radiance, represented via per-band spherical harmonics, and optimized under a dual-loss supervision scheme combining RGB and multispectral signals. To improve rendering fidelity, we perform spectral-to-RGB conversion at the pixel level, allowing richer spectral cues to be retained during optimization. Our method is evaluated on both public and self-captured real-world datasets, demonstrating consistent improvements over the RGB-only 3DGS baseline in terms of image quality and spectral consistency. Notably, it excels in challenging scenes involving translucent materials and anisotropic reflections. The proposed approach maintains the compactness and real-time efficiency of 3DGS while laying the foundation for future integration with physically based shading models.

  </details>

- **[RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM](https://arxiv.org/abs/2604.12942)**  
  *Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, Zefan Huang, Shuo Sun, Jiahui Liu, Chengran Yuan, Hongliang Guo, Francis E. H. Tay, Marcelo H. Ang*  
  `2026-04-14` · `cs.RO` · [abs](https://arxiv.org/abs/2604.12942) · [pdf](https://arxiv.org/pdf/2604.12942.pdf)
  > 💡 针对大规模场景实时3DGS SLAM挑战，提出多传感器紧耦合框架，并行优化与级联初始化实现实时建

  <details><summary>Abstract</summary>

  Achieving real-time Simultaneous Localization and Mapping (SLAM) based on 3D Gaussian splatting (3DGS) in large-scale real-world environments remains challenging, as existing methods still struggle to jointly achieve low-latency pose estimation, continuous 3D Gaussian reconstruction, and long-term global consistency. In this paper, we present a tightly coupled LiDAR-Inertial-Visual 3DGS-based SLAM framework for real-time pose estimation and photorealistic mapping in large-scale real-world scenes. The system executes state estimation and 3D Gaussian primitive initialization in parallel with global Gaussian optimization, enabling continuous dense mapping. To improve Gaussian initialization quality and accelerate optimization convergence, we introduce a cascaded strategy that combines feed-forward predictions with geometric priors derived from voxel-based principal component analysis. To enhance global consistency, we perform loop closure directly on the optimized global Gaussian map by estimating loop constraints through Gaussian-based Generalized Iterative Closest Point registration, followed by pose-graph optimization. We also collect challenging large-scale looped outdoor sequences with hardware-synchronized LiDAR-camera-IMU and ground-truth trajectories for realistic evaluation. Extensive experiments on both public datasets and our dataset demonstrate that the proposed method achieves a state of the art among real-time efficiency, localization accuracy, and rendering quality across diverse real-world scenes.

  </details>

- **[PDF-GS: Progressive Distractor Filtering for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2604.12580)**  
  *Kangmin Seo, MinKyu Lee, Tae-Young Kim, ByeongCheol Lee, JoonSeoung An, Jae-Pil Heo*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.12580) · [pdf](https://arxiv.org/pdf/2604.12580.pdf)
  > 💡 针对3DGS对多视角不一致干扰敏感问题，提出渐进式多阶段过滤方法，实现鲁棒高质量无干扰重建。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled impressive real-time photorealistic rendering. However, conventional training pipelines inherently assume full multi-view consistency among input images, which makes them sensitive to distractors that violate this assumption and cause visual artifacts. In this work, we revisit an underexplored aspect of 3DGS: its inherent ability to suppress inconsistent signals. Building on this insight, we propose PDF-GS (Progressive Distractor Filtering for Robust 3D Gaussian Splatting), a framework that amplifies this self-filtering property through a progressive multi-phase optimization. The progressive filtering phases gradually remove distractors by exploiting discrepancy cues, while the following reconstruction phase restores fine-grained, view-consistent details from the purified Gaussian representation. Through this iterative refinement, PDF-GS achieves robust, high-fidelity, and distractor-free reconstructions, consistently outperforming baselines across diverse datasets and challenging real-world conditions. Moreover, our approach is lightweight and easily adaptable to existing 3DGS frameworks, requiring no architectural changes or additional inference overhead, leading to a new state-of-the-art performance. The code is publicly available at https://github.com/kangrnin/PDF-GS.

  </details>

- **[Ψ-Map: Panoptic Surface Integrated Mapping Enables Real2Sim Transfer](https://arxiv.org/abs/2604.10982)**  
  *Xuan Yu, Yuxuan Xie, Changjian Jiang, Shichao Zhai, Rong Xiong, Yu Zhang, Yue Wang*  
  `2026-04-13` · `cs.RO` · [abs](https://arxiv.org/abs/2604.10982) · [pdf](https://arxiv.org/pdf/2604.10982.pdf)
  > 💡 提出几何强化、端到端全景学习与高效渲染框架，利用LiDAR平面约束和2D高斯曲面，实现高精度表面重建与全局一致全景分割，推理超40FPS。

  <details><summary>Abstract</summary>

  Open-vocabulary panoptic reconstruction is essential for advanced robotics perception and simulation. However, existing methods based on 3D Gaussian Splatting (3DGS) often struggle to simultaneously achieve geometric accuracy, coherent panoptic understanding, and real-time inference frequency in large-scale scenes. In this paper, we propose a comprehensive framework that integrates geometric reinforcement, end-to-end panoptic learning, and efficient rendering. First, to ensure physical realism in large-scale environments, we leverage LiDAR data to construct plane-constrained multimodal Gaussian Mixture Models (GMMs) and employ 2D Gaussian surfels as the map representation, enabling high-precision surface alignment and continuous geometric supervision. Building upon this, to overcome the error accumulation and cumbersome cross-frame association inherent in traditional multi-stage panoptic segmentation pipelines, we design a query-guided end-to-end learning architecture. By utilizing a local cross-attention mechanism within the view frustum, the system lifts 2D mask features directly into 3D space, achieving globally consistent panoptic understanding. Finally, addressing the computational bottlenecks caused by high-dimensional semantic features, we introduce Precise Tile Intersection and a Top-K Hard Selection strategy to optimize the rendering pipeline. Experimental results demonstrate that our system achieves superior geometric and panoptic reconstruction quality in large-scale scenes while maintaining an inference rate exceeding 40 FPS, meeting the real-time requirements of robotic control loops.

  </details>

- **[From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians](https://arxiv.org/abs/2604.07337)**  
  *Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, Maks Ovsjanikov*  
  `2026-04-08` · `cs.CV` · [abs](https://arxiv.org/abs/2604.07337) · [pdf](https://arxiv.org/pdf/2604.07337.pdf)
  > 💡 针对3DGS表面重建难题，通过可学习有向高斯及占用场公式，结合一致性损失与稠密化策略，实现高精度水

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized fast novel view synthesis, yet its opacity-based formulation makes surface extraction fundamentally difficult. Unlike implicit methods built on Signed Distance Fields or occupancy, 3DGS lacks a global geometric field, forcing existing approaches to resort to heuristics such as TSDF fusion of blended depth maps. Inspired by the Objects as Volumes framework, we derive a principled occupancy field for Gaussian Splatting and show how it can be used to extract highly accurate watertight meshes of complex scenes. Our key contribution is to introduce a learnable oriented normal at each Gaussian element and to define an adapted attenuation formulation, which leads to closed-form expressions for both the normal and occupancy fields at arbitrary locations in space. We further introduce a novel consistency loss and a dedicated densification strategy to enforce Gaussians to wrap the entire surface by closing geometric holes, ensuring a complete shell of oriented primitives. We modify the differentiable rasterizer to output depth as an isosurface of our continuous model, and introduce Primal Adaptive Meshing for Region-of-Interest meshing at arbitrary resolution. We additionally expose fundamental biases in standard surface evaluation protocols and propose two more rigorous alternatives. Overall, our method Gaussian Wrapping sets a new state-of-the-art on DTU and Tanks and Temples, producing complete, watertight meshes at a fraction of the size of concurrent work-recovering thin structures such as the notoriously elusive bicycle spokes.

  </details>

- **[Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D Gaussian Splatting under Constrained GPU Budgets](https://arxiv.org/abs/2604.07177)**  
  *Muhammad Fahim Tajwar, Arthur Wuhrlin, Bhojan Anand*  
  `2026-04-08` · `cs.GR` · [abs](https://arxiv.org/abs/2604.07177) · [pdf](https://arxiv.org/pdf/2604.07177.pdf)
  > 💡 通过模拟不同GPU能力层级，探究实时3DGS在受限预算下的性能与能耗权衡，评估边缘部署可行性。

  <details><summary>Abstract</summary>

  We investigate the feasibility of real-time 3D Gaussian Splatting (3DGS) rasterisation on edge clients with varying Gaussian splat counts and GPU computational budgets. Instead of evaluating multiple physical devices, we adopt an emulation-based approach that approximates different GPU capability tiers on a single high-end GPU. By systematically under-clocking the GPU core frequency and applying power caps, we emulate a controlled range of floating-point performance levels that approximate different GPU capability tiers. At each point in this range, we measure frame rate, runtime behaviour, and power consumption across scenes of varying complexity, pipelines, and optimisations, enabling analysis of power-performance relationships such as FPS-power curves, energy per frame, and performance per watt. This method allows us to approximate the performance envelope of a diverse class of GPUs, from embedded and mobile-class devices to high-end consumer-grade systems. Our objective is to explore the practical lower bounds of client-side 3DGS rasterisation and assess its potential for deployment in energy-constrained environments, including standalone headsets and thin clients. Through this analysis, we provide early insights into the performance-energy trade-offs that govern the viability of edge-deployed 3DGS systems.

  </details>

- **[GEMM-GS: Accelerating 3D Gaussian Splatting on Tensor Cores with GEMM-Compatible Blending](https://arxiv.org/abs/2604.02120)**  
  *Haomin Li, Bowen Zhu, Fangxin Liu, Zongwu Wang, Xinran Liang, Li Jiang, Haibing Guan*  
  `2026-04-02` · `cs.AR` · [abs](https://arxiv.org/abs/2604.02120) · [pdf](https://arxiv.org/pdf/2604.02120.pdf)
  > 💡 针对3DGS渲染慢且缺乏GEMM操作，提出GEMM-GS将混合过程转为GEMM兼容形式以利用张量核，实现1.

  <details><summary>Abstract</summary>

  Neural Radiance Fields (NeRF) enables 3D scene reconstruction from several 2D images but incurs high rendering latency via its point-sampling design. 3D Gaussian Splatting (3DGS) improves on NeRF with explicit scene representation and an optimized pipeline yet still fails to meet practical real-time demands. Existing acceleration works overlook the evolving Tensor Cores of modern GPUs because 3DGS pipeline lacks General Matrix Multiplication (GEMM) operations. This paper proposes GEMM-GS, an acceleration approach utilizing tensor cores on GPUs via GEMM-friendly blending transformation. It equivalently reformulates the 3DGS blending process into a GEMM-compatible form to utilize Tensor Cores. A high-performance CUDA kernel is designed, integrating a three-stage double-buffered pipeline that overlaps computation and memory access. Extensive experiments show that GEMM-GS achieves $1.42\times$ speedup over vanilla 3DGS and provides an additional $1.47\times$ speedup on average when combining with existing acceleration approaches. Code is released at https://github.com/shieldforever/GEMM-GS.

  </details>

- **[LESV: Language Embedded Sparse Voxel Fusion for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2604.01388)**  
  *Fusang Wang, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Fabien Moutarde*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01388) · [pdf](https://arxiv.org/pdf/2604.01388.pdf)
  > 💡 针对3DGS开集场景理解的空间和语义模糊，提出稀疏体素光栅化SVRaster与AM-RADIO对齐，实现确定性特征注册并抑制渗漏，性能SOTA。

  <details><summary>Abstract</summary>

  Recent advancements in open-vocabulary 3D scene understanding heavily rely on 3D Gaussian Splatting (3DGS) to register vision-language features into 3D space. However, we identify two critical limitations in these approaches: the spatial ambiguity arising from unstructured, overlapping Gaussians which necessitates probabilistic feature registration, and the multi-level semantic ambiguity caused by pooling features over object-level masks, which dilutes fine-grained details. To address these challenges, we present a novel framework that leverages Sparse Voxel Rasterization (SVRaster) as a structured, disjoint geometry representation. By regularizing SVRaster with monocular depth and normal priors, we establish a stable geometric foundation. This enables a deterministic, confidence-aware feature registration process and suppresses the semantic bleeding artifact common in 3DGS. Furthermore, we resolve multi-level ambiguity by exploiting the emerging dense alignment properties of foundation model AM-RADIO, avoiding the computational overhead of hierarchical training methods. Our approach achieves state-of-the-art performance on Open Vocabulary 3D Object Retrieval and Point Cloud Understanding benchmarks, particularly excelling on fine-grained queries where registration methods typically fail.

  </details>

- **[DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting with Cross-View Joint Optimization](https://arxiv.org/abs/2604.00648)**  
  *Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.00648) · [pdf](https://arxiv.org/pdf/2604.00648.pdf)
  > 💡 鱼眼畸变导致3DGS预处理损失信息与产生漂浮物，提出原生鱼眼模型集成与跨视图联合优化，提升重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has enabled efficient 3D scene reconstruction from everyday images with real-time, high-fidelity rendering, greatly advancing VR/AR applications. Fisheye cameras, with their wider field of view (FOV), promise high-quality reconstructions from fewer inputs and have recently attracted much attention. However, since 3DGS relies on rasterization, most subsequent works involving fisheye camera inputs first undistort images before training, which introduces two problems: 1) Black borders at image edges cause information loss and negate the fisheye's large FOV advantage; 2) Undistortion's stretch-and-interpolate resampling spreads each pixel's value over a larger area, diluting detail density -- causes 3DGS overfitting these low-frequency zones, producing blur and floating artifacts. In this work, we integrate fisheye camera model into the original 3DGS framework, enabling native fisheye image input for training without preprocessing. Despite correct modeling, we observed that the reconstructed scenes still exhibit floaters at image edges: Distortion increases toward the periphery, and 3DGS's original per-iteration random-selecting-view optimization ignores the cross-view correlations of a Gaussian, leading to extreme shapes (e.g., oversized or elongated) that degrade reconstruction quality. To address this, we introduce a feature-overlap-driven cross-view joint optimization strategy that establishes consistent geometric and photometric constraints across views-a technique equally applicable to existing pinhole-camera-based pipelines. Our DirectFisheye-GS matches or surpasses state-of-the-art performance on public datasets. Project Page: https://yzxqh.github.io/DirectFisheye-GS/ .

  </details>

- **[TreeGaussian: Tree-Guided Cascaded Contrastive Learning for Hierarchical Consistent 3D Gaussian Scene Segmentation and Understanding](https://arxiv.org/abs/2604.03309)**  
  *Jingbin You, Zehao Li, Hao Jiang, Xinzhu Ma, Shuqin Gao, Honglong Zhao, Congcong Zheng, Tianlu Mao, Feng Dai, Yucheng Zhang, Zhaoqi Wang*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03309) · [pdf](https://arxiv.org/pdf/2604.03309.pdf)
  > 💡 针对3DGS难以建模层次化语义和整体-部分关系的问题，TreeGaussian用树引导级联对比学习框架实现一致分割和理解。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a real-time, differentiable representation for neural scene understanding. However, existing 3DGS-based methods struggle to represent hierarchical 3D semantic structures and capture whole-part relationships in complex scenes. Moreover, dense pairwise comparisons and inconsistent hierarchical labels from 2D priors hinder feature learning, resulting in suboptimal segmentation. To address these limitations, we introduce TreeGaussian, a tree-guided cascaded contrastive learning framework that explicitly models hierarchical semantic relationships and reduces redundancy in contrastive supervision. By constructing a multi-level object tree, TreeGaussian enables structured learning across object-part hierarchies. In addition, we propose a two-stage cascaded contrastive learning strategy that progressively refines feature representations from global to local, mitigating saturation and stabilizing training. A Consistent Segmentation Detection (CSD) mechanism and a graph-based denoising module are further introduced to align segmentation modes across views while suppressing unstable Gaussian points, enhancing segmentation consistency and quality. Extensive experiments, including open-vocabulary 3D object selection, 3D point cloud understanding, and ablation studies, demonstrate the effectiveness and robustness of our approach.

  </details>

- **[Confidence-Based Mesh Extraction from 3D Gaussians](https://arxiv.org/abs/2603.24725)**  
  *Lukas Radl, Felix Windisch, Andreas Kurz, Thomas Köhler, Michael Steiner, Markus Steinberger*  
  `2026-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2603.24725) · [pdf](https://arxiv.org/pdf/2603.24725.pdf)
  > 💡 针对视图依赖场景下网格提取困难，提出自监督置信度框架动态平衡光度与几何监督，并引入颜色法线方差损失，实现高效SOTA网格提取。

  <details><summary>Abstract</summary>

  Recently, 3D Gaussian Splatting (3DGS) greatly accelerated mesh extraction from posed images due to its explicit representation and fast software rasterization. While the addition of geometric losses and other priors has improved the accuracy of extracted surfaces, mesh extraction remains difficult in scenes with abundant view-dependent effects. To resolve the resulting ambiguities, prior works rely on multi-view techniques, iterative mesh extraction, or large pre-trained models, sacrificing the inherent efficiency of 3DGS. In this work, we present a simple and efficient alternative by introducing a self-supervised confidence framework to 3DGS: within this framework, learnable confidence values dynamically balance photometric and geometric supervision. Extending our confidence-driven formulation, we introduce losses which penalize per-primitive color and normal variance and demonstrate their benefits to surface extraction. Finally, we complement the above with an improved appearance model, by decoupling the individual terms of the D-SSIM loss. Our final approach delivers state-of-the-art results for unbounded meshes while remaining highly efficient.

  </details>

- **[Accurate Point Measurement in 3DGS -- A New Alternative to Traditional Stereoscopic-View Based Measurements](https://arxiv.org/abs/2603.24716)**  
  *Deyan Deng, Rongjun Qin*  
  `2026-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2603.24716) · [pdf](https://arxiv.org/pdf/2603.24716.pdf)
  > 💡 针对3DGS几何测量未被充分利用，提出利用跨视图选点三角化，实现无需立体工作站的精确测量，精度匹敌传统方法。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized real-time rendering with its state-of-the-art novel view synthesis, but its utility for accurate geometric measurement remains underutilized. Compared to multi-view stereo (MVS) point clouds or meshes, 3DGS rendered views present superior visual quality and completeness. However, current point measurement methods still rely on demanding stereoscopic workstations or direct picking on often-incomplete and inaccurate 3D meshes. As a novel view synthesizer, 3DGS renders exact source views and smoothly interpolates in-between views. This allows users to intuitively pick congruent points across different views while operating 3DGS models. By triangulating these congruent points, one can precisely generate 3D point measurements. This approach mimics traditional stereoscopic measurement but is significantly less demanding: it requires neither a stereo workstation nor specialized operator stereoscopic capability. Furthermore, it enables multi-view intersection (more than two views) for higher measurement accuracy. We implemented a web-based application to demonstrate this proof-of-concept (PoC). Using several UAV aerial datasets, we show this PoC allows users to successfully perform highly accurate point measurements, achieving accuracy matching or exceeding traditional stereoscopic methods on standard hardware. Specifically, our approach significantly outperforms direct mesh-based measurements. Quantitatively, our method achieves RMSEs in the 1-2 cm range on well-defined points. More critically, on challenging thin structures where mesh-based RMSE was 0.062 m, our method achieved 0.037 m. On sharp corners poorly reconstructed in the mesh, our method successfully measured all points with a 0.013 m RMSE, whereas the mesh method failed entirely. Code is available at: https://github.com/GDAOSU/3dgs_measurement_tool.

  </details>

- **[Stochastic Ray Tracing for the Reconstruction of 3D Gaussian Splatting](https://arxiv.org/abs/2603.23637)**  
  *Peiyu Xu, Xin Sun, Krishna Mullia, Raymond Fei, Iliyan Georgiev, Shuang Zhao*  
  `2026-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2603.23637) · [pdf](https://arxiv.org/pdf/2603.23637.pdf)
  > 💡 针对3DGS射线追踪排序慢和近似阴影问题，提出无排序随机射线追踪，用蒙特卡洛梯度估计实现高效高质量标准与可重光照重建。

  <details><summary>Abstract</summary>

  Ray-tracing-based 3D Gaussian splatting (3DGS) methods overcome the limitations of rasterization -- rigid pinhole camera assumptions, inaccurate shadows, and lack of native reflection or refraction -- but remain slower due to the cost of sorting all intersecting Gaussians along every ray. Moreover, existing ray-tracing methods still rely on rasterization-style approximations such as shadow mapping for relightable scenes, undermining the generality that ray tracing promises. We present a differentiable, sorting-free stochastic formulation for ray-traced 3DGS -- the first framework that uses stochastic ray tracing to both reconstruct and render standard and relightable 3DGS scenes. At its core is an unbiased Monte Carlo estimator for pixel-color gradients that evaluates only a small sampled subset of Gaussians per ray, bypassing the need for sorting. For standard 3DGS, our method matches the reconstruction quality and speed of rasterization-based 3DGS while substantially outperforming sorting-based ray tracing. For relightable 3DGS, the same stochastic estimator drives per-Gaussian shading with fully ray-traced shadow rays, delivering notably higher reconstruction fidelity than prior work.

  </details>

- **[GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192)**  
  *Yan Fang, Jianfei Ge, Jiangjian Xiao*  
  `2026-03-24` · `cs.GR` · [abs](https://arxiv.org/abs/2603.23192) · [pdf](https://arxiv.org/pdf/2603.23192.pdf)
  > 💡 针对传统3DGS尺度模糊和几何一致性差，提出LiDAR度量感知分配与曲率自适应细化，实现高保真几何重建。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled real-time, photorealistic scene reconstruction. However, conventional 3DGS frameworks typically rely on sparse point clouds derived from Structure-from-Motion (SfM), which inherently suffer from scale ambiguity, limited geometric consistency, and strong view dependency due to the lack of geometric priors. In this work, a LiDAR-centric 3D Gaussian Splatting framework is proposed that explicitly incorporates metric geometric priors into the entire Gaussian optimization process. Instead of treating LiDAR data as a passive initialization source, 3DGS optimization is reformulated as a geometry-conditioned allocation and refinement problem under a fixed representational budget. Specifically, this work introduces (i) a geometry-texture-aware allocation strategy that selectively assigns Gaussian primitives to regions with high structural or appearance complexity, (ii) a curvature-adaptive refinement mechanism that dynamically guides Gaussian splitting toward geometrically complex areas during training, and (iii) a confidence-aware metric depth regularization that anchors the reconstructed geometry to absolute scale using LiDAR measurements while maintaining optimization stability. Extensive experiments on the ScanNet++ dataset and a custom real-world dataset validate the proposed approach. The results demonstrate state-of-the-art performance in metric-scale reconstruction with high geometric fidelity.

  </details>

