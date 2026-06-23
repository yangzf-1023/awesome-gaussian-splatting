# Autonomous Driving / Outdoor

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---






## 2026-06-23

- **[Non-line-of-sight imaging with arbitrary relay surface geometries via 3D Gaussian Transient Rendering](https://arxiv.org/abs/2606.21270)**  
  *Yi Wang, Ziyu Zhan, Yuran Wang, Hao Wang, Qiang Liu, Zuoqiang Shi, Lingyun Qiu, Xing Fu*  
  `2026-06-19` · `physics.optics` · [abs](https://arxiv.org/abs/2606.21270) · [pdf](https://arxiv.org/pdf/2606.21270.pdf)
  > 💡 通过3D高斯原语与可微瞬态渲染，解决了非视距成像中任意中继表面几何与稀疏采样下的重建难题。

  <details><summary>Abstract</summary>

  Imaging objects hidden outside the direct line of sight expands the effective field of view and is critical for applications such as autonomous driving and robotic perception. Despite impressive progress in time-of-flight (ToF)-based non-line-of-sight (NLOS) imaging, real-world deployment remains challenging because practical measurements are often collected over spatially limited, arbitrarily shaped relay regions-conditions that violate the planar-wall and dense-sampling assumptions made by most existing methods. To address these limitations, we propose a LOS-guided NLOS imaging pipeline that imposes no geometric assumptions on the relay surface and naturally supports both confocal and non-confocal configurations. Our method represents the hidden scene using 3D Gaussian primitives and couples them with an efficient, differentiable transient rendering model, enabling end-to-end optimization directly from measured transients. We validate our approach on real-world measurements from both a public dataset and a custom-built capture system. Across settings, our method achieves state-of-the-art reconstruction fidelity under spatially limited, sparsely sampled conditions, and significantly outperforms existing methods on complex, arbitrary relay surface geometries.

  </details>

## 2026-06-19

- **[Geometry-Preserving in 3D Gaussian Splatting for LiDAR-Camera Extrinsic Calibration](https://arxiv.org/abs/2606.20103)**  
  *Kyoleen Kwak, Daeho Kim, Jeong Woon Lee, Hyoseok Hwang*  
  `2026-06-18` · `cs.CV` · [abs](https://arxiv.org/abs/2606.20103) · [pdf](https://arxiv.org/pdf/2606.20103.pdf)
  > 💡 针对3DGS标定中几何漂移问题，提出多视图LiDAR深度监督并阻断光度梯度以保留度量几何，提升标定精度。

  <details><summary>Abstract</summary>

  Accurate LiDAR-camera calibration is essential for robust multi-modal perception. Targetless approaches avoid manual setup but remain limited by the scarcity of discriminative cross-modal features. Recent methods address this by reconstructing the scene within a differentiable model, enabling extrinsic optimization through dense photometric supervision. Among these, 3D Gaussian Splatting (3DGS) has been widely adopted as a geometric proxy that bridges LiDAR and camera within a single differentiable framework. However, since 3DGS was originally designed for novel view synthesis, existing methods tend to prioritize rendering quality, causing the proxy geometry to drift from the true LiDAR structure. We propose a framework that preserves the metric geometry of the Gaussian proxy by aggregating multi-view LiDAR observations for dense depth supervision and blocking photometric gradients from updating the Gaussian spatial parameters. We validate our method on public driving datasets, where it consistently outperforms existing targetless methods in calibration accuracy.

  </details>

## 2026-06-18

- **[TerraTransfer: Learning End-to-End Driving Policies Without Expert Demonstrations](https://arxiv.org/abs/2606.17386)**  
  *Zikang Xiong, Weixin Li, Zhouchonghao Wu, Akshay Rangesh, Saarth Bonde, Grantland Hall, Chen Tang, Yihan Hu, Wei Zhan*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17386) · [pdf](https://arxiv.org/pdf/2606.17386.pdf)
  > 💡 提出无需专家演示的端到端驾驶方法，通过自对弈预训练与视觉骨干对齐，降低采集和渲染成本并达到SOTA。

  <details><summary>Abstract</summary>

  End-to-end autonomous driving has achieved state-of-the-art performance on benchmarks and real-world deployments. Its standard training recipe, however, is expensive across all stages: collecting and labeling millions of driving frames is costly, and closed-loop RL on images is bottlenecked by the per-step cost of photorealistic rendering plus a forward pass through a large vision backbone. Self-play in vectorized simulators changes the economics: millions of rollout steps per second, and a state distribution naturally rich in collisions, near-misses, and recoveries that no driving log contains. Our approach exploits this asymmetry by decoupling learning to drive from learning to see. We pretrain a single policy by self-play, then align its latent space with a pretrained vision backbone, through the action KL divergence and a batch-relational low-rank structural loss. The action target comes from the self-play policy, so alignment never supervises against a logged trajectory: a paired dataset of (image, scene-state) frames suffices, with no need for the curated expert demonstrations that imitation pretraining is built on. On photorealistic 3D Gaussian splatting closed-loop scenarios, the resulting end-to-end policy matches or exceeds prior end-to-end methods.

  </details>

## 2026-06-11

- **[A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting](https://arxiv.org/abs/2606.11390)**  
  *Matthew Cong, Francis Williams, Jonathan Swartz, Mark Harris, Sanja Fidler, Ken Museth*  
  `2026-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11390) · [pdf](https://arxiv.org/pdf/2606.11390.pdf)
  > 💡 提出多GPU高斯溅射方法，利用CUDA统一内存和NVLink在算子级别隐藏通信，实现城市场景超10亿高斯块重建，规模提升25倍以上。

  <details><summary>Abstract</summary>

  Gaussian splatting methods have become increasingly popular for neural reconstruction of the real world. However, they are often limited in scale and resolution due to compute and memory constraints. We present a multi-GPU Gaussian splatting approach that scales reconstruction to higher resolutions and larger scenes while abstracting away the code complexity typically associated with distributing a model. To accomplish this, we propose a PyTorch backend that distributes the Gaussian parameters and splatting operators across GPUs via CUDA unified memory and NVLink. Because distribution occurs at the operator level, the model code requires no explicit cross-device communication. More broadly, the backend exposes multiple GPUs as an aggregate PyTorch device and supports other PyTorch operators. We demonstrate city-scale reconstructions with street-level detail consisting of over 1 billion Gaussian splats, more than 25 times as many as the current state of the art.

  </details>

## 2026-06-06

- **[UnsOcc: 3D Semantic Occupancy Prediction in Unstructured Scene via Rendering Fusion](https://arxiv.org/abs/2606.03581)**  
  *Ye Wu, Ruiqi Song, Baiyong Ding, Nanxin Zeng, Junjie Cheng, Yunfeng Ai*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03581) · [pdf](https://arxiv.org/pdf/2606.03581.pdf)
  > 💡 非结构化场景稀疏长尾问题，提出RenderFusion双向渲染融合与GSRefinement高斯泼溅监督，显著提升语义占用预测鲁棒性。

  <details><summary>Abstract</summary>

  Unstructured scenes present unique challenges for autonomous driving, as irregular obstacles and sparse scene layouts undermine the effectiveness of traditional perception methods such as 3D object detection. 3D semantic occupancy prediction has emerged as a prominent focus due to its ability to provide dense spatial representations by assigning semantic labels to individual voxels in 3D space. However, directly applying 3D semantic occupancy prediction to unstructured scenes remains challenging because scene sparsity hinders effective cross-modal fusion and the more severe long-tail distribution in these scenarios further degrades prediction performance. To validate the effectiveness of our approach, we construct a dedicated dataset of unstructured scenes collected from open-pit mines. Based on this, we propose UnsOcc, a multi-modal 3D semantic occupancy prediction framework that improves robustness in unstructured environments. At its core, we introduce a rendering-based fusion module, RenderFusion, which enhances cross-modal feature alignment through bidirectional rendering supervision. Furthermore, we propose GSRefinement, a detail-aware auxiliary supervision method based on Gaussian Splatting that projects sparse 3D occupancy predictions into dense 2D semantic segmentation maps, enabling effective supervision for long-tail categories. Extensive experiments on both the open-pit mine dataset and the nuScenes dataset demonstrate that our method significantly outperforms existing state-of-the-art approaches.

  </details>

## 2026-05-30

- **[Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328)**  
  *Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30328) · [pdf](https://arxiv.org/pdf/2605.30328.pdf)
  > 💡 结合深度估计的单模态热红外高斯泼溅方法，显著提升渲染质量并将训练时间缩减55%。

  <details><summary>Abstract</summary>

  Efficient and robust 3D scene representation is crucial in autonomous driving, robotics, and related fields. While RGB images provide valuable content for 3D reconstruction, other modalities like thermal or depth can enable additional information on the environment. Lately, novel view synthesis methods like 3D Gaussian Splatting have started using multiple modalities to further boost their performance. But fusing or combining multimodal data can make the process slower and can bring in additional challenges. Therefore, our project aims to use single modality based on thermal infrared domain, by removing the reliance on visible light as much as possible. This single modality can be expected to be faster as it does not rely on multimodal data. We propose a method, Thermal-to-Depth Gaussian Splatting (TDg), that uses only thermal images and depth estimation in its architecture to derive the radiance fields. Our TDg method outperforms the MSMG (Multiple Single-Modal Gaussians) baseline in most cases on our test datasets, RGBT-Scenes and ThermalMix. On average, the rendering quality metrics such as learned perceptual image patch similarity (LPIPS), structural similarity index measure (SSIM), and peak signal-to-noise ratio (PSNR) of TDg are 1.12%, 0.034%, and 0.01% better than the baseline MSMG values. It also reduces the training time significantly, by 12 mins 47 secs (55% improvement). Overall, our method is successful in deriving these thermal radiance fields, which can ultimately have several applications, such as identifying heat sources critical in surveillance, search or rescue operations, and industrial inspections where temperature is widely used to monitor machines.

  </details>

- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310)**  
  *Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30310) · [pdf](https://arxiv.org/pdf/2605.30310.pdf)
  > 💡 针对城市尺度多视图图像重建仿真就绪3D网格

  <details><summary>Abstract</summary>

  City-scale 3D surface reconstruction from multiview images for downstream 3D simulation, poses highly challenging problems due to the scale and complexity of urban scenes. Existing city-scale 3D reconstruction methods based on NeRF, Gaussian Splatting etc. often fail to recover 3D meshes ready for simulation due to incomplete/missing geometry and irregular, noisy surfaces. Scaling existing small-scale 3D reconstruction methods to arbitrarily large urban scenes is highly infeasible due to their computational complexity. We present City-Mesh3R, a scalable framework for reconstructing watertight surface meshes directly from large unordered image collections. Unlike recent methods which use global sparse SfM point-cloud initialization followed by a distributed 3D dense reconstruction of large-scale scenes, our method follows an end-to-end images-to-mesh 3D reconstruction approach using a divide-and-conquer strategy. The sparse city map is reconstructed via topological image clustering, cluster-wise independent sparse SfM and map merging, without need for exhaustive image feature matching. Then this map is partitioned spatially to perform geometry-aware camera selection, followed by dense surface reconstruction and surface refinement using curvature-aware adaptive vertex density remeshing. These partition meshes are then stitched together to produce the global mesh of the city. The proposed end-to-end framework is evaluated on city-scale reconstruction datasets. As demonstrated by our qualitative and quantitative results, our proposed method yields high-fidelity watertight 3D meshes with regular geometry, capturing fine surface details, and is suitable for scaling to arbitrarily large scenes owing to the end-to-end processing in a distributed setting.

  </details>

- **[3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation](https://arxiv.org/abs/2605.26500)**  
  *Jianzhe Gao, Rui Liu, Wenguan Wang*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26500) · [pdf](https://arxiv.org/pdf/2605.26500.pdf)
  > 💡 针对VLN场景理解不足，提出3D高斯地图与开放集语义分组及多级动作预测，提升导航泛化能力。

  <details><summary>Abstract</summary>

  Vision-language navigation (VLN) requires an agent to traverse complex 3D environments based on natural language instructions, necessitating a thorough scene understanding. While existing works equip agents with various scene representations to enhance spatial awareness, they often neglect the complex 3D geometry and rich semantics in VLN scenarios, limiting the ability to generalize across diverse and unseen environments. To address these challenges, this work proposes a 3D Gaussian Map that represents the environment as a set of differentiable 3D Gaussians and accordingly develops a navigation strategy for VLN. Specifically, Egocentric Scene Map is constructed online by initializing 3D Gaussians from sparse pseudo-lidar point clouds, providing informative geometric priors for scene understanding. Each Gaussian primitive is further enriched through Open-Set Semantic Grouping operation, which groups 3D Gaussians based on their membership in object instances or stuff categories within the open world, resulting in a unified 3D Gaussian Map. Building on this map, Multi-Level Action Prediction strategy, which combines spatial-semantic cues at multiple granularities, is designed to assist agents in decision-making. Extensive experiments conducted on three public benchmarks (i.e., R2R, R4R, and REVERIE) validate the effectiveness of our method.

  </details>

- **[PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11520)**  
  *Yixiao Song, Qingyong Li, Wen Wang, Zhicheng Yan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11520) · [pdf](https://arxiv.org/pdf/2605.11520.pdf)
  > 💡 用3D高斯溅射桥接离散点云与连续图像的域差距，结合SAM与对比学习实现无监督分割，性能达先进水平。

  <details><summary>Abstract</summary>

  Unsupervised point cloud segmentation is critical for embodied artificial intelligence and autonomous driving, as it mitigates the prohibitive cost of dense point-level annotations required by fully supervised methods. While integrating 2D pre-trained models such as the Segment Anything Model (SAM) to supplement semantic information is a natural choice, this approach faces a fundamental mismatch between discrete 3D points and continuous 2D images. This mismatch leads to inevitable projection overlap and complex modality alignment, resulting in compromised semantic consistency across 2D-3D transfer. To address these limitations, this paper proposes PointGS, a simple yet effective pipeline for unsupervised 3D point cloud segmentation. PointGS leverages 3D Gaussian Splatting as a unified intermediate representation to bridge the discrete-continuous domain gap. Input sparse point clouds are first reconstructed into dense 3D Gaussian spaces via multi-view observations, filling spatial gaps and encoding occlusion relationships to eliminate projection-induced semantic conflation. Multi-view dense images are rendered from the Gaussian space, with 2D semantic masks extracted via SAM, and semantics are distilled to 3D Gaussian primitives through contrastive learning to ensure consistent semantic assignments across different views. The Gaussian space is aligned with the original point cloud via two-step registration, and point semantics are assigned through nearest-neighbor search on labeled Gaussians. Experiments demonstrate that PointGS outperforms state-of-the-art unsupervised methods, achieving +0.9% mIoU on ScanNet-V2 and +2.8% mIoU on S3DIS.

  </details>

- **[UAV-Assisted Scan-to-Simulation for Landslides Using Physics-Informed Gaussian Splatting](https://arxiv.org/abs/2605.10715)**  
  *Zhenyu Liang, Jack C. P. Cheng*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10715) · [pdf](https://arxiv.org/pdf/2605.10715.pdf)
  > 💡 通过无人机倾斜摄影与3DGS重建结合MPM，实现滑坡场景的逼真视觉重建与物理模拟。

  <details><summary>Abstract</summary>

  Landslide monitoring and simulation play an important role in urban safety assessment and disaster prevention. Existing landslide simulation pipelines typically rely on digital elevation model and mesh-based representations, which are suitable for geometric analysis, but often lack visual realism. This limitation reduces their effectiveness in interactive applications, hazard communication, and public education. In this paper, we propose a UAV-based scan-to-simulation framework that bridges photorealistic scene capture and physics-based landslide simulation through 3DGS. Specifically, our pipeline includes four stages: (1) UAV-based acquisition of slope imagery, (2) reconstruction of a low-anisotropy 3DGS scene representation, (3) volumetric conversion of the target simulation region by filling the interior of the surface-based model, and (4) integration with the Material Point Method (MPM) for landslide simulation. We validate the proposed framework on a real landslide site in Hong Kong that experienced a severe landslide event. The results show that our method supports both realistic visual reconstruction and effective simulation.

  </details>

- **[GSDrive: Reinforcing Driving Policies by Multi-mode Future Trajectory Probing with 3D Gaussian Splatting Environment](https://arxiv.org/abs/2604.28111)**  
  *Ziang Guo, Chen Min, Xuefeng Zhang, Yixiao Zhou, Shuo Wang, Sifa Zheng, Dzmitry Tsetserukou, Zufeng Zhang*  
  `2026-04-30` · `cs.RO` · [abs](https://arxiv.org/abs/2604.28111) · [pdf](https://arxiv.org/pdf/2604.28111.pdf)
  > 💡 端到端自动驾驶中强化学习奖励稀疏，采用3DGS环境进行多模态未来轨迹探测与奖励塑形，结合IL-RL循环提升策略性能。

  <details><summary>Abstract</summary>

  End-to-end (E2E) autonomous driving aims to directly map sensory observations to driving actions, but its real-world deployment is hindered by evolving data distributions and the high cost of continual annotation. While combining imitation learning (IL) and reinforcement learning (RL) is a common strategy for policy improvement, conventional RL training relies on delayed, event-based rewards, where policies learn only from catastrophic outcomes such as collisions, leading to premature convergence to suboptimal behaviors. To address these limitations, we propose GSDrive, a framework that uses a differentiable 3D Gaussian Splatting (3DGS) environment for future-aware trajectory probing and reward shaping in E2E driving. GSDrive first learns a multi-mode trajectory probe via IL and then uses RL to evaluate multiple candidate futures in the 3DGS environment, converting their simulated returns into dense shaping rewards for policy optimization. This yields a cyclic hybrid IL-RL training loop, where IL supplies structured future priors and RL provides interactive feedback for iterative refinement. Evaluated on the reconstructed nuScenes dataset, our method outperforms other simulation-based RL approaches in closed-loop experiments. Code is available at https://github.com/ZionGo6/GSDrive.

  </details>

- **[Two-View Accumulation as the Primary Training Lever for Hybrid-Capture Gaussian Splatting: A Variance-Decomposition View of When Gradient Surgery Helps](https://arxiv.org/abs/2605.00052)**  
  *Sungjun Cho*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00052) · [pdf](https://arxiv.org/pdf/2605.00052.pdf)
  > 💡 混合捕捉3DGS中，每步两视图累积训练即可显著提升性能，配对方式无关，方差分解揭示其主导效应。

  <details><summary>Abstract</summary>

  Hybrid-capture novel view synthesis combines images at substantially different camera distances (e.g., aerial drone and ground-level views). Standard 3D Gaussian Splatting (3DGS), trained for 30K iterations with one rendered view per optimizer step, under-fits the minority regime by 1-3 dB on five hybrid-capture benchmarks. We isolate the lever that closes this gap. Among compute-matched alternatives -- vanilla 60K iterations, magnitude corrections (GradNorm), direction-aware near/far gradient surgery, projective preconditioning, confidence-gated sample-level surgery, and a random two-view-per-step control -- the simplest structural change wins: rendering two views per optimizer step. The pairing rule (geometry-defined near/far, random, or active loss-disparity) does not change PSNR beyond seed variance on any of the five scenes; the structural change of having two views per step does. We propose a variance-decomposition framework that predicts and explains this finding: under bimodal camera regimes, between-regime gradient variance turns out to be small relative to within-regime variance in 3DGS, so structured and random pairings are variance-equivalent in expectation, and the variance halving from two-view accumulation itself is the dominant effect. We verify the framework on five scenes whose camera-altitude bimodality coefficients span [0.55, 1.00], and we report the negative result that direction-aware projection, magnitude correction, confidence gating, and an active loss-disparity pairing all fall within seed variance of random two-view pairing. The two-view structural lever transfers cleanly to the Scaffold-GS and Pixel-GS backbones. We position this work as an honest characterization of which training-side axes do and do not move PSNR for hybrid-capture 3DGS, together with the framework that explains why.

  </details>

- **[EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors](https://arxiv.org/abs/2604.26238)**  
  *Rui Song, Tianhui Cai, Markus Gross, Yun Zhang, Walter Zimmer, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26238) · [pdf](https://arxiv.org/pdf/2604.26238.pdf)
  > 💡 将部分几何先验建模为连续能量场提供软引导，既提升光度质量又增强几何稳定性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and non-convex optimization problem. Recent works commonly incorporate geometric priors, such as LiDAR measurements, either for initialization or as training constraints, with the goal of improving photometric reconstruction quality. However, in large-scale outdoor scenarios, such geometric supervision is often spatially incomplete and uneven, which limits its effectiveness as a reliable prior and can even be detrimental to the final reconstruction. To address this challenge, we model partially observable geometry as a continuous energy field induced by geometric evidence and propose EnerGS. Rather than enforcing geometry as a hard constraint, EnerGS provides a soft geometric guidance for the optimization of Gaussian primitives, allowing geometric information to steer the optimization process without directly restricting the solution space. Extensive experiments on large-scale outdoor scenes demonstrate that, under both sparse multi-view and monocular settings, EnerGS consistently improves photometric quality and geometric stability, while effectively mitigating overfitting during 3DGS training.

  </details>

- **[AdaGScale: Viewpoint-Adaptive Gaussian Scaling in 3D Gaussian Splatting to Reduce Gaussian-Tile Pairs](https://arxiv.org/abs/2604.18980)**  
  *Joongho Jo, Hyerin Lim, Hanjun Choi, Jongsun Park*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18980) · [pdf](https://arxiv.org/pdf/2604.18980.pdf)
  > 💡 提出AdaGScale，通过估计高斯外围颜色贡献自适应缩放尺寸，减少高斯-瓦片对，实现13.8倍加速且仅降0.5dB PSNR。

  <details><summary>Abstract</summary>

  Reducing the number of Gaussian-tile pairs is one of the most promising approaches to improve 3D Gaussian Splatting (3D-GS) rendering speed on GPUs. However, the importance difference existing among Gaussian-tile pairs has never been considered in the previous works. In this paper, we propose AdaGScale, a novel viewpoint-adaptive Gaussian scaling technique for reducing the number of Gaussian-tile pairs. AdaGScale is based on the observation that the peripheral tiles located far from Gaussian center contribute negligibly to pixel color accumulation. This suggests an opportunity for reducing the number of Gaussian-tile pairs based on color contribution. AdaGScale efficiently estimates the color contribution in the peripheral region of each Gaussian during a preprocessing stage and adaptively scales its size based on the peripheral score. As a result, Gaussians with lower importance intersect with fewer tiles during the intersection test, which improves rendering speed while maintaining image quality. The adjusted size is used only for tile intersection test, and the original size is retained during color accumulation to preserve visual fidelity. Experimental results show that AdaGScale achieves a geometric mean speedup of 13.8x over original 3D-GS on a GPU, with only about 0.5 dB degradation in PSNR on city-scale scenes.

  </details>

- **[Efficient Transceiver Design for Aerial Image Transmission and Large-scale Scene Reconstruction](https://arxiv.org/abs/2604.11098)**  
  *Zeyi Ren, Jialin Dong, Wei Zuo, Yikun Wang, Bingyang Cheng, Sheng Zhou, Zhisheng Niu*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11098) · [pdf](https://arxiv.org/pdf/2604.11098.pdf)
  > 💡 针对低空大规模3D场景重建，提出融合3DGS渲染损失的端到端收发机，以稀疏导频降低开销并提升重建质量。

  <details><summary>Abstract</summary>

  Large-scale three-dimensional (3D) scene reconstruction in low-altitude intelligent networks (LAIN) demands highly efficient wireless image transmission. However, existing schemes struggle to balance severe pilot overhead with the transmission accuracy required to maintain reconstruction fidelity. To strike a balance between efficiency and reliability, this paper proposes a novel deep learning-based end-to-end (E2E) transceiver design that integrates 3D Gaussian Splatting (3DGS) directly into the training process. By jointly optimizing the communication modules via the combined 3DGS rendering loss, our approach explicitly improves scene recovery quality. Furthermore, this task-driven framework enables the use of a sparse pilot scheme, significantly reducing transmission overhead while maintaining robust image recovery under low-altitude channel conditions. Extensive experiments on real-world aerial image datasets demonstrate that the proposed E2E design significantly outperforms existing baselines, delivering superior transmission performance and accurate 3D scene reconstructions.

  </details>

- **[F3DGS: Federated 3D Gaussian Splatting for Decentralized Multi-Agent World Modeling](https://arxiv.org/abs/2604.01605)**  
  *Morui Zhu, Mohammad Dehghani Tezerjani, Mátyás Szántó, Márton Vaitkus, Song Fu, Qing Yang*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01605) · [pdf](https://arxiv.org/pdf/2604.01605.pdf)
  > 💡 针对分布式多智能体三维重建问题，提出联邦3DGS框架，固定几何只更新外观，可见性加权聚合，效果接近集中式训练。

  <details><summary>Abstract</summary>

  We present F3DGS, a federated 3D Gaussian Splatting framework for decentralized multi-agent 3D reconstruction. Existing 3DGS pipelines assume centralized access to all observations, which limits their applicability in distributed robotic settings where agents operate independently, and centralized data aggregation may be restricted. Directly extending centralized training to multi-agent systems introduces communication overhead and geometric inconsistency. F3DGS first constructs a shared geometric scaffold by registering locally merged LiDAR point clouds from multiple clients to initialize a global 3DGS model. During federated optimization, Gaussian positions are fixed to preserve geometric alignment, while each client updates only appearance-related attributes, including covariance, opacity, and spherical harmonic coefficients. The server aggregates these updates using visibility-aware aggregation, weighting each client's contribution by how frequently it observed each Gaussian, resolving the partial-observability challenge inherent to multi-agent exploration. To evaluate decentralized reconstruction, we collect a multi-sequence indoor dataset with synchronized LiDAR, RGB, and IMU measurements. Experiments show that F3DGS achieves reconstruction quality comparable to centralized training while enabling distributed optimization across agents. The dataset, development kit, and source code will be publicly released.

  </details>

