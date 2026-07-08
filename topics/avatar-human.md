# Avatar / Human / Face

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---













## 2026-07-08

- **[Rendering-Aware Bayesian 3D Gaussian Splatting with Native Uncertainty and Adaptive Complexity Control](https://arxiv.org/abs/2607.05522)**  
  *Gaoxiang Jia, Vikram Appia, Junzhou Huang, Xinlei Wang*  
  `2026-07-06` · `cs.CV` · [abs](https://arxiv.org/abs/2607.05522) · [pdf](https://arxiv.org/pdf/2607.05522.pdf)
  > 💡 提出渲染感知贝叶斯3DGS框架，用Normal-Inverse-Wishart后验实现不确定性量化与自适应复杂度控制，在主动视图选择任务中PSNR提升0.453dB。

  <details><summary>Abstract</summary>

  3D Gaussian splatting (3DGS) is a strong representation for real-time novel-view synthesis, but its standard training pipeline relies on point estimates and hand-tuned heuristics, providing no native uncertainty or principled complexity control. This is most limiting under sparse views or fixed acquisition budgets, where a model must identify weakly supported geometry and select informative views. We introduce a rendering-aware Bayesian 3DGS framework that tracks Gaussian geometry with a Normal-Inverse-Wishart posterior over means and covariances using renderer-derived surrogate summaries. An optional Dirichlet-process extension adds a probabilistic component-usage signal, and the training schedule makes the closed-form versus approximate inference boundary explicit. Re-rendering posterior geometry samples yields native predictive uncertainty for interval calibration and active view selection. In a fixed-budget 16-to-32 active-view task, native NIW acquisition improves PSNR by +0.453 dB and LPIPS by -0.0146 over a scoring-only 3-member standard-ensemble baseline, winning 29/39 scene-seed pairs and 10/13 scene means; it also improves over PPU-style (+0.355 dB) and NIW-proxy (+0.401 dB) acquisition. NIW native intervals reduce 95% coverage error by about 17x relative to a shared proxy (0.046 vs. 0.796) and are about 10x closer to nominal coverage than a 3-member deep ensemble (0.047 vs. 0.454) at roughly one-third the training cost. As a reconstruction compatibility check, paired NIW-vs-standard analysis over 39 scene-seed runs yields +0.030 dB PSNR with 1.6% additional training time. These results position Bayesian 3DGS as a practical probabilistic scene representation for decision-facing tasks such as active view selection.

  </details>

## 2026-07-07

- **[AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction](https://arxiv.org/abs/2607.04256)**  
  *Badrinath Singhal, Srihari K G, Sreehari Iyer, Ankit Dhiman, Venkatesh Babu Radhakrishnan*  
  `2026-07-05` · `cs.CV` · [abs](https://arxiv.org/abs/2607.04256) · [pdf](https://arxiv.org/pdf/2607.04256.pdf)
  > 💡 前馈3D高斯重建存在冗余问题，利用局部纹理信息进行感知剪枝，在不需微调下控制高斯数量并保持质量。

  <details><summary>Abstract</summary>

  Current feed-forward 3D reconstruction methods predict pixel aligned Gaussian primitives, resulting in highly redundant representations. A natural solution is to prune the redundant Gaussians, but naive pruning introduces severe artifacts and often requires inference time fine-tuning, breaking the feed-forward paradigm. Based on previous works, high frequency regions require more Gaussian primitives, while low frequency regions can be represented with significantly fewer primitives. Motivated by this, we propose a novel approach to explicitly control the number of Gaussians by leveraging local texture information. Our approach achieves this through three key components: (1) texture estimation to capture spatial variation in scene detail, (2) texture-aware pruning that removes redundant Gaussians from low frequency regions, and (3) an adaptive Gaussian head that predicts the modified attributes of the retained primitives without breaking the feed-forward paradigm. Experiments on RE10K, ACID, DL3DV, Tanks and Temples, and DTU demonstrate the effectiveness of our approach, while ablation studies validate the contributions of its key components.

  </details>

## 2026-07-02

- **[GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959)**  
  *Haijie Yang, Zhenyu Zhang, Yixuan Dong, Jianjun Qian, Jian Yang*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00959) · [pdf](https://arxiv.org/pdf/2607.00959.pdf)
  > 💡 情感说话头合成中实时可控情感表达挑战，提出基于3DGS的残差变形与空间-音频-情感注意力，实现高保真实时渲染。

  <details><summary>Abstract</summary>

  Audio-driven talking head synthesis has achieved impressive progress in lip synchronization and visual quality, yet generating expressive emotional avatars with controllable intensity remains challenging, especially under real-time constraints. In this paper, we present GaussianEmoTalker, an audio-driven framework for real-time emotional talking head synthesis based on 3D Gaussian Splatting. Instead of directly predicting the final emotional avatar from speech, we formulate emotional animation as a neutral-to-emotional residual deformation problem. GaussianEmoTalker first constructs an identity-specific neutral talking space with GaussianBlendshapes, which provides high-fidelity Gaussian attributes and phoneme-synchronized neutral motion. It then predicts an emotion-conditioned residual deformation by combining mesh displacement cues, audio features, emotion categories, and intensity encodings. To fuse these heterogeneous signals, we introduce a spatial-audio-emotion attention module that estimates the offsets of Gaussian attributes for expressive and temporally stable rendering. Extensive experiments demonstrate that GaussianEmoTalker achieves competitive video quality, accurate lip synchronization, controllable emotional expression, and real-time rendering compared with recent emotional talking head methods. Our project page is available at https://njust-yang.github.io/GaussianEmoTalker.github.io/

  </details>

- **[Path Planning in Physically Viable World Models](https://arxiv.org/abs/2607.00673)**  
  *Su Ann Low, Cheng-Hsi Hsiao, Xingjian Li, Adam J. Thorpe, Ufuk Topcu, Krishna Kumar*  
  `2026-07-01` · `cs.RO` · [abs](https://arxiv.org/abs/2607.00673) · [pdf](https://arxiv.org/pdf/2607.00673.pdf)
  > 💡 通过3D高斯泼溅重建结合物理模拟生成环境变形版本，评估地形变化下路径的长期可行性。

  <details><summary>Abstract</summary>

  Robots deployed in unstructured outdoor environments often plan from scene reconstructions collected before deployment because operators cannot remap large or remote sites before every mission. As a result, robots must make long-horizon planning decisions using stale maps that assume the terrain remains unchanged, even though physical changes to the environment may render previously feasible routes unsafe or unreachable at execution time. We present a physically viable world model for evaluating what-if queries for robot navigation under future terrain change. The system augments reconstructed 3D Gaussian splat scenes with physics-based simulation to generate physically modified versions of the same environment without recollecting sensor data or rebuilding the map. We then implement a terrain-aware planner that accounts for physical events, obstacles, and deformations that are simulated by the world model. This allows robots and human operators to evaluate whether planned routes remain feasible before committing to a planned route, particularly in constrained environments where retreat or recovery may become impossible once conditions change. We evaluate the system on a real outdoor field site in Central Texas using simulated flooding across multiple severity levels. We measure route and mission feasibility as terrain conditions deteriorate under physically simulated interventions. Our results show that physically viable world models expose long-horizon route failures and rerouting behavior that are not apparent when planning only on the original reconstructed environment, allowing robots to evaluate how future terrain changes may affect route feasibility before deployment.

  </details>

## 2026-07-01

- **[Practical High-Fidelity Novel-View Synthesis of Mounted Lepidoptera](https://arxiv.org/abs/2606.31679)**  
  *Kristof Overdulve, Lode Jorissen, Nick Michiels*  
  `2026-06-30` · `cs.GR` · [abs](https://arxiv.org/abs/2606.31679) · [pdf](https://arxiv.org/pdf/2606.31679.pdf)
  > 💡 针对蝴蝶标本微距景深小和腹面不可见难题，结合焦点堆叠、非接触镜面和镜面感知3DGS实现全方位高保真新视角合成。

  <details><summary>Abstract</summary>

  Mounted butterflies are among the most striking objects in natural history collections. However, their beauty is notoriously hard to digitize in 3D: they are small and fragile, with microscopic hairs and vein structures. Capturing them in sufficient detail, therefore, requires a macro lens, which has a very limited Depth of Field (DoF). Moreover, a camera body cannot be maneuvered beneath a pinned specimen to photograph its ventral surface (the underside of the wings). We introduce an end-to-end pipeline that resolves these challenges to turn such specimens into photo-realistic 3D models viewable from every direction. It combines three ingredients: handheld focus stacking for all-in-focus macro capture without a tripod, a non-contact first-surface mirror system that exposes the ventral surface without touching the specimen, and a segmentation-free, mirror-aware 3D Gaussian Splatting extension. We validate the reconstructions on four diverse specimens.

  </details>

## 2026-06-30

- **[VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](https://arxiv.org/abs/2606.30645)**  
  *Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu*  
  `2026-06-29` · `cs.RO` · [abs](https://arxiv.org/abs/2606.30645) · [pdf](https://arxiv.org/pdf/2606.30645.pdf)
  > 💡 利用3DGS重建场景合成视觉-语言-运动学数据，训练人形机器人全身操作策略，实现仿真到真实迁移。

  <details><summary>Abstract</summary>

  Perception-based humanoid loco-manipulation requires connecting egocentric observations and task instructions to whole-body motion. Learning this mapping requires synchronized egocentric images, language commands, and robot-compatible kinematic trajectories, yet no existing data source provides this complete tuple at scale. We address this bottleneck by generating vision-language-kinematics (VLK) supervision synthetically in reconstructed scenes. Our pipeline leverages 3D Gaussian Splatting to reconstruct metric-scale indoor environments, synthesizes navigation and object-interaction trajectories using privileged scene information, and renders paired egocentric observations after the fact. We produce 48,000 paired trajectories with no human intervention and train a VLK policy that predicts short-horizon whole-body kinematic trajectories. A whole-body tracker converts these predictions into actions on the physical humanoid. We evaluate on the physical Unitree G1 performing navigation and single-object transport, demonstrating that synthesized interactions in reconstructed scenes provide effective supervision for sim-to-real perception-based humanoid loco-manipulation. Project Website: https://vision-language-kinematics.github.io/

  </details>

- **[FalconTrack: Photorealistic Auto-Labeled Perception and Physics-Aware Vision-Based Aerial Tracking](https://arxiv.org/abs/2606.29783)**  
  *Yan Miao, Karteek Gandiboyina, Noah Giles, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Sayan Mitra*  
  `2026-06-29` · `cs.RO` · [abs](https://arxiv.org/abs/2606.29783) · [pdf](https://arxiv.org/pdf/2606.29783.pdf)
  > 💡 针对视觉跟踪中手动标注耗时问题，提出FalconTrack，利用高斯溅射模拟器自动生成标签，结合多感知头和物理感知EKF跟踪，实现零样本仿真到现实高成功率迁移。

  <details><summary>Abstract</summary>

  Vision-based aerial tracking is critical in GPS-denied environments. Reliable perception for tracking depends on large-scale labeled data, yet most photorealistic datasets rely on heavy manual annotation and are time-consuming to produce. We present FalconTrack, a unified perception-and-tracking framework that (i) leverages a photorealistic editable simulator for automated label generation and (ii) combines multi-head perception with physics-aware tracking for zero-shot sim-to-real transfer. FalconTrack provides an automated labeling pipeline in a Gaussian Splatting simulator that isolates target Gaussians from short object videos and composites them with randomized backgrounds to generate RGB, mask, class, and 6-DoF pose labels, producing about 10k labeled images in under 20 minutes. Using this dataset, we train a multi-head perception module with staged learning and reprojection consistency, and fuse its outputs with class-conditioned dynamics priors in an EKF for tracking. Our perception model outperforms two baselines and reaches 96-100% class accuracy in zero-shot sim-to-real transfer on three geometrically diverse objects and two environments, while maintaining consistent performance in unseen simulated and real scenes. In real hardware closed-loop visual tracking, the onboard system runs at about 25 Hz and achieves 100% success in sim-to-real F1-tenth and gate tracking in five trajectories across two environments, while a mask-centered vision baseline drops to 60% success on F1-tenth during fast out-of-view scenarios.

  </details>

## 2026-06-24

- **[ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos](https://arxiv.org/abs/2606.24628)**  
  *Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum*  
  `2026-06-23` · `cs.RO` · [abs](https://arxiv.org/abs/2606.24628) · [pdf](https://arxiv.org/pdf/2606.24628.pdf)
  > 💡 基于RGB-D视频，利用3D高斯溅射与无监督关节发现，无需CAD或标注即可自动构建可交互、真实感的可动对象数字孪生。

  <details><summary>Abstract</summary>

  Deploying robots in unstructured real-world environments needs accurate, interactive models of the objects. Constructing these models at scale remains a critical bottleneck for robotic system integration. We present ArtiTwinSplat, a framework that automatically constructs articulated, photo-realistic digital twins of objects directly from RGB-D videos, requiring no CAD models, simulation assets, or manual annotations. Our method is built on 3D Gaussian Splatting that preserve geometric fidelity and photometric realism, coupled with an unsupervised articulation discovery pipeline that recovers part structure and joint kinematics from observed motion alone. With tracking and optimization stages our method provides stable, queryable digital twins that support real-time rendering, viewpoint control, and interactive manipulation. Unlike prior methods confined to simulation, ArtiTwinSplat operates directly on real-world observations and produces twins that are immediately usable by downstream robot planning and learning systems. This method offers a practical, scalable pathway toward digital twin construction, lowering the integration barrier for articulated object manipulation in embodied AI and human-robot collaboration contexts.

  </details>

- **[FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image](https://arxiv.org/abs/2606.24232)**  
  *Kim Youwang, Zhengyu Yang, Liuhao Ge, Yu Rong, Timur Bagautdinov, Su Zhaoen, Nir Sopher, Jovan Popović, Teng Deng, Tae-Hyun Oh, Chen Cao*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24232) · [pdf](https://arxiv.org/pdf/2606.24232.pdf)
  > 💡 单张肖像图像中，结合视觉基础模型和扩散模型，前馈生成高质量可驱动的3D高斯头像，无需测试时优化。

  <details><summary>Abstract</summary>

  We introduce FiCA, a Feed-forward, instant Gaussian Codec Avatar generation pipeline that creates lifelike avatars from a single portrait image. Generating a photorealistic and drivable avatar from just a single image is significantly challenging due to the limited visual information available to accurately infer the 3D appearance and geometry of human heads. To address this, we develop a novel system that combines human-centric vision foundation models with a diffusion model. This system is designed to fully exploit partial visual observations to generate lifelike human avatars. Our proposed diffusion model learns a generative mapping from these partial observations to complete and authentic 3D mesh reconstruction. Additionally, we introduce a feed-forward mesh refinement network that enhances the fidelity and identity preservation of the generated avatars, eliminating the need for person-specific test-time optimization. By leveraging a universal prior model that decodes a generated mesh into a set of 3D Gaussians, we generate a photorealistic 3D Gaussian avatar, capable of being driven with novel expressions in real-time. Our experiments demonstrate that the avatars generated by our feed-forward approach faithfully represent diverse identities and surpass the visual quality of avatars produced by recent competing methods.

  </details>

## 2026-06-23

- **[ACEsplat: Accelerated 3D Gaussian Scene Regression via RGB and Poses Only](https://arxiv.org/abs/2606.22091)**  
  *Mingkai Liu, Haohua Que, Dikai Fan, Haojia Gao, Tianle Zhu, Handong Yao, Qian Zhang, Ruopeng Zhang, Xianliang Huang, Fei Qiao*  
  `2026-06-20` · `cs.RO` · [abs](https://arxiv.org/abs/2606.22091) · [pdf](https://arxiv.org/pdf/2606.22091.pdf)
  > 💡 提出ACEsplat，通过自监督场景坐标回归构建内部几何先验，实现仅由RGB和位姿快速重建3DGS，无需外部初始化，15-25分钟完成。

  <details><summary>Abstract</summary>

  Per-scene 3D Gaussian Splatting (3DGS) enables high-fidelity rendering, but practical robotic and AR scene capture pipelines often depend on external geometric initialization (e.g., SfM point clouds or depth estimates), which can be slow and brittle in on-site deployment. We present ACEsplat, a fast per-scene optimization framework that reconstructs 3D Gaussian representations from RGB images and camera poses only, without requiring external 3D priors (e.g., precomputed SfM models or supervised depth maps). ACEsplat uses a two-stage pipeline: (1) a self-supervised scene coordinate regression (SCR) module builds an internal geometry prior within 4--5 minutes; (2) SCR features and coordinate priors are fused by a lightweight Gaussian initialization head, followed by per-scene 3DGS optimization. On static-view rendering, ACEsplat achieves 29.11 dB PSNR on Wayspots with real-time SLAM poses and 33.20 dB on Cambridge Landmarks with SfM-refined poses. On RealEstate10K sparse-view novel view synthesis, it achieves competitive image fidelity under a challenging 2-view setting. ACEsplat completes scene-specific SCR mapping and 3DGS reconstruction within 15--25 minutes on a single GPU, making it a practical RGB+pose-only solution for rapid scene setup in robotics and mixed-reality applications.

  </details>

## 2026-06-19

- **[One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies](https://arxiv.org/abs/2606.19586)**  
  *Chuer Pan, Litian Liang, Dominik Bauer, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Shuran Song*  
  `2026-06-17` · `cs.RO` · [abs](https://arxiv.org/abs/2606.19586) · [pdf](https://arxiv.org/pdf/2606.19586.pdf)
  > 💡 针对操作任务中观测分布外导致失败的问题，提出基于高斯散射和轨迹优化的鱼眼视图动作增强框架，提升成功率。

  <details><summary>Abstract</summary>

  Visuomotor policies for manipulation have demonstrated remarkable potential in modeling complex robotic behaviors, yet minor alterations in the robot's initial configuration and unseen obstacles easily lead to out-of-distribution observations. Without extensive data collection effort, these result in catastrophic execution failures. In this work, we introduce an effective data augmentation framework that generates visually realistic fisheye image sequences and corresponding physically feasible action trajectories from real-world eye-in-hand demonstrations, captured with a portable parallel gripper with a single fisheye camera. We introduce a novel Gaussian Splatting formulation, adapted to wide FoV fisheye cameras, to reconstruct and edit the 3D scene with unseen objects. We utilize trajectory optimization to generate smooth, collision-free, view-rendering-friendly action trajectories and render visual observations from corresponding novel views. Comprehensive experiments in simulation and the real world show that our augmentation framework improves the success rate for various manipulation tasks in both the same scene and the augmented scene with obstacles requiring collision avoidance.

  </details>

## 2026-06-18

- **[AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement](https://arxiv.org/abs/2606.17998)**  
  *Yuhan Chen, Kunyang Huang, Fuchen Li, Zhuohan Qin, Guofa Li, Wenbo Chu, Keqiang Li*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17998) · [pdf](https://arxiv.org/pdf/2606.17998.pdf)
  > 💡 针对低光增强中光照建模与效率瓶颈，提出基于2D

  <details><summary>Abstract</summary>

  Existing low-light image enhancement methods often face a bottleneck between the representation capacity of illumination-field modeling and computational complexity. To address this issue, this paper proposes an Adaptive Illumination Gaussian Splatting Network (AIGS-Net), an ultra-lightweight architecture for fast low-light enhancement. Unlike conventional static priors, AIGS-Net constructs an input-adaptive 2D Gaussian Splatting illumination field. The opacity of Gaussian basis functions is dynamically modulated by relative luminance statistics of the input image, and spatially varying illumination compensation is rendered through ordered alpha compositing. To guide adaptive illumination compensation efficiently, a zero-parameter nonlinear multiscale contextual encoding module is introduced to extract low-frequency structures and local contrast cues without additional convolutional weights. To suppress noise amplification and sensor-induced color bias, AIGS-Net integrates noise-mask estimation, locked single-channel Gamma mapping, cross-channel consistency regularization, and target color-alignment constraints. Experiments on LOL and LSRW benchmarks show that AIGS-Net improves detail recovery and color fidelity while requiring only approximately 40 learnable parameters, achieving an effective trade-off between enhancement quality and extreme inference efficiency.

  </details>

## 2026-06-09

- **[Wispy to Voluminous: Prior-free Multi-view Capture of Strand-level Facial Hair](https://arxiv.org/abs/2606.08041)**  
  *Jaeseong Lee, Giljoo Nam, Adrian Jarabo, Carlos Aliaga*  
  `2026-06-06` · `cs.GR` · [abs](https://arxiv.org/abs/2606.08041) · [pdf](https://arxiv.org/pdf/2606.08041.pdf)
  > 💡 将多视图图像的无结构3

  <details><summary>Abstract</summary>

  Facial hair is a defining trait of personal identity, yet remains a critical bottleneck for digital avatars. Recent volumetric methods achieve photorealism but bake hair into the underlying face geometry, preventing editability and failing to resolve sparse, strand-like structures. Meanwhile, scalp-hair reconstruction methods target dense hair volumes and do not transfer to the sparse, spatially-varying nature of facial hair. We present a pipeline that automatically reconstructs facial hair -- beard, mustache, lashes, and brows -- from multi-view images, converting an unstructured 3D Gaussian representation into an explicit curve-based strand representation. We resolve geometric ambiguities in four stages: (i) optimizing 3D Gaussians constrained by tracked head geometry to enforce early ray termination and suppress sub-surface noise; (ii) tracing continuous strands robust to frequent crossings and extreme curvature; (iii) grounding strands to the surface and resolving root-tip ambiguity via a physically-motivated prior; and (iv) refining the reconstruction through opacity-driven density control under photometric optimization. To our knowledge, this is the first method to reconstruct high-fidelity facial hair strands from a 3D Gaussian representation. The recovered strands faithfully preserve the orientation and sparsity patterns characteristic of facial hair, and yield assets immediately suitable for downstream production tasks, including facial animation and physical simulation, geometric grooming and transfer, appearance editing, and physics-based rendering.

  </details>

## 2026-06-06

- **[VEDAL: Variational Error-Driven Asynchronous Learning for 3D Gaussian Splatting Pruning](https://arxiv.org/abs/2606.02346)**  
  *Aoduo Li, Jiancheng Li, Huan Ye, Hongjian Xu, Shiting Wu, Xiujun Zhang, Zimeng Li, Xuhang Chen*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02346) · [pdf](https://arxiv.org/pdf/2606.02346.pdf)
  > 💡 用变分自由能最小化建模剪枝，提出预测误差门控和变分不确定性头，实现5.2倍压缩仅降0.31 dB PSNR。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves remarkable novel view synthesis quality with real-time rendering, yet suffers from excessive memory consumption due to millions of Gaussian primitives. Existing pruning methods rely on heuristic importance scores or synchronous batch updates, leading to suboptimal compression and training instability. We propose VEDAL, a principled framework that formulates Gaussian pruning as variational free energy minimization. Our approach introduces (1) a prediction-error gating mechanism that asynchronously activates pruning based on per-Gaussian reconstruction uncertainty, and (2) a variational uncertainty head that models pruning decisions as latent variables with learnable priors. The free energy objective naturally balances reconstruction fidelity against model complexity through an information-theoretic lens. Extensive experiments on Mip-NeRF 360, Tanks&Temples, and Deep Blending demonstrate that VEDAL achieves 5.2x compression with only 0.31 dB PSNR drop, outperforming PUP 3D-GS by +0.05 dB at a higher compression ratio and LightGaussian by +0.35 dB at comparable quality, while maintaining real-time rendering at 185 FPS.

  </details>

- **[Splatshot: 3D Face Avatar Generation from a Single Unconstrained Photo](https://arxiv.org/abs/2606.01493)**  
  *Hao Liang, Zhixuan Ge, Soumendu Majee, Joanna Li, Ashok Veeraraghavan, Guha Balakrishnan*  
  `2026-05-31` · `cs.CV` · [abs](https://arxiv.org/abs/2606.01493) · [pdf](https://arxiv.org/pdf/2606.01493.pdf)
  > 💡 针对单张照片重建3D头像，SplatShot在扩散去噪中联合3DGS与2D先验，实现几何一致与逼真结果。

  <details><summary>Abstract</summary>

  Reconstructing a photorealistic 3D face avatar from a single unconstrained photograph is challenging: feed-forward 3D Gaussian Splatting (3DGS) models degrade on out-of-distribution inputs, while pretrained diffusion models produce high-fidelity images but lack multi-view consistency. We observe that these paradigms are fundamentally complementary: explicit 3D representations guarantee geometric consistency, whereas 2D diffusion priors ensure photorealism. Building on this, we propose SplatShot, a training-free framework that couples these representations directly within the denoising process. Given a base 3DGS face model and a single reference image, we jointly denoise all target views using a per-step 3D feedback loop. At each timestep, we predict clean images from the noisy latents, refit the 3DGS to these multi-view predictions, and back-propagate the photometric discrepancy between the 3DGS re-renderings and 2D predictions into the noise estimate. This steers the sampling trajectory toward strictly 3D-coherent, identity-faithful outputs. Experiments on diverse in-the-wild images demonstrate that SplatShot produces 3D avatars with superior identity preservation, photorealism, and multi-view consistency.

  </details>

- **[LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World](https://arxiv.org/abs/2606.01458)**  
  *Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang, Mac Schwager*  
  `2026-05-31` · `cs.RO` · [abs](https://arxiv.org/abs/2606.01458) · [pdf](https://arxiv.org/pdf/2606.01458.pdf)
  > 💡 LEGS用3DGS背景和程序化基元生成器

  <details><summary>Abstract</summary>

  Training vision-language-action (VLA) policies for humanoid loco-manipulation is constrained by the high cost and complexity of collecting human teleoperation demonstrations. VLA policies fine-tuned in simulators have, until now, failed to transfer effectively in humanoid loco-manipulation tasks. We present LEGS (Loco-manipulation via Embodied Gaussian Splatting), a hybrid simulator that composites a mesh foreground (robot, objects, props) over a photorealistic 3D Gaussian Splatting (3DGS) background reconstructed from a handheld scene capture. LEGS uses a procedural motion-primitive generator to synthesize labeled demonstrations at scale without human teleoperation, and a deterministic two-stage color calibration to align the rendered 3DGS image to the robot's deployment camera. On a Unitree G1 humanoid robot, across three pick-and-place tasks of increasing whole-body difficulty and three VLA backbones (psi_0, pi_0.5, GR00T N1.6), a policy trained purely on LEGS data matches or exceeds one trained on human teleoperation demos on every experiment. It also outperforms a mesh-only simulation baseline that ablates the effect of the 3DGS background, showing that photorealistic rendering is a key enabler for synthetic data transfer. Humanoid motion is recorded independently of scene appearance in LEGS, allowing the same auto-generated demonstrations to be re-rendered under new backgrounds and object meshes--covering a new scene at more than 15x lower cost than teleoperation--to augment training data for robustness to scene variations. Under combined object-and-scene appearance shift, the policy trained on re-rendered LEGS-AUG data maintains task success while the baseline trained on teleoperation data fails entirely. Our project page is located at https://legsvla.github.io/.

  </details>

- **[GeoSAM-3D: Geodesic Prompt Propagation for Open-Vocabulary 3D Scene Segmentation from Monocular Video](https://arxiv.org/abs/2606.00447)**  
  *Arun Sharma*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00447) · [pdf](https://arxiv.org/pdf/2606.00447.pdf)
  > 💡 结合单目视频与3D高斯重建，用测地线热核传播代替欧氏近邻，解决开放词汇分割中曲面连续性与泄漏问题。

  <details><summary>Abstract</summary>

  Open-vocabulary 3D scene segmentation usually assumes RGB-D video, calibrated multi-view imagery, or a reconstructed mesh. GeoSAM-3D studies a lighter setting: a user uploads a short monocular video, clicks or names an object in one frame, and receives a propagated 3D mask over a Gaussian scene. The implementation combines frozen image and video foundation models with a monocular 3D Gaussian Splatting reconstruction and a differentiable graph-geodesic propagation kernel over Gaussian centroids. The central design choice is to propagate prompts by heat-kernel distance on the reconstructed scene graph, rather than by Euclidean nearest neighbors in 3D. This preserves continuity around curved surfaces and reduces leakage across nearby but disconnected objects. This paper describes the repository state, the mathematical kernel implemented in geosam3d.propagate, the feature head trained from Segment Anything masks, and the validation already present in the codebase. The evaluation protocol separates implementation validation, graph propagation quality, leakage control, and interactive latency.

  </details>

## 2026-06-01

- **[Benchmarking Single-Step Inpainting Methods for Multi-Object 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2605.30987)**  
  *Finn Dröge, Cecilia Curreli, Abhishek Saroha, Daniel Cremers*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30987) · [pdf](https://arxiv.org/pdf/2605.30987.pdf)
  > 💡 对比2D修复器用于3DGS场景移除，重建型优于扩散，从头初始化胜于微调，并引入多对象真实数据集。

  <details><summary>Abstract</summary>

  The tasks of object removal and inpainting 3D Gaussian Splatting (3DGS) scenes face challenges such as 3D consistency across camera views. In comparing 2D inpainters and their suitability for the 3D domain, we find that reconstruction-based inpainters outperform generative diffusion models in 3D consistency. Integrating these 2D inpainters into different single-step methods for creating and finetuning 3DGS scenes, our results indicate that initializing the scene from scratch produces higher quality results than finetuning the existing scene. Using a state-of-the-art generative 2D inpainter, we create a straightforward baseline to underline the importance of object removal before inpainting in the 3D setting. Since 360° datasets rarely include real-world ground truths, and challenging occlusion scenarios are equally sparse, we introduce a novel multi-object scene with recorded ground truth data and many views with object occlusions.

  </details>

## 2026-05-30

- **[Eulerian Gaussian Splatting using Hashed Probability Pyramids](https://arxiv.org/abs/2605.29136)**  
  *Mia Gaia Polansky, George Kopanas, Stephan Garbin, Todd Zickler, Dor Verbin*  
  `2026-05-27` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29136) · [pdf](https://arxiv.org/pdf/2605.29136.pdf)
  > 💡 提出概率密度与多尺度分层网格优化，替代启发式原始操作，实现SOTA重建质量并保持快速渲染。

  <details><summary>Abstract</summary>

  We introduce a probabilistic splat-based radiance field framework that retains the fast rasterization and test-time efficiency of 3D Gaussian Splatting (3DGS) while replacing heuristic primitive manipulation with gradient-based optimization of a volumetric probability density. Rather than relocating, splitting, or culling Gaussians via hand-tuned densification (e.g., ADC), we treat primitive locations as samples drawn from a persistent, learnable density. We instantiate this density using a novel, memory-efficient multi-scale hierarchical grid that enables end-to-end gradient-based optimization. To stabilize the optimization, we derive an unbiased gradient estimator with control variates that markedly reduces variance. By allowing probability mass to flow to where the loss demands, our framework eliminates brittle priors and naturally explores the volume, achieving state-of-the-art reconstruction quality on mip-NeRF 360 while preserving 3DGS-level rendering speed.

  </details>

- **[ParkingWorld: End-to-End Autonomous Parking Reinforcement Learning from Corrective Experience in 3DGS Simulation](https://arxiv.org/abs/2605.25029)**  
  *Zhengcheng Yu, Changze Li, Haoran Liu, Tong Qin*  
  `2026-05-24` · `cs.RO` · [abs](https://arxiv.org/abs/2605.25029) · [pdf](https://arxiv.org/pdf/2605.25029.pdf)
  > 💡 针对自动泊车训练低效问题，提出在3DGS仿真中利用校正循环和多级回放缓冲区的CIL-SERL框架，显著提升成功率与安全性。

  <details><summary>Abstract</summary>

  Autonomous parking demands precise low-speed maneuvering within narrow, cluttered, and highly constrained environments, where vehicles must navigate tight spaces while avoiding static obstacles and complex geometric boundaries. Unlike imitation learning, which typically requires massive volumes of high-quality expert demonstrations to converge to a stable policy and often suffers from limited generalization to unseen scenarios, traditional reinforcement learning (RL) methods face persistent challenges including excessive training overhead, inefficient exploration, and even failure to learn viable parking strategies in challenging settings. To address these limitations, this paper presents a correction-in-the-loop sample-efficient reinforcement learning (CIL-SERL) framework for end-to-end autonomous parking, which is entirely trained in a photorealistic 3D Gaussian Splatting (3DGS) parking simulator that enables high-fidelity digital reconstruction of real-world scenes. Inspired by error-correction notebooks used in learning practice, we design a novel multi-level replay buffer mechanism. These buffers hierarchically organize and store standard RL rollouts, human corrective interventions, failed exploration trajectories, and rollback-based correction segments in separate yet interconnected memory regions, facilitating structured sampling and targeted learning during training. The proposed framework is systematically evaluated in both the 3DGS simulation environment and a physical vehicle platform. Extensive experimental results demonstrate that our method achieves substantial improvements in parking success rate, operational efficiency, and safety performance across diverse scenarios, validating the effectiveness and practical applicability of the proposed CIL-SERL-based end-to-end autonomous parking solution.

  </details>

- **[Multi-view Consistent 3D Gaussian Head Avatars 'without' Multi-view Generation](https://arxiv.org/abs/2605.25220)**  
  *Aviral Chharia, Fernando De la Torre*  
  `2026-05-24` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25220) · [pdf](https://arxiv.org/pdf/2605.25220.pdf)
  > 💡 单图生成多视图一致3D高斯头部，提出层次化状态空间与双向扫描及多视图评判器，超越先前方法并发布FaceGS-10K数据集。

  <details><summary>Abstract</summary>

  High-fidelity 3D Gaussian head avatar generation is critical for applications such as AR/VR, telepresence, and digital humans. Existing methods depend on multi-view datasets, 3D captures, or intermediate 2D view synthesis. In contrast, we learn both conditional and unconditional 3D head models from randomly sampled 2D images alone, without using multi-view data, 3D supervision, or intermediate view generation. We introduce MVCHead, a single-shot state space model that enforces multi-view consistency (MVC) directly in the 3D representation while regressing 3D Gaussians under these constraints. At its core, we propose a Hierarchical State Space (HiSS) block that progressively refines Gaussians from coarse to fine, while capturing long-range dependencies. Within each HiSS block, we modify Mamba's standard unidirectional scan with the proposed Hierarchical Bi-directional State Scan (HiBiSS) that aligns recurrence with the axes along which multi-view inconsistencies are strongest. Finally, we design an SE(3) Multi-view Critic that judges whether a set of self-renders arises from a single underlying 3D configuration, rewarding cross-view pixel alignment without observing real multi-view pairs. MVCHead achieves state-of-the-art perceptual quality, surpasses prior methods in both texture and geometric consistency, and maintains comparable shape consistency. To demonstrate scalability, we release FaceGS-10K, the first large-scale dataset of ready-to-use 3D Gaussian head assets for training and evaluation of 3D head models. Project Page and code: https://humansensinglab.github.io/MVCHead/

  </details>

- **[COSY: Compositional 3DGS Synthesis for Disentangled Human Head Editing](https://arxiv.org/abs/2605.24114)**  
  *Florian Barthel, Shalini De Mello, Koki Nagano, Wieland Morgenstern, Anna Hilsmann, Peter Eisert*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.24114) · [pdf](https://arxiv.org/pdf/2605.24114.pdf)
  > 💡 针对3DGS头部编辑中语义属性解耦难的问题，用独立成分合成与上下文token实现精准解耦编辑。

  <details><summary>Abstract</summary>

  Recent 3D Gaussian Splatting (3DGS) GANs for human heads synthesize and render photorealistic 3D models in real-time and offer a vast variety in identity and appearance. However, controlling specific semantic attributes such as hair color or glasses remains challenging, as edits in the entangled latent space often induce unintended changes in identity or appearance. Although there are several methods that aim to disentangle the latent space post training by estimating directions that only modify certain features, these methods cannot guarantee complete disentanglement and often require pre-trained classifiers. In our approach, we propose a new generator architecture that synthesizes components, such as hair, skin, glasses, and torso, completely independently. This allows for changing the latent vector for one region while keeping the remaining parts fixed. Further, we achieve this separation using only sparse information such as the hair or skin color, eliminating the requirement of segmentation masks or geometric priors, often seen in prior work. To ensure matching shape and lighting conditions during editing, we allow minimal shared information via context tokens between the independent generators. These tokens even allow us to control the shape and light, without any prior annotation. Compared to existing works on GAN-based generation and editing, our method shows better disentanglement, more precise editing control, and competitive visual quality.

  </details>

- **[ForeSplat: Optimization-Aware Foresight for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.22020)**  
  *Yuke Li, Weihang Liu, Cheng Zhang, Yuefeng Zhang, Jiadi Cui, Zixuan Wang, Junran Ding, Haoyu Wu, Yujiao Shi, Jingyi Yu, Xin Lou*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22020) · [pdf](https://arxiv.org/pdf/2605.22020.pdf)
  > 💡 用MetaGrad优化感知训练使前馈3DGS生成适于快速优化的初始化，缩小了与逐个场景优化的差距。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting models offer fast single-pass reconstruction,but scaling them to match per-scene optimization quality is fundamentally hindered by the scarcity of large-scale 3D annotations. A practical compromise is predict-then-refine,where post-prediction optimization compensates for the limited capacity of the feed-forward network. However,standard feed-forward 3DGS is trained solely for zero-step rendering error,ignoring whether its output constitutes a good initialization for the downstream optimizer. We present ForeSplat,an optimization-aware training framework that equips feed-forward 3DGS models to produce initializations explicitly designed for rapid,effective refinement. By offloading part of the scene-modeling burden to the optimizer,ForeSplat substantially reduces the capacity pressure on the feed-forward model,making high-quality reconstruction feasible even with compact networks. At its core is MetaGrad,a lightweight multi-anchor meta-gradient training rule that bypasses costly higher-order differentiation through the 3DGS optimizer. MetaGrad unrolls a short inner-loop refinement trajectory,samples anchor states,and back-propagates aggregated first-order gradients to the prediction head as a surrogate optimization-aware signal. This fine-tuning adds no inference cost and enables high-quality reconstruction within seconds after a few refinement steps. We instantiate ForeSplat on diverse backbones,including AnySplat,Pi3X,and a distilled variant tailored for edge deployment. Across all tested architectures,a ForeSplat-trained initialization converges in fewer refinement steps and reaches a higher peak reconstruction quality than its vanilla counterpart,even fully converged. The framework consistently bridges the gap between amortized prediction and per-scene optimization,establishing a practical path toward lightweight,high-fidelity 3D reconstruction.

  </details>

- **[GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](https://arxiv.org/abs/2605.20752)**  
  *Zijian Zhang, Yuqing Jiang, Qian Cheng, Xiaofan Li, Si Liu, Ding Zhao, Ping Luo, Weitao Zhou, Haibao Yu*  
  `2026-05-20` · `cs.RO` · [abs](https://arxiv.org/abs/2605.20752) · [pdf](https://arxiv.org/pdf/2605.20752.pdf)
  > 💡 针对VLA策略缺乏3D空间与未来演化建模，提出前馈3D高斯

  <details><summary>Abstract</summary>

  Vision-language-action (VLA) policies have advanced language-conditioned robotic manipulation by transferring semantic priors from pretrained vision-language models to action generation. However, standard action-imitation learning often lacks sufficient modeling of explicit 3D spatial information, dense geometric supervision, and future environment evolution, all critical for precise robotic interaction. To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in. Specifically, we introduce learnable GaussianDream Queries in the encoder, enabling the model to capture current-frame 3D spatial structure and short-horizon future evolution. During training, the latent GaussianDream prefix is processed by a static reconstruction head and a future prediction head to produce current 3D Gaussian scene states and future Gaussian evolution states. The current branch is supervised by RGB rendering and depth, while the future branch uses future RGB, depth, and pseudo 3D scene-flow signals. During inference, GaussianDream discards all auxiliary heads and retains only the learned prefix to condition action generation, without test-time Gaussian reconstruction or future prediction. Experimental results demonstrate that GaussianDream achieves state-of-the-art performance across multiple robotic manipulation benchmarks, reaching \textbf{98.4\%} on LIBERO, \textbf{54.8\%} on RoboCasa Human-50, and \textbf{50.0\%} on real-robot tasks. Compared with existing 3D-enhanced VLA methods, GaussianDream achieves strong accuracy while providing higher inference efficiency than video-based world-model approaches.

  </details>

- **[FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model](https://arxiv.org/abs/2605.19600)**  
  *Jinhan Li, Xijie Huang, Zhaoqi Wang, Yijin Wang, Weiqi Ge, Qiyi He, Mo Zhu, Fei Gao, Yuze Wu, Xin Zhou*  
  `2026-05-19` · `cs.RO` · [abs](https://arxiv.org/abs/2605.19600) · [pdf](https://arxiv.org/pdf/2605.19600.pdf)
  > 💡 采用LLM设计环境与3D高斯溅射生成世界模型，自动化生成多样可扩展的高保真无人机飞行数据。

  <details><summary>Abstract</summary>

  In the field of Vision-Language Navigation (VLN), aerial datasets remain limited in their ability to combine scale, diversity, and realism, often relying on either costly real-world scenes or visually limited simulations. To address these challenges, we introduce FlyMirage, a highly scalable and fully automated data generation pipeline for aerial VLN. Our approach leverages large language models (LLM) as an environment designer to promote scene diversity, paired with a generative world model that instantiates these designs into high-fidelity 3D Gaussian Splatting (3DGS) scenes. To substantially reduce human labor and ensure the feasibility of flight data, FlyMirage automates scene exploration and semantic information acquisition, and further integrates a dynamically feasible planner for uncrewed aerial vehicle (UAV) trajectory generation. Utilizing this toolchain, we generate a large-scale, diverse, and photorealistic aerial VLN dataset, with dynamically feasible flying trajectories, designed to support the development of next-generation embodied navigation models.

  </details>

- **[3D Skew Gaussian Splatting with Any Camera Trajectory Visualization Engine](https://arxiv.org/abs/2605.18334)**  
  *Beizhen Zhao, Yifan Zhou, Gaochao Song, Ziran Yin, Hao Wang*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18334) · [pdf](https://arxiv.org/pdf/2605.18334.pdf)
  > 💡 针对对称高斯分布导致视觉伪影的问题，提出3D偏斜高斯泼洒，通过非

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) has revolutionized real-time photorealistic view synthesis, its fundamental reliance on symmetric Gaussian distributions introduces visual artifacts that hinder accurate spatial data exploration. Specifically, symmetric kernels struggle to capture shape and color discontinuities , which cause blurriness and primitive redundancy that mislead human perception during visual analysis. To address these visualization barriers, we introduce 3D Skew Gaussian Splatting (3DSGS), a novel framework that significantly enhances the structural fidelity and compactness of explicit scene representations. Our key insight lies in extending the standard primitive to a general Skew Gaussian counterpart. This generalized primitive inherits the highly efficient rasterization properties of standard Gaussians while gaining intrinsic asymmetric modeling capabilities. We couple this with an enhanced opacity representation to better handle complex transparency, alongside a depth-aware densification strategy that intelligently manages primitive allocation. Furthermore, to make these advancements actionable for real-world visual analytics, we re-derive the CUDA rasterization pipeline to universally support both symmetric and skew Gaussians, integrating it into a decoupled, free-camera interactive visualization engine. Extensive experiments demonstrate that 3DSGS achieves superior rendering quality and structural compactness, particularly in regions with intricate details, while maintaining the real-time frame rates necessary for fluid interactive exploration. Supplementary derivations and visual results are available at \textbf{\textit{https://3d-skew-gs.github.io/}}.

  </details>

- **[Towards Accurate Single Panoramic 3D Detection: A Semantic Gaussian Centric Approach](https://arxiv.org/abs/2605.14601)**  
  *Kanglin Ning, Yiran Zhao, Wenrui Li, Shaoru Sun, Xingtao Wang, Xiaopeng Fan*  
  `2026-05-14` · `cs.CV` · [abs](https://arxiv.org/abs/2605.14601) · [pdf](https://arxiv.org/pdf/2605.14601.pdf)
  > 💡 针对全景3D检测中离散网格几何不连续问题，提出

  <details><summary>Abstract</summary>

  Three-dimensional object detection in panoramic imagery is crucial for comprehensive scene understanding, yet accurately mapping 2D features to 3D remains a significant challenge. Prevailing methods often project 2D features onto discrete 3D grids, which break geometric continuity and limit representation efficiency. To overcome this limitation, this paper proposes PanoGSDet, a monocular panoramic 3D detection framework built upon continuous semantic 3D Gaussian representations. The proposed framework comprises a panoramic depth estimation component and a semantic Gaussian component. The panoramic depth estimation component extracts the equirectangular semantic and depth features from the monocular panorama input. The semantic Gaussian component includes a semantic Gaussian lifting module that projects spherical features into 3D semantic Gaussians, a semantic Gaussian optimization module that refines these semantic Gaussians, and a Gaussian guided prediction head that generates 3D bounding boxes from optimized Gaussian representations. Extensive experiments on the Structured3D dataset demonstrate that our method significantly outperforms existing methods.

  </details>

- **[Forecast-aware Gaussian Splatting for Predictive 3D Representation in Language-Guided Pick-and-Place Manipulation](https://arxiv.org/abs/2605.11144)**  
  *Kaixin Jia, Jiacheng Xu*  
  `2026-05-11` · `cs.RO` · [abs](https://arxiv.org/abs/2605.11144) · [pdf](https://arxiv.org/pdf/2605.11144.pdf)
  > 💡 提出预测性三维高斯泼溅框架，显式建模任务完成状态，提升语言引导拾放操作成功率。

  <details><summary>Abstract</summary>

  We introduce Forecast-aware Gaussian Splatting (Forecast-GS), a predictive 3D representation framework for language-conditioned robotic manipulation. While recent manipulation systems have made progress by grounding language instructions into robot affordances, value maps, or relational keypoint constraints, they usually reason over the current scene and do not explicitly model the task-completed state. This limitation is critical when success depends on satisfying spatial and semantic goals under partial observations, where the robot must evaluate whether a candidate action leads to a feasible task-consistent outcome. We validate Forecast-GS on real-world pick-and-place manipulation tasks, including Cutter-to-Box, Apple-to-Bowl, and Sponge-to-Tray. For each task, we conduct 25 real-world trials under varied initial object configurations using the same robot platform and sensing setup. Forecast-GS with automatic candidate selection achieves success rates of 21/25, 23/25, and 16/25 on the three tasks, respectively, outperforming the ReKep baseline, which achieves 15/25, 19/25, and 10/25. A diagnostic human-assisted setting further improves success rates to 23/25, 24/25, and 19/25, suggesting that candidate generation is effective while automatic ranking remains imperfect. These results suggest that explicitly forecasting task-completed 3D states enables more reliable action evaluation, while the gap between automatic and human-assisted selection indicates that robust final-state ranking remains an important challenge for fully autonomous manipulation. Overall, Forecast-GS provides an interpretable bridge between language understanding, 3D perception, and robotic manipulation planning.

  </details>

- **[SDTalk: Structured Facial Priors and Dual-Branch Motion Fields for Generalizable Gaussian Talking Head Synthesis](https://arxiv.org/abs/2605.09956)**  
  *Peng Jia, Zhen Xiao, Jia Li, Xueliang Liu, Zhenzhen Hu, Lingyun Yu*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09956) · [pdf](https://arxiv.org/pdf/2605.09956.pdf)
  > 💡 提出SDTalk，利用结构化面部先验和双分支运动场实现单图像3DGS泛化说话头合成，无需个性化训练。

  <details><summary>Abstract</summary>

  High-quality, real-time talking head synthesis remains a fundamental challenge in computer vision. Existing reconstruction- and rendering-based methods typically rely on identity-specific models, limiting cross-identity generalization. To address this issue, we propose SDTalk, a one-shot 3D Gaussian Splatting (3DGS)-based framework that generalizes to unseen identities without personalized training or fine-tuning. Our framework comprises two modules with a two-stage training strategy. In the first stage, we incorporate structured facial priors into the reconstruction module and separately predict 3DGS parameters for visible and occluded regions, enabling complete head reconstruction from a single image. In the second stage, we introduce a dual-branch motion field to model coarse and fine facial dynamics, improving detail fidelity and lip synchronization. Experiments demonstrate that SDTalk surpasses existing methods in both visual quality and inference efficiency.

  </details>

- **[REAP: Reinforcement-Learning End-to-End Autonomous Parking with Gaussian Splatting Simulator for Real2Sim2Real Transfer](https://arxiv.org/abs/2605.08713)**  
  *Changze Li, Zhe Chen, Shaoyu Chen, Lisen Mu, Yijian Li, Yuelong Yu, Qian Zhang, Qing Su, Ming Yang, Tong Qin*  
  `2026-05-09` · `cs.RO` · [abs](https://arxiv.org/abs/2605.08713) · [pdf](https://arxiv.org/pdf/2605.08713.pdf)
  > 💡 提出REAP端到端自动泊车方法，结合SAC强化学习与3DGS仿真器，通过行为克隆和碰撞惩罚实现Real2Sim2Real迁移并提升极端场景性能。

  <details><summary>Abstract</summary>

  In recent years, autonomous parking has made significant advances, yet parking tasks still face challenges in extreme scenarios such as mechanical and dead-end parking slots, often resulting in failures. This is mainly due to traditional parking methods adopting a multistage approach, lacking the ability to optimize the parking problem as a whole. End-to-end methods enable joint optimization across perception and planning modules to eliminate the accumulation of errors, enhancing algorithm performance in extreme scenarios. Although several end-to-end parking methods use imitation or reinforcement learning, the former is limited by data cost and distribution coverage, while the latter suffers from inefficient exploration. To address these challenges, we propose a Reinforcement learning End-to-end Autonomous Parking method (REAP). REAP employs Soft Actor-Critic (SAC) within an asymmetric reinforcement learning framework to improve training efficiency and inference performance. To accelerate model convergence, we distill the capabilities of a rule-based planner into the end-to-end network through behavior cloning. We further introduce a soft predictive collision penalty mechanism to reduce collision rates by penalizing obstacle-approaching actions. To ensure that the trained reinforcement learning network can directly transfer to real-world scenarios, we have established a Real2Sim2Real simulator. In the Real2Sim step, we use 3D Gaussian Splatting (3DGS) to transform real-world scenes into digital scenes. In the Sim2Real step, we deploy the end-to-end model onto the vehicle to bridge the Sim2Real gap. Trained in the 3DGS simulator and deployed on physical vehicles, REAP successfully parks in various types of parking spaces, especially demonstrating the feasibility of end-to-end RL parking in extremely narrow mechanical slots.

  </details>

- **[Large-Scale High-Quality 3D Gaussian Head Reconstruction from Multi-View Captures](https://arxiv.org/abs/2605.04035)**  
  *Evangelos Ntavelis, Sean Wu, Mohamad Shahbazi, Fabio Maninchedda, Dmitry Kostiaev, Artem Sevastopolsky, Vittorio Megaro, Trevor Phillips, Alejandro Blumentals, Shridhar Ravikumar, Mehak Gupta, Reinhard Knothe, Jeronimo Bayer, Matthias Vestner, Simon Schaefer, Thomas Etterlin, Christian Zimmermann, Mathias Deschler, Peter Kaufmann, Stefan Brugger, Sebastian Martin, Brian Amberg, Tom Runia*  
  `2026-05-05` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04035) · [pdf](https://arxiv.org/pdf/2605.04035.pdf)
  > 💡 提出HeadsUp，用编码器-解码器与UV参数化高斯，从多视角捕获大规模重建高质量3D头部，在万级数据集上达SOTA并泛化。

  <details><summary>Abstract</summary>

  We propose HeadsUp, a scalable feed-forward method for reconstructing high-quality 3D Gaussian heads from large-scale multi-camera setups. Our method employs an efficient encoder-decoder architecture that compresses input views into a compact latent representation. This latent representation is then decoded into a set of UV-parameterized 3D Gaussians anchored to a neutral head template. This UV representation decouples the number of 3D Gaussians from the number and resolution of input images, enabling training with many high-resolution input views. We train and evaluate our model on an internal dataset with more than 10,000 subjects, which is an order of magnitude larger than existing multi-view human head datasets. HeadsUp achieves state-of-the-art reconstruction quality and generalizes to novel identities without test-time optimization. We extensively analyze the scaling behavior of our model across identities, views, and model capacity, revealing practical insights for quality-compute trade-offs. Finally, we highlight the strength of our latent space by showcasing two downstream applications: generating novel 3D identities and animating the 3D heads with expression blendshapes.

  </details>

- **[HumanSplatHMR: Closing the Loop Between Human Mesh Recovery and Gaussian Splatting Avatar](https://arxiv.org/abs/2605.02784)**  
  *Yeheng Zong, Pou-Chun Kung, Yike Pan, Seth Isaacson, Yizhou Chen, Ram Vasudevan, Katherine A. Skinner*  
  `2026-05-04` · `cs.CV` · [abs](https://arxiv.org/abs/2605.02784) · [pdf](https://arxiv.org/pdf/2605.02784.pdf)
  > 💡 人体姿态恢复和虚拟形象渲染分离导致几何不准确，提出HumanSplatHMR通过闭环优化联合细化姿态并学习高保真虚拟形象。

  <details><summary>Abstract</summary>

  Accurately recovering human pose and appearance from video is an essential component of scene reconstruction, with applications to motion capture, motion prediction, virtual reality, and digital twinning. Despite significant interest in building realistic human avatars from video, this paper demonstrates that existing methods do not accurately recover the 3D geometry of humans. ViT-based approaches are not consistently reliable and can overfit to 2D views, while NeRF- and Gaussian Splatting-based avatars treat pose and appearance separately, limiting rendering generalization to new poses. To resolve these shortcomings, this paper proposes HumanSplatHMR, a joint optimization framework that refines 3D human poses while simultaneously learning a high-fidelity avatar for novel-view and novel-pose synthesis. Our key insight is to close the loop between geometric pose estimation and differentiable rendering. Unlike prior human avatar methods that rely on accurate human pose obtained through motion capture systems or offline refinement, which are impractical in in-the-wild scenarios, our approach uses only human mesh estimates from a state-of-the-art human pose estimator to better reflect real-world conditions. Therefore, instead of using the human pose only as a deformation prior, HumanSplatHMR backpropagates photometric, segmentation, and depth losses through a differentiable renderer to the pose parameters and global position. This coupling refines the global 3D pose over time, improving accuracy and alignment while producing better renderings from novel views. Experiments show consistent improvements over pose recovery baselines that omit image-level refinement and avatar baselines that decouple pose estimation from avatar reconstruction.

  </details>

- **[GETA-3DGS: Automatic Joint Structured Pruning and Quantization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.02086)**  
  *Baobing Zhang, Wanxin Sui*  
  `2026-05-03` · `cs.LG` · [abs](https://arxiv.org/abs/2605.02086) · [pdf](https://arxiv.org/pdf/2605.02086.pdf)
  > 💡 针对3DGS压缩中手工阈值与分阶段短板，提出端到端联合结构化剪枝与量化框架GETA-3DGS，利用QADG、渲染感知显著性及异构混合精度实现自动压缩。

  <details><summary>Abstract</summary>

  3D Gaussian splatting (3DGS) is a state-of-the-art representation for real-time photorealistic novel-view synthesis, yet a single high-fidelity scene typically occupies hundreds of megabytes to several gigabytes, exceeding the budgets of mobile, immersive, and volumetric video platforms. Existing 3DGS compression methods (e.g., HAC++, FlexGaussian, LP-3DGS) treat pruning, quantization, and entropy coding as separate stages and rely on hand-tuned heuristics (opacity thresholds, fixed bit-widths, SH truncation), limiting cross-scene generalization and preventing users from specifying a target rate or quality budget. We propose GETA-3DGS, to our knowledge the first end-to-end automatic joint structured pruning and quantization framework for 3DGS. Building on GETA for joint pruning-quantization of deep networks, we contribute: (i) a 3DGS-aware quantization-aware dependency graph (QADG) treating each Gaussian primitive as a group with five attribute sub-nodes and degree-aware SH sub-nodes; (ii) a render-aware saliency fusing transmittance-weighted contribution, screen-space gradient, and pixel coverage into a Gaussian-level importance score; and (iii) a heterogeneous per-attribute mixed-precision scheme co-optimized with structural sparsity under a projected partial saliency-guided (PPSG) descent guarantee. On Mip-NeRF 360, Tanks and Temples, and Deep Blending, GETA-3DGS operates directly on raw Gaussian primitives rather than a post-hoc anchor representation, delivering ~5x storage reduction over Vanilla 3DGS with no per-scene thresholds. Bit-width policy is the dominant rate-distortion lever: a uniform 6-bit cap costs up to -6.74 dB on view-dependent scenes versus our heterogeneous allocation, matching an information-theoretic reverse-water-filling analysis we develop. GETA-3DGS is complementary to existing codecs: entropy coding (HAC++, CompGS) is downstream, so the two can be composed.

  </details>

- **[Semantic Foam: Unifying Spatial and Semantic Scene Decomposition](https://arxiv.org/abs/2604.26262)**  
  *Amr Sharafeldin, Shrisudhan Govindarajan, Thomas Walker, Aryan Mikaeili, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26262) · [pdf](https://arxiv.org/pdf/2604.26262.pdf)
  > 💡 提出基于Voronoi网格和显式语义特征场的语义分解方法，通过空间正则化提升分割一致性，优于现有技术。

  <details><summary>Abstract</summary>

  Modern scene reconstruction methods, such as 3D Gaussian Splatting, deliver photo-realistic novel view synthesis at real-time speeds, yet their adoption in interactive graphics applications has been limited. A major bottleneck is the difficulty of interacting with these representations compared to traditional, human-authored 3D assets. While previous research has attempted to impose semantic decomposition on these models, significant challenges remain regarding segmentation quality and consistency. To address this, we introduce Semantic Foam, extending the recently proposed Radiant Foam representations to semantic decomposition tasks. Our approach integrates the natural spatial volumetric decomposition of Radiant Foam's Voronoi mesh with an explicit semantic feature field parameterized at the cell level. This explicit structure enables direct spatial regularization, which prevents artifacts caused by occlusion or inconsistent supervision across views - common pitfalls for other point-based representations. Experimental results show that our method achieves superior object-level segmentation performance compared to state-of-the-art methods like Gaussian Grouping and SAGA.

  </details>

- **[Light 'em Up: Enabling Few-Shot Low-Light 3D Gaussian Splatting with Multi-Scale Explicit Retinex Illumination Decoupling](https://arxiv.org/abs/2604.24053)**  
  *YuHao Yin, Zongji Wang, Yuanben Zhang, Biqing Li, Jiesong Bai, Junyi Liu*  
  `2026-04-27` · `cs.CV` · [abs](https://arxiv.org/abs/2604.24053) · [pdf](https://arxiv.org/pdf/2604.24053.pdf)
  > 💡 针对低光360度新视图合成问题，提出MERID-GS框架，通过多尺度显式Retinex光照解

  <details><summary>Abstract</summary>

  Full 360$^\circ$ novel view synthesis under low-light conditions remains challenging. Insufficient illumination, noise amplification, and view-dependent photometric inconsistencies prevent existing methods from jointly preserving geometric consistency and photorealism. Unsupervised approaches often exhibit color drift under large viewpoint variations, while supervised low-light enhancement models, though effective for 2D tasks, struggle to generalize to new scenes and typically require retraining. To address this issue, we propose MERID-GS, a Multi-Scale Explicit Retinex Illumination-Decoupled Gaussian framework for low-light 360$^\circ$ synthesis. Based on Retinex theory, the method explicitly separates illumination and reflectance, and suppresses noise propagation while enhancing dark-region structures via a learnable gain and Illumination-State-Guided Frequency Gating. Combined with lightweight Reflection Head and 3D Gaussian Splatting, MERID-GS adapts to new scenes with only a few shots and enables stable low-light novel view synthesis from sparse-view observations. In addition, we construct a low-light multi-view dataset covering full 360$^\circ$ scenes for joint evaluation. Thorough experiments across multiple datasets in this area demonstrate that MERID-GS achieves SOTA performance, exhibiting superior cross-scene generalization and view consistency. The source code and pre-trained models are available at https://github.com/YhuoyuH/MERID-GS..

  </details>

- **[DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures](https://arxiv.org/abs/2604.21631)**  
  *Xu Wang, Zhiru Wang, Shiyun Xie, Chengwei Pan, Yisong Chen*  
  `2026-04-23` · `cs.CV` · [abs](https://arxiv.org/abs/2604.21631) · [pdf](https://arxiv.org/pdf/2604.21631.pdf)
  > 💡 利用重建失败生成伪掩码引导二次优化，解决3DGS在瞬态物体干扰下的性能退化问题，效果显著。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) achieves real-time photorealistic rendering, its performance degrades significantly when training images contain transient objects that violate multi-view consistency. Existing methods face a circular dependency: accurate transient detection requires a well-reconstructed static scene, while clean reconstruction itself depends on reliable transient masks. We address this challenge with DualSplat, a Failure-to-Prior framework that converts first-pass reconstruction failures into explicit priors for a second reconstruction stage. We observe that transients, which appear in only a subset of views, often manifest as incomplete fragments during conservative initial training. We exploit these failures to construct object-level pseudo-masks by combining photometric residuals, feature mismatches, and SAM2 instance boundaries. These pseudo-masks then guide a clean second-pass 3DGS optimization, while a lightweight MLP refines them online by gradually shifting from prior supervision to self-consistency. Experiments on RobustNeRF and NeRF On-the-go show that DualSplat outperforms existing baselines, demonstrating particularly clear advantages in transient-heavy scenes and transient regions.

  </details>

- **[SketchFaceGS: Real-Time Sketch-Driven Face Editing and Generation with Gaussian Splatting](https://arxiv.org/abs/2604.19202)**  
  *Bo Li, Jiahao Kang, Yubo Ma, Feng-Lin Liu, Bin Liu, Fang-Lue Zhang, Lin Gao*  
  `2026-04-21` · `cs.GR` · [abs](https://arxiv.org/abs/2604.19202) · [pdf](https://arxiv.org/pdf/2604.19202.pdf)
  > 💡 针对草图生成与编辑3D高斯人头困难，提出粗到细架构与UV特征增强，实现实时高保真编辑。

  <details><summary>Abstract</summary>

  3D Gaussian representations have emerged as a powerful paradigm for digital head modeling, achieving photorealistic quality with real-time rendering. However, intuitive and interactive creation or editing of 3D Gaussian head models remains challenging. Although 2D sketches provide an ideal interaction modality for fast, intuitive conceptual design, they are sparse, depth-ambiguous, and lack high-frequency appearance cues, making it difficult to infer dense, geometrically consistent 3D Gaussian structures from strokes - especially under real-time constraints. To address these challenges, we propose SketchFaceGS, the first sketch-driven framework for real-time generation and editing of photorealistic 3D Gaussian head models from 2D sketches. Our method uses a feed-forward, coarse-to-fine architecture. A Transformer-based UV feature-prediction module first reconstructs a coarse but geometrically consistent UV feature map from the input sketch, and then a 3D UV feature enhancement module refines it with high-frequency, photorealistic detail to produce a high-fidelity 3D head. For editing, we introduce a UV Mask Fusion technique combined with a layer-by-layer feature-fusion strategy, enabling precise, real-time, free-viewpoint modifications. Extensive experiments show that SketchFaceGS outperforms existing methods in both generation fidelity and editing flexibility, producing high-quality, editable 3D heads from sketches in a single forward pass.

  </details>

- **[CLOTH-HUGS: Cloth Aware Human Gaussian Splatting](https://arxiv.org/abs/2604.15875)**  
  *Sadia Mubashshira, Nazanin Amini, Kevin Desai*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15875) · [pdf](https://arxiv.org/pdf/2604.15875.pdf)
  > 💡 提出基于高斯泼溅的神经渲染框架，用分离的身体和衣物高斯层解耦重建，通过物理约束提升衣物真实感，实现高质量

  <details><summary>Abstract</summary>

  We present Cloth-HUGS, a Gaussian Splatting based neural rendering framework for photorealistic clothed human reconstruction that explicitly disentangles body and clothing. Unlike prior methods that absorb clothing into a single body representation and struggle with loose garments and complex deformations, Cloth-HUGS represents the performer using separate Gaussian layers for body and cloth within a shared canonical space. The canonical volume jointly encodes body, cloth, and scene primitives and is deformed through SMPL-driven articulation with learned linear blend skinning weights. To improve cloth realism, we initialize cloth Gaussians from mesh topology and apply physics-inspired constraints, including simulation-consistency, ARAP regularization, and mask supervision. We further introduce a depth-aware multi-pass rendering strategy for robust body-cloth-scene compositing, enabling real-time rendering at over 60 FPS. Experiments on multiple benchmarks show that Cloth-HUGS improves perceptual quality and geometric fidelity over state-of-the-art baselines, reducing LPIPS by up to 28% while producing temporally coherent cloth dynamics.

  </details>

- **[Any3DAvatar: Fast and High-Quality Full-Head 3D Avatar Reconstruction from Single Portrait Image](https://arxiv.org/abs/2604.13856)**  
  *Yujie Gao, Yao Xiao, Xiangnan Zhu, Ya Li, Yiyi Zhang, Liqing Zhang, Jianfu Zhang*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13856) · [pdf](https://arxiv.org/pdf/2604.13856.pdf)
  > 💡 使用统一数据集和Plücker感知结构化高斯支架，一步去噪生成完整3D头部头像，兼顾速度与高保真外观。

  <details><summary>Abstract</summary>

  Reconstructing a complete 3D head from a single portrait remains challenging because existing methods still face a sharp quality-speed trade-off: high-fidelity pipelines often rely on multi-stage processing and per-subject optimization, while fast feed-forward models struggle with complete geometry and fine appearance details. To bridge this gap, we propose Any3DAvatar, a fast and high-quality method for single-image 3D Gaussian head avatar generation, whose fastest setting reconstructs a full head in under one second while preserving high-fidelity geometry and texture. First, we build AnyHead, a unified data suite that combines identity diversity, dense multi-view supervision, and realistic accessories, filling the main gaps of existing head data in coverage, full-head geometry, and complex appearance. Second, rather than sampling unstructured noise, we initialize from a Plücker-aware structured 3D Gaussian scaffold and perform one-step conditional denoising, formulating full-head reconstruction into a single forward pass while retaining high fidelity. Third, we introduce auxiliary view-conditioned appearance supervision on the same latent tokens alongside 3D Gaussian reconstruction, improving novel-view texture details at zero extra inference cost. Experiments show that Any3DAvatar outperforms prior single-image full-head reconstruction methods in rendering fidelity while remaining substantially faster.

  </details>

- **[3DRealHead: Few-Shot Detailed Head Avatar](https://arxiv.org/abs/2604.13171)**  
  *Jalees Nehvi, Timo Bolkart, Thabo Beeler, Justus Thies*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13171) · [pdf](https://arxiv.org/pdf/2604.13171.pdf)
  > 💡 针对头部身份和表情细节缺失问题，提出基于Style U-Net发射3D高斯原语、融合3DMM与

  <details><summary>Abstract</summary>

  The human face is central to communication. For immersive applications, the digital presence of a person should mirror the physical reality, capturing the users idiosyncrasies and detailed facial expressions. However, current 3D head avatar methods often struggle to faithfully reproduce the identity and facial expressions, despite having multi-view data or learned priors. Learning priors that capture the diversity of human appearances, especially, for regions with highly person-specific features, like the mouth and teeth region is challenging as the underlying training data is limited. In addition, many of the avatar methods are purely relying on 3D morphable model-based expression control which strongly limits expressivity. To address these challenges, we are introducing 3DRealHead, a few-shot head avatar reconstruction method with a novel expression control signal that is extracted from a monocular video stream of the subject. Specifically, the subject can take a few pictures of themselves, recover a 3D head avatar and drive it with a consumer-level webcam. The avatar reconstruction is enabled via a novel few-shot inversion process of a 3D human head prior which is represented as a Style U-Net that emits 3D Gaussian primitives which can be rendered under novel views. The prior is learned on the NeRSemble dataset. For animating the avatar, the U-Net is conditioned on 3DMM-based facial expression signals, as well as features of the mouth region extracted from the driving video. These additional mouth features allow us to recover facial expressions that cannot be represented by the 3DMM leading to a higher expressivity and closer resemblance to the physical reality.

  </details>

- **[ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation](https://arxiv.org/abs/2604.11138)**  
  *Arjun Bhardwaj, Maximum Wilder-Smith, Mayank Mittal, Vaishakh Patil, Marco Hutter*  
  `2026-04-13` · `cs.RO` · [abs](https://arxiv.org/abs/2604.11138) · [pdf](https://arxiv.org/pdf/2604.11138.pdf)
  > 💡 利用3D高斯溅射实现视觉域随机化，单目RGB手中重定向训练，成本低且鲁棒。

  <details><summary>Abstract</summary>

  In-hand object reorientation requires precise estimation of the object pose to handle complex task dynamics. While RGB sensing offers rich semantic cues for pose tracking, existing solutions rely on multi-camera setups or costly ray tracing. We present a sim-to-real framework for monocular RGB in-hand reorientation that integrates 3D Gaussian Splatting (3DGS) to bridge the visual sim-to-real gap. Our key insight is performing domain randomization in the Gaussian representation space: by applying physically consistent, pre-rendering augmentations to 3D Gaussians, we generate photorealistic, randomized visual data for object pose estimation. The manipulation policy is trained using curriculum-based reinforcement learning with teacher-student distillation, enabling efficient learning of complex behaviors. Importantly, both perception and control models can be trained independently on consumer-grade hardware, eliminating the need for large compute clusters. Experiments show that the pose estimator trained with 3DGS data outperforms those trained using conventional rendering data in challenging visual environments. We validate the system on a physical multi-fingered hand equipped with an RGB camera, demonstrating robust reorientation of five diverse objects even under challenging lighting conditions. Our results highlight Gaussian splatting as a practical path for RGB-only dexterous manipulation. For videos of the hardware deployments and additional supplementary materials, please refer to the project website: https://rffr.leggedrobotics.com/works/viserdex/

  </details>

- **[Real-Time Human Reconstruction and Animation using Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2604.10259)**  
  *Devdoot Chatterjee, Zakaria Laskar, C. V. Jawahar*  
  `2026-04-11` · `cs.CV` · [abs](https://arxiv.org/abs/2604.10259) · [pdf](https://arxiv.org/pdf/2604.10259.pdf)
  > 💡 提出前馈高斯溅射框架，通过将高斯原语与SMPL-X顶点关联，实现单次前馈下的实时人体重建与动画。

  <details><summary>Abstract</summary>

  We present a generalizable feed-forward Gaussian splatting framework for human 3D reconstruction and real-time animation that operates directly on multi-view RGB images and their associated SMPL-X poses. Unlike prior methods that rely on depth supervision, fixed input views, UV map, or repeated feed-forward inference for each target view or pose, our approach predicts, in a canonical pose, a set of 3D Gaussian primitives associated with each SMPL-X vertex. One Gaussian is regularized to remain close to the SMPL-X surface, providing a strong geometric prior and stable correspondence to the parametric body model, while an additional small set of unconstrained Gaussians per vertex allows the representation to capture geometric structures that deviate from the parametric surface, such as clothing and hair. In contrast to recent approaches such as HumanRAM, which require repeated network inference to synthesize novel poses, our method produces an animatable human representation from a single forward pass; by explicitly associating Gaussian primitives with SMPL-X vertices, the reconstructed model can be efficiently animated via linear blend skinning without further network evaluation. We evaluate our method on the THuman 2.1, AvatarReX and THuman 4.0 datasets, where it achieves reconstruction quality comparable to state-of-the-art methods while uniquely supporting real-time animation and interactive applications. Code and pre-trained models are available at https://github.com/Devdoot57/HumanGS .

  </details>

