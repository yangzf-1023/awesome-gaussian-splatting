# Dynamic / 4D / Streaming

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---




















## 2026-07-09

- **[NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2607.07168)**  
  *Xiangyu Sun, Liu Liu, Seungkwon Yang, Jingbing Han, Seungtae Nam, Zhizhong Su, Eunbyung Park*  
  `2026-07-08` · `cs.CV` · [abs](https://arxiv.org/abs/2607.07168) · [pdf](https://arxiv.org/pdf/2607.07168.pdf)
  > 💡 针对长序列位姿漂移，提出Raymap引导耦合模块联合优化几何与外观，实现鲁棒的无位姿前馈3D重建。

  <details><summary>Abstract</summary>

  Pose-Free Feed-forward 3D Gaussian Splatting (3DGS) has recently emerged as a powerful paradigm for fast scene reconstruction. However, its performance degrades significantly in long image sequences due to cumulative camera pose estimation drift, which propagates errors into geometric modeling and severely limits rendering fidelity. In this work, we revisit the long-sequence bottleneck and identify pose drift as the primary factor restricting reconstruction quality. Furthermore, while SfM-based pseudo ground-truth poses introduce sensor noise, purely rendering-based supervision often leads to optimization instability and local minima due to the entangled optimization of geometry and pose. To address the challenges, we propose a synergistic pose-free framework that explicitly couples geometry and appearance via a Raymap-Guided Coupling Module (RGC). Concretely, we anchor Gaussian centers to raymap-induced geometry and jointly optimize RGB reconstruction, raymap consistency, and camera regularization under a unified objective, yielding a bidirectional feedback loop: stronger geometry improves rendering, and appearance supervision in turn refines geometry and pose. To further stabilize learning across wide temporal ranges, we introduce a Dual-Frequency Viewpoint Scheduling strategy that combines easy-to-hard interval expansion with replay of short-interval pairs. Extensive experiments across in-domain and cross-domain datasets show consistent gains in both rendering and pose estimation, with notably improved robustness on long sequences. Ablation studies validate our central insight: explicitly designed geometry-appearance synergy is the key to scalable and drift-robust pose-free feed-forward 3D reconstruction.

  </details>

## 2026-07-08

- **[PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238)**  
  *Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren*  
  `2026-07-07` · `cs.CV` · [abs](https://arxiv.org/abs/2607.06238) · [pdf](https://arxiv.org/pdf/2607.06238.pdf)
  > 💡 针对MRI超分辨忽略分辨率-SNR物理耦合，提出物理感知重建方法，结合

  <details><summary>Abstract</summary>

  Magnetic resonance imaging (MRI) super-resolution is vital for improving diagnostic accessibility, yet most methods treat it as a deterministic mapping from a fixed low-resolution input to a high-resolution target. This overlooks a key property of MRI acquisition physics: spatial resolution and signal-to-noise ratio (SNR) are inherently coupled, making any given low-resolution scan merely one of many possible realizations under varying acquisition trade-offs. We rethink MRI super-resolution as a physics-aware reconstruction problem, in which the goal is to identify the optimal resolution-SNR configuration and then super-resolve it to obtain high-quality MRI results. A key implication of this formulation is that MRI resolution becomes dynamic rather than fixed. To handle such resolution-heterogeneous inputs, we adapt 2D Gaussian Splatting (2D GS) to MRI by formulating reconstruction as a coordinate-based, resolution-agnostic rendering problem. To further enhance fidelity, we introduce three innovations: (1) a prior-aware Gaussian representation that combines an Anatomical Structure Prior for tissue-specific kernel initialization with an Imaging System Prior that captures hardware characteristics via a covariance dictionary; (2) a physics-constrained signal modeling scheme that predicts intrinsic tissue parameters (proton density rho and effective relaxation rate R2) and synthesizes intensities through governing physical equations, ensuring biophysically plausible contrast; and (3) a meta-learning framework that alleviates paired-data scarcity by pretraining on simulated data and adapting to real-world conditions. Extensive experiments on dynamic-resolution datasets and standard benchmarks demonstrate that our method achieves state-of-the-art performance, highlighting its strong potential for clinical deployment.

  </details>

## 2026-07-07

- **[GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243)**  
  *Keito Abe, Kaede Shiohara, Takashi Otonari, Toshihiko Yamasaki*  
  `2026-07-06` · `cs.CV` · [abs](https://arxiv.org/abs/2607.05243) · [pdf](https://arxiv.org/pdf/2607.05243.pdf)
  > 💡 提出GUSH3R前馈框架，从单目视频同时重建动态人体和静态场景为

  <details><summary>Abstract</summary>

  Reconstructing dynamic human-scene environments from monocular videos is a challenging problem that requires jointly modeling scene geometry, camera motion, and non-rigid human dynamics while enabling photorealistic rendering. Recent feed-forward methods can efficiently predict geometry, but they are often limited to non-photorealistic representations such as point clouds and meshes, or they fail to handle non-rigid objects, particularly dynamic humans. To fill this gap, we present GUSH3R (Gaussian-Unified Scene Human 3D Reconstruction), a feed-forward framework for online dynamic human-scene reconstruction. From a monocular human-scene video, our method reconstructs dynamic humans (everyone) and static scenes (everywhere) in a single forward pass (all at once) as 3D Gaussian Splatting (3DGS) primitives (as gaussians), which are geometrically consistent and capable of novel view synthesis. Experiments on monocular human-scene datasets demonstrate that our approach achieves competitive novel view synthesis quality while significantly improving inference efficiency compared to optimization-based methods.

  </details>

- **[DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting](https://arxiv.org/abs/2607.04761)**  
  *Yimo Wang, Bin Kang, Shuojue Yang, Yueming Jin*  
  `2026-07-06` · `cs.CV` · [abs](https://arxiv.org/abs/2607.04761) · [pdf](https://arxiv.org/pdf/2607.04761.pdf)
  > 💡 提出几何

  <details><summary>Abstract</summary>

  Real-time, text-promptable 4D reconstruction is indispensable for autonomous surgical interaction. Severe misalignment between semantic meaning and physical anatomy still persists, largely because existing solutions integrate Vision-Language Models into deformable fields via a rigid coupling scheme that tightly binds semantic features to geometric warping. In this paper, we propose DeGenseGS, Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting, a novel framework that independently models semantic evolution and geometric deformation. Specifically, we propose a HexPlane-based spatiotemporal entanglement module that uses shared kinematic latents to synchronize semantic mutations with scene dynamics, while explicitly disentangling semantic updates from geometric deformation. To further ensure robustness against reconstruction artifacts, we devise a Rasterization-Native Semantic Extraction mechanism that infers semantics from topologically continuous feature maps. Additionally, we incorporate an angular-aligned optimization strategy that conforms to the native hyperspherical latent space, thereby preventing semantic distortion. Extensive evaluations on the CholecSeg8k and EndoVis18 datasets demonstrate that DeGenseGS achieves state-of-the-art performance. Our framework yields enhanced geometric completeness and robust semantic-anatomic alignment, enabling spatially continuous segmentation despite drastic tissue deformation and topological transitions.

  </details>

- **[TemporalGS: Training-Free Plug-and-Play Acceleration for 3D Gaussian Splatting Rendering via Temporal Priors](https://arxiv.org/abs/2607.03390)**  
  *Yuhongze Zhou, Zihao Yang, Xinxin Zuo, Juwei Lu*  
  `2026-07-03` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03390) · [pdf](https://arxiv.org/pdf/2607.03390.pdf)
  > 💡 利用时间先验动态剔除与选择性渲染，无训练即插即用加速3DGS，提升渲染速度达1.48倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized novel-view synthesis with its fast and high-fidelity rendering. However, rendering at high FPS and low latency across various scenes remains a challenge, especially when large amounts of 3D Gaussian ellipsoids appear in the scene. To address this issue, we introduce TemporalGS, to the best of our knowledge, the first training-free plug-and-play algorithmic approach to accelerate 3DGS rendering without any post-training or post-processing, implemented on top of tile-based software rasterization. The key idea is that, instead of rendering frames independently as 3DGS, we leverage the temporal priors, represented by novel geometry and appearance buffers, etc., to reduce redundancy of Gaussian preprocessing, sorting, and rasterization operations of consecutive frames. Specifically, we propose two acceleration strategies: (1) temporal dynamic culling, which filters out Gaussians that contribute less to current frame rendering; (2) selective rendering, which renders only a small portion of tiles that cannot be approximated by the temporal priors. By adapting and interleaving these two strategies, TemporalGS yields a simple but effective plug-and-play solution for 3DGS rendering speed-up without any training. Extensive experiments show that TemporalGS achieves comparable or even better performance compared to existing state-of-the-art post-training or post-processing-based 3DGS rendering acceleration approaches. TemporalGS can significantly enhance the rendering speed of various 3DGS methods, achieving up to $1.48\times$ acceleration, while maintaining competitive rendering quality. We further extend our TemporalGS to hardware rasterization-based 3DGS to show the portability of our algorithm.

  </details>

## 2026-07-04

- **[DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability](https://arxiv.org/abs/2607.01860)**  
  *Ziheng Xu, Qingfeng Li, Xuefeng Liu, Chen Chen, Jianwei Niu*  
  `2026-07-02` · `cs.RO` · [abs](https://arxiv.org/abs/2607.01860) · [pdf](https://arxiv.org/pdf/2607.01860.pdf)
  > 💡 针对动态场景SLAM中瞬态物体导致伪影问题，提出双层次概率框架融合语义与几何信息，实现无伪影静态地图并提升跟踪精度13%。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in dense dynamic Simultaneous Localization And Mapping (SLAM). Prevailing methods typically discard predefined dynamic objects, ignoring that transiently static objects offer valuable geometric constraints for pose estimation. A recent work attempts to leverage this potential by employing per-pixel uncertainty maps to quantify the magnitude of motion. While this approach enables transiently static objects to enhance pose estimation, it erroneously integrates these objects into the static map, resulting in persistent artifacts. Moreover, its reliance on purely geometric information leads to ambiguous object boundaries in the uncertainty maps. To overcome these limitations, we present DL-SLAM, a monocular Gaussian Splatting SLAM system built upon a novel dual-level probabilistic framework. Our method computes dynamic probability maps by combining semantic and geometric information. These pixel-level probabilities are lifted to 3D and aggregated to derive an object-level dynamic probability for each instance. Object-level probability enables the categorical pruning of dynamic Gaussians, resulting in an artifact-free static map. The static map, in turn, provides a geometrically consistent guidance to refine the pixel-wise probabilities, enhancing their reliability. Experimental results demonstrate that DL-SLAM outperforms existing approaches, improving tracking accuracy by up to 13\% while generating high-fidelity semantic maps.

  </details>

- **[MVFusion-GS: Motion-Variance Guided Temporal Attention for High-Quality Dynamic Gaussian Splatting](https://arxiv.org/abs/2607.01578)**  
  *Jianwei Hu, Tingxuan Huang, Hengyu Zhou, Ningna Wang, Xiaohu Guo Jinshan Lai, Bin Wang*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.01578) · [pdf](https://arxiv.org/pdf/2607.01578.pdf)
  > 💡 针对动态场景重建，提出运动方差引导和运动形式时间注意力增强变形网络，提升前景建模与背景重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables real-time novel view synthesis for static scenes. Extending it to dynamic scenes via deformation fields has recently attracted significant attention, particularly for dynamic scene reconstructionband distractor-free. However, existing deformation networks lack explicit motion awareness: they neither capture long-term motion intensity nor exploit short-term temporal coherence, leading to inaccurate foreground deformation and pseudo-static residuals in the background. We present MVFusion-GS, a method that enhances deformation networks with two complementary motion-aware mechanisms. The Motion-Variance Guided Refinement aggregates per-Gaussian deformation statistics across time to estimate motion variance and uses it to guide dynamic-static separation during deformation prediction. The MotionFormer Temporal Attention module applies Transformer self-attention over neighboring timesteps to model local motion dependencies and improve temporal consistency. Extensive experiments on both dynamic scene reconstruction and distractor-free reconstruction benchmarks demonstrate state-of-the-art performance, showing that explicit motion awareness improves both foreground motion modeling and static background reconstruction.

  </details>

## 2026-07-02

- **[Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885)**  
  *Kangmin Seo, Sangeek Hyun, MinKyu Lee, Jae-Pil Heo*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00885) · [pdf](https://arxiv.org/pdf/2607.00885.pdf)
  > 💡 针对稀疏视图下3DGS泛化差，使用平坦最小值优化结合各向异性高斯扰动与周期性重初始化，提升新视角合成质量。

  <details><summary>Abstract</summary>

  Recent advances in neural rendering have established 3D Gaussian Splatting (3DGS) as a highly efficient representation for novel view synthesis, enabling fast training and real-time rendering with strong fidelity. However, when supervision is limited to sparse input views, 3DGS tends to overfit to the observed images and generalize poorly to unseen viewpoints. We address this challenge from the perspective of flat minima (FM) optimization, which seeks solutions that remain stable under small parameter perturbations. Viewing Gaussian parameters as trainable weights, we adapt FM principles to the geometric and dynamic nature of 3DGS with a lightweight training framework. Our method regularizes optimization with controlled Gaussian perturbations that account for each Gaussian's anisotropy and the training progress, preserving fine details while improving robustness to sparse-view overfitting. To further stabilize this flat minima optimization process, we introduce periodic reinitialization, which temporarily returns non-positional parameters to their initial states for a short window. Together, these techniques integrate seamlessly into existing 3DGS pipelines without architectural changes. Experiments on LLFF and Mip-NeRF360 datasets demonstrate improved quantitative metrics and perceptual quality under sparse-view supervision, producing reconstructions that are sharper, more stable, and better generalized to novel viewpoints.

  </details>

- **[GADA: Geometry-Aware Deformable Aggregation for Image-Based Gaussian Splatting](https://arxiv.org/abs/2607.00595)**  
  *Siwoo Lim, Sunjae Yoon, Gwanhyeong Koo, Chang D. Yoo*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00595) · [pdf](https://arxiv.org/pdf/2607.00595.pdf)
  > 💡 针对基于扭曲的高斯喷溅存在空间不对齐问题，提出几何感知可变形聚合方法，利用可变形偏移和隐式置信加权恢复局部线索，提升高频质量并加速2.13倍。

  <details><summary>Abstract</summary>

  Gaussian Splatting has achieved significant improvements by incorporating warping-based techniques. However, such methods suffer from pixel-level inaccuracies due to uncertain geometry. This uncertainty leads to spatial misalignments in the warped images, which disrupt residual learning used in warping-based methods and fundamentally limit the gains of correction, particularly on thin structures and high-frequency details. Driven by our insight that useful visual cues are not lost but locally preserved under slight displacement, we propose Geometry-Aware Deformable Aggregation (GADA). This method introduces an iterative refinement module with deformable offsets to actively correct spatial misalignments and recover these displaced cues. Furthermore, to address the limitations of standard pipelines where visibility checks (i.e., thresholding) often discard valid pixels and multi-view warped image fusion relies on naive mean aggregation, our module is coupled with an implicit confidence weighting mechanism that selectively suppresses unreliable evidence. Consequently, our approach outperforms prior warping-based Gaussian Splatting, preserving high-frequency quality while achieving 2.13 times faster FPS.

  </details>

- **[World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video](https://arxiv.org/abs/2607.01202)**  
  *Liyuan Zhu, Shengyu Huang, Amrita Mazumdar, Tianye Li, Zan Gojcic, Gordon Wetzstein, Iro Armeni, Shalini De Mello, Alex Trevithick*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.01202) · [pdf](https://arxiv.org/pdf/2607.01202.pdf)
  > 💡 提出生成式动态高斯重建方法，用视频模型纠正伪影和填补缺失区域，从单目视频生成

  <details><summary>Abstract</summary>

  We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To train this model, we construct a dataset of aligned multiview video pairs and dynamic 3DGS representations, with simulated artifacts characteristic of monocular reconstruction. At test time, we distill the model's generations, including newly observed regions and motions, back into a single consistent, high-quality dynamic 3DGS, improving both novel-view synthesis and the underlying 3D motion. Our method sets a new state of the art in 4D reconstruction and seamlessly generalizes to in-the-wild videos with large viewpoint changes and dynamic motions.

  </details>

- **[CORGI: Consistency-Aware 3D Dog Reconstruction from a Single Image in the Wild](https://arxiv.org/abs/2607.00321)**  
  *Yuxiao Wu, Weile Li, Boyi Zhu, Yumeng Liu, Youcheng Cai, Ligang Liu*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00321) · [pdf](https://arxiv.org/pdf/2607.00321.pdf)
  > 💡 提出一致性感知变形3DGS和生成修复的框架，从单张野外图像无监督重建高保真、可动画化的

  <details><summary>Abstract</summary>

  Reconstructing high-fidelity 3D models of highly articulated animals, such as dogs, from a single in-the-wild image remains a formidable challenge. In this paper, we introduce CORGI, a novel framework for consistency-aware 3D dog reconstruction from a single unconstrained image that completely eliminates the need for 3D supervision. To overcome generative inconsistencies and the lack of multi-view capture, our pipeline introduces three core components. First, we propose a Canonical-Driven Orbital Generation (CDOG) strategy, utilizing specialized Canonical and Orbit LoRAs to normalize arbitrary input poses and synthesize reliable 360-degree video observations. Second, we design a Consistency-aware Deformable 3DGS (CA-3DGS) module that anchors on a D-SMAL prior, explicitly modeling per-view generative errors through dedicated neural deformation fields to learn accurate vertex-level displacements. Finally, to eliminate structural distortions and recover high-frequency details, we introduce a self-supervised Deformation-Conditioned Generative Repair (DCGR) module. Extensive experiments demonstrate that CORGI achieves state-of-the-art performance, generalizing seamlessly across diverse dog breeds to produce geometrically accurate, visually coherent, and fully animatable 3D assets ready for downstream applications.

  </details>

- **[Progressive Pose-Guided 4D Animal Reconstruction from Monocular Video](https://arxiv.org/abs/2607.00157)**  
  *Siyuan Li, Weiying Chen, Yilin Wang, Xinxin Zuo, Xingyu Li, Li Cheng*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00157) · [pdf](https://arxiv.org/pdf/2607.00157.pdf)
  > 💡 针对单目视频4D动物重建的泛化与保真问题，提出基于3D高斯泼溅的渐进姿态引导优化，结合对称编码与可变形场实现高精度跨物种重建。

  <details><summary>Abstract</summary>

  Reconstructing 4D animals from monocular videos is challenging due to large inter-species variation, complex articulations, and the lack of reliable templates. Existing approaches typically rely on either strict category-specific priors that restrict generalization, or unconstrained generative models that sacrifice input fidelity. To bridge this gap, we present a progressive test-time optimization framework built on 3D Gaussian Splatting for high-fidelity 4D animal reconstruction from a single video. Our key insight is that a coarse shape prior suffices when coupled with a progressive strategy that disentangles articulated pose from non-rigid deformation. Specifically, we employ a symmetry-aware temporal encoding that exploits bilateral cues while absorbing camera estimation drift and a part-conditioned deformation mechanism guided by learnable part anchors and a learnable skinning field. Extensive experiments demonstrate that our approach generalizes robustly across diverse species, achieving superior geometric accuracy, temporal consistency, and visual fidelity compared to existing baselines, even under severe prior mismatch.

  </details>

## 2026-07-01

- **[PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](https://arxiv.org/abs/2606.32036)**  
  *Yujie Guo, Yudong Jin, Lingteng Qiu, Zehong Shen, Zhen Xu, Jing Zhang, Xianchao Shen, Hujun Bao, Sida Peng, Xiaowei Zhou*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.32036) · [pdf](https://arxiv.org/pdf/2606.32036.pdf)
  > 💡 通过3D空间预测和点-图像变换器，从输入点集直接推断高斯原语，减少冗余并提升人体重建效率与质量。

  <details><summary>Abstract</summary>

  Producing 3D human representations from input views on the fly is essential for immersive live streaming systems, where representation compactness is as critical as high fidelity given limited computational power and transmission bandwidth. Although recent feed-forward reconstruction methods achieve impressive quality through the view-centric prediction of 3D representations, they repeatedly encode the same subject content across multiple views, leading to significant inter-view redundancy. Our key insight is to perform predictions directly in 3D space, enabling the network to learn and produce a highly compact representation. To this end, we propose PointSplat, a novel human-centric approach that directly infers Gaussian primitives from an input point set. The proposed method first estimates a coarse geometric proxy and performs ray casting to prune redundant points and establish explicit 2D--3D correspondences. Subsequently, it employs a Point-Image Transformer to fuse appearance and geometry features, predicting Gaussian attributes in a single forward pass. This design restricts predictions to foreground regions of interest, substantially reducing the total number of Gaussians while improving novel-view rendering quality. Extensive experiments demonstrate that PointSplat achieves higher efficiency and quality while exhibiting strong robustness to variations in view count and image resolution across multiple datasets.

  </details>

- **[LUNA: Learning Universal 3D Human Animation Beyond Skinning](https://arxiv.org/abs/2606.31981)**  
  *Peng Li, Rawal Khirodkar, Junxuan Li, Yuan Dong, Chen Cao, Yuan Liu, Wenhan Luo, Yike Guo, Shunsuke Saito*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.31981) · [pdf](https://arxiv.org/pdf/2606.31981.pdf)
  > 💡 提出无线性混合蒙皮的通用神经动画模型LUNA，用transformer运动回归器和混合监督实现零样本跨身份3D人体动画。

  <details><summary>Abstract</summary>

  Creating photorealistic, animatable 3D human avatars from monocular images still largely depends on Linear Blend Skinning (LBS) and parametric body models, which constrain expressivity and often introduce artifacts due to imperfect fitting. We propose LUNA, an LBS-free universal neural animation model that directly maps multiple 2D controls like images, keypoints, sketches, and unseen characters into 3D Gaussian deformations, bypassing explicit body fitting. At its core, a transformer-based motion regressor disentangles global rigid motion from fine-grained local dynamics to capture both coherent movement and subtle non-rigid effects. To resolve the inherent ambiguity of 2D-to-3D lifting while scaling beyond fitted datasets, we introduce hybrid supervision that distills soft structural priors from an LBS teacher and a loss that supports training on both limited fitted data and large in-the-wild unlabeled videos. Extensive experiments show LUNA achieves competitive visual fidelity compared to LBS-based approaches, while delivering realistic human motion and zero-shot cross-identity generalization across diverse driving modalities. To the best of our knowledge, LUNA is the first end-to-end 3D animatable model that supports implicit 2D driving.

  </details>

## 2026-06-30

- **[Learning Efficient 4D Gaussian Representations from Monocular Videos with Flow Splatting](https://arxiv.org/abs/2606.29976)**  
  *Shengjun Zhang, Jinzhao Li, Xin Fei, Yueqi Duan*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29976) · [pdf](https://arxiv.org/pdf/2606.29976.pdf)
  > 💡 通过流溅射构建速度场监督动态学习，高效从单目视频重建4D高斯场景，实现更快训练与渲染。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from monocular videos is challenging due to scene complexity and temporal dynamics. With the advancement of 3D Gaussian Splatting in novel view synthesis, existing methods extend 3D Gaussians to 4D domain with deformation fields, trajectories or spatiotemporal 4D volumes to model scene element deformation. However, these methods suffer from long training time, low rendering speed or high memory consumption for per-frame reconstruction of 4D volumes, without fully exploiting dense dynamic information. To address this issue, we propose Flow Splatting, which constructs the velocity field and enables the conventional splatting technique to render optical flow from the velocity field to supervise dynamics learning process from monocular videos. Specifically, we extend 4D volumes with time varying means and covariance to represent complex dynamics. Then, we construct and approximate the velocity field naturally based on this representations. While conventional volume rendering techniques support to render color fields, we extend the volume rendering strategy to splat the velocity field by considering the influence of camera motions. We conduct experiments on various benchmarks to demonstrate the efficiency and effectiveness of our method. Compared to the state-of-the-art methods, our model achieves better image quality with less time consumption and higher rendering speed.

  </details>

- **[FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Sparse Portrait Images](https://arxiv.org/abs/2606.30347)**  
  *Jianjiang Yao, Ke Xian, Renxiang Dai, Robert Caiming Qiu*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30347) · [pdf](https://arxiv.org/pdf/2606.30347.pdf)
  > 💡 从单张或多张稀疏肖像图快速重建可驱动4D头部化身，提出Transformer与3D高斯框架，交替注意力解耦身份与表情，稀疏到稠密学习提升质量。

  <details><summary>Abstract</summary>

  We present FFAvatar, a Transformer-based 3D Gaussian framework for fast construction of high-quality and animatable 4D head avatars from one or more reference portrait images. Unlike existing feed-forward approaches that require a fixed number of input views, FFAvatar supports incremental reconstruction, progressively refining the avatar representation as additional reference images become available. At the core of our method is an alternating attention mechanism that disentangles identity appearance from expression and viewpoint variations, enabling the reconstruction of a canonical 3D appearance that remains consistent across poses and facial expressions. To balance visual fidelity and computational efficiency, we introduce a sparse-to-dense learning paradigm. Coarse appearance features are first learned using sparse primitives anchored to the FLAME vertex level and are subsequently densified in the UV domain to capture fine-grained geometric and texture details. We further propose a plug-and-play motion refinement module that enables subject-specific dynamic personalization by modeling residual motion beyond parametric deformation. Extensive experiments demonstrate that FFAvatar efficiently produces high-fidelity and controllable 4D head avatars, achieving superior flexibility, driving efficiency, and identity-consistent rendering across diverse expressions and viewpoints.

  </details>

- **[DR-GS: Physically-Based Deformable and Relightable 2D Gaussians](https://arxiv.org/abs/2606.29379)**  
  *Jiaxin Li, Tong Wu, Yi Wei, Tailin Wu, Li Zhang*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29379) · [pdf](https://arxiv.org/pdf/2606.29379.pdf)
  > 💡 针对可变形物体光照烘焙和材质编辑难问题，提出解耦几何-光照-材质的可变形重光照高斯框架，

  <details><summary>Abstract</summary>

  Gaussian splatting (GS) has garnered significant attention in VR/AR and digital content creation due to its explicit parameterization and efficient rendering capabilities. However, existing GS-based methods for deformable objects face two key limitations: (i) illumination is erroneously baked into textures, causing physically inconsistent responses under dynamic deformations and lighting changes; (ii) snapshot-based reconstruction restricts post-reconstruction material editing. To address these challenges, we propose Deformable and Relightable GS (DR-GS), a unified Gaussian framework that integrates physically-based inverse rendering, relighting, and deformation-aware manipulation. Through explicitly disentangling geometry, illumination, and material representations, DR-GS overcomes the limitations of static snapshots, resolving unrealistic appearance under varying conditions while enabling post-reconstruction parameter editing. Extensive experiments show that DR-GS achieves leading visual quality across static reconstruction, dynamic deformation, and relighting, reliably preserving reflections and specular highlights on glossy surfaces. It further establishes a fully decoupled geometry-illumination-material pipeline, enabling high-quality 3D asset creation and comprehensive post-editing.

  </details>

- **[L2D2-GS: Learning to Densify for Feedforward Dynamic Gaussian Scene Reconstruction](https://arxiv.org/abs/2606.29374)**  
  *Zetian Song, Chenming Wu, Junnan Liu, Chitian Sun, Liangliang He, Hangjun Ye, Jiaqi Zhang, Siwei Ma, Wen Gao*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29374) · [pdf](https://arxiv.org/pdf/2606.29374.pdf)
  > 💡 针对动态城市场景的高保真重建，提出自监督稠密化策略与几何正则化机制，实现高效零样本泛化，减少原语数量。

  <details><summary>Abstract</summary>

  High-fidelity reconstruction of dynamic urban environments is a cornerstone of autonomous driving simulation and large-scale world modeling. While 3D Gaussian Splatting (3DGS) has established a new standard for real-time rendering, its reliance on expensive per-scene optimization limits scalability. Conversely, recent feedforward methods that infer Gaussian parameters offer faster speed but face fundamental bottlenecks: they are memory-prohibitive at high resolutions and struggle to fuse dense multi-view observations consistently. This paper presents L2D2-GS, a unified framework that reformulates generalizable reconstruction not as a one-shot regression, but as a robust iterative process of optimization and densification. To resolve the ambiguity of supervision in primitive generation, we propose a self-supervised densification policy that derives explicit reward signals from global reconstruction gains to guide local densification. Furthermore, we mitigate irreversible early-stage artifacts through a geometric regularization mechanism, utilizing reparameterization to constrain the optimization manifold and prevent convergence to poor local optima. Extensive experiments on the PandaSet and Waymo datasets demonstrate that our method achieves state-of-the-art reconstruction fidelity and strong zero-shot generalization, while using fewer primitives than competing baselines.

  </details>

- **[RAGA: Real Time Ray Traced Gaussian Shadow Casting for 3DGS Avatar-Scene Interaction](https://arxiv.org/abs/2606.29329)**  
  *Aymen Mir, Riza Alp Guler, Jian Wang, Peter Wonka, Bing Zhou, Gerard Pons-Moll*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29329) · [pdf](https://arxiv.org/pdf/2606.29329.pdf)
  > 💡 针对3DGS虚拟角色阴影问题，提出基于光线-高斯线积分的实时阴影投射方法，无需网格重建，支持多人及物体交互场景。

  <details><summary>Abstract</summary>

  We study the problem of physically plausible shadow casting when animating 3D Gaussian Splatting (3DGS) avatars, either individually or in multi-avatar and object-interaction scenarios, within existing 3DGS scenes. In contrast to prior methods that rely on binary hit tests and mesh-based shadow casters, our method performs shadow computation entirely in Gaussian space, without requiring any mesh reconstruction. We introduce RAGA, a Ray-Traced Gaussian Shadow Casting formulation based on exact ray-Gaussian line integrals. For each occluding Gaussian, we integrate the opacity profile along the shadow ray and normalize by the theoretical maximum integral, producing a weight that captures how the ray traverses the occluder rather than merely whether an intersection occurred. To reduce temporal variance from clothing deformations in animated avatars, we further introduce an avatar proxy representation that stabilizes shadow casting while preserving visual fidelity. We implement RAGA using custom CUDA kernels integrated with the NVIDIA OptiX framework; as such, our shadow tracer runs at rates of about 50 FPS. We evaluate on single-avatar, multi-avatar, and avatar-object interaction scenarios across multiple datasets, demonstrating substantially improved shadow realism, temporal stability, and scene coherence. Our project page is available at https://miraymen.github.io/raga/.

  </details>

- **[Occlusion-Robust Multi-Object Decoupling for Physics-Based Interaction](https://arxiv.org/abs/2606.29303)**  
  *Xin Dong, Wenfeng Deng, Yansong Tang*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29303) · [pdf](https://arxiv.org/pdf/2606.29303.pdf)
  > 💡 无掩码多物体重建，利用3DGS和联合SDS解耦遮挡，结合扩散先验与几何先验，实现物理交互。

  <details><summary>Abstract</summary>

  We propose a mask-free method for lossless multi-object 3D reconstruction from sparse and occluded real-world views, enabling physically plausible interaction via Material Point Method (MPM) simulation. Our key insight is that object coupling stems from occlusion and limited viewpoints, which we address by formulating multi-object decoupling as a sparse-view reconstruction problem. Using 3D Gaussian Splatting as base representation, we first obtain coarse instance partitions with a SAM2-trained segmentation field. Rather than relying on masks, we reconstruct fragmented geometries by leveraging a joint Score Distillation Sampling (SDS) process, which integrates reference-view supervision with novel-view synthesis guided by 2D and 3D diffusion priors to enforce both texture fidelity and 3D consistency. Furthermore, we incorporate geometry-aware priors such as intra-object and inter-object similarity to regularize geometric reasoning. Experimental results demonstrate that our method produces complete, simulation-ready 3D objects without requiring manual masks, enabling realistic dynamic interactions on both synthetic and real-world datasets.

  </details>

- **[MoPe: Motion Permanence for Robust Monocular Gaussian Mapping in Dynamic Environments](https://arxiv.org/abs/2606.29237)**  
  *Qixin Xiao*  
  `2026-06-28` · `cs.RO` · [abs](https://arxiv.org/abs/2606.29237) · [pdf](https://arxiv.org/pdf/2606.29237.pdf)
  > 💡 动态场景下高斯映射易现鬼影，提出运动持续性原则与记忆感知滤波器MoPe，通过历史后验传播与贝叶斯融合提升鲁棒性。

  <details><summary>Abstract</summary>

  Robust robot autonomy depends on scene representations that remain stable enough to support localization, navigation, and downstream decision making in dynamic environments. Monocular Gaussian Splatting SLAM provides high-fidelity mapping, but current uncertainty-aware methods still treat dynamic regions largely as per-frame observations. This makes the representation effectively memoryless: when a pedestrian slows, pauses, or reappears after occlusion, the current frame may look static, allowing dynamic content to be absorbed into the map and leaving persistent ghosting artifacts. We argue that this failure reflects a representation-level mismatch. Dynamic-ness is not an instantaneous appearance property, but a temporal property defined by motion history. Building on this view, we introduce Motion Permanence: the principle that an object's dynamic identity should persist over time rather than be re-decided from each frame independently. We realize this principle in MoPe, a memory-aware uncertainty filter for monocular Gaussian mapping. MoPe propagates the historical dynamic posterior through geometry-consistent SE(3) warping and fuses it with current-frame evidence using bounded Bayesian log-odds updates. The resulting persistent posterior guides tracking, mapping, dynamic-aware Gaussian insertion, and Gaussian-level post-cleanup. On Wild-SLAM, Bonn, and TUM sequences, MoPe improves tracking robustness and reduces residual ghosting, with the strongest gains on dynamic-human scenes that most directly violate the memoryless assumption. These results show that maintaining temporal dynamic state inside the scene representation is a practical step toward more reliable representation-centric autonomy in changing real-world environments.

  </details>

- **[HiReFF: High-Resolution Feedforward Human Reconstruction from Uncalibrated Sparse-View Video](https://arxiv.org/abs/2606.29333)**  
  *Yiming Jiang, Hanzhang Tu, Wenfeng Song, Siyou Lin, Liang An, Shuai Li, Aimin Hao, Yebin Liu*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29333) · [pdf](https://arxiv.org/pdf/2606.29333.pdf)
  > 💡 提出无标定稀疏视频下2K人体重建方法HiReFF，用尺度同步标定和前景掩码处理模糊性，高分辨率侧调优降低计算开销。

  <details><summary>Abstract</summary>

  Uncalibrated volumetric video streaming for human reconstruction is essential for holographic communication and AR/VR, yet remains challenging due to the need for temporal consistency and computational efficiency from sparse-view inputs. Existing methods rely on per-scene optimization or calibrated cameras, while recent feed-forward models are limited to low-resolution (0.5K) single-frame synthesis. We present HiReFF, a feed-forward method for 2K-resolution 360° human video reconstruction from uncalibrated sparse-view videos. Our framework decomposes the problem into two key tasks: foreground 3D Gaussian reconstruction from sparse-view videos (four views separated by 90°) and computationally efficient high-resolution synthesis. To enable the former, we propose Scale-synchronized Camera Calibration to resolve scale ambiguity for multi-view supervision, and Gaussian-wise Foreground Masking to reconstruct clean foregrounds by modulating Gaussian parameters. For efficient high-resolution synthesis, our High-resolution Side-tuning achieves 2K rendering by augmenting the Gaussian head with supplementary features while keeping the backbone at 0.5K, drastically reducing computational overhead. Experiments demonstrate that HiReFF significantly outperforms existing methods in high-resolution streaming volumetric video reconstruction. https://iridescentjiang.github.io/HiReFF

  </details>

- **[DLGStream: Dynamic Language-embedded Guassian Splatting for Open-vocabulary Enabled Free-viewpoint Video Streaming](https://arxiv.org/abs/2606.28840)**  
  *Zhihui Ke, Yuyang Liu, Xiaobo Zhou, Tie Qiu*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28840) · [pdf](https://arxiv.org/pdf/2606.28840.pdf)
  > 💡 提出双不透明度动态语言高斯表示和插值变形场，实现低帧大小高帧率的开放词汇自由视点视频流。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting~(3DGS) has emerged as a promising paradigm for reconstructing streamable free-viewpoint video~(FVV) from multi-view videos. However, 3DGS-based FVVs typically lack user interaction and editing capabilities, which diminishes the immersive experience. Recent research has integrated language features from CLIP into 3DGS via distillation, enabling open-vocabulary queries and supporting many downstream applications. Nevertheless, the stringent requirements of FVV, low frame size and high FPS, make current language Gaussian representations unsuitable for language-embedded FVV. In this paper, we propose DLGStream, a novel language-embedded FVV representation that streams time-varying language features alongside Gaussian attributes to support 4D environment interaction, scene editing, and spatial intelligence. Specifically, we propose a dual-opacity dynamic language Gaussian representation, which maintains two opacity attributes for color and language features to deal with performance degradation that occurs when colors and features are jointly optimized. Furthermore, we introduce an interpolation-based deformation field to reduce temporal redundancy. This deformation field can also be used for 4D frame interpolation, boosting FVV sequences from low to high FPS. Experimental results demonstrate that DLGStream achieves superior performance in both on open-vocabulary segmentation and reconstruction quality with an average frame size of merely 43 KB. The code is available on \href{https://github.com/kkkzh/DLGStream}{https://github.com/kkkzh/DLGStream}.

  </details>

- **[Ground4D: Consistency-Aware 4D Reconstruction from Monocular Video](https://arxiv.org/abs/2606.28828)**  
  *Qing Zhao, Weijian Deng, Pengxu Wei, Liang Lin*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28828) · [pdf](https://arxiv.org/pdf/2606.28828.pdf)
  > 💡 用3D基础模型初始化几何，结合动态高斯泼溅进行几何一致性优化，实现单目视频的高保真4D重建与渲染。

  <details><summary>Abstract</summary>

  Learning a 4D scene representation from a single monocular video that supports dynamic novel-view synthesis while maintaining faithful geometry over time remains challenging. Dynamic Gaussian Splatting achieves strong rendering performance through photometric optimization, yet does not explicitly enforce multi-view geometric consistency. In contrast, 3D foundation models recover coherent scene geometry and camera motion, but their point-based outputs are not designed for photorealistic rendering. We propose Ground4D, a geometry-grounded framework built on two stages. First, we perform geometry initialization via 3D foundation models, leveraging VGGT in a training-free manner to reconstruct multi-view-consistent 3D geometry and camera poses from monocular video. The recovered geometry provides a structured and reliable initialization for dynamic Gaussian representations. Second, we conduct geometry-consistency-aware refinement via dynamic Gaussian Splatting, optimizing the representation through differentiable rendering while maintaining multi-view geometric consistency across both observed and synthesized viewpoints. Furthermore, Ground4D inherently models the continuous 4D dynamics of the scene, naturally supporting rendering at arbitrary timestamps. By integrating foundation-level geometric priors into dynamic Gaussian optimization, Ground4D achieves stronger reconstruction fidelity and rendering performance, underscoring the role of geometry-grounded constraints in robust 4D scene modeling.

  </details>

- **[CoGS: Compositional Dynamic Human-Object Scenes Gaussian Splatting from Monocular Video](https://arxiv.org/abs/2606.28820)**  
  *Jerrin Bright, John Zelek*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28820) · [pdf](https://arxiv.org/pdf/2606.28820.pdf)
  > 💡 用组合高斯泼溅分解单目视频中人、物、背景，经六阶段优化提升动态交互场景重建质量。

  <details><summary>Abstract</summary>

  Reconstructing dynamic human--object interaction scenes from monocular video is difficult because the human, manipulated object, and background obey different motion models while sharing the same pixels. Existing dynamic radiance-field and Gaussian-splatting methods often entangle these components, causing object motion to leak into the human or static scene, and monocular human reconstruction remains underconstrained in regions that are rarely observed. We present CoGS, a compositional Gaussian-splatting framework for monocular human--object scene reconstruction. CoGS decomposes the video into three coordinated branches: an articulated human initialized from a complete canonical prior, a rigid object field driven by an estimated object trajectory, and a static scene field regularized by weak scene-only planar primitives when available. A six-stage optimization schedule first stabilizes the human and object independently, then fuses them with the scene under full-image supervision, visibility-aware human anchoring, object silhouette and motion constraints, and delayed scene regularization. This design keeps each component responsible for its own geometry and motion while allowing photometric evidence to correct the final composite. Experiments on HOSNeRF and NeuMan show that CoGS improves both human--object interaction reconstruction and in-the-wild human--scene rendering, achieving stronger fidelity and perceptual quality across full-frame and human-focused evaluations. Code will be released upon publication.

  </details>

- **[SemDynReg: Semantics-Guided Deformation Regularization for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.28656)**  
  *Ruitao Chen, Mozhang Guo, Jinge Li*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28656) · [pdf](https://arxiv.org/pdf/2606.28656.pdf)
  > 💡 利用SAM提取语义引导对象级变形正则化，解决动态3DGS中对象变形不一致问题，提升渲染质量。

  <details><summary>Abstract</summary>

  Deformable 3D Gaussian Splatting (3DGS) has emerged as an efficient approach for rendering dynamic scenes in a wide range of 3D applications. However, existing deformation field-based approaches largely lack explicit object-level modeling, often resulting in inconsistent Gaussian deformations within individual objects and unwanted coupling between different objects. To address this limitation, we introduce a semantics-guided framework that enforces dynamic regularization at the object level, aiming to achieve spatially consistent object-wise deformation. Specifically, we first extract segmentation masks using the Segment Anything Model (SAM) and derive semantic features from input images. An object-ID map is then constructed via feature relevance matching with a predefined object dictionary. Guided by this object-ID map, we identify the pixel-wise top-k contributing Gaussians for each object and impose consistency regularization on their deformation parameters, including position, scale, and rotation. Unlike prior methods that learn deformation fields without explicit object-level constraints, our approach incorporates semantic cues to guide deformation behavior at the object level. Experimental results demonstrate that our semantics-aware regularization improves object-level deformation consistency and outperforms baseline methods in rendering quality, achieving higher PSNR and SSIM and lower LPIPS in dynamic 3DGS rendering. Our project page is available at https://dyn-reg-3dgs.github.io/.

  </details>

## 2026-06-25

- **[TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy](https://arxiv.org/abs/2606.26092)**  
  *Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang*  
  `2026-06-24` · `cs.CV` · [abs](https://arxiv.org/abs/2606.26092) · [pdf](https://arxiv.org/pdf/2606.26092.pdf)
  > 💡 通过可渲染4D试穿代理显式解耦人与环境，首个统一DiT框架实现任意相机轨迹下的逼真视频虚拟试穿。

  <details><summary>Abstract</summary>

  While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.

  </details>

## 2026-06-24

- **[OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis](https://arxiv.org/abs/2606.24799)**  
  *Chenrui Fan, Paolo Favaro*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24799) · [pdf](https://arxiv.org/pdf/2606.24799.pdf)
  > 💡 用冻结视频先验与高斯泼溅重建锚定，将单视频补全为闭轨3D场景，无需微调或蒸馏，提升视图覆盖率与一致性。

  <details><summary>Abstract</summary>

  Generic text-to-video models can be used as rich open-world scene priors. Despite the high quality of today's generated videos, they do not directly yield reliable 3D assets: camera motion is difficult to control, view coverage is partial, and frames often contain inconsistencies across time. We introduce OrbitForge, an adapter built from frozen video priors and per-prompt Gaussian Splatting reconstruction optimization that converts a single text-generated video into a canonical closed-orbit 3D Gaussian Splatting scene. We use 3D reconstruction as an anchor to improve the 3D consistency of the generated video. We obtain a preliminary 3D reconstruction from a first generated video via Deformable Gaussian Splatting with a robust MedianGS proxy. We render views from a prescribed orbit to detect missing viewpoints. OrbitForge uses the text-to-video model to complete only the missing views, and reconstructs the completed orbit into a final Gaussian Splatting scene. This design requires no task-specific video or multiview fine-tuning, avoids per-prompt score-distillation optimization, and does not progressively generate views one step at a time. We further argue that this setting demands coverage-aware evaluation: local smoothness alone rewards methods that never attempt a full orbit. On a frozen 300-prompt T3Bench-derived audit, OrbitForge reconstruction attains a 359.0-degree measured median span, raises originally unsupported-bin Q10 ImageReward from 8.07 to 16.36 relative to MedianGS-only reconstruction, while remaining competitive with VideoMV on the coverage-quality.

  </details>

## 2026-06-23

- **[Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild](https://arxiv.org/abs/2606.23688)**  
  *Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23688) · [pdf](https://arxiv.org/pdf/2606.23688.pdf)
  > 💡 通过因果潜在条件适应单视图3D重建生成时序一致初始预测，再经遮挡感知优化和扩散先验细化，显著提升大变形和遮挡下的4D重建质量。

  <details><summary>Abstract</summary>

  Reconstructing dynamic non-rigid objects from monocular video requires integrating visual cues from direct observations with data-driven priors over geometry and appearance. Prior approaches either learn to directly predict 4D representations from visual input or initialize a 3D representation that is subsequently deformed and refined based on video evidence. However, the former are constrained by the scarcity of 4D training data, while the latter leverage priors only for the initial reconstruction and rely solely on video supervision thereafter; neither handles complex in-the-wild scenarios with large deformations and occlusions well. We present Lift4D, a test-time optimization framework that addresses both limitations. First, we adapt an existing single-view 3D reconstruction model to yield temporally consistent per-frame predictions via causal latent conditioning, providing a coherent initialization for a deformable 3D Gaussian Splatting representation. We then ``sculpt'' this representation to match the input video through an occlusion-aware optimization that faithfully recovers visible surface details while completing unobserved regions using a view-conditioned diffusion prior. We demonstrate that Lift4D clearly improves over prior 4D reconstruction methods, particularly on challenging in-the-wild sequences with severe occlusions and non-rigid motion.

  </details>

- **[MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455)**  
  *Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui*  
  `2026-06-22` · `cs.CV` · [abs](https://arxiv.org/abs/2606.23455) · [pdf](https://arxiv.org/pdf/2606.23455.pdf)
  > 💡 针对现有物理仿真忽略温度场的问题，提出MeGAS将热力学相变融入3DGS，实现物理一致的热力学场景编辑与高保真渲染。

  <details><summary>Abstract</summary>

  Recent advances integrate physically grounded Newtonian dynamics with neural rendering frameworks, narrowing the gap between photorealistic scene reconstruction and physics-based animation. However, existing approaches focus on mechanically driven dynamics while neglecting temperature, a fundamental yet invisible physical factor underlying phenomena such as melting, solidification, and other thermomechanical processes. In this paper, we propose MeGAS, a novel framework that incorporates thermomechanical phase-change dynamics into 3D Gaussian Splatting (3DGS). Specifically, we propose a new thermomechanical dynamic Gaussian Splatting representation that augments 3DGS with temperature attributes and employs a heat advection-diffusion solver with MPM dynamics incorporating phase transitions, enabling physically plausible and visually realistic synthesis of thermophysical phenomena. Furthermore, a new topology-adaptive Gaussian rendering strategy is proposed to mitigate cracking and floaters under extreme deformation. Extensive experiments demonstrate that MeGAS produces physically consistent thermomechanical behavior while maintaining high-fidelity photorealistic rendering, advancing toward physics-integrated world models.

  </details>

- **[Multi4D: High-Fidelity Dynamic Gaussian Splatting via Multi-Level Competitive Allocation](https://arxiv.org/abs/2606.22197)**  
  *Rui Wang, Quentin Lohmeyer, Siyu Tang, Mirko Meboldt*  
  `2026-06-20` · `cs.CV` · [abs](https://arxiv.org/abs/2606.22197) · [pdf](https://arxiv.org/pdf/2606.22197.pdf)
  > 💡 针对动态高斯喷溅中运动一致性与视觉保真度的矛盾，提出多级竞争分配框架，显著提升渲染质量并保持实时性。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian splatting faces a fundamental tension between motion consistency and visual fidelity. Deformation-based approaches preserve temporal correspondence but suffer from motion over-factorization, oversmoothing high-frequency dynamics. In contrast, 4D-primitive methods capture fine visual details yet incur temporal overparameterization, breaking object identity and leading to severe storage overhead. To resolve this, we introduce Multi4D, a framework for high-fidelity dynamic Gaussian Splatting based on multi-level competitive allocation. Instead of a monolithic representation, we distribute modeling capacity across three structured levels: static structure, persistent dynamic geometry, and transient appearance primitives. Through shared rasterization and residual-driven optimization, these levels dynamically compete to explain photometric error, enabling adaptive specialization without pre-assigned decomposition. This allocation preserves long-term motion consistency while capturing fine dynamic detail, achieving state-of-the-art rendering quality and real-time performance with significantly fewer dynamic primitives. Furthermore, because our representation explicitly tracks compact persistent Gaussians over time, semantic features can be embedded afterward, enabling Multi4D to achieve state-of-the-art 4D segmentation accuracy with an order-of-magnitude speedup. Project page: https://batfacewayne.github.io/Multi4D.io/

  </details>

- **[Scene-Level Heterogeneous Physics Simulation with 3D Gaussian Splats](https://arxiv.org/abs/2606.21753)**  
  *Xiaoyang Liu, Shangzhe Wu, Kai Han*  
  `2026-06-19` · `cs.GR` · [abs](https://arxiv.org/abs/2606.21753) · [pdf](https://arxiv.org/pdf/2606.21753.pdf)
  > 💡 将3DGS等异构资产统一为物理粒子集，首次实现场景级多求解器物理模拟与非刚性变形。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has achieved state-of-the-art photorealistic rendering, but the representation gap prevents these assets from being physically interactive. Production-grade physics engines do not understand the 3DGS representation, while prior physics-for-3DGS methods are monolithic silos. These prior works are fundamentally limited, demonstrating only object-centric physics in isolated environments, such as on an ideal plane. They are incapable of interacting with complex static collision geometry or heterogeneous assets. We propose a novel framework that, for the first time, bridges this gap by enabling 3DGS assets to participate in scene-level, heterogeneous, multi-solver physical simulations. Our core contribution is a Representation Abstraction Framework that translates all diverse assets, including 3DGS, virtual meshes, and fluids, into a unified physical particle set. This abstraction is key to enabling complex behaviors, such as the non-rigid deformation of 3DGS assets, within a unified physics pipeline. This particle set, along with the static scene collision boundaries derived from scene capture, is processed within a solver-agnostic physics kernel. The physical results are then mapped back to drive each asset's specific visual reconstruction. This architecture unlocks capabilities impossible with prior art. We demonstrate complex, two-way interactions between deformable 3DGS assets, standard CG assets such as fluids and meshes, and large-scale captured static environments, showcasing realistic coupled phenomena that were previously unattainable.

  </details>

## 2026-06-18

- **[Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos](https://arxiv.org/abs/2606.19156)**  
  *Jeongmin Bae, Seoha Kim, Marc Pollefeys, Mahdi Rad, Youngjung Uh, Taein Kwon*  
  `2026-06-17` · `cs.CV` · [abs](https://arxiv.org/abs/2606.19156) · [pdf](https://arxiv.org/pdf/2606.19156.pdf)
  > 💡 首个前馈框架通过网格引导和时间卷积从第一视角视频重建动态4D手部，实现快速推理与强泛化。

  <details><summary>Abstract</summary>

  Dynamic 3D hand reconstruction from egocentric videos is essential for next-generation computing platforms such as AR/VR and AI glasses. Despite its importance, most prior works focus either on multi-view 3D hand reconstruction or on 4D human body reconstruction. Egocentric 4D hand reconstruction remains challenging due to fast head motion, rapid hand dynamics, severe occlusions, and inherent ambiguity from single-view observations. To address these challenges, we introduce Hand-4DGS, the first feed-forward framework for reconstructing dynamic 4D hands directly from egocentric videos, enabling both fast (~60 FPS) inference and strong generalization. Our approach incorporates a mesh-guided representation for structural priors and temporal convolutions to model dynamic motion. We evaluate our framework on two challenging egocentric datasets, H2O and ARCTIC, and demonstrate significant improvements over baselines. Our method benefits from the generalization capability of feed-forward networks and effective 2D image supervision through Gaussian splatting, without requiring expensive 3D hand pose ground-truth annotations.

  </details>

- **[Intrinsic 4D Gaussian Segmentation from Scene Cues](https://arxiv.org/abs/2606.18623)**  
  *Hasan Yazar, Mohamed Rayan Barhdadi, Erchin Serpedin, Mehmet Tuncel, Hasan Kurban*  
  `2026-06-17` · `cs.CV` · [abs](https://arxiv.org/abs/2606.18623) · [pdf](https://arxiv.org/pdf/2606.18623.pdf)
  > 💡 利用高斯原语自身的外观、形变轨迹等线索构建亲和图并进行社区检测，实现无需掩码和训练的4D高斯分割，速度提升12.5倍且精度与监督方法相当。

  <details><summary>Abstract</summary>

  Dynamic 4D Gaussian Splatting reconstructs deforming scenes with high fidelity and is increasingly adopted as a representation for dynamic 3D scenes. Putting such a scene to use, for editing, manipulation or motion analysis, first requires segmenting it: grouping the Gaussian primitives into coherent objects. Current pipelines obtain this grouping by importing 2D masks from foundation models such as SAM and lifting or distilling them into the Gaussian representation. In dynamic scenes these masks must be generated across many frames and views, which is costly, and the resulting segmentation can depend strongly on the quality and consistency of those external masks. We ask how much object-level structure can instead be recovered from the Gaussians themselves, and propose Intrinsic-GS, a training-free, mask-free method that builds a sparse affinity graph over Gaussian primitives from appearance, orientation, scale, deformation-trajectory and non-learned rendered-boundary cues. The graph is partitioned with Leiden community detection, requiring no foundation model and no learned feature field. On the standard 4D Gaussian segmentation benchmarks, Neu3D and HyperNeRF, Intrinsic-GS recovers substantial object structure without mask supervision, reaching 0.746 mIoU on Neu3D and 0.575 on HyperNeRF; on Neu3D, a geometry-only variant reaches 0.902 mIoU, matching SAM-supervised TRASE. On HyperNeRF, Intrinsic-GS runs 12.5x faster than the mask-generation and feature-rendering stages used by mask-supervised pipelines. These results suggest that much of the segmentation signal is already encoded in the Gaussians themselves, offering a fast, mask-free direction for 3D and 4D Gaussian segmentation that may also point toward more generalizable, robust segmentation in settings where external masks are unreliable or expensive.

  </details>

- **[Edit3DGS: Unified Framework for Dynamic Head Editing via 2D Instruction-Guided Diffusion and 3D Gaussian Splatting](https://arxiv.org/abs/2606.17432)**  
  *Duy-Dat Tran, Trung-Nghia Le*  
  `2026-06-16` · `cs.GR` · [abs](https://arxiv.org/abs/2606.17432) · [pdf](https://arxiv.org/pdf/2606.17432.pdf)
  > 💡 利用2D指令扩散与3D高斯泼溅，实现动态头部编辑的统一框架，支持时域一致的高保真编辑。

  <details><summary>Abstract</summary>

  We present Edit3DGS, a unified framework for dynamic 3D head editing that integrates 2D instruction-guided diffusion with 3D Gaussian splatting. Unlike prior approaches that separately address frame-based edits or static 3D reconstruction, our method couples semantic controllability in the image domain with photorealistic, temporally consistent 3D representations. Given an input video, editable facial regions are masked and modified using a text-conditioned diffusion model to support fine-grained operations such as expression transformation, attribute modification, and appearance refinement. The edited frames are then aggregated through 3D Gaussian splatting to produce a coherent, high-fidelity avatar that preserves both identity and motion dynamics. To enforce consistency, Edit3DGS incorporates multi-view batch editing and lightweight inpainting strategies that recover lost expressions across timesteps. Experimental results demonstrate that our framework enables controllable, artifact-free head editing with smooth temporal transitions, offering practical applications in virtual avatars, immersive communication, film production, and interactive media.

  </details>

- **[Renderable Partial Representations for Dynamic Gaussian Splatting under Incomplete Delivery](https://arxiv.org/abs/2606.17212)**  
  *Faruk Alpay, Levent Sarioglu, Yaser Hadri*  
  `2026-06-15` · `cs.GR` · [abs](https://arxiv.org/abs/2606.17212) · [pdf](https://arxiv.org/pdf/2606.17212.pdf)
  > 💡 动态高斯溅射面临部分传输不可渲染问题，提出时空聚类与反事实效用层优化可渲染部分表示，显著改善质量退化。

  <details><summary>Abstract</summary>

  Dynamic Gaussian compression is normally optimized for complete files or complete progressive prefixes, but interactive rendering encounters partial representations: some spatiotemporal regions are present, others missing, and late refinements cannot affect the displayed frame. We study dynamic Gaussian representations whose incomplete delivery states remain directly renderable and whose degradation is optimized in image space. Gaussian primitives are organized into independently addressable spatiotemporal clusters with a base level and three refinements; training samples partial dependency graphs, renders many counterfactual states in one GPU batch, and minimizes expected distortion, tail distortion, temporal inconsistency, rate, and prefix regressions. A counterfactual utility layer measures the marginal render contribution of each completion group across valid receiver contexts. The same graph admits a concrete delivery realization with MTU-bounded entropy-coded chunks, deadline-aware scheduling, and receiver-side dependency closure. On held-out views, the finest refinement has negative mean marginal utility in 3/32 D-NeRF bouncingballs, 49/64 HyperNeRF broom2, and 28/64 HyperNeRF chicken clusters; its lower-tail utility is negative in 21/32, 61/64, and 42/64 clusters, respectively. On broom2, render-utility ordering removes both PSNR regressions produced by nominal layer order at matched byte budgets; on chicken, utilities measured on disjoint training cameras improve held-out PSNR by 3.03 dB at the lowest matched budget. These scoped results show why nominal refinement order cannot substitute for render-conditioned utility: the formulation treats network delivery as a distribution over renderable scene states rather than as an external wrapper around a graphics codec.

  </details>

## 2026-06-16

- **[RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278)**  
  *Zhenhua Wu, Yun Pang, Mingkun Chang, Yuwei Ning, Liangzhi Wang, Yi Xiao, Guanbin Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16278) · [pdf](https://arxiv.org/pdf/2606.16278.pdf)
  > 💡 针对可编辑3DGS仿真视频与现实差距，提出RealityBridge，利用多模态控制和门控网络改善伪影、光照和

  <details><summary>Abstract</summary>

  Long-tail hazardous scenarios are essential for safety-oriented autonomous driving, yet they are difficult to collect and reproduce at scale. Editable 3D Gaussian Splatting (3DGS) simulation offers a promising alternative by reconstructing real driving scenes and supporting controllable scene editing. However, edited 3DGS-rendered videos still suffer from a significant Sim-to-Real gap, including rendering artifacts, degraded foreground assets, inconsistent illumination, and temporal flickering. Existing restoration and video generation methods are insufficient for this task, as they often fail to jointly repair 3DGS-specific artifacts, improve visual realism, and ensure temporal consistency. To fill this gap, we propose RealityBridge, a structure-preserving and asset-aware Sim-to-Real framework for edited 3DGS driving videos. RealityBridge uses multimodal controls, including rendered videos, foreground masks, edge maps, and semantic masks, together with a lightweight GateNet for adaptive condition allocation across backbone layers. We further construct targeted training data and introduce autoregressive long-video training with reward-guided post-training to improve restoration quality, temporal stability, and hallucination suppression. Extensive experiments on internal and public driving datasets show that RealityBridge outperforms existing methods in artifact removal, illumination harmonization, and long-sequence temporal consistency.

  </details>

- **[EmoZone-Talker: Regional Semantic Control of Audio-Driven 3DGS Talking Heads via Facial Action Units](https://arxiv.org/abs/2606.15848)**  
  *Tingting Chen, Shaojun Wang, Huaye Zhang, Diqiong Jiang, Chenglizhao Chen*  
  `2026-06-14` · `cs.CV` · [abs](https://arxiv.org/abs/2606.15848) · [pdf](https://arxiv.org/pdf/2606.15848.pdf)
  > 💡 提出了EmoZone-Talker，利用区域语义解耦AU编码，实现音频驱动3DGS说话头的精细表情控制，提升上脸精度和时间一致性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has shown strong potential for high-fidelity talking head synthesis. However, enabling fine-grained, interpretable, and editable facial expression control remains fundamentally challenging due to intrinsic conflicts between speech-driven facial dynamics and explicit expression signals. Existing methods rely on implicit multimodal fusion, leading to spatial entanglement and temporal instability. We present EmoZone-Talker, a novel framework that reformulates audio-driven facial animation as a structured spatial-temporal coordination problem under cross-modal conflicts. Our approach introduces an explicit spatial disentanglement and temporal dynamics modeling of facial motion. Specifically, we propose Synergy Zones with Prioritized Attention Bias (SZ-PAB) to explicitly decouple modality contributions via region-wise constraints guided by anatomical priors, and a Channel-Independent Temporal AU Encoder (CIT-AE) to model temporally coherent AU dynamics. By integrating these representations into 3D Gaussian deformation, EmoZone-Talker enables precise and interpretable control over facial expressions. Extensive experiments demonstrate that our method improves expression controllability and realism, with notable gains in upper-face accuracy and temporal coherence, while preserving high rendering quality and accurate lip synchronization. Code will be publicly released to facilitate reproducibility and further research.

  </details>

## 2026-06-12

- **[Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction](https://arxiv.org/abs/2606.13655)**  
  *Jen-Hao Cheng, Yipeng Wang, Hao Zhang, Gengshan Yang, Jenq-Neng Hwang*  
  `2026-06-11` · `cs.CV` · [abs](https://arxiv.org/abs/2606.13655) · [pdf](https://arxiv.org/pdf/2606.13655.pdf)
  > 💡 提出Flex4DHuman，用相对相机姿态编码的多视角视频扩散模型，无需几何先验，从单目视频生成动态4D高斯

  <details><summary>Abstract</summary>

  We present Flex4DHuman, a multi-view video diffusion model that transforms a monocular or sparse multi-view video of a dynamic subject into synchronized dense multi-view videos using only relative camera-pose conditioning. Unlike prior human-centric methods that rely on skeletons, depth maps, normals, or rendered target-view geometry, Flex4DHuman requires no explicit geometry priors and instead conditions generation through relative camera-pose positional encoding. The generated videos can be directly ingested by downstream reconstruction pipelines to create dynamic 4D Gaussian splats. Built on the Wan 2.1 1.3B text-to-video model, Flex4DHuman preserves the backbone architecture and encodes camera and view information through a five-axis positional encoding that extends spatio-temporal RoPE with view indices and continuous SE(3) relative camera geometry. A three-stage curriculum progressively trains the model for pose following, flexible reference-to-target view generation, and temporal rollout. To support temporal rollout, we train with clean historical target-view tokens. We also add multi-view captions to enable test-time text control. Combined with an off-the-shelf 4D Gaussian Splatting stage, our framework lifts monocular static-camera videos into dynamic 4D Gaussian splats. Experiments on DNA-Rendering and ActorsHQ show that Flex4DHuman surpasses prior state-of-the-art methods, while the same formulation generalizes to animal categories after mixed human-animal training. These capabilities make Flex4DHuman a practical step toward scalable 4D content creation from casual monocular videos for simulation, gaming, AR/VR, and video re-shooting.

  </details>

- **[MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold](https://arxiv.org/abs/2606.13376)**  
  *Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu, Jun Liang, Shengfeng He, Jing Li*  
  `2026-06-11` · `cs.CV` · [abs](https://arxiv.org/abs/2606.13376) · [pdf](https://arxiv.org/pdf/2606.13376.pdf)
  > 💡 用单张窄视场图像，通过全景扩散和3D高斯支架构建，再经条件视频生成器实时渲染，支持8FPS交互漫游。

  <details><summary>Abstract</summary>

  We present MoVerse, a real-time video world model that creates an interactively navigable scene from a single narrow-field-of-view image. This setting is challenging because the input observes only a small fraction of the environment, while interactive roaming requires a complete surrounding world, persistent geometry, controllable camera motion, and temporally coherent high-fidelity observations. MoVerse addresses this problem by separating world construction from observation rendering. It first expands the input into a gravity-aligned 360$^\circ$ panorama with topology-aware diffusion, closing the missing field of view before 3D reasoning. It then lifts the panorama into a persistent 3D Gaussian scaffold using panoramic geometry-aware residual prediction, yielding a dense and directly renderable spatial memory. Finally, a Gaussian-conditioned video renderer translates scaffold renderings along user-specified camera trajectories into photorealistic video. To make this renderer practical for interaction, we train a bidirectional diffusion teacher for high-quality conditional rendering and distill it into a causal autoregressive student for bounded-latency streaming. This design combines the controllability and long-range consistency of explicit 3D representations with the perceptual quality of generative video models. MoVerse supports real-time scene roaming at 8~FPS on a single NVIDIA RTX~4090 GPU, demonstrating a practical path toward single-image world creation with interactive video output.

  </details>

## 2026-06-11

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

## 2026-06-10

- **[Envision4D: Envisioning Visual Futures via Feed-forward 4D Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2606.10656)**  
  *Qi Song, Yifei He, Chi Zhang, Zheng Fu, Xuhe Zhao, Mengmeng Yang, Kun Jiang, Rui Huang, Diange Yang*  
  `2026-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2606.10656) · [pdf](https://arxiv.org/pdf/2606.10656.pdf)
  > 💡 提出自监督前馈4D高斯泼溅框架，结合未来姿态预测与条件运动提升，解决自动驾驶外推重影伪影，实现SOTA未来视图合成。

  <details><summary>Abstract</summary>

  Forecasting the future evolution of dynamic scenes is crucial in autonomous driving. However, existing feed-forward paradigms are primarily designed for interpolation. When extended to future extrapolation, they suffer from ghosting artifacts under large displacements and are constrained by simplified motion assumptions or strict future priors. To overcome these challenges, we propose Envision4D, a fully self-supervised feed-forward framework for pose-free future extrapolation. Specifically, we introduce a Future Pose Prediction module that infers future camera parameters via an iterative denoising process. Furthermore, to capture non-linear dynamics, we propose In-layer Temporal Attention and employ Conditioned Motion Lifting, which transforms the highly uncertain extrapolation process into robust relational mappings. Finally, a Progressive Training Strategy is utilized to stabilize unsupervised motion learning against error accumulation. Extensive experiments demonstrate that Envision4D achieves state-of-the-art performance, significantly outperforming existing methods in future view synthesis.

  </details>

- **[ManiSplat: Manipulation Trajectory Synthesis from Monocular Video via Decoupled 3D Gaussian Splatting](https://arxiv.org/abs/2606.10645)**  
  *Wenhao Hu, Haonan Zhou, Liu Liu, Yun Du, Xinjie Wang, Ziang Li, Zhizhong Su, Gaoang Wang*  
  `2026-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2606.10645) · [pdf](https://arxiv.org/pdf/2606.10645.pdf)
  > 💡 通过图结构解耦表示和任务导向时空对齐，从单目视频重建高保真可控的动态交互场景，支持下游机器人任务。

  <details><summary>Abstract</summary>

  Reconstructing dynamic and interactive 3D scenes from real-world observations remains a fundamental challenge in computer vision and robotics. While recent advances in 3D Gaussian Splatting have enabled high-fidelity static reconstruction, extending it to interactive environments with articulated robots and manipulable objects remains difficult due to complex contact interactions and abrupt pose changes. To address these challenges, we introduce ManiSplat, a unified framework that reconstructs controllable and decoupled Gaussian digital twins directly from monocular ego-view robotic videos. Our method introduces a Graph-Structured Disentangled Representation that separates the robot, objects, and background into independently optimizable Gaussian subfields organized within a scene graph. To ensure stability, we propose a Task-Oriented Spatio-Temporal Alignment module that leverages the inherent logic of manipulation tasks-alternating between Motion and Skill phases-to construct accurate pseudo-ground-truth trajectories. Finally, a joint photometric-geometric optimization ensures the reconstructed scenes are temporally coherent, physically consistent, and simulation-ready. Extensive experiments demonstrate that our approach reconstructs interaction-driven dynamic scenes with high fidelity and controllability, effectively supporting downstream robotic tasks and policy learning.

  </details>

## 2026-06-09

- **[Liquid Neural Networks as a Drop-in Continuous-Time Deformation Field for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.07670)**  
  *Mingzhao Li, Arghya Pal, Guan Yuan Tan*  
  `2026-06-04` · `cs.CV` · [abs](https://arxiv.org/abs/2606.07670) · [pdf](https://arxiv.org/pdf/2606.07670.pdf)
  > 💡 用液态神经网络替代MLP变形场，实现显式连续时间平滑动态场景重建。

  <details><summary>Abstract</summary>

  Deformable 3D Gaussian Splatting (D-3DGS) re-constructs dynamic scenes from monocular video by deforming a canonical set of 3D Gaussians through a positional-encoded MLP of frame time t. Although fitted to a continuous variable, the MLP couples no two values of t in its architecture and effectively predicts discrete per-frame offsets, leaving temporal smoothness to emerge only as a byproduct of optimisation. We redesign the deformation field as a stack of Closed-form Continuous-time (CfC) cells, a Liquid Neural Network (LNN), that is the closed-form solution of the Liquid Time-constant ODE while preserving every other part of the D-3DGS pipeline. Each cell exposes a sigmoidal time gate that interpolates between two candidate hidden states, baking a learned smooth response to t into the loss landscape without invoking any numerical solver. On the eight D-NeRF and seven NeRF-DS scenes the liquid field matches or exceeds the MLP baseline in aggregate, with its largest gains concentrated on the scenes with the most high-frequency articulated motion. The result is a near-zero-friction architectural design that turns the discrete MLP deformation field into an explicit continuous-time function of t.

  </details>

## 2026-06-08

- **[EvoGS: Constructing Continuous-Layered Gaussian Splatting with Evolution Tree for Scalable 3D Streaming](https://arxiv.org/abs/2606.07179)**  
  *Yuang Shi, Simone Gasparini, Géraldine Morin, Wei Tsang Ooi*  
  `2026-06-05` · `cs.CV` · [abs](https://arxiv.org/abs/2606.07179) · [pdf](https://arxiv.org/pdf/2606.07179.pdf)
  > 💡 现有离散分层3DGS流式传输存在冗余和误差累积，提出连续分层进化树表示，消除冗余并大幅降低传输和显存占用。

  <details><summary>Abstract</summary>

  Streaming 3D Gaussian Splatting requires highly scalable, progressive representations. Existing progressive methods rely on \textit{discrete layering}, accumulating separate splat sets for each level of detail. This structural independence between layers inherently leads to error accumulation, severe splat redundancy, and uncontrolled quality transitions. We propose EvoGS, the first \textit{continuous-layering} representation. Organized as an Evolution Tree, EvoGS generates finer details via an explicit, wavelet-inspired parent-child refinement. This empowers child nodes to structurally correct ancestral errors, yield inherently sparse and highly compressible inter-layer signals. Extensive experiments show EvoGS eliminates splat redundancy from over 65\% to under 25\%. Compared to state-of-the-art baselines, it reduces transmission payload and GPU VRAM footprint by up to 2.4$\times$ and 5.5$\times$, respectively, and achieves smooth quality transitions optimal for real-time adaptive streaming. Project page: https://yuang-ian.github.io/evogs/

  </details>

- **[QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation](https://arxiv.org/abs/2606.07118)**  
  *Yuxiang Chen, Yuanhao Wang, Ziheng Zhang, Meng Zhang, Yu Liu, Yufei Jia, Tiancai Wang, Erjin Zhou, Jin Xie*  
  `2026-06-05` · `cs.RO` · [abs](https://arxiv.org/abs/2606.07118) · [pdf](https://arxiv.org/pdf/2606.07118.pdf)
  > 💡 利用重建场景校准视觉、接触和动力学，通过3DGS与残差补偿缩小仿真到现实差距，实现零样本地形导航。

  <details><summary>Abstract</summary>

  Simulation is central to robot learning, yet the sim-to-real gap remains a major bottleneck.Existing approaches often tackle visual or dynamic gaps separately, overlooking how these individual mismatches accumulate and propagate throughout the robot's state evolution.In this paper, we introduce QuadVerse, an integrated framework that uses reconstructed scenes as a calibration substrate for aligning visual perception, physical interaction, and actuator dynamics.From captured RGB videos, we reconstruct geometry-constrained 3D Gaussian Splatting (3DGS) scenes that support batched photorealistic ego-view rendering and collision-ready semantic mesh extraction. The meshes further enable contact calibration by initializing spatially varying friction priors and refining them through trajectory-based posterior search.To address remaining actuator discrepancies, QuadVerse trains a residual dynamics compensator by replaying real-world trajectories on the contact-calibrated terrain, reducing the entanglement between terrain-induced contact errors and actuator non-idealities.Experiments show that QuadVerse improves reconstruction quality and locomotion tracking over relevant baselines.Leveraging this foundation, we demonstrate robust zero-shot visual-navigation policy deployment without task-specific real-world rollouts.

  </details>

## 2026-06-06

- **[GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds](https://arxiv.org/abs/2606.05650)**  
  *Rajrup Ghosh, Haodong Wang, Haoran Hong, Eduardo Pavez, Amartya Chaudhuri, Weiwu Pang, Harsha V. Madhyastha, Antonio Ortega, Ramesh Govindan*  
  `2026-06-04` · `cs.MM` · [abs](https://arxiv.org/abs/2606.05650) · [pdf](https://arxiv.org/pdf/2606.05650.pdf)
  > 💡 针对动态高斯泼溅流传输中压缩慢的问题，提出GPU并行加速编解码，实现全帧率处理，速度提升1-2个数量级，压缩与渲染质量相当。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian Splatting (3DGS) holds great promise as a 3D video streaming technology since it can represent complex 3D scenes with high fidelity. In this approach, every frame in a 3D video represents the environment as a collection of Gaussians with position and other attributes such as scale, rotation, opacity, and color. Frames capture fine details, permit views from any arbitrary perspective, but are an order of magnitude, or more, larger than 2D video frames. A line of recent work has explored how to compress dynamic 3DGS frames, but these approaches are often slow, in part because their compression techniques are not amenable to efficient acceleration. GS-NFS accelerates dynamic 3DGS compression and decompression on a GPU, to the point where it can encode and decode at full frame rate. It achieves this by developing novel GPU-based parallelizations of existing algorithms for encoding both positions and attributes of Gaussians. As a result, it is 1-2 orders of magnitude faster than the state-of-the-art in encoding and decoding a frame, while offering competitive compression performance and rendering quality.

  </details>

- **[Self-Learning Expression Deformations for Data-Efficient Gaussian Avatars](https://arxiv.org/abs/2606.05912)**  
  *Jiahao Yang, Xiaohang Yang, Qing Wang, Yilan Dong, Gregory Slabaugh, Shanxin Yuan*  
  `2026-06-04` · `cs.CV` · [abs](https://arxiv.org/abs/2606.05912) · [pdf](https://arxiv.org/pdf/2606.05912.pdf)
  > 💡 针对高斯头像数据需求大的问题，提出自监督SAGE框架，联合2D高斯和SDF实现极少量数据的高质量表情动画。

  <details><summary>Abstract</summary>

  Modeling dynamic facial expressions using 3D Gaussian representations remains challenging due to their unstructured nature. Conventional Gaussian avatar pipelines require extensive multiview and sequential expression data, limiting scalability and accessibility. In this work, we introduce Self-Adaptive Gaussian Expression (SAGE), a framework for self-learning expression-induced Gaussian deformations that enables high-fidelity, animatable avatars from minimal input data. Our method jointly optimizes 2D Gaussian surfels and a Signed Distance Field (SDF) to enforce compact, surface-aligned Gaussian distributions, while a self-supervised expression learning phase replaces long training sequences with geometric and appearance consistency constraints. This design allows flexible deployment across multiple reconstruction regimes: in the multiview setting, only a single frame (timestep) is required instead of thousands; in the monocular setting, only head rotations are needed without expression sequences; and in the one-shot setting, no pretraining or priors are necessary. Experiments demonstrate that our approach achieves reconstruction and animation quality comparable to state-of-the-art methods, while reducing data requirements by several orders of magnitude. Our results highlight the potential of self-supervised Gaussian deformation learning as a step toward accessible, data-efficient avatar creation.

  </details>

- **[SparseStreet: Sparse Gaussian Splatting for Real-Time Street Scene Simulation](https://arxiv.org/abs/2606.03909)**  
  *Qingpo Wuwu, Xiaobao Wei, Peng Chen, Nan Huang, Zhongyu Zhao, Hao Wang, Ming Lu, Ningning Ma, Shanghang Zhang*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03909) · [pdf](https://arxiv.org/pdf/2606.03909.pdf)
  > 💡 街道场景高斯点冗余导致存储渲染瓶颈，提出节点剪枝和背景压缩框架，实现80%压缩率且质量损失极小。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting has shown promising results in street scene reconstruction, existing methods require massive numbers of Gaussian primitives to capture fine details, leading to prohibitive storage costs and slow rendering speeds. We observe that dynamic objects (e.g., vehicles and pedestrians) demand high-fidelity representations to maintain temporal consistency, while static background regions often contain substantial redundancy. Motivated by this, we propose SparseStreet, a general compression framework specifically designed for street scenes. First, we introduce a node-based learnable pruning strategy that systematically removes low-contributing Gaussian primitives while preserving visually critical regions. Second, after the scene representation stabilizes, we apply background compression, further reducing redundancy in static regions. Our method effectively preserves the geometry and appearance of dynamic objects while significantly reducing the total number of Gaussian primitives. Extensive experiments on the Waymo and nuScenes demonstrate that SparseStreet achieves up to 80% compression ratio with minimal quality degradation, enabling resource-efficient, high-fidelity dynamic scene reconstruction. Project website: https://sparsestreet.github.io/.

  </details>

- **[PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting](https://arxiv.org/abs/2606.03479)**  
  *Adrian Ramlal, John S. Zelek*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03479) · [pdf](https://arxiv.org/pdf/2606.03479.pdf)
  > 💡 通过可微刚体模拟与3DGS结合，解决遮挡时物体高斯退化问题，实现物理准确轨迹预测并降低40%轨迹误差。

  <details><summary>Abstract</summary>

  Dynamic 3D Gaussian Splatting (3DGS) methods reconstruct time-varying scenes from synchronized multi-camera video using photometric supervision. When a moving object becomes fully occluded from all training cameras, this supervision vanishes: the Gaussians representing it receive no gradient signal and degrade. Existing approaches to incomplete observations in neural reconstruction rely on learned generative priors that prioritize visual plausibility over physical correctness. We propose $\textbf{PersistGS}$, a method that restores object permanence during occlusion by coupling differentiable rigid body simulation with 3D Gaussian Splatting. Our approach decomposes the scene into per-object Gaussians and collision meshes, estimates friction and velocity from the observed pre-occlusion trajectory via differentiable simulation, and uses the resulting SE(3) trajectory to position object Gaussians throughout the occlusion period. Because the predicted trajectory satisfies the governing equations of rigid body dynamics, it faithfully captures contact events (bounces, friction-based deceleration, direction changes) that kinematic extrapolation cannot model. We introduce a centroid silhouette loss that isolates positional gradients from appearance noise, yielding 40% lower trajectory error than photometric supervision. We evaluate using cameras withheld from training that observe the object during its occlusion. Experiments on synthetic scenes show that PersistGS outperforms constant velocity extrapolation by +2.46dB PSNR and comes within 0.19dB of a ground-truth trajectory upper bound.

  </details>

- **[FreeStreamGS: Online Feed-forward 3D Gaussian Splatting from Unposed Streaming Inputs](https://arxiv.org/abs/2606.03254)**  
  *Ruiyang Chen, Feiran Li, Chu Zhou, Zonglin Li, Zhanyu Ma, Heng Guo*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03254) · [pdf](https://arxiv.org/pdf/2606.03254.pdf)
  > 💡 提出解耦内在恢复头和动态点细化偏移策略，解决流式无位姿输入下3D高斯溅射的累积漂移与渲染伪影问题。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting (3DGS) allows efficient and high-fidelity novel view synthesis (NVS) from an offline recorded image sequence. However, achieving online NVS from streaming and unposed image inputs remains challenging. Although online feed-forward geometric estimation methods have been proposed for streaming depth and point cloud recovery, they cannot be adapted to NVS due to severe rendering artifacts. This is because NVS demands stricter multi-view consistency in Gaussian scales and pose-geometry alignment; even minor deviations would accumulate over time and visibly degrade rendering quality. To this end, we propose FreeStreamGS, a robust online feed-forward framework for efficient and high-quality NVS. We introduce two key mechanisms: a Decoupled Intrinsic Recovery Head that removes cumulative camera intrinsic bias and prevents scene scale jitter during long-term streaming, and a Dynamic Point Refinement Offset strategy that relaxes rigid unprojection to correct coupled pose-depth drift. Extensive experiments show that FreeStreamGS achieves rendering quality competitive with state-of-the-art offline feed-forward 3DGS methods, despite operating without access to future frames.

  </details>

- **[TIDES: Time-Derivative Event Simulation via Deformable Reconstruction](https://arxiv.org/abs/2606.02058)**  
  *Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02058) · [pdf](https://arxiv.org/pdf/2606.02058.pdf)
  > 💡 基于动态高斯泼溅的连续时间事件模拟器，解决时间戳批处理问题，实现高保真事件流并提升下游任务迁移效果。

  <details><summary>Abstract</summary>

  Event cameras emit asynchronous events in response to environmental appearance changes. The scarcity of real-world event datasets makes simulation essential. However, most simulators infer event timestamps from frame sequences, forcing many threshold crossings to share a small set of discrete times; a failure mode we term timestamp batching that worsens under fast motion and occlusion. We present TIDES, a continuous-time event simulator built on dynamic Gaussian splatting. Because TIDES operates on an explicit 3D scene representation with learnt geometry and motion, it can derive per-pixel intensity dynamics directly from the scene, rather than by differencing rendered frames. This enables accurate threshold-crossing prediction, including multiple crossings per rendering step, without temporal upsampling or frame interpolation. The same 3D scene model reveals where objects partially occlude one another; TIDES uses this to guide adaptive time stepping, concentrating computation only in regions where occlusion dynamics make simple models of brightness change unreliable. Finally, we model finite sensor bandwidth using a tile-level arbiter whose throughput, jitter, and event drops reproduce realistic sensor artifacts. Across paired RGB-event benchmarks, TIDES attains state-of-the-art event-stream fidelity. We also show that events simulated by TIDES transfer more effectively to real downstream tasks than competitors'.

  </details>

- **[Learning Action-Conditional and Object-Centric Gaussian Splatting World Models for Rigid Objects](https://arxiv.org/abs/2606.01950)**  
  *Jens U. Kreber, Lukas Mack, Joerg Stueckler*  
  `2026-06-01` · `cs.RO` · [abs](https://arxiv.org/abs/2606.01950) · [pdf](https://arxiv.org/pdf/2606.01950.pdf)
  > 💡 用物体中心高斯和时空Transformer预测刚体动作动力学，处理多物体遮挡，实现无抓取操控。

  <details><summary>Abstract</summary>

  World models enable intelligent agents to predict the consequences of their actions on the environment. In this paper, we propose Multi Rigid Object Gaussian World Model (MRO-GWM), a novel model that learns action-conditional dynamics of rigid objects in 3D. By representing the scene by object-centric Gaussians, we can represent arbitrary object shapes and multi-object scenes. We develop a novel spatio-temporal transformer architecture that predicts future rigid body motion from a history of object Gaussians and future actions. Objects are represented by their Gaussians in a canonical frame, which allows for describing object motion as rigid body transformation. Our model is trained on reconstructions from multiple viewpoints, which requires the model to handle partial observations of objects due to occlusions. We analyze prediction performance of our approach on synthetic datasets composed of typical household objects with multi-object dynamics and interactions by a robot end effector. We also evaluate our model in model-predictive control for non-prehensile manipulation in simulation.

  </details>

- **[MORPHOS: Autoregressive 4D Generation with Temporal Structured Latents](https://arxiv.org/abs/2606.02491)**  
  *Minkyung Kwon, Jinhyeok Choi, Youngjin Shin, Jaeyeong Kim, JongMin Lee, Seungryong Kim*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02491) · [pdf](https://arxiv.org/pdf/2606.02491.pdf)
  > 💡 针对动态3D生成中表示单一和时序不一致问题，提出自回归框架MORPHOS，利用Temporal Structured Latents统一表示实现因果注意力生成，在多种表示上达到SOTA。

  <details><summary>Abstract</summary>

  We present MORPHOS, a novel autoregressive framework that generates dynamic 3D assets from videos across diverse representations, including meshes, 3D Gaussians, and radiance fields. Existing methods are typically limited to a single representation, struggle to model topological changes, or fail to maintain temporal consistency over long videos. To address these limitations, we introduce the Temporal Structured Latents (T-SLAT), a unified 4D representation that jointly encodes geometry and appearance along the temporal dimension. Leveraging T-SLAT, MORPHOS autoregressively generates dynamic 3D assets via causal attention, conditioning each frame on its preceding history to ensure temporal consistency while handling evolving topologies. We also propose a temporal-structural augmentation to mitigate error accumulation in autoregressive generation. MORPHOS achieves state-of-the-art performance in appearance and competitive results in geometry across multiple benchmarks, demonstrating superior generalization across various representations and robustness in long-horizon generation.

  </details>

- **[WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos](https://arxiv.org/abs/2606.02096)**  
  *Jongmin Park, Jeonghwan Yun, Minh-Quan Viet Bui, Munchurl Kim*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02096) · [pdf](https://arxiv.org/pdf/2606.02096.pdf)
  > 💡 针对单目视频动态场景重建的结构与细节平衡难题，提出WebSpline，用结构信息样条和图代理实现快速、高保真渲染，质量领先且提速10倍。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction from monocular videos remains highly challenging, as existing methods often struggle to balance global structural coherence and local fine-grained details under limited multi-view cues. To address this challenge, we propose WebSpline, a novel dynamic 3D Gaussian framework that enables structurally coherent and high-fidelity reconstruction from monocular videos with fast rendering. The core of WebSpline is the Structure-Informed Spline (SIS) representation, which models each dynamic Gaussian trajectory using a learnable cubic Hermite spline whose motion is structurally organized with an auxiliary Structural Proxy Graph (SPG). The proposed framework is optimized in two stages: (i) in the first stage, the SPG is initialized from 2D point tracks and refined with temporal rigidity regularization to establish structural coherence for moving objects across the sequence; and (ii) in the second stage, the SIS representation is initialized from the refined SPG and optimized under both spatial and structural neighborhood constraints. At inference, Gaussian motion is obtained solely by evaluating the learned SIS, enabling fast rendering. Extensive experiments on the challenging monocular dynamic scene benchmarks, iPhone and NVIDIA, demonstrate that our WebSpline achieves state-of-the-art rendering quality while rendering over 10 times faster than WorldTree, the second-best method on the iPhone dataset.

  </details>

- **[Real-Time Physics Simulation with Dynamic Mesh-Gaussian Reconstructions](https://arxiv.org/abs/2606.00444)**  
  *Adrian Ramlal, John S. Zelek*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00444) · [pdf](https://arxiv.org/pdf/2606.00444.pdf)
  > 💡 提出固定拓扑网格与高斯泼溅双表征框架实现4.65倍加速模拟，揭示高质量重建与物理兼容拓扑本质矛盾。

  <details><summary>Abstract</summary>

  Integrating dynamic 3D reconstructions into physics simulation requires fixed mesh topology for efficient collision detection, but state-of-the-art methods like DG-Mesh produce varying topology optimized for geometric quality. We investigate whether topology conversion can enable physics integration while preserving reconstruction fidelity. We propose a dual-representation framework combining fixed-topology meshes for physics with Gaussian splatting for rendering, achieving 4.65$\times$ speedup over varying-topology baselines through runtime vertex buffer updates. We evaluate two conversion strategies, temporal correspondence tracking and template-based projection, against native fixed-topology methods (MaGS) on the DG-Mesh dataset. Our evaluation reveals that both conversion approaches incur 65-80% geometric degradation, producing results inferior to MaGS despite DG-Mesh's superior initial quality. This demonstrates that high-quality reconstruction and physics-compatible topology represent fundamentally distinct objectives that cannot be reconciled through post-processing. Our findings inform future development of physics-aware reconstruction methods and our framework enables real-time simulation with any fixed-topology approach.

  </details>

## 2026-06-01

- **[DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.30863)**  
  *Youngtae Han, Sung-hwan Han, Youngmin Yi*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30863) · [pdf](https://arxiv.org/pdf/2605.30863.pdf)
  > 💡 提出静态-动态分解的高斯泼溅框架，结合前馈编码器和光流模型，实现高效高保真动态场景重建，无需COLMAP预处理。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction and novel view synthesis are fundamental to next-generation visual intelligence applications such as virtual reality, robotics, and digital twins. However, high-fidelity reconstruction of complex, time-varying scenes from arbitrary viewpoints remains a significant challenge. Existing dynamic 3DGS methods suffer from computational inefficiency, since they model all Gaussians as dynamic components. While recent decomposition-based approaches address this issue, they still struggle with degraded reconstruction quality and prolonged training time. To mitigate these limitations, we propose a novel dynamic reconstruction framework built upon an efficient static-dynamic decomposition strategy using a Feed-Forward Gaussian Splatting encoder and an optical flow model. By eliminating redundant computations on static regions, our method achieves state-of-the-art performance, outperforming existing baselines across rendering quality, training and rendering speed, and storage efficiency. Notably, on the Neural 3D dataset, our framework requires only 10 minutes for training and achieves a rendering speed of over 700 FPS on a single NVIDIA RTX 5090 GPU at resolution of 1352x1014. Furthermore, our decomposition strategy eliminates the need for COLMAP preprocessing and enables deterministic initialization, thereby enhancing both efficiency and reproducibility.

  </details>

- **[Robust Dreamer: Deviation-Aware Latent Gaussian Memory for Action-Controlled AR Video Generation](https://arxiv.org/abs/2605.30855)**  
  *Hanlin Chen, Jiaxin Wei, Xibin Song, Yifu Wang, Steve Wang, Hongdong Li, Pan Ji, Gim Hee Lee*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30855) · [pdf](https://arxiv.org/pdf/2605.30855.pdf)
  > 💡 针对长序列AR视频生成中的累积漂移问题，提出潜在高斯记忆与偏差学习框架，实现稳健的状态保持与SOTA性能。

  <details><summary>Abstract</summary>

  Frame-wise action-controlled image-to-video generation is a promising paradigm for interactive world simulation, where each control signal should elicit an immediate visual response. However, maintaining visual fidelity and 3D consistency over long autoregressive rollouts remains challenging. Existing 3D-aware methods often suffer from catastrophic drift due to two impediments: information loss from \textit{Latent--RGB Cycling}, where generated latents are repeatedly decoded to RGB and re-encoded for future conditioning, and the training--inference gap induced by the \textit{error-free hypothesis}, where clean training memory fails to match prediction-corrupted inference memory. To address these challenges, we present \textbf{Robust Dreamer}, a memory-augmented framework built around how to design 3D memory and how to use it robustly. First, we introduce \textbf{Latent Gaussian Memory}, which anchors diffusion latents inherited from the generation process to Gaussian primitives and recalls them via latent-space Gaussian splatting. This provides dense, geometry-aware, view-aligned conditioning while avoiding accumulated degradation from repeated VAE conversion. Second, we propose \textbf{Deviation Learning with Dynamic Deviation Archive}, which synthesizes rollout-induced latent deviations through a one-step approximation, stores them by autoregressive stage and denoising timestamp, and injects them into historical memory during training. This exposes the generator to realistic corrupted memory states and teaches internal correction before inference. Experiments on ScanNet, DL3DV, and OmniWorldGame demonstrate state-of-the-art long-horizon performance.

  </details>

- **[Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2605.31595)**  
  *Mungyeom Kim, Minkyeong Jeon, Honggyu An, Jaewoo Jung, Hyuna Ko, Jisang Han, Hyeonseo Yu, Donghwan Shin, Sunghwan Hong, Takuya Narihira, Kazumi Fukuda, Yuki Mitsufuji, Seungryong Kim*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.31595) · [pdf](https://arxiv.org/pdf/2605.31595.pdf)
  > 💡 用紧凑高斯查询令牌聚合时序特征，实现前馈4D

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction from monocular video remains a fundamental challenge in computer vision. Existing feed-forward methods predict 3D Gaussians pixel-wise for each frame, suffering from duplicated Gaussians and view-dependent biases that hinder effective learning of scene motion. We present C4G, a feed-forward 4D reconstruction framework built upon a compact set of timestamp-conditioned learnable Gaussian query tokens. Each token aggregates corresponding features across the full temporal context and decodes a 3D Gaussian whose position is modulated by the target timestamp, enabling globally coherent motion modeling without per-scene optimization. To capture fine-grained details, we further introduce a video diffusion model-based rendering enhancement module. Since our framework effectively aggregates features into Gaussians, we extend this capability to feature lifting, producing a 4D feature field that supports point tracking and dynamic scene understanding. C4G achieves strong novel-view synthesis performance using significantly fewer Gaussians and without requiring camera poses, while exhibiting stronger motion modeling and robustness to large temporal gaps.

  </details>

## 2026-05-30

- **[MonoPhysics: Estimating Geometry, Appearance, and Physical Parameters from Monocular Videos](https://arxiv.org/abs/2605.30320)**  
  *Daniel Rho, Jun Myeong Choi, Matthew Thornton, Biswadip Dey, Roni Sengupta*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30320) · [pdf](https://arxiv.org/pdf/2605.30320.pdf)
  > 💡 单目视频缺乏几何约束，提出结合3DGS和可微MPM仿真的MonoPhysics，通过三个视觉-物理桥梁联合优化几何、外观和物理参数，性能媲美多视图方法。

  <details><summary>Abstract</summary>

  Existing inverse physics methods recover physical parameters from multi-view videos, where geometric constraints across views resolve scale and 3D structure. In monocular settings, however, such constraints are absent, leading to severe scale ambiguity, inaccurate geometry, and weak coupling between appearance optimization and physical simulation. We propose MonoPhysics, a framework for monocular inverse physics estimation of deformable objects using differentiable MPM simulation and 3D Gaussian Splatting, which jointly optimizes geometry, appearance, and physical parameters from a single camera view. We address these challenges through three visual-physical bridges: global scale alignment, physics-aware geometry refinement, and a differentiable position map, which together enable accurate optimization from monocular observations alone. We evaluate on Vid2Sim and our new dataset of elastic and plastic objects, showing that MonoPhysics outperforms existing baselines in monocular settings and achieves performance comparable to multi-view baselines using only a single camera. Our project page is available at https://daniel03c1.github.io/MonoPhysics/

  </details>

- **[PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions](https://arxiv.org/abs/2605.30268)**  
  *Omer Benishu, Gal Fiebelman, Sagie Benaim*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30268) · [pdf](https://arxiv.org/pdf/2605.30268.pdf)
  > 💡 结合运动扩散与物质点物理模拟，以3D高斯为统一表示，生成物理一致的4D人-物交互动态场景。

  <details><summary>Abstract</summary>

  We address the task of generating physically accurate and visually faithful 4D Human-Object Interaction (HOI). Given a static 3D human and target object represented as 3D Gaussian Splats (3DGS), our goal is to synthesize dynamic scenes where the human actively engages with the object through actions, such as punching or kicking, in accordance with a given input text. To this end, we introduce PhyGenHOI, a novel framework that couples generative human motion with an explicit physical object simulation. We model the human as a semantic agent driven by a Motion Diffusion Model (MDM) and the object as a physical agent simulated via the Material Point Method (MPM), utilizing 3D Gaussians as a unified, differentiable representation. We supervise their interaction through three coupled mechanisms: (1) A Windowed Attraction Loss that temporally synchronizes generative motion to intercept the object; (2) A Contact-Driven Re-simulation step that triggers physically consistent momentum transfer upon impact; and (3) A Masked Video-SDS objective that injects video-based priors to enhance contact fidelity. Experiments show PhyGenHOI generates physically consistent 4D HOI across diverse actions, humans, and objects, outperforming baselines. Project page and videos: https://omerbenishu.github.io/PhyGenHOI/

  </details>

- **[FRUC: Feedforward Dynamic Scene Reconstruction from Uncalibrated Collaborative Driving Views](https://arxiv.org/abs/2605.29997)**  
  *Yihang Tao, Yu Guo, Zhengru Fang, Haonan An, Yuguang Fang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29997) · [pdf](https://arxiv.org/pdf/2605.29997.pdf)
  > 💡 提出无标定协作驾驶动态场景重建方法FRUC，利用前馈3D高斯和因果遮挡场实现高效单次重建，显著提升渲染质量。

  <details><summary>Abstract</summary>

  We present FRUC, a feed-forward 3D Gaussian splatting framework for dynamic scene reconstruction from uncalibrated collaborative driving views. Existing multi-agent reconstruction frameworks are often hindered by rigid prerequisites, demanding precise spatial calibration and slow per-scene optimization. In this paper, we rethink this task by conceptualizing a distributed multi-vehicle network as a spatio-temporally unstructured ego-centric multi-camera system, where the core challenge lies in enhancing ego-centric occluded geometry through collaboration without degrading the ego's accurately observed visible geometry, while preserving reconstruction efficiency. For efficient reconstruction, FRUC is built upon a visual grounded geometric Transformer backbone to enable one-shot, calibration-free inference from a flexible number of multi-vehicle views. To achieve non-destructive geometric supplementation under uncalibrated cross-agent misalignment, FRUC first introduces an ego-centric causal occlusion field that explicitly derives occlusion evolution as latent priors by modeling agent-wise spatio-temporal correlations. Guided by these occlusion priors, it further formulates cross-agent integration as a deterministic residual denoising process via zero-initialized injection, turning challenging cross-agent fusion into bounded residual learning for robust collaborative blind-spot completion. Through extensive evaluations on the real-world V2XReal and UrbanIng-V2X datasets, FRUC is shown to be a new state-of-the-art for the scene reconstruction of dynamic collaborative driving environments, significantly outperforming existing methods in both rendering quality and efficiency.

  </details>

- **[DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](https://arxiv.org/abs/2605.29879)**  
  *Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29879) · [pdf](https://arxiv.org/pdf/2605.29879.pdf)
  > 💡 提出混合实例感知3D高斯动态场景图系统，结合概率体素与显式高斯实现跨模态融合和动态更新，零样本3D视觉定位和语义分割性能领先。

  <details><summary>Abstract</summary>

  Integrating open-vocabulary semantic information into dynamic 3D scene representations is essential for long-term embodied scene understanding. However, existing methods often suffer from fragile instance association due to incomplete cross-view cues, while their limited ability to handle object-level topological changes restricts long-term robotic task execution. Moreover, current 3D scene understanding methods either rely on simple feature matching without explicit spatial reasoning or assume offline ground-truth 3D geometry. To address these challenges, we present DGSG-Mind, a hybrid instance-aware 3D Gaussian dynamic scene graph system with an embodied reasoning agent. Our system couples a probabilistic voxel grid with explicit 3D Gaussians to enable robust cross-modal instance fusion and incremental semantic mapping. It handles dynamic changes through Gaussian-based visual relocalization and localized masked refinement guided by geometric-semantic consistency. Built on the instance Gaussian map, DGSG-Mind further constructs a hierarchical scene graph and develops the 3D Gaussian Mind, which integrates structural relations, spatial-semantic information, and visually annotated RoI Gaussian renderings for multimodal reasoning. Extensive experiments show that DGSG-Mind achieves the best zero-shot 3DVG performance among methods operating on self-reconstructed maps, while also delivering strong performance in 3D open-vocabulary semantic segmentation and scene reconstruction. We further deploy DGSG-Mind on real-world robots to demonstrate its target-oriented reasoning and dynamic update capabilities. The project page of DGSG-Mind is available at https://icr-lab.github.io/DGSG-Mind

  </details>

- **[R5DGS: Semantic-Aware 4D Gaussian Splatting with Rigid Body Constraints for Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.25909)**  
  *Denis Gridusov, Maxim Popov, Sergey Kolyubin*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25909) · [pdf](https://arxiv.org/pdf/2605.25909.pdf)
  > 💡 利用语义编码和CLIP查找表实现物体关联，通过刚体中心推理加速外推，实现高效动态场景重建。

  <details><summary>Abstract</summary>

  Reconstructing and predicting dynamic 3D scenes from multi-view videos is a foundational task for robotics, AR/VR, and digital twins. Recent physics-informed Gaussian Splatting methods achieve impressive future frame extrapolation but lack semantic awareness and suffer from large computational overhead. We introduce $\textbf{R5DGS}$, a framework that augments a physics-driven 4D Gaussian representation with compact Identity Encoding vectors, enabling precise Gaussian-to-object association. By constructing an offline CLIP-based object lookup table, we support open-vocabulary text prompting to retrieve and render object-specific Gaussians across arbitrary timestamps and viewpoints. Furthermore, we propose a rigid-body inference constraint that predicts and integrates physical dynamics exclusively for object centroids, propagating motion to associated Gaussians via relative transformations. This optimization yields a 11 FPS speedup during extrapolation without compromising trajectories plausibility.

  </details>

- **[SplitAvatar: One-shot Head Avatar with Autoregressive Gaussian Splitting](https://arxiv.org/abs/2605.25751)**  
  *Hongzhe Liao, Chuhua Xian, Hongmin Cai, Haiyang Liu, Fa-Ting Hong*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25751) · [pdf](https://arxiv.org/pdf/2605.25751.pdf)
  > 💡 基于单图重建可动头部头像，提出自回归图分裂网络逐步细化高斯分布，解决数量不匹配问题，提升表情细节与重建质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) provides an efficient method for high-quality scene reconstruction using anisotropic Gaussians. Recently, 3DGS-based methods have significantly improved the rendering quality of human avatars while enabling real-time performance. However, existing methods suffer from a magnitude mismatch in the number of Gaussians generated by image-based and 3DMM-based approaches. This discrepancy results in reconstructed expressions that lack fine-grained detail. In this paper, we introduce a novel method for reconstructing an animatable head avatar from a single image. We propose a Graph splitting network to progressively generate Gaussians from coarse to fine using an autoregressive architecture. To address the graph inconsistency caused by split Gaussians, we employ a mesh topology extension method to align the GNN's connectivity with the increased Gaussian count. Furthermore, we introduce a novel density control method that includes a gating mechanism that generates soft masks for Gaussians, preventing over-densification after the splitting operation. This allows for dynamic control over Gaussian density across different facial regions. For smooth and rapid training, we employ a delayed filtering strategy to avoid re-computing the graph topology during training. Experimental results demonstrate that our autoregressive structure effectively improves expression representation ability by progressively splitting Gaussians. This process, enabled by the GNN-guided splitting, synthesizes more precise facial details and achieves higher reconstruction quality.

  </details>

- **[Physics-Aware 3D Gaussian Editing for Driving Scene Generation](https://arxiv.org/abs/2605.25373)**  
  *Feng Zhou, Jian Zhang, Yuhang Sun, He Wang, Qiong Wen, Debao Kong, Tieru Wu, Rui Ma*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25373) · [pdf](https://arxiv.org/pdf/2605.25373.pdf)
  > 💡 现有3DGS编辑缺乏道路几何修改和车辆动力学耦合，提出RoVES通过单图驱动和半车模型实现物理感知的快速道路插入与姿态校正。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has shown great potential in autonomous driving simulation and data generation, enabling photorealistic reconstruction and flexible scene manipulation. However, existing 3DGS scene editing methods have limited support for road geometry editing (e.g., inserting speed humps or sunken roads), and generally do not couple such edits with plausible vehicle-road interaction dynamics. Such editing is essential for generating training data under extreme driving scenarios or evaluating system reliability under these road irregularities. Moreover, many optimization-based methods require minutes of per-edit refinement, while existing efficient alternatives mainly focus on appearance-level or object-level manipulation rather than physics-aware road irregularity editing. To address these limitations, we propose RoVES, a Road-and-Vehicle Editing System for physics-aware 3D Gaussian editing in driving scenes. RoVES enables single-image-driven road geometry insertion and couples the edited road profile with a 4-DOF half-car vehicle dynamics model to achieve physics-aware vehicle pose correction in vertical displacement and pitch. RoVES inserts road elements in a one-shot, optimization-free pipeline (1.84s), and the full pipeline (including color transfer and vehicle-dynamics-based pose correction) completes in 6.24s; it edits dynamic vehicles via pose editing and corrects poses frame-by-frame to approximate dynamics-consistent vertical displacement and pitch responses. Experiments on the Waymo dataset show that RoVES provides practical efficiency and competitive visual consistency for physics-aware driving scene generation.

  </details>

- **[Full-4D: Generating Full-Scope 4D Scenes from a Single-View Video](https://arxiv.org/abs/2605.25500)**  
  *Tingxi Chen, Ke Hao, Yabo Chen, Zhengxue Cheng, Rong Xie, Li Song, Haibin Huang, Chi Zhang, Xuelong Li*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25500) · [pdf](https://arxiv.org/pdf/2605.25500.pdf)
  > 💡 从单视角视频生成全范围4D场景，通过多

  <details><summary>Abstract</summary>

  Generating 4D scenes from a single-view video is inherently ill-posed: a single viewpoint lacks the information needed to recover a complete, dynamic scene with full coverage. Existing methods are typically limited to monocular videos, simple 3D effects, or only small viewpoint perturbations around the original viewpoint, falling short of true 4D generation. Meanwhile, the lack of large-scale datasets capturing full-scope 4D scenes with synchronized multi-view videos further hinders progress in this direction. We propose a novel single-view video-to-4D framework that casts full-scope 4D generation as a multi-view video synthesis followed by optimization-based 4D reconstruction from the generated views. To instantiate this formulation end-to-end, we make three key contributions. First, we introduce Real-MV-4D, a large-scale dataset of synchronized multi-view videos captured in diverse real-world environments to provide the 4D supervision. Second, we train a multi-view video diffusion model driven by a novel fused time(T)-view(V) attention mechanism that directly embeds geometric reprojection priors and explicit camera conditioning into its view-time interactions. Unlike basic feature fusion, this direct binding strictly aligns the generation process with physical 3D priors to produce a dense, synchronized T$\times $V video grid. Third, rather than relying on non-interactive and inconsistent 2D video interpolations, we lift the synthesized multi-view videos into an explicit 4D representation (i.e. 4DGS), regularized by a Flow Matching Distillation loss that exploits the multi-view prior to improve novel-view rendering. Extensive experiments demonstrate that our method outperforms existing approaches in both visual fidelity and geometric consistency, enabling full-scope 4D scene generation from single-view videos.

  </details>

- **[Learning a Particle Dynamics Model with Real-world Videos](https://arxiv.org/abs/2605.23845)**  
  *Chanho Kim, Suhas V. Sumukh, Li Fuxin*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23845) · [pdf](https://arxiv.org/pdf/2605.23845.pdf)
  > 💡 从真实视频无监督学习高斯泼溅粒子动力学模型，通过渲染监督训练，避免模拟到真实差距。

  <details><summary>Abstract</summary>

  Data-driven learning approaches for physics simulation, sometimes referred to as world models, have emerged as promising alternatives to traditional physics simulators due to their differentiable nature. Prior work has demonstrated impressive results in predicting the motions of rigid and non-rigid objects in complex scenes involving multiple interacting bodies. However, these models are typically trained in simulated environments because obtaining perfect state information such as complete scene point clouds and point correspondences over time is challenging in real-world settings. This reliance on synthetic data can limit their applicability when the sim-to-real gap is large. In this work, we aim to overcome these limitations by introducing a novel framework for training neural object dynamics models directly from unlabeled real-world videos. Specifically, we propose to learn a particle-based dynamics model compatible with a Gaussian splatting framework, which operates on dense particles derived from Gaussians (i.e., particles with scales and rotations) and predicts their position and rotation changes over time. The model is trained via rendering supervision, enabling learning from real-world videos without requiring particle-level labeled states. Our model operates directly on dense Gaussians without relying on heuristic subsampling anchor points. To enable this study, we also present a real-world dataset consisting of about 500 videos capturing diverse object interactions.

  </details>

- **[RiGS: Rigid-aware 4D Gaussian Splatting from a Single Monocular Video](https://arxiv.org/abs/2605.23672)**  
  *Chenyu Wu, Wanhua Li, Zhu-Tian Chen, Hanspeter Pfister*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23672) · [pdf](https://arxiv.org/pdf/2605.23672.pdf)
  > 💡 针对单目视频动态场景重建，RiGS引入静态、刚体、瞬态高斯基元，结合物体动态掩码与场景流，实现多时间

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from monocular videos is a fundamental yet highly challenging task, as real-world motions often involve both long-term smooth transformations and short-term complex deformations. Existing methods either struggle to maintain temporal consistency or fail to capture high-frequency dynamics due to limited motion modeling capacity. In this work, we present Rigid-aware 4D Gaussian Splatting (RiGS), which simultaneously captures motions across multiple temporal scales. Specifically, RiGS introduces three types of Gaussian primitives: static, rigid, and transient, which represent static backgrounds, long-term low-frequency motions, and short-term high-frequency dynamics, respectively. An object-wise dynamic mask is proposed to aggregate long-range spatiotemporal motion information and guide the decomposition of static and dynamic regions. To jointly model motion across scales, rigid Gaussians are allowed to transition into transient Gaussians based on their temporal duration, and both are optimized under scene flow guidance, providing dense 3D motion supervision. Extensive experiments demonstrate that RiGS achieves state-of-the-art performance on novel view synthesis benchmarks. Code is available at \hyperlink{https://github.com/ladvu/RiGS}{https://github.com/ladvu/RiGS}.

  </details>

- **[Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving](https://arxiv.org/abs/2605.22809)**  
  *Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng, Zehao Zhu, Meng-Li Shih, Xander Masotto, Shih-Yang Su, Kanaad V Parvate, Tiancheng Ge, Linn Bieske, Dragomir Anguelov, Mingxing Tan, Chiyu Max Jiang*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22809) · [pdf](https://arxiv.org/pdf/2605.22809.pdf)
  > 💡 针对行车记录仪视频与多模态传感器数据不兼容问题，用4DGS和扩散模型实现跨传感器转换，解锁外部数据源。

  <details><summary>Abstract</summary>

  Robust training and validation of Autonomous Driving Systems (ADS) require massive, diverse datasets. Proprietary data collected by Autonomous Vehicle (AV) fleets, while high-fidelity, are limited in scale, diversity of sensor configurations, as well as geographic and long-tail-behavioral coverage. In contrast, in-the-wild data from sources like dashcams offers immense scale and diversity, capturing critical long-tail scenarios and novel environments. However, this unstructured, in-the-wild video data is incompatible with ADS expecting structured, multi-modal sensor inputs for validation and training. To bridge this data gap, we propose Sensor2Sensor, a novel generative modeling paradigm that translates in-the-wild monocular dashcam videos into a high-fidelity, multi-modal sensor suite (AV logs) comprising multi-view camera images and LiDAR point clouds. A core challenge is the lack of paired training data. We address this by converting real AV logs into dashcam-style videos via 4D Gaussian Splatting (4DGS) reconstruction and novel-view rendering. Sensor2Sensor then utilizes a diffusion architecture to perform the generative conversion. We perform comprehensive quantitative evaluations on the fidelity and realism of the generated sensor data. We demonstrate Sensor2Sensor's practical utility by converting challenging in-the-wild internet and dashcam footage into realistic, multi-modal data formats, further unlocking vast external data sources for AV development.

  </details>

- **[4D-GSW: Kinematic-Aware Spatio-Temporal Consistent Watermarking for 4D Gaussian Splatting](https://arxiv.org/abs/2605.22342)**  
  *Sifan Zhou, Hang Zhang, Yuhang Wang, Ming Li*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22342) · [pdf](https://arxiv.org/pdf/2605.22342.pdf)
  > 💡 针对4D高斯溅射水印缺乏运动感知导致时序伪影，引入时空曲率度量与HMM-MRF能量模型实现鲁棒且高时空一致的水印嵌入。

  <details><summary>Abstract</summary>

  While 4D Gaussian Splatting (4DGS) has revolutionized high-fidelity dynamic reconstruction, safeguarding the intellectual property of these assets remains an open challenge. Conventional steganographic techniques often neglect the underlying kinematic manifolds, triggering non-physical artifacts such as severe temporal flickering and "FVD collapse". To address this, we propose \textbf{4D-GSW}, a kinematic-aware watermarking framework designed to embed robust copyright information while preserving high spatio-temporal consistency. Unlike prior 4D steganography that primarily focuses on opacity-guided invisibility, our approach explicitly addresses the physical coherence of motion trajectories. We introduce a \textbf{Spatio-Temporal Curvature (STC)} metric to identify "Dynamic Instants," adaptively gating watermark gradient injection to shield critical motion manifolds from non-physical perturbations. To ensure global coherence across complex deformations, we formulate a joint \textbf{HMM-MRF energy minimization} model that synchronizes watermark phases within both temporal trajectories and spatial neighborhoods. Furthermore, an \textbf{anisotropic gradient routing} mechanism ensures that watermark embedding remains strictly decoupled from photometric reconstruction fidelity. Extensive experiments have demonstrated the superior performance of our method in robustly hiding watermarks while resisting various attacks and maintaining high rendering quality and spatiotemporal consistency.

  </details>

- **[No Pose, No Problem in 4D: Feed-Forward Dynamic Gaussians from Unposed Multi-View Videos](https://arxiv.org/abs/2605.22190)**  
  *Matteo Balice, Yanik Kunzi, Chenyangguang Zhang, Matteo Matteucci, Marc Pollefeys, Sungwhan Hong*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22190) · [pdf](https://arxiv.org/pdf/2605.22190.pdf)
  > 💡 提出无位姿多视图动态高斯泼溅方法，通过速度分解与双向运动编码器，实现高效前馈4D重建，性能超越以往基线。

  <details><summary>Abstract</summary>

  Recent feed-forward 3D gaussian splatting methods have made dramatic progress on individual aspects of 3D scene reconstruction, but no existing method jointly addresses dynamic content, multi-view input, and unknown camera poses in a single feed-forward pass. Methods that handle dynamics either require accurate camera poses or accept only monocular input; pose-free multi-view methods address only static scenes; and per-scene optimization methods bridge some of these gaps but at minutes-to-hours cost per scene. We introduce NoPo4D, the first feed-forward system that addresses this empty quadrant. Building on a pretrained geometry backbone and recent 4D Gaussian frameworks, NoPo4D introduces a velocity decomposition that splits Gaussian motion into per-pixel image-plane shifts and depth changes, allowing direct supervision from pseudo ground-truth optical flow on the 2D component. This sidesteps both the differentiable rendering that couples prior posed methods to pose accuracy and the 3D motion ground truth that prior pose-free methods require. The system is rounded out by a bidirectional motion encoder for cross-view and cross-frame feature aggregation, and view-dependent opacity that mitigates cross-view and cross-timestep Gaussian misalignments. On four multi-view dynamic benchmarks, NoPo4D consistently outperforms prior feed-forward baselines, and with an optional post-optimization stage surpasses per-scene optimization methods, while running orders of magnitude faster.

  </details>

- **[TWINGS: Thin Plate Splines Warp-aligned Initialization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.22069)**  
  *Hyeseong Kim, Geonhui Son, Deukhee Lee, Dosik Hwang*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22069) · [pdf](https://arxiv.org/pdf/2605.22069.pdf)
  > 💡 针对稀疏视图下3DGS点云稀疏问题，采用薄板样条对齐反投影点初始化，提升几何精度与重建质量。

  <details><summary>Abstract</summary>

  Novel view synthesis from sparse-view inputs poses a significant challenge in 3D computer vision, particularly for achieving high-quality scene reconstructions with limited viewpoints. We introduce TWINGS, a framework that enhances 3D Gaussian Splatting (3DGS) by directly addressing point sparsity. We employ Thin Plate Splines (TPS), a smooth non-rigid deformation model that minimizes bending energy to estimate a globally coherent warp from control-point correspondences, to align backprojected points from estimated depth with triangulated 3D control points, yielding calibrated backprojected points. By sampling these calibrated points near the control points, TWINGS provides a fast and geometrically accurate initialization for 3DGS, ultimately improving structural detail preservation and color fidelity in reconstructed scenes. Extensive experiments on DTU, LLFF, and Mip-NeRF360 demonstrate that TWINGS consistently outperforms existing methods, delivering detailed and accurate reconstructions under sparse-view scenarios.

  </details>

- **[Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935)**  
  *Peifeng Jiang, Hong Liu, Jin Jin, Wenshuai Wang, Xia Li*  
  `2026-05-21` · `cs.RO` · [abs](https://arxiv.org/abs/2605.21935) · [pdf](https://arxiv.org/pdf/2605.21935.pdf)
  > 💡 提出多模态交互场，联合不确定感知3DGS与动态更新，实现动态环境下人形机器人鲁棒导航，重定位成功率从12%提升至94%。

  <details><summary>Abstract</summary>

  Safe manipulation-oriented navigation for humanoid robots requires scene memory that remains reliable under locomotion-induced perceptual distortion, environmental changes, and interaction-level geometric safety constraints. Existing semantic mapping and scene-graph systems are difficult to deploy directly in this setting because they often assume stable camera trajectories, static environments, or coarse object geometry. We introduce the Multi-modal Interactive Field (MIF), a humanoid-oriented system that integrates confidence-aware semantic 3D Gaussian Splatting, discrepancy-triggered spatial memory updates, and task-driven geometric reconstruction within a closed-loop perception-adaptation pipeline. MIF couples three fields: an uncertainty-aware 3DGS Appearance Field that suppresses gait-induced blur, a Spatial Field that maintains topological memory, and a Geometry Field that supports Interaction Pose Safety (IPS) before manipulation. A discrepancy detection score is introduced to separate locomotion-induced false-positive changes from persistent changes and updates only locally inconsistent regions. On a Unitree-G1 humanoid in a real dynamic office, MIF improves relocation success in non-static environments from 12% to 94% compared with static scene-graph memory, while reducing semantic memory footprint by 91.4% through feature distillation for practical online operation. Project page and code: https://ziya-jiang.github.io/MIF-homepage/

  </details>

- **[Latent Dynamics for Full Body Avatar Animation](https://arxiv.org/abs/2605.21478)**  
  *Shichong Peng, Chengxiang Yin, Fei Jiang, Zhongshi Jiang, Lingchen Yang, Qingyang Tan, Amin Jourabloo, Jason Saragih, Ke Li, Christian Häne*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.21478) · [pdf](https://arxiv.org/pdf/2605.21478.pdf)
  > 💡 为松散衣物动态建模，提出基于3D高斯与transformer的潜在动力学残差模型，实现历史依赖、时间连贯且可控的全身动画。

  <details><summary>Abstract</summary>

  Pose-driven full-body avatars built on neural rendering produce high-quality novel views of a captured subject. Yet loose clothing and other dynamic elements deform in ways pose alone cannot explain: the same pose can correspond to many different states, because their motion depends on history, inertia, and contact. Explicit simulation and layered-garment methods can model such dynamics, but they require either a dedicated garment template, which raw multi-view capture does not naturally provide, or a test-time physics simulator with non-trivial runtime cost. A parallel line of work learns data-driven clothing avatars that avoid explicit garment layers. These methods add an auxiliary latent for variation beyond pose; at inference, they fix it, regress it from pose, or retrieve it from training data, without explicitly modeling how the latent evolves with its own dynamics. Additionally, even in everyday motion with loose clothing, existing architectures often struggle to capture fine-grained detail, producing blurry renderings and temporal artifacts. We augment a pose-conditioned 3D Gaussian avatar with a transformer-based decoder and a dynamics residual latent that captures temporal appearance and geometry variation beyond the driving signals. At inference, a learned latent dynamics model evolves the residual latent from a short pose history and the previous latent state. The model decomposes each update into driving, restoring, and dissipative forces, producing temporally coherent, history-dependent rollouts with negligible added cost. Different initial conditions yield diverse yet plausible motion trajectories, and the force decomposition exposes controls such as stiffness. Across nine captured sequences of everyday motion with diverse loose garments, quantitative metrics and a perceptual user study show improved animation quality over recent data-driven baselines.

  </details>

- **[Towards Physically Consistent 4D Scene Reconstruction for Closed-loop Autonomous Driving Simulation](https://arxiv.org/abs/2605.21032)**  
  *Bowyn Tan, Yutong Xie, Bai Huang, Fan Luo, Xiao Li, Naizheng Wang, Yang Guan, Shengbo Eben Li*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.21032) · [pdf](https://arxiv.org/pdf/2605.21032.pdf)
  > 💡 现有4DGS方法因空间-时间参数耦合导致低秩歧义，提出正交投影梯度与时序正则化实现物理一致重建。

  <details><summary>Abstract</summary>

  High-fidelity street scene reconstruction is pivotal for end-to-end autonomous driving simulation, where novel-view synthesis (NVS) and time-varying information modeling are two fundamental capabilities to facilitate closed-loop training. However, existing 3DGS methods and their 4D extensions fail to simultaneously achieve both. To bridge this gap, we establish an information-geometric diagnostic framework, revealing that this limitation stems from a credit assignment dilemma between spatial and temporal parameters. Specifically, the deterministic coupling between viewpoint and time in single-source observation creates a low-rank structure that induces massive null-space ambiguity between static view-dependent and dynamic time-varying components. Temporal information overshadows spatial cues, causing the estimation variance of spatial parameters to diverge. To address this issue, we propose Orthogonal Projected Gradient (OPG), a hierarchical training method designed to restore spatial identifiability. OPG prioritizes the integrity of spatial representations by securing them in an initial stage, then restricts temporal updates to the spatial null space, enabling proactive credit assignment. While OPG isolates temporal updates algebraically, Temporal Regularization Strategy is proposed to further refine the temporal solution space by imposing a smoothness constraint based on the physical prior of consistent appearance evolution, ensuring that the reconstructed scene remains physically consistent in closed-loop simulation. Extensive experiments demonstrate that our method not only maintains stable NVS capabilities but also demonstrates superior performance in traditional observation-reproducing metrics, which indirectly reflect the capability of modeling temporal dynamics.

  </details>

- **[FlowLong: Inference-time Long Video Generation via Manifold-constrained Tweedie Matching](https://arxiv.org/abs/2605.20910)**  
  *Jangho Park, Geon Yeong Park, Gihyun Kwon, Jong Chul Ye*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20910) · [pdf](https://arxiv.org/pdf/2605.20910.pdf)
  > 💡 用重叠滑动窗口和Tweedie匹配施加流形约束与时间一致性，随机早期采样同步轨迹，实现无

  <details><summary>Abstract</summary>

  Extending the generation horizon of video diffusion models to long sequences remains a long-standing and important challenge. Existing training-free approaches fall into two categories: extensions of bidirectional models, which are tightly coupled to specific architectures and suffer from quality degradation over long horizons, and autoregressive models, which accumulate drift errors due to exposure bias and tend to produce repetitive motion patterns. To address these issues, we propose a novel but simple inference-time approach for long video generation that is architecture-agnostic and requires no additional training. Our method generates long videos via overlapping sliding windows, where predicted clean samples from adjacent windows are blended via \emph{Tweedie matching} to enforce both \textbf{manifold constraint and temporal consistency} across overlap regions. \emph{Stochastic early-phase sampling} then synchronizes per-window trajectories by injecting fresh noise after each Tweedie matching correction in the high-noise phase, before transitioning to deterministic ODE sampling to preserve fine-grained visual fidelity. Applied to various video generation models, our method generates videos several times longer than the native window length while outperforming both training-free and autoregressive baselines in temporal consistency and visual quality, and further extends to audio-video joint generation and text-to-3DGS without any fine-tuning.

  </details>

- **[TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization](https://arxiv.org/abs/2605.20150)**  
  *Chonghao Zhong, Linfeng Shi, Hua Chen, Tiecheng Sun, Hao Zhao, Binhang Yuan, Chaojian Li*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20150) · [pdf](https://arxiv.org/pdf/2605.20150.pdf)
  > 💡 针对大规模3DGS训练内存瓶颈，提出TideGS框架，利用SSD-CPU-GPU层次存储和轨迹自适应差分流，单24GB GPU训练超十亿

  <details><summary>Abstract</summary>

  Training 3D Gaussian Splatting (3DGS) at billion-primitive scale is fundamentally memory-bound: each Gaussian primitive carries a large attribute vector, and the aggregate parameter table quickly exceeds GPU capacity, limiting prior systems to tens of millions of Gaussians on commodity single-GPU hardware. We observe that 3DGS training is inherently sparse and trajectory-conditioned: each iteration activates only the Gaussians visible from the current camera batch, so GPU memory can serve as a working-set cache rather than a persistent parameter store. Building on this insight, we introduce TideGS, an out-of-core training framework that manages parameters across an SSD-CPU-GPU hierarchy via three synergistic techniques: block-virtualized geometry for SSD-aligned spatial locality, a hierarchical asynchronous pipeline to overlap I/O with computation, and trajectory-adaptive differential streaming that transfers only incremental working-set deltas between iterations. Experiments show that TideGS enables training with over one billion Gaussians on a single 24 GB GPU while achieving the best reconstruction quality among evaluated single-GPU baselines on large-scale scenes, scaling beyond prior out-of-core baselines (e.g., approximately 100M Gaussians) and standard in-memory training (e.g., approximately 11M Gaussians).

  </details>

- **[PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis](https://arxiv.org/abs/2605.17916)**  
  *Jinrang Jia, Zhenjia Li, Yijiang Hu, Yifeng Shi*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.17916) · [pdf](https://arxiv.org/pdf/2605.17916.pdf)
  > 💡 将全屋全景合成建模为自回归节点生成，用3D外壳引导几何

  <details><summary>Abstract</summary>

  Generating a consistent whole-house VR tour from a floorplan and style reference requires both photorealistic panoramas and cross-view spatial coherence. Pure 2D generators produce appealing single panoramas but re-imagine geometry and materials when the viewpoint changes, whereas monolithic 3D generation becomes expensive and loses fine texture at multi-room scale. We introduce PanoWorld, a generative spatial world model that treats whole-house synthesis as autoregressive generation of node-based 360-degree panoramas, matching the discrete navigation used by real VR tour products. PanoWorld uses a floorplan-derived 3D shell as a global geometric proxy and a dynamic 3D Gaussian Splatting cache as renderable spatial memory. A feed-forward panoramic LRM designed for metric-scale multi-room 360-degree inputs lifts generated panoramas into local 3DGS updates, while Room-aware Group Attention suppresses cross-room feature interference. A topology-aware progressive caching strategy fuses these local updates without repeatedly reconstructing the full history. By decoupling shell-based geometry guidance from cache-rendered visual memory, PanoWorld preserves high-frequency 2D synthesis quality while improving cross-node layout and material consistency. The project link is https://jjrcn.github.io/PanoWorld-project-home/

  </details>

- **[Xiaomi Auto World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving](https://arxiv.org/abs/2605.18137)**  
  *Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu, Kaixin Xiong, Lei Gong, Zhanqian Wu, Zehan Zhang, Fangzhen Li, Hao Li, Yingying Shen, Jiale He, Haohui Zhu, Shan Zhao, Kai Wang, Zhiwei Zhan, Yuechuan Pu, Kaiyuan Tan, Ruiling Yang, Xianqi Wang, Tianyi Yan, Jiawei Zhou, Lei Zhang, Jingyang Zhao, Xi Zhou, Chitian Sun, Chenming Wu, Jiong Deng, Hongwei Xie, Ming Lu, Kun Ma, Long Chen, Guang Chen, Hangjun Ye, Bing Wang, Haiyang Sun*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18137) · [pdf](https://arxiv.org/pdf/2605.18137.pdf)
  > 💡 提出联合重建与生成的世界模型JWM，用稀疏查询和两阶段训练实现高保真场景表示与高效在线视频生成。

  <details><summary>Abstract</summary>

  This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.

  </details>

- **[CATRF: Codec-Adaptive TriPlane Radiance Fields for Volumetric Content Delivery](https://arxiv.org/abs/2605.18054)**  
  *Tung-I Chen, Lingdong Wang, Subhransu Maji, Ramesh K. Sitaraman*  
  `2026-05-18` · `eess.IV` · [abs](https://arxiv.org/abs/2605.18054) · [pdf](https://arxiv.org/pdf/2605.18054.pdf)
  > 💡 提出CATRF，用标准编解码器回路训练辐射场，自适应压缩失真，实现更低码率下更优率失真性能。

  <details><summary>Abstract</summary>

  Volumetric media promises next-generation content delivery applications, but its bandwidth demand remains a key bottleneck. Implicit and hybrid volumetric representations reduce model sizes, yet still require careful coding to reach 2D video-like bitrates. We present CATRF, a standard-codec-in-the-loop compression framework for plane-factorized radiance fields. During training, we quantize and pack 2D feature planes into codec-friendly canvases, run a standard codec roundtrip (JPEG/VP9/HEVC/AV1), then unpack and dequantize the decoded features before volume rendering. We use a straight-through estimator (STE) to insert the non-differentiable, standard codec pipeline into the training loop, allowing radiance-field features to adapt directly to the real, client-side codec distortions without introducing any learned codec parameters. On both static and dynamic benchmarks, CATRF consistently achieves a better rate-distortion trade-off over codec-agnostic and learned-codec-in-the-loop baselines, and also outperforms recent compressed 3DGS methods in both compression efficiency and decoding speed. These results highlight a practical path toward low-bitrate, compression-resilient volumetric representations for free-viewpoint video streaming.

  </details>

- **[GEM: Gaussian Evolution Model for Occupancy Forecasting and Motion Planning](https://arxiv.org/abs/2605.17682)**  
  *Cheng Chen, Hao Huang, Saurabh Bagchi*  
  `2026-05-17` · `cs.CV` · [abs](https://arxiv.org/abs/2605.17682) · [pdf](https://arxiv.org/pdf/2605.17682.pdf)
  > 💡 针对离散自回归占用预测的时序限制与误差累积，提出基于4D高斯原语的非自回归语义占用查询与运动规划模型，实现SOTA性能。

  <details><summary>Abstract</summary>

  Future 3D semantic occupancy forecasting and motion planning are central to autonomous driving, as they require models to reason about how surrounding scenes evolve and how the ego vehicle should act. Existing occupancy world models commonly discretize scenes into latent embeddings, volumetric features, or quantized tokens, and forecast future states through fixed-step autoregressive generation. This limits temporal flexibility, obscures scene evolution, accumulates errors over long horizons, and poorly matches the continuous-time dynamics of real driving scenes. We propose GEM, a Gaussian Evolution Model for non-autoregressive occupancy world modeling, where driving scenes are represented as explicit continuous 4D Gaussian primitives with learned dynamics. Instead of rolling out future occupancy states step by step, GEM directly queries the Gaussian world representation at arbitrary timestamps and splats the corresponding conditional 3D Gaussians into semantic occupancy volumes. This enables efficient forecasting over the full horizon while retaining a compact and interpretable scene representation. By decoupling spatial geometry, temporal support, and primitive motion, GEM makes the predicted world easier to inspect, as each primitive's evolution can be followed continuously over time. The same representation also supports motion planning by predicting future ego trajectories from the learned Gaussian world. Extensive experiments show that GEM achieves state-of-the-art future semantic occupancy forecasting and strong motion planning performance, while providing flexible temporal querying.

  </details>

- **[P2GS: Physical Prior-guided Gaussian Splatting for Photometrically Consistent Urban Reconstruction](https://arxiv.org/abs/2605.16925)**  
  *Kota Shimomura, Hidehisa Arai, Tsubasa Takahashi, Takayoshi Yamashita, Hironobu Fujiyoshi*  
  `2026-05-16` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16925) · [pdf](https://arxiv.org/pdf/2605.16925.pdf)
  > 💡 针对跨视角光度不一致，P2

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently emerged as a powerful explicit representation enabling fast, high-fidelity rendering, making it a promising foundation for closed-loop simulators and perception models in autonomous driving. However, conventional 3DGS implicitly assumes consistent exposure and tone mapping across views. Real driving data violates this assumption due to heterogeneous camera pipelines and dynamic outdoor illumination, baking exposure discrepancies and sensor noise into the radiance field and producing artifacts and inconsistent illumination especially in static backgrounds crucial for realistic simulation. These issues are amplified in autonomous driving, where sparse viewpoints, varying exposures, and outdoor lighting interact, while prior work mainly targets dynamic-object reconstruction and overlooks cross-view photometric consistency. To address this limitation, we introduce P2GS, a physically consistent Gaussian Splatting framework that jointly decomposes a view-invariant linear HDR radiance field, per-view exposure scales, and tone-mapping functions from only LDR images without HDR supervision. P2GS employs a unified optimization strategy grounded in the physical image-formation process, enforcing relative-exposure consistency and HDR-domain radiance regularization. This yields a radiance field robust to inter-camera illumination differences while preserving the real-time efficiency of standard 3DGS. Experiments across real and simulated driving environments show that P2GS matches or surpasses prior methods in LDR reconstruction while providing substantially improved photometric consistency, reliable exposure normalization, and physically coherent illumination across diverse scenes.

  </details>

- **[EndoGSim: Physics-Aware 4D Dynamic Endoscopic Scene Simulations via MLLM-Guided Gaussian Splatting](https://arxiv.org/abs/2605.16022)**  
  *Changjing Liu, Yiming Huang, Long Bai, Beilei Cui, Hongliang Ren*  
  `2026-05-15` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16022) · [pdf](https://arxiv.org/pdf/2605.16022.pdf)
  > 💡 通过MLLM引导4D高斯泼溅与可微分MPM，实现内窥镜场景的物理感知重建与高保真动态模拟。

  <details><summary>Abstract</summary>

  In robot-assisted minimally invasive surgery, high-fidelity dynamic endoscopic scene reconstruction and simulation are crucial to enhancing downstream tasks and advancing surgical outcomes. However, existing methods primarily focus on visual reconstruction, lacking physics-based descriptions of the scene required for realistic simulation. We propose a unified framework that achieves physics-aware reconstruction and physical simulation of endoscopic scenes through Multi-modal Large Language Models (MLLMs)-guided Gaussian Splatting. Our approach utilizes 4D Gaussian Splatting (4DGS) integrated with pre-trained segmentation and depth estimation to represent deformable tissues and tools. To achieve automatic inference of physical properties, we introduce an object-wise material field that initializes material parameters via MLLM and refines them through a differentiable Material Point Method (MPM) under joint supervision from rendered images and optical flow. Validated on both open-source and in-house datasets, our framework achieves superior simulation fidelity and physical accuracy compared to state-of-the-art methods, underscoring its potential to advance robot-assisted surgical applications.

  </details>

- **[Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes](https://arxiv.org/abs/2605.13591)**  
  *Kaicong Huang, Talha Azfar, Weisong Shi, Ruimin Ke*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13591) · [pdf](https://arxiv.org/pdf/2605.13591.pdf)
  > 💡 结合4DGS与可微MPM，实现物理感知、可编辑的动态驾驶场景合成，支持碰撞等极端情况。

  <details><summary>Abstract</summary>

  Reliable autonomous driving relies on large-scale, well-labeled data and robust models. However, manual data collection is resource-intensive, and traditional simulation suffers from a persistent reality gap. While recent generative frameworks and radiance-field methods improve visual fidelity, they still struggle with temporal and spatial consistency and cannot ensure physics-aware behavior, limiting their applicability to driving scenario generation. To address these challenges, we propose Real2Sim, an unified framework that combines 4D Gaussian Splatting (4DGS) with a differentiable Material Point Method (MPM) solver. Real2Sim explicitly reconstructs dynamic driving scenes as temporally continuous Gaussian primitives, supports instance-level editing, and simulates realistic object-object and object-environment interactions. This framework enables physics-aware, high-fidelity synthesis of diverse, editable scenarios, including challenging corner cases such as collisions and post-impact trajectories. Experiments on the Waymo Open Dataset validate Real2Sim's capabilities in rendering, reconstruction, editing, and physics simulation, demonstrating its potential as a scalable tool for data generation in downstream tasks such as perception, tracking, trajectory prediction, and end-to-end policy learning.

  </details>

- **[PointForward: Feedforward Driving Reconstruction through Point-Aligned Representations](https://arxiv.org/abs/2605.11594)**  
  *Cheng Chi, Xianqi Wang, Hongcheng Luo, Mingfei Tu, Gangwei Xu, Zehan Zhang, Bing Wang, Guang Chen, Hangjun Ye, Sida Peng, Xin Yang, Haiyang Sun*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11594) · [pdf](https://arxiv.org/pdf/2605.11594.pdf)
  > 💡 针对前馈驾驶重建的多视图不一致和动态建模问题，提出点对齐表示与场景图，实现显式跨视图一致与实例级运动传播，性能领先。

  <details><summary>Abstract</summary>

  High-fidelity reconstruction of driving scenes is crucial for autonomous driving. While recent feedforward 3D Gaussian Splatting (3DGS) methods enable fast reconstruction, their per-pixel Gaussian prediction paradigm often suffers from multi-view inconsistency and layering artifacts. Moreover, existing methods often model dynamic instances via dense flow prediction, which lacks explicit cross-view correspondence and instance-level consistency. In this paper, we propose PointForward, a feedforward driving reconstruction framework through point-aligned representations. Unlike pixel-aligned methods, we initialize sparse 3D queries in world space and aggregate multi-view image information via spatial-temporal fusion onto these queries, enforcing explicit cross-view consistency in a single feedforward pass. To handle scene dynamics, we introduce scene graphs that explicitly organize moving instances during reconstruction. By leveraging 3D bounding boxes, our method enables instance-level motion propagation and temporally consistent dynamic representations. Extensive experiments demonstrate that PointForward achieves state-of-the-art performance on large-scale driving benchmarks. The code will be available upon the publication of the paper.

  </details>

- **[3DGS$^3$: Joint Super Sampling and Frame Interpolation for Real-Time Large-Scale 3DGS Rendering](https://arxiv.org/abs/2605.11489)**  
  *Yibo Zhao, Fan Gao, Youcheng Cai, Ligang Liu*  
  `2026-05-12` · `cs.GR` · [abs](https://arxiv.org/abs/2605.11489) · [pdf](https://arxiv.org/pdf/2605.11489.pdf)
  > 💡 针对3D

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables high-quality real-time 3D rendering but faces challenges in efficiently scaling to ultra-dense scenes and high-resolution due to computational bottlenecks that limit its use in latency-sensitive applications. Instead of optimizing the splatting pipeline itself, we propose \textbf{3DGS$^3$}, a unified post-rendering framework that jointly performs super sampling and frame interpolation through differentiable processing of low-resolution outputs to achieve both high-resolution and high-frame-rate rendering. Our \textbf{Gradient\- \-Aware Super Sampling (GASS)} module leverages the continuous differentiability of 3DGS to extract image gradients that guide a GRU-based refinement network to enable high-fidelity super sampling. Furthermore, a \textbf{Lightweight Temporal Frame Interpolation (LTFI)} module based on a compact U-Net-like backbone fuses temporal and differentiable spatial cues from consecutive frames to synthesize temporally coherent intermediate frames. Experiments on public datasets demonstrate that 3DGS$^3$ achieves superior rendering efficiency and visual quality when compared with state-of-the-art methods and remains compatible with existing 3DGS acceleration techniques. The code will be publicly released upon acceptance.

  </details>

- **[DySurface: Consistent 4D Surface Reconstruction via Bridging Explicit Gaussians and Implicit Functions](https://arxiv.org/abs/2605.10360)**  
  *Minje Kim, Younghyun Noh, Jaesoon Kim, Tae-Kyun Kim*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10360) · [pdf](https://arxiv.org/pdf/2605.10360.pdf)
  > 💡 针对动态

  <details><summary>Abstract</summary>

  While novel view synthesis (NVS) for dynamic scenes has seen significant progress, reconstructing temporally consistent geometric surfaces remains a challenge. Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) offer powerful dynamic scene rendering capabilities; however, relying solely on photometric optimization often leads to geometric ambiguities. This results in discontinuous surfaces, severe artifacts, and broken surfaces over time. To address these limitations, we present DySurface, a novel framework that bridges the effectiveness of explicit Gaussians with the geometric fidelity of implicit Signed Distance Functions (SDFs) in dynamic scenes. Our approach tackles the structural discrepancy between the forward deformation of 3DGS ($canonical \rightarrow dynamic$) and the backward deformation required for volumetric SDF rendering ($dynamic \rightarrow canonical$). Specifically, we propose the VoxGS-DSDF branch that leverages deformed Gaussians to construct a dynamic sparse voxel grid, providing explicit geometric guidance to the implicit SDF field. This explicit anchoring effectively regularizes the volumetric rendering process, significantly improving surface reconstruction quality, with watertight boundaries and detailed representations. Quantitative and qualitative experiments demonstrate that DySurface significantly outperforms state-of-the-art baselines in geometric accuracy metrics while maintaining competitive rendering performance.

  </details>

- **[PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2605.10307)**  
  *Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10307) · [pdf](https://arxiv.org/pdf/2605.10307.pdf)
  > 💡 动态场景复杂运动重建中，提出PaMoSplat，结合部位感知与运动先验，实现高保真渲染、精准跟踪和快速收敛。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.

  </details>

- **[LagrangianSplats: Divergence-Free Transport of Gaussian Primitives for Fluid Reconstruction](https://arxiv.org/abs/2605.09299)**  
  *Ningxiao Tao, Baoquan Chen, Mengyu Chu*  
  `2026-05-10` · `cs.GR` · [abs](https://arxiv.org/abs/2605.09299) · [pdf](https://arxiv.org/pdf/2605.09299.pdf)
  > 💡 从稀疏2D视频重建流体使用散度自由核驱动3D高斯泼溅，保证不可压缩性和长程传输，滑动窗口优化提升精度。

  <details><summary>Abstract</summary>

  Reconstructing 3D fluid velocity fields from sparse 2D video observations is a highly ill-posed inverse problem, demanding both transport consistency with observed motion and physical validity under fluid laws. Existing methods typically impose these constraints through soft penalties, often leading to compromised accuracy and convergence issues. We introduce a reconstruction framework that structurally enforces both constraints. Specifically, we parameterize the reconstructed velocity using a continuous Divergence-Free Kernel representation, driving the advection of a Lagrangian 3D Gaussian Splatting representation. This formulation intrinsically guarantees both flow incompressibility and long-range transport coherence by construction. To enable the efficient optimization of such a constrained system, we introduce a novel Sliding Window scheme that propagates gradients over meaningful temporal horizons while maintaining tractable training costs. Experiments on synthetic and real-world datasets demonstrate that our method outperforms state-of-the-art baselines in both transport consistency and physical accuracy, enabling applications such as high-quality re-simulation and flow analysis.

  </details>

- **[CAGS: Color-Adaptive Volumetric Video Streaming with Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2605.09279)**  
  *Daheng Yin, Yili Jin, Jianxin Shi, Isaac Ding, Miao Zhang, Fangxin Wang, Zhaowu Huang, Cong Zhang, Jiangchuan Liu, Fang Dong*  
  `2026-05-10` · `cs.GR` · [abs](https://arxiv.org/abs/2605.09279) · [pdf](https://arxiv.org/pdf/2605.09279.pdf)
  > 💡 针对3DGS流中带宽与质量矛盾，提出矢量量化LoD及低分辨率参考图颜色校正方案，PSNR提升5~20dB。

  <details><summary>Abstract</summary>

  Volumetric video (VV) streaming enables real-time, immersive access to remote 3D environments, powering telepresence, ecological monitoring, and robotic teleoperation. These applications turn VV streaming into a real-time interface to remote physical environments, imposing new system-level demands for photorealistic scene representation, low-latency interaction, and robust performance under heterogeneous networks. 3D Gaussian Splatting (3DGS) has been widely used for real-time photorealistic rendering, offering superior visual quality and rendering performance, but it faces challenges due to bandwidth consumption. Furthermore, as the foundation of adaptive VV streaming, existing Levels of Detail (LoD) methods based on density are not well-suited to Gaussian representations, leading to visible gaps and severe quality degradation. Recent studies have also explored attribute compression techniques to reduce bandwidth consumption. Our preliminary studies reveal that aggressive attribute compression primarily causes color distortion, which can be effectively corrected in the rendered image using a reference image. Motivated by these findings, we propose a novel Color-Adaptive scheme for adaptive VV streaming that uses vector quantization (VQ) to establish LoDs and correct color distortions with low-resolution reference images. We further present CAGS, an adaptive VV streaming system compatible with diverse Gaussian representations, which integrates the Color-Adaptive scheme by rendering reference images on the streaming server and performing color restoration on the client. Extensive experiments on our prototype system demonstrate that CAGS outperforms the existing adaptive streaming systems in PSNR by 5$\sim$20 dB under fluctuating bandwidth, operates significantly faster than existing scalable Gaussian compression methods, and generalizes across different Gaussian representations.

  </details>

- **[Thin-Client Interactive Gaussian Adaptive Streaming over HTTP/3](https://arxiv.org/abs/2605.08699)**  
  *Emanuele Artioli, Philipp Fößl, Daniele Lorenzi, Farzad Tashtarian, Mahdi Dolati, Cheng-Hsin Hsu, Christian Timmerer*  
  `2026-05-09` · `eess.IV` · [abs](https://arxiv.org/abs/2605.08699) · [pdf](https://arxiv.org/pdf/2605.08699.pdf)
  > 💡 针对3DGS移动端计算与带宽瓶颈，提出TIGAS远程渲染框架，通过QUIC和ABR算法实现低延迟高质量流式传输。

  <details><summary>Abstract</summary>

  Recent advancements in 3D Gaussian Splatting (3DGS) have enabled photorealistic rendering of complex scenes, yet widespread adoption on mobile and Extended Reality (XR) devices is hindered by substantial computational and bandwidth requirements. While existing solutions often focus on model compression for client-side rendering, they still demand significant GPU power, limiting applicability on resource-constrained hardware. We propose TIGAS (Thin-client Interactive Gaussian Adaptive Streaming), a remote rendering framework offloading rasterization to a backend. To bypass the prohibitive latencies connected to fluctuating network conditions, TIGAS streams view-dependent 2D projections to a lightweight web client over QUIC, minimizing head-of-line (HoL) blocking. A dedicated ABR algorithm adapts rendering quality to fluctuating network conditions, maintaining motion-to-photon latency within strict 6DoF interactive constraints. Furthermore, we discuss the integration of an experimental WebGPU super-resolution pipeline to analyze the trade-offs between perceptual quality enhancements and thin-client processing bottlenecks. We extensively evaluate TIGAS across multi-continental environments using 14 3DGS models and real 6DoF EyeNavGS movement traces. Powered by a backend rendering frames in under 10 milliseconds, TIGAS maintains latency within interactive thresholds while achieving an average SSIM of 0.88, serving both as a robust testbed for 3DGS streaming research and a capable delivery system. The source code is available at: https://github.com/Rekenar/GaussianAdaptiveStreamer.

  </details>

- **[AsyncEvGS: Asynchronous Event-Assisted Gaussian Splatting for Handheld Motion-Blurred Scenes](https://arxiv.org/abs/2605.07192)**  
  *Jun Dai, Renbiao Jin, Bo Xu, Yutian Chen, Linning Xu, Mulin Yu, Tianfan Xue, Shi Guo*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07192) · [pdf](https://arxiv.org/pdf/2605.07192.pdf)
  > 💡 使用异步事件相机辅助3DGS，通过事件重建锐图和跨域位姿估计，解决手持运动

  <details><summary>Abstract</summary>

  3D reconstruction methods such as 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) achieve impressive photorealism but fail when input images suffer from severe motion blur. While event cameras provide high-temporal-resolution motion cues, existing event-assisted approaches rely on low-resolution sensors and strict synchronization, limiting their practicality for handheld 3D capture on common devices, such as smartphones. We introduce a flexible, high-resolution asynchronous RGB-Event dual-camera system and a corresponding reconstruction framework. Our approach first reconstructs sharp images from the event data and then employs a cross-domain pose estimation module based on the Visual Geometry Transformer (VGGT) to obtain robust initialization for 3DGS. During optimization, we employ a structure-driven event loss and view-specific consistency regularizers to mitigate the ill-posed behavior of traditional event losses and deblurring losses, ensuring both stable and high-fidelity reconstruction. We further contribute AsyncEv-Deblur, a new high-resolution RGB-Event dataset captured with our asynchronous system. Experiments demonstrate that our method achieves state-of-the-art performance on both our challenging dataset and existing benchmarks, substantially improving reconstruction robustness under severe motion blur. Project page: https://openimaginglab.github.io/AsyncEvGS/

  </details>

- **[ST-Gen4D: Embedding 4D Spatiotemporal Cognition into World Model for 4D Generation](https://arxiv.org/abs/2605.07390)**  
  *Haonan Wang, Hanyu Zhou, Tao Gu, Luxin Yan*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07390) · [pdf](https://arxiv.org/pdf/2605.07390.pdf)
  > 💡 现有4D生成模型忽视局部动态，ST-Gen4D通过构建4D认知图结合世界模型与扩散生成，实现结构合理且拓扑一致的4D高斯。

  <details><summary>Abstract</summary>

  Generative models have achieved success in producing apparently coherent 2D videos, but remain challenging in the physical world due to lack of 4D spatiotemporal scale. Typically, existing 4D generative models directly embed macro scale constraints to enhance overall spatiotemporal consistency. However, these methods only ensure global appearance coherence and fail to reveal the local dynamics of the physical world. Our insight is that global appearance structure and local dynamic topology empower 4D spatiotemporal cognition, thereby enabling 4D generation with spatiotemporal regularities. In this work, we propose ST-Gen4D, a 4D generation framework with 4D spatiotemporal cognition-based world model. Our model is guided by four key designs: 1) Spatiotemporal representation. We encode various modalities into multiple representations as a feature basis. 2) Spatiotemporal cognition. We sculpture these representations into global appearance graph and local dynamic graph, and fuse them via semantic-bridged spatiotemporal fusion to obtain a 4D cognition graph. 3) Spatiotemporal reasoning. We utilize a world model to derive future state based on the 4D cognition. 4) Spatiotemporal generation. We leverage the derived cognition as condition to guide latent diffusion for 4D Gaussian generation. By deeply integrating 4D intrinsic cognition with generative priors, our model guarantees the structural rationality and topological consistency of 4D generation. Moreover, we propose ST-4D datasets by aggregating public 4D datasets and self-built subset. Extensive experiments demonstrate the superiority of our ST-Gen4D across 3D and 4D generation tasks.

  </details>

- **[Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435)**  
  *Shuo Wang, Jilin Mei, Fuyang Liu, Wenfei Guan, Fanjie Kong, Zhihua Zhao, Shuai Wang, Chen Min, Yu Hu*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04435) · [pdf](https://arxiv.org/pdf/2605.04435.pdf)
  > 💡 针对越野场景4D重建中时序冲突问题，提出体素接地时序高斯聚合和表面法线正则化，提升质量并泛化到未知域。

  <details><summary>Abstract</summary>

  Feedforward Gaussian Splatting has recently emerged as an efficient paradigm for 4D reconstruction in autonomous driving. However, in unstructured off-road scenes, its performance degrades due to high-frequency geometry, ego-motion jitter, and increased non-rigid dynamics. These factors introduce conflicting Gaussian observations across timestamps, leading to either over-smoothed renderings or structural artifacts. To address this issue, we propose Ground4D, a spatially-grounded 4D feedforward framework for pose-free off-road reconstruction. The key idea is to resolve temporal conflicts through spatially localized conditioning. Specifically, we introduce voxel-grounded temporal Gaussian aggregation, which partitions the canonical Gaussian space into spatial voxels and performs query-conditioned temporal attention within each voxel. Intra-voxel softmax normalization ensures that temporal selectivity and spatial occupancy become mutually reinforcing rather than conflicting. We furthermore introduce surface normal cues as auxiliary geometric guidance to regularize the geometry of Gaussian primitives. Extensive experiments on ORAD-3D and RELLIS-3D demonstrate that Ground4D consistently outperforms existing feedforward methods in reconstruction quality and generalizes zero-shot to unseen off-road domains. Project page and code:https://github.com/wsnbws/Ground4D.

  </details>

- **[Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527)**  
  *Anagh Malik, Dorian Chan, Xiaoming Zhao, David B. Lindell, Oncel Tuzel, Jen-Hao Rick Chang*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04527) · [pdf](https://arxiv.org/pdf/2605.04527.pdf)
  > 💡 用编码器将动态点云压缩为形状token，经表面与高斯解码器学习4D几何外观，在生成跟踪等任务性能优异。

  <details><summary>Abstract</summary>

  We introduce a framework for learning latent representations of 4D objects which are descriptive, faithfully capturing object geometry and appearance; compressive, aiding in downstream efficiency; and accessible, requiring minimal input, i.e., an unstructured dynamic point cloud, to construct. Specifically, Velox trains an encoder to compress spatiotemporal color point clouds into a set of dynamic shape tokens. These tokens are supervised using two complementary decoders: a 4D surface decoder, which models the time-varying surface distribution capturing the geometry; and a Gaussian decoder, which maps the tokens to 3D Gaussians, helping learn appearance. To demonstrate the utility of our representation, we evaluate it across three downstream tasks -- video-to-4D generation, 3D tracking, and cloth simulation via image-to-4D generation -- and observe strong performances in all settings.

  </details>

- **[FreeTimeGS++: Secrets of Dynamic Gaussian Splatting and Their Principles](https://arxiv.org/abs/2605.03337)**  
  *Lucas Yunkyu Lee, Soonho Kim, Youngwook Kim, Sangmin Kim, Jaesik Park*  
  `2026-05-05` · `cs.CV` · [abs](https://arxiv.org/abs/2605.03337) · [pdf](https://arxiv.org/pdf/2605.03337.pdf)
  > 💡 分析4DGS隐藏驱动因素，发现时间分区与光度-时空差异，提出门控边缘化和神经速度场实现稳定动态重建。

  <details><summary>Abstract</summary>

  The recent surge in 4D Gaussian Splatting (4DGS) has achieved impressive dynamic scene reconstruction. While these methods demonstrate remarkable performance, the specific drivers behind such gains remain less explored, making a systematic understanding of the underlying principles challenging. In this paper, we perform a comprehensive analysis of these hidden factors to provide a clearer perspective on the 4DGS framework. We first establish a controlled baseline, FreeTimeGS_ours, by formalizing and reproducing the heuristics of the state-of-the-art FreeTimeGS. Using this framework, we dissect 4DGS along its fundamental axes and uncover key secrets, including the emergent temporal partitioning driven by Gaussian durations and the discrepancy between photometric fidelity and spatiotemporal consistency. Based on these insights, we propose FreeTimeGS++, a principled method that employs gated marginalization and neural velocity fields to achieve superior stability and robust dynamic representations. Our approach yields reproducible results with reduced run-to-run variance. We will release our implementation to provide a reliable foundation for future 4DGS research.

  </details>

- **[From Concept to Capability: Evaluating 3D Gaussian Splatting for Synthetic Scene Editing in Autonomous Driving](https://arxiv.org/abs/2605.01995)**  
  *Ali Nouri, Yifei Zhang, Yifan Zhang, Tayssir Bouraffa, Zhennan Fei, Zijian Han, Håkan Sivencrona, Anders Heyden*  
  `2026-05-03` · `cs.CV` · [abs](https://arxiv.org/abs/2605.01995) · [pdf](https://arxiv.org/pdf/2605.01995.pdf)
  > 💡 评估3DGS在自动驾驶安全场景重建中的保真度，提出系统分析框架，揭示多视角下车辆与行人的质量退化。

  <details><summary>Abstract</summary>

  The perception of an Autonomous Driving System (ADS) critically depends on relevant, comprehensive, and diverse datasets to ensure its safety while operating in the environment. Field data collection lacks completeness with respect to the list of rare but still possible safety-related scenarios needed for the development, verification, and validation of the ADS. 3D Gaussian Splatting (3DGS) has shown promising capabilities for the reconstruction and editing of scenes based on data collected by cameras and LiDAR sensors. However, the industrial fidelity evaluation of reconstructions is underexplored, which is crucial when employing such methods in safety-related systems, especially for ADS. This becomes more challenging as ADS operates in a dynamic, uncontrolled environment with limited viewpoints and often partially occluded objects. This paper addresses this gap by proposing and implementing a framework (Fig. 1) to systematically analyze the capabilities and limitations of 3DGS for use in the reconstruction of safety-related scenes. It focuses on the quality of reconstruction for vehicles and pedestrians, which are the two most critical object classes for ADS. Our findings provide industry insights into the fidelity degradation of reconstructions from multiple novel viewpoints, both lateral and longitudinal, enabling the integration of these methods into real-world industrial AD software development and testing pipelines.

  </details>

- **[A Principled Approach for Creating High-fidelity Synthetic Demonstrations for Imitation Learning](https://arxiv.org/abs/2605.01232)**  
  *Moniruzzaman Akash, Momotaz Begum*  
  `2026-05-02` · `cs.RO` · [abs](https://arxiv.org/abs/2605.01232) · [pdf](https://arxiv.org/pdf/2605.01232.pdf)
  > 💡 针对3DGS生成演示偏离专家轨迹的问题，提出以动态运动基元保留运动结构，并引入解析避障DMP直接操作密度场，实现高保真多样化合成。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled visually realistic demonstration generation from a single expert trajectory and a short multi-view scan. However, existing 3DGS-based synthesis pipelines typically generate new motions using sampling-based planners or trajectory optimization, which often deviate substantially from the expert's demonstrated path. While such deviations may be acceptable for tasks insensitive to motion shape, they discard subtle spatial and temporal structure that is critical for contact-rich and shape-sensitive manipulation, causing increased demonstration diversity to harm downstream policy learning. We argue that demonstration synthesis should treat the expert trajectory as a strong prior. Building on this principle, we propose a framework that synthesizes diverse task demonstrations while explicitly preserving expert motion structure. We model the expert trajectory using Dynamic Movement Primitives (DMPs) and retarget it to new goals, object configurations, and viewpoints within a reconstructed 3DGS scene, yielding phase-consistent, shape-preserving motion by construction. To safely realize this expert-preserving diversity in cluttered scenes, we introduce an analytic obstacle-aware DMP formulation that operates directly on the continuous density field induced by the 3DGS representation. This enables collision avoidance while minimally perturbing the nominal expert motion, unifying photorealistic rendering and geometric reasoning without additional scene representations. We evaluate our approach on a Spot mobile manipulator across three manipulation tasks with increasing sensitivity to trajectory fidelity. Compared to planner- and optimization-based synthesis, our method produces trajectories with lower deviation and collision rates and yields higher task success when training diffusion-based visuomotor policies.

  </details>

- **[Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179)**  
  *Andrea Dunn Beltran, Daniel Rho, Aarav Mehta, Xinqi Xiong, Raúl San José Estépar, Ron Alterovitz, Marc Niethammer, Roni Sengupta*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.28179) · [pdf](https://arxiv.org/pdf/2604.28179.pdf)
  > 💡 利用配对CT呼吸扫描建模变形空间，嵌入网格锚定高斯泼溅实现无屏气动态支气管镜重建，实现高精度定位与快速训练。

  <details><summary>Abstract</summary>

  Bronchoscopic navigation relies on registering endoscopic video to a preoperative CT scan, but respiratory motion deforms the airway by 5-20 mm, creating CT-to-body divergence that limits localization accuracy. In practice, this is mitigated through breath-hold protocols, which attempt to match the intraoperative anatomy to a static CT, but are difficult to reproduce and disrupt clinical workflow. We propose to eliminate the need for breath-hold protocols by leveraging patient-specific respiratory modeling. Paired inhale-exhale CT scans, already acquired for planning, implicitly define the patient-specific deformation space of the breathing airway. By registering these scans, we reduce respiratory motion to a single scalar breathing phase per frame, constraining all reconstructions to anatomically observed configurations. We embed this representation within a mesh-anchored Gaussian splatting framework, where a lightweight estimator infers breathing phase directly from endoscopic RGB, enabling continuous, deformation-aware reconstruction throughout the respiratory cycle without breath-holds or external sensing. To enable quantitative evaluation, we introduce RESPIRE, a physically grounded bronchoscopy simulation pipeline with per-frame ground truth for geometry, pose, breathing phase, and deformation. Experiments on RESPIRE show that our approach achieves geometrically faithful reconstruction, over 20x faster training, and 1.22 mm target localization accuracy (within the 3mm clinically relevant tolerances) outperforming unconstrained single-CT baselines. Please check out our website for additional visuals: https://asdunnbe.github.io/RESPIRE/

  </details>

- **[Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction](https://arxiv.org/abs/2604.26920)**  
  *David Novikov, Eilon Vaknin, Narek Tumanyan, Mark Sheinin*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26920) · [pdf](https://arxiv.org/pdf/2604.26920.pdf)
  > 💡 利用颜色编码照明将高速时序信息编码至低速相机图像，结合动态高斯泼溅解码重建高速体积场景。

  <details><summary>Abstract</summary>

  The task of capturing and rendering 3D dynamic scenes from 2D images has become increasingly popular in recent years. However, most conventional cameras are bandwidth-limited to 30-60 FPS, restricting these methods to static or slowly evolving scenes. While overcoming bandwidth limitations is difficult for general scenes, recent years have seen a flurry of computational imaging methods that yield high-speed videos using conventional cameras for specific applications (e.g., motion capture and particle image velocimetry). However, most of these methods require modifications to a camera's optics or the addition of mechanically moving components, limiting them to a single-view high-speed capture. Consequently, these methods cannot be readily used to capture a 3D representation of rapid scene motion. In this paper, we propose a novel method to capture and reconstruct a volumetric representation of a high-speed scene using only unaugmented low-speed cameras. Instead of modifying the hardware or optics of each individual camera, we encode high-speed scene dynamics by illuminating the scene with a rapid, sequential color-coded sequence. This results in simultaneous multi-view capture of the scene, where high-speed temporal information is encoded in the spatial intensity and color variations of the captured images. To construct a high-speed volumetric representation of the dynamic scene, we develop a novel dynamic Gaussian Splatting-based approach that decodes the temporal information from the images. We evaluate our approach on simulated scenes and real-world experiments using a multi-camera imaging setup, showing first-of-a-kind high-speed volumetric scene reconstructions.

  </details>

- **[Generalizable 3D Gaussian Splatting enabled Semantic Coding for Real-Time Immersive Video Communications](https://arxiv.org/abs/2604.25330)**  
  *Dingxi Yang, Wenqi Guo, Yue Liu, Jungong Han, Zhijin Qin*  
  `2026-04-28` · `eess.IV` · [abs](https://arxiv.org/abs/2604.25330) · [pdf](https://arxiv.org/pdf/2604.25330.pdf)
  > 💡 提出GS-SCNet统一框架，融合可泛化3DGS与语义编码，以视差引导编解码和轻量预测器实现高效实时沉浸式视频通信。

  <details><summary>Abstract</summary>

  Real-time immersive video communications, particularly high-fidelity 3D telepresence, necessitates a synergistic balance between instantaneous dynamic scene reconstruction and high-efficiency data transmission. While recent advancements in feed-forward 3D Gaussian Splatting (3DGS) have enabled real-time rendering, performing multi-view video coding and 3D reconstruction in a decoupled manner leads to suboptimal compression efficiency and high computational complexity. To address this, we propose GS-SCNet, the first unified end-to-end framework that seamlessly integrates generalizable 3DGS reconstruction with a dedicated deep Semantic Coding pipeline. Our architecture is underpinned by two core technical contributions: (i) we introduce a Disparity-Guided Parallel Semantic Codec that exploits epipolar geometric priors to facilitate cross-view contextual interaction via disparity compensation and semantic fusion, thereby enabling real-time parallel processing of stereo streams while significantly enhancing rate-distortion performance, and (ii) we develop a Lightweight Gaussian Parameter Predictor which directly projects decoded semantic latents into 3DGS attributes, obviating the need for intermediate pixel-domain reconstruction. By coupling the codec with the task-specific predictor, our framework extracts geometric correlations only once, effectively eliminating the redundant computational bottleneck inherent in conventional decoupled paradigms. Extensive evaluations on both synthetic and real-world human datasets demonstrate that GS-SCNet achieves a superior trade-off across compression efficiency, rendering quality, and real-time performance. Notably, our framework exhibits strong cross-domain generalization and robustness against compression artifacts when applied to out-of-domain real-world data, significantly outperforming conventional decoupled transmission paradigms.

  </details>

- **[Bringing a Personal Point of View: Evaluating Dynamic 3D Gaussian Splatting for Egocentric Scene Reconstruction](https://arxiv.org/abs/2604.23803)**  
  *Jan Warchocki, Xi Wang, Jonas Kulhanek, Jan van Gemert*  
  `2026-04-26` · `cs.CV` · [abs](https://arxiv.org/abs/2604.23803) · [pdf](https://arxiv.org/pdf/2604.23803.pdf)
  > 💡 评估动态3D

  <details><summary>Abstract</summary>

  Egocentric video provides a unique view into human perception and interaction, with growing relevance for augmented reality, robotics, and assistive technologies. However, rapid camera motion and complex scene dynamics pose major challenges for 3D reconstruction from this perspective. While 3D Gaussian Splatting (3DGS) has become a state-of-the-art method for efficient, high-quality novel view synthesis, variants, that focus on reconstructing dynamic scenes from monocular video are rarely evaluated on egocentric video. It remains unclear whether existing models generalize to this setting or if egocentric-specific solutions are needed. In this work, we evaluate dynamic monocular 3DGS models on egocentric and exocentric video using paired ego-exo recordings from the EgoExo4D dataset. We find that reconstruction quality is consistently lower in egocentric views. Analysis reveals that the difference in reconstruction quality, measured in peak signal-to-noise ratio, stems from the reconstruction of static, not dynamic, content. Our findings underscore current limitations and motivate the development of egocentric-specific approaches, while also highlighting the value of separately evaluating static and dynamic regions of a video.

  </details>

- **[Flow4DGS-SLAM: Optical Flow-Guided 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2604.22339)**  
  *Yunsong Wang, Gim Hee Lee*  
  `2026-04-24` · `cs.CV` · [abs](https://arxiv.org/abs/2604.22339) · [pdf](https://arxiv.org/pdf/2604.22339.pdf)
  > 💡 面向动态场景SLAM，提出光流引导的4DGS，通过运动掩码分离动态静态并显式建模时间中心与GMM，实现追踪、重建

  <details><summary>Abstract</summary>

  Handling the dynamic environments is a significant research challenge in Visual Simultaneous Localization and Mapping (SLAM). Recent research combines 3D Gaussian Splatting (3DGS) with SLAM to achieve both robust camera pose estimation and photorealistic renderings. However, using SLAM to efficiently reconstruct both static and dynamic regions remains challenging. In this work, we propose an efficient framework for dynamic 3DGS SLAM guided by optical flow. Using the input depth and prior optical flow, we first propose a category-agnostic motion mask generation strategy by fitting a camera ego-motion model to decompose the optical flow. This module separates dynamic and static Gaussians and simultaneously provides flow-guided camera pose initialization. We boost the training speed of dynamic 3DGS by explicitly modeling their temporal centers at keyframes. These centers are propagated using 3D scene flow priors and are dynamically initialized with an adaptive insertion strategy. Alongside this, we model the temporal opacity and rotation using a Gaussian Mixture Model (GMM) to adaptively learn the complex dynamics. The empirical results demonstrate our state-of-the-art performance in tracking, dynamic reconstruction, and training efficiency.

  </details>

- **[EvFlow-GS: Event Enhanced Motion Deblurring with Optical Flow for 3D Gaussian Splatting](https://arxiv.org/abs/2604.22183)**  
  *Feiyu An, Yufei Deng, Zihui Zhang, Rong Xiao*  
  `2026-04-24` · `cs.CV` · [abs](https://arxiv.org/abs/2604.22183) · [pdf](https://arxiv.org/pdf/2604.22183.pdf)
  > 💡 利用事件流与光流联合优化可学习双重积分和3DGS，提出新事件损失和残差先验，实现高质量运动去模糊三维重建。

  <details><summary>Abstract</summary>

  Achieving sharp 3D reconstruction from motion-blurred images alone becomes challenging, motivating recent methods to incorporate event cameras, benefiting from microsecond temporal resolution. However, they suffer from residual artifacts and blurry texture details due to misleading supervision from inaccurate event double integral priors and noisy, blurry events. In this study, we propose EvFlow-GS, a unified framework that leverages event streams and optical flow to optimize an end-to-end learnable double integral (LDI), camera poses, and 3D Gaussian Splatting (3DGS) jointly on-the-fly. Specifically, we first extract edge information from the events using optical flow and then formulate a novel event-based loss applied separately to different modules. Additionally, we exploit a novel event-residual prior to strengthen the supervision of intensity changes between images rendered from 3DGS. Finally, we integrate the outputs of both 3DGS and LDI into a joint loss, enabling their optimization to mutually facilitate each other. Experiments demonstrate the leading performance of our EvFlow-GS.

  </details>

- **[GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784)**  
  *Zhenlong Wu, Zihan Zheng, Xuanxuan Wang, Qianhe Wang, Hua Yang, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang*  
  `2026-04-22` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20784) · [pdf](https://arxiv.org/pdf/2604.20784.pdf)
  > 💡 针对动态稀疏视图重建的几何崩溃问题，提出结合3D一致性与扩散整流器的闭环优化框架，实现高保真度和时空一致性。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from sparse multi-view videos is highly ill-posed, often leading to geometric collapse, trajectory drift, and floating artifacts. Recent attempts introduce generative priors to hallucinate missing content, yet naive integration frequently causes structural drift and temporal inconsistency due to the mismatch between stochastic 2D generation and deterministic 3D geometry. In this paper, we propose GeoRect4D, a novel unified framework for sparse-view dynamic reconstruction that couples explicit 3D consistency with generative refinement via a closed-loop optimization process. Specifically, GeoRect4D introduces a degradation-aware feedback mechanism that incorporates a robust anchor-based dynamic 3DGS substrate with a single-step diffusion rectifier to hallucinate high-fidelity details. This rectifier utilizes a structural locking mechanism and spatiotemporal coordinated attention, effectively preserving physical plausibility while restoring missing content. Furthermore, we present a progressive optimization strategy that employs stochastic geometric purification to eliminate floaters and generative distillation to infuse texture details into the explicit representation. Extensive experiments demonstrate that GeoRect4D achieves state-of-the-art performance in reconstruction fidelity, perceptual quality, and spatiotemporal consistency across multiple datasets.

  </details>

- **[High-Fidelity 3D Gaussian Human Reconstruction via Region-Aware Initialization and Geometric Priors](https://arxiv.org/abs/2604.21714)**  
  *Yang Liu, Zhiyong Zhang*  
  `2026-04-20` · `cs.MM` · [abs](https://arxiv.org/abs/2604.21714) · [pdf](https://arxiv.org/pdf/2604.21714.pdf)
  > 💡 针对动态人体重建细节丢失和伪影问题，提出结合SMPL-X区域感知初始化与几何先验的3D高斯方法，实现高质量

  <details><summary>Abstract</summary>

  Real-time, high-fidelity 3D human reconstruction from RGB images is essential for interactive applications such as virtual reality and gaming, yet remains challenging due to the complex non-rigid deformations of dynamic human bodies. Although 3D Gaussian Splatting enables efficient rendering, existing methods struggle to capture fine geometric details and often produce artifacts such as fused fingers and over-smoothed faces. Moreover, conventional spatial-field-based dynamic modeling faces a trade-off between reconstruction fidelity and GPU memory consumption. To address these issues, we propose a novel 3D Gaussian human reconstruction framework that combines region-aware initialization with rich geometric priors. Specifically, we leverage the expressive SMPL-X model to initialize both 3D Gaussians and skinning weights, providing a robust geometric foundation for precise reconstruction. We further introduce a region-aware density initialization strategy and a geometry-aware multi-scale hash encoding module to improve local detail recovery while maintaining computational efficiency.Experiments on PeopleSnapshot and GalaBasketball show that our method achieves superior reconstruction quality and finer detail preservation under complex motions, while maintaining real-time rendering speed.

  </details>

- **[GS-STVSR: Ultra-Efficient Continuous Spatio-Temporal Video Super-Resolution via 2D Gaussian Splatting](https://arxiv.org/abs/2604.18047)**  
  *Mingyu Shi, Xin Di, Long Peng, Boxiang Cao, Anran Wu, Zhanfeng Feng, Jiaming Guo, Renjing Pei, Xueyang Fu, Yang Cao, Zhengjun Zha*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18047) · [pdf](https://arxiv.org/pdf/2604.18047.pdf)
  > 💡 针对连续时空视频超分存在的低效密集查询问题，提出基于2D高斯泼溅的GS-STVSR框架，通过运动建模驱动高斯核演化，实现高质量、近乎恒定时间的超高效推理。

  <details><summary>Abstract</summary>

  Continuous Spatio-Temporal Video Super-Resolution (C-STVSR) aims to simultaneously enhance the spatial resolution and frame rate of videos by arbitrary scale factors, offering greater flexibility than fixed-scale methods that are constrained by predefined upsampling ratios. In recent years, methods based on Implicit Neural Representations (INR) have made significant progress in C-STVSR by learning continuous mappings from spatio-temporal coordinates to pixel values. However, these methods fundamentally rely on dense pixel-wise grid queries, causing computational cost to scale linearly with the number of interpolated frames and severely limiting inference efficiency. We propose GS-STVSR, an ultra-efficient C-STVSR framework based on 2D Gaussian Splatting (2D-GS) that drives the spatiotemporal evolution of Gaussian kernels through continuous motion modeling, bypassing dense grid queries entirely. We exploit the strong temporal stability of covariance parameters for lightweight intermediate fitting, design an optical flow-guided motion module to derive Gaussian position and color at arbitrary time steps, introduce a Covariance resampling alignment module to prevent covariance drift, and propose an adaptive offset window for large-scale motion. Extensive experiments on Vid4, GoPro, and Adobe240 show that GS-STVSR achieves state-of-the-art quality across all benchmarks. Moreover, its inference time remains nearly constant at conventional temporal scales (X2--X8) and delivers over X3 speedup at extreme scales X32, demonstrating strong practical applicability.

  </details>

- **[D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082)**  
  *Xingyuan Yu, Yijin Li, Chong Zeng, Yuhang Ming, Hujun Bao, Guofeng Zhang*  
  `2026-04-18` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17082) · [pdf](https://arxiv.org/pdf/2604.17082.pdf)
  > 💡 针对结构化动态物体，通过可微基元绑定3DGS与变形网络及自适应控制，实现高保真几何与运动联合建模。

  <details><summary>Abstract</summary>

  Capturing both geometry and rigid motion for structured dynamic objects, like multi-part assemblies or jointed mechanisms, remains a key challenge. Existing dynamic methods, such as deformable meshes or 3DGS, rely on unstructured representations and fail to jointly model suitable geometry and articulated motion. Primitive-based methods excel at structured static scenes, but their dynamic potential is still unexplored. We propose D-Prism, the first framework to achieve high-fidelity structured dynamic modeling by extending differentiable primitives to the dynamic domain. Specifically, we bind 3DGS to primitive surfaces, leveraging their respective strengths in appearance and geometry. We introduce a deformation network to control primitive motion, ensuring it accurately matches the object's movement. Furthermore, we design a novel adaptive control strategy to dynamically adjust primitive counts, better matching objects' true spatial footprint. Experiments confirm that our method excels at structured dynamic modeling, providing both structured geometry and precise motion tracking.

  </details>

- **[Splats in Splats++: Robust and Generalizable 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2604.15862)**  
  *Yijia Guo, Wenkai Huang, Tong Hu, Gaolei Li, Yang Li, Yuxin Hong, Liwen Hu, Xitong Ling, Jianhua Li, Shengbo Chen, Tiejun Huang, Lei Ma*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15862) · [pdf](https://arxiv.org/pdf/2604.15862.pdf)
  > 💡 针对3DGS隐写，提出基于SH重要性加密与哈希网格引导不透明度映射的框架，实现高容量、鲁棒且快速的不可感知信息嵌入。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently redefined the paradigm of 3D reconstruction, striking an unprecedented balance between visual fidelity and computational efficiency. As its adoption proliferates, safeguarding the copyright of explicit 3DGS assets has become paramount. However, existing invisible message embedding frameworks struggle to reconcile secure and high-capacity data embedding with intrinsic asset utility, often disrupting the native rendering pipeline or exhibiting vulnerability to structural perturbations. In this work, we present \textbf{\textit{Splats in Splats++}}, a unified and pipeline-agnostic steganography framework that seamlessly embeds high-capacity 3D/4D content directly within the native 3DGS representation. Grounded in a principled analysis of the frequency distribution of Spherical Harmonics (SH), we propose an importance-graded SH coefficient encryption scheme that achieves imperceptible embedding without compromising the original expressive power. To fundamentally resolve the geometric ambiguities that lead to message leakage, we introduce a \textbf{Hash-Grid Guided Opacity Mapping} mechanism. Coupled with a novel \textbf{Gradient-Gated Opacity Consistency Loss}, our formulation enforces a stringent spatial-attribute coupling between the original and hidden scenes, effectively projecting the discrete attribute mapping into a continuous, attack-resilient latent manifold. Extensive experiments demonstrate that our method substantially outperforms existing approaches, achieving up to \textbf{6.28 db} higher message fidelity, \textbf{3$\times$} faster rendering, and exceptional robustness against aggressive 3D-targeted structural attacks (e.g., GSPure). Furthermore, our framework exhibits remarkable versatility, generalizing seamlessly to 2D image embedding, 4D dynamic scene steganography, and diverse downstream tasks.

  </details>

- **[TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens](https://arxiv.org/abs/2604.15239)**  
  *Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang, Zan Gojcic*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15239) · [pdf](https://arxiv.org/pdf/2604.15239.pdf)
  > 💡 针对传统沿射线回归深度的缺陷，提出直接预测3D坐标的可学习高斯令牌编码-解码架构，实现解耦预测与更优重建。

  <details><summary>Abstract</summary>

  In this work, we revisit several key design choices of modern Transformer-based approaches for feed-forward 3D Gaussian Splatting (3DGS) prediction. We argue that the common practice of regressing Gaussian means as depths along camera rays is suboptimal, and instead propose to directly regress 3D mean coordinates using only a self-supervised rendering loss. This formulation allows us to move from the standard encoder-only design to an encoder-decoder architecture with learnable Gaussian tokens, thereby unbinding the number of predicted primitives from input image resolution and number of views. Our resulting method, TokenGS, demonstrates improved robustness to pose noise and multiview inconsistencies, while naturally supporting efficient test-time optimization in token space without degrading learned priors. TokenGS achieves state-of-the-art feed-forward reconstruction performance on both static and dynamic scenes, producing more regularized geometry and more balanced 3DGS distribution, while seamlessly recovering emergent scene attributes such as static-dynamic decomposition and scene flow.

  </details>

- **[One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782)**  
  *Yuan Sun, Xuan Wang, WeiLi Zhang, Wenxuan Zhang, Yu Guo, Fei Wang*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.14782) · [pdf](https://arxiv.org/pdf/2604.14782.pdf)
  > 💡 单张图像构建可动3D头像，显式解耦头发与面部，分别用FLAME网格和PBD笼控制变形，实现逼真头发动态。

  <details><summary>Abstract</summary>

  We propose a compositional method for constructing a complete 3D head avatar from a single image. Prior one-shot holistic approaches frequently fail to produce realistic hair dynamics during animation, largely due to inadequate decoupling of hair from the facial region, resulting in entangled geometry and unnatural deformations. Our method explicitly decouples hair from the face, modeling these components using distinct deformation paradigms while integrating them into a unified rendering pipeline. Furthermore, by leveraging image-to-3D lifting techniques, we preserve fine-grained textures from the input image to the greatest extent possible, effectively mitigating the common issue of high-frequency information loss in generalized models. Specifically, given a frontal portrait image, we first perform hair removal to obtain a bald image. Both the original image and the bald image are then lifted to dense, detail-rich 3D Gaussian Splatting (3DGS) representations. For the bald 3DGS, we rig it to a FLAME mesh via non-rigid registration with a prior model, enabling natural deformation that follows the mesh triangles during animation. For the hair component, we employ semantic label supervision combined with a boundary-aware reassignment strategy to extract a clean and isolated set of hair Gaussians. To control hair deformation, we introduce a cage structure that supports Position-Based Dynamics (PBD) simulation, allowing realistic and physically plausible transformations of the hair Gaussian primitives under head motion, gravity, and inertial effects. Striking qualitative results, including dynamic animations under diverse head motions, gravity effects, and expressions, showcase substantially more realistic hair behavior alongside faithfully preserved facial details, outperforming state-of-the-art one-shot methods in perceptual realism.

  </details>

- **[4D Radar Gaussian Modeling and Scan Matching with RCS](https://arxiv.org/abs/2604.14868)**  
  *Fernando Amodeo, Luis Merino, Fernando Caballero*  
  `2026-04-16` · `cs.RO` · [abs](https://arxiv.org/abs/2604.14868) · [pdf](https://arxiv.org/pdf/2604.14868.pdf)
  > 💡 针对4D雷达RCS被忽视问题，提出融合RCS物理特性的高斯建模与扫描匹配方法，提升匹配鲁棒性。

  <details><summary>Abstract</summary>

  4D millimeter-wave (mmWave) radars are increasingly used in robotics, as they offer robustness against adverse environmental conditions. Besides the usual XYZ position, they provide Doppler velocity measurements as well as Radar Cross Section (RCS) information for every point. While Doppler is widely used to filter out dynamic points, RCS is often overlooked and not usually used in modeling and scan matching processes. Building on previous 3D Gaussian modeling and scan matching work, we propose incorporating the physical behavior of RCS in the model, in order to further enrich the summarized information about the scene, and improve the scan matching process.

  </details>

- **[ClipGStream: Clip-Stream Gaussian Splatting for Any Length and Any Motion Multi-View Dynamic Scene Reconstruction](https://arxiv.org/abs/2604.13746)**  
  *Jie Liang, Jiahao Wu, Chao Wang, Jiayu Yang, Xiaoyun Zheng, Kaiqiang Xiong, Zhanke Wang, Jinbo Yan, Feng Gao, Ronggang Wang*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13746) · [pdf](https://arxiv.org/pdf/2604.13746.pdf)
  > 💡 针对长序列大运动动态场景，提出Clip-Stream高斯混合优化，用clip级时空场与残差锚点实现可扩展无闪烁高质量重建。

  <details><summary>Abstract</summary>

  Dynamic 3D scene reconstruction is essential for immersive media such as VR, MR, and XR, yet remains challenging for long multi-view sequences with large-scale motion. Existing dynamic Gaussian approaches are either Frame-Stream, offering scalability but poor temporal stability, or Clip, achieving local consistency at the cost of high memory and limited sequence length. We propose ClipGStream, a hybrid reconstruction framework that performs stream optimization at the clip level rather than the frame level. The sequence is divided into short clips, where dynamic motion is modeled using clip-independent spatio-temporal fields and residual anchor compensation to capture local variations efficiently, while inter-clip inherited anchors and decoders maintain structural consistency across clips. This Clip-Stream design enables scalable, flicker-free reconstruction of long dynamic videos with high temporal coherence and reduced memory overhead. Extensive experiments demonstrate that ClipGStream achieves state-of-the-art reconstruction quality and efficiency. The project page is available at: https://liangjie1999.github.io/ClipGStreamWeb/

  </details>

- **[RobotPan: A 360$^\circ$ Surround-View Robotic Vision System for Embodied Perception](https://arxiv.org/abs/2604.13476)**  
  *Jiahao Ma, Qiang Zhang, Peiran Liu, Zeran Su, Pihai Sun, Gang Han, Wen Zhao, Wei Cui, Zhang Zhang, Zhiyuan Xu, Renjing Xu, Jian Tang, Miaomiao Liu, Yijie Guo*  
  `2026-04-15` · `cs.RO` · [abs](https://arxiv.org/abs/2604.13476) · [pdf](https://arxiv.org/pdf/2604.13476.pdf)
  > 💡 现有机器人视觉系统视野窄、易抖动，提出RobotPan结合六相机与LiDAR，用稀疏视图预测度量尺度的紧凑3D高斯实现360度实时渲染与重建。

  <details><summary>Abstract</summary>

  Surround-view perception is increasingly important for robotic navigation and loco-manipulation, especially in human-in-the-loop settings such as teleoperation, data collection, and emergency takeover. However, current robotic visual interfaces are often limited to narrow forward-facing views, or, when multiple on-board cameras are available, require cumbersome manual switching that interrupts the operator's workflow. Both configurations suffer from motion-induced jitter that causes simulator sickness in head-mounted displays. We introduce a surround-view robotic vision system that combines six cameras with LiDAR to provide full 360$^\circ$ visual coverage, while meeting the geometric and real-time constraints of embodied deployment. We further present \textsc{RobotPan}, a feed-forward framework that predicts \emph{metric-scaled} and \emph{compact} 3D Gaussians from calibrated sparse-view inputs for real-time rendering, reconstruction, and streaming. \textsc{RobotPan} lifts multi-view features into a unified spherical coordinate representation and decodes Gaussians using hierarchical spherical voxel priors, allocating fine resolution near the robot and coarser resolution at larger radii to reduce computational redundancy without sacrificing fidelity. To support long sequences, our online fusion updates dynamic content while preventing unbounded growth in static regions by selectively updating appearance. Finally, we release a multi-sensor dataset tailored to 360$^\circ$ novel view synthesis and metric 3D reconstruction for robotics, covering navigation, manipulation, and locomotion on real platforms. Experiments show that \textsc{RobotPan} achieves competitive quality against prior feed-forward reconstruction and view-synthesis methods while producing substantially fewer Gaussians, enabling practical real-time embodied deployment.

  </details>

- **[GGD-SLAM: Monocular 3DGS SLAM Powered by Generalizable Motion Model for Dynamic Environments](https://arxiv.org/abs/2604.12837)**  
  *Yi Liu, Haoxuan Xu, Hongbo Duan, Keyu Fan, Zhengyang Zhang, Peiyu Zhuang, Pengting Luo, Houde Liu*  
  `2026-04-14` · `cs.RO` · [abs](https://arxiv.org/abs/2604.12837) · [pdf](https://arxiv.org/pdf/2604.12837.pdf)
  > 💡 针对动态环境单目SLAM位姿估计和密集重建退化问题，提出通用运动模型、动态语义分离与遮挡填充，实现性能领先。

  <details><summary>Abstract</summary>

  Visual SLAM algorithms achieve significant improvements through the exploration of 3D Gaussian Splatting (3DGS) representations, particularly in generating high-fidelity dense maps. However, they depend on a static environment assumption and experience significant performance degradation in dynamic environments. This paper presents GGD-SLAM, a framework that employs a generalizable motion model to address the challenges of localization and dense mapping in dynamic environments - without predefined semantic annotations or depth input. Specifically, the proposed system employs a First-In-First-Out (FIFO) queue to manage incoming frames, facilitating dynamic semantic feature extraction through a sequential attention mechanism. This is integrated with a dynamic feature enhancer to separate static and dynamic components. Additionally, to minimize dynamic distractors' impact on the static components, we devise a method to fill occluded areas via static information sampling and design a distractor-adaptive Structure Similarity Index Measure (SSIM) loss tailored for dynamic environments, significantly enhancing the system's resilience. Experiments conducted on real-world dynamic datasets demonstrate that the proposed system achieves state-of-the-art performance in camera pose estimation and dense reconstruction in dynamic scenes.

  </details>

- **[Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.12626)**  
  *Ziyuan Xia, Jingyi Xu, Chong Cui, Yuanhong Yu, Jiazhao Zhang, Qingsong Yan, Tao Ni, Junbo Chen, Xiaowei Zhou, Hujun Bao, Ruizhen Hu, Sida Peng*  
  `2026-04-14` · `cs.RO` · [abs](https://arxiv.org/abs/2604.12626) · [pdf](https://arxiv.org/pdf/2604.12626.pdf)
  > 💡 集成3DGS渲染与可驱动高斯化身，实现高保真动态导航模拟，提升跨域泛化和人类感知能力。

  <details><summary>Abstract</summary>

  Training embodied AI agents depends critically on the visual fidelity of simulation environments and the ability to model dynamic humans. Current simulators rely on mesh-based rasterization with limited visual realism, and their support for dynamic human avatars, where available, is constrained to mesh representations, hindering agent generalization to human-populated real-world scenarios. We present Habitat-GS, a navigation-centric embodied AI simulator extended from Habitat-Sim that integrates 3D Gaussian Splatting scene rendering and drivable gaussian avatars while maintaining full compatibility with the Habitat ecosystem. Our system implements a 3DGS renderer for real-time photorealistic rendering and supports scalable 3DGS asset import from diverse sources. For dynamic human modeling, we introduce a gaussian avatar module that enables each avatar to simultaneously serve as a photorealistic visual entity and an effective navigation obstacle, allowing agents to learn human-aware behaviors in realistic settings. Experiments on point-goal navigation demonstrate that agents trained on 3DGS scenes achieve stronger cross-domain generalization, with mixed-domain training being the most effective strategy. Evaluations on avatar-aware navigation further confirm that gaussian avatars enable effective human-aware navigation. Finally, performance benchmarks validate the system's scalability across varying scene complexity and avatar counts.

  </details>

- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251)**  
  *Xinliang Wang, Yifeng Shi, Zhenyu Wu*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.12251) · [pdf](https://arxiv.org/pdf/2604.12251.pdf)
  > 💡 针对3DGS稀疏视图退化，用大规模视频数据扩展和同构双模型范式的视频扩散及热图引导修复，实现SOTA性能。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) delivers high-fidelity real-time rendering but suffers from geometric and photometric degradations under sparse-view constraints. Current generative restoration approaches are often limited by insufficient temporal coherence, a lack of explicit spatial constraints, and a lack of large-scale training data, resulting in multi-view inconsistencies, erroneous geometric hallucinations, and limited generalization to diverse real-world artifact distributions. In this paper, we present ArtifactWorld, a framework that resolves 3DGS artifact repair through systematic data expansion and a homogeneous dual-model paradigm. To address the data bottleneck, we establish a fine-grained phenomenological taxonomy of 3DGS artifacts and construct a comprehensive training set of 107.5K diverse paired video clips to enhance model robustness. Architecturally, we unify the restoration process within a video diffusion backbone, utilizing an isomorphic predictor to localize structural defects via an artifact heatmap. This heatmap then guides the restoration through an Artifact-Aware Triplet Fusion mechanism, enabling precise, intensity-guided spatio-temporal repair within native self-attention. Extensive experiments demonstrate that ArtifactWorld achieves state-of-the-art performance in sparse novel view synthesis and robust 3D reconstruction. Code and dataset will be made public.

  </details>

- **[Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis](https://arxiv.org/abs/2604.11685)**  
  *Yuqin Lu, Yang Zhou, Yihua Dai, Guiqing Li, Shengfeng He*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11685) · [pdf](https://arxiv.org/pdf/2604.11685.pdf)
  > 💡 通过自顶向下的可学习掩码剪枝和层次空间网格与共享锚点码本，实现紧凑多级LOD的3DGS高效渐进渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become a state-of-the-art framework for real-time, high-fidelity novel view synthesis. However, its substantial storage requirements and inherently unstructured representation pose challenges for deployment in streaming and resource-constrained environments. Existing Level-of-Detail (LOD) strategies, particularly those based on bottom-up construction, often introduce redundancy or lead to fidelity degradation. To overcome these limitations, we propose Iterative Gaussian Synopsis, a novel framework for compact and progressive rendering through a top-down "unfolding" scheme. Our approach begins with a full-resolution 3DGS model and iteratively derives coarser LODs using an adaptive, learnable mask-based pruning mechanism. This process constructs a multi-level hierarchy that preserves visual quality while improving efficiency. We integrate hierarchical spatial grids, which capture the global scene structure, with a shared Anchor Codebook that models localized details. This combination produces a compact yet expressive feature representation, designed to minimize redundancy and support efficient, level-specific adaptation. The unfolding mechanism promotes inter-layer reusability and requires only minimal data overhead for progressive refinement. Experiments show that our method maintains high rendering quality across all LODs while achieving substantial storage reduction. These results demonstrate the practicality and scalability of our approach for real-time 3DGS rendering in bandwidth- and memory-constrained scenarios.

  </details>

- **[4D Vessel Reconstruction for Benchtop Thrombectomy Analysis](https://arxiv.org/abs/2604.06671)**  
  *Ethan Nguyen, Javier Carmona, Arisa Matsuzaki, Naoki Kaneko, Katsushi Arisaka*  
  `2026-04-08` · `eess.IV` · [abs](https://arxiv.org/abs/2604.06671) · [pdf](https://arxiv.org/pdf/2604.06671.pdf)
  > 💡 多相机4D高斯泼溅重建硅胶血管模型，实现时间分辨位移与应力代理测量，支持血栓切除台架分析。

  <details><summary>Abstract</summary>

  Introduction: Mechanical thrombectomy can cause vessel deformation and procedure-related injury. Benchtop models are widely used for device testing, but time-resolved, full-field 3D vessel-motion measurements remain limited. Methods: We developed a nine-camera, low-cost multi-view workflow for benchtop thrombectomy in silicone middle cerebral artery phantoms (2160p, 20 fps). Multi-view videos were calibrated, segmented, and reconstructed with 4D Gaussian Splatting. Reconstructed point clouds were converted to fixed-connectivity edge graphs for region-of-interest (ROI) displacement tracking and a relative surface-based stress proxy. Stress-proxy values were derived from edge stretch using a Neo-Hookean mapping and reported as comparative surface metrics. A synthetic Blender pipeline with known deformation provided geometric and temporal validation. Results: In synthetic bulk translation, the stress proxy remained near zero for most edges (median $\approx$ 0 MPa; 90th percentile 0.028 MPa), with sparse outliers. In synthetic pulling (1-5 mm), reconstruction showed close geometric and temporal agreement with ground truth, with symmetric Chamfer distance of 1.714-1.815 mm and precision of 0.964-0.972 at $τ= 1$ mm. In preliminary benchtop comparative trials (one trial per condition), cervical aspiration catheter placement showed higher max-median ROI displacement and stress-proxy values than internal carotid artery terminus placement. Conclusion: The proposed protocol provides standardized, time-resolved surface kinematics and comparative relative displacement and stress proxy measurements for thrombectomy benchtop studies. The framework supports condition-to-condition comparisons and methods validation, while remaining distinct from absolute wall-stress estimation. Implementation code and example data are available at https://ethanuser.github.io/vessel4D

  </details>

- **[AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://arxiv.org/abs/2604.04787)**  
  *Hongyu Liu, Xuan Wang, Zijian Wu, Yating Wang, Ziyu Wan, Yue Ma, Runtao Liu, Boyao Zhou, Yujun Shen, Qifeng Chen*  
  `2026-04-06` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04787) · [pdf](https://arxiv.org/pdf/2604.04787.pdf)
  > 💡 提出自回归Transformer生成3D高斯点云，从单图创建高质量可控4D动态化身。

  <details><summary>Abstract</summary>

  We introduce AvatarPointillist, a novel framework for generating dynamic 4D Gaussian avatars from a single portrait image. At the core of our method is a decoder-only Transformer that autoregressively generates a point cloud for 3D Gaussian Splatting. This sequential approach allows for precise, adaptive construction, dynamically adjusting point density and the total number of points based on the subject's complexity. During point generation, the AR model also jointly predicts per-point binding information, enabling realistic animation. After generation, a dedicated Gaussian decoder converts the points into complete, renderable Gaussian attributes. We demonstrate that conditioning the decoder on the latent features from the AR generator enables effective interaction between stages and markedly improves fidelity. Extensive experiments validate that AvatarPointillist produces high-quality, photorealistic, and controllable avatars. We believe this autoregressive formulation represents a new paradigm for avatar generation, and we will release our code inspire future research.

  </details>

- **[4C4D: 4 Camera 4D Gaussian Splatting](https://arxiv.org/abs/2604.04063)**  
  *Junsheng Zhou, Zhifan Yang, Liang Han, Wenyuan Zhang, Kanle Shi, Shenkun Xu, Yu-Shen Liu*  
  `2026-04-05` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04063) · [pdf](https://arxiv.org/pdf/2604.04063.pdf)
  > 💡 提出4C4D框架，用神经衰减函数增强高斯不透明度几何学习，以极稀疏四相机视频实现高保真4D动态场景渲染。

  <details><summary>Abstract</summary>

  This paper tackles the challenge of recovering 4D dynamic scenes from videos captured by as few as four portable cameras. Learning to model scene dynamics for temporally consistent novel-view rendering is a foundational task in computer graphics, where previous works often require dense multi-view captures using camera arrays of dozens or even hundreds of views. We propose \textbf{4C4D}, a novel framework that enables high-fidelity 4D Gaussian Splatting from video captures of extremely sparse cameras. Our key insight lies that the geometric learning under sparse settings is substantially more difficult than modeling appearance. Driven by this observation, we introduce a Neural Decaying Function on Gaussian opacities for enhancing the geometric modeling capability of 4D Gaussians. This design mitigates the inherent imbalance between geometry and appearance modeling in 4DGS by encouraging the 4DGS gradients to focus more on geometric learning. Extensive experiments across sparse-view datasets with varying camera overlaps show that 4C4D achieves superior performance over prior art. Project page at: https://junshengzhou.github.io/4C4D.

  </details>

- **[HOIGS: Human-Object Interaction Gaussian Splatting](https://arxiv.org/abs/2604.04016)**  
  *Taewoo Kim, Suwoong Yeom, Jaehyun Pyun, Geonho Cha, Dongyoon Wee, Joonsik Nam, Yun-Seong Jeong, Kyeongbo Kong, Suk-Ju Kang*  
  `2026-04-05` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04016) · [pdf](https://arxiv.org/pdf/2604.04016.pdf)
  > 💡 提出交叉注意力HOI模块显式建模人-物交互形变，用HexPlane和CHS分别处理人体和物体，提升动态场景重建质量。

  <details><summary>Abstract</summary>

  Reconstructing dynamic scenes with complex human-object interactions is a fundamental challenge in computer vision and graphics. Existing Gaussian Splatting methods either rely on human pose priors while neglecting dynamic objects, or approximate all motions within a single field, limiting their ability to capture interaction-rich dynamics. To address this gap, we propose Human-Object Interaction Gaussian Splatting (HOIGS), which explicitly models interaction-induced deformation between humans and objects through a cross-attention-based HOI module. Distinct deformation baselines are employed to extract features: HexPlane for humans and Cubic Hermite Spline (CHS) for objects. By integrating these heterogeneous features, HOIGS effectively captures interdependent motions and improves deformation estimation in scenarios involving occlusion, contact, and object manipulation. Comprehensive experiments on multiple datasets demonstrate that our method consistently outperforms state-of-the-art human-centric and 4D Gaussian approaches, highlighting the importance of explicitly modeling human-object interactions for high-fidelity reconstruction.

  </details>

- **[GP-4DGS: Probabilistic 4D Gaussian Splatting from Monocular Video via Variational Gaussian Processes](https://arxiv.org/abs/2604.02915)**  
  *Mijeong Kim, Jungtaek Kim, Bohyung Han*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02915) · [pdf](https://arxiv.org/pdf/2604.02915.pdf)
  > 💡 针对4DGS缺少运动不确定性量化，引入变分高斯过程实现概率建模和可靠预测。

  <details><summary>Abstract</summary>

  We present GP-4DGS, a novel framework that integrates Gaussian Processes (GPs) into 4D Gaussian Splatting (4DGS) for principled probabilistic modeling of dynamic scenes. While existing 4DGS methods focus on deterministic reconstruction, they are inherently limited in capturing motion ambiguity and lack mechanisms to assess prediction reliability. By leveraging the kernel-based probabilistic nature of GPs, our approach introduces three key capabilities: (i) uncertainty quantification for motion predictions, (ii) motion estimation for unobserved or sparsely sampled regions, and (iii) temporal extrapolation beyond observed training frames. To scale GPs to the large number of Gaussian primitives in 4DGS, we design spatio-temporal kernels that capture the correlation structure of deformation fields and adopt variational Gaussian Processes with inducing points for tractable inference. Our experiments show that GP-4DGS enhances reconstruction quality while providing reliable uncertainty estimates that effectively identify regions of high motion ambiguity. By addressing these challenges, our work takes a meaningful step toward bridging probabilistic modeling and neural graphics.

  </details>

- **[Streaming Real-Time Rendered Scenes as 3D Gaussians](https://arxiv.org/abs/2604.02851)**  
  *Matti Siekkinen, Teemu Kämäräinen*  
  `2026-04-03` · `eess.IV` · [abs](https://arxiv.org/abs/2604.02851) · [pdf](https://arxiv.org/pdf/2604.02851.pdf)
  > 💡 针对云渲染2D视频流视点受限

  <details><summary>Abstract</summary>

  Cloud rendering is widely used in gaming and XR to overcome limited client-side GPU resources and to support heterogeneous devices. Existing systems typically deliver the rendered scene as a 2D video stream, which tightly couples the transmitted content to the server-rendered viewpoint and limits latency compensation to image-space reprojection or warping. In this paper, we investigate an alternative approach based on streaming a live 3D Gaussian Splatting (3DGS) scene representation instead of only rendered video. We present a Unity-based prototype in which a server constructs and continuously optimizes a 3DGS model from real-time rendered reference views, while streaming the evolving representation to remote clients using full model snapshots and incremental updates supporting relighting and rigid object dynamics. The clients reconstruct the streamed Gaussian model locally and render their current viewpoint from the received representation. This approach aims to improve viewpoint flexibility for latency compensation and to better amortize server-side scene modeling across multiple users than per-user rendering and video streaming. We describe the system design, evaluate it, and compare it with conventional image warping.

  </details>

- **[NavCrafter: Exploring 3D Scenes from a Single Image](https://arxiv.org/abs/2604.02828)**  
  *Hongbo Duan, Peiyu Zhuang, Yi Liu, Zhengyang Zhang, Yuxin Zhang, Pengting Luo, Fangming Liu, Xueqian Wang*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02828) · [pdf](https://arxiv.org/pdf/2604.02828.pdf)
  > 💡 从单张图像生成可控制相机路径的3D场景，利用视频扩散几何扩展和增强3DGS实现大视角新视图合成与高保真重建。

  <details><summary>Abstract</summary>

  Creating flexible 3D scenes from a single image is vital when direct 3D data acquisition is costly or impractical. We introduce NavCrafter, a novel framework that explores 3D scenes from a single image by synthesizing novel-view video sequences with camera controllability and temporal-spatial consistency. NavCrafter leverages video diffusion models to capture rich 3D priors and adopts a geometry-aware expansion strategy to progressively extend scene coverage. To enable controllable multi-view synthesis, we introduce a multi-stage camera control mechanism that conditions diffusion models with diverse trajectories via dual-branch camera injection and attention modulation. We further propose a collision-aware camera trajectory planner and an enhanced 3D Gaussian Splatting (3DGS) pipeline with depth-aligned supervision, structural regularization and refinement. Extensive experiments demonstrate that NavCrafter achieves state-of-the-art novel-view synthesis under large viewpoint shifts and substantially improves 3D reconstruction fidelity.

  </details>

- **[DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos](https://arxiv.org/abs/2604.02781)**  
  *Ziyu Luo, Lin Chen, Qiang Qu, Xiaoming Chen, Yiran Shen*  
  `2026-04-03` · `cs.SD` · [abs](https://arxiv.org/abs/2604.02781) · [pdf](https://arxiv.org/pdf/2604.02781.pdf)
  > 💡 针对动态声学复杂场景，提出DynFOA结合3DGS重建与条件扩散生成一阶高保真立体声，并贡献M2G-360数据集。

  <details><summary>Abstract</summary>

  Spatial audio is crucial for immersive 360-degree video experiences, yet most 360-degree videos lack it due to the difficulty of capturing spatial audio during recording. Automatically generating spatial audio such as first-order ambisonics (FOA) from video therefore remains an important but challenging problem. In complex scenes, sound perception depends not only on sound source locations but also on scene geometry, materials, and dynamic interactions with the environment. However, existing approaches only rely on visual cues and fail to model dynamic sources and acoustic effects such as occlusion, reflections, and reverberation. To address these challenges, we propose DynFOA, a generative framework that synthesizes FOA from 360-degree videos by integrating dynamic scene reconstruction with conditional diffusion modeling. DynFOA analyzes the input video to detect and localize dynamic sound sources, estimate depth and semantics, and reconstruct scene geometry and materials using 3D Gaussian Splatting (3DGS). The reconstructed scene representation provides physically grounded features that capture acoustic interactions between sources, environment, and listener viewpoint. Conditioned on these features, a diffusion model generates spatial audio consistent with the scene dynamics and acoustic context. We introduce M2G-360, a dataset of 600 real-world clips divided into MoveSources, Multi-Source, and Geometry subsets for evaluating robustness under diverse conditions. Experiments show that DynFOA consistently outperforms existing methods in spatial accuracy, acoustic fidelity, distribution matching, and perceived immersive experience.

  </details>

- **[Director: Instance-aware Gaussian Splatting for Dynamic Scene Modeling and Understanding](https://arxiv.org/abs/2604.01678)**  
  *Yuheng Jiang, Yiwen Cai, Zihao Wang, Yize Wu, Sicheng Li, Zhuo Su, Shaohui Jiao, Lan Xu*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01678) · [pdf](https://arxiv.org/pdf/2604.01678.pdf)
  > 💡 针对动态场景缺乏实例级语义的问题，提出将实例一致语义嵌入4D高斯，结合光流与SDF约束，实现高保真渲染、实例分割和开放词汇查询。

  <details><summary>Abstract</summary>

  Volumetric video seeks to model dynamic scenes as temporally coherent 4D representations. While recent Gaussian-based approaches achieve impressive rendering fidelity, they primarily emphasize appearance but are largely agnostic to instance-level structure, limiting stable tracking and semantic reasoning in highly dynamic scenarios. In this paper, we present Director, a unified spatio-temporal Gaussian representation that jointly models human performance, high-fidelity rendering, and instance-level semantics. Our key insight is that embedding instance-consistent semantics naturally complements 4D modeling, enabling more accurate scene decomposition while supporting robust dynamic scene understanding. To this end, we leverage temporally aligned instance masks and sentence embeddings derived from Multimodal Large Language Models to supervise the learnable semantic features of each Gaussian via two MLP decoders, enabling language-aligned 4D representations and enforcing identity consistency over time. To enhance temporal stability, we bridge 2D optical flow with 4D Gaussians and finetune their motions, yielding reliable initialization and reducing drift. For the training, we further introduce a geometry-aware SDF constraints, along with regularization terms that enforces surface continuity, enhancing temporal coherence in dynamic foreground modeling. Experiments demonstrate that Director achieves temporally coherent 4D reconstructions while simultaneously enabling instance segmentation and open-vocabulary querying.

  </details>

- **[TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction](https://arxiv.org/abs/2604.02586)**  
  *Daheng Yin, Isaac Ding, Yili Jin, Jianxin Shi, Jiangchuan Liu*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02586) · [pdf](https://arxiv.org/pdf/2604.02586.pdf)
  > 💡 将点跟踪与3D高斯结合，用像素轨迹指导高斯变换，解决大位移下的伪影问题，提升动态重建鲁棒性与吞吐量。

  <details><summary>Abstract</summary>

  Recent advancements in 3D Gaussian Splatting (3DGS) have demonstrated its potential for efficient and photorealistic 3D reconstructions, which is crucial for diverse applications such as robotics and immersive media. However, current Gaussian-based methods for dynamic scene reconstruction struggle with large inter-frame displacements, leading to artifacts and temporal inconsistencies under fast object motions. To address this, we introduce \textit{TrackerSplat}, a novel method that integrates advanced point tracking methods to enhance the robustness and scalability of 3DGS for dynamic scene reconstruction. TrackerSplat utilizes off-the-shelf point tracking models to extract pixel trajectories and triangulate per-view pixel trajectories onto 3D Gaussians to guide the relocation, rotation, and scaling of Gaussians before training. This strategy effectively handles large displacements between frames, dramatically reducing the fading and recoloring artifacts prevalent in prior methods. By accurately positioning Gaussians prior to gradient-based optimization, TrackerSplat overcomes the quality degradation associated with large frame gaps when processing multiple adjacent frames in parallel across multiple devices, thereby boosting reconstruction throughput while preserving rendering quality. Experiments on real-world datasets confirm the robustness of TrackerSplat in challenging scenarios with significant displacements, achieving superior throughput under parallel settings and maintaining visual quality compared to baselines. The code is available at https://github.com/yindaheng98/TrackerSplat.

  </details>

- **[TRiGS: Temporal Rigid-Body Motion for Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2604.00538)**  
  *Suwoong Yeom, Joonsik Nam, Seunggyu Choi, Lucas Yunkyu Lee, Sangmin Kim, Jaesik Park, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong, Sukju Kang*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.00538) · [pdf](https://arxiv.org/pdf/2604.00538.pdf)
  > 💡 现有4DGS因分段线性近似导致时间碎片化和内存爆炸，TRiGS用SE(3)变换和贝塞尔残差实现连续刚体运动，高效扩展至长视频。

  <details><summary>Abstract</summary>

  Recent 4D Gaussian Splatting (4DGS) methods achieve impressive dynamic scene reconstruction but often rely on piecewise linear velocity approximations and short temporal windows. This disjointed modeling leads to severe temporal fragmentation, forcing primitives to be repeatedly eliminated and regenerated to track complex nonlinear dynamics. This makeshift approximation eliminates the long-term temporal identity of objects and causes an inevitable proliferation of Gaussians, hindering scalability to extended video sequences. To address this, we propose TRiGS, a novel 4D representation that utilizes unified, continuous geometric transformations. By integrating $SE(3)$ transformations, hierarchical Bezier residuals, and learnable local anchors, TRiGS models geometrically consistent rigid motions for individual primitives. This continuous formulation preserves temporal identity and effectively mitigates unbounded memory growth. Extensive experiments demonstrate that TRiGS achieves high fidelity rendering on standard benchmarks while uniquely scaling to extended video sequences (e.g., 600 to 1200 frames) without severe memory bottlenecks, significantly outperforming prior works in temporal stability.

  </details>

- **[MotionScale: Reconstructing Appearance, Geometry, and Motion of Dynamic Scenes with Scalable 4D Gaussian Splatting](https://arxiv.org/abs/2603.29296)**  
  *Haoran Zhou, Gim Hee Lee*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2603.29296) · [pdf](https://arxiv.org/pdf/2603.29296.pdf)
  > 💡 提出可缩放4D高斯泼溅框架，用簇中心基础变换和渐进优化实现大规模动态场景的高质量几何与运动重建。

  <details><summary>Abstract</summary>

  Realistic reconstruction of dynamic 4D scenes from monocular videos is essential for understanding the physical world. Despite recent progress in neural rendering, existing methods often struggle to recover accurate 3D geometry and temporally consistent motion in complex environments. To address these challenges, we propose MotionScale, a 4D Gaussian Splatting framework that scales efficiently to large scenes and extended sequences while maintaining high-fidelity structural and motion coherence. At the core of our approach is a scalable motion field parameterized by cluster-centric basis transformations that adaptively expand to capture diverse and evolving motion patterns. To ensure robust reconstruction over long durations, we introduce a progressive optimization strategy comprising two decoupled propagation stages: 1) A background extension stage that adapts to newly visible regions, refines camera poses, and explicitly models transient shadows; 2) A foreground propagation stage that enforces motion consistency through a specialized three-stage refinement process. Extensive experiments on challenging real-world benchmarks demonstrate that MotionScale significantly outperforms state-of-the-art methods in both reconstruction quality and temporal stability. Project page: https://hrzhou2.github.io/motion-scale-web/.

  </details>

- **[ObjectMorpher: 3D-Aware Image Editing via Deformable 3DGS Models](https://arxiv.org/abs/2603.28152)**  
  *Yuhuan Xie, Aoxuan Pan, Yi-Hua Huang, Chirui Chang, Peng Dai, Xin Yu, Xiaojuan Qi*  
  `2026-03-30` · `cs.CV` · [abs](https://arxiv.org/abs/2603.28152) · [pdf](https://arxiv.org/pdf/2603.28152.pdf)
  > 💡 针对2D编辑缺乏3D感知，提出ObjectMorpher，利用

  <details><summary>Abstract</summary>

  Achieving precise, object-level control in image editing remains challenging: 2D methods lack 3D awareness and often yield ambiguous or implausible results, while existing 3D-aware approaches rely on heavy optimization or incomplete monocular reconstructions. We present ObjectMorpher, a unified, interactive framework that converts ambiguous 2D edits into geometry-grounded operations. ObjectMorpher lifts target instances with an image-to-3D generator into editable 3D Gaussian Splatting (3DGS), enabling fast, identity-preserving manipulation. Users drag control points; a graph-based non-rigid deformation with as-rigid-as-possible (ARAP) constraints ensures physically sensible shape and pose changes. A composite diffusion module harmonizes lighting, color, and boundaries for seamless reintegration. Across diverse categories, ObjectMorpher delivers fine-grained, photorealistic edits with superior controllability and efficiency, outperforming 2D drag and 3D-aware baselines on KID, LPIPS, SIFID, and user preference.

  </details>

- **[R-PGA: Robust Physical Adversarial Camouflage Generation via Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2603.26067)**  
  *Tianrui Lou, Siyuan Liang, Jiawei Liang, Yuze Gao, Xiaochun Cao*  
  `2026-03-27` · `cs.CV` · [abs](https://arxiv.org/abs/2603.26067) · [pdf](https://arxiv.org/pdf/2603.26067.pdf)
  > 💡 针对物理对抗伪装不鲁棒，提出可重照明3DGS与硬物理配置挖掘，提升模拟真实性和优化鲁棒性。

  <details><summary>Abstract</summary>

  Physical adversarial camouflage poses a severe security threat to autonomous driving systems by mapping adversarial textures onto 3D objects. Nevertheless, current methods remain brittle in complex dynamic scenarios, failing to generalize across diverse geometric (e.g., viewing configurations) and radiometric (e.g., dynamic illumination, atmospheric scattering) variations. We attribute this deficiency to two fundamental limitations in simulation and optimization. First, the reliance on coarse, oversimplified simulations (e.g., via CARLA) induces a significant domain gap, confining optimization to a biased feature space. Second, standard strategies targeting average performance result in a rugged loss landscape, leaving the camouflage vulnerable to configuration shifts.To bridge these gaps, we propose the Relightable Physical 3D Gaussian Splatting (3DGS) based Attack framework (R-PGA). Technically, to address the simulation fidelity issue, we leverage 3DGS to ensure photo-realistic reconstruction and augment it with physically disentangled attributes to decouple intrinsic material from lighting. Furthermore, we design a hybrid rendering pipeline that leverages precise Relightable 3DGS for foreground rendering, while employing a pre-trained image translation model to synthesize plausible relighted backgrounds that align with the relighted foreground.To address the optimization robustness issue, we propose the Hard Physical Configuration Mining (HPCM) module, designed to actively mine worst-case physical configurations and suppress their corresponding loss peaks. This strategy not only diminishes the overall loss magnitude but also effectively flattens the rugged loss landscape, ensuring consistent adversarial effectiveness and robustness across varying physical configurations.

  </details>

- **[arg-VU: Affordance Reasoning with Physics-Aware 3D Geometry for Visual Understanding in Robotic Surgery](https://arxiv.org/abs/2603.26814)**  
  *Nan Xiao, Yunxin Fan, Farong Wang, Fei Liu*  
  `2026-03-26` · `cs.CV` · [abs](https://arxiv.org/abs/2603.26814) · [pdf](https://arxiv.org/pdf/2603.26814.pdf)
  > 💡 利用3DGS与XPBD融合物理感知变形约束，实现手术环境中更稳定可解释的可操作推理。

  <details><summary>Abstract</summary>

  Affordance reasoning provides a principled link between perception and action, yet remains underexplored in surgical robotics, where tissues are highly deformable, compliant, and dynamically coupled with tool motion. We present arg-VU, a physics-aware affordance reasoning framework that integrates temporally consistent geometry tracking with constraint-induced mechanical modeling for surgical visual understanding. Surgical scenes are reconstructed using 3D Gaussian Splatting (3DGS) and converted into a temporally tracked surface representation. Extended Position-Based Dynamics (XPBD) embeds local deformation constraints and produces representative geometry points (RGPs) whose constraint sensitivities define anisotropic stiffness metrics capturing the local constraint-manifold geometry. Robotic tool poses in SE(3) are incorporated to compute rigidly induced displacements at RGPs, from which we derive two complementary measures: a physics-aware compliance energy that evaluates mechanical feasibility with respect to local deformation constraints, and a positional agreement score that captures motion alignment (as kinematic motion baseline). Experiments on surgical video datasets show that arg-VU yields more stable, physically consistent, and interpretable affordance predictions than kinematic baselines. These results demonstrate that physics-aware geometric representations enable reliable affordance reasoning for deformable surgical environments and support embodied robotic interaction.

  </details>

- **[Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning](https://arxiv.org/abs/2603.18402)**  
  *Yonghan Lee, Dinesh Manocha*  
  `2026-03-19` · `cs.CV` · [abs](https://arxiv.org/abs/2603.18402) · [pdf](https://arxiv.org/pdf/2603.18402.pdf)
  > 💡 通过可微排列学习对齐多视频实例标签，实现实例分解4DGS，显著提升渲染与分割质量。

  <details><summary>Abstract</summary>

  We present Inst4DGS, an instance-decomposed 4D Gaussian Splatting (4DGS) approach with long-horizon per-Gaussian trajectories. While dynamic 4DGS has advanced rapidly, instance-decomposed 4DGS remains underexplored, largely due to the difficulty of associating inconsistent instance labels across independently segmented multi-view videos. We address this challenge by introducing per-video label-permutation latents that learn cross-video instance matches through a differentiable Sinkhorn layer, enabling direct multi-view supervision with consistent identity preservation. This explicit label alignment yields sharp decision boundaries and temporally stable identities without identity drift. To further improve efficiency, we propose instance-decomposed motion scaffolds that provide low-dimensional motion bases per object for long-horizon trajectory optimization. Experiments on Panoptic Studio and Neural3DV show that Inst4DGS jointly supports tracking and instance decomposition while achieving state-of-the-art rendering and segmentation quality. On the Panoptic Studio dataset, Inst4DGS improves PSNR from 26.10 to 28.36, and instance mIoU from 0.6310 to 0.9129, over the strongest baseline.

  </details>

- **[Adaptive Anchor Policies for Efficient 4D Gaussian Streaming](https://arxiv.org/abs/2603.17227)**  
  *Ashim Dahal, Rabab Abdelfattah, Nick Rahimi*  
  `2026-03-18` · `cs.CV` · [abs](https://arxiv.org/abs/2603.17227) · [pdf](https://arxiv.org/pdf/2603.17227.pdf)
  > 💡 针对固定锚点选择导致计算浪费的问题，提出强化学习驱动的自适应锚点策略，在4D高斯流中提升质量-效率权衡。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction with Gaussian Splatting has enabled efficient streaming for real-time rendering and free-viewpoint video. However, most pipelines rely on fixed anchor selection such as Farthest Point Sampling (FPS), typically using 8,192 anchors regardless of scene complexity, which over-allocates computation under strict budgets. We propose Efficient Gaussian Streaming (EGS), a plug-in, budget-aware anchor sampler that replaces FPS with a reinforcement-learned policy while keeping the Gaussian streaming reconstruction backbone unchanged. The policy jointly selects an anchor budget and a subset of informative anchors under discrete constraints, balancing reconstruction quality and runtime using spatial features of the Gaussian representation. We evaluate EGS in two settings: fast rendering, which prioritizes runtime efficiency, and high-quality refinement, which enables additional optimization. Experiments on dynamic multi-view datasets show consistent improvements in the quality--efficiency trade-off over FPS sampling. On unseen data, in fast rendering at 256 anchors ($32\times$ fewer than 8,192), EGS improves PSNR by $+0.52$--$0.61$\,dB while running $1.29$--$1.35\times$ faster than IGS@8192 (N3DV and MeetingRoom). In high-quality refinement, EGS remains competitive with the full-anchor baseline at substantially lower anchor budgets. \emph{Code and pretrained checkpoints will be released upon acceptance.} \keywords{4D Gaussian Splatting \and 4D Gaussian Streaming \and Reinforcement Learning}

  </details>

- **[4D Synchronized Fields: Motion-Language Gaussian Splatting for Temporal Scene Understanding](https://arxiv.org/abs/2603.14301)**  
  *Mohamed Rayan Barhdadi, Samir Abdaljalil, Rasul Khanbayov, Erchin Serpedin, Hasan Kurban*  
  `2026-03-15` · `cs.CV` · [abs](https://arxiv.org/abs/2603.14301) · [pdf](https://arxiv.org/pdf/2603.14301.pdf)
  > 💡 因子化物体运动并同步语言场的4D高斯表示，实现重建-运动-语义耦合，时空查询精度领先。

  <details><summary>Abstract</summary>

  Current 4D representations decouple geometry, motion, and semantics: reconstruction methods discard interpretable motion structure; language-grounded methods attach semantics after motion is learned, blind to how objects move; and motion-aware methods encode dynamics as opaque per-point residuals without object-level organization. We propose 4D Synchronized Fields, a 4D Gaussian representation that learns object-factored motion in-loop during reconstruction and synchronizes language to the resulting kinematics through a per-object conditioned field. Each Gaussian trajectory is decomposed into shared object motion plus an implicit residual, and a kinematic-conditioned ridge map predicts temporal semantic variation, yielding a single representation in which reconstruction, motion, and semantics are structurally coupled and enabling open-vocabulary temporal queries that retrieve both objects and moments. On HyperNeRF, 4D Synchronized Fields achieves 28.52 dB mean PSNR, the highest among all language-grounded and motion-aware baselines, within 1.5 dB of reconstruction-only methods. On targeted temporal-state retrieval, the kinematic-conditioned field attains 0.884 mean accuracy, 0.815 mean vIoU, and 0.733 mean tIoU, surpassing 4D LangSplat (0.620, 0.433, and 0.439 respectively) and LangSplat (0.415, 0.304, and 0.262). Ablation confirms that kinematic conditioning is the primary driver, accounting for +0.45 tIoU over a static-embedding-only baseline. 4D Synchronized Fields is the only method that jointly exposes interpretable motion primitives and temporally grounded language fields from a single trained representation. Code will be released.

  </details>

- **[RetimeGS: Continuous-Time Reconstruction of 4D Gaussian Splatting](https://arxiv.org/abs/2603.13783)**  
  *Xuezhen Wang, Li Ma, Yulin Shen, Zeyu Wang, Pedro V. Sander*  
  `2026-03-14` · `cs.CV` · [abs](https://arxiv.org/abs/2603.13783) · [pdf](https://arxiv.org/pdf/2603.13783.pdf)
  > 💡 针对4DGS时间混叠导致的插值鬼影，提出显式高斯时间行为建模与光流引导策略，实现无鬼影连续时间渲染。

  <details><summary>Abstract</summary>

  Temporal retiming, the ability to reconstruct and render dynamic scenes at arbitrary timestamps, is crucial for applications such as slow-motion playback, temporal editing, and post-production. However, most existing 4D Gaussian Splatting (4DGS) methods overfit at discrete frame indices but struggle to represent continuous-time frames, leading to ghosting artifacts when interpolating between timestamps. We identify this limitation as a form of temporal aliasing and propose RetimeGS, a simple yet effective 4DGS representation that explicitly defines the temporal behavior of the 3D Gaussian and mitigates temporal aliasing. To achieve smooth and consistent interpolation, we incorporate optical flow-guided initialization and supervision, triple-rendering supervision, and other targeted strategies. Together, these components enable ghost-free, temporally coherent rendering even under large motions. Experiments on datasets featuring fast motion, non-rigid deformation, and severe occlusions demonstrate that RetimeGS achieves superior quality and coherence over state-of-the-art methods.

  </details>

- **[Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation](https://arxiv.org/abs/2603.12766)**  
  *Shifeng Chen, Yihui Li, Jun Liao, Hongyu Yang, Di Huang*  
  `2026-03-13` · `cs.CV` · [abs](https://arxiv.org/abs/2603.12766) · [pdf](https://arxiv.org/pdf/2603.12766.pdf)
  > 💡 引入锚点运动引导和颜色不确定性外观精炼，解决动态编辑时序闪烁与运动漂移，实现高保真4D编辑。

  <details><summary>Abstract</summary>

  Recent advances in 3D scene editing using NeRF and 3DGS enable high-quality static scene editing. In contrast, dynamic scene editing remains challenging, as methods that directly extend 2D diffusion models to 4D often produce motion artifacts, temporal flickering, and inconsistent style propagation. We introduce Catalyst4D, a framework that transfers high-quality 3D edits to dynamic 4D Gaussian scenes while maintaining spatial and temporal coherence. At its core, Anchor-based Motion Guidance (AMG) builds a set of structurally stable and spatially representative anchors from both original and edited Gaussians. These anchors serve as robust region-level references, and their correspondences are established via optimal transport to enable consistent deformation propagation without cross-region interference or motion drift. Complementarily, Color Uncertainty-guided Appearance Refinement (CUAR) preserves temporal appearance consistency by estimating per-Gaussian color uncertainty and selectively refining regions prone to occlusion-induced artifacts. Extensive experiments demonstrate that Catalyst4D achieves temporally stable, high-fidelity dynamic scene editing and outperforms existing methods in both visual quality and motion coherence.

  </details>

- **[Mango-GS: Enhancing Spatio-Temporal Consistency in Dynamic Scenes Reconstruction using Multi-Frame Node-Guided 4D Gaussian Splatting](https://arxiv.org/abs/2603.11543)**  
  *Tingxuan Huang, Haowei Zhu, Jun-hai Yong, Hao Pan, Bin Wang*  
  `2026-03-12` · `cs.CV` · [abs](https://arxiv.org/abs/2603.11543) · [pdf](https://arxiv.org/pdf/2603.11543.pdf)
  > 💡 使用多帧节点引导与时序Transformer解决动态场景时空不一致，实现高保真重建与实时渲染。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes with photorealistic detail and strong temporal coherence remains a significant challenge. Existing Gaussian splatting approaches for dynamic scene modeling often rely on per-frame optimization, which can overfit to instantaneous states instead of capturing underlying motion dynamics. To address this, we present Mango-GS, a multi-frame, node-guided framework for high-fidelity 4D reconstruction. Mango-GS leverages a temporal Transformer to model motion dependencies within a short window of frames, producing temporally consistent deformations. For efficiency, temporal modeling is confined to a sparse set of control nodes. Each node is represented by a decoupled canonical position and a latent code, providing a stable semantic anchor for motion propagation and preventing correspondence drift under large motion. Our framework is trained end-to-end, enhanced by an input masking strategy and two multi-frame losses to improve robustness. Extensive experiments demonstrate that Mango-GS achieves state-of-the-art reconstruction quality and real-time rendering speed, enabling high-fidelity reconstruction and interactive rendering of dynamic scenes.

  </details>

- **[HDR-NSFF: High Dynamic Range Neural Scene Flow Fields](https://arxiv.org/abs/2603.08313)**  
  *Shin Dong-Yeon, Kim Jun-Seong, Kwon Byung-Ki, Tae-Hyun Oh*  
  `2026-03-09` · `cs.CV` · [abs](https://arxiv.org/abs/2603.08313) · [pdf](https://arxiv.org/pdf/2603.08313.pdf)
  > 💡 用4D时空建模替换2D对齐，结合曝光不变运动估计和生成先验，实现动态场景高动态范围重建与时空视图合成。

  <details><summary>Abstract</summary>

  Radiance of real-world scenes typically spans a much wider dynamic range than what standard cameras can capture. While conventional HDR methods merge alternating-exposure frames, these approaches are inherently constrained to 2D pixel-level alignment, often leading to ghosting artifacts and temporal inconsistency in dynamic scenes. To address these limitations, we present HDR-NSFF, a paradigm shift from 2D-based merging to 4D spatio-temporal modeling. Our framework reconstructs dynamic HDR radiance fields from alternating-exposure monocular videos by representing the scene as a continuous function of space and time, and is compatible with both neural radiance field and 4D Gaussian Splatting (4DGS) based dynamic representations. This unified end-to-end pipeline explicitly models HDR radiance, 3D scene flow, geometry, and tone-mapping, ensuring physical plausibility and global coherence. We further enhance robustness by (i) extending semantic-based optical flow with DINO features to achieve exposure-invariant motion estimation, and (ii) incorporating a generative prior as a regularizer to compensate for limited observation in monocular captures and saturation-induced information loss. To evaluate HDR space-time view synthesis, we present the first real-world HDR-GoPro dataset specifically designed for dynamic HDR scenes. Experiments demonstrate that HDR-NSFF recovers fine radiance details and coherent dynamics even under challenging exposure variations, thereby achieving state-of-the-art performance in novel space-time view synthesis. Project page: https://shin-dong-yeon.github.io/HDR-NSFF/

  </details>

- **[ReconDrive: Fast Feed-Forward 4D Gaussian Splatting for Autonomous Driving Scene Reconstruction](https://arxiv.org/abs/2603.07552)**  
  *Haibao Yu, Kuntao Xiao, Jiahang Wang, Ruiyang Hao, Yuxin Huang, Guoran Hu, Haifang Qin, Bowen Jing, Yuntian Bo, Ping Luo*  
  `2026-03-08` · `cs.CV` · [abs](https://arxiv.org/abs/2603.07552) · [pdf](https://arxiv.org/pdf/2603.07552.pdf)
  > 💡 基于3D基础模型VGGT，提出混合高斯预测头和静动态组合策略，实现快速高保真4DGS重建，性能与逐场景优化相当且速度更快。

  <details><summary>Abstract</summary>

  High-fidelity visual reconstruction and novel-view synthesis are essential for realistic closed-loop evaluation in autonomous driving. While 4D Gaussian Splatting (4DGS) offers a promising balance of accuracy and efficiency, existing per-scene optimization methods require costly iterative refinement, rendering them unscalable for extensive urban environments. Conversely, current feed-forward approaches often suffer from degraded photometric quality. To address these limitations, we propose ReconDrive, a feed-forward framework that leverages and extends the 3D foundation model VGGT for rapid, high-fidelity 4DGS generation. Our architecture introduces two core adaptations to tailor the foundation model to dynamic driving scenes: (1) Hybrid Gaussian Prediction Heads, which decouple the regression of spatial coordinates and appearance attributes to overcome the photometric deficiencies inherent in generalized foundation features; and (2) a Static-Dynamic 4D Composition strategy that explicitly captures temporal motion via velocity modeling to represent complex dynamic environments. Benchmarked on nuScenes, ReconDrive significantly outperforms existing feed-forward baselines in reconstruction, novel-view synthesis, and 3D perception. It achieves performance competitive with per-scene optimization while being orders of magnitude faster, providing a scalable and practical solution for realistic driving simulation.

  </details>

- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081)**  
  *Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu*  
  `2026-03-05` · `cs.CV` · [abs](https://arxiv.org/abs/2603.05081) · [pdf](https://arxiv.org/pdf/2603.05081.pdf)
  > 💡 针对4D数据集匮乏导致质量受限，提出正交时空分布转移机制，利用STD-4D扩散与ST-HexPlane，实现高质量时空一致4D生成。

  <details><summary>Abstract</summary>

  In the AIGC era, generating high-quality 4D content has garnered increasing research attention. Unfortunately, current 4D synthesis research is severely constrained by the lack of large-scale 4D datasets, preventing models from adequately learning the critical spatial-temporal features necessary for high-quality 4D generation, thus hindering progress in this domain. To combat this, we propose a novel framework that transfers rich spatial priors from existing 3D diffusion models and temporal priors from video diffusion models to enhance 4D synthesis. We develop a spatial-temporal-disentangled 4D (STD-4D) Diffusion model, which synthesizes 4D-aware videos through disentangled spatial and temporal latents. To facilitate the best feature transfer, we design a novel Orthogonal Spatial-temporal Distributional Transfer (Orster) mechanism, where the spatiotemporal feature distributions are carefully modeled and injected into the STD-4D Diffusion. Furthermore, during the 4D construction, we devise a spatial-temporal-aware HexPlane (ST-HexPlane) to integrate the transferred spatiotemporal features, thereby improving 4D deformation and 4D Gaussian feature modeling. Experiments demonstrate that our method significantly outperforms existing approaches, achieving superior spatial-temporal consistency and higher-quality 4D synthesis.

  </details>

- **[Decoupling Motion and Geometry in 4D Gaussian Splatting](https://arxiv.org/abs/2603.00952)**  
  *Yi Zhang, Yulei Kang, Jiangxin Sun, Beihao Xia, Jisheng Dang, Jian-Fang Hu*  
  `2026-03-01` · `cs.CV` · [abs](https://arxiv.org/abs/2603.00952) · [pdf](https://arxiv.org/pdf/2603.00952.pdf)
  > 💡 针对4DGS中运动与几何耦合限制动态表达的问题，提出基于速度的解耦框架VeGaS，引入伽利略剪切矩阵和几何变形网络，实现高保真动态场景重建。

  <details><summary>Abstract</summary>

  High-fidelity reconstruction of dynamic scenes is an important yet challenging problem. While recent 4D Gaussian Splatting (4DGS) has demonstrated the ability to model temporal dynamics, it couples Gaussian motion and geometric attributes within a single covariance formulation, which limits its expressiveness for complex motions and often leads to visual artifacts. To address this, we propose VeGaS, a novel velocity-based 4D Gaussian Splatting framework that decouples Gaussian motion and geometry. Specifically, we introduce a Galilean shearing matrix that explicitly incorporates time-varying velocity to flexibly model complex non-linear motions, while strictly isolating the effects of Gaussian motion from the geometry-related conditional Gaussian covariance. Furthermore, a Geometric Deformation Network is introduced to refine Gaussian shapes and orientations using spatio-temporal context and velocity cues, enhancing temporal geometric modeling. Extensive experiments on public datasets demonstrate that VeGaS achieves state-of-the-art performance.

  </details>

- **[PackUV: Packed Gaussian UV Maps for 4D Volumetric Video](https://arxiv.org/abs/2602.23040)**  
  *Aashish Rai, Angela Xing, Anushka Agarwal, Xiaoyan Cong, Zekun Li, Tao Lu, Aayush Prakash, Srinath Sridhar*  
  `2026-02-26` · `cs.CV` · [abs](https://arxiv.org/abs/2602.23040) · [pdf](https://arxiv.org/pdf/2602.23040.pdf)
  > 💡 将高斯点云属性编码为多尺度UV图集，实现与标准视频编码兼容的4D体视频，解决长序列大运动下的时空不一致问题。

  <details><summary>Abstract</summary>

  Volumetric videos offer immersive 4D experiences, but remain difficult to reconstruct, store, and stream at scale. Existing Gaussian Splatting based methods achieve high-quality reconstruction but break down on long sequences, temporal inconsistency, and fail under large motions and disocclusions. Moreover, their outputs are typically incompatible with conventional video coding pipelines, preventing practical applications. We introduce PackUV, a novel 4D Gaussian representation that maps all Gaussian attributes into a sequence of structured, multi-scale UV atlas, enabling compact, image-native storage. To fit this representation from multi-view videos, we propose PackUV-GS, a temporally consistent fitting method that directly optimizes Gaussian parameters in the UV domain. A flow-guided Gaussian labeling and video keyframing module identifies dynamic Gaussians, stabilizes static regions, and preserves temporal coherence even under large motions and disocclusions. The resulting UV atlas format is the first unified volumetric video representation compatible with standard video codecs (e.g., FFV1) without losing quality, enabling efficient streaming within existing multimedia infrastructure. To evaluate long-duration volumetric capture, we present PackUV-2B, the largest multi-view video dataset to date, featuring more than 50 synchronized cameras, substantial motion, and frequent disocclusions across 100 sequences and 2B (billion) frames. Extensive experiments demonstrate that our method surpasses existing baselines in rendering fidelity while scaling to sequences up to 30 minutes with consistent quality.

  </details>

- **[AeroDGS: Physically Consistent Dynamic Gaussian Splatting for Single-Sequence Aerial 4D Reconstruction](https://arxiv.org/abs/2602.22376)**  
  *Hanyang Liu, Rongjun Qin*  
  `2026-02-25` · `cs.CV` · [abs](https://arxiv.org/abs/2602.22376) · [pdf](https://arxiv.org/pdf/2602.22376.pdf)
  > 💡 提出AeroDGS，以单目几何提升和物理引导优化解决航拍动态重建的深度模糊，实现高保真四维重建。

  <details><summary>Abstract</summary>

  Recent advances in 4D scene reconstruction have significantly improved dynamic modeling across various domains. However, existing approaches remain limited under aerial conditions with single-view capture, wide spatial range, and dynamic objects of limited spatial footprint and large motion disparity. These challenges cause severe depth ambiguity and unstable motion estimation, making monocular aerial reconstruction inherently ill-posed. To this end, we present AeroDGS, a physics-guided 4D Gaussian splatting framework for monocular UAV videos. AeroDGS introduces a Monocular Geometry Lifting module that reconstructs reliable static and dynamic geometry from a single aerial sequence, providing a robust basis for dynamic estimation. To further resolve monocular ambiguity, we propose a Physics-Guided Optimization module that incorporates differentiable ground-support, upright-stability, and trajectory-smoothness priors, transforming ambiguous image cues into physically consistent motion. The framework jointly refines static backgrounds and dynamic entities with stable geometry and coherent temporal evolution. We additionally build a real-world UAV dataset that spans various altitudes and motion conditions to evaluate dynamic aerial reconstruction. Experiments on synthetic and real UAV scenes demonstrate that AeroDGS outperforms state-of-the-art methods, achieving superior reconstruction fidelity in dynamic aerial environments.

  </details>

- **[Space-Time Forecasting of Dynamic Scenes with Motion-aware Gaussian Grouping](https://arxiv.org/abs/2602.21668)**  
  *Junmyeong Lee, Hoseung Choi, Minsu Cho*  
  `2026-02-25` · `cs.CV` · [abs](https://arxiv.org/abs/2602.21668) · [pdf](https://arxiv.org/pdf/2602.21668.pdf)
  > 💡 MoGaF利用运动感知高斯分组和分组优化，基于4DGS实现长期动态场景预测，提升运动一致性和稳定性。

  <details><summary>Abstract</summary>

  Forecasting dynamic scenes remains a fundamental challenge in computer vision, as limited observations make it difficult to capture coherent object-level motion and long-term temporal evolution. We present Motion Group-aware Gaussian Forecasting (MoGaF), a framework for long-term scene extrapolation built upon the 4D Gaussian Splatting representation. MoGaF introduces motion-aware Gaussian grouping and group-wise optimization to enforce physically consistent motion across both rigid and non-rigid regions, yielding spatially coherent dynamic representations. Leveraging this structured space-time representation, a lightweight forecasting module predicts future motion, enabling realistic and temporally stable scene evolution. Experiments on synthetic and real-world datasets demonstrate that MoGaF consistently outperforms existing baselines in rendering quality, motion plausibility, and long-term forecasting stability. Our project page is available at https://slime0519.github.io/mogaf

  </details>

- **[RU4D-SLAM: Reweighting Uncertainty in Gaussian Splatting SLAM for 4D Scene Reconstruction](https://arxiv.org/abs/2602.20807)**  
  *Yangfan Zhao, Hanwei Zhang, Ke Huang, Qiufeng Wang, Zhenzhou Shao, Dengyu Wu*  
  `2026-02-24` · `cs.CV` · [abs](https://arxiv.org/abs/2602.20807) · [pdf](https://arxiv.org/pdf/2602.20807.pdf)
  > 💡 针对动态环境下的SLAM与4D重建困难，提出不确定性重加权4D高斯溅射框架，引入运动模糊渲染与语义引导重加权，显著提升轨迹精度与场景重建质量。

  <details><summary>Abstract</summary>

  Combining 3D Gaussian splatting with Simultaneous Localization and Mapping (SLAM) has gained popularity as it enables continuous 3D environment reconstruction during motion. However, existing methods struggle in dynamic environments, particularly moving objects complicate 3D reconstruction and, in turn, hinder reliable tracking. The emergence of 4D reconstruction, especially 4D Gaussian splatting, offers a promising direction for addressing these challenges, yet its potential for 4D-aware SLAM remains largely underexplored. Along this direction, we propose a robust and efficient framework, namely Reweighting Uncertainty in Gaussian Splatting SLAM (RU4D-SLAM) for 4D scene reconstruction, that introduces temporal factors into spatial 3D representation while incorporating uncertainty-aware perception of scene changes, blurred image synthesis, and dynamic scene reconstruction. We enhance dynamic scene representation by integrating motion blur rendering, and improve uncertainty-aware tracking by extending per-pixel uncertainty modeling, which is originally designed for static scenarios, to handle blurred images. Furthermore, we propose a semantic-guided reweighting mechanism for per-pixel uncertainty estimation in dynamic scenes, and introduce a learnable opacity weight to support adaptive 4D mapping. Extensive experiments on standard benchmarks demonstrate that our method substantially outperforms state-of-the-art approaches in both trajectory accuracy and 4D scene reconstruction, particularly in dynamic environments with moving objects and low-quality inputs. Code available: https://ru4d-slam.github.io

  </details>

- **[Time-Archival Camera Virtualization for Sports and Visual Performances](https://arxiv.org/abs/2602.15181)**  
  *Yunxiao Zhang, William Stone, Suryansh Kumar*  
  `2026-02-16` · `cs.CV` · [abs](https://arxiv.org/abs/2602.15181) · [pdf](https://arxiv.org/pdf/2602.15181.pdf)
  > 💡 针对动态场景快速运动及多物体不连贯问题，采用神经体素渲染和刚性变换建模，实现时间存档与回顾性渲染。

  <details><summary>Abstract</summary>

  Camera virtualization -- an emerging solution to novel view synthesis -- holds transformative potential for visual entertainment, live performances, and sports broadcasting by enabling the generation of photorealistic images from novel viewpoints using images from a limited set of calibrated multiple static physical cameras. Despite recent advances, achieving spatially and temporally coherent and photorealistic rendering of dynamic scenes with efficient time-archival capabilities, particularly in fast-paced sports and stage performances, remains challenging for existing approaches. Recent methods based on 3D Gaussian Splatting (3DGS) for dynamic scenes could offer real-time view-synthesis results. Yet, they are hindered by their dependence on accurate 3D point clouds from the structure-from-motion method and their inability to handle large, non-rigid, rapid motions of different subjects (e.g., flips, jumps, articulations, sudden player-to-player transitions). Moreover, independent motions of multiple subjects can break the Gaussian-tracking assumptions commonly used in 4DGS, ST-GS, and other dynamic splatting variants. This paper advocates reconsidering a neural volume rendering formulation for camera virtualization and efficient time-archival capabilities, making it useful for sports broadcasting and related applications. By modeling a dynamic scene as rigid transformations across multiple synchronized camera views at a given time, our method performs neural representation learning, providing enhanced visual rendering quality at test time. A key contribution of our approach is its support for time-archival, i.e., users can revisit any past temporal instance of a dynamic scene and can perform novel view synthesis, enabling retrospective rendering for replay, analysis, and archival of live events, a functionality absent in existing neural rendering approaches and novel view synthesis...

  </details>

- **[Faster-GS: Analyzing and Improving Gaussian Splatting Optimization](https://arxiv.org/abs/2602.09999)**  
  *Florian Hahlbohm, Linus Franke, Martin Eisemann, Marcus Magnor*  
  `2026-02-10` · `cs.CV` · [abs](https://arxiv.org/abs/2602.09999) · [pdf](https://arxiv.org/pdf/2602.09999.pdf)
  > 💡 通过整合并改进数值稳定性等优化，实现5倍训练加速且保持质量，并扩展到4DGS。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have focused on accelerating optimization while preserving reconstruction quality. However, many proposed methods entangle implementation-level improvements with fundamental algorithmic modifications or trade performance for fidelity, leading to a fragmented research landscape that complicates fair comparison. In this work, we consolidate and evaluate the most effective and broadly applicable strategies from prior 3DGS research and augment them with several novel optimizations. We further investigate underexplored aspects of the framework, including numerical stability, Gaussian truncation, and gradient approximation. The resulting system, Faster-GS, provides a rigorously optimized algorithm that we evaluate across a comprehensive suite of benchmarks. Our experiments demonstrate that Faster-GS achieves up to 5$\times$ faster training while maintaining visual quality, establishing a new cost-effective and resource efficient baseline for 3DGS optimization. Furthermore, we demonstrate that optimizations can be applied to 4D Gaussian reconstruction, leading to efficient non-rigid scene optimization.

  </details>

- **[Grow with the Flow: 4D Reconstruction of Growing Plants with Gaussian Flow Fields](https://arxiv.org/abs/2602.08958)**  
  *Weihan Luo, Lily Goli, Sherwin Bahmani, Felix Taubner, Andrea Tagliasacchi, David B. Lindell*  
  `2026-02-09` · `cs.CV` · [abs](https://arxiv.org/abs/2602.08958) · [pdf](https://arxiv.org/pdf/2602.08958.pdf)
  > 💡 针对植物生长中几何持续变化导致时间不一致问题，提出GrowFlow用3D高斯与神经ODE建模连续流场，实现高质量渲染与时序连贯重建。

  <details><summary>Abstract</summary>

  Modeling the time-varying 3D appearance of plants during growth poses unique challenges: unlike most dynamic scenes, plants continuously generate new geometry as they expand, branch, and differentiate. Existing dynamic scene representations are ill-suited to this setting: deformation fields provide insufficient constraints to yield physically plausible scene dynamics, and 4D Gaussian splatting represents the same physical structures with different Gaussian primitives at different times, breaking temporal consistency. We introduce GrowFlow, a dynamic representation that couples 3D Gaussian primitives with a neural ordinary differential equation to model plant growth as a continuous flow field over geometric parameters (position, scale, and orientation). Our representation enables consistent appearance rendering and models nonlinear, continuous-time growth dynamics with full temporal correspondences for every primitive. To initialize a sufficient set of Gaussian primitives, we first reconstruct the mature plant and then learn a reverse-growth process, effectively simulating the plant's developmental history in reverse. GrowFlow achieves superior image quality and geometric coherence compared to prior methods on a new, multi-view timelapse dataset of plant growth, and provides the first temporally coherent representation for appearance modeling of growing 3D structures.

  </details>

- **[TIBR4D: Tracing-Guided Iterative Boundary Refinement for Efficient 4D Gaussian Segmentation](https://arxiv.org/abs/2602.08540)**  
  *He Wu, Xia Yan, Yanghui Xu, Liegang Xia, Jiazhou Chen*  
  `2026-02-09` · `cs.CV` · [abs](https://arxiv.org/abs/2602.08540) · [pdf](https://arxiv.org/pdf/2602.08540.pdf)
  > 💡 提出无学习4D高斯分割框架，通过迭代实例追踪和渲染范围控制，高效处理运动遮挡并细化边界。

  <details><summary>Abstract</summary>

  Object-level segmentation in dynamic 4D Gaussian scenes remains challenging due to complex motion, occlusions, and ambiguous boundaries. In this paper, we present an efficient learning-free 4D Gaussian segmentation framework that lifts video segmentation masks to 4D spaces, whose core is a two-stage iterative boundary refinement, TIBR4D. The first stage is an Iterative Gaussian Instance Tracing (IGIT) at the temporal segment level. It progressively refines Gaussian-to-instance probabilities through iterative tracing, and extracts corresponding Gaussian point clouds that better handle occlusions and preserve completeness of object structures compared to existing one-shot threshold-based methods. The second stage is a frame-wise Gaussian Rendering Range Control (RCC) via suppressing highly uncertain Gaussians near object boundaries while retaining their core contributions for more accurate boundaries. Furthermore, a temporal segmentation merging strategy is proposed for IGIT to balance identity consistency and dynamic awareness. Longer segments enforce stronger multi-frame constraints for stable identities, while shorter segments allow identity changes to be captured promptly. Experiments on HyperNeRF and Neu3D demonstrate that our method produces accurate object Gaussian point clouds with clearer boundaries and higher efficiency compared to SOTA methods.

  </details>

- **[Uncertainty-Aware 4D Gaussian Splatting for Monocular Occluded Human Rendering](https://arxiv.org/abs/2602.06343)**  
  *Weiquan Wang, Feifei Shao, Lin Li, Zhen Wang, Jun Xiao, Long Chen*  
  `2026-02-06` · `cs.CV` · [abs](https://arxiv.org/abs/2602.06343) · [pdf](https://arxiv.org/pdf/2602.06343.pdf)
  > 💡 单目视频遮挡下人体渲染退化，提出U-4DGS用概率形变网络渲染不确定性图调节梯度，并施加置信度正则化，达SOTA保真度和鲁棒性。

  <details><summary>Abstract</summary>

  High-fidelity rendering of dynamic humans from monocular videos typically degrades catastrophically under occlusions. Existing solutions incorporate external priors-either hallucinating missing content via generative models, which induces severe temporal flickering, or imposing rigid geometric heuristics that fail to capture diverse appearances. To this end, we reformulate the task as a Maximum A Posteriori estimation problem under heteroscedastic observation noise. In this paper, we propose U-4DGS, a framework integrating a Probabilistic Deformation Network and a Joint Rasterization pipeline. This architecture renders pixel-aligned uncertainty maps that act as an adaptive gradient modulator, automatically attenuating artifacts from unreliable observations. Furthermore, to prevent geometric drift in regions lacking reliable visual cues, we enforce Confidence-Aware Regularizations, which leverage the learned uncertainty to selectively propagate spatial-temporal validity. Extensive experiments on the ZJU-MoCap and OcMotion datasets demonstrate that U-4DGS achieves state-of-the-art rendering fidelity and robustness.

  </details>

- **[ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors](https://arxiv.org/abs/2602.05572)**  
  *Zhenxiao Liang, Ning Zhang, Youbao Tang, Ruei-Sung Lin, Qixing Huang, Peng Chang, Jing Xiao*  
  `2026-02-05` · `cs.CV` · [abs](https://arxiv.org/abs/2602.05572) · [pdf](https://arxiv.org/pdf/2602.05572.pdf)
  > 💡 利用2D视觉先验和无模板两步法（粗几何+神经变形细化），实现单目视频中高保真且稳健的4D人体重建。

  <details><summary>Abstract</summary>

  We introduce ShapeGaussian, a high-fidelity, template-free method for 4D human reconstruction from casual monocular videos. Generic reconstruction methods lacking robust vision priors, such as 4DGS, struggle to capture high-deformation human motion without multi-view cues. While template-based approaches, primarily relying on SMPL, such as HUGS, can produce photorealistic results, they are highly susceptible to errors in human pose estimation, often leading to unrealistic artifacts. In contrast, ShapeGaussian effectively integrates template-free vision priors to achieve both high-fidelity and robust scene reconstructions. Our method follows a two-step pipeline: first, we learn a coarse, deformable geometry using pretrained models that estimate data-driven priors, providing a foundation for reconstruction. Then, we refine this geometry using a neural deformation model to capture fine-grained dynamic details. By leveraging 2D vision priors, we mitigate artifacts from erroneous pose estimation in template-based methods and employ multiple reference frames to resolve the invisibility issue of 2D keypoints in a template-free manner. Extensive experiments demonstrate that ShapeGaussian surpasses template-based methods in reconstruction accuracy, achieving superior visual quality and robustness across diverse human motions in casual monocular videos.

  </details>

- **[SharpTimeGS: Sharp and Stable Dynamic Gaussian Splatting via Lifespan Modulation](https://arxiv.org/abs/2602.02989)**  
  *Zhanfeng Liao, Jiajun Zhang, Hanzhang Tu, Zhixi Wang, Yunqi Gao, Hongwen Zhang, Yebin Liu*  
  `2026-02-03` · `cs.CV` · [abs](https://arxiv.org/abs/2602.02989) · [pdf](https://arxiv.org/pdf/2602.02989.pdf)
  > 💡 提出可学习寿命参数调制时间可见性和运动，解耦运动与时长，实现动态场景清晰稳定渲染，达SOTA 4

  <details><summary>Abstract</summary>

  Novel view synthesis of dynamic scenes is fundamental to achieving photorealistic 4D reconstruction and immersive visual experiences. Recent progress in Gaussian-based representations has significantly improved real-time rendering quality, yet existing methods still struggle to maintain a balance between long-term static and short-term dynamic regions in both representation and optimization. To address this, we present SharpTimeGS, a lifespan-aware 4D Gaussian framework that achieves temporally adaptive modeling of both static and dynamic regions under a unified representation. Specifically, we introduce a learnable lifespan parameter that reformulates temporal visibility from a Gaussian-shaped decay into a flat-top profile, allowing primitives to remain consistently active over their intended duration and avoiding redundant densification. In addition, the learned lifespan modulates each primitives' motion, reducing drift in long-lived static points while retaining unrestricted motion for short-lived dynamic ones. This effectively decouples motion magnitude from temporal duration, improving long-term stability without compromising dynamic fidelity. Moreover, we design a lifespan-velocity-aware densification strategy that mitigates optimization imbalance between static and dynamic regions by allocating more capacity to regions with pronounced motion while keeping static areas compact and stable. Extensive experiments on multiple benchmarks demonstrate that our method achieves state-of-the-art performance while supporting real-time rendering up to 4K resolution at 100 FPS on one RTX 4090.

  </details>

- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148)**  
  *Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu*  
  `2026-01-29` · `cs.CV` · [abs](https://arxiv.org/abs/2602.00148) · [pdf](https://arxiv.org/pdf/2602.00148.pdf)
  > 💡 针对物理动态建模成本高问题，提出神经高斯力场端到端框架，整合感知与物理建模实现快速4D视频生成，速度提升两个数量级。

  <details><summary>Abstract</summary>

  Predicting physical dynamics from raw visual data remains a major challenge in AI. While recent video generation models have achieved impressive visual quality, they still cannot consistently generate physically plausible videos due to a lack of modeling of physical laws. Recent approaches combining 3D Gaussian splatting and physics engines can produce physically plausible videos, but are hindered by high computational costs in both reconstruction and simulation, and often lack robustness in complex real-world scenarios. To address these issues, we introduce Neural Gaussian Force Field (NGFF), an end-to-end neural framework that integrates 3D Gaussian perception with physics-based dynamic modeling to generate interactive, physically realistic 4D videos from multi-view RGB inputs, achieving two orders of magnitude faster than prior Gaussian simulators. To support training, we also present GSCollision, a 4D Gaussian dataset featuring diverse materials, multi-object interactions, and complex scenes, totaling over 640k rendered physical videos (~4 TB). Evaluations on synthetic and real 3D scenarios show NGFF's strong generalization and robustness in physical reasoning, advancing video prediction towards physics-grounded world models.

  </details>

- **[Graphical X Splatting (GraphiXS): A Graphical Model for 4D Gaussian Splatting under Uncertainty](https://arxiv.org/abs/2601.19843)**  
  *Doğa Yılmaz, Jialin Zhu, Deshan Gong, He Wang*  
  `2026-01-27` · `cs.GR` · [abs](https://arxiv.org/abs/2601.19843) · [pdf](https://arxiv.org/pdf/2601.19843.pdf)
  > 💡 GraphiXS 提出概率框架，系统性建模 4DGS 中多种数据不确定性，支持多种基元，性能优于现有方法。

  <details><summary>Abstract</summary>

  We propose a new framework to systematically incorporate data uncertainty in Gaussian Splatting. Being the new paradigm of neural rendering, Gaussian Splatting has been investigated in many applications, with the main effort in extending its representation, improving its optimization process, and accelerating its speed. However, one orthogonal, much needed, but under-explored area is data uncertainty. In standard 4D Gaussian Splatting, data uncertainty can manifest as view sparsity, missing frames, camera asynchronization, etc. So far, there has been little research to holistically incorporating various types of data uncertainty under a single framework. To this end, we propose Graphical X Splatting, or GraphiXS, a new probabilistic framework that considers multiple types of data uncertainty, aiming for a fundamental augmentation of the current 4D Gaussian Splatting paradigm into a probabilistic setting. GraphiXS is general and can be instantiated with a range of primitives, e.g. Gaussians, Student's-t. Furthermore, GraphiXS can be used to `upgrade' existing methods to accommodate data uncertainty. Through exhaustive evaluation and comparison, we demonstrate that GraphiXS can systematically model various uncertainties in data, outperform existing methods in many settings where data are missing or polluted in space and time, and therefore is a major generalization of the current 4D Gaussian Splatting research.

  </details>

- **[Uncertainty-Aware 3D Emotional Talking Face Synthesis with Emotion Prior Distillation](https://arxiv.org/abs/2601.19112)**  
  *Nanhan Shen, Zhilei Liu*  
  `2026-01-27` · `cs.AI` · [abs](https://arxiv.org/abs/2601.19112) · [pdf](https://arxiv.org/pdf/2601.19112.pdf)
  > 💡 针对情感对齐差和融合忽略不确定性问题，提出UA-3DTalk采用情感先验

  <details><summary>Abstract</summary>

  Emotional Talking Face synthesis is pivotal in multimedia and signal processing, yet existing 3D methods suffer from two critical challenges: poor audio-vision emotion alignment, manifested as difficult audio emotion extraction and inadequate control over emotional micro-expressions; and a one-size-fits-all multi-view fusion strategy that overlooks uncertainty and feature quality differences, undermining rendering quality. We propose UA-3DTalk, Uncertainty-Aware 3D Emotional Talking Face Synthesis with emotion prior distillation, which has three core modules: the Prior Extraction module disentangles audio into content-synchronized features for alignment and person-specific complementary features for individualization; the Emotion Distillation module introduces a multi-modal attention-weighted fusion mechanism and 4D Gaussian encoding with multi-resolution code-books, enabling fine-grained audio emotion extraction and precise control of emotional micro-expressions; the Uncertainty-based Deformation deploys uncertainty blocks to estimate view-specific aleatoric (input noise) and epistemic (model parameters) uncertainty, realizing adaptive multi-view fusion and incorporating a multi-head decoder for Gaussian primitive optimization to mitigate the limitations of uniform-weight fusion. Extensive experiments on regular and emotional datasets show UA-3DTalk outperforms state-of-the-art methods like DEGSTalk and EDTalk by 5.2% in E-FID for emotion alignment, 3.1% in SyncC for lip synchronization, and 0.015 in LPIPS for rendering quality. Project page: https://mrask999.github.io/UA-3DTalk

  </details>

- **[DriveExplorer: Images-Only Decoupled 4D Reconstruction with Progressive Restoration for Driving View Extrapolation](https://arxiv.org/abs/2512.23983)**  
  *Yuang Jia, Jinlong Wang, Jiayi Zhao, Chunlam Li, Shunzhou Wang, Wei Gao*  
  `2025-12-30` · `cs.CV` · [abs](https://arxiv.org/abs/2512.23983) · [pdf](https://arxiv.org/pdf/2512.23983.pdf)
  > 💡 仅用图像和相机位姿，通过静态与动态点云融合及可变形4D高斯重建，结合扩散模型逐步细化实现高质量驾驶视图外推。

  <details><summary>Abstract</summary>

  This paper presents an effective solution for view extrapolation in autonomous driving scenarios. Recent approaches focus on generating shifted novel view images from given viewpoints using diffusion models. However, these methods heavily rely on priors such as LiDAR point clouds, 3D bounding boxes, and lane annotations, which demand expensive sensors or labor-intensive labeling, limiting applicability in real-world deployment. In this work, with only images and optional camera poses, we first estimate a global static point cloud and per-frame dynamic point clouds, fusing them into a unified representation. We then employ a deformable 4D Gaussian framework to reconstruct the scene. The initially trained 4D Gaussian model renders degraded and pseudo-images to train a video diffusion model. Subsequently, progressively shifted Gaussian renderings are iteratively refined by the diffusion model,and the enhanced results are incorporated back as training data for 4DGS. This process continues until extrapolation reaches the target viewpoints. Compared with baselines, our method produces higher-quality images at novel extrapolated viewpoints.

  </details>

- **[AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences](https://arxiv.org/abs/2512.20943)**  
  *Zhe Wang, Jinghang Li, Yifei Zhu*  
  `2025-12-24` · `cs.GR` · [abs](https://arxiv.org/abs/2512.20943) · [pdf](https://arxiv.org/pdf/2512.20943.pdf)
  > 💡 针对4DGS长序列质量退化与高带宽问题，AirGS采用多通道2D转换、关键帧识别及自适应剪枝，降低质量偏差20%并提速6倍。

  <details><summary>Abstract</summary>

  Free-viewpoint video (FVV) enables immersive viewing experiences by allowing users to view scenes from arbitrary perspectives. As a prominent reconstruction technique for FVV generation, 4D Gaussian Splatting (4DGS) models dynamic scenes with time-varying 3D Gaussian ellipsoids and achieves high-quality rendering via fast rasterization. However, existing 4DGS approaches suffer from quality degradation over long sequences and impose substantial bandwidth and storage overhead, limiting their applicability in real-time and wide-scale deployments. Therefore, we present AirGS, a streaming-optimized 4DGS framework that rearchitects the training and delivery pipeline to enable high-quality, low-latency FVV experiences. AirGS converts Gaussian video streams into multi-channel 2D formats and intelligently identifies keyframes to enhance frame reconstruction quality. It further combines temporal coherence with inflation loss to reduce training time and representation size. To support communication-efficient transmission, AirGS models 4DGS delivery as an integer linear programming problem and design a lightweight pruning level selection algorithm to adaptively prune the Gaussian updates to be transmitted, balancing reconstruction quality and bandwidth consumption. Extensive experiments demonstrate that AirGS reduces quality deviation in PSNR by more than 20% when scene changes, maintains frame-level PSNR consistently above 30, accelerates training by 6 times, reduces per-frame transmission size by nearly 50% compared to the SOTA 4DGS approaches.

  </details>

- **[4D Gaussian Splatting as a Learned Dynamical System](https://arxiv.org/abs/2512.19648)**  
  *Arnold Caleb Asiimwe, Carl Vondrick*  
  `2025-12-22` · `cs.CV` · [abs](https://arxiv.org/abs/2512.19648) · [pdf](https://arxiv.org/pdf/2512.19648.pdf)
  > 💡 将4D高斯溅射视为学习动力学系统，通过神经动力学场建模运动，实现样本高效学习与时间外推。

  <details><summary>Abstract</summary>

  We reinterpret 4D Gaussian Splatting as a continuous-time dynamical system, where scene motion arises from integrating a learned neural dynamical field rather than applying per-frame deformations. This formulation, which we call EvoGS, treats the Gaussian representation as an evolving physical system whose state evolves continuously under a learned motion law. This unlocks capabilities absent in deformation-based approaches:(1) sample-efficient learning from sparse temporal supervision by modeling the underlying motion law; (2) temporal extrapolation enabling forward and backward prediction beyond observed time ranges; and (3) compositional dynamics that allow localized dynamics injection for controllable scene synthesis. Experiments on dynamic scene benchmarks show that EvoGS achieves better motion coherence and temporal consistency compared to deformation-field baselines while maintaining real-time rendering

  </details>

- **[D$^2$GSLAM: 4D Dynamic Gaussian Splatting SLAM](https://arxiv.org/abs/2512.09411)**  
  *Siting Zhu, Yuxiang Huang, Wenhua Wu, Chaokang Jiang, Yongbo Chen, I-Ming Chen, Hesheng Wang*  
  `2025-12-10` · `cs.RO` · [abs](https://arxiv.org/abs/2512.09411) · [pdf](https://arxiv.org/pdf/2512.09411.pdf)
  > 💡 利用动态静态高斯表示和几何提示分离，实现动态场景下高精度重建与鲁棒跟踪。

  <details><summary>Abstract</summary>

  Recent advances in Dense Simultaneous Localization and Mapping (SLAM) have demonstrated remarkable performance in static environments. However, dense SLAM in dynamic environments remains challenging. Most methods directly remove dynamic objects and focus solely on static scene reconstruction, which ignores the motion information contained in these dynamic objects. In this paper, we present D$^2$GSLAM, a novel dynamic SLAM system utilizing Gaussian representation, which simultaneously performs accurate dynamic reconstruction and robust tracking within dynamic environments. Our system is composed of four key components: (i) We propose a geometric-prompt dynamic separation method to distinguish between static and dynamic elements of the scene. This approach leverages the geometric consistency of Gaussian representation and scene geometry to obtain coarse dynamic regions. The regions then serve as prompts to guide the refinement of the coarse mask for achieving accurate motion mask. (ii) To facilitate accurate and efficient mapping of the dynamic scene, we introduce dynamic-static composite representation that integrates static 3D Gaussians with dynamic 4D Gaussians. This representation allows for modeling the transitions between static and dynamic states of objects in the scene for composite mapping and optimization. (iii) We employ a progressive pose refinement strategy that leverages both the multi-view consistency of static scene geometry and motion information from dynamic objects to achieve accurate camera tracking. (iv) We introduce a motion consistency loss, which leverages the temporal continuity in object motions for accurate dynamic modeling. Our D$^2$GSLAM demonstrates superior performance on dynamic scenes in terms of mapping and tracking accuracy, while also showing capability in accurate dynamic modeling.

  </details>

- **[MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification](https://arxiv.org/abs/2512.09270)**  
  *Sangwoon Kwak, Weeyoung Kwon, Jun Young Jeong, Geonho Kim, Won-Sik Cheong, Jihyong Oh*  
  `2025-12-10` · `cs.CV` · [abs](https://arxiv.org/abs/2512.09270) · [pdf](https://arxiv.org/pdf/2512.09270.pdf)
  > 💡 针对长范围4D动态场景的内存爆炸与闪烁问题，提出锚点中继双向混合与层次稠密化，实现无闪烁高效重建。

  <details><summary>Abstract</summary>

  Recent advances in 4D Gaussian Splatting (4DGS) have extended the high-speed rendering capability of 3D Gaussian Splatting (3DGS) into the temporal domain, enabling real-time rendering of dynamic scenes. However, one of the major remaining challenges lies in modeling long-range motion-contained dynamic videos, where a naive extension of existing methods leads to severe memory explosion, temporal flickering, and failure to handle appearing or disappearing occlusions over time. To address these challenges, we propose a novel 4DGS framework characterized by an Anchor Relay-based Bidirectional Blending (ARBB) mechanism, named MoRel, which enables temporally consistent and memory-efficient modeling of long-range dynamic scenes. Our method progressively constructs locally canonical anchor spaces at key-frame time index and models inter-frame deformations at the anchor level, enhancing temporal coherence. By learning bidirectional deformations between KfA and adaptively blending them through learnable opacity control, our approach mitigates temporal discontinuities and flickering artifacts. We further introduce a Feature-variance-guided Hierarchical Densification (FHD) scheme that effectively densifies KfA's while keeping rendering quality, based on an assigned level of feature-variance. To effectively evaluate our model's capability to handle real-world long-range 4D motion, we newly compose long-range 4D motion-contained dataset, called SelfCap$_{\text{LR}}$. It has larger average dynamic motion magnitude, captured at spatially wider spaces, compared to previous dynamic video datasets. Overall, our MoRel achieves temporally coherent and flicker-free long-range 4D reconstruction while maintaining bounded memory usage, demonstrating both scalability and efficiency in dynamic Gaussian-based representations.

  </details>

- **[Visionary: The World Model Carrier Built on WebGPU-Powered Gaussian Splatting Platform](https://arxiv.org/abs/2512.08478)**  
  *Yuning Gong, Yifei Liu, Yifan Zhan, Muyao Niu, Xueying Li, Yuanjun Liao, Jiaming Chen, Yuanyuan Gao, Jiaqi Chen, Minming Chen, Li Zhou, Yuning Zhang, Wei Wang, Xiaoqing Hou, Huaxi Huang, Shixiang Tang, Le Ma, Dingwen Zhang, Xue Yang, Junchi Yan, Yanchi Zhang, Yinqiang Zheng, Xiao Sun, Zhihang Zhong*  
  `2025-12-09` · `cs.CV` · [abs](https://arxiv.org/abs/2512.08478) · [pdf](https://arxiv.org/pdf/2512.08478.pdf)
  > 💡 提出WebGPU驱动的Gaussian Splatting平台Visionary，实现高效神经渲染和生成后处理，降低3DGS部署门槛。

  <details><summary>Abstract</summary>

  Neural rendering, particularly 3D Gaussian Splatting (3DGS), has evolved rapidly and become a key component for building world models. However, existing viewer solutions remain fragmented, heavy, or constrained by legacy pipelines, resulting in high deployment friction and limited support for dynamic content and generative models. In this work, we present Visionary, an open, web-native platform for real-time various Gaussian Splatting and meshes rendering. Built on an efficient WebGPU renderer with per-frame ONNX inference, Visionary enables dynamic neural processing while maintaining a lightweight, "click-to-run" browser experience. It introduces a standardized Gaussian Generator contract, which not only supports standard 3DGS rendering but also allows plug-and-play algorithms to generate or update Gaussians each frame. Such inference also enables us to apply feedforward generative post-processing. The platform further offers a plug in three.js library with a concise TypeScript API for seamless integration into existing web applications. Experiments show that, under identical 3DGS assets, Visionary achieves superior rendering efficiency compared to current Web viewers due to GPU-based primitive sorting. It already supports multiple variants, including MLP-based 3DGS, 4DGS, neural avatars, and style transformation or enhancement networks. By unifying inference and rendering directly in the browser, Visionary significantly lowers the barrier to reproduction, comparison, and deployment of 3DGS-family methods, serving as a unified World Model Carrier for both reconstructive and generative paradigms.

  </details>

- **[Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation](https://arxiv.org/abs/2512.06158)**  
  *Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Victor Chen, Mei Chen*  
  `2025-12-05` · `cs.CV` · [abs](https://arxiv.org/abs/2512.06158) · [pdf](https://arxiv.org/pdf/2512.06158.pdf)
  > 💡 提出Track4DGen，将跟踪运动先验注入扩散模型和混合4D高斯泼溅，解决稀疏输入4D生成的视图不一致与时序漂移。

  <details><summary>Abstract</summary>

  Generating dynamic 4D objects from sparse inputs is difficult because it demands joint preservation of appearance and motion coherence across views and time while suppressing artifacts and temporal drift. We hypothesize that the view discrepancy arises from supervision limited to pixel- or latent-space video-diffusion losses, which lack explicitly temporally aware, feature-level tracking guidance. We present \emph{Track4DGen}, a two-stage framework that couples a multi-view video diffusion model with a foundation point tracker and a hybrid 4D Gaussian Splatting (4D-GS) reconstructor. The central idea is to explicitly inject tracker-derived motion priors into intermediate feature representations for both multi-view video generation and 4D-GS. In Stage One, we enforce dense, feature-level point correspondences inside the diffusion generator, producing temporally consistent features that curb appearance drift and enhance cross-view coherence. In Stage Two, we reconstruct a dynamic 4D-GS using a hybrid motion encoding that concatenates co-located diffusion features (carrying Stage-One tracking priors) with Hex-plane features, and augment them with 4D Spherical Harmonics for higher-fidelity dynamics modeling. \emph{Track4DGen} surpasses baselines on both multi-view video generation and 4D generation benchmarks, yielding temporally stable, text-editable 4D assets. Lastly, we curate \emph{Sketchfab28}, a high-quality dataset for benchmarking object-centric 4D generation and fostering future research.

  </details>

- **[TED-4DGS: Temporally Activated and Embedding-based Deformation for 4DGS Compression](https://arxiv.org/abs/2512.05446)**  
  *Cheng-Yuan Ho, He-Bi Yang, Jui-Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng*  
  `2025-12-05` · `cs.CV` · [abs](https://arxiv.org/abs/2512.05446) · [pdf](https://arxiv.org/pdf/2512.05446.pdf)
  > 💡 针对动态3DGS压缩，提出时间激活与嵌入变形方法，结合隐式神经超先验和自回归模型，实现率失真优化SOTA。

  <details><summary>Abstract</summary>

  Building on the success of 3D Gaussian Splatting (3DGS) in static 3D scene representation, its extension to dynamic scenes, commonly referred to as 4DGS or dynamic 3DGS, has attracted increasing attention. However, designing more compact and efficient deformation schemes together with rate-distortion-optimized compression strategies for dynamic 3DGS representations remains an underexplored area. Prior methods either rely on space-time 4DGS with overspecified, short-lived Gaussian primitives or on canonical 3DGS with deformation that lacks explicit temporal control. To address this, we present TED-4DGS, a temporally activated and embedding-based deformation scheme for rate-distortion-optimized 4DGS compression that unifies the strengths of both families. TED-4DGS is built on a sparse anchor-based 3DGS representation. Each canonical anchor is assigned learnable temporal-activation parameters to specify its appearance and disappearance transitions over time, while a lightweight per-anchor temporal embedding queries a shared deformation bank to produce anchor-specific deformation. For rate-distortion compression, we incorporate an implicit neural representation (INR)-based hyperprior to model anchor attribute distributions, along with a channel-wise autoregressive model to capture intra-anchor correlations. With these novel elements, our scheme achieves state-of-the-art rate-distortion performance on several real-world datasets. To the best of our knowledge, this work represents one of the first attempts to pursue a rate-distortion-optimized compression framework for dynamic 3DGS representations.

  </details>

- **[SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting](https://arxiv.org/abs/2512.04315)**  
  *Yonghan Lee, Tsung-Wei Huang, Shiv Gehlot, Jaehoon Choi, Guan-Ming Su, Dinesh Manocha*  
  `2025-12-03` · `cs.CV` · [abs](https://arxiv.org/abs/2512.04315) · [pdf](https://arxiv.org/pdf/2512.04315.pdf)
  > 💡 利用密集4D轨迹和最优传输实现未同步视频的跨视频对齐与亚帧同步，首个通用多视频4D高斯泼溅方法。

  <details><summary>Abstract</summary>

  Modeling dynamic 3D scenes is challenging due to their high-dimensional nature, which requires aggregating information from multiple views to reconstruct time-evolving 3D geometry and motion. We present a novel multi-video 4D Gaussian Splatting (4DGS) approach designed to handle real-world, unsynchronized video sets. Our approach, SyncTrack4D, directly leverages dense 4D track representation of dynamic scene parts as cues for simultaneous cross-video synchronization and 4DGS reconstruction. We first compute dense per-video 4D feature tracks and cross-video track correspondences by Fused Gromov-Wasserstein optimal transport approach. Next, we perform global frame-level temporal alignment to maximize overlapping motion of matched 4D tracks. Finally, we achieve sub-frame synchronization through our multi-video 4D Gaussian splatting built upon a motion-spline scaffold representation. The final output is a synchronized 4DGS representation with dense, explicit 3D trajectories, and temporal offsets for each video. We evaluate our approach on the Panoptic Studio and SyncNeRF Blender, demonstrating sub-frame synchronization accuracy with an average temporal error below 0.26 frames, and high-fidelity 4D reconstruction reaching 26.3 PSNR scores on the Panoptic Studio dataset. To the best of our knowledge, our work is the first general 4D Gaussian Splatting approach for unsynchronized video sets, without assuming the existence of predefined scene objects or prior models.

  </details>

- **[Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding](https://arxiv.org/abs/2512.03601)**  
  *Haoran Zhou, Gim Hee Lee*  
  `2025-12-03` · `cs.CV` · [abs](https://arxiv.org/abs/2512.03601) · [pdf](https://arxiv.org/pdf/2512.03601.pdf)
  > 💡 融合2D先验到4D高斯泼溅，通过两阶段优化和3D置信图解决动态场景3D不一致，显著提升跟踪、分割和新视图合成精度。

  <details><summary>Abstract</summary>

  Recent advancements in foundation models for 2D vision have substantially improved the analysis of dynamic scenes from monocular videos. However, despite their strong generalization capabilities, these models often lack 3D consistency, a fundamental requirement for understanding scene geometry and motion, thereby causing severe spatial misalignment and temporal flickering in complex 3D environments. In this paper, we present Motion4D, a novel framework that addresses these challenges by integrating 2D priors from foundation models into a unified 4D Gaussian Splatting representation. Our method features a two-part iterative optimization framework: 1) Sequential optimization, which updates motion and semantic fields in consecutive stages to maintain local consistency, and 2) Global optimization, which jointly refines all attributes for long-term coherence. To enhance motion accuracy, we introduce a 3D confidence map that dynamically adjusts the motion priors, and an adaptive resampling process that inserts new Gaussians into under-represented regions based on per-pixel RGB and semantic errors. Furthermore, we enhance semantic coherence through an iterative refinement process that resolves semantic inconsistencies by alternately optimizing the semantic fields and updating prompts of SAM2. Extensive evaluations demonstrate that our Motion4D significantly outperforms both 2D foundation models and existing 3D-based approaches across diverse scene understanding tasks, including point-based tracking, video object segmentation, and novel view synthesis. Our code is available at https://hrzhou2.github.io/motion4d-web/.

  </details>

- **[Dynamic-eDiTor: Training-Free Text-Driven 4D Scene Editing with Multimodal Diffusion Transformer](https://arxiv.org/abs/2512.00677)**  
  *Dong In Lee, Hyungjun Doh, Seunggeun Chi, Runlin Duan, Sangpil Kim, Karthik Ramani*  
  `2025-11-30` · `cs.CV` · [abs](https://arxiv.org/abs/2512.00677) · [pdf](https://arxiv.org/pdf/2512.00677.pdf)
  > 💡 针对4D编辑时空不一致问题，提出基于多模态扩散变压器的无训练框架，通过STGA和CTP实现全局一致编辑。

  <details><summary>Abstract</summary>

  Recent progress in 4D representations, such as Dynamic NeRF and 4D Gaussian Splatting (4DGS), has enabled dynamic 4D scene reconstruction. However, text-driven 4D scene editing remains under-explored due to the challenge of ensuring both multi-view and temporal consistency across space and time during editing. Existing studies rely on 2D diffusion models that edit frames independently, often causing motion distortion, geometric drift, and incomplete editing. We introduce Dynamic-eDiTor, a training-free text-driven 4D editing framework leveraging Multimodal Diffusion Transformer (MM-DiT) and 4DGS. This mechanism consists of Spatio-Temporal Sub-Grid Attention (STGA) for locally consistent cross-view and temporal fusion, and Context Token Propagation (CTP) for global propagation via token inheritance and optical-flow-guided token replacement. Together, these components allow Dynamic-eDiTor to perform seamless, globally consistent multi-view video without additional training and directly optimize pre-trained source 4DGS. Extensive experiments on multi-view video dataset DyNeRF demonstrate that our method achieves superior editing fidelity and both multi-view and temporal consistency prior approaches. Project page for results and code: https://di-lee.github.io/dynamic-eDiTor/

  </details>

- **[Geometry-Consistent 4D Gaussian Splatting for Sparse-Input Dynamic View Synthesis](https://arxiv.org/abs/2511.23044)**  
  *Yiwei Li, Jiannong Cao, Penghui Ruan, Divya Saxena, Songye Zhu, Yinfeng Cao*  
  `2025-11-28` · `cs.CV` · [abs](https://arxiv.org/abs/2511.23044) · [pdf](https://arxiv.org/pdf/2511.23044.pdf)
  > 💡 针对稀疏输入动态视图合成中几何不一致问题，提出动态一致性检查与全局-局部深度正则化，显著提升渲染质量且保持实时性。

  <details><summary>Abstract</summary>

  Gaussian Splatting has been considered as a novel way for view synthesis of dynamic scenes, which shows great potential in AIoT applications such as digital twins. However, recent dynamic Gaussian Splatting methods significantly degrade when only sparse input views are available, limiting their applicability in practice. The issue arises from the incoherent learning of 4D geometry as input views decrease. This paper presents GC-4DGS, a novel framework that infuses geometric consistency into 4D Gaussian Splatting (4DGS), offering real-time and high-quality dynamic scene rendering from sparse input views. While learning-based Multi-View Stereo (MVS) and monocular depth estimators (MDEs) provide geometry priors, directly integrating these with 4DGS yields suboptimal results due to the ill-posed nature of sparse-input 4D geometric optimization. To address these problems, we introduce a dynamic consistency checking strategy to reduce estimation uncertainties of MVS across spacetime. Furthermore, we propose a global-local depth regularization approach to distill spatiotemporal-consistent geometric information from monocular depths, thereby enhancing the coherent geometry and appearance learning within the 4D volume. Extensive experiments on the popular N3DV and Technicolor datasets validate the effectiveness of GC-4DGS in rendering quality without sacrificing efficiency. Notably, our method outperforms RF-DeRF, the latest dynamic radiance field tailored for sparse-input dynamic view synthesis, and the original 4DGS by 2.62dB and 1.58dB in PSNR, respectively, with seamless deployability on resource-constrained IoT edge devices.

  </details>

- **[Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes](https://arxiv.org/abs/2511.21367)**  
  *Yangle Liu, Fengze Li, Kan Liu, Jieming Ma*  
  `2025-11-26` · `cs.CV` · [abs](https://arxiv.org/abs/2511.21367) · [pdf](https://arxiv.org/pdf/2511.21367.pdf)
  > 💡 针对内窥镜场景几何漂移，提出几何引导先验蒸馏与时间嵌入4DGS，联合深度和运动正则化实现时序一致与最优重建。

  <details><summary>Abstract</summary>

  Endoscopic (endo) video exhibits strong view-dependent effects such as specularities, wet reflections, and occlusions. Pure photometric supervision misaligns with geometry and triggers early geometric drift, where erroneous shapes are reinforced during densification and become hard to correct. We ask how to anchor geometry early for 4D Gaussian splatting (4DGS) while maintaining temporal consistency and efficiency in dynamic endoscopic scenes. Thus, we present Endo-G$^{2}$T, a geometry-guided and temporally aware training scheme for time-embedded 4DGS. First, geo-guided prior distillation converts confidence-gated monocular depth into supervision with scale-invariant depth and depth-gradient losses, using a warm-up-to-cap schedule to inject priors softly and avoid early overfitting. Second, a time-embedded Gaussian field represents dynamics in XYZT with a rotor-like rotation parameterization, yielding temporally coherent geometry with lightweight regularization that favors smooth motion and crisp opacity boundaries. Third, keyframe-constrained streaming improves efficiency and long-horizon stability through keyframe-focused optimization under a max-points budget, while non-keyframes advance with lightweight updates. Across EndoNeRF and StereoMIS-P1 datasets, Endo-G$^{2}$T achieves state-of-the-art results among monocular reconstruction baselines.

  </details>

- **[Alias-free 4D Gaussian Splatting](https://arxiv.org/abs/2511.18367)**  
  *Zilong Chen, Huan-ang Gao, Delin Qu, Haohan Chi, Hao Tang, Kai Zhang, Hao Zhao*  
  `2025-11-23` · `cs.CV` · [abs](https://arxiv.org/abs/2511.18367) · [pdf](https://arxiv.org/pdf/2511.18367.pdf)
  > 💡 针对动态场景重建中分辨率变化导致伪影的问题，引入4D尺度自适应滤波与尺度损失，消除高频伪影并减少冗余高斯。

  <details><summary>Abstract</summary>

  Existing dynamic scene reconstruction methods based on Gaussian Splatting enable real-time rendering and generate realistic images. However, adjusting the camera's focal length or the distance between Gaussian primitives and the camera to modify rendering resolution often introduces strong artifacts, stemming from the frequency constraints of 4D Gaussians and Gaussian scale mismatch induced by the 2D dilated filter. To address this, we derive a maximum sampling frequency formulation for 4D Gaussian Splatting and introduce a 4D scale-adaptive filter and scale loss, which flexibly regulates the sampling frequency of 4D Gaussian Splatting. Our approach eliminates high-frequency artifacts under increased rendering frequencies while effectively reducing redundant Gaussians in multi-view video reconstruction. We validate the proposed method through monocular and multi-view video reconstruction experiments.Ours project page: https://4d-alias-free.github.io/4D-Alias-free/

  </details>

- **[Clustered Error Correction with Grouped 4D Gaussian Splatting](https://arxiv.org/abs/2511.16112)**  
  *Taeho Kang, Jaeyeon Park, Kyungjin Lee, Youngki Lee*  
  `2025-11-20` · `cs.CV` · [abs](https://arxiv.org/abs/2511.16112) · [pdf](https://arxiv.org/pdf/2511.16112.pdf)
  > 💡 针对4DGS动态场景重建模糊问题，提出椭圆错误聚类与分组高斯致密化，显著提升渲染质量及时空一致性。

  <details><summary>Abstract</summary>

  Existing 4D Gaussian Splatting (4DGS) methods struggle to accurately reconstruct dynamic scenes, often failing to resolve ambiguous pixel correspondences and inadequate densification in dynamic regions. We address these issues by introducing a novel method composed of two key components: (1) Elliptical Error Clustering and Error Correcting Splat Addition that pinpoints dynamic areas to improve and initialize fitting splats, and (2) Grouped 4D Gaussian Splatting that improves consistency of mapping between splats and represented dynamic objects. Specifically, we classify rendering errors into missing-color and occlusion types, then apply targeted corrections via backprojection or foreground splitting guided by cross-view color consistency. Evaluations on Neural 3D Video and Technicolor datasets demonstrate that our approach significantly improves temporal consistency and achieves state-of-the-art perceptual rendering quality, improving 0.39dB of PSNR on the Technicolor Light Field dataset. Our visualization shows improved alignment between splats and dynamic objects, and the error correction method's capability to identify errors and properly initialize new splats. Our implementation details and source code are available at https://github.com/tho-kn/cem-4dgs.

  </details>

- **[Interaction-Aware 4D Gaussian Splatting for Dynamic Hand-Object Interaction Reconstruction](https://arxiv.org/abs/2511.14540)**  
  *Hao Tian, Chenyangguang Zhang, Rui Liu, Wen Shen, Xiaolin Qin*  
  `2025-11-18` · `cs.CV` · [abs](https://arxiv.org/abs/2511.14540) · [pdf](https://arxiv.org/pdf/2511.14540.pdf)
  > 💡 针对无先验的手-物交互动态重建，提出交互感知4D高斯和分段线性假设，结合手信息变形场与渐进优化，实现SOTA。

  <details><summary>Abstract</summary>

  This paper focuses on a challenging setting of simultaneously modeling geometry and appearance of hand-object interaction scenes without any object priors. We follow the trend of dynamic 3D Gaussian Splatting based methods, and address several significant challenges. To model complex hand-object interaction with mutual occlusion and edge blur, we present interaction-aware hand-object Gaussians with newly introduced optimizable parameters aiming to adopt piecewise linear hypothesis for clearer structural representation. Moreover, considering the complementarity and tightness of hand shape and object shape during interaction dynamics, we incorporate hand information into object deformation field, constructing interaction-aware dynamic fields to model flexible motions. To further address difficulties in the optimization process, we propose a progressive strategy that handles dynamic regions and static background step by step. Correspondingly, explicit regularizations are designed to stabilize the hand-object representations for smooth motion transition, physical interaction reality, and coherent lighting. Experiments show that our approach surpasses existing dynamic 3D-GS-based methods and achieves state-of-the-art performance in reconstructing dynamic hand-object interaction.

  </details>

- **[Dynamic Gaussian Scene Reconstruction from Unsynchronized Videos](https://arxiv.org/abs/2511.11175)**  
  *Zhixin Xu, Hengyu Zhou, Yuan Liu, Wenhan Xue, Hao Pan, Wenping Wang, Bin Wang*  
  `2025-11-14` · `cs.CV` · [abs](https://arxiv.org/abs/2511.11175) · [pdf](https://arxiv.org/pdf/2511.11175.pdf)
  > 💡 针对非同步多视角视频，提出粗到细时间对齐模块，消除时移误差以增强4DGS重建鲁棒性。

  <details><summary>Abstract</summary>

  Multi-view video reconstruction plays a vital role in computer vision, enabling applications in film production, virtual reality, and motion analysis. While recent advances such as 4D Gaussian Splatting (4DGS) have demonstrated impressive capabilities in dynamic scene reconstruction, they typically rely on the assumption that input video streams are temporally synchronized. However, in real-world scenarios, this assumption often fails due to factors like camera trigger delays or independent recording setups, leading to temporal misalignment across views and reduced reconstruction quality. To address this challenge, a novel temporal alignment strategy is proposed for high-quality 4DGS reconstruction from unsynchronized multi-view videos. Our method features a coarse-to-fine alignment module that estimates and compensates for each camera's time shift. The method first determines a coarse, frame-level offset and then refines it to achieve sub-frame accuracy. This strategy can be integrated as a readily integrable module into existing 4DGS frameworks, enhancing their robustness when handling asynchronous data. Experiments show that our approach effectively processes temporally misaligned videos and significantly enhances baseline methods.

  </details>

- **[4DSTR: Advancing Generative 4D Gaussians with Spatial-Temporal Rectification for High-Quality and Consistent 4D Generation](https://arxiv.org/abs/2511.07241)**  
  *Mengmeng Liu, Jiuming Liu, Yunpeng Zhang, Jiangtao Li, Michael Ying Yang, Francesco Nex, Hao Cheng*  
  `2025-11-10` · `cs.CV` · [abs](https://arxiv.org/abs/2511.07241) · [pdf](https://arxiv.org/pdf/2511.07241.pdf)
  > 💡 4D生成缺乏时空一致性，提出时空矫正与自适应密集化剪枝策略，实现高质量、一致性的动态4D内容生成。

  <details><summary>Abstract</summary>

  Remarkable advances in recent 2D image and 3D shape generation have induced a significant focus on dynamic 4D content generation. However, previous 4D generation methods commonly struggle to maintain spatial-temporal consistency and adapt poorly to rapid temporal variations, due to the lack of effective spatial-temporal modeling. To address these problems, we propose a novel 4D generation network called 4DSTR, which modulates generative 4D Gaussian Splatting with spatial-temporal rectification. Specifically, temporal correlation across generated 4D sequences is designed to rectify deformable scales and rotations and guarantee temporal consistency. Furthermore, an adaptive spatial densification and pruning strategy is proposed to address significant temporal variations by dynamically adding or deleting Gaussian points with the awareness of their pre-frame movements. Extensive experiments demonstrate that our 4DSTR achieves state-of-the-art performance in video-to-4D generation, excelling in reconstruction quality, spatial-temporal consistency, and adaptation to rapid temporal movements.

  </details>

- **[Sparse4DGS: 4D Gaussian Splatting for Sparse-Frame Dynamic Scene Reconstruction](https://arxiv.org/abs/2511.07122)**  
  *Changyue Shi, Chuxiao Yang, Xinyuan Hu, Minghao Chen, Wenwen Pan, Yan Yang, Jiajun Ding, Zhou Yu, Jun Yu*  
  `2025-11-10` · `cs.CV` · [abs](https://arxiv.org/abs/2511.07122) · [pdf](https://arxiv.org/pdf/2511.07122.pdf)
  > 💡 针对稀疏帧动态场景重建中纹理丰富区域失效问题，提出纹理感知变形正则化和规范优化，实现高质量4D重建。

  <details><summary>Abstract</summary>

  Dynamic Gaussian Splatting approaches have achieved remarkable performance for 4D scene reconstruction. However, these approaches rely on dense-frame video sequences for photorealistic reconstruction. In real-world scenarios, due to equipment constraints, sometimes only sparse frames are accessible. In this paper, we propose Sparse4DGS, the first method for sparse-frame dynamic scene reconstruction. We observe that dynamic reconstruction methods fail in both canonical and deformed spaces under sparse-frame settings, especially in areas with high texture richness. Sparse4DGS tackles this challenge by focusing on texture-rich areas. For the deformation network, we propose Texture-Aware Deformation Regularization, which introduces a texture-based depth alignment loss to regulate Gaussian deformation. For the canonical Gaussian field, we introduce Texture-Aware Canonical Optimization, which incorporates texture-based noise into the gradient descent process of canonical Gaussians. Extensive experiments show that when taking sparse frames as inputs, our method outperforms existing dynamic or few-shot techniques on NeRF-Synthetic, HyperNeRF, NeRF-DS, and our iPhone-4D datasets.

  </details>

- **[DIAL-GS: Dynamic Instance Aware Reconstruction for Label-free Street Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2511.06632)**  
  *Chenpeng Su, Wenhua Wu, Chensheng Peng, Tianchen Deng, Zhe Liu, Hesheng Wang*  
  `2025-11-10` · `cs.CV` · [abs](https://arxiv.org/abs/2511.06632) · [pdf](https://arxiv.org/pdf/2511.06632.pdf)
  > 💡 利用外观位置不一致识别动态实例，结合实例感知4D高斯实现无标签街景重建与编辑。

  <details><summary>Abstract</summary>

  Urban scene reconstruction is critical for autonomous driving, enabling structured 3D representations for data synthesis and closed-loop testing. Supervised approaches rely on costly human annotations and lack scalability, while current self-supervised methods often confuse static and dynamic elements and fail to distinguish individual dynamic objects, limiting fine-grained editing. We propose DIAL-GS, a novel dynamic instance-aware reconstruction method for label-free street scenes with 4D Gaussian Splatting. We first accurately identify dynamic instances by exploiting appearance-position inconsistency between warped rendering and actual observation. Guided by instance-level dynamic perception, we employ instance-aware 4D Gaussians as the unified volumetric representation, realizing dynamic-adaptive and instance-aware reconstruction. Furthermore, we introduce a reciprocal mechanism through which identity and dynamics reinforce each other, enhancing both integrity and consistency. Experiments on urban driving scenarios show that DIAL-GS surpasses existing self-supervised baselines in reconstruction quality and instance-level editing, offering a concise yet powerful solution for urban scene modeling.

  </details>

- **[Detail Enhanced Gaussian Splatting for Large-Scale Volumetric Capture](https://arxiv.org/abs/2511.21697)**  
  *Julien Philip, Li Ma, Pascal Clausen, Wenqi Xian, Ahmet Levent Taşel, Mingming He, Xueming Yu, David M. George, Ning Yu, Oliver Pilarski, Paul Debevec*  
  `2025-10-31` · `cs.GR` · [abs](https://arxiv.org/abs/2511.21697) · [pdf](https://arxiv.org/pdf/2511.21697.pdf)
  > 💡 提出动态高斯泼溅与扩散细节增强的4D捕捉管遍，实现大规模场景到4K面部特写的高质量渲染。

  <details><summary>Abstract</summary>

  We present a unique system for large-scale, multi-performer, high resolution 4D volumetric capture providing realistic free-viewpoint video up to and including 4K resolution facial closeups. To achieve this, we employ a novel volumetric capture, reconstruction and rendering pipeline based on Dynamic Gaussian Splatting and Diffusion-based Detail Enhancement. We design our pipeline specifically to meet the demands of high-end media production. We employ two capture rigs: the Scene Rig, which captures multi-actor performances at a resolution which falls short of 4K production quality, and the Face Rig, which records high-fidelity single-actor facial detail to serve as a reference for detail enhancement. We first reconstruct dynamic performances from the Scene Rig using 4D Gaussian Splatting, incorporating new model designs and training strategies to improve reconstruction, dynamic range, and rendering quality. Then to render high-quality images for facial closeups, we introduce a diffusion-based detail enhancement model. This model is fine-tuned with high-fidelity data from the same actors recorded in the Face Rig. We train on paired data generated from low- and high-quality Gaussian Splatting (GS) models, using the low-quality input to match the quality of the Scene Rig, with the high-quality GS as ground truth. Our results demonstrate the effectiveness of this pipeline in bridging the gap between the scalable performance capture of a large-scale rig and the high-resolution standards required for film and media production.

  </details>

- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694)**  
  *Bernhard Kerbl*  
  `2025-10-30` · `cs.CV` · [abs](https://arxiv.org/abs/2510.26694) · [pdf](https://arxiv.org/pdf/2510.26694.pdf)
  > 💡 回顾3DGS在效率、动态化、数学基础及平台适配方面的进展，展现其成为3D视觉与图形基础工具的演变。

  <details><summary>Abstract</summary>

  Since its introduction, 3D Gaussian Splatting (3DGS) has rapidly transformed the landscape of 3D scene representations, inspiring an extensive body of associated research. Follow-up work includes analyses and contributions that enhance the efficiency, scalability, and real-world applicability of 3DGS. In this summary, we present an overview of several key directions that have emerged in the wake of 3DGS. We highlight advances enabling resource-efficient training and rendering, the evolution toward dynamic (or four-dimensional, 4DGS) representations, and deeper exploration of the mathematical foundations underlying its appearance modeling and rendering process. Furthermore, we examine efforts to bring 3DGS to mobile and virtual reality platforms, its extension to massive-scale environments, and recent progress toward near-instant radiance field reconstruction via feed-forward or distributed computation. Collectively, these developments illustrate how 3DGS has evolved from a breakthrough representation into a versatile and foundational tool for 3D vision and graphics.

  </details>

- **[EndoWave: Rational-Wavelet 4D Gaussian Splatting for Endoscopic Reconstruction](https://arxiv.org/abs/2510.23087)**  
  *Taoyu Wu, Yiyi Miao, Jiaxin Guo, Ziyan Chen, Sihang Zhao, Zhuoxiao Li, Zhe Tang, Baoru Huang, Limin Yu*  
  `2025-10-27` · `cs.CV` · [abs](https://arxiv.org/abs/2510.23087) · [pdf](https://arxiv.org/pdf/2510.23087.pdf)
  > 💡 针对内窥镜动态场景，提出4D高斯泼溅结合光流约束与有理小波监督，实现高质量时空重建。

  <details><summary>Abstract</summary>

  In robot-assisted minimally invasive surgery, accurate 3D reconstruction from endoscopic video is vital for downstream tasks and improved outcomes. However, endoscopic scenarios present unique challenges, including photometric inconsistencies, non-rigid tissue motion, and view-dependent highlights. Most 3DGS-based methods that rely solely on appearance constraints for optimizing 3DGS are often insufficient in this context, as these dynamic visual artifacts can mislead the optimization process and lead to inaccurate reconstructions. To address these limitations, we present EndoWave, a unified spatio-temporal Gaussian Splatting framework by incorporating an optical flow-based geometric constraint and a multi-resolution rational wavelet supervision. First, we adopt a unified spatio-temporal Gaussian representation that directly optimizes primitives in a 4D domain. Second, we propose a geometric constraint derived from optical flow to enhance temporal coherence and effectively constrain the 3D structure of the scene. Third, we propose a multi-resolution rational orthogonal wavelet as a constraint, which can effectively separate the details of the endoscope and enhance the rendering performance. Extensive evaluations on two real surgical datasets, EndoNeRF and StereoMIS, demonstrate that our method EndoWave achieves state-of-the-art reconstruction quality and visual accuracy compared to the baseline method.

  </details>

- **[DynaPose4D: High-Quality 4D Dynamic Content Generation via Pose Alignment Loss](https://arxiv.org/abs/2510.22473)**  
  *Jing Yang, Yufeng Yang*  
  `2025-10-26` · `cs.CV` · [abs](https://arxiv.org/abs/2510.22473) · [pdf](https://arxiv.org/pdf/2510.22473.pdf)
  > 💡 单图生成4D动态内容困难，融合4D高斯溅射与类别无关姿态估计，通过姿态对齐损失增强运动一致性与流畅性。

  <details><summary>Abstract</summary>

  Recent advancements in 2D and 3D generative models have expanded the capabilities of computer vision. However, generating high-quality 4D dynamic content from a single static image remains a significant challenge. Traditional methods have limitations in modeling temporal dependencies and accurately capturing dynamic geometry changes, especially when considering variations in camera perspective. To address this issue, we propose DynaPose4D, an innovative solution that integrates 4D Gaussian Splatting (4DGS) techniques with Category-Agnostic Pose Estimation (CAPE) technology. This framework uses 3D Gaussian Splatting to construct a 3D model from single images, then predicts multi-view pose keypoints based on one-shot support from a chosen view, leveraging supervisory signals to enhance motion consistency. Experimental results show that DynaPose4D achieves excellent coherence, consistency, and fluidity in dynamic motion generation. These findings not only validate the efficacy of the DynaPose4D framework but also indicate its potential applications in the domains of computer vision and animation production.

  </details>

- **[Virtually Being: Customizing Camera-Controllable Video Diffusion Models with Multi-View Performance Captures](https://arxiv.org/abs/2510.14179)**  
  *Yuancheng Xu, Wenqi Xian, Li Ma, Julien Philip, Ahmet Levent Taşel, Yiwei Zhao, Ryan Burgert, Mingming He, Oliver Hermann, Oliver Pilarski, Rahul Garg, Paul Debevec, Ning Yu*  
  `2025-10-16` · `cs.CV` · [abs](https://arxiv.org/abs/2510.14179) · [pdf](https://arxiv.org/pdf/2510.14179.pdf)
  > 💡 利用4DGS与重照明生成多视角数据，微调视频扩散模型实现角色一致与相机可控，提升虚拟制作视频质量。

  <details><summary>Abstract</summary>

  We introduce a framework that enables both multi-view character consistency and 3D camera control in video diffusion models through a novel customization data pipeline. We train the character consistency component with recorded volumetric capture performances re-rendered with diverse camera trajectories via 4D Gaussian Splatting (4DGS), lighting variability obtained with a video relighting model. We fine-tune state-of-the-art open-source video diffusion models on this data to provide strong multi-view identity preservation, precise camera control, and lighting adaptability. Our framework also supports core capabilities for virtual production, including multi-subject generation using two approaches: joint training and noise blending, the latter enabling efficient composition of independently customized models at inference time; it also achieves scene and real-life video customization as well as control over motion and spatial layout during customization. Extensive experiments show improved video quality, higher personalization accuracy, and enhanced camera control and lighting adaptability, advancing the integration of video generation into virtual production. Our project page is available at: https://eyeline-labs.github.io/Virtually-Being.

  </details>

- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030)**  
  *Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen*  
  `2025-10-11` · `cs.CV` · [abs](https://arxiv.org/abs/2510.10030) · [pdf](https://arxiv.org/pdf/2510.10030.pdf)
  > 💡 利用帧间预测与自适应量化熵编码压缩动态3DGS时空冗余，实现90倍压缩且保持高质量与高速渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has garnered significant attention due to its superior scene representation fidelity and real-time rendering performance, especially for dynamic 3D scene reconstruction (\textit{i.e.}, 4D reconstruction). However, despite achieving promising results, most existing algorithms overlook the substantial temporal and spatial redundancies inherent in dynamic scenes, leading to prohibitive memory consumption. To address this, we propose P-4DGS, a novel dynamic 3DGS representation for compact 4D scene modeling. Inspired by intra- and inter-frame prediction techniques commonly used in video compression, we first design a 3D anchor point-based spatial-temporal prediction module to fully exploit the spatial-temporal correlations across different 3D Gaussian primitives. Subsequently, we employ an adaptive quantization strategy combined with context-based entropy coding to further reduce the size of the 3D anchor points, thereby achieving enhanced compression efficiency. To evaluate the rate-distortion performance of our proposed P-4DGS in comparison with other dynamic 3DGS representations, we conduct extensive experiments on both synthetic and real-world datasets. Experimental results demonstrate that our approach achieves state-of-the-art reconstruction quality and the fastest rendering speed, with a remarkably low storage footprint (around \textbf{1MB} on average), achieving up to \textbf{40$\times$} and \textbf{90$\times$} compression on synthetic and real-world scenes, respectively.

  </details>

- **[SIMSplat: Predictive Driving Scene Editing with Language-aligned 4D Gaussian Splatting](https://arxiv.org/abs/2510.02469)**  
  *Sung-Yeon Park, Adam Lee, Juanwu Lu, Can Cui, Luyang Jiang, Rohit Gupta, Kyungtae Han, Ahmadreza Moradipari, Ziran Wang*  
  `2025-10-02` · `cs.RO` · [abs](https://arxiv.org/abs/2510.02469) · [pdf](https://arxiv.org/pdf/2510.02469.pdf)
  > 💡 语言对齐4D高斯泼溅实现自然语言驱动的驾驶场景编辑，支持物体级添加与轨迹修改，并通过运动预测细化路径。

  <details><summary>Abstract</summary>

  Driving scene manipulation with sensor data is emerging as a promising alternative to traditional virtual driving simulators. However, existing frameworks struggle to generate realistic scenarios efficiently due to limited editing capabilities. To address these challenges, we present SIMSplat, a predictive driving scene editor with language-aligned Gaussian splatting. As a language-controlled editor, SIMSplat enables intuitive manipulation using natural language prompts. By aligning language with Gaussian-reconstructed scenes, it further supports direct querying of road objects, allowing precise and flexible editing. Our method provides detailed object-level editing, including adding new objects and modifying the trajectories of both vehicles and pedestrians, while also incorporating predictive path refinement through multi-agent motion prediction to generate realistic interactions among all agents in the scene. Experiments on the Waymo dataset demonstrate SIMSplat's extensive editing capabilities and adaptability across a wide range of scenarios. Project page: https://sungyeonparkk.github.io/simsplat/

  </details>

- **[4DGS-Craft: Consistent and Interactive 4D Gaussian Splatting Editing](https://arxiv.org/abs/2510.01991)**  
  *Lei Liu, Can Wang, Zhenghao Chen, Dong Xu*  
  `2025-10-02` · `cs.CV` · [abs](https://arxiv.org/abs/2510.01991) · [pdf](https://arxiv.org/pdf/2510.01991.pdf)
  > 💡 针对4DGS编辑中一致性与交互性不足，提出4D感知模型与LLM模块，实现可控

  <details><summary>Abstract</summary>

  Recent advances in 4D Gaussian Splatting (4DGS) editing still face challenges with view, temporal, and non-editing region consistency, as well as with handling complex text instructions. To address these issues, we propose 4DGS-Craft, a consistent and interactive 4DGS editing framework. We first introduce a 4D-aware InstructPix2Pix model to ensure both view and temporal consistency. This model incorporates 4D VGGT geometry features extracted from the initial scene, enabling it to capture underlying 4D geometric structures during editing. We further enhance this model with a multi-view grid module that enforces consistency by iteratively refining multi-view input images while jointly optimizing the underlying 4D scene. Furthermore, we preserve the consistency of non-edited regions through a novel Gaussian selection mechanism, which identifies and optimizes only the Gaussians within the edited regions. Beyond consistency, facilitating user interaction is also crucial for effective 4DGS editing. Therefore, we design an LLM-based module for user intent understanding. This module employs a user instruction template to define atomic editing operations and leverages an LLM for reasoning. As a result, our framework can interpret user intent and decompose complex instructions into a logical sequence of atomic operations, enabling it to handle intricate user commands and further enhance editing performance. Compared to related works, our approach enables more consistent and controllable 4D scene editing. Our code will be made available upon acceptance.

  </details>

- **[Instant4D: 4D Gaussian Splatting in Minutes](https://arxiv.org/abs/2510.01119)**  
  *Zhanpeng Luo, Haoxi Ran, Li Lu*  
  `2025-10-01` · `cs.CV` · [abs](https://arxiv.org/abs/2510.01119) · [pdf](https://arxiv.org/pdf/2510.01119.pdf)
  > 💡 针对非标定视频动态重建，提出Instant4D，结合视觉SLAM与网格剪枝的4D高斯表示，实现分钟级高效重建。

  <details><summary>Abstract</summary>

  Dynamic view synthesis has seen significant advances, yet reconstructing scenes from uncalibrated, casual video remains challenging due to slow optimization and complex parameter estimation. In this work, we present Instant4D, a monocular reconstruction system that leverages native 4D representation to efficiently process casual video sequences within minutes, without calibrated cameras or depth sensors. Our method begins with geometric recovery through deep visual SLAM, followed by grid pruning to optimize scene representation. Our design significantly reduces redundancy while maintaining geometric integrity, cutting model size to under 10% of its original footprint. To handle temporal dynamics efficiently, we introduce a streamlined 4D Gaussian representation, achieving a 30x speed-up and reducing training time to within two minutes, while maintaining competitive performance across several benchmarks. Our method reconstruct a single video within 10 minutes on the Dycheck dataset or for a typical 200-frame video. We further apply our model to in-the-wild videos, showcasing its generalizability. Our project website is published at https://instant4d.github.io/.

  </details>

- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853)**  
  *Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu*  
  `2025-09-26` · `cs.CV` · [abs](https://arxiv.org/abs/2509.21853) · [pdf](https://arxiv.org/pdf/2509.21853.pdf)
  > 💡 针对动态高动态范围新视角合成难题，提出HDR-4DGS，通过动态色调映射实现时空一致的逼真渲染。

  <details><summary>Abstract</summary>

  High Dynamic Range Novel View Synthesis (HDR NVS) seeks to learn an HDR 3D model from Low Dynamic Range (LDR) training images captured under conventional imaging conditions. Current methods primarily focus on static scenes, implicitly assuming all scene elements remain stationary and non-living. However, real-world scenarios frequently feature dynamic elements, such as moving objects, varying lighting conditions, and other temporal events, thereby presenting a significantly more challenging scenario. To address this gap, we propose a more realistic problem named HDR Dynamic Novel View Synthesis (HDR DNVS), where the additional dimension ``Dynamic'' emphasizes the necessity of jointly modeling temporal radiance variations alongside sophisticated 3D translation between LDR and HDR. To tackle this complex, intertwined challenge, we introduce HDR-4DGS, a Gaussian Splatting-based architecture featured with an innovative dynamic tone-mapping module that explicitly connects HDR and LDR domains, maintaining temporal radiance coherence by dynamically adapting tone-mapping functions according to the evolving radiance distributions across the temporal dimension. As a result, HDR-4DGS achieves both temporal radiance consistency and spatially accurate color translation, enabling photorealistic HDR renderings from arbitrary viewpoints and time instances. Extensive experiments demonstrate that HDR-4DGS surpasses existing state-of-the-art methods in both quantitative performance and visual fidelity. Source code is available at https://github.com/prinasi/HDR-4DGS.

  </details>

- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251)**  
  *Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen*  
  `2025-09-24` · `cs.CV` · [abs](https://arxiv.org/abs/2509.20251) · [pdf](https://arxiv.org/pdf/2509.20251.pdf)
  > 💡 提出PhiGenesis框架，结合视频VAE与Stereo Forcing条件策略，实现无需逐场景优化的4D驾驶场景生成，在几何与时间一致性上达到SOTA。

  <details><summary>Abstract</summary>

  Current generative models struggle to synthesize dynamic 4D driving scenes that simultaneously support temporal extrapolation and spatial novel view synthesis (NVS) without per-scene optimization. Bridging generation and novel view synthesis remains a major challenge. We present PhiGenesis, a unified framework for 4D scene generation that extends video generation techniques with geometric and temporal consistency. Given multi-view image sequences and camera parameters, PhiGenesis produces temporally continuous 4D Gaussian splatting representations along target 3D trajectories. In its first stage, PhiGenesis leverages a pre-trained video VAE with a novel range-view adapter to enable feed-forward 4D reconstruction from multi-view images. This architecture supports single-frame or video inputs and outputs complete 4D scenes including geometry, semantics, and motion. In the second stage, PhiGenesis introduces a geometric-guided video diffusion model, using rendered historical 4D scenes as priors to generate future views conditioned on trajectories. To address geometric exposure bias in novel views, we propose Stereo Forcing, a novel conditioning strategy that integrates geometric uncertainty during denoising. This method enhances temporal coherence by dynamically adjusting generative influence based on uncertainty-aware perturbations. Our experimental results demonstrate that our method achieves state-of-the-art performance in both appearance and geometric reconstruction, temporal generation and novel view synthesis (NVS) tasks, while simultaneously delivering competitive performance in downstream evaluations. Homepage is at \href{https://jiangxb98.github.io/PhiGensis}{PhiGensis}.

  </details>

- **[4DGCPro: Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming](https://arxiv.org/abs/2509.17513)**  
  *Zihan Zheng, Zhenlong Wu, Houqiang Zhong, Yuan Tian, Ning Cao, Lan Xu, Jiangchao Yao, Xiaoyun Zhang, Qiang Hu, Wenjun Zhang*  
  `2025-09-22` · `cs.CV` · [abs](https://arxiv.org/abs/2509.17513) · [pdf](https://arxiv.org/pdf/2509.17513.pdf)
  > 💡 针对现有体积视频压缩缺乏灵活性和实时移动端渲染问题，提出层次化4D高斯压缩框架，实现单模型内可伸缩多码率与实时移动端解码。

  <details><summary>Abstract</summary>

  Achieving seamless viewing of high-fidelity volumetric video, comparable to 2D video experiences, remains an open challenge. Existing volumetric video compression methods either lack the flexibility to adjust quality and bitrate within a single model for efficient streaming across diverse networks and devices, or struggle with real-time decoding and rendering on lightweight mobile platforms. To address these challenges, we introduce 4DGCPro, a novel hierarchical 4D Gaussian compression framework that facilitates real-time mobile decoding and high-quality rendering via progressive volumetric video streaming in a single bitstream. Specifically, we propose a perceptually-weighted and compression-friendly hierarchical 4D Gaussian representation with motion-aware adaptive grouping to reduce temporal redundancy, preserve coherence, and enable scalable multi-level detail streaming. Furthermore, we present an end-to-end entropy-optimized training scheme, which incorporates layer-wise rate-distortion (RD) supervision and attribute-specific entropy modeling for efficient bitstream generation. Extensive experiments show that 4DGCPro enables flexible quality and multiple bitrate within a single model, achieving real-time decoding and rendering on mobile devices while outperforming existing methods in RD performance across multiple datasets. Project Page: https://mediax-sjtu.github.io/4DGCPro

  </details>

- **[4D-MoDe: Towards Editable and Scalable Volumetric Streaming via Motion-Decoupled 4D Gaussian Compression](https://arxiv.org/abs/2509.17506)**  
  *Houqiang Zhong, Zihan Zheng, Qiang Hu, Yuan Tian, Ning Cao, Lan Xu, Xiaoyun Zhang, Zhengxue Cheng, Li Song, Wenjun Zhang*  
  `2025-09-22` · `cs.CV` · [abs](https://arxiv.org/abs/2509.17506) · [pdf](https://arxiv.org/pdf/2509.17506.pdf)
  > 💡 提出

  <details><summary>Abstract</summary>

  Volumetric video has emerged as a key medium for immersive telepresence and augmented/virtual reality, enabling six-degrees-of-freedom (6DoF) navigation and realistic spatial interactions. However, delivering high-quality dynamic volumetric content at scale remains challenging due to massive data volume, complex motion, and limited editability of existing representations. In this paper, we present 4D-MoDe, a motion-decoupled 4D Gaussian compression framework designed for scalable and editable volumetric video streaming. Our method introduces a layered representation that explicitly separates static backgrounds from dynamic foregrounds using a lookahead-based motion decomposition strategy, significantly reducing temporal redundancy and enabling selective background/foreground streaming. To capture continuous motion trajectories, we employ a multi-resolution motion estimation grid and a lightweight shared MLP, complemented by a dynamic Gaussian compensation mechanism to model emergent content. An adaptive grouping scheme dynamically inserts background keyframes to balance temporal consistency and compression efficiency. Furthermore, an entropy-aware training pipeline jointly optimizes the motion fields and Gaussian parameters under a rate-distortion (RD) objective, while employing range-based and KD-tree compression to minimize storage overhead. Extensive experiments on multiple datasets demonstrate that 4D-MoDe consistently achieves competitive reconstruction quality with an order of magnitude lower storage cost (e.g., as low as \textbf{11.4} KB/frame) compared to state-of-the-art methods, while supporting practical applications such as background replacement and foreground-only streaming.

  </details>

- **[E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event Cameras](https://arxiv.org/abs/2508.09912)**  
  *Chaoran Feng, Zhenyu Tang, Wangbo Yu, Yatian Pang, Yian Zhao, Jianbin Zhao, Li Yuan, Yonghong Tian*  
  `2025-08-13` · `cs.CV` · [abs](https://arxiv.org/abs/2508.09912) · [pdf](https://arxiv.org/pdf/2508.09912.pdf)
  > 💡 针对RGB相机在高速场景中的局限，利用多视角事件相机结合4D Gaussian Splatting实现高保真动态重建。

  <details><summary>Abstract</summary>

  Novel view synthesis and 4D reconstruction techniques predominantly rely on RGB cameras, thereby inheriting inherent limitations such as the dependence on adequate lighting, susceptibility to motion blur, and a limited dynamic range. Event cameras, offering advantages of low power, high temporal resolution and high dynamic range, have brought a new perspective to addressing the scene reconstruction challenges in high-speed motion and

  </details>

- **[S^2VG: 3D Stereoscopic and Spatial Video Generation via Denoising Frame Matrix](https://arxiv.org/abs/2508.08048)**  
  *Peng Dai, Feitong Tan, Qiangeng Xu, Yihua Huang, David Futschik, Ruofei Du, Sean Fanello, Yinda Zhang, Xiaojuan Qi*  
  `2025-08-11` · `cs.CV` · [abs](https://arxiv.org/abs/2508.08048) · [pdf](https://arxiv.org/pdf/2508.08048.pdf)
  > 💡 提出无姿态无训练方法，利用单目视频模型结合帧矩阵修复和双重更新生成3D立体和空间视频，无需微调。

  <details><summary>Abstract</summary>

  While video generation models excel at producing high-quality monocular videos, generating 3D stereoscopic and spatial videos for immersive applications remains an underexplored challenge. We present a pose-free and training-free method that leverages an off-the-shelf monocular video generation model to produce immersive 3D videos. Our approach first warps the generated monocular video into pre-defined camera viewpoints using estimated depth information, then applies a novel \textit{frame matrix} inpainting framework. This framework utilizes the original video generation model to synthesize missing content across different viewpoints and timestamps, ensuring spatial and temporal consistency without requiring additional model fine-tuning. Moreover, we develop a \dualupdate~scheme that further improves the quality of video inpainting by alleviating the negative effects propagated from disoccluded areas in the latent space. The resulting multi-view videos are then adapted into stereoscopic pairs or optimized into 4D Gaussians for spatial video synthesis. We validate the efficacy of our proposed method by conducting experiments on videos from various generative models, such as Sora, Lumiere, WALT, and Zeroscope. The experiments demonstrate that our method has a significant improvement over previous methods. Project page at: https://daipengwa.github.io/S-2VG_ProjectPage/

  </details>

- **[Splat4D: Diffusion-Enhanced 4D Gaussian Splatting for Temporally and Spatially Consistent Content Creation](https://arxiv.org/abs/2508.07557)**  
  *Minghao Yin, Yukang Cao, Songyou Peng, Kai Han*  
  `2025-08-11` · `cs.CV` · [abs](https://arxiv.org/abs/2508.07557) · [pdf](https://arxiv.org/pdf/2508.07557.pdf)
  > 💡 使用多视图渲染、不一致识别、视频扩散模型和非对称U-Net，Splat4D实现高质量时空一致的4D内容生成。

  <details><summary>Abstract</summary>

  Generating high-quality 4D content from monocular videos for applications such as digital humans and AR/VR poses challenges in ensuring temporal and spatial consistency, preserving intricate details, and incorporating user guidance effectively. To overcome these challenges, we introduce Splat4D, a novel framework enabling high-fidelity 4D content generation from a monocular video. Splat4D achieves superior performance while maintaining faithful spatial-temporal coherence by leveraging multi-view rendering, inconsistency identification, a video diffusion model, and an asymmetric U-Net for refinement. Through extensive evaluations on public benchmarks, Splat4D consistently demonstrates state-of-the-art performance across various metrics, underscoring the efficacy of our approach. Additionally, the versatility of Splat4D is validated in various applications such as text/image conditioned 4D generation, 4D human generation, and text-guided content editing, producing coherent outcomes following user instructions.

  </details>

- **[VDEGaussian: Video Diffusion Enhanced 4D Gaussian Splatting for Dynamic Urban Scenes Modeling](https://arxiv.org/abs/2508.02129)**  
  *Yuru Xiao, Zihan Lin, Chao Lu, Deming Zhai, Kui Jiang, Wenbo Zhao, Wei Zhang, Junjun Jiang, Huanran Wang, Xianming Liu*  
  `2025-08-04` · `cs.CV` · [abs](https://arxiv.org/abs/2508.02129) · [pdf](https://arxiv.org/pdf/2508.02129.pdf)
  > 💡 利用视频扩散模型蒸馏时间一致先验，结合联合时间戳优化与不确定性蒸馏，提升动态城市场景中快速运动物体的建模，PSNR提升约2dB。

  <details><summary>Abstract</summary>

  Dynamic urban scene modeling is a rapidly evolving area with broad applications. While current approaches leveraging neural radiance fields or Gaussian Splatting have achieved fine-grained reconstruction and high-fidelity novel view synthesis, they still face significant limitations. These often stem from a dependence on pre-calibrated object tracks or difficulties in accurately modeling fast-moving objects from undersampled capture, particularly due to challenges in handling temporal discontinuities. To overcome these issues, we propose a novel video diffusion-enhanced 4D Gaussian Splatting framework. Our key insight is to distill robust, temporally consistent priors from a test-time adapted video diffusion model. To ensure precise pose alignment and effective integration of this denoised content, we introduce two core innovations: a joint timestamp optimization strategy that refines interpolated frame poses, and an uncertainty distillation method that adaptively extracts target content while preserving well-reconstructed regions. Extensive experiments demonstrate that our method significantly enhances dynamic modeling, especially for fast-moving objects, achieving an approximate PSNR gain of 2 dB for novel view synthesis over baseline approaches.

  </details>

- **[MVG4D: Image Matrix-Based Multi-View and Motion Generation for 4D Content Creation from a Single Image](https://arxiv.org/abs/2507.18371)**  
  *DongFu Yin, Xiaotian Chen, Fei Richard Yu, Xuanchen Li, Xinhao Zhang*  
  `2025-07-24` · `cs.CV` · [abs](https://arxiv.org/abs/2507.18371) · [pdf](https://arxiv.org/pdf/2507.18371.pdf)
  > 💡 提出MVG4D框架，用图像矩阵合成时空一致多视角图像，结合4D高斯泼溅和变形网络，从单图生成高保真动态4D内容。

  <details><summary>Abstract</summary>

  Advances in generative modeling have significantly enhanced digital content creation, extending from 2D images to complex 3D and 4D scenes. Despite substantial progress, producing high-fidelity and temporally consistent dynamic 4D content remains a challenge. In this paper, we propose MVG4D, a novel framework that generates dynamic 4D content from a single still image by combining multi-view synthesis with 4D Gaussian Splatting (4D GS). At its core, MVG4D employs an image matrix module that synthesizes temporally coherent and spatially diverse multi-view images, providing rich supervisory signals for downstream 3D and 4D reconstruction. These multi-view images are used to optimize a 3D Gaussian point cloud, which is further extended into the temporal domain via a lightweight deformation network. Our method effectively enhances temporal consistency, geometric fidelity, and visual realism, addressing key challenges in motion discontinuity and background degradation that affect prior 4D GS-based methods. Extensive experiments on the Objaverse dataset demonstrate that MVG4D outperforms state-of-the-art baselines in CLIP-I, PSNR, FVD, and time efficiency. Notably, it reduces flickering artifacts and sharpens structural details across views and time, enabling more immersive AR/VR experiences. MVG4D sets a new direction for efficient and controllable 4D generation from minimal inputs.

  </details>

- **[Temporal Smoothness-Aware Rate-Distortion Optimized 4D Gaussian Splatting](https://arxiv.org/abs/2507.17336)**  
  *Hyeongmin Lee, Kyungjune Baek*  
  `2025-07-23` · `cs.GR` · [abs](https://arxiv.org/abs/2507.17336) · [pdf](https://arxiv.org/pdf/2507.17336.pdf)
  > 💡 针对4DGS存储庞大问题，提出端到端率失真优化压缩框架，利用小波变换及时序平滑先验，实现91倍压缩且保持高保真。

  <details><summary>Abstract</summary>

  Dynamic 4D Gaussian Splatting (4DGS) effectively extends the high-speed rendering capabilities of 3D Gaussian Splatting (3DGS) to represent volumetric videos. However, the large number of Gaussians, substantial temporal redundancies, and especially the absence of an entropy-aware compression framework result in large storage requirements. Consequently, this poses significant challenges for practical deployment, efficient edge-device processing, and data transmission. In this paper, we introduce a novel end-to-end RD-optimized compression framework tailored for 4DGS, aiming to enable flexible, high-fidelity rendering across varied computational platforms. Leveraging Fully Explicit Dynamic Gaussian Splatting (Ex4DGS), one of the state-of-the-art 4DGS methods, as our baseline, we start from the existing 3DGS compression methods for compatibility while effectively addressing additional challenges introduced by the temporal axis. In particular, instead of storing motion trajectories independently per point, we employ a wavelet transform to reflect the real-world smoothness prior, significantly enhancing storage efficiency. This approach yields significantly improved compression ratios and provides a user-controlled balance between compression efficiency and rendering quality. Extensive experiments demonstrate the effectiveness of our method, achieving up to 91$\times$ compression compared to the original Ex4DGS model while maintaining high visual fidelity. These results highlight the applicability of our framework for real-time dynamic scene rendering in diverse scenarios, from resource-constrained edge devices to high-performance environments. The source code is available at https://github.com/HyeongminLEE/RD4DGS.

  </details>

- **[SD-GS: Structured Deformable 3D Gaussians for Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2507.07465)**  
  *Wei Yao, Shuzhao Xie, Letian Li, Weixiang Zhang, Zhixin Lai, Shiqi Dai, Ke Zhang, Zhi Wang*  
  `2025-07-10` · `cs.GR` · [abs](https://arxiv.org/abs/2507.07465) · [pdf](https://arxiv.org/pdf/2507.07465.pdf)
  > 💡 提出可变形锚点网格与变形感知密集化策略，实现动态场景重建模型大小减少60%、速度提升100%且质量不减。

  <details><summary>Abstract</summary>

  Current 4D Gaussian frameworks for dynamic scene reconstruction deliver impressive visual fidelity and rendering speed, however, the inherent trade-off between storage costs and the ability to characterize complex physical motions significantly limits the practical application of these methods. To tackle these problems, we propose SD-GS, a compact and efficient dynamic Gaussian splatting framework for complex dynamic scene reconstruction, featuring two key contributions. First, we introduce a deformable anchor grid, a hierarchical and memory-efficient scene representation where each anchor point derives multiple 3D Gaussians in its local spatiotemporal region and serves as the geometric backbone of the 3D scene. Second, to enhance modeling capability for complex motions, we present a deformation-aware densification strategy that adaptively grows anchors in under-reconstructed high-dynamic regions while reducing redundancy in static areas, achieving superior visual quality with fewer anchors. Experimental results demonstrate that, compared to state-of-the-art methods, SD-GS achieves an average of 60\% reduction in model size and an average of 100\% improvement in FPS, significantly enhancing computational efficiency while maintaining or even surpassing visual quality.

  </details>

- **[Endo-4DGX: Robust Endoscopic Scene Reconstruction and Illumination Correction with Gaussian Splatting](https://arxiv.org/abs/2506.23308)**  
  *Yiming Huang, Long Bai, Beilei Cui, Yanheng Li, Tong Chen, Jie Wang, Jinlin Wu, Zhen Lei, Hongbin Liu, Hongliang Ren*  
  `2025-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2506.23308) · [pdf](https://arxiv.org/pdf/2506.23308.pdf)
  > 💡 针对内窥镜场景光照不均问题，提出光照自适应高斯泼溅，通过嵌入与模块建模亮度变化，实现鲁棒重建与校正。

  <details><summary>Abstract</summary>

  Accurate reconstruction of soft tissue is crucial for advancing automation in image-guided robotic surgery. The recent 3D Gaussian Splatting (3DGS) techniques and their variants, 4DGS, achieve high-quality renderings of dynamic surgical scenes in real-time. However, 3D-GS-based methods still struggle in scenarios with varying illumination, such as low light and over-exposure. Training 3D-GS in such extreme light conditions leads to severe optimization problems and devastating rendering quality. To address these challenges, we present Endo-4DGX, a novel reconstruction method with illumination-adaptive Gaussian Splatting designed specifically for endoscopic scenes with uneven lighting. By incorporating illumination embeddings, our method effectively models view-dependent brightness variations. We introduce a region-aware enhancement module to model the sub-area lightness at the Gaussian level and a spatial-aware adjustment module to learn the view-consistent brightness adjustment. With the illumination adaptive design, Endo-4DGX achieves superior rendering performance under both low-light and over-exposure conditions while maintaining geometric accuracy. Additionally, we employ an exposure control loss to restore the appearance from adverse exposure to the normal level for illumination-adaptive optimization. Experimental results demonstrate that Endo-4DGX significantly outperforms combinations of state-of-the-art reconstruction and restoration methods in challenging lighting environments, underscoring its potential to advance robot-assisted surgical applications. Our code is available at https://github.com/lastbasket/Endo-4DGX.

  </details>

- **[DIGS: Dynamic CBCT Reconstruction using Deformation-Informed 4D Gaussian Splatting and a Low-Rank Free-Form Deformation Model](https://arxiv.org/abs/2506.22280)**  
  *Yuliang Huang, Imraj Singh, Thomas Joyce, Kris Thielemans, Jamie R. McClelland*  
  `2025-06-27` · `eess.IV` · [abs](https://arxiv.org/abs/2506.22280) · [pdf](https://arxiv.org/pdf/2506.22280.pdf)
  > 💡 用变形引导的4D高斯散点结合低秩自由变形模型，实现高效动态CBCT重建，抑制呼吸运动伪影且速度比HexPlane快6倍。

  <details><summary>Abstract</summary>

  3D Cone-Beam CT (CBCT) is widely used in radiotherapy but suffers from motion artifacts due to breathing. A common clinical approach mitigates this by sorting projections into respiratory phases and reconstructing images per phase, but this does not account for breathing variability. Dynamic CBCT instead reconstructs images at each projection, capturing continuous motion without phase sorting. Recent advancements in 4D Gaussian Splatting (4DGS) offer powerful tools for modeling dynamic scenes, yet their application to dynamic CBCT remains underexplored. Existing 4DGS methods, such as HexPlane, use implicit motion representations, which are computationally expensive. While explicit low-rank motion models have been proposed, they lack spatial regularization, leading to inconsistencies in Gaussian motion. To address these limitations, we introduce a free-form deformation (FFD)-based spatial basis function and a deformation-informed framework that enforces consistency by coupling the temporal evolution of Gaussian's mean position, scale, and rotation under a unified deformation field. We evaluate our approach on six CBCT datasets, demonstrating superior image quality with a 6x speedup over HexPlane. These results highlight the potential of deformation-informed 4DGS for efficient, motion-compensated CBCT reconstruction. The code is available at https://github.com/Yuliang-Huang/DIGS.

  </details>

- **[HoliGS: Holistic Gaussian Splatting for Embodied View Synthesis](https://arxiv.org/abs/2506.19291)**  
  *Xiaoyuan Wang, Yizhou Zhao, Botao Ye, Xiaojun Shan, Weijie Lyu, Lu Qi, Kelvin C. K. Chan, Yinxiao Li, Ming-Hsuan Yang*  
  `2025-06-24` · `cs.CV` · [abs](https://arxiv.org/abs/2506.19291) · [pdf](https://arxiv.org/pdf/2506.19291.pdf)
  > 💡 针对长单目视频具身视图合成，提出可逆高斯泼溅形变网络分层分解静态背景与动态物体，实现高效高质量重建。

  <details><summary>Abstract</summary>

  We propose HoliGS, a novel deformable Gaussian splatting framework that addresses embodied view synthesis from long monocular RGB videos. Unlike prior 4D Gaussian splatting and dynamic NeRF pipelines, which struggle with training overhead in minute-long captures, our method leverages invertible Gaussian Splatting deformation networks to reconstruct large-scale, dynamic environments accurately. Specifically, we decompose each scene into a static background plus time-varying objects, each represented by learned Gaussian primitives undergoing global rigid transformations, skeleton-driven articulation, and subtle non-rigid deformations via an invertible neural flow. This hierarchical warping strategy enables robust free-viewpoint novel-view rendering from various embodied camera trajectories by attaching Gaussians to a complete canonical foreground shape (\eg, egocentric or third-person follow), which may involve substantial viewpoint changes and interactions between multiple actors. Our experiments demonstrate that \ourmethod~ achieves superior reconstruction quality on challenging datasets while significantly reducing both training and rendering time compared to state-of-the-art monocular deformable NeRFs. These results highlight a practical and scalable solution for EVS in real-world scenarios. The source code will be released.

  </details>

- **[4D-LRM: Large Space-Time Reconstruction Model From and To Any View at Any Time](https://arxiv.org/abs/2506.18890)**  
  *Ziqiao Ma, Xuweiyi Chen, Shoubin Yu, Sai Bi, Kai Zhang, Chen Ziwen, Sihan Xu, Jianing Yang, Zexiang Xu, Kalyan Sunkavalli, Mohit Bansal, Joyce Chai, Hao Tan*  
  `2025-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2506.18890) · [pdf](https://arxiv.org/pdf/2506.18890.pdf)
  > 💡 从任意视角和时间输入重建任意视角时间，提出4D-LRM用4D高斯原语统一时空表示，实现高效高质量渲染。

  <details><summary>Abstract</summary>

  Can we scale 4D pretraining to learn general space-time representations that reconstruct an object from a few views at some times to any view at any time? We provide an affirmative answer with 4D-LRM, the first large-scale 4D reconstruction model that takes input from unconstrained views and timestamps and renders arbitrary novel view-time combinations. Unlike prior 4D approaches, e.g., optimization-based, geometry-based, or generative, that struggle with efficiency, generalization, or faithfulness, 4D-LRM learns a unified space-time representation and directly predicts per-pixel 4D Gaussian primitives from posed image tokens across time, enabling fast, high-quality rendering at, in principle, infinite frame rate. Our results demonstrate that scaling spatiotemporal pretraining enables accurate and efficient 4D reconstruction. We show that 4D-LRM generalizes to novel objects, interpolates across time, and handles diverse camera setups. It reconstructs 24-frame sequences in one forward pass with less than 1.5 seconds on a single A100 GPU.

  </details>

- **[BulletGen: Improving 4D Reconstruction with Bullet-Time Generation](https://arxiv.org/abs/2506.18601)**  
  *Denis Rozumny, Jonathon Luiten, Numair Khan, Johannes Schönberger, Peter Kontschieder*  
  `2025-06-23` · `cs.GR` · [abs](https://arxiv.org/abs/2506.18601) · [pdf](https://arxiv.org/pdf/2506.18601.pdf)
  > 💡 利用扩散模型对齐子弹时间步骤监督4D高斯优化，修复单目视频动态重建中的缺失与错误，在新视图合成和跟踪任务上取得最优。

  <details><summary>Abstract</summary>

  Transforming casually captured, monocular videos into fully immersive dynamic experiences is a highly ill-posed task, and comes with significant challenges, e.g., reconstructing unseen regions, and dealing with the ambiguity in monocular depth estimation. In this work we introduce BulletGen, an approach that takes advantage of generative models to correct errors and complete missing information in a Gaussian-based dynamic scene representation. This is done by aligning the output of a diffusion-based video generation model with the 4D reconstruction at a single frozen "bullet-time" step. The generated frames are then used to supervise the optimization of the 4D Gaussian model. Our method seamlessly blends generative content with both static and dynamic scene components, achieving state-of-the-art results on both novel-view synthesis, and 2D/3D tracking tasks.

  </details>

- **[4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos](https://arxiv.org/abs/2506.08015)**  
  *Zhen Xu, Zhengqin Li, Zhao Dong, Xiaowei Zhou, Richard Newcombe, Zhaoyang Lv*  
  `2025-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2506.08015) · [pdf](https://arxiv.org/pdf/2506.08015.pdf)
  > 💡 使用4D高斯作为归纳偏置的Transformer模型，通过密度控制和滚动窗口处理，将动态场景重建从小时级缩短至秒级，性能优于现有方法。

  <details><summary>Abstract</summary>

  We propose 4DGT, a 4D Gaussian-based Transformer model for dynamic scene reconstruction, trained entirely on real-world monocular posed videos. Using 4D Gaussian as an inductive bias, 4DGT unifies static and dynamic components, enabling the modeling of complex, time-varying environments with varying object lifespans. We proposed a novel density control strategy in training, which enables our 4DGT to handle longer space-time input and remain efficient rendering at runtime. Our model processes 64 consecutive posed frames in a rolling-window fashion, predicting consistent 4D Gaussians in the scene. Unlike optimization-based methods, 4DGT performs purely feed-forward inference, reducing reconstruction time from hours to seconds and scaling effectively to long video sequences. Trained only on large-scale monocular posed video datasets, 4DGT can outperform prior Gaussian-based networks significantly in real-world videos and achieve on-par accuracy with optimization-based methods on cross-domain videos. Project page: https://4dgt.github.io

  </details>

- **[WeatherEdit: Controllable Weather Editing with 4D Gaussian Field](https://arxiv.org/abs/2505.20471)**  
  *Chenghao Qian, Wenjing Li, Yuhu Guo, Gustav Markkula*  
  `2025-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2505.20471) · [pdf](https://arxiv.org/pdf/2505.20471.pdf)
  > 💡 提出WeatherEdit，结合全适配器与4D高斯场，实现3D场景中可控类型和强度的逼真天气编辑，用于自动驾驶模拟。

  <details><summary>Abstract</summary>

  In this work, we present WeatherEdit, a novel weather editing pipeline for generating realistic weather effects with controllable types and severity in 3D scenes. Our approach is structured into two key components: weather background editing and weather particle construction. For weather background editing, we introduce an all-in-one adapter that integrates multiple weather styles into a single pretrained diffusion model, enabling the generation of diverse weather effects in 2D image backgrounds. During inference, we design a Temporal-View (TV-) attention mechanism that follows a specific order to aggregate temporal and spatial information, ensuring consistent editing across multi-frame and multi-view images. To construct the weather particles, we first reconstruct a 3D scene using the edited images and then introduce a dynamic 4D Gaussian field to generate snowflakes, raindrops and fog in the scene. The attributes and dynamics of these particles are precisely controlled through physical-based modelling and simulation, ensuring realistic weather representation and flexible severity adjustments. Finally, we integrate the 4D Gaussian field with the 3D scene to render consistent and highly realistic weather effects. Experiments on multiple driving datasets demonstrate that WeatherEdit can generate diverse weather effects with controllable condition severity, highlighting its potential for autonomous driving simulation in adverse weather. See project page: https://jumponthemoon.github.io/w-edit

  </details>

- **[CTRL-GS: Cascaded Temporal Residue Learning for 4D Gaussian Splatting](https://arxiv.org/abs/2505.18306)**  
  *Karly Hou, Wanhua Li, Hanspeter Pfister*  
  `2025-05-23` · `cs.CV` · [abs](https://arxiv.org/abs/2505.18306) · [pdf](https://arxiv.org/pdf/2505.18306.pdf)
  > 💡 将动态场景分解为视频-片段-帧结构并利用残差学习建模，实现4D高斯泼溅的实时渲染与最优视觉质量。

  <details><summary>Abstract</summary>

  Recently, Gaussian Splatting methods have emerged as a desirable substitute for prior Radiance Field methods for novel-view synthesis of scenes captured with multi-view images or videos. In this work, we propose a novel extension to 4D Gaussian Splatting for dynamic scenes. Drawing on ideas from residual learning, we hierarchically decompose the dynamic scene into a "video-segment-frame" structure, with segments dynamically adjusted by optical flow. Then, instead of directly predicting the time-dependent signals, we model the signal as the sum of video-constant values, segment-constant values, and frame-specific residuals, as inspired by the success of residual learning. This approach allows more flexible models that adapt to highly variable scenes. We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets, with the greatest improvements on complex scenes with large movements, occlusions, and fine details, where current methods degrade most.

  </details>

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535)**  
  *Asrar Alruwayqi*  
  `2025-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2505.16535) · [pdf](https://arxiv.org/pdf/2505.16535.pdf)
  > 💡 使用三平面变形场和球谐注意力渲染，结合潜在扩散先验实现紧凑一致的动态三维重建，显著提升稀疏视图下的质量与鲁棒性。

  <details><summary>Abstract</summary>

  We present a novel framework for dynamic 3D scene reconstruction that integrates three key components: an explicit tri-plane deformation field, a view-conditioned canonical radiance field with spherical harmonics (SH) attention, and a temporally-aware latent diffusion prior. Our method encodes 4D scenes using three orthogonal 2D feature planes that evolve over time, enabling efficient and compact spatiotemporal representation. These features are explicitly warped into a canonical space via a deformation offset field, eliminating the need for MLP-based motion modeling. In canonical space, we replace traditional MLP decoders with a structured SH-based rendering head that synthesizes view-dependent color via attention over learned frequency bands improving both interpretability and rendering efficiency. To further enhance fidelity and temporal consistency, we introduce a transformer-guided latent diffusion module that refines the tri-plane and deformation features in a compressed latent space. This generative module denoises scene representations under ambiguous or out-of-distribution (OOD) motion, improving generalization. Our model is trained in two stages: the diffusion module is first pre-trained independently, and then fine-tuned jointly with the full pipeline using a combination of image reconstruction, diffusion denoising, and temporal consistency losses. We demonstrate state-of-the-art results on synthetic benchmarks, surpassing recent methods such as HexPlane and 4D Gaussian Splatting in visual quality, temporal coherence, and robustness to sparse-view dynamic inputs.

  </details>

- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215)**  
  *Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park*  
  `2025-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2505.13215) · [pdf](https://arxiv.org/pdf/2505.13215.pdf)
  > 💡 针对动态场景中4D高斯冗余问题，提出混合3D-4D高斯表示，迭代转换静态区域，降低计算开销并加速训练。

  <details><summary>Abstract</summary>

  Recent advancements in dynamic 3D scene reconstruction have shown promising results, enabling high-fidelity 3D novel view synthesis with improved temporal consistency. Among these, 4D Gaussian Splatting (4DGS) has emerged as an appealing approach due to its ability to model high-fidelity spatial and temporal variations. However, existing methods suffer from substantial computational and memory overhead due to the redundant allocation of 4D Gaussians to static regions, which can also degrade image quality. In this work, we introduce hybrid 3D-4D Gaussian Splatting (3D-4DGS), a novel framework that adaptively represents static regions with 3D Gaussians while reserving 4D Gaussians for dynamic elements. Our method begins with a fully 4D Gaussian representation and iteratively converts temporally invariant Gaussians into 3D, significantly reducing the number of parameters and improving computational efficiency. Meanwhile, dynamic Gaussians retain their full 4D representation, capturing complex motions with high fidelity. Our approach achieves significantly faster training times compared to baseline 4D Gaussian Splatting methods while maintaining or improving the visual quality.

  </details>

- **[ADC-GS: Anchor-Driven Deformable and Compressed Gaussian Splatting for Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.08196)**  
  *He Huang, Qi Yang, Mufan Liu, Yiling Xu, Zhu Li*  
  `2025-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2505.08196) · [pdf](https://arxiv.org/pdf/2505.08196.pdf)
  > 💡 针对动态场景重建中高斯原语冗余，提出锚定驱动变形压缩GS，结合分层运动捕获与率失真优化，渲染速度提升300%-800%且存储高效。

  <details><summary>Abstract</summary>

  Existing 4D Gaussian Splatting methods rely on per-Gaussian deformation from a canonical space to target frames, which overlooks redundancy among adjacent Gaussian primitives and results in suboptimal performance. To address this limitation, we propose Anchor-Driven Deformable and Compressed Gaussian Splatting (ADC-GS), a compact and efficient representation for dynamic scene reconstruction. Specifically, ADC-GS organizes Gaussian primitives into an anchor-based structure within the canonical space, enhanced by a temporal significance-based anchor refinement strategy. To reduce deformation redundancy, ADC-GS introduces a hierarchical coarse-to-fine pipeline that captures motions at varying granularities. Moreover, a rate-distortion optimization is adopted to achieve an optimal balance between bitrate consumption and representation fidelity. Experimental results demonstrate that ADC-GS outperforms the per-Gaussian deformation approaches in rendering speed by 300%-800% while achieving state-of-the-art storage efficiency without compromising rendering quality. The code is released at https://github.com/H-Huang774/ADC-GS.git.

  </details>

- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539)**  
  *Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao*  
  `2025-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2505.07539) · [pdf](https://arxiv.org/pdf/2505.07539.pdf)
  > 💡 使用规范空间和变形场结合时间特征流，实现30Mbps高质沉浸视频实时渲染与快速解码。

  <details><summary>Abstract</summary>

  Immersive video offers a 6-Dof-free viewing experience, potentially playing a key role in future video technology. Recently, 4D Gaussian Splatting has gained attention as an effective approach for immersive video due to its high rendering efficiency and quality, though maintaining quality with manageable storage remains challenging. To address this, we introduce GIFStream, a novel 4D Gaussian representation using a canonical space and a deformation field enhanced with time-dependent feature streams. These feature streams enable complex motion modeling and allow efficient compression by leveraging temporal correspondence and motion-aware pruning. Additionally, we incorporate both temporal and spatial compression networks for end-to-end compression. Experimental results show that GIFStream delivers high-quality immersive video at 30 Mbps, with real-time rendering and fast decoding on an RTX 4090. Project page: https://xdimlab.github.io/GIFStream

  </details>

- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650)**  
  *Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan*  
  `2025-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2504.21650) · [pdf](https://arxiv.org/pdf/2504.21650.pdf)
  > 💡 提出HoloTime，用视频扩散模型生成全景视频，结合时空深度估计与4D高斯泼溅重建一致性4D场景。

  <details><summary>Abstract</summary>

  The rapid advancement of diffusion models holds the promise of revolutionizing the application of VR and AR technologies, which typically require scene-level 4D assets for user experience. Nonetheless, existing diffusion models predominantly concentrate on modeling static 3D scenes or object-level dynamics, constraining their capacity to provide truly immersive experiences. To address this issue, we propose HoloTime, a framework that integrates video diffusion models to generate panoramic videos from a single prompt or reference image, along with a 360-degree 4D scene reconstruction method that seamlessly transforms the generated panoramic video into 4D assets, enabling a fully immersive 4D experience for users. Specifically, to tame video diffusion models for generating high-fidelity panoramic videos, we introduce the 360World dataset, the first comprehensive collection of panoramic videos suitable for downstream 4D scene reconstruction tasks. With this curated dataset, we propose Panoramic Animator, a two-stage image-to-video diffusion model that can convert panoramic images into high-quality panoramic videos. Following this, we present Panoramic Space-Time Reconstruction, which leverages a space-time depth estimation method to transform the generated panoramic videos into 4D point clouds, enabling the optimization of a holistic 4D Gaussian Splatting representation to reconstruct spatially and temporally consistent 4D scenes. To validate the efficacy of our method, we conducted a comparative analysis with existing approaches, revealing its superiority in both panoramic video generation and 4D scene reconstruction. This demonstrates our method's capability to create more engaging and realistic immersive environments, thereby enhancing user experiences in VR and AR applications.

  </details>

- **[4DGS-CC: A Contextual Coding Framework for 4D Gaussian Splatting Data Compression](https://arxiv.org/abs/2504.18925)**  
  *Zicong Chen, Zhenghao Chen, Wei Jiang, Wei Wang, Lei Liu, Dong Xu*  
  `2025-04-26` · `cs.CE` · [abs](https://arxiv.org/abs/2504.18925) · [pdf](https://arxiv.org/pdf/2504.18925.pdf)
  > 💡 针对4DGS数据存储挑战，提出上下文编码框架，通过NVCC和VQCC分解压缩4D神经体素与规范3DGS，实现约12倍存储缩减且保持渲染质量。

  <details><summary>Abstract</summary>

  Storage is a significant challenge in reconstructing dynamic scenes with 4D Gaussian Splatting (4DGS) data. In this work, we introduce 4DGS-CC, a contextual coding framework that compresses 4DGS data to meet specific storage constraints. Building upon the established deformable 3D Gaussian Splatting (3DGS) method, our approach decomposes 4DGS data into 4D neural voxels and a canonical 3DGS component, which are then compressed using Neural Voxel Contextual Coding (NVCC) and Vector Quantization Contextual Coding (VQCC), respectively. Specifically, we first decompose the 4D neural voxels into distinct quantized features by separating the temporal and spatial dimensions. To losslessly compress each quantized feature, we leverage the previously compressed features from the temporal and spatial dimensions as priors and apply NVCC to generate the spatiotemporal context for contextual coding. Next, we employ a codebook to store spherical harmonics information from canonical 3DGS as quantized vectors, which are then losslessly compressed by using VQCC with the auxiliary learned hyperpriors for contextual coding, thereby reducing redundancy within the codebook. By integrating NVCC and VQCC, our contextual coding framework, 4DGS-CC, enables multi-rate 4DGS data compression tailored to specific storage requirements. Extensive experiments on three 4DGS data compression benchmarks demonstrate that our method achieves an average storage reduction of approximately 12 times while maintaining rendering fidelity compared to our baseline 4DGS approach.

  </details>

- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318)**  
  *Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu*  
  `2025-04-25` · `cs.CV` · [abs](https://arxiv.org/abs/2504.18318) · [pdf](https://arxiv.org/pdf/2504.18318.pdf)
  > 💡 现有方法缺乏时空-提示一致性导致4D生成质量低，提出时变提示嵌入、几何增强和时域变形模块，首个扩散模型生成4D高斯，实现高质量高效生成（约4.6s/资产）。

  <details><summary>Abstract</summary>

  Text-to-4D generation is rapidly developing and widely applied in various scenarios. However, existing methods often fail to incorporate adequate spatio-temporal modeling and prompt alignment within a unified framework, resulting in temporal inconsistencies, geometric distortions, or low-quality 4D content that deviates from the provided texts. Therefore, we propose STP4D, a novel approach that aims to integrate comprehensive spatio-temporal-prompt consistency modeling for high-quality text-to-4D generation. Specifically, STP4D employs three carefully designed modules: Time-varying Prompt Embedding, Geometric Information Enhancement, and Temporal Extension Deformation, which collaborate to accomplish this goal. Furthermore, STP4D is among the first methods to exploit the Diffusion model to generate 4D Gaussians, combining the fine-grained modeling capabilities and the real-time rendering process of 4DGS with the rapid inference speed of the Diffusion model. Extensive experiments demonstrate that STP4D excels in generating high-fidelity 4D content with exceptional efficiency (approximately 4.6s per asset), surpassing existing methods in both quality and speed.

  </details>

- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844)**  
  *Zhicong Sun, Jacqueline Lo, Jinxing Hu*  
  `2025-04-07` · `cs.RO` · [abs](https://arxiv.org/abs/2504.04844) · [pdf](https://arxiv.org/pdf/2504.04844.pdf)
  > 💡 首个基于4DGS动态场景表示的SLAM，用动力学感知模块滤除不稳定点并施加各向同性正则化，提升了跟踪与建图质量。

  <details><summary>Abstract</summary>

  Simultaneous localization and mapping (SLAM) technology has recently achieved photorealistic mapping capabilities thanks to the real-time, high-fidelity rendering enabled by 3D Gaussian Splatting (3DGS). However, due to the static representation of scenes, current 3DGS-based SLAM encounters issues with pose drift and failure to reconstruct accurate maps in dynamic environments. To address this problem, we present D4DGS-SLAM, the first SLAM method based on 4DGS map representation for dynamic environments. By incorporating the temporal dimension into scene representation, D4DGS-SLAM enables high-quality reconstruction of dynamic scenes. Utilizing the dynamics-aware InfoModule, we can obtain the dynamics, visibility, and reliability of scene points, and filter out unstable dynamic points for tracking accordingly. When optimizing Gaussian points, we apply different isotropic regularization terms to Gaussians with varying dynamic characteristics. Experimental results on real-world dynamic scene datasets demonstrate that our method outperforms state-of-the-art approaches in both camera pose tracking and map quality.

  </details>

- **[Optimizing 4D Gaussians for Dynamic Scene Video from Single Landscape Images](https://arxiv.org/abs/2504.05458)**  
  *In-Hwan Jin, Haesoo Choo, Seong-Hun Jeong, Heemoon Park, Junghwan Kim, Oh-joon Kwon, Kyeongbo Kong*  
  `2025-04-04` · `cs.CV` · [abs](https://arxiv.org/abs/2504.05458) · [pdf](https://arxiv.org/pdf/2504.05458.pdf)
  > 💡 针对单图动画深度感和视角缺陷，提出4D高斯优化完整3D空间，通过多视图生成和一致运动估计实现动态场景视频。

  <details><summary>Abstract</summary>

  To achieve realistic immersion in landscape images, fluids such as water and clouds need to move within the image while revealing new scenes from various camera perspectives. Recently, a field called dynamic scene video has emerged, which combines single image animation with 3D photography. These methods use pseudo 3D space, implicitly represented with Layered Depth Images (LDIs). LDIs separate a single image into depth-based layers, which enables elements like water and clouds to move within the image while revealing new scenes from different camera perspectives. However, as landscapes typically consist of continuous elements, including fluids, the representation of a 3D space separates a landscape image into discrete layers, and it can lead to diminished depth perception and potential distortions depending on camera movement. Furthermore, due to its implicit modeling of 3D space, the output may be limited to videos in the 2D domain, potentially reducing their versatility. In this paper, we propose representing a complete 3D space for dynamic scene video by modeling explicit representations, specifically 4D Gaussians, from a single image. The framework is focused on optimizing 3D Gaussians by generating multi-view images from a single image and creating 3D motion to optimize 4D Gaussians. The most important part of proposed framework is consistent 3D motion estimation, which estimates common motion among multi-view images to bring the motion in 3D space closer to actual motions. As far as we know, this is the first attempt that considers animation while representing a complete 3D space from a single landscape image. Our model demonstrates the ability to provide realistic immersion in various landscape images through diverse experiments and metrics. Extensive experimental results are https://cvsp-lab.github.io/ICLR2025_3D-MOM/.

  </details>

- **[Divide-and-Conquer: Dual-Hierarchical Optimization for Semantic 4D Gaussian Spatting](https://arxiv.org/abs/2503.19332)**  
  *Zhiying Yan, Yiyuan Liang, Shilv Cai, Tao Zhang, Sheng Zhong, Luxin Yan, Xu Zou*  
  `2025-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2503.19332) · [pdf](https://arxiv.org/pdf/2503.19332.pdf)
  > 💡 针对语义4D高斯泼溅中动静部分混同导致伪影的问题，提出分治双层次优化，用层次化高斯流与引导实现有效划分，显著提升动态场景

  <details><summary>Abstract</summary>

  Semantic 4D Gaussians can be used for reconstructing and understanding dynamic scenes, with temporal variations than static scenes. Directly applying static methods to understand dynamic scenes will fail to capture the temporal features. Few works focus on dynamic scene understanding based on Gaussian Splatting, since once the same update strategy is employed for both dynamic and static parts, regardless of the distinction and interaction between Gaussians, significant artifacts and noise appear. We propose Dual-Hierarchical Optimization (DHO), which consists of Hierarchical Gaussian Flow and Hierarchical Gaussian Guidance in a divide-and-conquer manner. The former implements effective division of static and dynamic rendering and features. The latter helps to mitigate the issue of dynamic foreground rendering distortion in textured complex scenes. Extensive experiments show that our method consistently outperforms the baselines on both synthetic and real-world datasets, and supports various downstream tasks. Project Page: https://sweety-yan.github.io/DHO.

  </details>

- **[4DGC: Rate-Aware 4D Gaussian Compression for Efficient Streamable Free-Viewpoint Video](https://arxiv.org/abs/2503.18421)**  
  *Qiang Hu, Zihan Zheng, Houqiang Zhong, Sihua Fu, Li Song, XiaoyunZhang, Guangtao Zhai, Yanfeng Wang*  
  `2025-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2503.18421) · [pdf](https://arxiv.org/pdf/2503.18421.pdf)
  > 💡 针对动态3DGS存储传输挑战，提出运动感知动态高斯表示与率失真联合优化压缩框架，显著降低存储且优于现有方法。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has substantial potential for enabling photorealistic Free-Viewpoint Video (FVV) experiences. However, the vast number of Gaussians and their associated attributes poses significant challenges for storage and transmission. Existing methods typically handle dynamic 3DGS representation and compression separately, neglecting motion information and the rate-distortion (RD) trade-off during training, leading to performance degradation and increased model redundancy. To address this gap, we propose 4DGC, a novel rate-aware 4D Gaussian compression framework that significantly reduces storage size while maintaining superior RD performance for FVV. Specifically, 4DGC introduces a motion-aware dynamic Gaussian representation that utilizes a compact motion grid combined with sparse compensated Gaussians to exploit inter-frame similarities. This representation effectively handles large motions, preserving quality and reducing temporal redundancy. Furthermore, we present an end-to-end compression scheme that employs differentiable quantization and a tiny implicit entropy model to compress the motion grid and compensated Gaussians efficiently. The entire framework is jointly optimized using a rate-distortion trade-off. Extensive experiments demonstrate that 4DGC supports variable bitrates and consistently outperforms existing methods in RD performance across multiple datasets.

  </details>

- **[4D Gaussian Splatting SLAM](https://arxiv.org/abs/2503.16710)**  
  *Yanyan Li, Youxu Fang, Zunjie Zhu, Kunyi Li, Yong Ding, Federico Tombari*  
  `2025-03-20` · `cs.CV` · [abs](https://arxiv.org/abs/2503.16710) · [pdf](https://arxiv.org/pdf/2503.16710.pdf)
  > 💡 在动态场景中分类静态与动态高斯，结合控制点与光流监督，实现鲁棒跟踪与高质量视图合成。

  <details><summary>Abstract</summary>

  Simultaneously localizing camera poses and constructing Gaussian radiance fields in dynamic scenes establish a crucial bridge between 2D images and the 4D real world. Instead of removing dynamic objects as distractors and reconstructing only static environments, this paper proposes an efficient architecture that incrementally tracks camera poses and establishes the 4D Gaussian radiance fields in unknown scenarios by using a sequence of RGB-D images. First, by generating motion masks, we obtain static and dynamic priors for each pixel. To eliminate the influence of static scenes and improve the efficiency on learning the motion of dynamic objects, we classify the Gaussian primitives into static and dynamic Gaussian sets, while the sparse control points along with an MLP is utilized to model the transformation fields of the dynamic Gaussians. To more accurately learn the motion of dynamic Gaussians, a novel 2D optical flow map reconstruction algorithm is designed to render optical flows of dynamic objects between neighbor images, which are further used to supervise the 4D Gaussian radiance fields along with traditional photometric and geometric constraints. In experiments, qualitative and quantitative evaluation results show that the proposed method achieves robust tracking and high-quality view synthesis performance in real-world environments.

  </details>

- **[1000+ FPS 4D Gaussian Splatting for Dynamic Scene Rendering](https://arxiv.org/abs/2503.16422)**  
  *Yuheng Yuan, Qiuhong Shen, Xingyi Yang, Xinchao Wang*  
  `2025-03-20` · `cs.CV` · [abs](https://arxiv.org/abs/2503.16422) · [pdf](https://arxiv.org/pdf/2503.16422.pdf)
  > 💡 针对4DGS存储大渲染慢，用时空变化分数剪枝短寿命高斯和活跃掩码减少冗余，实现1000+ FPS。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting (4DGS) has recently gained considerable attention as a method for reconstructing dynamic scenes. Despite achieving superior quality, 4DGS typically requires substantial storage and suffers from slow rendering speed. In this work, we delve into these issues and identify two key sources of temporal redundancy. (Q1) \textbf{Short-Lifespan Gaussians}: 4DGS uses a large portion of Gaussians with short temporal span to represent scene dynamics, leading to an excessive number of Gaussians. (Q2) \textbf{Inactive Gaussians}: When rendering, only a small subset of Gaussians contributes to each frame. Despite this, all Gaussians are processed during rasterization, resulting in redundant computation overhead. To address these redundancies, we present \textbf{4DGS-1K}, which runs at over 1000 FPS on modern GPUs. For Q1, we introduce the Spatial-Temporal Variation Score, a new pruning criterion that effectively removes short-lifespan Gaussians while encouraging 4DGS to capture scene dynamics using Gaussians with longer temporal spans. For Q2, we store a mask for active Gaussians across consecutive frames, significantly reducing redundant computations in rendering. Compared to vanilla 4DGS, our method achieves a $41\times$ reduction in storage and $9\times$ faster rasterization speed on complex dynamic scenes, while maintaining comparable visual quality. Please see our project page at https://4DGS-1K.github.io.

  </details>

- **[Light4GS: Lightweight Compact 4D Gaussian Splatting Generation via Context Model](https://arxiv.org/abs/2503.13948)**  
  *Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu*  
  `2025-03-18` · `cs.CV` · [abs](https://arxiv.org/abs/2503.13948) · [pdf](https://arxiv.org/pdf/2503.13948.pdf)
  > 💡 针对4DGS存储开销大，提出时空显著性剪枝与深度上下文模型，实现120倍压缩并提升渲染速度。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as an efficient and high-fidelity paradigm for novel view synthesis. To adapt 3DGS for dynamic content, deformable 3DGS incorporates temporally deformable primitives with learnable latent embeddings to capture complex motions. Despite its impressive performance, the high-dimensional embeddings and vast number of primitives lead to substantial storage requirements. In this paper, we introduce a \textbf{Light}weight \textbf{4}D\textbf{GS} framework, called Light4GS, that employs significance pruning with a deep context model to provide a lightweight storage-efficient dynamic 3DGS representation. The proposed Light4GS is based on 4DGS that is a typical representation of deformable 3DGS. Specifically, our framework is built upon two core components: (1) a spatio-temporal significance pruning strategy that eliminates over 64\% of the deformable primitives, followed by an entropy-constrained spherical harmonics compression applied to the remainder; and (2) a deep context model that integrates intra- and inter-prediction with hyperprior into a coarse-to-fine context structure to enable efficient multiscale latent embedding compression. Our approach achieves over 120x compression and increases rendering FPS up to 20\% compared to the baseline 4DGS, and also superior to frame-wise state-of-the-art 3DGS compression methods, revealing the effectiveness of our Light4GS in terms of both intra- and inter-prediction methods without sacrificing rendering quality.

  </details>

- **[7DGS: Unified Spatial-Temporal-Angular Gaussian Splatting](https://arxiv.org/abs/2503.07946)**  
  *Zhongpai Gao, Benjamin Planche, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Ziyan Wu*  
  `2025-03-11` · `cs.CV` · [abs](https://arxiv.org/abs/2503.07946) · [pdf](https://arxiv.org/pdf/2503.07946.pdf)
  > 💡 针对动态场景和视角依赖效果缺乏统一方法的问题，提出7D高斯表示与条件切片机制，实现联合优化及实时高质量渲染，PSNR提升7.36 dB。

  <details><summary>Abstract</summary>

  Real-time rendering of dynamic scenes with view-dependent effects remains a fundamental challenge in computer graphics. While recent advances in Gaussian Splatting have shown promising results separately handling dynamic scenes (4DGS) and view-dependent effects (6DGS), no existing method unifies these capabilities while maintaining real-time performance. We present 7D Gaussian Splatting (7DGS), a unified framework representing scene elements as seven-dimensional Gaussians spanning position (3D), time (1D), and viewing direction (3D). Our key contribution is an efficient conditional slicing mechanism that transforms 7D Gaussians into view- and time-conditioned 3D Gaussians, maintaining compatibility with existing 3D Gaussian Splatting pipelines while enabling joint optimization. Experiments demonstrate that 7DGS outperforms prior methods by up to 7.36 dB in PSNR while achieving real-time rendering (401 FPS) on challenging dynamic scenes with complex view-dependent effects. The project page is: https://gaozhongpai.github.io/7dgs/.

  </details>

- **[CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving](https://arxiv.org/abs/2503.06744)**  
  *Rui Song, Chenwei Liang, Yan Xia, Walter Zimmer, Hu Cao, Holger Caesar, Andreas Festag, Alois Knoll*  
  `2025-03-09` · `cs.CV` · [abs](https://arxiv.org/abs/2503.06744) · [pdf](https://arxiv.org/pdf/2503.06744.pdf)
  > 💡 针对自动驾驶动态场景渲染，提出上下文和变形感知的4DGS，利用语义自监督和时域变形跟踪提升动态表示精度。

  <details><summary>Abstract</summary>

  Dynamic scene rendering opens new avenues in autonomous driving by enabling closed-loop simulations with photorealistic data, which is crucial for validating end-to-end algorithms. However, the complex and highly dynamic nature of traffic environments presents significant challenges in accurately rendering these scenes. In this paper, we introduce a novel 4D Gaussian Splatting (4DGS) approach, which incorporates context and temporal deformation awareness to improve dynamic scene rendering. Specifically, we employ a 2D semantic segmentation foundation model to self-supervise the 4D semantic features of Gaussians, ensuring meaningful contextual embedding. Simultaneously, we track the temporal deformation of each Gaussian across adjacent frames. By aggregating and encoding both semantic and temporal deformation features, each Gaussian is equipped with cues for potential deformation compensation within 3D space, facilitating a more precise representation of dynamic scenes. Experimental results show that our method improves 4DGS's ability to capture fine details in dynamic scene rendering for autonomous driving and outperforms other self-supervised methods in 4D reconstruction and novel view synthesis. Furthermore, CoDa-4DGS deforms semantic features with each Gaussian, enabling broader applications.

  </details>

- **[Feature-EndoGaussian: Feature Distilled Gaussian Splatting in Surgical Deformable Scene Reconstruction](https://arxiv.org/abs/2503.06161)**  
  *Kai Li, Junhao Wang, William Han, Ding Zhao*  
  `2025-03-08` · `cs.CV` · [abs](https://arxiv.org/abs/2503.06161) · [pdf](https://arxiv.org/pdf/2503.06161.pdf)
  > 💡 提出特征蒸馏4D高斯泼溅实现手术变形场景实时重建与语义分割，在渲染保真度与分割精度上达到最优。

  <details><summary>Abstract</summary>

  Minimally invasive surgery (MIS) requires high-fidelity, real-time visual feedback of dynamic and low-texture surgical scenes. To address these requirements, we introduce FeatureEndo-4DGS (FE-4DGS), the first real time pipeline leveraging feature-distilled 4D Gaussian Splatting for simultaneous reconstruction and semantic segmentation of deformable surgical environments. Unlike prior feature-distilled methods restricted to static scenes, and existing 4D approaches that lack semantic integration, FE-4DGS seamlessly leverages pre-trained 2D semantic embeddings to produce a unified 4D representation-where semantics also deform with tissue motion. This unified approach enables the generation of real-time RGB and semantic outputs through a single, parallelized rasterization process. Despite the additional complexity from feature distillation, FE-4DGS sustains real-time rendering (61 FPS) with a compact footprint, achieves state-of-the-art rendering fidelity on EndoNeRF (39.1 PSNR) and SCARED (27.3 PSNR), and delivers competitive EndoVis18 segmentation, matching or exceeding strong 2D baselines for binary segmentation tasks (0.93 DSC) and remaining competitive for multi-label segmentation (0.77 DSC).

  </details>

- **[NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics](https://arxiv.org/abs/2503.03115)**  
  *Kun Yang, Yuxiang Liu, Zeyu Cui, Yu Liu, Maojun Zhang, Shen Yan, Qing Wang*  
  `2025-03-05` · `cs.CV` · [abs](https://arxiv.org/abs/2503.03115) · [pdf](https://arxiv.org/pdf/2503.03115.pdf)
  > 💡 针对夜间动态热重建，提出基于热力学和4DGS的NTR-Gaussian，用神经网络预测热力学参数，实现温度预测误差低于1°C。

  <details><summary>Abstract</summary>

  Thermal infrared imaging offers the advantage of all-weather capability, enabling non-intrusive measurement of an object's surface temperature. Consequently, thermal infrared images are employed to reconstruct 3D models that accurately reflect the temperature distribution of a scene, aiding in applications such as building monitoring and energy management. However, existing approaches predominantly focus on static 3D reconstruction for a single time period, overlooking the impact of environmental factors on thermal radiation and failing to predict or analyze temperature variations over time. To address these challenges, we propose the NTR-Gaussian method, which treats temperature as a form of thermal radiation, incorporating elements like convective heat transfer and radiative heat dissipation. Our approach utilizes neural networks to predict thermodynamic parameters such as emissivity, convective heat transfer coefficient, and heat capacity. By integrating these predictions, we can accurately forecast thermal temperatures at various times throughout a nighttime scene. Furthermore, we introduce a dynamic dataset specifically for nighttime thermal imagery. Extensive experiments and evaluations demonstrate that NTR-Gaussian significantly outperforms comparison methods in thermal reconstruction, achieving a predicted temperature error within 1 degree Celsius.

  </details>

- **[Gaussian Difference: Find Any Change Instance in 3D Scenes](https://arxiv.org/abs/2502.16941)**  
  *Binbin Jiang, Rui Huang, Qingyi Zhao, Yuxiang Zhang*  
  `2025-02-24` · `cs.CV` · [abs](https://arxiv.org/abs/2502.16941) · [pdf](https://arxiv.org/pdf/2502.16941.pdf)
  > 💡 利用4D高斯分布嵌入图像并对比实例ID，实现鲁棒的3D场景实例级变化检测，显著优于现有方法。

  <details><summary>Abstract</summary>

  Instance-level change detection in 3D scenes presents significant challenges, particularly in uncontrolled environments lacking labeled image pairs, consistent camera poses, or uniform lighting conditions. This paper addresses these challenges by introducing a novel approach for detecting changes in real-world scenarios. Our method leverages 4D Gaussians to embed multiple images into Gaussian distributions, enabling the rendering of two coherent image sequences. We segment each image and assign unique identifiers to instances, facilitating efficient change detection through ID comparison. Additionally, we utilize change maps and classification encodings to categorize 4D Gaussians as changed or unchanged, allowing for the rendering of comprehensive change maps from any viewpoint. Extensive experiments across various instance-level change detection datasets demonstrate that our method significantly outperforms state-of-the-art approaches like C-NERF and CYWS-3D, especially in scenarios with substantial lighting variations. Our approach offers improved detection accuracy, robustness to lighting changes, and efficient processing times, advancing the field of 3D change detection.

  </details>

- **[Efficient 4D Gaussian Stream with Low Rank Adaptation](https://arxiv.org/abs/2502.16575)**  
  *Zhenhuan Liu, Shuai Liu, Yidong Lu, Yirui Chen, Jie Yang, Wei Liu*  
  `2025-02-23` · `cs.CV` · [abs](https://arxiv.org/abs/2502.16575) · [pdf](https://arxiv.org/pdf/2502.16575.pdf)
  > 💡 利用3D高斯和低秩自适应模型进行动态场景连续学习，减少90%流带宽并保持高渲染质量。

  <details><summary>Abstract</summary>

  Recent methods have made significant progress in synthesizing novel views with long video sequences. This paper proposes a highly scalable method for dynamic novel view synthesis with continual learning. We leverage the 3D Gaussians to represent the scene and a low-rank adaptation-based deformation model to capture the dynamic scene changes. Our method continuously reconstructs the dynamics with chunks of video frames, reduces the streaming bandwidth by $90\%$ while maintaining high rendering quality comparable to the off-line SOTA methods.

  </details>

- **[High-Dynamic Radar Sequence Prediction for Weather Nowcasting Using Spatiotemporal Coherent Gaussian Representation](https://arxiv.org/abs/2502.14895)**  
  *Ziye Wang, Yiran Qin, Lin Zeng, Ruimao Zhang*  
  `2025-02-17` · `cs.CV` · [abs](https://arxiv.org/abs/2502.14895) · [pdf](https://arxiv.org/pdf/2502.14895.pdf)
  > 💡 针对天气预测中3D雷达序列预测难题，提出时空一致高斯表示STC-GS与GauMamba，实现高效高分辨率动态表示与精准预测。

  <details><summary>Abstract</summary>

  Weather nowcasting is an essential task that involves predicting future radar echo sequences based on current observations, offering significant benefits for disaster management, transportation, and urban planning. Current prediction methods are limited by training and storage efficiency, mainly focusing on 2D spatial predictions at specific altitudes. Meanwhile, 3D volumetric predictions at each timestamp remain largely unexplored. To address such a challenge, we introduce a comprehensive framework for 3D radar sequence prediction in weather nowcasting, using the newly proposed SpatioTemporal Coherent Gaussian Splatting (STC-GS) for dynamic radar representation and GauMamba for efficient and accurate forecasting. Specifically, rather than relying on a 4D Gaussian for dynamic scene reconstruction, STC-GS optimizes 3D scenes at each frame by employing a group of Gaussians while effectively capturing their movements across consecutive frames. It ensures consistent tracking of each Gaussian over time, making it particularly effective for prediction tasks. With the temporally correlated Gaussian groups established, we utilize them to train GauMamba, which integrates a memory mechanism into the Mamba framework. This allows the model to learn the temporal evolution of Gaussian groups while efficiently handling a large volume of Gaussian tokens. As a result, it achieves both efficiency and accuracy in forecasting a wide range of dynamic meteorological radar signals. The experimental results demonstrate that our STC-GS can efficiently represent 3D radar sequences with over $16\times$ higher spatial resolution compared with the existing 3D representation methods, while GauMamba outperforms state-of-the-art methods in forecasting a broad spectrum of high-dynamic weather conditions.

  </details>

- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297)**  
  *Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu*  
  `2025-02-12` · `cs.GR` · [abs](https://arxiv.org/abs/2502.08297) · [pdf](https://arxiv.org/pdf/2502.08297.pdf)
  > 💡 引入4D高斯与物理渲染结合，通过粗到细优化恢复几何与PBR属性，实现高质量可重光照体积视频。

  <details><summary>Abstract</summary>

  Volumetric video enables immersive experiences by capturing dynamic 3D scenes, enabling diverse applications for virtual reality, education, and telepresence. However, traditional methods struggle with fixed lighting conditions, while neural approaches face trade-offs in efficiency, quality, or adaptability for relightable scenarios. To address these limitations, we present BEAM, a novel pipeline that bridges 4D Gaussian representations with physically-based rendering (PBR) to produce high-quality, relightable volumetric videos from multi-view RGB footage. BEAM recovers detailed geometry and PBR properties via a series of available Gaussian-based techniques. It first combines Gaussian-based human performance tracking with geometry-aware rasterization in a coarse-to-fine optimization framework to recover spatially and temporally consistent geometries. We further enhance Gaussian attributes by incorporating PBR properties step by step. We generate roughness via a multi-view-conditioned diffusion model, and then derive AO and base color using a 2D-to-3D strategy, incorporating a tailored Gaussian-based ray tracer for efficient visibility computation. Once recovered, these dynamic, relightable assets integrate seamlessly into traditional CG pipelines, supporting real-time rendering with deferred shading and offline rendering with ray tracing. By offering realistic, lifelike visualizations under diverse lighting conditions, BEAM opens new possibilities for interactive entertainment, storytelling, and creative visualization.

  </details>

- **[Instruct-4DGS: Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://arxiv.org/abs/2502.02091)**  
  *Joohyun Kwon, Hanbyel Cho, Junmo Kim*  
  `2025-02-04` · `cs.CV` · [abs](https://arxiv.org/abs/2502.02091) · [pdf](https://arxiv.org/pdf/2502.02091.pdf)
  > 💡 利用4D高斯静态-动态分离表示仅编辑静态部分，配合分数蒸馏对齐，实现高效4D场景编辑，时间减半且质量高。

  <details><summary>Abstract</summary>

  Recent 4D dynamic scene editing methods require editing thousands of 2D images used for dynamic scene synthesis and updating the entire scene with additional training loops, resulting in several hours of processing to edit a single dynamic scene. Therefore, these methods are not scalable with respect to the temporal dimension of the dynamic scene (i.e., the number of timesteps). In this work, we propose Instruct-4DGS, an efficient dynamic scene editing method that is more scalable in terms of temporal dimension. To achieve computational efficiency, we leverage a 4D Gaussian representation that models a 4D dynamic scene by combining static 3D Gaussians with a Hexplane-based deformation field, which captures dynamic information. We then perform editing solely on the static 3D Gaussians, which is the minimal but sufficient component required for visual editing. To resolve the misalignment between the edited 3D Gaussians and the deformation field, which may arise from the editing process, we introduce a refinement stage using a score distillation mechanism. Extensive editing results demonstrate that Instruct-4DGS is efficient, reducing editing time by more than half compared to existing methods while achieving high-quality edits that better follow user instructions. Code and results: https://hanbyelcho.info/instruct-4dgs/

  </details>

- **[GaussianAvatar-Editor: Photorealistic Animatable Gaussian Head Avatar Editor](https://arxiv.org/abs/2501.09978)**  
  *Xiangyue Liu, Kunming Luo, Heng Li, Qi Zhang, Yuan Liu, Li Yi, Ping Tan*  
  `2025-01-17` · `cs.CV` · [abs](https://arxiv.org/abs/2501.09978) · [pdf](https://arxiv.org/pdf/2501.09978.pdf)
  > 💡 通过加权Alpha混合方程处理运动遮挡，条件对抗学习保证时空一致性，实现可动画4D高斯头像的真实感文本驱动编辑。

  <details><summary>Abstract</summary>

  We introduce GaussianAvatar-Editor, an innovative framework for text-driven editing of animatable Gaussian head avatars that can be fully controlled in expression, pose, and viewpoint. Unlike static 3D Gaussian editing, editing animatable 4D Gaussian avatars presents challenges related to motion occlusion and spatial-temporal inconsistency. To address these issues, we propose the Weighted Alpha Blending Equation (WABE). This function enhances the blending weight of visible Gaussians while suppressing the influence on non-visible Gaussians, effectively handling motion occlusion during editing. Furthermore, to improve editing quality and ensure 4D consistency, we incorporate conditional adversarial learning into the editing process. This strategy helps to refine the edited results and maintain consistency throughout the animation. By integrating these methods, our GaussianAvatar-Editor achieves photorealistic and consistent results in animatable 4D Gaussian editing. We conduct comprehensive experiments across various subjects to validate the effectiveness of our proposed techniques, which demonstrates the superiority of our approach over existing methods. More results and code are available at: [Project Link](https://xiangyueliu.github.io/GaussianAvatar-Editor/).

  </details>

- **[Spatiotemporal Gaussian Optimization for 4D Cone Beam CT Reconstruction from Sparse Projections](https://arxiv.org/abs/2501.04140)**  
  *Yabo Fu, Hao Zhang, Weixing Cai, Huiqiao Xie, Licheng Kuo, Laura Cervino, Jean Moran, Xiang Li, Tianfang Li*  
  `2025-01-07` · `physics.med-ph` · [abs](https://arxiv.org/abs/2501.04140) · [pdf](https://arxiv.org/pdf/2501.04140.pdf)
  > 💡 用时空高斯优化从稀疏投影重建4D锥束CT，平衡伪影消除、动态保留和细节恢复。

  <details><summary>Abstract</summary>

  In image-guided radiotherapy (IGRT), four-dimensional cone-beam computed tomography (4D-CBCT) is critical for assessing tumor motion during a patients breathing cycle prior to beam delivery. However, generating 4D-CBCT images with sufficient quality requires significantly more projection images than a standard 3D-CBCT scan, leading to extended scanning times and increased imaging dose to the patient. To address these limitations, there is a strong demand for methods capable of reconstructing high-quality 4D-CBCT images from a 1-minute 3D-CBCT acquisition. The challenge lies in the sparse sampling of projections, which introduces severe streaking artifacts and compromises image quality. This paper introduces a novel framework leveraging spatiotemporal Gaussian representation for 4D-CBCT reconstruction from sparse projections, achieving a balance between streak artifact reduction, dynamic motion preservation, and fine detail restoration. Each Gaussian is characterized by its 3D position, covariance, rotation, and density. Two-dimensional X-ray projection images can be rendered from the Gaussian point cloud representation via X-ray rasterization. The properties of each Gaussian were optimized by minimizing the discrepancy between the measured projections and the rendered X-ray projections. A Gaussian deformation network is jointly optimized to deform these Gaussian properties to obtain a 4D Gaussian representation for dynamic CBCT scene modeling. The final 4D-CBCT images are reconstructed by voxelizing the 4D Gaussians, achieving a high-quality representation that preserves both motion dynamics and spatial detail. The code and reconstruction results can be found at https://github.com/fuyabo/4DGS_for_4DCBCT/tree/main

  </details>

- **[GS-DiT: Advancing Video Generation with Pseudo 4D Gaussian Fields through Efficient Dense 3D Point Tracking](https://arxiv.org/abs/2501.02690)**  
  *Weikang Bian, Zhaoyang Huang, Xiaoyu Shi, Yijin Li, Fu-Yun Wang, Hongsheng Li*  
  `2025-01-05` · `cs.CV` · [abs](https://arxiv.org/abs/2501.02690) · [pdf](https://arxiv.org/pdf/2501.02690.pdf)
  > 💡 用伪4D高斯场和高效密集3D点跟踪赋予DiT视频生成4D可控性，支持镜头变换与创意制作。

  <details><summary>Abstract</summary>

  4D video control is essential in video generation as it enables the use of sophisticated lens techniques, such as multi-camera shooting and dolly zoom, which are currently unsupported by existing methods. Training a video Diffusion Transformer (DiT) directly to control 4D content requires expensive multi-view videos. Inspired by Monocular Dynamic novel View Synthesis (MDVS) that optimizes a 4D representation and renders videos according to different 4D elements, such as camera pose and object motion editing, we bring pseudo 4D Gaussian fields to video generation. Specifically, we propose a novel framework that constructs a pseudo 4D Gaussian field with dense 3D point tracking and renders the Gaussian field for all video frames. Then we finetune a pretrained DiT to generate videos following the guidance of the rendered video, dubbed as GS-DiT. To boost the training of the GS-DiT, we also propose an efficient Dense 3D Point Tracking (D3D-PT) method for the pseudo 4D Gaussian field construction. Our D3D-PT outperforms SpatialTracker, the state-of-the-art sparse 3D point tracking method, in accuracy and accelerates the inference speed by two orders of magnitude. During the inference stage, GS-DiT can generate videos with the same dynamic content while adhering to different camera parameters, addressing a significant limitation of current video generation models. GS-DiT demonstrates strong generalization capabilities and extends the 4D controllability of Gaussian splatting to video generation beyond just camera poses. It supports advanced cinematic effects through the manipulation of the Gaussian field and camera intrinsics, making it a powerful tool for creative video production. Demos are available at https://wkbian.github.io/Projects/GS-DiT/.

  </details>

- **[EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation](https://arxiv.org/abs/2501.01895)**  
  *Siyuan Huang, Liliang Chen, Pengfei Zhou, Shengcong Chen, Zhengkai Jiang, Yue Hu, Yue Liao, Peng Gao, Hongsheng Li, Maoqing Yao, Guanghui Ren*  
  `2025-01-03` · `cs.RO` · [abs](https://arxiv.org/abs/2501.01895) · [pdf](https://arxiv.org/pdf/2501.01895.pdf)
  > 💡 块式自回归视频扩散预测未来空间，融合多视角表示与4D高斯泼溅数据引擎，实现机器人操控SOTA性能。

  <details><summary>Abstract</summary>

  We introduce EnerVerse, a generative robotics foundation model that constructs and interprets embodied spaces. EnerVerse employs a chunk-wise autoregressive video diffusion framework to predict future embodied spaces from instructions, enhanced by a sparse context memory for long-term reasoning. To model the 3D robotics world, we adopt a multi-view video representation, providing rich perspectives to address challenges like motion ambiguity and 3D grounding. Additionally, EnerVerse-D, a data engine pipeline combining generative modeling with 4D Gaussian Splatting, forms a self-reinforcing data loop to reduce the sim-to-real gap. Leveraging these innovations, EnerVerse translates 4D world representations into physical actions via a policy head (EnerVerse-A), achieving state-of-the-art performance in both simulation and real-world tasks. For efficiency, EnerVerse-A reuses features from the first denoising step and predicts action chunks, achieving about 280 ms per 8-step action chunk on a single RTX 4090. Further video demos, dataset samples could be found in our project page.

  </details>

- **[4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives](https://arxiv.org/abs/2412.20720)**  
  *Zeyu Yang, Zijie Pan, Xiatian Zhu, Li Zhang, Jianfeng Feng, Yu-Gang Jiang, Philip H. S. Torr*  
  `2024-12-30` · `cs.CV` · [abs](https://arxiv.org/abs/2412.20720) · [pdf](https://arxiv.org/pdf/2412.20720.pdf)
  > 💡 针对动态场景新视角合成难题，提出原生4D高斯原语建模时空体积，首次实现实时高分辨率逼真渲染并压缩内存。

  <details><summary>Abstract</summary>

  Dynamic 3D scene representation and novel view synthesis are crucial for enabling immersive experiences required by AR/VR and metaverse applications. It is a challenging task due to the complexity of unconstrained real-world scenes and their temporal dynamics. In this paper, we reformulate the reconstruction of a time-varying 3D scene as approximating its underlying spatiotemporal 4D volume by optimizing a collection of native 4D primitives, i.e., 4D Gaussians, with explicit geometry and appearance modeling. Equipped with a tailored rendering pipeline, our representation can be end-to-end optimized using only photometric supervision while free viewpoint viewing at interactive frame rate, making it suitable for representing real world scene with complex dynamic. This approach has been the first solution to achieve real-time rendering of high-resolution, photorealistic novel views for complex dynamic scenes. To facilitate real-world applications, we derive several compact variants that effectively reduce the memory footprint to address its storage bottleneck. Extensive experiments validate the superiority of 4DGS in terms of visual quality and efficiency across a range of dynamic scene-related tasks (e.g., novel view synthesis, 4D generation, scene understanding) and scenarios (e.g., single object, indoor scenes, driving environments, synthetic and real data).

  </details>

- **[Representing Long Volumetric Video with Temporal Gaussian Hierarchy](https://arxiv.org/abs/2412.09608)**  
  *Zhen Xu, Yinghao Xu, Zhiyuan Yu, Sida Peng, Jiaming Sun, Hujun Bao, Xiaowei Zhou*  
  `2024-12-12` · `cs.CV` · [abs](https://arxiv.org/abs/2412.09608) · [pdf](https://arxiv.org/pdf/2412.09608.pdf)
  > 💡 针对长体积视频重建的内存瓶颈，提出时序高斯层级表示，通过多级自适应共享原语，实现分钟级视频的高效低存储高质量渲染。

  <details><summary>Abstract</summary>

  This paper aims to address the challenge of reconstructing long volumetric videos from multi-view RGB videos. Recent dynamic view synthesis methods leverage powerful 4D representations, like feature grids or point cloud sequences, to achieve high-quality rendering results. However, they are typically limited to short (1~2s) video clips and often suffer from large memory footprints when dealing with longer videos. To solve this issue, we propose a novel 4D representation, named Temporal Gaussian Hierarchy, to compactly model long volumetric videos. Our key observation is that there are generally various degrees of temporal redundancy in dynamic scenes, which consist of areas changing at different speeds. Motivated by this, our approach builds a multi-level hierarchy of 4D Gaussian primitives, where each level separately describes scene regions with different degrees of content change, and adaptively shares Gaussian primitives to represent unchanged scene content over different temporal segments, thus effectively reducing the number of Gaussian primitives. In addition, the tree-like structure of the Gaussian hierarchy allows us to efficiently represent the scene at a particular moment with a subset of Gaussian primitives, leading to nearly constant GPU memory usage during the training or rendering regardless of the video length. Extensive experimental results demonstrate the superiority of our method over alternative methods in terms of training cost, rendering speed, and storage usage. To our knowledge, this work is the first approach capable of efficiently handling minutes of volumetric video data while maintaining state-of-the-art rendering quality. Our project page is available at: https://zju3dv.github.io/longvolcap.

  </details>

- **[DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving](https://arxiv.org/abs/2412.09043)**  
  *Hao Lu, Tianshuo Xu, Wenzhao Zheng, Yunpeng Zhang, Wei Zhan, Dalong Du, Masayoshi Tomizuka, Kurt Keutzer, Yingcong Chen*  
  `2024-12-12` · `cs.CV` · [abs](https://arxiv.org/abs/2412.09043) · [pdf](https://arxiv.org/pdf/2412.09043.pdf)
  > 💡 现有街景4D重建耗时长，提出DrivingRecon模型，用Prune and Dilate块和动静态解耦直接预测4D高斯，显著提升质量与效率。

  <details><summary>Abstract</summary>

  Photorealistic 4D reconstruction of street scenes is essential for developing real-world simulators in autonomous driving. However, most existing methods perform this task offline and rely on time-consuming iterative processes, limiting their practical applications. To this end, we introduce the Large 4D Gaussian Reconstruction Model (DrivingRecon), a generalizable driving scene reconstruction model, which directly predicts 4D Gaussian from surround view videos. To better integrate the surround-view images, the Prune and Dilate Block (PD-Block) is proposed to eliminate overlapping Gaussian points between adjacent views and remove redundant background points. To enhance cross-temporal information, dynamic and static decoupling is tailored to better learn geometry and motion features. Experimental results demonstrate that DrivingRecon significantly improves scene reconstruction quality and novel view synthesis compared to existing methods. Furthermore, we explore applications of DrivingRecon in model pre-training, vehicle adaptation, and scene editing. Our code is available at https://github.com/EnVision-Research/DriveRecon.

  </details>

- **[Deblur4DGS: 4D Gaussian Splatting from Blurry Monocular Video](https://arxiv.org/abs/2412.06424)**  
  *Renlong Wu, Zhilu Zhang, Mingyang Chen, Zifei Yan, Wangmeng Zuo*  
  `2024-12-09` · `cs.CV` · [abs](https://arxiv.org/abs/2412.06424) · [pdf](https://arxiv.org/pdf/2412.06424.pdf)
  > 💡 针对模糊单目视频，提出将动态估计转化为曝光时间估计并引入正则项与模糊感知高斯，实现高质量4D重建及多任务应用。

  <details><summary>Abstract</summary>

  Recent 4D reconstruction methods have yielded impressive results but rely on sharp videos as supervision. However, motion blur often occurs in videos due to camera shake and object movement, while existing methods render blurry results when using such videos for reconstructing 4D models. Although a few approaches attempted to address the problem, they struggled to produce high-quality results, due to the inaccuracy in estimating continuous dynamic representations within the exposure time. Encouraged by recent works in 3D motion trajectory modeling using 3D Gaussian Splatting (3DGS), we take 3DGS as the scene representation manner, and propose Deblur4DGS to reconstruct a high-quality 4D model from blurry monocular video. Specifically, we transform continuous dynamic representations estimation within an exposure time into the exposure time estimation. Moreover, we introduce the exposure regularization term, multi-frame, and multi-resolution consistency regularization term to avoid trivial solutions. Furthermore, to better represent objects with large motion, we suggest blur-aware variable canonical Gaussians. Beyond novel-view synthesis, Deblur4DGS can be applied to improve blurry video from multiple perspectives, including deblurring, frame interpolation, and video stabilization. Extensive experiments in both synthetic and real-world data on the above four tasks show that Deblur4DGS outperforms state-of-the-art 4D reconstruction methods. The codes are available at https://github.com/ZcsrenlongZ/Deblur4DGS.

  </details>

- **[4D Gaussian Splatting with Scale-aware Residual Field and Adaptive Optimization for Real-time Rendering of Temporally Complex Dynamic Scenes](https://arxiv.org/abs/2412.06299)**  
  *Jinbo Yan, Rui Peng, Luyang Tang, Ronggang Wang*  
  `2024-12-09` · `cs.CV` · [abs](https://arxiv.org/abs/2412.06299) · [pdf](https://arxiv.org/pdf/2412.06299.pdf)
  > 💡 针对动态场景渲染慢和时间复杂性难题，提出尺度感知残差场和自适应优化4D高斯溅射，实现实时渲染和最优性能。

  <details><summary>Abstract</summary>

  Reconstructing dynamic scenes from video sequences is a highly promising task in the multimedia domain. While previous methods have made progress, they often struggle with slow rendering and managing temporal complexities such as significant motion and object appearance/disappearance. In this paper, we propose SaRO-GS as a novel dynamic scene representation capable of achieving real-time rendering while effectively handling temporal complexities in dynamic scenes. To address the issue of slow rendering speed, we adopt a Gaussian primitive-based representation and optimize the Gaussians in 4D space, which facilitates real-time rendering with the assistance of 3D Gaussian Splatting. Additionally, to handle temporally complex dynamic scenes, we introduce a Scale-aware Residual Field. This field considers the size information of each Gaussian primitive while encoding its residual feature and aligns with the self-splitting behavior of Gaussian primitives. Furthermore, we propose an Adaptive Optimization Schedule, which assigns different optimization strategies to Gaussian primitives based on their distinct temporal properties, thereby expediting the reconstruction of dynamic regions. Through evaluations on monocular and multi-view datasets, our method has demonstrated state-of-the-art performance. Please see our project page at https://yjb6.github.io/SaRO-GS.github.io.

  </details>

- **[Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2412.05700)**  
  *Saqib Javed, Ahmad Jarrar Khan, Corentin Dumery, Chen Zhao, Mathieu Salzmann*  
  `2024-12-07` · `cs.CV` · [abs](https://arxiv.org/abs/2412.05700) · [pdf](https://arxiv.org/pdf/2412.05700.pdf)
  > 💡 针对动态场景高斯泼溅内存占用高问题，TC3DGS通过时间相关剪枝、混合精度量化和轨迹插值实现高达67倍压缩。

  <details><summary>Abstract</summary>

  Recent advancements in high-fidelity dynamic scene reconstruction have leveraged dynamic 3D Gaussians and 4D Gaussian Splatting for realistic scene representation. However, to make these methods viable for real-time applications such as AR/VR, gaming, and rendering on low-power devices, substantial reductions in memory usage and improvements in rendering efficiency are required. While many state-of-the-art methods prioritize lightweight implementations, they struggle in handling {scenes with complex motions or long sequences}. In this work, we introduce Temporally Compressed 3D Gaussian Splatting (TC3DGS), a novel technique designed specifically to effectively compress dynamic 3D Gaussian representations. TC3DGS selectively prunes Gaussians based on their temporal relevance and employs gradient-aware mixed-precision quantization to dynamically compress Gaussian parameters. In addition, TC3DGS exploits an adapted version of the Ramer-Douglas-Peucker algorithm to further reduce storage by interpolating Gaussian trajectories across frames. Our experiments on multiple datasets demonstrate that TC3DGS achieves up to 67$\times$ compression with minimal or no degradation in visual quality. More results and videos are provided in the supplementary. Project Page: https://ahmad-jarrar.github.io/tc-3dgs/

  </details>

- **[UrbanGS: Semantic-Guided Gaussian Splatting for Urban Scene Reconstruction](https://arxiv.org/abs/2412.03473)**  
  *Ziwen Li, Jiaxin Huang, Runnan Chen, Yunlong Che, Yandong Guo, Tongliang Liu, Fakhri Karray, Mingming Gong*  
  `2024-12-04` · `cs.CV` · [abs](https://arxiv.org/abs/2412.03473) · [pdf](https://arxiv.org/pdf/2412.03473.pdf)
  > 💡 使用2D语义图区分静态与动态区域，通过全局一致性和KNN正则化优化静态，时间嵌入建模动态，实现高质量高效重建。

  <details><summary>Abstract</summary>

  Reconstructing urban scenes is challenging due to their complex geometries and the presence of potentially dynamic objects. 3D Gaussian Splatting (3DGS)-based methods have shown strong performance, but existing approaches often incorporate manual 3D annotations to improve dynamic object modeling, which is impractical due to high labeling costs. Some methods leverage 4D Gaussian Splatting (4DGS) to represent the entire scene, but they treat static and dynamic objects uniformly, leading to unnecessary updates for static elements and ultimately degrading reconstruction quality. To address these issues, we propose UrbanGS, which leverages 2D semantic maps and an existing dynamic Gaussian approach to distinguish static objects from the scene, enabling separate processing of definite static and potentially dynamic elements. Specifically, for definite static regions, we enforce global consistency to prevent unintended changes in dynamic Gaussian and introduce a K-nearest neighbor (KNN)-based regularization to improve local coherence on low-textured ground surfaces. Notably, for potentially dynamic objects, we aggregate temporal information using learnable time embeddings, allowing each Gaussian to model deformations over time. Extensive experiments on real-world datasets demonstrate that our approach outperforms state-of-the-art methods in reconstruction quality and efficiency, accurately preserving static content while capturing dynamic elements.

  </details>

- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684)**  
  *Lingteng Qiu, Shenhao Zhu, Qi Zuo, Xiaodong Gu, Yuan Dong, Junfei Zhang, Chao Xu, Zhe Li, Weihao Yuan, Liefeng Bo, Guanying Chen, Zilong Dong*  
  `2024-12-03` · `cs.CV` · [abs](https://arxiv.org/abs/2412.02684) · [pdf](https://arxiv.org/pdf/2412.02684.pdf)
  > 💡 从单图生成可动画化人体头像，利用生成模型输出多视图规范姿态，结合4D高斯溅射处理不一致性，实现逼真实时动画。

  <details><summary>Abstract</summary>

  Generating animatable human avatars from a single image is essential for various digital human modeling applications. Existing 3D reconstruction methods often struggle to capture fine details in animatable models, while generative approaches for controllable animation, though avoiding explicit 3D modeling, suffer from viewpoint inconsistencies in extreme poses and computational inefficiencies. In this paper, we address these challenges by leveraging the power of generative models to produce detailed multi-view canonical pose images, which help resolve ambiguities in animatable human reconstruction. We then propose a robust method for 3D reconstruction of inconsistent images, enabling real-time rendering during inference. Specifically, we adapt a transformer-based video generation model to generate multi-view canonical pose images and normal maps, pretraining on a large-scale video dataset to improve generalization. To handle view inconsistencies, we recast the reconstruction problem as a 4D task and introduce an efficient 3D modeling approach using 4D Gaussian Splatting. Experiments demonstrate that our method achieves photorealistic, real-time animation of 3D human avatars from in-the-wild images, showcasing its effectiveness and generalization capability.

  </details>

- **[Gaussians on their Way: Wasserstein-Constrained 4D Gaussian Splatting with State-Space Modeling](https://arxiv.org/abs/2412.00333)**  
  *Junli Deng, Yihao Luo*  
  `2024-11-30` · `cs.CV` · [abs](https://arxiv.org/abs/2412.00333) · [pdf](https://arxiv.org/pdf/2412.00333.pdf)
  > 💡 融合状态空间建模与Wasserstein几何，通过状态一致性滤波和Wasserstein正则化实现4D高斯的平滑运动，提升动态场景渲染质量和效率。

  <details><summary>Abstract</summary>

  Dynamic scene rendering has taken a leap forward with the rise of 4D Gaussian Splatting, but there's still one elusive challenge: how to make 3D Gaussians move through time as naturally as they would in the real world, all while keeping the motion smooth and consistent. In this paper, we unveil a fresh approach that blends state-space modeling with Wasserstein geometry, paving the way for a more fluid and coherent representation of dynamic scenes. We introduce a State Consistency Filter that merges prior predictions with the current observations, enabling Gaussians to stay true to their way over time. We also employ Wasserstein distance regularization to ensure smooth, consistent updates of Gaussian parameters, reducing motion artifacts. Lastly, we leverage Wasserstein geometry to capture both translational motion and shape deformations, creating a more physically plausible model for dynamic scenes. Our approach guides Gaussians along their natural way in the Wasserstein space, achieving smoother, more realistic motion and stronger temporal coherence. Experimental results show significant improvements in rendering quality and efficiency, outperforming current state-of-the-art techniques.

  </details>

- **[4D Scaffold Gaussian Splatting with Dynamic-Aware Anchor Growing for Efficient and High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2411.17044)**  
  *Woong Oh Cho, In Cho, Seoha Kim, Jeongmin Bae, Youngjung Uh, Seon Joo Kim*  
  `2024-11-26` · `cs.CV` · [abs](https://arxiv.org/abs/2411.17044) · [pdf](https://arxiv.org/pdf/2411.17044.pdf)
  > 💡 针对动态场景重建存储与质量权衡问题，提出保留高斯的4D锚定框架和动态感知锚增长策略，实现高效高保真重建。

  <details><summary>Abstract</summary>

  Modeling dynamic scenes through 4D Gaussians offers high visual fidelity and fast rendering speeds, but comes with significant storage overhead. Recent approaches mitigate this cost by aggressively reducing the number of Gaussians. However, this inevitably removes Gaussians essential for high-quality rendering, leading to severe degradation in dynamic regions. In this paper, we introduce a novel 4D anchor-based framework that tackles the storage cost in different perspective. Rather than reducing the number of Gaussians, our method retains a sufficient quantity to accurately model dynamic contents, while compressing them into compact, grid-aligned 4D anchor features. Each anchor is processed by an MLP to spawn a set of neural 4D Gaussians, which represent a local spatiotemporal region. We design these neural 4D Gaussians to capture temporal changes with minimal parameters, making them well-suited for the MLP-based spawning. Moreover, we introduce a dynamic-aware anchor growing strategy to effectively assign additional anchors to under-reconstructed dynamic regions. Our method adjusts the accumulated gradients with Gaussians' temporal coverage, significantly improving reconstruction quality in dynamic regions. Experimental results highlight that our method achieves state-of-the-art visual quality in dynamic regions, outperforming all baselines by a large margin with practical storage costs.

  </details>

- **[EMD: Explicit Motion Modeling for High-Quality Street Gaussian Splatting](https://arxiv.org/abs/2411.15582)**  
  *Xiaobao Wei, Qingpo Wuwu, Zhongyu Zhao, Zhuangzhe Wu, Nan Huang, Ming Lu, Ningning MA, Shanghang Zhang*  
  `2024-11-23` · `cs.CV` · [abs](https://arxiv.org/abs/2411.15582) · [pdf](https://arxiv.org/pdf/2411.15582.pdf)
  > 💡 针对街景动态物体运动建模不足，提出显式运动分解（EMD）嵌入可学习运动嵌入，实现最先进新视角合成。

  <details><summary>Abstract</summary>

  Photorealistic reconstruction of street scenes is essential for developing real-world simulators in autonomous driving. While recent methods based on 3D/4D Gaussian Splatting (GS) have demonstrated promising results, they still encounter challenges in complex street scenes due to the unpredictable motion of dynamic objects. Current methods typically decompose street scenes into static and dynamic objects, learning the Gaussians in either a supervised manner (e.g., w/ 3D bounding-box) or a self-supervised manner (e.g., w/o 3D bounding-box). However, these approaches do not effectively model the motions of dynamic objects (e.g., the motion speed of pedestrians is clearly different from that of vehicles), resulting in suboptimal scene decomposition. To address this, we propose Explicit Motion Decomposition (EMD), which models the motions of dynamic objects by introducing learnable motion embeddings to the Gaussians, enhancing the decomposition in street scenes. The proposed plug-and-play EMD module compensates for the lack of motion modeling in self-supervised street Gaussian splatting methods. We also introduce tailored training strategies to extend EMD to supervised approaches. Comprehensive experiments demonstrate the effectiveness of our method, achieving state-of-the-art novel view synthesis performance in self-supervised settings. The code is available at: https://qingpowuwu.github.io/emd.

  </details>

- **[SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving](https://arxiv.org/abs/2411.15482)**  
  *Su Sun, Cheng Zhao, Zhuoyang Sun, Yingjie Victor Chen, Mei Chen*  
  `2024-11-23` · `cs.CV` · [abs](https://arxiv.org/abs/2411.15482) · [pdf](https://arxiv.org/pdf/2411.15482.pdf)
  > 💡 用自监督神经运动流场建模4D高斯，无需标注即可实现动态城市场景重建与视图合成，性能领先。

  <details><summary>Abstract</summary>

  Most existing Dynamic Gaussian Splatting methods for complex dynamic urban scenarios rely on accurate object-level supervision from expensive manual labeling, limiting their scalability in real-world applications. In this paper, we introduce SplatFlow, a Self-Supervised Dynamic Gaussian Splatting within Neural Motion Flow Fields (NMFF) to learn 4D space-time representations without requiring tracked 3D bounding boxes, enabling accurate dynamic scene reconstruction and novel view RGB/depth/flow synthesis. SplatFlow designs a unified framework to seamlessly integrate time-dependent 4D Gaussian representation within NMFF, where NMFF is a set of implicit functions to model temporal motions of both LiDAR points and Gaussians as continuous motion flow fields. Leveraging NMFF, SplatFlow effectively decomposes static background and dynamic objects, representing them with 3D and 4D Gaussian primitives, respectively. NMFF also models the correspondences of each 4D Gaussian across time, which aggregates temporal features to enhance cross-view consistency of dynamic components. SplatFlow further improves dynamic object identification by distilling features from 2D foundation models into 4D space-time representation. Comprehensive evaluations conducted on the Waymo and KITTI Datasets validate SplatFlow's state-of-the-art (SOTA) performance for both image reconstruction and novel view synthesis in dynamic urban scenarios.

  </details>

- **[4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization](https://arxiv.org/abs/2411.08879)**  
  *Mijeong Kim, Jongwoo Lim, Bohyung Han*  
  `2024-11-13` · `cs.CV` · [abs](https://arxiv.org/abs/2411.08879) · [pdf](https://arxiv.org/pdf/2411.08879.pdf)
  > 💡 提出不确定性感知正则化和动态区域致密化，解决单目视频4DGS过拟合与初始化问题，提升动态场景新视图合成质量。

  <details><summary>Abstract</summary>

  Novel view synthesis of dynamic scenes is becoming important in various applications, including augmented and virtual reality. We propose a novel 4D Gaussian Splatting (4DGS) algorithm for dynamic scenes from casually recorded monocular videos. To overcome the overfitting problem of existing work for these real-world videos, we introduce an uncertainty-aware regularization that identifies uncertain regions with few observations and selectively imposes additional priors based on diffusion models and depth smoothness on such regions. This approach improves both the performance of novel view synthesis and the quality of training image reconstruction. We also identify the initialization problem of 4DGS in fast-moving dynamic regions, where the Structure from Motion (SfM) algorithm fails to provide reliable 3D landmarks. To initialize Gaussian primitives in such regions, we present a dynamic region densification method using the estimated depth maps and scene flow. Our experiments show that the proposed method improves the performance of 4DGS reconstruction from a video captured by a handheld monocular camera and also exhibits promising results in few-shot static scene reconstruction.

  </details>

- **[Real-Time Spatio-Temporal Reconstruction of Dynamic Endoscopic Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2411.01218)**  
  *Fengze Li, Jishuai He, Jieming Ma, Zhijing Wu*  
  `2024-11-02` · `cs.CV` · [abs](https://arxiv.org/abs/2411.01218) · [pdf](https://arxiv.org/pdf/2411.01218.pdf)
  > 💡 用无偏4DGS和球柱谐函数实时重建动态内窥镜场景，法线对齐约束提升几何精度，达新SOTA。

  <details><summary>Abstract</summary>

  Dynamic scene reconstruction is essential in robotic minimally invasive surgery, providing crucial spatial information that enhances surgical precision and outcomes. However, existing methods struggle to address the complex, temporally dynamic nature of endoscopic scenes. This paper presents ST-Endo4DGS, a novel framework that models the spatio-temporal volume of dynamic endoscopic scenes using unbiased 4D Gaussian Splatting (4DGS) primitives, parameterized by anisotropic ellipses with flexible 4D rotations. This approach enables precise representation of deformable tissue dynamics, capturing intricate spatial and temporal correlations in real time. Additionally, we extend spherindrical harmonics to represent time-evolving appearance, achieving realistic adaptations to lighting and view changes. A new endoscopic normal alignment constraint (ENAC) further enhances geometric fidelity by aligning rendered normals with depth-derived geometry. Extensive evaluations show that ST-Endo4DGS outperforms existing methods in both visual quality and real-time performance, establishing a new state-of-the-art in dynamic scene reconstruction for endoscopic surgery.

  </details>

- **[Fully Explicit Dynamic Gaussian Splatting](https://arxiv.org/abs/2410.15629)**  
  *Junoh Lee, Chang-Yeon Won, Hyunjun Jung, Inhwan Bae, Hae-Gon Jeon*  
  `2024-10-21` · `cs.CV` · [abs](https://arxiv.org/abs/2410.15629) · [pdf](https://arxiv.org/pdf/2410.15629.pdf)
  > 💡 针对动态场景渲染，通过分离静动态高斯并显式插值位置旋转，结合渐进训练和点回溯，实现高质量快速渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting has shown fast and high-quality rendering results in static scenes by leveraging dense 3D prior and explicit representations. Unfortunately, the benefits of the prior and representation do not involve novel view synthesis for dynamic motions. Ironically, this is because the main barrier is the reliance on them, which requires increasing training and rendering times to account for dynamic motions. In this paper, we design a Explicit 4D Gaussian Splatting(Ex4DGS). Our key idea is to firstly separate static and dynamic Gaussians during training, and to explicitly sample positions and rotations of the dynamic Gaussians at sparse timestamps. The sampled positions and rotations are then interpolated to represent both spatially and temporally continuous motions of objects in dynamic scenes as well as reducing computational cost. Additionally, we introduce a progressive training scheme and a point-backtracking technique that improves Ex4DGS's convergence. We initially train Ex4DGS using short timestamps and progressively extend timestamps, which makes it work well with a few point clouds. The point-backtracking is used to quantify the cumulative error of each Gaussian over time, enabling the detection and removal of erroneous Gaussians in dynamic scenes. Comprehensive experiments on various scenes demonstrate the state-of-the-art rendering quality from our method, achieving fast rendering of 62 fps on a single 2080Ti GPU.

  </details>

- **[MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2410.13613)**  
  *Xinjie Zhang, Zhening Liu, Yifan Zhang, Xingtong Ge, Dailan He, Tongda Xu, Yan Wang, Zehong Lin, Shuicheng Yan, Jun Zhang*  
  `2024-10-17` · `cs.CV` · [abs](https://arxiv.org/abs/2410.13613) · [pdf](https://arxiv.org/pdf/2410.13613.pdf)
  > 💡 针对4DGS内存大问题，提出分解颜色属性和熵约束变形，实现约190倍和125倍存储压缩，保持渲染速度和质量。

  <details><summary>Abstract</summary>

  4D Gaussian Splatting (4DGS) has recently emerged as a promising technique for capturing complex dynamic 3D scenes with high fidelity. It utilizes a 4D Gaussian representation and a GPU-friendly rasterizer, enabling rapid rendering speeds. Despite its advantages, 4DGS faces significant challenges, notably the requirement of millions of 4D Gaussians, each with extensive associated attributes, leading to substantial memory and storage cost. This paper introduces a memory-efficient framework for 4DGS. We streamline the color attribute by decomposing it into a per-Gaussian direct color component with only 3 parameters and a shared lightweight alternating current color predictor. This approach eliminates the need for spherical harmonics coefficients, which typically involve up to 144 parameters in classic 4DGS, thereby creating a memory-efficient 4D Gaussian representation. Furthermore, we introduce an entropy-constrained Gaussian deformation technique that uses a deformation field to expand the action range of each Gaussian and integrates an opacity-based entropy loss to limit the number of Gaussians, thus forcing our model to use as few Gaussians as possible to fit a dynamic scene well. With simple half-precision storage and zip compression, our framework achieves a storage reduction by approximately 190$\times$ and 125$\times$ on the Technicolor and Neural 3D Video datasets, respectively, compared to the original 4DGS. Meanwhile, it maintains comparable rendering speeds and scene representation quality, setting a new standard in the field. Code is available at https://github.com/Xinjie-Q/MEGA.

  </details>

- **[DN-4DGS: Denoised Deformable Network with Temporal-Spatial Aggregation for Dynamic Scene Rendering](https://arxiv.org/abs/2410.13607)**  
  *Jiahao Lu, Jiacheng Deng, Ruijie Zhu, Yanzhe Liang, Wenfei Yang, Tianzhu Zhang, Xu Zhou*  
  `2024-10-17` · `cs.CV` · [abs](https://arxiv.org/abs/2410.13607) · [pdf](https://arxiv.org/pdf/2410.13607.pdf)
  > 💡 提出噪声抑制策略和解耦时空聚合模块，解决规范3D高斯坐标噪声和4D信息缺失问题，实现实时高质量动态场景渲染。

  <details><summary>Abstract</summary>

  Dynamic scenes rendering is an intriguing yet challenging problem. Although current methods based on NeRF have achieved satisfactory performance, they still can not reach real-time levels. Recently, 3D Gaussian Splatting (3DGS) has garnered researchers attention due to their outstanding rendering quality and real-time speed. Therefore, a new paradigm has been proposed: defining a canonical 3D gaussians and deforming it to individual frames in deformable fields. However, since the coordinates of canonical 3D gaussians are filled with noise, which can transfer noise into the deformable fields, and there is currently no method that adequately considers the aggregation of 4D information. Therefore, we propose Denoised Deformable Network with Temporal-Spatial Aggregation for Dynamic Scene Rendering (DN-4DGS). Specifically, a Noise Suppression Strategy is introduced to change the distribution of the coordinates of the canonical 3D gaussians and suppress noise. Additionally, a Decoupled Temporal-Spatial Aggregation Module is designed to aggregate information from adjacent points and frames. Extensive experiments on various real-world datasets demonstrate that our method achieves state-of-the-art rendering quality under a real-time level.

  </details>

- **[DriveDreamer4D: World Models Are Effective Data Machines for 4D Driving Scene Representation](https://arxiv.org/abs/2410.13571)**  
  *Guosheng Zhao, Chaojun Ni, Xiaofeng Wang, Zheng Zhu, Xueyang Zhang, Yida Wang, Guan Huang, Xinze Chen, Boyuan Wang, Youyi Zhang, Wenjun Mei, Xingang Wang*  
  `2024-10-17` · `cs.CV` · [abs](https://arxiv.org/abs/2410.13571) · [pdf](https://arxiv.org/pdf/2410.13571.pdf)
  > 💡 利用世界模型生成新轨迹视频并采用cousin数据策略优化4DGS，首次提升4D驾驶场景重建的时空一致性和质量。

  <details><summary>Abstract</summary>

  Closed-loop simulation is essential for advancing end-to-end autonomous driving systems. Contemporary sensor simulation methods, such as NeRF and 3DGS, rely predominantly on conditions closely aligned with training data distributions, which are largely confined to forward-driving scenarios. Consequently, these methods face limitations when rendering complex maneuvers (e.g., lane change, acceleration, deceleration). Recent advancements in autonomous-driving world models have demonstrated the potential to generate diverse driving videos. However, these approaches remain constrained to 2D video generation, inherently lacking the spatiotemporal coherence required to capture intricacies of dynamic driving environments. In this paper, we introduce DriveDreamer4D, which enhances 4D driving scene representation leveraging world model priors. Specifically, we utilize the world model as a data machine to synthesize novel trajectory videos, where structured conditions are explicitly leveraged to control the spatial-temporal consistency of traffic elements. Besides, the cousin data training strategy is proposed to facilitate merging real and synthetic data for optimizing 4DGS. To our knowledge, DriveDreamer4D is the first to utilize video generation models for improving 4D reconstruction in driving scenarios. Experimental results reveal that DriveDreamer4D significantly enhances generation quality under novel trajectory views, achieving a relative improvement in FID by 32.1%, 46.4%, and 16.3% compared to PVG, S3Gaussian, and Deformable-GS. Moreover, DriveDreamer4D markedly enhances the spatiotemporal coherence of driving agents, which is verified by a comprehensive user study and the relative increases of 22.6%, 43.5%, and 15.6% in the NTA-IoU metric.

  </details>

- **[4DStyleGaussian: Zero-shot 4D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2410.10412)**  
  *Wanlin Liang, Hongbin Xu, Weitao Chen, Feng Xiao, Wenxiong Kang*  
  `2024-10-14` · `cs.CV` · [abs](https://arxiv.org/abs/2410.10412) · [pdf](https://arxiv.org/pdf/2410.10412.pdf)
  > 💡 针对动态场景风格迁移的时域一致性问题，嵌入4D高斯泼溅与可逆网络，实现零样本实时风格迁移。

  <details><summary>Abstract</summary>

  3D neural style transfer has gained significant attention for its potential to provide user-friendly stylization with spatial consistency. However, existing 3D style transfer methods often fall short in terms of inference efficiency, generalization ability, and struggle to handle dynamic scenes with temporal consistency. In this paper, we introduce 4DStyleGaussian, a novel 4D style transfer framework designed to achieve real-time stylization of arbitrary style references while maintaining reasonable content affinity, multi-view consistency, and temporal coherence. Our approach leverages an embedded 4D Gaussian Splatting technique, which is trained using a reversible neural network for reducing content loss in the feature distillation process. Utilizing the 4D embedded Gaussians, we predict a 4D style transformation matrix that facilitates spatially and temporally consistent style transfer with Gaussian Splatting. Experiments demonstrate that our method can achieve high-quality and zero-shot stylization for 4D scenarios with enhanced efficiency and spatial-temporal consistency.

  </details>

- **[EmoTalk3D: High-Fidelity Free-View Synthesis of Emotional 3D Talking Head](https://arxiv.org/abs/2408.00297)**  
  *Qianyun He, Xinya Ji, Yicheng Gong, Yuanxun Lu, Zhengyu Diao, Linjia Huang, Yao Yao, Siyu Zhu, Zhan Ma, Songcen Xu, Xiaofei Wu, Zixiao Zhang, Xun Cao, Hao Zhu*  
  `2024-08-01` · `cs.CV` · [abs](https://arxiv.org/abs/2408.00297) · [pdf](https://arxiv.org/pdf/2408.00297.pdf)
  > 💡 提出情感可控3D说话头合成方法，利用语音到几何到外观框架和4D高斯表示实现高保真自由视角渲染与动态细节捕捉。

  <details><summary>Abstract</summary>

  We present a novel approach for synthesizing 3D talking heads with controllable emotion, featuring enhanced lip synchronization and rendering quality. Despite significant progress in the field, prior methods still suffer from multi-view consistency and a lack of emotional expressiveness. To address these issues, we collect EmoTalk3D dataset with calibrated multi-view videos, emotional annotations, and per-frame 3D geometry. By training on the EmoTalk3D dataset, we propose a \textit{`Speech-to-Geometry-to-Appearance'} mapping framework that first predicts faithful 3D geometry sequence from the audio features, then the appearance of a 3D talking head represented by 4D Gaussians is synthesized from the predicted geometry. The appearance is further disentangled into canonical and dynamic Gaussians, learned from multi-view videos, and fused to render free-view talking head animation. Moreover, our model enables controllable emotion in the generated talking heads and can be rendered in wide-range views. Our method exhibits improved rendering quality and stability in lip motion generation while capturing dynamic facial details such as wrinkles and subtle expressions. Experiments demonstrate the effectiveness of our approach in generating high-fidelity and emotion-controllable 3D talking heads. The code and EmoTalk3D dataset are released at https://nju-3dv.github.io/projects/EmoTalk3D.

  </details>

- **[Registering Neural 4D Gaussians for Endoscopic Surgery](https://arxiv.org/abs/2407.20213)**  
  *Yiming Huang, Beilei Cui, Ikemura Kei, Jiekai Zhang, Long Bai, Hongliang Ren*  
  `2024-07-29` · `cs.RO` · [abs](https://arxiv.org/abs/2407.20213) · [pdf](https://arxiv.org/pdf/2407.20213.pdf)
  > 💡 针对动态手术场景配准难题，利用4D高斯泼溅表示和空间感知特征聚合SWC，提出可变形配准策略，实现精确对齐。

  <details><summary>Abstract</summary>

  The recent advance in neural rendering has enabled the ability to reconstruct high-quality 4D scenes using neural networks. Although 4D neural reconstruction is popular, registration for such representations remains a challenging task, especially for dynamic scene registration in surgical planning and simulation. In this paper, we propose a novel strategy for dynamic surgical neural scene registration. We first utilize 4D Gaussian Splatting to represent the surgical scene and capture both static and dynamic scenes effectively. Then, a spatial aware feature aggregation method, Spatially Weight Cluttering (SWC) is proposed to accurately align the feature between surgical scenes, enabling precise and realistic surgical simulations. Lastly, we present a novel strategy of deformable scene registration to register two dynamic scenes. By incorporating both spatial and temporal information for correspondence matching, our approach achieves superior performance compared to existing registration methods for implicit neural representation. The proposed method has the potential to improve surgical planning and training, ultimately leading to better patient outcomes.

  </details>

- **[Segment Any 4D Gaussians](https://arxiv.org/abs/2407.04504)**  
  *Shengxiang Ji, Guanjun Wu, Jiemin Fang, Jiazhong Cen, Taoran Yi, Wenyu Liu, Qi Tian, Xinggang Wang*  
  `2024-07-05` · `cs.CV` · [abs](https://arxiv.org/abs/2407.04504) · [pdf](https://arxiv.org/pdf/2407.04504.pdf)
  > 💡 提出首个基于4D高斯的分割一切框架SA4D，用时域身份特征场和细化过程实现精确分割。

  <details><summary>Abstract</summary>

  Modeling, understanding, and reconstructing the real world are crucial in XR/VR. Recently, 3D Gaussian Splatting (3D-GS) methods have shown remarkable success in modeling and understanding 3D scenes. Similarly, various 4D representations have demonstrated the ability to capture the dynamics of the 4D world. However, there is a dearth of research focusing on segmentation within 4D representations. In this paper, we propose Segment Any 4D Gaussians (SA4D), one of the first frameworks to segment anything in the 4D digital world based on 4D Gaussians. In SA4D, an efficient temporal identity feature field is introduced to handle Gaussian drifting, with the potential to learn precise identity features from noisy and sparse input. Additionally, a 4D segmentation refinement process is proposed to remove artifacts. Our SA4D achieves precise, high-quality segmentation within seconds in 4D Gaussians and shows the ability to remove, recolor, compose, and render high-quality anything masks. More demos are available at: https://jsxzs.github.io/sa4d/.

  </details>

- **[Dynamic Gaussian Marbles for Novel View Synthesis of Casual Monocular Videos](https://arxiv.org/abs/2406.18717)**  
  *Colton Stearns, Adam Harley, Mikaela Uy, Florian Dubost, Federico Tombari, Gordon Wetzstein, Leonidas Guibas*  
  `2024-06-26` · `cs.CV` · [abs](https://arxiv.org/abs/2406.18717) · [pdf](https://arxiv.org/pdf/2406.18717.pdf)
  > 💡 针对单目视频新视角合成，提出各向同性高斯球结合层次化学习和点跟踪先验，实现高质量动态重建。

  <details><summary>Abstract</summary>

  Gaussian splatting has become a popular representation for novel-view synthesis, exhibiting clear strengths in efficiency, photometric quality, and compositional edibility. Following its success, many works have extended Gaussians to 4D, showing that dynamic Gaussians maintain these benefits while also tracking scene geometry far better than alternative representations. Yet, these methods assume dense multi-view videos as supervision. In this work, we are interested in extending the capability of Gaussian scene representations to casually captured monocular videos. We show that existing 4D Gaussian methods dramatically fail in this setup because the monocular setting is underconstrained. Building off this finding, we propose a method we call Dynamic Gaussian Marbles, which consist of three core modifications that target the difficulties of the monocular setting. First, we use isotropic Gaussian "marbles'', reducing the degrees of freedom of each Gaussian. Second, we employ a hierarchical divide and-conquer learning strategy to efficiently guide the optimization towards solutions with globally coherent motion. Finally, we add image-level and geometry-level priors into the optimization, including a tracking loss that takes advantage of recent progress in point tracking. By constraining the optimization, Dynamic Gaussian Marbles learns Gaussian trajectories that enable novel-view rendering and accurately capture the 3D motion of the scene elements. We evaluate on the Nvidia Dynamic Scenes dataset and the DyCheck iPhone dataset, and show that Gaussian Marbles significantly outperforms other Gaussian baselines in quality, and is on-par with non-Gaussian representations, all while maintaining the efficiency, compositionality, editability, and tracking benefits of Gaussians. Our project page can be found here https://geometry.stanford.edu/projects/dynamic-gaussian-marbles.github.io/.

  </details>

- **[LGS: A Light-weight 4D Gaussian Splatting for Efficient Surgical Scene Reconstruction](https://arxiv.org/abs/2406.16073)**  
  *Hengyu Liu, Yifan Liu, Chenxin Li, Wuyang Li, Yixuan Yuan*  
  `2024-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2406.16073) · [pdf](https://arxiv.org/pdf/2406.16073.pdf)
  > 💡 针对动态手术场景重建中4D高斯泼溅存储和渲染瓶颈，提出变形感知剪枝与特征场压缩的轻量框架，实现9倍以上压缩并保持高质量实时渲染。

  <details><summary>Abstract</summary>

  The advent of 3D Gaussian Splatting (3D-GS) techniques and their dynamic scene modeling variants, 4D-GS, offers promising prospects for real-time rendering of dynamic surgical scenarios. However, the prerequisite for modeling dynamic scenes by a large number of Gaussian units, the high-dimensional Gaussian attributes and the high-resolution deformation fields, all lead to serve storage issues that hinder real-time rendering in resource-limited surgical equipment. To surmount these limitations, we introduce a Lightweight 4D Gaussian Splatting framework (LGS) that can liberate the efficiency bottlenecks of both rendering and storage for dynamic endoscopic reconstruction. Specifically, to minimize the redundancy of Gaussian quantities, we propose Deformation-Aware Pruning by gauging the impact of each Gaussian on deformation. Concurrently, to reduce the redundancy of Gaussian attributes, we simplify the representation of textures and lighting in non-crucial areas by pruning the dimensions of Gaussian attributes. We further resolve the feature field redundancy caused by the high resolution of 4D neural spatiotemporal encoder for modeling dynamic scenes via a 4D feature field condensation. Experiments on public benchmarks demonstrate efficacy of LGS in terms of a compression rate exceeding 9 times while maintaining the pleasing visual quality and real-time rendering efficiency. LGS confirms a substantial step towards its application in robotic surgical services.

  </details>

- **[L4GM: Large 4D Gaussian Reconstruction Model](https://arxiv.org/abs/2406.10324)**  
  *Jiawei Ren, Kevin Xie, Ashkan Mirzaei, Hanxue Liang, Xiaohui Zeng, Karsten Kreis, Ziwei Liu, Antonio Torralba, Sanja Fidler, Seung Wook Kim, Huan Ling*  
  `2024-06-14` · `cs.CV` · [abs](https://arxiv.org/abs/2406.10324) · [pdf](https://arxiv.org/pdf/2406.10324.pdf)
  > 💡 单视图视频输入生成动画3D物体，利用3D高斯和时间自注意力实现快速前馈，合成训练泛化真实视频。

  <details><summary>Abstract</summary>

  We present L4GM, the first 4D Large Reconstruction Model that produces animated objects from a single-view video input -- in a single feed-forward pass that takes only a second. Key to our success is a novel dataset of multiview videos containing curated, rendered animated objects from Objaverse. This dataset depicts 44K diverse objects with 110K animations rendered in 48 viewpoints, resulting in 12M videos with a total of 300M frames. We keep our L4GM simple for scalability and build directly on top of LGM, a pretrained 3D Large Reconstruction Model that outputs 3D Gaussian ellipsoids from multiview image input. L4GM outputs a per-frame 3D Gaussian Splatting representation from video frames sampled at a low fps and then upsamples the representation to a higher fps to achieve temporal smoothness. We add temporal self-attention layers to the base LGM to help it learn consistency across time, and utilize a per-timestep multiview rendering loss to train the model. The representation is upsampled to a higher framerate by training an interpolation model which produces intermediate 3D Gaussian representations. We showcase that L4GM that is only trained on synthetic data generalizes extremely well on in-the-wild videos, producing high quality animated 3D assets.

  </details>

- **[Improving Gaussian Splatting with Localized Points Management](https://arxiv.org/abs/2406.04251)**  
  *Haosen Yang, Chenhao Zhang, Wenqing Wang, Marco Volino, Adrian Hilton, Li Zhang, Xiatian Zhu*  
  `2024-06-06` · `cs.CV` · [abs](https://arxiv.org/abs/2406.04251) · [pdf](https://arxiv.org/pdf/2406.04251.pdf)
  > 💡 针对3DGS点管理局限，提出局部点管理（LPM），利用多视图几何识别需优化区域，提升静态/动态GS渲染质量达SOTA。

  <details><summary>Abstract</summary>

  Point management is critical for optimizing 3D Gaussian Splatting models, as point initiation (e.g., via structure from motion) is often distributionally inappropriate. Typically, Adaptive Density Control (ADC) algorithm is adopted, leveraging view-averaged gradient magnitude thresholding for point densification, opacity thresholding for pruning, and regular all-points opacity reset. We reveal that this strategy is limited in tackling intricate/special image regions (e.g., transparent) due to inability of identifying all 3D zones requiring point densification, and lacking an appropriate mechanism to handle ill-conditioned points with negative impacts (e.g., occlusion due to false high opacity). To address these limitations, we propose a Localized Point Management (LPM) strategy, capable of identifying those error-contributing zones in greatest need for both point addition and geometry calibration. Zone identification is achieved by leveraging the underlying multiview geometry constraints, subject to image rendering errors. We apply point densification in the identified zones and then reset the opacity of the points in front of these regions, creating a new opportunity to correct poorly conditioned points. Serving as a versatile plugin, LPM can be seamlessly integrated into existing static 3D and dynamic 4D Gaussian Splatting models with minimal additional cost. Experimental evaluations validate the efficacy of our LPM in boosting a variety of existing 3D/4D models both quantitatively and qualitatively. Notably, LPM improves both static 3DGS and dynamic SpaceTimeGS to achieve state-of-the-art rendering quality while retaining real-time speeds, excelling on challenging datasets such as Tanks & Temples and the Neural 3D Video dataset.

  </details>

- **[Self-Calibrating 4D Novel View Synthesis from Monocular Videos Using Gaussian Splatting](https://arxiv.org/abs/2406.01042)**  
  *Fang Li, Hao Zhang, Narendra Ahuja*  
  `2024-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2406.01042) · [pdf](https://arxiv.org/pdf/2406.01042.pdf)
  > 💡 现有4DGS依赖COLMAP参数精度差且耗时，本文用自校准联合优化相机参数与4D场景，提升大运动及极端视角下新视角合成质量。

  <details><summary>Abstract</summary>

  Gaussian Splatting (GS) has significantly elevated scene reconstruction efficiency and novel view synthesis (NVS) accuracy compared to Neural Radiance Fields (NeRF), particularly for dynamic scenes. However, current 4D NVS methods, whether based on GS or NeRF, primarily rely on camera parameters provided by COLMAP and even utilize sparse point clouds generated by COLMAP for initialization, which lack accuracy as well are time-consuming. This sometimes results in poor dynamic scene representation, especially in scenes with large object movements, or extreme camera conditions e.g. small translations combined with large rotations. Some studies simultaneously optimize the estimation of camera parameters and scenes, supervised by additional information like depth, optical flow, etc. obtained from off-the-shelf models. Using this unverified information as ground truth can reduce robustness and accuracy, which does frequently occur for long monocular videos (with e.g. > hundreds of frames). We propose a novel approach that learns a high-fidelity 4D GS scene representation with self-calibration of camera parameters. It includes the extraction of 2D point features that robustly represent 3D structure, and their use for subsequent joint optimization of camera parameters and 3D structure towards overall 4D scene optimization. We demonstrate the accuracy and time efficiency of our method through extensive quantitative and qualitative experimental results on several standard benchmarks. The results show significant improvements over state-of-the-art methods for 4D novel view synthesis. The source code will be released soon at https://github.com/fangli333/SC-4DGS.

  </details>

- **[PLA4D: Pixel-Level Alignments for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2405.19957)**  
  *Qiaowei Miao, JinSheng Quan, Kehan Li, Yawei Luo*  
  `2024-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2405.19957) · [pdf](https://arxiv.org/pdf/2405.19957.pdf)
  > 💡 提出像素级对齐（PLA4D）解决文本到4D高斯泼溅中运动-几何冲突，通过静态和动态对齐实现一致的高质量4D生成。

  <details><summary>Abstract</summary>

  Previous text-to-4D methods have leveraged multiple Score Distillation Sampling (SDS) techniques, combining motion priors from video-based diffusion models (DMs) with geometric priors from multiview DMs to implicitly guide 4D renderings. However, differences in these priors result in conflicting gradient directions during optimization, causing trade-offs between motion fidelity and geometry accuracy, and requiring substantial optimization time to reconcile the models. In this paper, we introduce \textbf{P}ixel-\textbf{L}evel \textbf{A}lignment for text-driven \textbf{4D} Gaussian splatting (PLA4D) to resolve this motion-geometry conflict. PLA4D provides an anchor reference, i.e., text-generated video, to align the rendering process conditioned by different DMs in pixel space. For static alignment, our approach introduces a focal alignment method and Gaussian-Mesh contrastive learning to iteratively adjust focal lengths and provide explicit geometric priors at each timestep. At the dynamic level, a motion alignment technique and T-MV refinement method are employed to enforce both pose alignment and motion continuity across unknown viewpoints, ensuring intrinsic geometric consistency across views. With such pixel-level multi-DM alignment, our PLA4D framework is able to generate 4D objects with superior geometric, motion, and semantic consistency. Fully implemented with open-source tools, PLA4D offers an efficient and accessible solution for high-quality 4D digital content creation with significantly reduced generation time.

  </details>

- **[HFGS: 4D Gaussian Splatting with Emphasis on Spatial and Temporal High-Frequency Components for Endoscopic Scene Reconstruction](https://arxiv.org/abs/2405.17872)**  
  *Haoyu Zhao, Xingyue Zhao, Lingting Zhu, Weixi Zheng, Yongchao Xu*  
  `2024-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2405.17872) · [pdf](https://arxiv.org/pdf/2405.17872.pdf)
  > 💡 提出HFGS，通过空间和时间高频强调重建，解决内窥镜动态场景中3DGS的欠重建问题，显著提升渲染质量。

  <details><summary>Abstract</summary>

  Robot-assisted minimally invasive surgery benefits from enhancing dynamic scene reconstruction, as it improves surgical outcomes. While Neural Radiance Fields (NeRF) have been effective in scene reconstruction, their slow inference speeds and lengthy training durations limit their applicability. To overcome these limitations, 3D Gaussian Splatting (3D-GS) based methods have emerged as a recent trend, offering rapid inference capabilities and superior 3D quality. However, these methods still struggle with under-reconstruction in both static and dynamic scenes. In this paper, we propose HFGS, a novel approach for deformable endoscopic reconstruction that addresses these challenges from spatial and temporal frequency perspectives. Our approach incorporates deformation fields to better handle dynamic scenes and introduces Spatial High-Frequency Emphasis Reconstruction (SHF) to minimize discrepancies in spatial frequency spectra between the rendered image and its ground truth. Additionally, we introduce Temporal High-Frequency Emphasis Reconstruction (THF) to enhance dynamic awareness in neural rendering by leveraging flow priors, focusing optimization on motion-intensive parts. Extensive experiments on two widely used benchmarks demonstrate that HFGS achieves superior rendering quality.

  </details>

- **[NeuroGauss4D-PCI: 4D Neural Fields and Gaussian Deformation Fields for Point Cloud Interpolation](https://arxiv.org/abs/2405.14241)**  
  *Chaokang Jiang, Dalong Du, Jiuming Liu, Siting Zhu, Zhenqiang Liu, Zhuang Ma, Zhujin Liang, Jie Zhou*  
  `2024-05-23` · `cs.CV` · [abs](https://arxiv.org/abs/2405.14241) · [pdf](https://arxiv.org/pdf/2405.14241.pdf)
  > 💡 利用迭代高斯聚类、时变高斯残差和4D变形场与神经场融合，实现复杂非刚性动态点云的高效插值。

  <details><summary>Abstract</summary>

  Point Cloud Interpolation confronts challenges from point sparsity, complex spatiotemporal dynamics, and the difficulty of deriving complete 3D point clouds from sparse temporal information. This paper presents NeuroGauss4D-PCI, which excels at modeling complex non-rigid deformations across varied dynamic scenes. The method begins with an iterative Gaussian cloud soft clustering module, offering structured temporal point cloud representations. The proposed temporal radial basis function Gaussian residual utilizes Gaussian parameter interpolation over time, enabling smooth parameter transitions and capturing temporal residuals of Gaussian distributions. Additionally, a 4D Gaussian deformation field tracks the evolution of these parameters, creating continuous spatiotemporal deformation fields. A 4D neural field transforms low-dimensional spatiotemporal coordinates ($x,y,z,t$) into a high-dimensional latent space. Finally, we adaptively and efficiently fuse the latent features from neural fields and the geometric features from Gaussian deformation fields. NeuroGauss4D-PCI outperforms existing methods in point cloud frame interpolation, delivering leading performance on both object-level (DHB) and large-scale autonomous driving datasets (NL-Drive), with scalability to auto-labeling and point cloud densification tasks. The source code is released at https://github.com/jiangchaokang/NeuroGauss4D-PCI.

  </details>

- **[PhysAvatar: Learning the Physics of Dressed 3D Avatars from Visual Observations](https://arxiv.org/abs/2404.04421)**  
  *Yang Zheng, Qingqing Zhao, Guandao Yang, Wang Yifan, Donglai Xiang, Florian Dubost, Dmitry Lagun, Thabo Beeler, Federico Tombari, Leonidas Guibas, Gordon Wetzstein*  
  `2024-04-05` · `cs.GR` · [abs](https://arxiv.org/abs/2404.04421) · [pdf](https://arxiv.org/pdf/2404.04421.pdf)
  > 💡 结合逆向渲染与物理模拟，利用4D高斯和物理基础渲染器自动估计人体形状、外观及衣物物理参数，实现宽松衣物下的高质量新视角渲染。

  <details><summary>Abstract</summary>

  Modeling and rendering photorealistic avatars is of crucial importance in many applications. Existing methods that build a 3D avatar from visual observations, however, struggle to reconstruct clothed humans. We introduce PhysAvatar, a novel framework that combines inverse rendering with inverse physics to automatically estimate the shape and appearance of a human from multi-view video data along with the physical parameters of the fabric of their clothes. For this purpose, we adopt a mesh-aligned 4D Gaussian technique for spatio-temporal mesh tracking as well as a physically based inverse renderer to estimate the intrinsic material properties. PhysAvatar integrates a physics simulator to estimate the physical parameters of the garments using gradient-based optimization in a principled manner. These novel capabilities enable PhysAvatar to create high-quality novel-view renderings of avatars dressed in loose-fitting clothes under motions and lighting conditions not seen in the training data. This marks a significant advancement towards modeling photorealistic digital humans using physically based inverse rendering with physics in the loop. Our project website is at: https://qingqing-zhao.github.io/PhysAvatar

  </details>

- **[STAG4D: Spatial-Temporal Anchored Generative 4D Gaussians](https://arxiv.org/abs/2403.14939)**  
  *Yifei Zeng, Yanqin Jiang, Siyu Zhu, Yuanxun Lu, Youtian Lin, Hao Zhu, Weiming Hu, Xun Cao, Yao Yao*  
  `2024-03-22` · `cs.CV` · [abs](https://arxiv.org/abs/2403.14939) · [pdf](https://arxiv.org/pdf/2403.14939.pdf)
  > 💡 结合多视图扩散与动态3D高斯泼溅，使用时序锚点和自适应密度策略，实现高保真、时空一致的4D生成。

  <details><summary>Abstract</summary>

  Recent progress in pre-trained diffusion models and 3D generation have spurred interest in 4D content creation. However, achieving high-fidelity 4D generation with spatial-temporal consistency remains a challenge. In this work, we propose STAG4D, a novel framework that combines pre-trained diffusion models with dynamic 3D Gaussian splatting for high-fidelity 4D generation. Drawing inspiration from 3D generation techniques, we utilize a multi-view diffusion model to initialize multi-view images anchoring on the input video frames, where the video can be either real-world captured or generated by a video diffusion model. To ensure the temporal consistency of the multi-view sequence initialization, we introduce a simple yet effective fusion strategy to leverage the first frame as a temporal anchor in the self-attention computation. With the almost consistent multi-view sequences, we then apply the score distillation sampling to optimize the 4D Gaussian point cloud. The 4D Gaussian spatting is specially crafted for the generation task, where an adaptive densification strategy is proposed to mitigate the unstable Gaussian gradient for robust optimization. Notably, the proposed pipeline does not require any pre-training or fine-tuning of diffusion networks, offering a more accessible and practical solution for the 4D generation task. Extensive experiments demonstrate that our method outperforms prior 4D generation works in rendering quality, spatial-temporal consistency, and generation robustness, setting a new state-of-the-art for 4D generation from diverse inputs, including text, image, and video.

  </details>

- **[4D-Rotor Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes](https://arxiv.org/abs/2402.03307)**  
  *Yuanxing Duan, Fangyin Wei, Qiyu Dai, Yuhang He, Wenzheng Chen, Baoquan Chen*  
  `2024-02-05` · `cs.CV` · [abs](https://arxiv.org/abs/2402.03307) · [pdf](https://arxiv.org/pdf/2402.03307.pdf)
  > 💡 用各向异性4D XYZT高斯表示动态场景，通过时间切片实现高效新视角合成，实时渲染达277-583 FPS，优于现有方法。

  <details><summary>Abstract</summary>

  We consider the problem of novel-view synthesis (NVS) for dynamic scenes. Recent neural approaches have accomplished exceptional NVS results for static 3D scenes, but extensions to 4D time-varying scenes remain non-trivial. Prior efforts often encode dynamics by learning a canonical space plus implicit or explicit deformation fields, which struggle in challenging scenarios like sudden movements or generating high-fidelity renderings. In this paper, we introduce 4D Gaussian Splatting (4DRotorGS), a novel method that represents dynamic scenes with anisotropic 4D XYZT Gaussians, inspired by the success of 3D Gaussian Splatting in static scenes. We model dynamics at each timestamp by temporally slicing the 4D Gaussians, which naturally compose dynamic 3D Gaussians and can be seamlessly projected into images. As an explicit spatial-temporal representation, 4DRotorGS demonstrates powerful capabilities for modeling complicated dynamics and fine details--especially for scenes with abrupt motions. We further implement our temporal slicing and splatting techniques in a highly optimized CUDA acceleration framework, achieving real-time inference rendering speeds of up to 277 FPS on an RTX 3090 GPU and 583 FPS on an RTX 4090 GPU. Rigorous evaluations on scenes with diverse motions showcase the superior efficiency and effectiveness of 4DRotorGS, which consistently outperforms existing methods both quantitatively and qualitatively.

  </details>

- **[Endo-4DGS: Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting](https://arxiv.org/abs/2401.16416)**  
  *Yiming Huang, Beilei Cui, Long Bai, Ziqi Guo, Mengya Xu, Mobarakol Islam, Hongliang Ren*  
  `2024-01-29` · `cs.CV` · [abs](https://arxiv.org/abs/2401.16416) · [pdf](https://arxiv.org/pdf/2401.16416.pdf)
  > 💡 针对内窥镜动态重建慢与深度不一致，提出4DGS结合轻量MLP变形场和深度先验，实现实时高精度重建。

  <details><summary>Abstract</summary>

  In the realm of robot-assisted minimally invasive surgery, dynamic scene reconstruction can significantly enhance downstream tasks and improve surgical outcomes. Neural Radiance Fields (NeRF)-based methods have recently risen to prominence for their exceptional ability to reconstruct scenes but are hampered by slow inference speed, prolonged training, and inconsistent depth estimation. Some previous work utilizes ground truth depth for optimization but is hard to acquire in the surgical domain. To overcome these obstacles, we present Endo-4DGS, a real-time endoscopic dynamic reconstruction approach that utilizes 3D Gaussian Splatting (GS) for 3D representation. Specifically, we propose lightweight MLPs to capture temporal dynamics with Gaussian deformation fields. To obtain a satisfactory Gaussian Initialization, we exploit a powerful depth estimation foundation model, Depth-Anything, to generate pseudo-depth maps as a geometry prior. We additionally propose confidence-guided learning to tackle the ill-pose problems in monocular depth estimation and enhance the depth-guided reconstruction with surface normal constraints and depth regularization. Our approach has been validated on two surgical datasets, where it can effectively render in real-time, compute efficiently, and reconstruct with remarkable accuracy.

  </details>

- **[Efficient4D: Fast Dynamic 3D Object Generation from a Single-view Video](https://arxiv.org/abs/2401.08742)**  
  *Zijie Pan, Zeyu Yang, Xiatian Zhu, Li Zhang*  
  `2024-01-16` · `cs.CV` · [abs](https://arxiv.org/abs/2401.08742) · [pdf](https://arxiv.org/pdf/2401.08742.pdf)
  > 💡 单视频生成动态3D物体速度慢，提出Efficient4D框架，用4D高斯溅射和置信度加权损失，实现10倍加速与实时渲染。

  <details><summary>Abstract</summary>

  Generating dynamic 3D object from a single-view video is challenging due to the lack of 4D labeled data. An intuitive approach is to extend previous image-to-3D pipelines by transferring off-the-shelf image generation models such as score distillation sampling.However, this approach would be slow and expensive to scale due to the need for back-propagating the information-limited supervision signals through a large pretrained model. To address this, we propose an efficient video-to-4D object generation framework called Efficient4D. It generates high-quality spacetime-consistent images under different camera views, and then uses them as labeled data to directly reconstruct the 4D content through a 4D Gaussian splatting model. Importantly, our method can achieve real-time rendering under continuous camera trajectories. To enable robust reconstruction under sparse views, we introduce inconsistency-aware confidence-weighted loss design, along with a lightly weighted score distillation loss. Extensive experiments on both synthetic and real videos show that Efficient4D offers a remarkable 10-fold increase in speed when compared to prior art alternatives while preserving the quality of novel view synthesis. For example, Efficient4D takes only 10 minutes to model a dynamic object, vs 120 minutes by the previous art model Consistent4D.

  </details>

- **[DreamGaussian4D: Generative 4D Gaussian Splatting](https://arxiv.org/abs/2312.17142)**  
  *Jiawei Ren, Liang Pan, Jiaxiang Tang, Chi Zhang, Ang Cao, Gang Zeng, Ziwei Liu*  
  `2023-12-28` · `cs.CV` · [abs](https://arxiv.org/abs/2312.17142) · [pdf](https://arxiv.org/pdf/2312.17142.pdf)
  > 💡 针对4D生成耗时长、运动难控、细节不足，提出结合高斯溅射与HexPlane变形及视频纹理细化，数分钟生成高质量可控4D内容。

  <details><summary>Abstract</summary>

  4D content generation has achieved remarkable progress recently. However, existing methods suffer from long optimization times, a lack of motion controllability, and a low quality of details. In this paper, we introduce DreamGaussian4D (DG4D), an efficient 4D generation framework that builds on Gaussian Splatting (GS). Our key insight is that combining explicit modeling of spatial transformations with static GS makes an efficient and powerful representation for 4D generation. Moreover, video generation methods have the potential to offer valuable spatial-temporal priors, enhancing the high-quality 4D generation. Specifically, we propose an integral framework with two major modules: 1) Image-to-4D GS - we initially generate static GS with DreamGaussianHD, followed by HexPlane-based dynamic generation with Gaussian deformation; and 2) Video-to-Video Texture Refinement - we refine the generated UV-space texture maps and meanwhile enhance their temporal consistency by utilizing a pre-trained image-to-video diffusion model. Notably, DG4D reduces the optimization time from several hours to just a few minutes, allows the generated 3D motion to be visually controlled, and produces animated meshes that can be realistically rendered in 3D engines.

  </details>

- **[HiFi4G: High-Fidelity Human Performance Rendering via Compact Gaussian Splatting](https://arxiv.org/abs/2312.03461)**  
  *Yuheng Jiang, Zhehao Shen, Penghao Wang, Zhuo Su, Yu Hong, Yingliang Zhang, Jingyi Yu, Lan Xu*  
  `2023-12-06` · `cs.CV` · [abs](https://arxiv.org/abs/2312.03461) · [pdf](https://arxiv.org/pdf/2312.03461.pdf)
  > 💡 提出紧凑高斯溅射与非刚性跟踪结合，通过双图机制和自适应正则化实现高保真人体性能渲染，压缩率达25倍。

  <details><summary>Abstract</summary>

  We have recently seen tremendous progress in photo-real human modeling and rendering. Yet, efficiently rendering realistic human performance and integrating it into the rasterization pipeline remains challenging. In this paper, we present HiFi4G, an explicit and compact Gaussian-based approach for high-fidelity human performance rendering from dense footage. Our core intuition is to marry the 3D Gaussian representation with non-rigid tracking, achieving a compact and compression-friendly representation. We first propose a dual-graph mechanism to obtain motion priors, with a coarse deformation graph for effective initialization and a fine-grained Gaussian graph to enforce subsequent constraints. Then, we utilize a 4D Gaussian optimization scheme with adaptive spatial-temporal regularizers to effectively balance the non-rigid prior and Gaussian updating. We also present a companion compression scheme with residual compensation for immersive experiences on various platforms. It achieves a substantial compression rate of approximately 25 times, with less than 2MB of storage per frame. Extensive experiments demonstrate the effectiveness of our approach, which significantly outperforms existing approaches in terms of optimization speed, rendering quality, and storage overhead.

  </details>

- **[Real-time Photorealistic Dynamic Scene Representation and Rendering with 4D Gaussian Splatting](https://arxiv.org/abs/2310.10642)**  
  *Zeyu Yang, Hongye Yang, Zijie Pan, Li Zhang*  
  `2023-10-16` · `cs.CV` · [abs](https://arxiv.org/abs/2310.10642) · [pdf](https://arxiv.org/pdf/2310.10642.pdf)
  > 💡 针对动态场景时空结构建模困难，提出4D高斯原语表示时空体积，实现实时高质量新视角合成。

  <details><summary>Abstract</summary>

  Reconstructing dynamic 3D scenes from 2D images and generating diverse views over time is challenging due to scene complexity and temporal dynamics. Despite advancements in neural implicit models, limitations persist: (i) Inadequate Scene Structure: Existing methods struggle to reveal the spatial and temporal structure of dynamic scenes from directly learning the complex 6D plenoptic function. (ii) Scaling Deformation Modeling: Explicitly modeling scene element deformation becomes impractical for complex dynamics. To address these issues, we consider the spacetime as an entirety and propose to approximate the underlying spatio-temporal 4D volume of a dynamic scene by optimizing a collection of 4D primitives, with explicit geometry and appearance modeling. Learning to optimize the 4D primitives enables us to synthesize novel views at any desired time with our tailored rendering routine. Our model is conceptually simple, consisting of a 4D Gaussian parameterized by anisotropic ellipses that can rotate arbitrarily in space and time, as well as view-dependent and time-evolved appearance represented by the coefficient of 4D spherindrical harmonics. This approach offers simplicity, flexibility for variable-length video and end-to-end training, and efficient real-time rendering, making it suitable for capturing complex dynamic scene motions. Experiments across various benchmarks, including monocular and multi-view scenarios, demonstrate our 4DGS model's superior visual quality and efficiency.

  </details>

- **[4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://arxiv.org/abs/2310.08528)**  
  *Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Qi Tian, Xinggang Wang*  
  `2023-10-12` · `cs.CV` · [abs](https://arxiv.org/abs/2310.08528) · [pdf](https://arxiv.org/pdf/2310.08528.pdf)
  > 💡 提出4D高斯溅

  <details><summary>Abstract</summary>

  Representing and rendering dynamic scenes has been an important but challenging task. Especially, to accurately model complex motions, high efficiency is usually hard to guarantee. To achieve real-time dynamic scene rendering while also enjoying high training and storage efficiency, we propose 4D Gaussian Splatting (4D-GS) as a holistic representation for dynamic scenes rather than applying 3D-GS for each individual frame. In 4D-GS, a novel explicit representation containing both 3D Gaussians and 4D neural voxels is proposed. A decomposed neural voxel encoding algorithm inspired by HexPlane is proposed to efficiently build Gaussian features from 4D neural voxels and then a lightweight MLP is applied to predict Gaussian deformations at novel timestamps. Our 4D-GS method achieves real-time rendering under high resolutions, 82 FPS at an 800$\times$800 resolution on an RTX 3090 GPU while maintaining comparable or better quality than previous state-of-the-art methods. More demos and code are available at https://guanjunwu.github.io/4dgs/.

  </details>

- **[Equilibrium and off-equilibrium simulations of the 4d Gaussian spin glass](https://arxiv.org/abs/cond-mat/9606051)**  
  *Giorgio Parisi, Federico Ricci-Tersenghi, Juan J. Ruiz-Lorenzo*  
  `1996-06-09` · `cond-mat` · [abs](https://arxiv.org/abs/cond-mat/9606051) · [pdf](https://arxiv.org/pdf/cond-mat/9606051.pdf)
  > 💡 通过平衡与非平衡模拟，更精确确定了四维高斯自旋玻璃的临界温度与指数，并首次动态获取了序参量值。

  <details><summary>Abstract</summary>

  In this paper we study the on and off-equilibrium properties of the four dimensional Gaussian spin glass. In the static case we determine with more precision that in previous simulations both the critical temperature as well as the critical exponents. In the off-equilibrium case we settle the general form of the autocorrelation function, and show that is possible to obtain dynamically, for the first time, a value for the order parameter.

  </details>

