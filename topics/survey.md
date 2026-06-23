# Survey & Benchmark

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---








## 2026-06-23

- **[Temporally Aware Densification for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.23212)**  
  *Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23212) · [pdf](https://arxiv.org/pdf/2606.23212.pdf)
  > 💡 提出可见性感知致密化，用时域自适应阈值和偏移扭曲改进动态高斯致密化，提升动态场景重建质量。

  <details><summary>Abstract</summary>

  Despite modeling temporal motion, dynamic 3D Gaussian Splatting (3DGS) methods still inherit a static densification strategy that is ill-suited for dynamic scenes. This neglect of temporal behavior leads to under-reconstructed and blurry dynamic regions, as short-lived Gaussians receive sparse supervision and fail to densify effectively. We propose a Visibility-Aware Densification (VAD) framework that integrates temporal visibility into the densification process, ensuring that Gaussians are refined based on their actual temporal presence. A Temporally-Adaptive Thresholding (TAT) mechanism further adjusts each Gaussian's densification threshold according to its temporal lifespan, promoting balanced refinement of both static and dynamic regions. Finally, a Temporal Offset Warping (TOW) design enhances deformation capacity around temporal centers, extending the lifespan of highly dynamic Gaussians and facilitating more effective densification. Our approach achieves substantial improvements in the visual quality of dynamic regions, outperforming existing methods across three dynamic multi-view benchmark datasets. Moreover, the proposed VAD module generalizes across diverse dynamic 3DGS methods, consistently improving dynamic reconstruction as a plug-and-play component.

  </details>

- **[DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction](https://arxiv.org/abs/2606.23031)**  
  *Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23031) · [pdf](https://arxiv.org/pdf/2606.23031.pdf)
  > 💡 提出组合稀疏体素光栅化框架，用多八叉树表示动态与静态场景，通过LiDAR先验加速训练，高效重建动态驾驶场景。

  <details><summary>Abstract</summary>

  Reconstructing dynamic urban scenes remains challenging due to the unbounded nature of driving environments and the presence of multiple dynamic objects. Currently, potentially faster sparse voxel methods are mainly designed for static scenarios. On the other hand, dynamic approaches based on 3D Gaussian Splatting, despite their high-fidelity, are often time-consuming for driving scenarios and exhibit uncontrollable memory growth in large scenes. To address these limitations, we present DrivingVoxels, a compositional sparse voxel rendering framework for dynamic driving scenes. Our method jointly rasterizes sparse voxels from multiple independent octrees within a single rendering pass. Each rigid dynamic object is represented by an octree defined in its local coordinate frame, while a separate static octree models the stationary background. DrivingVoxels adopts a fully explicit, neural-free representation together with a LiDAR-guided structural initialization that efficiently captures scene geometry. We evaluate our framework on the PandaSet benchmark, demonstrating that DrivingVoxels performs on par on perceptual metrics and better on structural metrics for NVS and reconstruction while requiring shorter training times than previous 3DGS-base methods to an efficient optimization workflow anchored by a strong LiDAR prior.

  </details>

- **[LOGOS: LiDAR-Only Gaussian Elevation Splatting for Unified Tiny Obstacle Segmentation](https://arxiv.org/abs/2606.21527)**  
  *Nan Ming, Yeqiang Qian, Chunxiang Wang, Ming Yang*  
  `2026-06-19` · `cs.RO` · [abs](https://arxiv.org/abs/2606.21527) · [pdf](https://arxiv.org/pdf/2606.21527.pdf)
  > 💡 提出基于2D高斯原语的无反向传播LiDAR高程溅射方法，实现微小障碍物鲁棒分割，在退化点云中性能显著优于现有方法。

  <details><summary>Abstract</summary>

  Robust obstacle segmentation is essential for the safety of intelligent robots, where LiDAR-based perception systems play a fundamental role in the robot-environment interaction. While extensive LiDAR-based approaches have demonstrated high performance on common obstacles in urban scenarios, their results on tiny obstacles such as curbs, gravel, and potholes remain unsatisfactory due to the significant similarity between tiny obstacles and inherent road undulations. Moreover, their segmentation accuracy even deteriorates sharply when the LiDAR scans suffer from degradation in challenging off-road scenes. To overcome these bottlenecks, we propose LOGOS, a LiDAR-only unified tiny obstacle segmentation system, which models the road surface as a continuous mixture of 2D Gaussian primitives and distinguishes tiny obstacles via high-presicion elevation estimation. Unlike existing Gaussian splatting methods that rely on iterative RGB training, LOGOS is a backpropagation-free LiDAR-only approach. It directly estimates Gaussian parameters via a freespace-aware initialization by incrementally pruning non-road primitives using smoothness constraints. Subsequently, pointwise signed distances are computed via a novel normal-aware elevation splatting function, ensuring robustness to both flat and sloped terrains. We evaluate LOGOS on a highly heterogeneous benchmark of point cloud frames collected from urban mobility scenarios and mining haulage off-road environments. These data are practically acquired using different LiDAR sensors and exhibit large variations in point density, terrain roughness, and obstacle types. Experiments on the road and off-road scenes demonstrate that LOGOS significantly outperforms other state-of-the-art methods, particularly in degraded point cloud regions and challenging off-road scenarios, while maintaining real-time efficiency.

  </details>

- **[ACE-GS: Acing the Trade-off with Accurate, Compact and Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2606.21244)**  
  *Jijian Zhao*  
  `2026-06-19` · `cs.CV` · [abs](https://arxiv.org/abs/2606.21244) · [pdf](https://arxiv.org/pdf/2606.21244.pdf)
  > 💡 ACE-GS通过动量一致稠密化、统计剪枝和跨维频率补偿，在3-5分钟收敛，加速3.7倍并提升PSNR 0.89dB。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting achieves exceptional real-time rendering, but its substantial computational and storage demands hinder widespread deployment. Existing accelerated paradigms often aggressively prune primitives for rapid convergence, causing severe loss of high-frequency details. To address this, we tackle the fundamental problem of achieving both exceptional rendering quality and ultra-fast reconstruction speed. In this paper, we propose ACE-GS, a progressive optimization framework tailored for accurate, compressed, and efficient scene representation. We realize that precise primitive management is the key to breaking this trade-off. Therefore, we first design a momentum consistency-guided densification strategy, strictly constraining primitive growth onto authentic geometric manifolds to avoid computational waste while significantly accelerating convergence. Building upon this efficient initialization, we deploy a statistical sensitivity-driven sparsification mechanism to precisely prune redundant primitives, yielding a further compressed footprint. Finally, to thoroughly compensate for the risk of micro-structure loss caused by the aforementioned strict primitive control, we introduce a cross-dimensional residual frequency compensation scheme that explicitly back-injects high-frequency error energy into primitive attributes, perfectly restoring sharp geometric details. Extensive experiments validate our superiority. While maintaining a highly compact scene representation, our system achieves up to 3.7 times training acceleration against the rapid framework Speedy-Splat. Requiring only 3 to 5 minutes to converge, ACE-GS secures the highest structural similarity and achieves a peak PSNR improvement of up to 0.89 dB over the original 3DGS, establishing a new benchmark for ultra-fast and high-fidelity novel view synthesis.

  </details>

## 2026-06-16

- **[MVM-IOD: An Industrial Object-Centric Benchmark Dataset for the Evaluation of 3D Reconstruction Methods](https://arxiv.org/abs/2606.16638)**  
  *Robert Langendörfer, Markus Hillemann, Markus Ulrich*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16638) · [pdf](https://arxiv.org/pdf/2606.16638.pdf)
  > 💡 针对工业物体3D重建评估缺乏真实数据集的问题，提出MVM-IOD基准，评估多种方法并发现前馈方法在分布外图像上效果不佳。

  <details><summary>Abstract</summary>

  3D object reconstruction, and camera pose estimation in industrial applications are challenging tasks, as errors are costly while the computation time is often limited. The complexity of typical industrial objects further complicates these tasks. Most of the existing datasets in this context do not depict realistic industrial scenarios. Therefore, we introduce the Machine Vision Metrology Industrial Object Dataset (MVM-IOD). Images of typical industrial objects are captured systematically, by moving a camera, mounted at the end effector of an industrial robot arm, on a hemisphere around the objects. MVM-IOD contains reference camera poses and reference 3D point clouds, the acquired RGB images of 9 objects and 2 background choices resulting in 18 scenes, which allows evaluation of all image based methods that compute a 3D reconstruction, camera poses, or novel views of a scene. Based on MVM-IOD, we extensively evaluate current SOTA 3D reconstruction and camera pose estimation methods, such as Structure from Motion, Multi-View Stereo, recent feed forward methods (Visual Geometry Grounded Transformer, π3), and 2D Gaussian Splatting and report our findings as a baseline for future research. The experiments show that capture setups like ours generate out-of distribution images for feed forward methods, leading to suboptimal point clouds and camera poses. However, these out-of-distribution images can be shifted closer to the training distribution by applying simple preprocessing steps. Consequently, in certain industrial applications, feed forward methods should be used with caution.

  </details>

- **[Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing](https://arxiv.org/abs/2606.16168)**  
  *Yuhan Chen, Ying Fang, Guofa Li, Wenxuan Yu, Yicui Shi, Kunyang Huang, Wenbo Chu, Keqiang Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16168) · [pdf](https://arxiv.org/pdf/2606.16168.pdf)
  > 💡 采用频率感知隐式高斯泼溅解耦高低频信息，结合物理散射重归一化，实现单图像去雾SOTA。

  <details><summary>Abstract</summary>

  Single image dehazing continues to be hindered by the loss of high-frequency details and the difficulty of accurate physical scattering modeling. To address these issues, we propose Fi-Gaussian, a frequency-aware implicit Gaussian splatting network for single image dehazing. Unlike explicit rendering methods that rely on 3D point clouds, our method employs implicit Gaussian splatting to adaptively model the underlying distribution of clear images as a continuous representation in 2D feature space. The core of the network is a frequency-aware implicit Gaussian splatting module, which decouples low-frequency structural information and high-frequency texture information in the frequency domain and then performs adaptive Gaussian aggregation with complex-valued weights to recover fine details. In addition, a physics-driven scattering renormalization mechanism is introduced to estimate the transmission map and atmospheric light under the guidance of implicit Gaussian priors. Extensive experiments on multiple benchmark datasets demonstrate that Fi-Gaussian achieves state-of-the-art quantitative performance and produces visually superior dehazed results, validating the effectiveness of implicit Gaussian splatting for low-level vision tasks.

  </details>

- **[SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction](https://arxiv.org/abs/2606.15659)**  
  *Yiran Wang, Zeyu Zhang, Yuanming Li, Ziming Wang, Yang Zhao*  
  `2026-06-14` · `cs.CV` · [abs](https://arxiv.org/abs/2606.15659) · [pdf](https://arxiv.org/pdf/2606.15659.pdf)
  > 💡 通过共享FLAME绑定的高斯表示和多阶段重建，解决前馈与优化器

  <details><summary>Abstract</summary>

  High-quality 4D head avatars from one or a few source portraits are central to telepresence, AR/VR, and digital-human interaction. 3D Gaussian Splatting (3DGS) has emerged as the dominant representation, with two complementary regimes (generalizable feed-forward predictors and per-subject refiners) maturing in parallel. However, existing feed-forward predictors are trained on a single dataset family with a hard-coded source count, inheriting the corresponding domain bias. Per-subject refiners require 300K--600K iterations and rely on adaptive densification that destroys upstream Gaussian layouts, preventing the two regimes from sharing a representation end-to-end. To bridge both regimes we propose SpatialAvatar-0 on a shared FLAME-mesh-bound Gaussian representation: a feed-forward generator with a parameter-free K-source mean-pool and a monocular-temporal to multi-view-spatial two-phase schedule that anchors against identity-prior collapse onto the smaller multi-view set. We further introduce a 10K-iter layout-preserving per-subject refinement loop that freezes the FLAME-binding and Gaussian count and replaces densification with a three-component anti-spike regularization. On VFHQ/HDTF cross-domain zero-shot we surpass the in-domain leader GAGAvatar by +1.5 dB PSNR despite never training on either test domain, and on the SplattingAvatar monocular benchmark we lead every reported metric, surpassing the 300K-iter GeoAvatar by +1.3 dB PSNR at up to 60x shorter per-subject schedule than common SOTA baselines. Website: https://spatialwalk.github.io/SpatialAvatar-0.

  </details>

## 2026-06-10

- **[WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129)**  
  *Yuke Zhao, Wangbo Zhao, Weijie Wang, Zeyu Zhang, Dakai An, Akide Liu, Yinghao Yu, Jiasheng Tang, Fan Wang, Wei Wang, Bohan Zhuang*  
  `2026-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11129) · [pdf](https://arxiv.org/pdf/2606.11129.pdf)
  > 💡 提出WorldOlympiad基准，从物理、几何、交互三维度评估视频世界模型，揭示其在物理和3D一致性上的不足。

  <details><summary>Abstract</summary>

  We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity. While existing benchmarks often focus on visual quality, semantic alignment, or short-term temporal coherence, they provide limited insight into whether generated videos obey physical rules, preserve coherent 3D structure, and sustain controllable interactions over long horizons. To address this gap, WorldOlympiad decomposes world-model evaluation into three complementary dimensions. The physical track uses object segmentation and MLLM-as-judge to assess whether generated videos follow interpretable rules in mechanics, thermal phenomena, and material properties. The geometry track reconstructs generated videos with Gaussian splatting and evaluates structural consistency, cross-view coherence, and camera-trajectory alignment. The interaction track assesses whether generated rollouts follow complex action prompts and maintain smooth, coherent transitions across consecutive video chunks. WorldOlympiad further covers three major downstream scenarios, including gaming, robotics, and general real-world videos, capturing diverse challenges from interactive control and embodied manipulation to open-domain motion and camera dynamics. Together, these tracks and scenarios form a scalable and interpretable evaluation suite that exposes failure modes beyond generic video quality. Experiments on state-of-the-art models reveal substantial gaps in physical reasoning, 3D consistency, and long-horizon interaction, underscoring the need for more structured evaluation protocols for generative world models.

  </details>

## 2026-06-09

- **[REFINE: Super-efficient 3D Gaussian Splatting Pruning via Rendering-Free Primitive Importance](https://arxiv.org/abs/2606.09074)**  
  *Zhang Chen, Shuai Wan, Mengting Yu, Fuzheng Yang, Junhui Hou*  
  `2026-06-08` · `cs.CV` · [abs](https://arxiv.org/abs/2606.09074) · [pdf](https://arxiv.org/pdf/2606.09074.pdf)
  > 💡 针对3DGS剪枝效率低的问题，提出基于无渲染Hessian场的重要性度量，实现3000倍加速且保持

  <details><summary>Abstract</summary>

  Existing pruning methods for 3D Gaussian splatting (3DGS) suffer from either severe quality degradation or prohibitive computational overhead. In this paper, we propose REFINE, a highly accelerated 3DGS pruning framework centered on a novel rendering-free primitive importance metric. Our approach leverages an analytically approximated, rendering-aware Hessian field to quantify the expected perceptual error induced by the removal of individual primitives. By modeling the joint modulation of visibility, projection geometry and the content adaptive hyperparameter, we entirely bypass costly forward rendering passes and derive an anisotropic perceptual weight field that serves as a high-fidelity proxy for primitive importance. Extensive experiments across multiple benchmark datasets demonstrate that REFINE maintains highly competitive rendering quality while achieving an unprecedented $3,000\times$ reduction in pruning-related computational complexity compared to state-of-the-art pruning methods.

  </details>

## 2026-06-08

- **[RPC-GS: Gaussian Splatting with native RPC Rendering for Satellite Imagery](https://arxiv.org/abs/2606.06690)**  
  *Valentin Wagner, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens*  
  `2026-06-04` · `cs.CV` · [abs](https://arxiv.org/abs/2606.06690) · [pdf](https://arxiv.org/pdf/2606.06690.pdf)
  > 💡 针对卫星影像高斯泼溅中相机模型近似导致几何误差的问题，提出原生RPC渲染框架，通过直接投影与雅可比协方差变换，显著降低重建误差。

  <details><summary>Abstract</summary>

  We present RPC-GS, the first Gaussian Splatting framework for satellite imagery that operates natively with Rational Polynomial Camera (RPC) models. The RPC model is the de facto standard for representing the complex imaging geometry of modern pushbroom satellite sensors. To simplify rendering, prior satellite Gaussian Splatting methods replace the RPC model with perspective or affine camera approximations, leading to geometric errors during reconstruction. RPC-GS avoids these approximations by projecting Gaussian means and covariances directly through the RPC model during the splatting process. We embed the RPC model in a chain of carefully selected geo-coordinate transformations representing a mapping from splatting-suitable scene coordinates to image coordinates. To map the Gaussian covariance matrices, we derive a numerically robust Jacobian-based covariance projection for the (partially nonlinear) coordinate transformations. Since RPCs lack an explicit notion of camera depth, we integrate a metric ray-based depth formulation. We benchmark RPC, perspective, and affine camera models in a unified framework, with our native RPC renderer consistently achieving the lowest reconstruction error on leading satellite benchmark datasets, improving mean altitude error over perspective and affine approximations by 29.6% and 63.8% on DFC2019, and by 9.9% and 37.9% on IARPA2016. We release our code to support future research of Gaussian Splatting in the satellite imaging domain.

  </details>

## 2026-06-06

- **[Recent Advances and Trends in Learning-based 3D Representations](https://arxiv.org/abs/2606.04871)**  
  *Adrien Schockaert, Hamid Laga, Hazem Wannous, Vincent Magnier, Guillaume Dufaye, Jean-françois Witz*  
  `2026-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2606.04871) · [pdf](https://arxiv.org/pdf/2606.04871.pdf)
  > 💡 综述了3D表示从离散显式到连续隐式的演变，侧重神经渲染与高斯泼溅，揭示范式转变。

  <details><summary>Abstract</summary>

  The selection of an appropriate 3D representation is a fundamental design decision that dictates the efficiency, quality, and capabilities of modern computer vision and graphics pipelines for tasks such as 3D reconstruction, novel-view synthesis and rendering, shape and motion analysis, recognition, and generation. While traditional representations (\eg meshes, point clouds, and volumetric grids) remain standard outputs of 3D sensors (\eg LiDAR and 3D scanners) and are widely used in downstream applications (\eg editing and simulation), recent neural and primitive-based representations (\eg 3D Gaussian Splatting) offer compact and differentiable alternatives opening a wide range of opportunities in applications such as games, AR/VR, autonomous driving, robot navigation, and medical imaging, to name a few. The goal of this paper is to survey the main families of 3D representations from discrete explicit formats to continuous implicit fields based either on neural rendering or primitive splatting. For each type of representation, we present the general formulation and its variants, discuss its benefits and limitations, and highlight key applications. We conclude the paper by outlining the open challenges and potential directions for future research. Distinct from recent surveys that broadly cover 3D object and scene reconstruction, this paper provides a focused analysis on the evolution of 3D representations themselves. We specifically emphasize the paradigm shift toward implicit representations, offering a novel perspective on how these emerging formats fundamentally alter 3D/4D workflows.

  </details>

- **[GN0: Toward a Unified Paradigm for Generation, Evaluation, and Policy Learning in Visual-Language Navigation](https://arxiv.org/abs/2606.03682)**  
  *Xinhai Li, Xiaotao Zhang, Yuehao Huang, Jiankun Dong, Tianhang Wang, Sunyao Zhou, Yunzi Wu, Chengnuo Sun, Yunfei Ge, Qizhen Weng, Chi Zhang, Chenjia Bai, Xuelong Li*  
  `2026-06-02` · `cs.RO` · [abs](https://arxiv.org/abs/2606.03682) · [pdf](https://arxiv.org/pdf/2606.03682.pdf)
  > 💡 构建GN-Matrix数据集与3DGS仿真平台，提出RL驱动基础模型BAE，统一地图式与地图-free视觉语言导航任务，超越SOTA。

  <details><summary>Abstract</summary>

  Embodied navigation connects intelligent agents with the physical world and is fundamental for general robotic intelligence. Limited availability and quality of navigation data have constrained Vision-and-Language Navigation (VLN) systems' generalization and long-horizon capabilities. To address this, we curate diverse 3D scenes and develop an automated pipeline for large-scale navigation data, resulting in the GN-Matrix dataset. Building on a 3D Gaussian Splatting (3DGS) engine, we introduce a high-fidelity simulation platform supporting interactive roaming and collision-aware navigation. We further propose GN-Bench, the first BEV-based benchmark incorporating dynamic 3DGS avatars for human-robot interaction evaluation. To leverage the simulator, we develop an RL-driven navigation foundation model, Break and Establish (BAE). After supervised learning, DAgger exposes the model to rollout-induced states, breaking narrow expert-centric distributions and enabling downstream RL exploration. This unified VLN paradigm integrates map-based and map-free tasks, including instruction following, human following, and goal navigation. GN-BAE formalizes high-fidelity 3DGS-rendered Bird's Eye View representations as compact memory, unlocking latent spatial reasoning in VLMs. Extensive evaluations on GN-Bench and VLN-CE show that GN0 outperforms state-of-the-art VLN methods. Overall, GN-Matrix offers a unified framework spanning data, simulation, and learning, advancing embodied navigation in research and industrial applications.

  </details>

- **[Characterizing Detectability in 3DGS Poisoning: A Stage-wise Benchmark](https://arxiv.org/abs/2606.03499)**  
  *Quoc-Anh Bui-Huynh, Thanh Duc Ngo, Xue Geng, Kaixin Xu, Wang Zhe, Xulei Yang, Ngai-Man Cheung*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03499) · [pdf](https://arxiv.org/pdf/2606.03499.pdf)
  > 💡 提出Poison-3DGS基准，系统分析3DGS投毒攻击在不同重建阶段的可检测性，发现检测效果高度依赖阶段信号。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has rapidly emerged as a leading representation for real-time novel view synthesis, but recent work shows it is vulnerable to diverse poisoning attacks, including illusory object injection, computation cost amplification, and post hoc model watermarking. Despite this expanding threat surface, existing studies focus mainly on attack success, while defense and detection remain underexplored. From a detection perspective, a key challenge and opportunity arise from the multi-stage nature of the 3DGS reconstruction pipeline, which produces heterogeneous intermediate representations. Forensic signals for detecting poisoning are inherently stage dependent: an attack introduced at one stage may produce signals that emerge only at later stages. This motivates a stage-wise view of detectability that goes beyond single-stage evaluation. We introduce Poison-3DGS, a benchmark for stage-wise characterization of poisoning detection in 3DGS. It exposes stage-specific artifacts, including multi-view images, geometry, training dynamics, and Gaussian parameters, across a diverse set of scenes and attacks. Using it, we conduct a systematic study of detectability across pipeline stages. Our analysis reveals several insights. First, detectability varies significantly across stages, and no single stage consistently dominates across attack types. Second, different attacks exhibit distinct stage-specific forensic signals, so detection effectiveness depends critically on where signals are observed. Third, later-stage signals such as training dynamics and Gaussian parameter statistics provide strong cues not observable at earlier stages. Overall, our work provides a principled benchmark and the first systematic characterization of stage-dependent detectability in 3DGS, offering a foundation for future research on robust and reliable 3DGS systems.

  </details>

- **[A Cookbook of 3D Vision: Data, Learning Paradigms, and Application](https://arxiv.org/abs/2606.04291)**  
  *Hongyang Du, Zongxia Li, Dawei Liu, Runhao Li, Haoyuan Song, Qingyu Zhang, Yubo Wang, Jingcheng Ni, Shihang Gui, Congchao Dong, Tao Hu*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.04291) · [pdf](https://arxiv.org/pdf/2606.04291.pdf)
  > 💡 提出3D视觉数据驱动分类法，系统梳理点云、3D高斯等表示与学习范式，整合重建、生成应用。

  <details><summary>Abstract</summary>

  3D vision has rapidly evolved, driven by increasingly diverse data representations, learning paradigms, and modeling strategies. Yet the field remains fragmented across representations and benchmarks, making it difficult to develop unified perspectives on efficiency, fidelity, and scalability. This work provides a data-centric taxonomy of 3D vision that connects geometric representations, datasets, learning frameworks, and applications within a single conceptual map. We begin by analysing the principal structural representations of 3D data--point clouds, meshes, voxels, and 3D Gaussians--along with their acquisition pipelines. We then examine how dataset design, benchmark construction, and supervision regimes shape recent advances, spanning 2D-supervised 3D learning, implicit neural representations, and 4D world modeling. Through this integrative lens, we clarify the relationships among representations, learning paradigms, and downstream tasks in reconstruction, generation, and video modeling, offering a consolidated view of emerging trends toward balancing efficiency and fidelity and toward multimodal geometric grounding.

  </details>

- **[Beyond Static Gaussians: An Empirical Investigation of Architectural Paradigms for Dynamic 3D Scene Reconstruction](https://arxiv.org/abs/2606.00452)**  
  *Adrian Ramlal, John S. Zelek*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00452) · [pdf](https://arxiv.org/pdf/2606.00452.pdf)
  > 💡 动态3DGS中结构引导方法重建质量高，高斯中心方法渲染更快但质量不稳，揭示了两者

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction via 3D Gaussian Splatting (3DGS) has emerged as a compelling approach for representing evolving environments, yet understanding trade-offs between methodologies remains crucial. This paper presents a comprehensive analysis of dynamic 3DGS methods, categorizing them into two paradigms: structure-guided methods employing auxiliary representations (deformation fields, canonical spaces, grids) to model temporal changes, and gaussian-centric methods encoding dynamics directly into primitives via continuous functions or 4D representations. We evaluate representative methods from both paradigms on the D-NeRF benchmark. Our findings reveal that structure-guided methods achieve superior reconstruction fidelity and compact model sizes, while gaussian-centric approaches demonstrate significantly higher rendering speeds enabling real-time performance, though with greater quality variability and potentially substantial storage overhead. This analysis highlights a fundamental trade-off between reconstruction quality/compactness versus rendering speed, providing insights to guide future research and application development in dynamic scene reconstruction.

  </details>

- **[Advances in Neural 3D Mesh Texturing: A Survey](https://arxiv.org/abs/2606.00137)**  
  *Sai Raj Kishore Perla, Hao Zhang, Ali Mahdavi-Amiri*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00137) · [pdf](https://arxiv.org/pdf/2606.00137.pdf)
  > 💡 综述了神经3D网格纹理化方法，从GAN到扩散模型，统一分类并分析架构、监督策略及未来挑战。

  <details><summary>Abstract</summary>

  Texturing 3D meshes plays a vital role in determining the visual realism of digital objects and scenes. Although recent generative 3D approaches based on Neural Radiance Fields and Gaussian Splatting can produce textured assets directly, polygonal meshes remain the core representation across modeling, animation, visual effects, and gaming pipelines. Neural 3D mesh texturing therefore continues to be an essential and active area of research. In this survey, we present a comprehensive review of recent advances in neural 3D mesh texturing, covering methods for texture synthesis, transfer, and completion. We first summarize key foundations in mesh geometry, texture mapping, differentiable rendering, and neural generative models, and then organize the literature into a unified taxonomy spanning early GAN-based methods to modern diffusion-based pipelines. We further analyze common architectures and supervision strategies, review datasets and evaluation protocols, and discuss emerging applications, practical/commercial systems, and open challenges. Together, these insights provide a structured perspective on the current landscape and help guide future developments in learning-based 3D mesh texturing.

  </details>

## 2026-06-01

- **[Smaller and Faster 3DGS via Post-Training Dictionary Learning](https://arxiv.org/abs/2605.30396)**  
  *Jiarong Gong, Jonas Unger, Ehsan Miandji*  
  `2026-05-28` · `cs.GR` · [abs](https://arxiv.org/abs/2605.30396) · [pdf](https://arxiv.org/pdf/2605.30396.pdf)
  > 💡 提出基于字典学习的后训练压缩框架，无需重训练，实现3.95倍压缩同时提升渲染速度约24%并保持图像质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a promising neural scene representation for real-time rendering, but trained models often suffer from large memory footprints, limiting deployment on less powerful devices. Existing compression techniques often lead to architectures with several additional trainable parameters. While achieving outstanding compression ratios, they introduce noticeable drops in image quality. In this work, we introduce the first dictionary-learning-based compression framework for 3DGS. The proposed post-training compression pipeline can be deployed in virtually any 3DGS model without the need for re-training or modifications to existing 3DGS models. Our compression framework is straightforward to implement, yet provides significant compression capabilities, preserves image quality, and improves real-time rendering performance. Across 13 benchmark scenes, our approach achieves an average compression ratio of 3.95x, 3.10x, and 4.55x when applied to 3DGS, 3DGS-MCMC, and PixelGS, respectively. This yields consistent rendering speedups of 23.3%, 24.3%, and 25.3%, while maintaining image quality.

  </details>

## 2026-05-30

- **[Learning Representations from 3D Gaussian Splats](https://arxiv.org/abs/2605.29549)**  
  *Julia Farganus, Krzysztof Żurawicki, Arkadiusz Gaweł, Weronika Jakubowska, Halina Kwaśnicka*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29549) · [pdf](https://arxiv.org/pdf/2605.29549.pdf)
  > 💡 评估点云和图模型对3D高斯场景分类的性能，揭示高斯属性对表示质量的影响。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a recent approach for scene rendering. Although primarily designed for view synthesis, its potential for scene understanding tasks remains underexplored. In this work, we conduct a comparative evaluation of various geometric deep learning architectures for the classification of 3D scenes represented using Gaussian Splatting. We benchmark point-based and graph-based models across both traditional point cloud datasets and dedicated Gaussian Splatting datasets. Scenes are embedded into latent representations, which are evaluated through end-to-end classification, linear probing, and clustering analysis. Our study provides insight into the suitability of different geometry-aware architectures and input feature configurations for learning effective 3D Gaussian Splat representations. The results highlight consistent differences between architectural families and reveal the impact of Gaussian-specific attributes on the quality of representation.

  </details>

- **[POINav: Benchmarking and Enhancing Final-Meters Arrival in Real-World Vision-Language Navigation](https://arxiv.org/abs/2605.28237)**  
  *Ruiyan Gong, Meisheng Zhang, Yuxiang Zhao, Mingchao Sun, Yanfen Shen, Zedong Chu, Zhining Gu, Wei Guo, Xiaolong Cheng, Qiming Li, Kangning Niu, Yanqing Zhu, Xiaolong Wu, Tianlun Li, Mu Xu*  
  `2026-05-27` · `cs.RO` · [abs](https://arxiv.org/abs/2605.28237) · [pdf](https://arxiv.org/pdf/2605.28237.pdf)
  > 💡 面对真实世界POI导航的“最后几米”挑战，提出基于3DGS重建的POINav-Bench基准和脑-动作框架，实现闭环评估与连续航点预测。

  <details><summary>Abstract</summary>

  Real-world navigation is fundamentally driven by Points of Interest (POIs), yet reaching a precise POI remains a critical "final-meters" challenge. Existing Vision-Language Navigation (VLN) benchmarks of POI-goal navigation often suffer from coarse granularity or significant sim-to-real gaps due to generated scene. To bridge this gap, we present POINav-Bench, the first benchmark designed for closed-loop evaluation of real-world POI-goal navigation. It comprises 11 commercial areas reconstructed from real-world captures using 3D Gaussian Splatting (3DGS), covering 126,398 $m^{2}$ in total and spanning 163 distinct POIs. With traversability-aware annotations and reference trajectories, POINav-Bench enables high-fidelity evaluation of navigation agents in realistic, POI-rich real-world environments. Building on this, we propose the POINav Brain-Action Framework where a Brain module performs POI-grounded reasoning to guide an Action module in predicting continuous waypoints for real-world execution. We further curate the POINav-Dataset, containing 70K real-world signage-entrance pairs. Experiments show that our framework provides a viable path toward refining real-world POI-goal navigation.

  </details>

- **[GScomp-QA: A Subjective Dataset for Quality Assessment of Compressed Gaussian Splatting](https://arxiv.org/abs/2605.26880)**  
  *Pedro Martin, António Rodrigues, João Ascenso, Maria Paula Queluz*  
  `2026-05-26` · `eess.IV` · [abs](https://arxiv.org/abs/2605.26880) · [pdf](https://arxiv.org/pdf/2605.26880.pdf)
  > 💡 针对Gaussian Splatting压缩缺乏感知评估，构建GScomp-QA主观数据集，含331视频覆盖9种压缩方案，提供基准与感知率失真分析。

  <details><summary>Abstract</summary>

  Gaussian Splatting (GS) has emerged as an efficient representation for high-quality 3D reconstruction and novel view synthesis. However, its large model size poses challenges for storage and transmission. While several GS compression solutions have been proposed, their perceptual impact remains poorly understood due to the lack of dedicated evaluation datasets. To address this gap, this paper introduces GScomp-QA, a subjective quality assessment dataset for evaluating synthesis quality from compressed GS models. The dataset comprises 331 video stimuli from 13 real-world scenes, covering 9 state-of-the-art GS compression solutions. By using videos synthesized from uncompressed models as reference, GScomp-QA isolates compression-induced distortions from synthesis artifacts. A subjective study with 20 participants was conducted, providing reliable perceptual scores. Based on these data, GS compression solutions are evaluated through perceptual rate-distortion analysis. In addition, 18 objective quality metrics are evaluated, showing that they do not fully capture GS-specific distortions. GScomp-QA will be publicly available and provide a benchmark for evaluating GS compression solutions and supporting the development of quality metrics tailored to GS compression.

  </details>

- **[DelowlightSplat: Feed-Forward Gaussian Splatting for Lowlight 3D Scene Reconstruction](https://arxiv.org/abs/2605.26629)**  
  *Fuzhen Jiang, Zengtian Xie, Zhuoran Li*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26629) · [pdf](https://arxiv.org/pdf/2605.26629.pdf)
  > 💡 针对弱光噪声与色偏导致前馈3DGS失败的问题，提出低光适配器增强匹配性，结合成本体积推理直接预测干净3D高斯，实现高质量重建。

  <details><summary>Abstract</summary>

  Novel-view synthesis and 3D reconstruction from sparse posed images are central to robotics and AR/VR. Yet, feed-forward 3D Gaussian reconstruction fails under lowlight due to noise, color shifts, and unreliable correspondence. We propose DelowlightSplat, a lowlight-aware feed-forward Gaussian splatting framework for clean novel-view rendering. We build a controllable multi-view lowlight benchmark by degrading only context views while keeping target views clean. We introduce a lightweight Lowlight Adapter for residual enhancement to improve matchability, and couple it with cost-volume-based multi-view inference to directly predict clean 3D Gaussians. Experiments show that DelowlightSplat significantly outperforms previous feed-forward method and two-stage pipeline under lowlight conditions.

  </details>

- **[Underwater360: Reconstructing Underwater Scenes from Panoramic Images with Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2605.26447)**  
  *Jiangbei Hu, Weichao Song, Shibo Yu, Mohan Wang, Zihan Yi, Rui Wu, Mingkang Xiang, Na Lei, Shengfa Wang, Zhongxuan Luo, Ying He*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26447) · [pdf](https://arxiv.org/pdf/2605.26447.pdf)
  > 💡 用物理感知的全向3DGS直接球面光线投射和介质建模，恢复水下场景并提升渲染质量与一致性。

  <details><summary>Abstract</summary>

  Underwater scene reconstruction is essential for immersive exploration of aquatic environments, yet remains challenging due to complex participating-media effects such as absorption and scattering, as well as the limited field of view (FoV) of conventional cameras. Although combining panoramic imaging with 3D Gaussian Splatting (3DGS) offers a promising direction for photorealistic underwater rendering, traditional 3DGS struggles with both spherical projection distortion and underwater medium degradation. In this paper, we propose \textbf{Underwater360}, a physics-informed omnidirectional 3DGS framework for underwater panoramic scene reconstruction. First, we introduce an Omnidirectional Gaussian Splatting module that performs ray casting directly in spherical camera space instead of relying on 2D projection approximations, thereby reducing geometric distortions under 360$^\circ$ FoV. Second, we design a physics-based appearance-medium modeling architecture with pose-conditioned appearance embeddings to explicitly decouple intrinsic scene radiance from depth-dependent backscatter and attenuation, enabling physically grounded scene appearance restoration. Finally, we establish a new panoramic underwater benchmark dataset containing both synthetic and real-world scenes. Extensive experiments demonstrate that Underwater360 achieves superior performance in underwater novel view synthesis and scene appearance restoration, delivering improved rendering quality and cross-view consistency in complex underwater environments. The code and datasets are released at https://github.com/SwcK423/Underwater360

  </details>

- **[SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation](https://arxiv.org/abs/2605.22536)**  
  *Xiaolong Zhou, Yifei Liu, Ziyang Gong, Jiarui Li, Qiyue Zhao, Muyao Niu, Yuanyuan Gao, Le Ma, Xue Yang, Hongjie Zhang, Zhihang Zhong*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22536) · [pdf](https://arxiv.org/pdf/2605.22536.pdf)
  > 💡 提出空间智能对九种视觉退化的鲁棒性基准SpaceDG，利用3DGS渲染合成退化场景，揭示多模态大模型在退化条件下空间推理能力显著下降。

  <details><summary>Abstract</summary>

  Multimodal Large Language Models (MLLMs) have made rapid progress in spatial intelligence, yet existing spatial reasoning benchmarks largely assume pristine visual inputs and overlook the degradations that commonly occur in real-world deployment, such as motion blur, low light, adverse weather, lens distortion, and compression artifacts. This raises a fundamental question: how robust is the spatial intelligence of current MLLMs when visual observations are imperfect? To answer this question, we introduce SpaceDG, the first large-scale dataset for degradation-aware spatial understanding. It is constructed with a physically grounded degradation synthesis engine that embeds degradation formation process into 3D Gaussian Splatting (3DGS) rendering, enabling realistic simulation of nine degradation types. The resulting dataset contains approximately 1M QA pairs from nearly 1,000 indoor scenes. We further introduce SpaceDG-Bench, an human-verified benchmark with 1,102 questions spanning 11 reasoning categories and 9 visual degradation types, yielding over 10K VQA instances. Evaluating 25 open- and closed-source MLLMs reveals that visual degradations consistently and substantially impair spatial reasoning, exposing a critical robustness gap. Finally, we show that finetuning on SpaceDG markedly improves degradation robustness and can even surpass human performance under degraded conditions without any performance drop on clean images, highlighting the promise of degradation-aware training for robust spatial intelligence.

  </details>

- **[RCGDet3D: Rethinking 4D Radar-Camera Fusion-based 3D Object Detection with Enhanced Radar Feature Encoding](https://arxiv.org/abs/2605.21112)**  
  *Weiyi Xiong, Bing Zhu*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.21112) · [pdf](https://arxiv.org/pdf/2605.21112.pdf)
  > 💡 4D雷达-相机融合检测速度慢，通过增强雷达特征编码（R-PGE和语义注入）简化融合，RCGDet3D实现精度与速度双领先。

  <details><summary>Abstract</summary>

  4D automotive radar is indispensable for autonomous driving due to its low cost and robustness, yet its point cloud sparsity challenges 3D object detection. Existing 4D radar-camera fusion methods focus on complex fusion strategies, trading inference speed for marginal gains. This trade-off hinders real-time deployment due to heavy computation on dense feature maps. In contrast, feature extraction from sparse radar points is less time-consuming but remains under-explored. This work uncovers that simply enhancing radar feature extraction can achieve comparable or even higher performance than elaborate fusion modules, while maintaining real-time performance. Based on this finding, we propose RCGDet3D, which centers on radar feature encoding and simplifies multi-modal fusion. Its encoder inherits from the efficient Gaussian Splatting-based Point Gaussian Encoder (PGE) in RadarGaussianDet3D with two key improvements. First, the Ray-centric PGE (R-PGE) predicts Gaussian attributes in ray-aligned coordinate systems before unifying them to Bird's-Eye View (BEV) space, significantly improving geometric consistency and reducing learning difficulty by decoupling the coordinate transformation from representation learning. Second, a Semantic Injection (SI) module incorporates visual cues from images, producing more geometrically accurate and semantically enriched radar features. Experiments on View-of-Delft (VoD) and TJ4DRadSet show that RCGDet3D outperforms state-of-the-art methods in both accuracy and speed, setting a new benchmark for real-time deployment.

  </details>

- **[ArtMesh: Part-Aware Articulated Mesh Fields with Motion-Consistent Dynamics](https://arxiv.org/abs/2605.16582)**  
  *Sylvia Yuan, Dan Wang, Ravi Ramamoorthi, Xinrui Cui*  
  `2026-05-15` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16582) · [pdf](https://arxiv.org/pdf/2605.16582.pdf)
  > 💡 针对3DGS缺乏表面拓扑问题，提出基于网格的关节重建，用部分感知重网格和双向运动一致性，在关节参数估计和几何重建上超越现有方法。

  <details><summary>Abstract</summary>

  We present ArtMesh, a mesh-native method for reconstructing articulated objects explicitly as connected triangle meshes with per-part rigid motion from multi-view images in start and end states. Existing 3D Gaussian Splatting pipelines for articulated reconstruction inherit the unstructured point-based geometry of their splatting base, which provides no surface topology for reasoning about part boundaries or enforcing motion consistency along the object's connectivity. ArtMesh instead builds on a mesh-based differentiable rendering backbone, enabling part-aware dynamics to act directly on the structured topology. To make the topology compatible with articulation, we introduce part-aware restricted Delaunay remeshing, producing connected submeshes whose triangles do not cross semantic part boundaries. The dynamic mesh field then optimizes articulation using bidirectional Vertex-wise Motion Consistency on transported mesh vertices and Pixel-wise Motion Consistency on rendered RGB-D observations. We introduce Articulate-100, a new benchmark of 100 articulated objects spanning 16 PartNet-Mobility categories. On this benchmark, ArtMesh outperforms prior 3DGS-based pipelines in joint parameter estimation and part-level geometric reconstruction, with the largest gains on objects with many movable parts.

  </details>

- **[3DEditSafe: Defending 3D Editing Pipelines from Unsafe Generation](https://arxiv.org/abs/2605.15398)**  
  *Nicole Meng, Zheyuan Liu, Meng Jiang, Yingjie Lao*  
  `2026-05-14` · `cs.GR` · [abs](https://arxiv.org/abs/2605.15398) · [pdf](https://arxiv.org/pdf/2605.15398.pdf)
  > 💡 针对3DGS编辑中不安全NSFW内容传播，提出安全正则化与语义投影的3DEditSafe框架，首次防御3D编辑不安全生成。

  <details><summary>Abstract</summary>

  Recent advances in 3D generative editing, particularly pipelines based on 3D Gaussian Splatting (3DGS), have achieved high-fidelity, multi-view-consistent scene manipulation from text prompts. However, we find that these pipelines also introduce new safety risks when unsafe prompts produce edits that are propagated and optimized across views. In this work, we study unsafe generation in 3D editing pipelines and show that such behavior can lead to coherent, undesirable Not-Safe-For-Work (NSFW) content in the final 3D representation. To address this, we propose 3DEditSafe, a safety-regularized 3D editing framework that constrains unsafe semantic propagation during optimization. 3DEditSafe combines generation-stage safety guidance with rendered-view 3D safety regularization, safe semantic projection, residue suppression, and mask-aware preservation to steer optimization away from unsafe editing directions. We evaluate our approach on EditSplat scenes using an object-compatible unsafe prompt benchmark and show that 2D safety guidance alone is not consistently sufficient to prevent unsafe 3D edits. 3DEditSafe reduces unsafe semantic alignment and view-level attack success rates, while revealing a safety-quality tradeoff in which stronger unsafe suppression can introduce artifacts or reduce unsafe-prompt fidelity. To our knowledge, this work is the first attempt to study and defend against unsafe generation in text-driven 3D editing pipelines, highlighting the need for safety mechanisms that operate directly on optimized 3D representations.

  </details>

- **[Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880)**  
  *Qingyuan Zhou, Xinyi Liu, Weidong Yang, Ning Wang, Shuquan Ye, Ben Fei, Ying He, Wanli Ouyang*  
  `2026-05-14` · `cs.CV` · [abs](https://arxiv.org/abs/2605.14880) · [pdf](https://arxiv.org/pdf/2605.14880.pdf)
  > 💡 针对3DGS中噪声原语问题，提出空间感知去噪框架，联合位置与空间结构优化，提升新视图合成质量与紧凑性。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable success in high-fidelity Novel View Synthesis (NVS), yet the optimization process inevitably introduces noisy Gaussian primitives due to the sparse and incomplete initialization from Structure-from-Motion (SfM) point clouds. Most existing methods focus solely on adjusting the positions of primitives during optimization, while neglecting the underlying spatial structure. To this end, we introduce a new perspective by formulating the optimization of 3DGS as a primitive denoising process and propose Denoising-GS, a spatial-aware denoising framework for Gaussian primitives by taking both the positions and spatial structure into consideration. Specifically, we design an optimizer that preserves the spatial optimization flow of primitives, facilitating coherent and directed denoising rather than random perturbations. Building upon this, the Spatial Gradient-based Denoising strategy jointly considers the spatial supports of primitives to ensure gradient-consistent updates. Furthermore, the Uncertainty-based Denoising module estimates primitive-wise uncertainty to prune redundant or noisy primitives, while the Spatial Coherence Refinement strategy selectively splits primitives in sparse regions to maintain structural completeness. Experiments conducted on three benchmark datasets demonstrate that Denoising-GS consistently enhances NVS fidelity while maintaining representation compactness, achieving state-of-the-art performance across all benchmarks. Source code and models will be made publicly available.

  </details>

- **[FFAvatar: Few-Shot, Feed-Forward, and Generalizable Avatar Reconstruction](https://arxiv.org/abs/2605.15320)**  
  *Thuan Hoang Nguyen, Jiahao Luo, Yinyu Nie, Hao Li, Gordon Guocheng Qian, Jian Wang*  
  `2026-05-14` · `cs.GR` · [abs](https://arxiv.org/abs/2605.15320) · [pdf](https://arxiv.org/pdf/2605.15320.pdf)
  > 💡 FFAvatar利用多视图

  <details><summary>Abstract</summary>

  Avatar reconstruction has traditionally relied on per-subject optimization that requires hours of computation or on expensive preprocessing that limits scalability. We introduce FFAvatar, a generalizable feed-forward framework that reconstructs high-quality, animatable 3D Gaussian head avatars from few-shot unposed portrait images in seconds. FFAvatar fuses information from multiple source images into a unified canonical Gaussian representation through Multi-View Query-Former, which is animated via FLAME parameters predicted end-to-end directly from pixels, eliminating the overhead of offline FLAME extraction. We further propose a three-stage training curriculum that achieves both broad generalization and high-fidelity reconstruction: (i) scalable pretraining on extensive monocular video data with over 1M identities to learn strong generalizable priors; (ii) multi-view fine-tuning on a small but high-quality dataset of 360-degree captures to enhance geometric fidelity and extreme-view awareness; and (iii) optional personalization that adapts to specific identities for maximum fidelity within 500 optimization steps. Extensive experiments demonstrate that FFAvatar sets a new standard for identity preservation, geometric consistency, and animation fidelity. On the NeRSemble benchmark, it outperforms the state-of-the-art LAM by a substantial 5.5 PSNR gain. Furthermore, FFAvatar enables real-time deployment, reconstructing avatars in 2 seconds without personalization and 10 seconds with personalization, while supporting 49 FPS animation on a single NVIDIA A100 GPU.

  </details>

- **[RoSplat: Robust Feed-Forward Pixel-wise Gaussian Splatting for Varying Input Views and High-Resolution Rendering](https://arxiv.org/abs/2605.13093)**  
  *Hoang Chuong Nguyen, Renjie Wu, Jose M. Alvarez, Miaomiao Liu*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13093) · [pdf](https://arxiv.org/pdf/2605.13093.pdf)
  > 💡 提出alpha归一化和3D采样正则化，解决变输入视图过亮与高分辨率渲染空洞问题，提升前馈高斯泼溅鲁棒性。

  <details><summary>Abstract</summary>

  Generalizable 3D Gaussian Splatting has recently emerged as an efficient approach for novel-view synthesis, enabling feed-forward synthesis from only a few input views. However, existing pixel-wise feed-forward methods suffer from over-bright renderings when the number of input views varies during inference, as well as insufficient supervision for accurate Gaussian scale estimation, which leads to hole artifacts, particularly in high-resolution renderings. To address these issues, we identify that the over-brightness is caused by the varying number of overlapping Gaussians and propose a simple alpha normalization strategy to maintain brightness consistency across different number of input views. In addition, we introduce an auxiliary 3D sampling-based regularizer to improve Gaussian scale estimation, thereby mitigating hole artifacts in high-resolution rendering. Experiments on benchmark datasets demonstrate that our method significantly improves baseline models under varying input-view and high-resolution rendering settings.

  </details>

- **[3D Gaussian Splatting for Efficient Retrospective Dynamic Scene Novel View Synthesis with a Standardized Benchmark](https://arxiv.org/abs/2605.12437)**  
  *Yunxiao Zhang, Suryansh Kumar*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12437) · [pdf](https://arxiv.org/pdf/2605.12437.pdf)
  > 💡 针对同步多视角动态场景，提出无需时间变形约束的3DGS方法，并构建标准化基准实现高效回顾性新视图合成。

  <details><summary>Abstract</summary>

  Retrospective novel view synthesis (NVS) of dynamic scenes is fundamental to applications such as sports. Recent dynamic 3D Gaussian Splatting (3DGS) approaches introduce temporally coupled formulations to enforce motion coherence across time. In this paper, we argue that, in a synchronized multi-view (MV) setting typical of sports, the dynamic scene at each time step is already strongly geometrically constrained. We posit that the availability of calibrated, synchronized viewpoints provides sufficient spatial consistency, and therefore, explicit temporal coupling, or complex multi-body constraints seems unnecessary for retrospective NVS. To this end, we propose an approach tailored for synchronized MV dynamic scene. By initializing the SfM-derived point cloud at the start time and propagating optimized Gaussians over time, we show that efficient retrospective NVS can be achieved without imposing a temporal deformation constraint. Complementing our methodological contribution, we introduce a Dynamic MV dataset framework built on Blender for reproducible NeRF and 3DGS research. The framework generates high-quality, synchronized camera rigs and exports training-ready datasets in standard formats, eliminating inconsistencies in coordinate conventions and data pipelines. Using the framework, we construct a dynamic benchmark suite and evaluate representative NeRF and 3DGS approaches under controlled conditions. Together, we show that, under a synchronized MV setup, efficient retrospective dynamic scene NVS can be achieved using 3DGS. At the same time, the dataset-generation framework enables reproducible and principled benchmarking of dynamic NVS methods.

  </details>

- **[PD-4DGS:Progressive Decomposition of 4D Gaussian Splatting for Bandwidth-Adaptive Dynamic Scene Streaming](https://arxiv.org/abs/2605.11427)**  
  *Jiachen Li, Guangzhi Han, Jin Wan, Delong Han, Yuan Gao, Min Li, Mingle Zhou, Gang Li*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11427) · [pdf](https://arxiv.org/pdf/2605.11427.pdf)
  > 💡 针对4DGS全量下载延迟问题，提出渐进式分解带宽自适应流媒体方法，层次化变形分解与率失真损失降低首帧延迟至1.7秒。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting (4DGS) enables high-quality dynamic novel view synthesis, yet current models remain monolithic bitstreams that clients must download in full before any frame can be rendered, causing black-screen waits of tens to hundreds of seconds on mobile bandwidth and leaving 4DGS incompatible with modern adaptive-bitrate delivery. Progressive 3DGS compression alleviates this for static scenes, but it acts only on spatial anchors and cannot partition the temporal deformation networks that dominate dynamic-scene size. We present PD-4DGS, the first framework for progressive compression and on-demand transmission of 4DGS. Hierarchical Deformation Decomposition (HDD) externalises the coarse-to-fine motion hierarchy already latent in 4DGS into three independently transmittable layers -- a static scaffold, a global deformation, and a local refinement -- so that any prefix of the bitstream is already renderable, turning a single training run into a scalable, DASH/HLS-compatible bitstream. A Gaussian-entropy attribute rate-distortion loss together with a temporal mask consistency regulariser shrink the base layer while suppressing low-bitrate flicker; a capacity-weighted rollout schedule, gated online by a learnt activation rate rho, then prevents deformation-network under-training without any per-scene hyperparameter. On the Dycheck iPhone benchmark, PD-4DGS cuts the streamed bitstream by >60% at matched rendering fidelity and reduces first-frame latency from 73--930 s to ~1.7 s on a 2 Mbps link, uniquely enabling true on-demand progressive streaming for 4DGS.

  </details>

- **[MAGS-SLAM: Monocular Multi-Agent Gaussian Splatting SLAM for Geometrically and Photometrically Consistent Reconstruction](https://arxiv.org/abs/2605.10760)**  
  *Zhihao Cao, Qi Shao, Shuhao Zhai, Jing Zhang, Anh Nguyen, Baoru Huang*  
  `2026-05-11` · `cs.RO` · [abs](https://arxiv.org/abs/2605.10760) · [pdf](https://arxiv.org/pdf/2605.10760.pdf)
  > 💡 针对多智能体SLAM依赖

  <details><summary>Abstract</summary>

  Collaborative photorealistic 3D reconstruction from multiple agents enables rapid large-scale scene capture for virtual production and cooperative multi-robot exploration. While recent 3D Gaussian Splatting (3DGS) SLAM algorithms can generate high-fidelity real-time mapping, most of the existing multi-agent Gaussian SLAM methods still rely on RGB-D sensors to obtain metric depth and simplify cross-agent alignment, which limits the deployment on lightweight, low-cost, or power-constrained robotic platforms. To address this challenge, we propose MAGS-SLAM, the first RGB-only multi-agent 3DGS SLAM framework for collaborative scene reconstruction. Each agent independently builds local monocular Gaussian submaps and transmits compact submap summaries rather than raw observations or dense maps. To facilitate robust collaboration in the presence of monocular scale ambiguity, our framework integrates compact submap communication, geometry- and appearance-aware loop verification, and occupancy-aware Gaussian fusion, enabling coherent global reconstruction without active depth sensors. We further introduce ReplicaMultiagent Plus benchmark for evaluating collaborative Gaussian SLAM. Intensive experiments on synthetic and real-world datasets show that MAGS-SLAM achieves competitive tracking accuracy and comparable or superior rendering quality to state-of-the-art RGB-D collaborative Gaussian SLAM methods while relying only RGB images.

  </details>

- **[VEGA: Visual Encoder Grounding Alignment for Spatially-Aware Vision-Language-Action Models](https://arxiv.org/abs/2605.10485)**  
  *Hao Wang, Xiaobao Wei, Jingyang He, Chengyu Bai, Chun-Kai Fan, Jiajun Cao, Jintao Chen, Ying Li, Shanyu Rong, Ming Lu, Xiaozhu Ju, Jian Tang, Shanghang Zhang*  
  `2026-05-11` · `cs.RO` · [abs](https://arxiv.org/abs/2605.10485) · [pdf](https://arxiv.org/pdf/2605.10485.pdf)
  > 💡 VLA模型缺乏空间感知，VEGA通过对齐视觉编码器输出与3DGS微调的DINOv2-FiT3D，提升空间推理且无额外开销。

  <details><summary>Abstract</summary>

  Precise spatial reasoning is fundamental to robotic manipulation, yet the visual backbones of current vision-language-action (VLA) models are predominantly pretrained on 2D image data without explicit 3D geometric supervision, resulting in representations that lack accurate spatial awareness. Existing implicit spatial grounding methods partially address this by aligning VLA features with those of 3D-aware foundation models, but they rely on empirical layer search and perform alignment on LLM-level visual tokens where spatial structure has already been entangled with linguistic semantics, limiting both generalizability and geometric interpretability. We propose VEGA (Visual Encoder Grounding Alignment), a simple yet effective framework that directly aligns the output of the VLA's visual encoder with spatially-aware features from DINOv2-FiT3D, a DINOv2 model fine-tuned with multi-view consistent 3D Gaussian Splatting supervision. By performing alignment at the visual encoder output level, VEGA grounds spatial awareness before any linguistic entanglement occurs, offering a more interpretable and principled alignment target. The alignment is implemented via a lightweight projector trained with a cosine similarity loss alongside the standard action prediction objective, and is discarded at inference time, introducing no additional computational overhead. Extensive experiments on simulation benchmark and real-world manipulation tasks demonstrate that VEGA consistently outperforms existing implicit spatial grounding baselines, establishing a new state-of-the-art among implicit spatial grounding methods for VLA models.

  </details>

- **[Aes3D: Aesthetic Assessment in 3D Gaussian Splatting](https://arxiv.org/abs/2605.05155)**  
  *Chuanzhi Xu, Boyu Wei, Haoxian Zhou, Xuanhua Yin, Zihan Deng, Haodong Chen, Qiang Qu, Weidong Cai*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.05155) · [pdf](https://arxiv.org/pdf/2605.05155.pdf)
  > 💡 针对3DGS场景缺乏美学评估，提出首个数据集Aesthetic3D和轻量模型Aes3DGSNet，直接预测场景美学分数。

  <details><summary>Abstract</summary>

  As 3D Gaussian Splatting (3DGS) gains attention in immersive media and digital content creation, assessing the aesthetics of 3D scenes becomes important in helping creators build more visually compelling 3D content. However, existing evaluation methods for 3D scenes primarily emphasize reconstruction fidelity and perceptual realism, largely overlooking higher-level aesthetic attributes such as composition, harmony, and visual appeal. This limitation comes from two key challenges: (1) the absence of general 3DGS datasets with aesthetic annotations, and (2) the intrinsic nature of 3DGS as a low-level primitive representation, which makes it difficult to capture high-level aesthetic features. To address these challenges, we propose Aes3D, the first systematic framework for assessing the aesthetics of 3D neural rendering scenes. Aes3D includes Aesthetic3D, the first dataset dedicated to 3D scene aesthetic assessment, built on our proposed annotation strategy for 3D scene aesthetics. In addition, we present Aes3DGSNet, a lightweight model that directly predicts scene-level aesthetic scores from 3DGS representations. Notably, our model operates solely on 3D Gaussian primitives, eliminating the need for rendering multi-view images and thus reducing computational cost and hardware requirements. Through aesthetics-supervised learning on multi-view 3DGS scene representations, Aes3DGSNet effectively captures high-level aesthetic cues and accurately regresses aesthetic scores. Experimental results demonstrate that our approach achieves strong performance while maintaining a lightweight design, establishing a new benchmark for 3D scene aesthetic assessment. Code and datasets will be made available in a future version.

  </details>

- **[SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion](https://arxiv.org/abs/2605.01466)**  
  *Zhaoyang Li, Zhichao You, Tianrui Li*  
  `2026-05-02` · `cs.CV` · [abs](https://arxiv.org/abs/2605.01466) · [pdf](https://arxiv.org/pdf/2605.01466.pdf)
  > 💡 点云补全中硬投影导致跨模态熵崩溃，提出可微高斯泼溅与注意力框架实现密集连续表示，达SOTA并增强视觉依赖。

  <details><summary>Abstract</summary>

  Although multi-modal learning has advanced point cloud completion, the theoretical mechanisms remain unclear. Recent works attribute success to the connection between modalities, yet we identify that standard hard projection severs this connection: projecting a sparse point cloud onto the image plane yields an extremely sparse support, which hinders visual prior propagation, a failure mode we term Cross-Modal Entropy Collapse. To address this practical limitation, we propose SplAttN, which replaces hard projection with Differentiable Gaussian Splatting to produce a dense, continuous image-plane representation. By reformulating projection as continuous density estimation, SplAttN avoids collapsed sparse support, facilitates gradient flow, and improves cross-modal connection learnability. Extensive experiments show that SplAttN achieves state-of-the-art performance on PCN and ShapeNet-55/34. Crucially, we utilize the real-world KITTI benchmark as a stress test for multi-modal reliance. Counter-factual evaluation reveals that while baselines degenerate into unimodal template retrievers insensitive to visual removal, SplAttN maintains a robust dependency on visual cues, validating that our method establishes an effective cross-modal connection. Code is available at https://github.com/zay002/SplAttN.

  </details>

- **[Fake3DGS: A Benchmark for 3D Manipulation Detection in Neural Rendering](https://arxiv.org/abs/2604.27590)**  
  *Davide Di Nucci, Riccardo Catalini, Guido Borghi, Roberto Vezzani*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.27590) · [pdf](https://arxiv.org/pdf/2604.27590.pdf)
  > 💡 为3D高斯泼溅提出伪造检测基准与多视图一致性特征方法，显著提升识别能力。

  <details><summary>Abstract</summary>

  Recent advances in 3D reconstruction and neural rendering,particularly 3D Gaussian Splatting, make it feasible and simple to edit 3D scenes and re-render them as highly realistic images. Therefore, security concerns arise regarding the authenticity of 3D content. Despite this threat, 3D fake detection remains largely unexplored in the literature, and most existing work is limited to 2D space. Therefore, in this paper, we formalize the concept of 3D fake detection and introduce Fake3DGS, a dataset of 3D Gaussian splatting scenes and corresponding rendered views, where fake images are produced by controlled manipulations of geometry, appearance, and spatial layout, while preserving high visual realism. Using this benchmark, we demonstrate that current state-of-the-art 2D detectors struggle to distinguish between original and 3D manipulated images. To bridge this gap, we introduce a 3D-aware detection method that leverages multi-view coherence and features derived from the Gaussian splatting representation. Experimental results demonstrate a substantial improvement in recognizing modified 3D content, underscoring the validity of the new dataset and the necessity for authenticity assessment techniques that extend beyond 2D evidence. Code and data are publicly released for future investigations.

  </details>

- **[Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193)**  
  *Vinayak Gupta, Chih-Hao Lin, Shenlong Wang, Anand Bhattad, Jia-Bin Huang*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.28193) · [pdf](https://arxiv.org/pdf/2604.28193.pdf)
  > 💡 提出GenWildSplat，用前馈框架从稀疏无约束图像预测深度、相机参数和3D高斯，结合外观适配与语义分割实现泛化实时重建。

  <details><summary>Abstract</summary>

  Reconstructing 3D scenes from sparse, unposed images remains challenging under real-world conditions with varying illumination and transient occlusions. Existing methods rely on scene-specific optimization using appearance embeddings or dynamic masks, which requires extensive per-scene training and fails under sparse views. Moreover, evaluations on limited scenes raise questions about generalization. We present GenWildSplat, a feed-forward framework for sparse-view outdoor reconstruction that requires no per-scene optimization. Given unposed internet images, GenWildSplat predicts depth, camera parameters, and 3D Gaussians in a canonical space using learned geometric priors. An appearance adapter modulates appearance for target lighting conditions, while semantic segmentation handles transient objects. Through curriculum learning on synthetic and real data, GenWildSplat generalizes across diverse illumination and occlusion patterns. Evaluations on PhotoTourism and MegaScenes benchmark demonstrate state-of-the-art feed-forward rendering quality, achieving real-time inference without test-time optimization

  </details>

- **[FreeOcc: Training-Free Embodied Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2604.28115)**  
  *Zeyu Jiang, Changqing Zhou, Xingxing Zuo, Changhao Chen*  
  `2026-04-30` · `cs.RO` · [abs](https://arxiv.org/abs/2604.28115) · [pdf](https://arxiv.org/pdf/2604.28115.pdf)
  > 💡 针对占据预测依赖3D标注和泛化差的问题，FreeOcc无需训练，结合SLAM、高斯图和视觉语言模型实现开放词汇预测，性能提升2倍以上。

  <details><summary>Abstract</summary>

  Existing learning-based occupancy prediction methods rely on large-scale 3D annotations and generalize poorly across environments. We present FreeOcc, a training-free framework for open-vocabulary occupancy prediction from monocular or RGB-D sequences. Unlike prior approaches that require voxel-level supervision and ground-truth camera poses, FreeOcc operates without 3D annotations, pose ground truth, or any learning stage. FreeOcc incrementally builds a globally consistent occupancy map via a four-layer pipeline: a SLAM backbone estimates poses and sparse geometry; a geometrically consistent Gaussian update constructs dense 3D Gaussian maps; open-vocabulary semantics from off-the-shelf vision-language models are associated with Gaussian primitives; and a probabilistic Gaussian-to-occupancy projection produces dense voxel occupancy. Despite being entirely training-free and pose-agnostic, FreeOcc achieves over $2\times$ improvements in IoU and mIoU on EmbodiedOcc-ScanNet compared to prior self-supervised methods. We further introduce ReplicaOcc, a benchmark for indoor open-vocabulary occupancy prediction, and show that FreeOcc transfers zero-shot to novel environments, substantially outperforming both supervised and self-supervised baselines. Project page: https://the-masses.github.io/freeocc-web/.

  </details>

- **[Generalizable Human Gaussian Splatting via Multi-view Semantic Consistency](https://arxiv.org/abs/2604.25466)**  
  *Jingi Kim, Wonjun Kim*  
  `2026-04-28` · `cs.CV` · [abs](https://arxiv.org/abs/2604.25466) · [pdf](https://arxiv.org/pdf/2604.25466.pdf)
  > 💡 通过跨视图注意力校准多视图潜在特征，解决人体高斯溅射中特征不一致问题，提升稀疏视图渲染质量。

  <details><summary>Abstract</summary>

  Recently, generalizable human Gaussian splatting from sparse-view inputs has been actively studied for the photorealistic human rendering. Most existing methods rely on explicit geometric constraints or predefined structural representations to accurately position 3D Gaussians. Although these approaches have shown the remarkable progress in this field, they still suffer from inconsistent feature representations across multi-view inputs due to complex articulations of the human body and limited overlaps between different views. To address this problem, we propose a novel method to accurately localize 3D Gaussians and ultimately improve the quality of human rendering. The key idea is to unproject latent embeddings encoded from each viewpoint into a shared 3D space through predicted depth maps and recalibrate them belonging to the same body part based on cross-view attention. This helps the model resolve the spatial ambiguity occurring in highly textured regions as well as occluded body parts, thus leading to the accurate localization of 3D Gaussians. Experimental results on benchmark datasets show that the proposed method efficiently improves the performance of generalizable human Gaussian splatting from sparse-view inputs.

  </details>

- **[Spatiotemporal Degradation-Aware 3D Gaussian Splatting for Realistic Underwater Scene Reconstruction](https://arxiv.org/abs/2604.23551)**  
  *Shaohua Liu, Ning Gao, Zuoya Gu, Hongkun Dou, Yue Deng, Hongjue Li*  
  `2026-04-26` · `cs.CV` · [abs](https://arxiv.org/abs/2604.23551) · [pdf](https://arxiv.org/pdf/2604.23551.pdf)
  > 💡 针对水下视频中的时空退化，提出MarineSTD-GS框架，利用成对高斯原语和时空退化建模实现自监督解耦，重建高质量场景。

  <details><summary>Abstract</summary>

  Reconstructing realistic underwater scenes from underwater video remains a meaningful yet challenging task in the multimedia domain. The inherent spatiotemporal degradations in underwater imaging, including caustics, flickering, attenuation, and backscattering, frequently result in inaccurate geometry and appearance in existing 3D reconstruction methods. While a few recent works have explored underwater degradation-aware reconstruction, they often address either spatial or temporal degradation alone, falling short in more real-world underwater scenarios where both types of degradation occur. We propose MarineSTD-GS, a novel 3D Gaussian Splatting-based framework that explicitly models both temporal and spatial degradations for realistic underwater scene reconstruction. Specifically, we introduce two paired Gaussian primitives: Intrinsic Gaussians represent the true scene, while Degraded Gaussians render the degraded observations. The color of each Degraded Gaussian is physically derived from its paired Intrinsic Gaussian via a Spatiotemporal Degradation Modeling (SDM) module, enabling self-supervised disentanglement of realistic appearance from degraded images. To ensure stable training and accurate geometry, we further propose a Depth-Guided Geometry Loss and a Multi-Stage Optimization strategy. We also construct a simulated benchmark with diverse spatial and temporal degradations and ground-truth appearances for comprehensive evaluation. Experiments on both simulated and real-world datasets show that MarineSTD-GS robustly handles spatiotemporal degradations and outperforms existing methods in novel view synthesis with realistic, water-free scene appearances.

  </details>

- **[BALTIC: A Benchmark and Cross-Domain Strategy for 3D Reconstruction Across Air and Underwater Domains Under Varying Illumination](https://arxiv.org/abs/2604.19133)**  
  *Michele Grimaldi, David Nakath, Oscar Pizarro, Jonatan Scharff Willners, Ignacio Carlucho, Yvan R. Petillot*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.19133) · [pdf](https://arxiv.org/pdf/2604.19133.pdf)
  > 💡 提出空气-水下跨域3D重建基准BALTIC，评估光照变化，发现3DGS经白平衡预处理可媲美专用方法。

  <details><summary>Abstract</summary>

  Robust 3D reconstruction across varying environmental conditions remains a critical challenge for robotic perception, particularly when transitioning between air and water. To address this, we introduce BALTIC, a controlled benchmark designed to systematically evaluate modern 3D reconstruction methods under variations in medium and lighting. The benchmark comprises 13 datasets spanning two media (air and water) and three lighting conditions (ambient, artificial, and mixed), with additional variations in motion type, scanning pattern, and initialization trajectory, resulting in a diverse set of sequences. Our experimental setup features a custom water tank equipped with a monocular camera and an HTC Vive tracker, enabling accurate ground-truth pose estimation. We further investigate cross-domain reconstruction by augmenting underwater image sequences with a small number of in-air views captured under similar lighting conditions. We evaluate Structure-from-Motion reconstruction using COLMAP in terms of both trajectory accuracy and scene geometry, and use these reconstructions as input to Neural Radiance Fields and 3D Gaussian Splatting methods. The resulting models are assessed against ground-truth trajectories and in-air references, while rendered outputs are compared using perceptual and photometric metrics. Additionally, we perform a color restoration analysis to evaluate radiometric consistency across domains. Our results show that under controlled, texture-consistent conditions, Gaussian Splatting with simple preprocessing (e.g., white balance correction) can achieve performance comparable to specialized underwater methods, although its robustness decreases in more complex and heterogeneous real-world environments

  </details>

- **[A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting](https://arxiv.org/abs/2604.18205)**  
  *Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada, Jan Baturo, Mateusz Capala, Dominik Belter*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18205) · [pdf](https://arxiv.org/pdf/2604.18205.pdf)
  > 💡 聚焦几何精度的NeRF与Gaussian Splatting评估流程与基准，弥补视觉指标对表面形状保真度的忽视。

  <details><summary>Abstract</summary>

  Recent advances in neural rendering have introduced numerous 3D scene representations. Although standard computer vision metrics evaluate the visual quality of generated images, they often overlook the fidelity of surface geometry. This limitation is particularly critical in robotics, where accurate geometry is essential for tasks such as grasping and object manipulation. In this paper, we present an evaluation pipeline for neural rendering methods that focuses on geometric accuracy, along with a benchmark comprising 19 diverse scenes. Our approach enables a systematic assessment of reconstruction methods in terms of surface and shape fidelity, complementing traditional visual metrics.

  </details>

- **[E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2604.17969)**  
  *Koya Sakamoto, Taiki Miyanishi, Daichi Azuma, Shuhei Kurita, Shu Morikuni, Naoya Chiba, Motoaki Kawanabe, Yusuke Iwasawa, Yutaka Matsuo*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17969) · [pdf](https://arxiv.org/pdf/2604.17969.pdf)
  > 💡 针对现有基准无法评估5自由度视点依赖主动感知，提出

  <details><summary>Abstract</summary>

  Visual search in 3D environments requires embodied agents to actively explore their surroundings and acquire task-relevant evidence. However, existing visual search and embodied AI benchmarks, including EQA, typically rely on static observations or constrained egocentric motion, and thus do not explicitly evaluate fine-grained viewpoint-dependent phenomena that arise under unrestricted 5-DoF viewpoint control in real-world 3D environments, such as visibility changes caused by vertical viewpoint shifts, revealing contents inside containers, and disambiguating object attributes that are only observable from specific angles. To address this limitation, we introduce {E3VS-Bench}, a benchmark for embodied 3D visual search where agents must control their viewpoints in 5-DoF to gather viewpoint-dependent evidence for question answering. E3VS-Bench consists of 99 high-fidelity 3D scenes reconstructed using 3D Gaussian Splatting and 2,014 question-driven episodes. 3D Gaussian Splatting enables photorealistic free-viewpoint rendering that preserves fine-grained visual details (e.g., small text and subtle attributes) often degraded in mesh-based simulators, thereby allowing the construction of questions that cannot be answered from a single view and instead require active inspection across viewpoints in 5-DoF. We evaluate multiple state-of-the-art VLMs and compare their performance with humans. Despite strong 2D reasoning ability, all models exhibit a substantial gap from humans, highlighting limitations in active perception and coherent viewpoint planning specifically under full 5-DoF viewpoint changes.

  </details>

- **[Voronoi-guided Bilateral 2D Gaussian Splatting for Arbitrary-Scale Hyperspectral Image Super-Resolution](https://arxiv.org/abs/2604.17727)**  
  *Jie Zhang, Jinkun You, Shi Chen, Yicong Zhou*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17727) · [pdf](https://arxiv.org/pdf/2604.17727.pdf)
  > 💡 针对任意尺度高光谱超分难题，提出Voronoi引导双边2D高斯散射与光谱增强模块，实现灵活空间重建并保持光谱保真度。

  <details><summary>Abstract</summary>

  Most existing hyperspectral image super-resolution methods require modifications for different scales, limiting their flexibility in arbitrary-scale reconstruction. 2D Gaussian splatting provides a continuous representation that is compatible with arbitrary-scale super-resolution. Existing methods often rely on rasterization strategies, which may limit flexible spatial modeling. Extending them to hyperspectral image super-resolution remains challenging, as the task requires adaptive spatial reconstruction while preserving spectral fidelity. This paper proposes GaussianHSI, a Gaussian-Splatting-based framework for arbitrary-scale hyperspectral image super-resolution. We develop a Voronoi-Guided Bilateral 2D Gaussian Splatting for spatial reconstruction. After predicting a set of Gaussian functions to represent the input, it associates each target pixel with relevant Gaussian functions through Voronoi-guided selection. The target pixel is then reconstructed by aggregating the selected Gaussian functions with reference-aware bilateral weighting, which considers both geometric relevance and consistency with low-resolution features. We further introduce a Spectral Detail Enhancement module to improve spectral reconstruction. Extensive experiments on benchmark datasets demonstrate the effectiveness of GaussianHSI over state-of-the-art methods for arbitrary-scale hyperspectral image super-resolution.

  </details>

- **[Incoherent Deformation, Not Capacity: Diagnosing and Mitigating Overfitting in Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.16747)**  
  *Ahmad Droby*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16747) · [pdf](https://arxiv.org/pdf/2604.16747.pdf)
  > 💡 动态高斯泼溅中分割操作导致形变不连贯引发过拟合，弹性能量正则化缩小测试PSNR差距。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian Splatting methods achieve strong training-view PSNR on monocular video but generalize poorly: on the D-NeRF benchmark we measure an average train-test PSNR gap of 6.18 dB, rising to 11 dB on individual scenes. We report two findings that together account for most of that gap. Finding 1 (the role of splitting). A systematic ablation of the Adaptive Density Control pipeline (split, clone, prune, frequency, threshold, schedule) shows that splitting is responsible for over 80% of the gap: disabling split collapses the cloud from 44K to 3K Gaussians and the gap from 6.18 dB to 1.15 dB. Across all threshold-varying ablations, gap is log-linear in count (r = 0.995, bootstrap 95% CI [0.99, 1.00]), which suggests a capacity-based explanation. Finding 2 (the role of deformation coherence). We show that the capacity explanation is incomplete. A local-smoothness penalty on the per-Gaussian deformation field -- Elastic Energy Regularization (EER) -- reduces the gap by 40.8% while growing the cloud by 85%. Measuring per-Gaussian strain directly on trained checkpoints, EER reduces mean strain by 99.72% (median 99.80%) across all 8 scenes; on 8/8 scenes the median Gaussian under EER is less strained than the 1st-percentile (best-behaved) Gaussian under baseline. Alongside EER, we evaluate two further regularizers: GAD, a loss-rate-aware densification threshold, and PTDrop, a jitter-weighted Gaussian dropout. GAD+EER reduces the gap by 48%; adding PTDrop and a soft growth cap reaches 57%. We confirm that coherence generalizes to (a) a different deformation architecture (Deformable-3DGS, +40.6% gap reduction at re-tuned lambda), and (b) real monocular video (4 HyperNeRF scenes, reducing the mean PSNR gap by 14.9% at the same lambda as D-NeRF, with near-zero quality cost). The overfitting in dynamic 3DGS is driven by incoherent deformation, not parameter count.

  </details>

- **[DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis](https://arxiv.org/abs/2604.13416)**  
  *Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi, Hao-Ping Wang, Charlie Li-Ting Tsai, Yu-Cheng Chang, Yu-Lun Liu, Thomas Do, Chin-Teng Lin*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13416) · [pdf](https://arxiv.org/pdf/2604.13416.pdf)
  > 💡 针对无干扰辐射场缺乏大规模数据集的问题，构建含1048场景的DF3DV-1K数据集，用于基准测试并提升方法性能。

  <details><summary>Abstract</summary>

  Advances in radiance fields have enabled photorealistic novel view synthesis. In several domains, large-scale real-world datasets have been developed to support comprehensive benchmarking and to facilitate progress beyond scene-specific reconstruction. However, for distractor-free radiance fields, a large-scale dataset with clean and cluttered images per scene remains lacking, limiting the development. To address this gap, we introduce DF3DV-1K, a large-scale real-world dataset comprising 1,048 scenes, each providing clean and cluttered image sets for benchmarking. In total, the dataset contains 89,924 images captured using consumer cameras to mimic casual capture, spanning 128 distractor types and 161 scene themes across indoor and outdoor environments. A curated subset of 41 scenes, DF3DV-41, is systematically designed to evaluate the robustness of distractor-free radiance field methods under challenging scenarios. Using DF3DV-1K, we benchmark nine recent distractor-free radiance field methods and 3D Gaussian Splatting, identifying the most robust methods and the most challenging scenarios. Beyond benchmarking, we demonstrate an application of DF3DV-1K by fine-tuning a diffusion-based 2D enhancer to improve radiance field methods, achieving average improvements of 0.96 dB PSNR and 0.057 LPIPS on the held-out set (e.g., DF3DV-41) and the On-the-go dataset. We hope DF3DV-1K facilitates the development of distractor-free vision and promotes progress beyond scene-specific approaches.

  </details>

- **[PatchPoison: Poisoning Multi-View Datasets to Degrade 3D Reconstruction](https://arxiv.org/abs/2604.13153)**  
  *Prajas Wadekar, Venkata Sai Pranav Bachina, Kunal Bhosikar, Ankit Gangwal, Charu Sharma*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13153) · [pdf](https://arxiv.org/pdf/2604.13153.pdf)
  > 💡 针对多视图数据集，通过添加高频棋盘格补丁破坏SfM特征匹配，显著提升3DGS重建误差，无需修改pipeline。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently enabled highly photorealistic 3D reconstruction from casually captured multi-view images. However, this accessibility raises a privacy concern: publicly available images or videos can be exploited to reconstruct detailed 3D models of scenes or objects without the owner's consent. We present PatchPoison, a lightweight dataset-poisoning method that prevents unauthorized 3D reconstruction. Unlike global perturbations, PatchPoison injects a small high-frequency adversarial patch, a structured checkerboard, into the periphery of each image in a multi-view dataset. The patch is designed to corrupt the feature-matching stage of Structure-from-Motion (SfM) pipelines such as COLMAP by introducing spurious correspondences that systematically misalign estimated camera poses. Consequently, downstream 3DGS optimization diverges from the correct scene geometry. On the NeRF-Synthetic benchmark, inserting a 12 X 12 pixel patch increases reconstruction error by 6.8x in LPIPS, while the poisoned images remain unobtrusive to human viewers. PatchPoison requires no pipeline modifications, offering a practical, "drop-in" preprocessing step for content creators to protect their multi-view data.

  </details>

- **[ReefMapGS: Enabling Large-Scale Underwater Reconstruction by Closing the Loop Between Multimodal SLAM and Gaussian Splatting](https://arxiv.org/abs/2604.11992)**  
  *Daniel Yang, Jungseok Hong, John J. Leonard, Yogesh Girdhar*  
  `2026-04-13` · `cs.RO` · [abs](https://arxiv.org/abs/2604.11992) · [pdf](https://arxiv.org/pdf/2604.11992.pdf)
  > 💡 提出ReefMapGS，融合多模态SLAM与3DGS闭环迭代，摆脱COLMAP依赖，实现大规模水下场景重建与精准位姿估计。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting is a powerful visual representation, providing high-quality and efficient 3D scene reconstruction, but it is crucially dependent on accurate camera poses typically obtained from computationally intensive processes like structure-from-motion that are unsuitable for field robot applications. However, in these domains, multimodal sensor data from acoustic, inertial, pressure, and visual sensors are available and suitable for pose-graph optimization-based SLAM methods that can estimate the vehicle's trajectory and thus our needed camera poses while providing uncertainty. We propose a 3DGS-based incremental reconstruction framework, ReefMapGS, that builds an initial model from a high certainty region and progressively expands to incorporate the whole scene. We reconstruct the scene incrementally by interleaving local tracking of new image observations with optimization of the underlying 3DGS scene. These refined poses are integrated back into the pose-graph to globally optimize the whole trajectory. We show COLMAP-free 3D reconstruction of two underwater reef sites with complex geometry as well as more accurate global pose estimation of our AUV over survey trajectories spanning up to 700 m.

  </details>

- **[A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482)**  
  *Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy, Rowel Atienza*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16482) · [pdf](https://arxiv.org/pdf/2604.16482.pdf)
  > 💡 引入α=峰值内存/地图大小，揭示神经方法内存架构决定部署可行性，提出标准化协议与帕累托分析，提供参考值与预算算法。

  <details><summary>Abstract</summary>

  As vision-based robots navigate larger environments, their spatial memory grows without bound, eventually exhausting computational resources, particularly on embedded platforms (8-16GB shared memory, $<$30W) where adding hardware is not an option. This survey examines the spatial memory efficiency problem across 88 references spanning 52 systems (1989-2025), from occupancy grids to neural implicit representations. We introduce the $α= M_{\text{peak}} / M_{\text{map}}$, the ratio of peak runtime memory (the total RAM or GPU memory consumed during operation) to saved map size (the persistent checkpoint written to disk), exposing the gap between published map sizes and actual deployment cost. Independent profiling on an NVIDIA A100 GPU reveals that $α$ spans two orders of magnitude within neural methods alone, ranging from 2.3 (Point-SLAM) to 215 (NICE-SLAM, whose 47,MB map requires 10GB at runtime), showing that memory architecture, not paradigm label, determines deployment feasibility. We propose a standardized evaluation protocol comprising memory growth rate, query latency, memory-completeness curves, and throughput degradation, none of which current benchmarks capture. Through a Pareto frontier analysis with explicit benchmark separation, we show that no single paradigm dominates within its evaluation regime: 3DGS methods achieve the best absolute accuracy at 90-254,MB map size on Replica, while scene graphs provide semantic abstraction at predictable cost. We provide the first independently measured $α$ reference values and an $α$-aware budgeting algorithm enabling practitioners to assess deployment feasibility on target hardware prior to implementation.

  </details>

- **[AnchorSplat: Feed-Forward 3D Gaussian Splatting with 3D Geometric Priors](https://arxiv.org/abs/2604.07053)**  
  *Xiaoxue Zhang, Xiaoxu Zheng, Yixuan Yin, Tiao Zhao, Kaihua Tang, Michael Bi Mi, Zhan Xu, Dave Zhenyu Chen*  
  `2026-04-08` · `cs.CV` · [abs](https://arxiv.org/abs/2604.07053) · [pdf](https://arxiv.org/pdf/2604.07053.pdf)
  > 💡 提出AnchorSplat，利用3D几何先验的锚点对齐高斯表示替代像素对齐，减少高斯数量，提升重建质量与效率。

  <details><summary>Abstract</summary>

  Recent feed-forward Gaussian reconstruction models adopt a pixel-aligned formulation that maps each 2D pixel to a 3D Gaussian, entangling Gaussian representations tightly with the input images. In this paper, we propose AnchorSplat, a novel feed-forward 3DGS framework for scene-level reconstruction that represents the scene directly in 3D space. AnchorSplat introduces an anchor-aligned Gaussian representation guided by 3D geometric priors (e.g., sparse point clouds, voxels, or RGB-D point clouds), enabling a more geometry-aware renderable 3D Gaussians that is independent of image resolution and number of views. This design substantially reduces the number of required Gaussians, improving computational efficiency while enhancing reconstruction fidelity. Beyond the anchor-aligned design, we utilize a Gaussian Refiner to adjust the intermediate Gaussiansy via merely a few forward passes. Experiments on the ScanNet++ v2 NVS benchmark demonstrate the SOTA performance, outperforming previous methods with more view-consistent and substantially fewer Gaussian primitives.

  </details>

- **[PanopticQuery: Unified Query-Time Reasoning for 4D Scenes](https://arxiv.org/abs/2604.05638)**  
  *Ruilin Tang, Yang Zhou, Zhong Ye, Wenxi Liu, Yan Huang, Shengfeng He*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05638) · [pdf](https://arxiv.org/pdf/2604.05638.pdf)
  > 💡 针对动态4D场景语言推理不足，提出基于4D Gaussian Splatting与多视图语义共识的查询推理框架，在复杂查询上达

  <details><summary>Abstract</summary>

  Understanding dynamic 4D environments through natural language queries requires not only accurate scene reconstruction but also robust semantic grounding across space, time, and viewpoints. While recent methods using neural representations have advanced 4D reconstruction, they remain limited in contextual reasoning, especially for complex semantics such as interactions, temporal actions, and spatial relations. A key challenge lies in transforming noisy, view-dependent predictions into globally consistent 4D interpretations. We introduce PanopticQuery, a framework for unified query-time reasoning in 4D scenes. Our approach builds on 4D Gaussian Splatting for high-fidelity dynamic reconstruction and introduces a multi-view semantic consensus mechanism that grounds natural language queries by aggregating 2D semantic predictions across multiple views and time frames. This process filters inconsistent outputs, enforces geometric consistency, and lifts 2D semantics into structured 4D groundings via neural field optimization. To support evaluation, we present Panoptic-L4D, a new benchmark for language-based querying in dynamic scenes. Experiments demonstrate that PanopticQuery sets a new state of the art on complex language queries, effectively handling attributes, actions, spatial relationships, and multi-object interactions. A video demonstration is available in the supplementary materials.

  </details>

- **[GenSmoke-GS: A Multi-Stage Method for Novel View Synthesis from Smoke-Degraded Images Using a Generative Model](https://arxiv.org/abs/2604.03039)**  
  *Qida Cao, Xinyuan Hu, Changyue Shi, Jiajun Ding, Zhou Yu, Jun Yu*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03039) · [pdf](https://arxiv.org/pdf/2604.03039.pdf)
  > 💡 针对烟尘降质图像，提出含去雾、大模型增强与3DGS-MCMC的多阶段方法，提升可见性并保持视图一致性，在挑战赛获第一。

  <details><summary>Abstract</summary>

  This paper describes our method for Track 2 of the NTIRE 2026 3D Restoration and Reconstruction (3DRR) Challenge on smoke-degraded images. In this task, smoke reduces image visibility and weakens the cross-view consistency required by scene optimization and rendering. We address this problem with a multi-stage pipeline consisting of image restoration, dehazing, MLLM-based enhancement, 3DGS-MCMC optimization, and averaging over repeated runs. The main purpose of the pipeline is to improve visibility before rendering while limiting scene-content changes across input views. Experimental results on the challenge benchmark show improved quantitative performance and better visual quality than the provided baselines. The code is available at https://github.com/plbbl/GenSmoke-GS. Our method achieved a ranking of 1 out of 14 participants in Track 2 of the NTIRE 3DRR Challenge, as reported on the official competition website: https://www.codabench.org/competitions/13993/#/results-tab.

  </details>

- **[LightHarmony3D: Harmonizing Illumination and Shadows for Object Insertion in 3D Gaussian Splatting](https://arxiv.org/abs/2603.29209)**  
  *Tianyu Huang, Zhenyang Ren, Zhenchen Wan, Jiyang Zheng, Wenjie Wang, Runnan Chen, Mingming Gong, Tongliang Liu*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2603.29209) · [pdf](https://arxiv.org/pdf/2603.29209.pdf)
  > 💡 在3DGS中插入网格物体时照明与阴影难以一致，提出生成模块预测360° HDR环境图，实现物理逼真渲染并建立首个专用基准。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables high-fidelity reconstruction of scene geometry and appearance. Building on this capability, inserting external mesh objects into reconstructed 3DGS scenes enables interactive editing and content augmentation for immersive applications such as AR/VR, virtual staging, and digital content creation. However, achieving physically consistent lighting and shadows for mesh insertion remains challenging, as it requires accurate scene illumination estimation and multi-view consistent rendering. To address this challenge, we present LightHarmony3D, a novel framework for illumination-consistent mesh insertion in 3DGS scenes. Central to our approach is our proposed generative module that predicts a full 360° HDR environment map at the insertion location via a single forward pass. By leveraging generative priors instead of iterative optimization, our method efficiently captures dominant scene illumination and enables physically grounded shading and shadows for inserted meshes while maintaining multi-view coherence. Furthermore, we introduce the first dedicated benchmark for mesh insertion in 3DGS, providing a standardized evaluation framework for assessing lighting consistency and photorealism. Extensive experiments across multiple real-world reconstruction datasets demonstrate that LightHarmony3D achieves state-of-the-art realism and multi-view consistency.

  </details>

- **[GS3LAM: Gaussian Semantic Splatting SLAM](https://arxiv.org/abs/2603.27781)**  
  *Linfei Li, Lin Zhang, Zhong Wang, Ying Shen*  
  `2026-03-29` · `cs.CV` · [abs](https://arxiv.org/abs/2603.27781) · [pdf](https://arxiv.org/pdf/2603.27781.pdf)
  > 💡 GS3LAM用语义高斯场联合优化位姿与场景，引入深度自适应尺度和随机采样关键帧映射，实现实时稠密语义SLAM。

  <details><summary>Abstract</summary>

  Recently, the multi-modal fusion of RGB, depth, and semantics has shown great potential in dense Simultaneous Localization and Mapping (SLAM). However, a prerequisite for generating consistent semantic maps is the availability of dense, efficient, and scalable scene representations. Existing semantic SLAM systems based on explicit representations are often limited by resolution and an inability to predict unknown areas. Conversely, implicit representations typically rely on time-consuming ray tracing, failing to meet real-time requirements. Fortunately, 3D Gaussian Splatting (3DGS) has emerged as a promising representation that combines the efficiency of point-based methods with the continuity of geometric structures. To this end, we propose GS3LAM, a Gaussian Semantic Splatting SLAM framework that processes multimodal data to render consistent, dense semantic maps in real-time. GS3LAM models the scene as a Semantic Gaussian Field (SG-Field) and jointly optimizes camera poses and the field via multimodal error constraints. Furthermore, a Depth-adaptive Scale Regularization (DSR) scheme is introduced to resolve misalignments between scale-invariant Gaussians and geometric surfaces. To mitigate catastrophic forgetting, we propose a Random Sampling-based Keyframe Mapping (RSKM) strategy, which demonstrates superior performance over common local covisibility optimization methods. Extensive experiments on benchmark datasets show that GS3LAM achieves increased tracking robustness, superior rendering quality, and enhanced semantic precision compared to state-of-the-art methods. Source code is available at https://github.com/lif314/GS3LAM.

  </details>

- **[SGS-Intrinsic: Semantic-Invariant Gaussian Splatting for Sparse-View Indoor Inverse Rendering](https://arxiv.org/abs/2603.27516)**  
  *Jiahao Niu, Rongjia Zheng, Wenju Xu, Wei-Shi Zheng, Qing Zhang*  
  `2026-03-29` · `cs.CV` · [abs](https://arxiv.org/abs/2603.27516) · [pdf](https://arxiv.org/pdf/2603.27516.pdf)
  > 💡 针对稀疏视角室内逆渲染，提出语义不变高斯泼溅，利用语义几何先验构建密集场，结合混合光照和材质先验解耦，提升重建与逆渲染质量。

  <details><summary>Abstract</summary>

  We present SGS-Intrinsic, an indoor inverse rendering framework that works well for sparse-view images. Unlike existing 3D Gaussian Splatting (3DGS) based methods that focus on object-centric reconstruction and fail to work under sparse view settings, our method allows to achieve high-quality geometry reconstruction and accurate disentanglement of material and illumination. The core idea is to construct a dense and geometry-consistent Gaussian semantic field guided by semantic and geometric priors, providing a reliable foundation for subsequent inverse rendering. Building upon this, we perform material-illumination disentanglement by combining a hybrid illumination model and material prior to effectively capture illumination-material interactions. To mitigate the impact of cast shadows and enhance the robustness of material recovery, we introduce illumination-invariant material constraint together with a deshadowing model. Extensive experiments on benchmark datasets show that our method consistently improves both reconstruction fidelity and inverse rendering quality over existing 3DGS-based inverse rendering approaches. Our code is available at https://github.com/GrumpySloths/SGS_Intrinsic.github.io.

  </details>

- **[SUCCESS-GS: Survey of Compactness and Compression for Efficient Static and Dynamic Gaussian Splatting](https://arxiv.org/abs/2512.07197)**  
  *Seokhyun Youn, Soohyun Lee, Geonho Kim, Weeyoung Kwon, Sung-Ho Bae, Jihyong Oh*  
  `2025-12-08` · `cs.CV` · [abs](https://arxiv.org/abs/2512.07197) · [pdf](https://arxiv.org/pdf/2512.07197.pdf)
  > 💡 综述高效3D/4D高斯泼溅，按参数压缩与结构压缩分类方法，系统总结趋势与基准。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a powerful explicit representation enabling real-time, high-fidelity 3D reconstruction and novel view synthesis. However, its practical use is hindered by the massive memory and computational demands required to store and render millions of Gaussians. These challenges become even more severe in 4D dynamic scenes. To address these issues, the field of Efficient Gaussian Splatting has rapidly evolved, proposing methods that reduce redundancy while preserving reconstruction quality. This survey provides the first unified overview of efficient 3D and 4D Gaussian Splatting techniques. For both 3D and 4D settings, we systematically categorize existing methods into two major directions, Parameter Compression and Restructuring Compression, and comprehensively summarize the core ideas and methodological trends within each category. We further cover widely used datasets, evaluation metrics, and representative benchmark comparisons. Finally, we discuss current limitations and outline promising research directions toward scalable, compact, and real-time Gaussian Splatting for both static and dynamic 3D scene representation.

  </details>

- **[Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from Alternating-exposure Monocular Videos](https://arxiv.org/abs/2510.18489)**  
  *Jinfeng Liu, Lingtong Kong, Mi Zhou, Jinwen Chen, Dan Xu*  
  `2025-10-21` · `cs.CV` · [abs](https://arxiv.org/abs/2510.18489) · [pdf](https://arxiv.org/pdf/2510.18489.pdf)
  > 💡 用两阶段高斯泼溅从交替曝光单目LDR视频重建4D HDR场景，无需相机位姿，实现了高质量快速渲染。

  <details><summary>Abstract</summary>

  We introduce Mono4DGS-HDR, the first system for reconstructing renderable 4D high dynamic range (HDR) scenes from unposed monocular low dynamic range (LDR) videos captured with alternating exposures. To tackle such a challenging problem, we present a unified framework with two-stage optimization approach based on Gaussian Splatting. The first stage learns a video HDR Gaussian representation in orthographic camera coordinate space, eliminating the need for camera poses and enabling robust initial HDR video reconstruction. The second stage transforms video Gaussians into world space and jointly refines the world Gaussians with camera poses. Furthermore, we propose a temporal luminance regularization strategy to enhance the temporal consistency of the HDR appearance. Since our task has not been studied before, we construct a new evaluation benchmark using publicly available datasets for HDR video reconstruction. Extensive experiments demonstrate that Mono4DGS-HDR significantly outperforms alternative solutions adapted from state-of-the-art methods in both rendering quality and speed.

  </details>

- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857)**  
  *Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park*  
  `2025-10-04` · `cs.CV` · [abs](https://arxiv.org/abs/2510.03857) · [pdf](https://arxiv.org/pdf/2510.03857.pdf)
  > 💡 通过三阶段渐进剪枝和隐式外观压缩及4D SVQ，将4DGS模型大小减少60%以上，同时保持高质量。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting has emerged as a new paradigm for dynamic scene representation, enabling real-time rendering of scenes with complex motions. However, it faces a major challenge of storage overhead, as millions of Gaussians are required for high-fidelity reconstruction. While several studies have attempted to alleviate this memory burden, they still face limitations in compression ratio or visual quality. In this work, we present OMG4 (Optimized Minimal 4D Gaussian Splatting), a framework that constructs a compact set of salient Gaussians capable of faithfully representing 4D Gaussian models. Our method progressively prunes Gaussians in three stages: (1) Gaussian Sampling to identify primitives critical to reconstruction fidelity, (2) Gaussian Pruning to remove redundancies, and (3) Gaussian Merging to fuse primitives with similar characteristics. In addition, we integrate implicit appearance compression and generalize Sub-Vector Quantization (SVQ) to 4D representations, further reducing storage while preserving quality. Extensive experiments on standard benchmark datasets demonstrate that OMG4 significantly outperforms recent state-of-the-art methods, reducing model sizes by over 60% while maintaining reconstruction quality. These results position OMG4 as a significant step forward in compact 4D scene representation, opening new possibilities for a wide range of applications. Our source code is available at https://minshirley.github.io/OMG4/.

  </details>

- **[WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving](https://arxiv.org/abs/2509.23402)**  
  *Ziyue Zhu, Zhanqian Wu, Zhenxin Zhu, Lijun Zhou, Haiyang Sun, Bing Wan, Kun Ma, Guang Chen, Hangjun Ye, Jin Xie, jian Yang*  
  `2025-09-27` · `cs.CV` · [abs](https://arxiv.org/abs/2509.23402) · [pdf](https://arxiv.org/pdf/2509.23402.pdf)
  > 💡 引入4D感知扩散生成像素对齐4D高斯，结合视频扩散细化，实现高保真时空一致多视角驾驶场景生成。

  <details><summary>Abstract</summary>

  Recent advances in driving-scene generation and reconstruction have demonstrated significant potential for enhancing autonomous driving systems by producing scalable and controllable training data. Existing generation methods primarily focus on synthesizing diverse and high-fidelity driving videos; however, due to limited 3D consistency and sparse viewpoint coverage, they struggle to support convenient and high-quality novel-view synthesis (NVS). Conversely, recent 3D/4D reconstruction approaches have significantly improved NVS for real-world driving scenes, yet inherently lack generative capabilities. To overcome this dilemma between scene generation and reconstruction, we propose WorldSplat, a novel feed-forward framework for 4D driving-scene generation. Our approach effectively generates consistent multi-track videos through two key steps: (i) We introduce a 4D-aware latent diffusion model integrating multi-modal information to produce pixel-aligned 4D Gaussians in a feed-forward manner. (ii) Subsequently, we refine the novel view videos rendered from these Gaussians using a enhanced video diffusion model. Extensive experiments conducted on benchmark datasets demonstrate that WorldSplat effectively generates high-fidelity, temporally and spatially consistent multi-track novel view driving videos. Project: https://wm-research.github.io/worldsplat/

  </details>

- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759)**  
  *Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen*  
  `2025-09-13` · `cs.CV` · [abs](https://arxiv.org/abs/2509.10759) · [pdf](https://arxiv.org/pdf/2509.10759.pdf)
  > 💡 结合4D高斯泼溅与物理光线追踪模拟相机效应，实现快速、可控的高质量动态场景渲染。

  <details><summary>Abstract</summary>

  Common computer vision systems typically assume ideal pinhole cameras but fail when facing real-world camera effects such as fisheye distortion and rolling shutter, mainly due to the lack of learning from training data with camera effects. Existing data generation approaches suffer from either high costs, sim-to-real gaps or fail to accurately model camera effects. To address this bottleneck, we propose 4D Gaussian Ray Tracing (4D-GRT), a novel two-stage pipeline that combines 4D Gaussian Splatting with physically-based ray tracing for camera effect simulation. Given multi-view videos, 4D-GRT first reconstructs dynamic scenes, then applies ray tracing to generate videos with controllable, physically accurate camera effects. 4D-GRT achieves the fastest rendering speed while performing better or comparable rendering quality compared to existing baselines. Additionally, we construct eight synthetic dynamic scenes in indoor environments across four camera effects as a benchmark to evaluate generated videos with camera effects.

  </details>

- **[Style4D-Bench: A Benchmark Suite for 4D Stylization](https://arxiv.org/abs/2508.19243)**  
  *Beiqi Chen, Shuai Shao, Haitang Feng, Jianhuang Lai, Jianlou Si, Guangcong Wang*  
  `2025-08-26` · `cs.CV` · [abs](https://arxiv.org/abs/2508.19243) · [pdf](https://arxiv.org/pdf/2508.19243.pdf)
  > 💡 首个4D风格化基准，提出基于4D高斯泼溅的Style4D，用MLP实现时空感知风格化与几何保持。

  <details><summary>Abstract</summary>

  We introduce Style4D-Bench, the first benchmark suite specifically designed for 4D stylization, with the goal of standardizing evaluation and facilitating progress in this emerging area. Style4D-Bench comprises: 1) a comprehensive evaluation protocol measuring spatial fidelity, temporal coherence, and multi-view consistency through both perceptual and quantitative metrics, 2) a strong baseline that make an initial attempt for 4D stylization, and 3) a curated collection of high-resolution dynamic 4D scenes with diverse motions and complex backgrounds. To establish a strong baseline, we present Style4D, a novel framework built upon 4D Gaussian Splatting. It consists of three key components: a basic 4DGS scene representation to capture reliable geometry, a Style Gaussian Representation that leverages lightweight per-Gaussian MLPs for temporally and spatially aware appearance control, and a Holistic Geometry-Preserved Style Transfer module designed to enhance spatio-temporal consistency via contrastive coherence learning and structural content preservation. Extensive experiments on Style4D-Bench demonstrate that Style4D achieves state-of-the-art performance in 4D stylization, producing fine-grained stylistic details with stable temporal dynamics and consistent multi-view rendering. We expect Style4D-Bench to become a valuable resource for benchmarking and advancing research in stylized rendering of dynamic 3D scenes. Project page: https://becky-catherine.github.io/Style4D . Code: https://github.com/Becky-catherine/Style4D-Bench .

  </details>

- **[CharacterShot: Controllable and Consistent 4D Character Animation](https://arxiv.org/abs/2508.07409)**  
  *Junyao Gao, Jiaxing Li, Wenran Liu, Yanhong Zeng, Fei Shen, Kai Chen, Yanan Sun, Cairong Zhao*  
  `2025-08-10` · `cs.CV` · [abs](https://arxiv.org/abs/2508.07409) · [pdf](https://arxiv.org/pdf/2508.07409.pdf)
  > 💡 从单张角色图和2D姿态生成可控一致4D动画，采用DiT模型、双注意力与邻域约束4D高斯泼溅，构建大规模数据集。

  <details><summary>Abstract</summary>

  In this paper, we propose \textbf{CharacterShot}, a controllable and consistent 4D character animation framework that enables any individual designer to create dynamic 3D characters (i.e., 4D character animation) from a single reference character image and a 2D pose sequence. We begin by pretraining a powerful 2D character animation model based on a cutting-edge DiT-based image-to-video model, which allows for any 2D pose sequnce as controllable signal. We then lift the animation model from 2D to 3D through introducing dual-attention module together with camera prior to generate multi-view videos with spatial-temporal and spatial-view consistency. Finally, we employ a novel neighbor-constrained 4D gaussian splatting optimization on these multi-view videos, resulting in continuous and stable 4D character representations. Moreover, to improve character-centric performance, we construct a large-scale dataset Character4D, containing 13,115 unique characters with diverse appearances and motions, rendered from multiple viewpoints. Extensive experiments on our newly constructed benchmark, CharacterBench, demonstrate that our approach outperforms current state-of-the-art methods. Code, models, and datasets will be publicly available at https://github.com/Jeoyal/CharacterShot.

  </details>

- **[4DVD: Cascaded Dense-view Video Diffusion Model for High-quality 4D Content Generation](https://arxiv.org/abs/2508.04467)**  
  *Shuzhou Yang, Xiaodong Cun, Xiaoyu Li, Yaowei Li, Jian Zhang*  
  `2025-08-06` · `cs.CV` · [abs](https://arxiv.org/abs/2508.04467) · [pdf](https://arxiv.org/pdf/2508.04467.pdf)
  > 💡 提出级联扩散模型4DVD，将4D生成解耦为布局预测和结构感知生成，由单目视频生成高质量密集视图视频，实现SOTA的4D内容生成。

  <details><summary>Abstract</summary>

  Given the high complexity of directly generating high-dimensional data such as 4D, we present 4DVD, a cascaded video diffusion model that generates 4D content in a decoupled manner. Unlike previous multi-view video methods that directly model 3D space and temporal features simultaneously with stacked cross view/temporal attention modules, 4DVD decouples this into two subtasks: coarse multi-view layout generation and structure-aware conditional generation, and effectively unifies them. Specifically, given a monocular video, 4DVD first predicts the dense view content of its layout with superior cross-view and temporal consistency. Based on the produced layout priors, a structure-aware spatio-temporal generation branch is developed, combining these coarse structural priors with the exquisite appearance content of input monocular video to generate final high-quality dense-view videos. Benefit from this, explicit 4D representation~(such as 4D Gaussian) can be optimized accurately, enabling wider practical application. To train 4DVD, we collect a dynamic 3D object dataset, called D-Objaverse, from the Objaverse benchmark and render 16 videos with 21 frames for each object. Extensive experiments demonstrate our state-of-the-art performance on both novel view synthesis and 4D generation. Our project page is https://4dvd.github.io/

  </details>

- **[PhysGaia: A Physics-Aware Benchmark with Multi-Body Interactions for Dynamic Novel View Synthesis](https://arxiv.org/abs/2506.02794)**  
  *Mijeong Kim, Gunhee Kim, Jungyoon Choi, Wonjae Roh, Bohyung Han*  
  `2025-06-03` · `cs.GR` · [abs](https://arxiv.org/abs/2506.02794) · [pdf](https://arxiv.org/pdf/2506.02794.pdf)
  > 💡 针对动态新视角合成缺乏物理感知基准的问题，提出包含多体交互与多种材料的PhysGaia，提供3D轨迹和物理参数以评估物理建模一致性。

  <details><summary>Abstract</summary>

  We introduce PhysGaia, a novel physics-aware benchmark for Dynamic Novel View Synthesis (DyNVS) that encompasses both structured objects and unstructured physical phenomena. While existing datasets primarily focus on photorealistic appearance, PhysGaia is specifically designed to support physics-consistent dynamic reconstruction. Our benchmark features complex scenarios with rich multi-body interactions, where objects realistically collide and exchange forces. Furthermore, it incorporates a diverse range of materials, including liquid, gas, textile, and rheological substance, moving beyond the rigid-body assumptions prevalent in prior work. To ensure physical fidelity, all scenes in PhysGaia are generated using material-specific physics solvers that strictly adhere to fundamental physical laws. We provide comprehensive ground-truth information, including 3D particle trajectories and physical parameters (e.g., viscosity), enabling the quantitative evaluation of physical modeling. To facilitate research adoption, we also provide integration pipelines for recent 4D Gaussian Splatting models along with our dataset and their results. By addressing the critical shortage of physics-aware benchmarks, PhysGaia can significantly advance research in dynamic view synthesis, physics-based scene understanding, and the integration of deep learning with physical simulation, ultimately enabling more faithful reconstruction and interpretation of complex dynamic scenes.

  </details>

- **[Disentangled 4D Gaussian Splatting: Rendering High-Resolution Dynamic World at 343 FPS](https://arxiv.org/abs/2503.22159)**  
  *Hao Feng, Hao Sun, Wei Xie, Zhi Zuo, Zhengzhe Liu*  
  `2025-03-28` · `cs.GR` · [abs](https://arxiv.org/abs/2503.22159) · [pdf](https://arxiv.org/pdf/2503.22159.pdf)
  > 💡 通过解耦4D高斯的时空分量并引入动态2D高斯与流损失，实现了343 FPS的高质量动态场景渲染。

  <details><summary>Abstract</summary>

  While dynamic novel view synthesis from 2D videos has seen progress, achieving efficient reconstruction and rendering of dynamic scenes remains a challenging task. In this paper, we introduce Disentangled 4D Gaussian Splatting (Disentangled4DGS), a novel representation and rendering pipeline that achieves real-time performance without compromising visual fidelity. Disentangled4DGS decouples the temporal and spatial components of 4D Gaussians, avoiding the need for slicing first and four-dimensional matrix calculations in prior methods. By projecting temporal and spatial deformations into dynamic 2D Gaussians and deferring temporal processing, we minimize redundant computations of 4DGS. Our approach also features a gradient-guided flow loss and temporal splitting strategy to reduce artifacts. Experiments demonstrate a significant improvement in rendering speed and quality, achieving 343 FPS when render 1352*1014 resolution images on a single RTX3090 while reducing storage requirements by at least 4.5%. Our approach sets a new benchmark for dynamic novel view synthesis, outperforming existing methods on both multi-view and monocular dynamic scene datasets.

  </details>

- **[SDD-4DGS: Static-Dynamic Aware Decoupling in Gaussian Splatting for 4D Scene Reconstruction](https://arxiv.org/abs/2503.09332)**  
  *Dai Sun, Huhao Guan, Kun Zhang, Xike Xie, S. Kevin Zhou*  
  `2025-03-12` · `cs.CV` · [abs](https://arxiv.org/abs/2503.09332) · [pdf](https://arxiv.org/pdf/2503.09332.pdf)
  > 💡 针对动静不加区分问题，提出SDD-4DGS，引入概率动态感知系数实现高斯泼溅的动静解耦，提升重建保真度。

  <details><summary>Abstract</summary>

  Dynamic and static components in scenes often exhibit distinct properties, yet most 4D reconstruction methods treat them indiscriminately, leading to suboptimal performance in both cases. This work introduces SDD-4DGS, the first framework for static-dynamic decoupled 4D scene reconstruction based on Gaussian Splatting. Our approach is built upon a novel probabilistic dynamic perception coefficient that is naturally integrated into the Gaussian reconstruction pipeline, enabling adaptive separation of static and dynamic components. With carefully designed implementation strategies to realize this theoretical framework, our method effectively facilitates explicit learning of motion patterns for dynamic elements while maintaining geometric stability for static structures. Extensive experiments on five benchmark datasets demonstrate that SDD-4DGS consistently outperforms state-of-the-art methods in reconstruction fidelity, with enhanced detail restoration for static structures and precise modeling of dynamic motions. The code will be released.

  </details>

