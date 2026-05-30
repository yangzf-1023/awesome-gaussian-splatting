# SLAM / Localization / Mapping

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---

## 2026-05-30

- **[PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting](https://arxiv.org/abs/2605.08035)**  
  *William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp*  
  `2026-05-08` · `eess.SP` · [abs](https://arxiv.org/abs/2605.08035) · [pdf](https://arxiv.org/pdf/2605.08035.pdf)
  > 💡 提出PropSplat，用3D高斯原语无地图重建射频场，稀疏测量下精度优于现有方法。

  <details><summary>Abstract</summary>

  Building a site-specific propagation model typically requires either ray-tracing over detailed 3D maps or dense measurement campaigns. Both approaches are expensive and often infeasible for rapid deployments where geographic data is unavailable or outdated. We present PropSplat, a map-free propagation modeling method that reconstructs radio frequency (RF) fields using 3D anisotropic Gaussian primitives. Each Gaussian encodes a scalar path loss offset relative to an explicit baseline path loss model with a learnable path loss exponent. Gaussians are initialized along observed transmitter--receiver paths and optimized end-to-end to learn the propagation environment without external information like floor plans, terrain databases, or clutter data. We evaluate PropSplat against wireless radiance field methods NeRF$^2$, GSRF, and WRF-GS+ on two real-world datasets. On large-scale outdoor drive-tests spanning multiple topographical regions at six sub-6 GHz frequencies, PropSplat achieves 5.38 dB RMSE when training measurements are spaced 300m apart and outperforms WRF-GS+ (5.87 dB), GSRF (7.46 dB), and NeRF$^2$ (14.76 dB). On indoor Bluetooth Low Energy measurements, PropSplat achieves 0.19m mean localization error, an order of magnitude better than NeRF$^2$ (1.84m), while achieving near-identical received signal strength prediction accuracy. These results show that accurate site-specific propagation reconstruction is achievable from sparse RF-native measurements. The need for geographic data as a prerequisite for scalable RF environment modeling is reduced.

  </details>

- **[ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730)**  
  *Yingdong Gu, Shaocheng Yan, Zhenjun Zhao, Yuan Kou, Jianxin Luo, Pengcheng Shi, Jiayuan Li*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04730) · [pdf](https://arxiv.org/pdf/2605.04730.pdf)
  > 💡 针对3DGS中α混合导致的特征偏差，提出几何加权融合与地标采样，降低17%平移误差且训练时间仅1/10。

  <details><summary>Abstract</summary>

  Visual localization is a core technology for augmented reality and autonomous navigation. Recent methods combine the efficient rendering of 3D Gaussian Splatting (3DGS) with feature-based localization. These methods rely on direct matching between 2D query features and the 3D Gaussian feature field, but this often results in mismatches due to an inherent bias in the learned Gaussian feature. We theoretically analyze the feature learning process in 3DGS, revealing that the widely adopted $α$-blending optimization inherently introduces bias into 3D point features. This bias stems from the entanglement between individual Gaussians and their neighboring Gaussians, making the learned features unsuitable for precise matching tasks. Motivated by these findings, we propose ULF-Loc, an unbiased landmark feature framework that replaces biased feature optimization with geometry-weighted feature fusion. We further introduce keypoint-consensus landmark sampling to select reliable Gaussians and local geometric consistency verification to reject mismatches caused by rendering artifacts. On the Cambridge Landmarks dataset, ULF-Loc reduces the mean median translation error by 17\% compared to the state-of-the-art, while achieving superior efficiency with only 1/10 the training time and 1/6 the GPU memory of STDLoc.

  </details>

- **[PoInit-of-View: Poisoning Initialization of Views Transfers Across Multiple 3D Reconstruction Systems](https://arxiv.org/abs/2604.16540)**  
  *Weijie Wang, Songlong Xing, Zhengyu Zhao, Nicu Sebe, Bruno Lepri*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.16540) · [pdf](https://arxiv.org/pdf/2604.16540.pdf)
  > 💡 针对SfM初始化模块制造跨视图梯度不一致，破坏关键点匹配与位姿估计，实现跨3D重建系统的高迁移性投毒攻击。

  <details><summary>Abstract</summary>

  Poisoning input views of 3D reconstruction systems has been recently studied. However, we identify that existing studies simply backpropagate adversarial gradients through the 3D reconstruction pipeline as a whole, without uncovering the new vulnerability rooted in specific modules of the 3D reconstruction pipeline. In this paper, we argue that the structure-from-motion (SfM) initialization, as the geometric core of many widely used reconstruction systems, can be targeted to achieve transferable poisoning effects across diverse 3D reconstruction systems. To this end, we propose PoInit-of-View, which optimizes adversarial perturbations to intentionally introduce cross-view gradient inconsistencies at projections of corresponding 3D points. These inconsistencies disrupt keypoint detection and feature matching, thereby corrupting pose estimation and triangulation within SfM, eventually resulting in low-quality rendered views. We also provide a theoretical analysis that connects cross-view inconsistency to correspondence collapse. Experimental results demonstrate the effectiveness of our PoInit-of-View on diverse 3D reconstruction systems and datasets, surpassing the single-view baseline by 25.1% in PSNR and 16.5% in SSIM in black-box transfer settings, such as 3DGS to NeRF.

  </details>

- **[RadarSplat-RIO: Indoor Radar-Inertial Odometry with Gaussian Splatting-Based Radar Bundle Adjustment](https://arxiv.org/abs/2604.13492)**  
  *Pou-Chun Kung, Yuan Tian, Zhengqin Li, Yue Liu, Eric Whitmire, Wolf Kienzle, Hrvoje Benko*  
  `2026-04-15` · `cs.RO` · [abs](https://arxiv.org/abs/2604.13492) · [pdf](https://arxiv.org/pdf/2604.13492.pdf)
  > 💡 针对雷达SLAM漂移问题，提出首个高斯溅射雷达束调整方法，联合优化位姿与场景几何，误差降低90%和80%。

  <details><summary>Abstract</summary>

  Radar is more resilient to adverse weather and lighting conditions than visual and Lidar simultaneous localization and mapping (SLAM). However, most radar SLAM pipelines still rely heavily on frame-to-frame odometry, which leads to substantial drift. While loop closure can correct long-term errors, it requires revisiting places and relies on robust place recognition. In contrast, visual odometry methods typically leverage bundle adjustment (BA) to jointly optimize poses and map within a local window. However, an equivalent BA formulation for radar has remained largely unexplored. We present the first radar BA framework enabled by Gaussian Splatting (GS), a dense and differentiable scene representation. Our method jointly optimizes radar sensor poses and scene geometry using full range-azimuth-Doppler data, bringing the benefits of multi-frame BA to radar for the first time. When integrated with an existing radar-inertial odometry frontend, our approach significantly reduces pose drift and improves robustness. Across multiple indoor scenes, our radar BA achieves substantial gains over the prior radar-inertial odometry, reducing average absolute translational and rotational errors by 90% and 80%, respectively.

  </details>

- **[LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios](https://arxiv.org/abs/2604.05402)**  
  *Xiang Zhang, Tengfei Wang, Fang Xu, Xin Wang, Zongqian Zhan*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05402) · [pdf](https://arxiv.org/pdf/2604.05402.pdf)
  > 💡 应对大规模无人机场景下3DGS定位的位姿初始化难和渲染伪影问题，提出尺度感知初始化和拉普拉斯可靠性掩码，显著提升精度与鲁棒性。

  <details><summary>Abstract</summary>

  Visual localization in large-scale UAV scenarios is a critical capability for autonomous systems, yet it remains challenging due to geometric complexity and environmental variations. While 3D Gaussian Splatting (3DGS) has emerged as a promising scene representation, existing 3DGS-based visual localization methods struggle with robust pose initialization and sensitivity to rendering artifacts in large-scale settings. To address these limitations, we propose LSGS-Loc, a novel visual localization pipeline tailored for large-scale 3DGS scenes. Specifically, we introduce a scale-aware pose initialization strategy that combines scene-agnostic relative pose estimation with explicit 3DGS scale constraints, enabling geometrically grounded localization without scene-specific training. Furthermore, in the pose refinement, to mitigate the impact of reconstruction artifacts such as blur and floaters, we develop a Laplacian-based reliability masking mechanism that guides photometric refinement toward high-quality regions. Extensive experiments on large-scale UAV benchmarks demonstrate that our method achieves state-of-the-art accuracy and robustness for unordered image queries, significantly outperforming existing 3DGS-based approaches. Code is available at: https://github.com/xzhang-z/LSGS-Loc

  </details>

- **[Efficient Camera Pose Augmentation for View Generalization in Robotic Policy Learning](https://arxiv.org/abs/2603.29192)**  
  *Sen Wang, Huaiyi Dong, Jingyi Tian, Jiayi Li, Zhuo Yang, Tongtong Cao, Anlin Chen, Shuang Wu, Le Wang, Sanping Zhou*  
  `2026-03-31` · `cs.RO` · [abs](https://arxiv.org/abs/2603.29192) · [pdf](https://arxiv.org/pdf/2603.29192.pdf)
  > 💡 针对机器人策略新视角泛化差的问题，提出GenSplat，利用前馈3DGS和3D先验蒸馏生成合成视图增强训练，提升鲁棒性。

  <details><summary>Abstract</summary>

  Prevailing 2D-centric visuomotor policies exhibit a pronounced deficiency in novel view generalization, as their reliance on static observations hinders consistent action mapping across unseen views. In response, we introduce GenSplat, a feed-forward 3D Gaussian Splatting framework that facilitates view-generalized policy learning through novel view rendering. GenSplat employs a permutation-equivariant architecture to reconstruct high-fidelity 3D scenes from sparse, uncalibrated inputs in a single forward pass. To ensure structural integrity, we design a 3D-prior distillation strategy that regularizes the 3DGS optimization, preventing the geometric collapse typical of purely photometric supervision. By rendering diverse synthetic views from these stable 3D representations, we systematically augment the observational manifold during training. This augmentation forces the policy to ground its decisions in underlying 3D structures, thereby ensuring robust execution under severe spatial perturbations where baselines severely degrade.

  </details>

- **[Unblur-SLAM: Dense Neural SLAM for Blurry Inputs](https://arxiv.org/abs/2603.26810)**  
  *Qi Zhang, Denis Rozumny, Francesco Girlanda, Sezer Karaoglu, Marc Pollefeys, Theo Gevers, Martin R. Oswald*  
  `2026-03-26` · `cs.CV` · [abs](https://arxiv.org/abs/2603.26810) · [pdf](https://arxiv.org/pdf/2603.26810.pdf)
  > 💡 使用前馈去模糊与3DGS模糊建模，从模糊输入实现锐利SLAM重建，姿态与几何纹理

  <details><summary>Abstract</summary>

  We propose Unblur-SLAM, a novel RGB SLAM pipeline for sharp 3D reconstruction from blurred image inputs. In contrast to previous work, our approach is able to handle different types of blur and demonstrates state-of-the-art performance in the presence of both motion blur and defocus blur. Moreover, we adjust the computation effort with the amount of blur in the input image. As a first stage, our method uses a feed-forward image deblurring model for which we propose a suitable training scheme that can improve both tracking and mapping modules. Frames that are successfully deblurred by the feed-forward network obtain refined poses and depth through local-global multi-view optimization and loop closure. Frames that fail the first stage deblurring are directly modeled through the global 3DGS representation and an additional blur network to model multiple blurred sub-frames and simulate the blur formation process in 3D space, thereby learning sharp details and refined sub-frame poses. Experiments on several real-world datasets demonstrate consistent improvements in both pose estimation and sharp reconstruction results of geometry and texture.

  </details>

- **[Pose-Free Omnidirectional Gaussian Splatting for 360-Degree Videos with Consistent Depth Priors](https://arxiv.org/abs/2603.23324)**  
  *Chuanqing Zhuang, Xin Lu, Zehui Deng, Zhengda Lu, Yiqun Wang, Junqi Diao, Jun Xiao*  
  `2026-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2603.23324) · [pdf](https://arxiv.org/pdf/2603.23324.pdf)
  > 💡 针对无姿态360度视频，提出PFGS360，用球面一致性姿态估计和深度内点感知密集化模块，实现高效重建及逼真新视角合成。

  <details><summary>Abstract</summary>

  Omnidirectional 3D Gaussian Splatting with panoramas is a key technique for 3D scene representation, and existing methods typically rely on slow SfM to provide camera poses and sparse points priors. In this work, we propose a pose-free omnidirectional 3DGS method, named PFGS360, that reconstructs 3D Gaussians from unposed omnidirectional videos. To achieve accurate camera pose estimation, we first construct a spherical consistency-aware pose estimation module, which recovers poses by establishing consistent 2D-3D correspondences between the reconstructed Gaussians and the unposed images using Gaussians' internal depth priors. Besides, to enhance the fidelity of novel view synthesis, we introduce a depth-inlier-aware densification module to extract depth inliers and Gaussian outliers with consistent monocular depth priors, enabling efficient Gaussian densification and achieving photorealistic novel view synthesis. The experiments show significant outperformance over existing pose-free and pose-aware 3DGS methods on both real-world and synthetic 360-degree videos. Code is available at https://github.com/zcq15/PFGS360.

  </details>

