# Generation / Diffusion

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---






















## 2026-07-23

- **[Look Before You Edit: Attention-Guided Camera Placement and Multi-View Alignment for 3D Gaussian Splatting Editing](https://arxiv.org/abs/2607.19777)**  
  *Jaeyeon Park, Taeho Kang, Youngki Lee*  
  `2026-07-22` · `cs.CV` · [abs](https://arxiv.org/abs/2607.19777) · [pdf](https://arxiv.org/pdf/2607.19777.pdf)
  > 💡 通过注意力引导的相机放置和多视图注意力对齐，实现了高效、局部、一致的3D高斯泼溅编辑。

  <details><summary>Abstract</summary>

  Text-driven 3D scene editing with 3D Gaussian Splatting (3DGS) typically applies a 2D diffusion editor to views rendered from fixed training cameras, limiting both the spatial coverage of edits and the user's freedom to target specific objects in complex scenes. We present LB-Edit, a framework that addresses two coupled problems: where to place editing cameras for localized edits, and how to make per-view edits agree with one another so that the 3D scene remains consistent after fine-tuning. First, Attention-Guided Editing Camera Placement (ACP) probes the diffusion model's self- and cross-attention at multiple candidate camera distances to find where attention is well-contained in the region of interest, then places a compact, geometrically diverse editing camera set at that attention-optimal distance. Second, Multi-view Attention Alignment (MAA) steers the editor toward the same edit across views along two axes: it aligns appearance by sharing self-attention features via token-level correspondence, and aligns spatial location by lifting cross-attention maps onto the 3D Gaussians as a shared 3D attention field, suppressing both appearance and spatial drift. Experiments on multi-object and single-object scenes show that our method achieves the highest user preference in instruction fidelity, multi-view consistency, and editing locality, using as few as 5 editing views and reducing latency by up to 7x over existing methods.

  </details>

## 2026-07-22

- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539)**  
  *Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.18539) · [pdf](https://arxiv.org/pdf/2607.18539.pdf)
  > 💡 利用时间条件变形场和视频扩散先验实现大尺度场景的细微动态动画，同时保持刚性结构，提升沉浸感。

  <details><summary>Abstract</summary>

  Novel view rendering of large and complex reconstructed scenes is becoming increasingly photorealistic. However, most reconstructions remain static and lack the ambient motion that makes environments immersive. We present AniGS, a method for scene-level animation of 3D Gaussian Splatting (3DGS) reconstructions that adds subtle, distributed dynamics, e.g., vegetation motion, while preserving rigid structures. Unlike existing 3D animation techniques which are limited to object-centric subjects or small regions, AniGS is designed for large, cluttered, navigable scenes. AniGS represents the scene with a canonical 3DGS and models motion using a time-conditioned deformation field. To animate the entire scene, we leverage a pretrained video diffusion model and introduce an iterative dataset--model update strategy that progressively expands viewpoint coverage and repeatedly updates camera-fixed training videos using a render-and-refine scheme. To prevent artifacts from unintended motion in static areas, we further introduce a composed video-to-video refinement scheme that restricts motion to desired regions. Experiments on five real-world, large-scale outdoor scenes demonstrate that AniGS produces natural ambient dynamics and high-quality novel view videos, enabling more immersive viewing experiences of reconstructed environments.

  </details>

## 2026-07-21

- **[FillGauss: Fine-Grained Filling-Aware Impact Sound Generation for 3D Gaussian Splatting](https://arxiv.org/abs/2607.17773)**  
  *Chen Yang, Ganye Wen, Bin Huang, Jiayi Lyu, Zehai Niu, Linlin Shen, Jinbao Wang*  
  `2026-07-20` · `cs.MM` · [abs](https://arxiv.org/abs/2607.17773) · [pdf](https://arxiv.org/pdf/2607.17773.pdf)
  > 💡 针对忽略内部填充状态导致声学失真的问题，提出FillGauss框架，融合3DGS几何特征与潜扩散生成高保真冲击声。

  <details><summary>Abstract</summary>

  Synthesizing physically plausible impact sounds from visual observations remains a great challenge in multi-modal AI. Existing 3D-aware audio generation methods primarily model the surface geometry of hollow rigid bodies. However, they fundamentally overlook internal filling states, a critical physical factor that drastically modulates acoustic resonance and damping. To address this issue, we have defined a new task called Fine-Grained Filling-Aware Impact Sound Generation. As a foundational step, we first introduce the fine-grained fill-aware dataset (FillImpact), a pioneering multi-modal collection comprising over 5,000 rigorous acoustic recordings from 88 diverse real-world objects. It captures impact interactions with varying internal contents (i.e., water, rice), a continuous range of fill levels, and distinct striker materials. Furthermore, comprehensive acoustic analysis confirms that the collected data closely aligns with established physical laws governing acoustic resonance and damping, indicating its suitability for physically grounded modeling. Building on this dataset, we propose a novel generative framework (FillGauss) that integrates 3D Gaussian Splatting (3DGS) with internal state conditioning for sound generation. By fusing 3DGS geometric features, precise 3D spatial strike coordinates, and fine-grained textual physical conditions within a latent diffusion architecture, FillGauss enables position-aware, striker-aware, and filling-aware audio generation. Extensive experiments demonstrate that our approach could generate high-fidelity impact sounds that adhere to underlying physical principles, establishing a new state-of-the-art for physically grounded cross-modal audio generation.

  </details>

## 2026-07-17

- **[RoGS: Adaptive Meshgrid Gaussian for Large-Scale Road Surface Mapping](https://arxiv.org/abs/2607.15048)**  
  *Tianchen Deng, Zhiheng Feng, Wenhua Wu, Ziming Li, Siting Zhu, Hesheng Wang*  
  `2026-07-16` · `cs.CV` · [abs](https://arxiv.org/abs/2607.15048) · [pdf](https://arxiv.org/pdf/2607.15048.pdf)
  > 💡 使用自适应网格高斯表示实现大规模道路表面高效鲁棒映射

  <details><summary>Abstract</summary>

  Road surface mapping plays a crucial role in autonomous driving, supporting high-definition map generation, lane-level perception, and automatic road annotation. Recent mesh-based road surface reconstruction methods have shown promising results, but they still suffer from limited reconstruction quality and high optimization cost, especially in large-scale driving scenarios. To address these limitations, we propose ROADGS-T, a robust and efficient large-scale road surface mapping framework based on adaptive meshgrid Gaussian representation. Specifically, we model the road surface by placing 2D Gaussian surfels on a meshgrid, where each surfel explicitly stores color, semantic, and geometric information. Compared with conventional mesh-based representations and 3D Gaussian primitives, the proposed meshgrid Gaussian representation better matches the thin-surface property of roads while significantly reducing redundant primitives and overlap during optimization. To further improve representation efficiency and structural fidelity, we introduce a road-structure-aware adaptive meshgrid strategy, which allocates denser Gaussian surfels to geometrically or semantically complex regions, such as lane markings, road boundaries, and height discontinuities, while maintaining a compact representation in flat road areas. Moreover, instead of relying on a single nearest vehicle pose, we design a trajectory-consistency-guided pose-robust refinement strategy, which estimates local surface priors from multiple neighboring poses and adaptively weights pose-guided height regularization according to their geometric consistency.

  </details>

## 2026-07-15

- **[ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting](https://arxiv.org/abs/2607.12785)**  
  *Cheng-Tai Hsieh, Jiwei Shan, Han Fang, Jianshu Hu, Tao Ni, Lijun Han, Yutong Ban, Shing Shin Cheng, Hesheng Wang*  
  `2026-07-14` · `cs.CV` · [abs](https://arxiv.org/abs/2607.12785) · [pdf](https://arxiv.org/pdf/2607.12785.pdf)
  > 💡 通过扩散引导的3D高斯泼溅和不确定性采样，有效减少内窥镜视野外推伪影，实现SOTA新视角合成。

  <details><summary>Abstract</summary>

  Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating beyond the training trajectory.In this work, we propose ExtraGS, a framework for enhancing endoscopic view extrapolation via diffusion-guided 3D Gaussian Splatting. Starting from an initial reconstruction, we introduce an uncertainty-guided virtual camera sampling strategy to actively explore blind spots and maximize information gain. The rendered views from these sampled locations are refined using a diffusion model to recover plausible anatomical structures, producing pseudo observations that guide further optimization. To prevent the generated content from degrading reliable regions, we adopt a confidence-weighted fine-tuning strategy when incorporating these pseudo observations.Extensive experiments on multiple public endoscopic datasets demonstrate that ExtraGS significantly reduces extrapolation artifacts and achieves state-of-the-art performance in endoscopic novel view synthesis.

  </details>

- **[GeoFovea-GS: Geometry-Aware Cross-Layer Gaussian Splatting for Wireless Aerial VR](https://arxiv.org/abs/2607.12641)**  
  *Zeyi Ren, Wencheng Yan, Jiawen Zhang, Jintao Yan, Sheng Zhou, Zhisheng Niu*  
  `2026-07-14` · `cs.MM` · [abs](https://arxiv.org/abs/2607.12641) · [pdf](https://arxiv.org/pdf/2607.12641.pdf)
  > 💡 提出几何感知跨层框架GeoFovea-GS，用注视点失真度量和信息价值调度优化无线VR渲染传输，降低带宽并提升质量。

  <details><summary>Abstract</summary>

  Wireless aerial virtual reality (VR) aims to provide immersive access to large-scale scenes, but high-resolution view generation and delivery are jointly constrained by limited bandwidth, latency, and power. 3D Gaussian Splatting (3DGS) can reduce the payload by rendering views from compact pose information, yet its geometry errors may cause severe VR quality degradation. Existing channel-aware or pixel-level resource allocation schemes fail to capture such geometry-sensitive distortion. To address this issue, this paper proposes GeoFovea-GS as a geometry-aware cross-layer framework for communication-efficient wireless aerial VR. A foveated geometry-aware distortion metric is developed to characterize photometric rendering error, geometric inconsistency, and view-dependent perceptual importance in a unified form. Based on this metric, the joint selection of pose-only 3DGS rendering and image/tile correction transmission is formulated as a cross-layer optimization problem under wireless constraints. A lightweight value-of-information scheduler is further developed to allocate communication resources to regions that are both geometry-critical and perceptually important. Experiments on real-world 3DGS scenes demonstrate that GeoFovea-GS achieves superior immersive rendering quality with substantially reduced transmission cost.

  </details>

## 2026-07-14

- **[ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673)**  
  *Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.11673) · [pdf](https://arxiv.org/pdf/2607.11673.pdf)
  > 💡 提出SGP统一多模态输入，通过全景视频生成与3DGS重建，实现从文本/图像/视频到高保真可探索3D世界。

  <details><summary>Abstract</summary>

  We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds. At the heart of our framework is a unified Spatial Generative Primitive (SGP), a compact tuple of a high-quality panorama and a spatial point cloud that delivers an efficient description of any 3D space. Multimodal inputs are first lifted into this primitive; a 3D-consistent panoramic video generator then explores the primitive along a planned trajectory; finally, our panoramic video reconstruction engine converts the generated video into a clean, photorealistic 3D Gaussian Splatting (3DGS) world. This pipeline covers two regimes: rich inputs (multi-view sets, casual video) are lifted into the SGP through a geometry-rigorous recovery that mirrors the observed scene, while a single image or sentence is completed generatively into a creative world. The result is one low-barrier engine for general 3D content creation that further anchors generated worlds to geographic points of interest, enabling map-native spatial exploration at consumer scale. Experiments show that ABot-3DWorld 0 sets the state of the art among open-source methods and demonstrates stronger scene fidelity than Marble under rich multimodal inputs.

  </details>

## 2026-07-13

- **[StereoSplat+: Feed-Forward Stereo Gaussian Splatting with Diffusion-Assisted Progressive Inference](https://arxiv.org/abs/2607.08808)**  
  *Zihua Liu, Masatoshi Okutomi*  
  `2026-07-09` · `cs.CV` · [abs](https://arxiv.org/abs/2607.08808) · [pdf](https://arxiv.org/pdf/2607.08808.pdf)
  > 💡 单个立体对重建3DGS困难，提出StereoSplat前馈估计器融合成本体积与三平面，结合扩散增强渐进推理提升遮挡区渲染质量与几何精度。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled high-quality, render-ready scene representations for novel-view synthesis. However, most existing 3DGS pipelines rely on multi-view observations (or non-causal access to future frames) to achieve sufficient coverage, which is often unavailable in on-device robotics and AR settings where sensing is restricted to a single stereo rig. Recovering a high-quality 3DGS scene from one stereo observation, therefore, remains challenging due to occlusions, limited field of view, and missing geometry. We present StereoSplat+, a diffusion-enhanced feed-forward framework that enables causal reconstruction from a single stereo pair. Our method builds on two key components. First, we propose StereoSplat, an input-invariant feed-forward 3D Gaussian estimator that takes a variable number of posed stereo pairs as input and predicts high-quality 3D Gaussians. StereoSplat fuses complementary geometry cues via a cost-volume branch and a triplane-based 3D volume branch and leverages continuous pose encoding to generalize across view counts and camera configurations. Second, since multiple posed stereo pairs are typically unavailable at inference time, we introduce a diffusion-enhanced one-shot progressive inference scheme called StereoSplat+: starting from one stereo pair, we render novel stereo views from the predicted 3DGS, refine them with a one-step diffusion enhancer, and feed them back as additional inputs to update the 3DGS. Experiments on the KITTI-360 dataset show that StereoSplat+ improves novel-view rendering quality and geometry accuracy, especially in occluded regions and under strong view extrapolation, outperforming recent feed-forward 3DGS baselines.

  </details>

## 2026-07-09

- **[EscFOA: Enhancing Spatial Learning for Visually Impaired Learners via Generative Spatial Audio in 360-Degree Educational Environments](https://arxiv.org/abs/2607.07015)**  
  *Ziyu Luo, Xiaowei Dai, Siying Zhu, Xiaoming Chen*  
  `2026-07-08` · `cs.SD` · [abs](https://arxiv.org/abs/2607.07015) · [pdf](https://arxiv.org/pdf/2607.07015.pdf)
  > 💡 针对360度教育环境中视障学习者空间定向困难，提出基于3DGS与条件扩散模型的几何感知空间音频生成框架，显著提升空间学习。

  <details><summary>Abstract</summary>

  Immersive 360-degree educational environments often lack accessible spatial structure, limiting visually impaired learners' ability to orient, explore, and construct mental representations. This paper proposes EscFOA, a geometry-aware spatial audio generation framework designed as an \emph{acoustic scaffolding} to support spatial cognition. By integrating 3D Gaussian Splatting (3DGS) with conditional diffusion models, EscFOA reconstructs scene geometry from 360-degree videos to synthesize high-fidelity spatial audio consistent with the environmental structure. Explicitly targeting learning outcomes like independent spatial orientation and reduced cognitive load, EscFOA significantly outperforms conventional monaural and stereo audio in supporting spatial learning behaviors among blindfolded sighted participants (simulating visually impaired learners). These findings demonstrate that geometry-consistent generative audio can effectively enable inclusive access to complex spatial learning materials.

  </details>

- **[PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.07170)**  
  *Yi Yang, Myrna Castillo, Bodo Rosenhahn, Michael Ying Yang*  
  `2026-07-08` · `cs.CV` · [abs](https://arxiv.org/abs/2607.07170) · [pdf](https://arxiv.org/pdf/2607.07170.pdf)
  > 💡 针对在线3D场景图生成中确定性融合忽视不确定性问题，提出即插即用不确定性感知融合框架，用概率似然和狄利克雷证据累积提升性能。

  <details><summary>Abstract</summary>

  Online 3D scene graph generation builds a persistent, structured representation of a scene by incrementally fusing 2D observations into a global 3D graph. Existing online methods treat this fusion as a fully deterministic pipeline, where we identify three sources of uncertainty that are overlooked: observation, 2D model, and 3D representation. We propose PUF: a Plug-and-play, Uncertainty-aware, and training-free Fusion framework. Scene graph node association is reformulated as a probabilistic likelihood over semantic and spatial factors, replacing binary accept/reject gates. Dirichlet evidence accumulation distributes class and relationship evidence across plausible candidates proportional to association likelihood. An optional class-conditional prior completes edges for sparsely or never co-observed object pairs. We instantiate PUF with both a 3D Gaussian and a 3D voxel backend and observe consistent improvements, demonstrating its ability to generalize across different representations. Experiments on the 3DSSG and ReplicaSSG benchmarks show that our method substantially outperforms existing approaches while maintaining real-time latency. These results establish uncertainty-aware fusion as a principled and effective paradigm for online 3D scene understanding. The source code is publicly available at https://github.com/yyyyangyi/PUF.

  </details>

- **[RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation](https://arxiv.org/abs/2607.06699)**  
  *Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen*  
  `2026-07-07` · `cs.RO` · [abs](https://arxiv.org/abs/2607.06699) · [pdf](https://arxiv.org/pdf/2607.06699.pdf)
  > 💡 通过分层设计融合碰撞感知前景和3D高斯泼溅背景，将单张RGB图转化为稳定仿真场景，支持机器人泛化学习与评估。

  <details><summary>Abstract</summary>

  Recovering real-world scenes as interactive simulation environments can enable generalizable robot learning and reproducible policy evaluation. However, constructing scenes that are both physically stable and visually faithful remains slow and expensive. In this work, we present RoboSnap, a real-to-sim framework that turns a single RGB image into a simulation-ready scene. The key idea is a layered design that separates the physics-critical interaction area from the surrounding visual context: collision-aware foreground assets are refined for stable robot interaction, while a 3D Gaussian splatting visual layer preserves faithful background appearance under novel views. Experiments on DROID scenes and real-robot tasks show that RoboSnap achieves reliable trajectory replay in the recovered scenes, supports task-specific synthetic data generation for policy training, and yields meaningful sim-real correlation for policy evaluation. To further support real-to-sim research, we introduce DROID-Sim, a real-to-sim companion dataset constructed from 564 real-world scenes in DROID. Extensive experiments suggest that the value of real-to-sim methods lies not only in high-fidelity visual reconstruction, but in turning real environments into reusable infrastructure for robot learning and evaluation.

  </details>

## 2026-07-07

- **[Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.04770)**  
  *Davide Jannussi, Stefano Carlo Lambertenghi, Constantin Carste, Andrea Stocco*  
  `2026-07-06` · `cs.SE` · [abs](https://arxiv.org/abs/2607.04770) · [pdf](https://arxiv.org/pdf/2607.04770.pdf)
  > 💡 利用Gaussian Splatting将真实驾驶记录重建为可交互CARLA场景，减少仿真与真实视觉差距并提升行为相似性。

  <details><summary>Abstract</summary>

  Simulation-based testing enables safe and repeatable evaluation of autonomous driving systems, but its effectiveness is limited by the gap between synthetic simulator outputs and real-world camera observations. To address this problem, we present Cam2Sim, a tool that transforms real-world driving recordings into playable CARLA simulation scenarios. Starting from camera images and poses, Cam2Sim reconstructs road geometry, ego trajectories, parked vehicles, and simulation assets, and augments the reconstructed environment with Gaussian Splatting to render camera observations that resemble the original recording. The framework supports ROS-based data extraction, parked-vehicle detection, OpenStreetMap-based map generation, CARLA scenario construction, Gaussian Splatting training, trajectory replay, and closed-loop execution with a system under test. We validate Cam2Sim on a real-world urban-driving scenario with a camera-based end-to-end driving model, comparing reconstruction quality, image-generation quality, and closed-loop behavior against both a simulation-only baseline and the real-world target. Results show that Gaussian-Splatting-based rendering reduces the visual gap with respect to standard simulator rendering and improves behavioral similarity to the real-world reference runs. The artifact is publicly available at https: //github.com/ast-fortiss-tum/cam2sim, and a screencast showing the tool is available at https://youtu.be/KmZ74l1__lI

  </details>

- **[MACRO: Training-free Multi-plane Attention for Closeup Render Optimization](https://arxiv.org/abs/2607.03875)**  
  *Nitzan Hodos, Roy Amoyal, Lior Fritz, Ianir Ideses, Sagie Benaim, Netalee Efrat*  
  `2026-07-04` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03875) · [pdf](https://arxiv.org/pdf/2607.03875.pdf)
  > 💡 针对3DGS近距离渲染尺度失配问题，提出多平面注意力训练-free优化方法，实现高质量渲染并创立新基准。

  <details><summary>Abstract</summary>

  Close-up rendering, zooming into a scene well beyond any training camera, is important for virtual production and interactive 3D content, yet remains an open challenge. 3D Gaussian splatting (3DGS) enables high-fidelity, real-time novel view synthesis, but its rendering quality degrades at close range. Recent diffusion-based methods that enhance the rendering by conditioning on reference images from the training set produce significant artifacts in this setting. We analyze this failure and identify its root cause: the scale gap between the close-up and reference views. We show that the features in reference-conditioned enhancement models are not scale-invariant, causing cross-view attention to retrieve incorrect correspondences when the same content appears at different scales, and that this mismatch cannot be corrected in latent space because the VAE encoder is not scale-equivariant. Building on this analysis we introduce MACRO, Multi-plane Attention for Closeup Render Optimization, a training-free method for high-quality close-up novel view synthesis from 3DGS. MACRO resolves the scale gap by leveraging the scene's known 3D structure: it decomposes the close-up into depth planes, crops and resizes references in image space to match the scale of each plane before encoding, and applies a depth-aware attention mask so each token attends only to scale-matched references. The method requires no architectural changes or additional training. We further contribute two new close-up novel view synthesis benchmarks, the first standardized evaluation protocol for this setting, and demonstrate state-of-the-art results on both, outperforming existing 3DGS and diffusion-based methods on both reconstruction and perceptual metrics. Project page: https://nitzanhod.github.io/MACRO

  </details>

- **[CGGS: Consistency-Augmented Geometric Gaussian Splatting for Ego-centric 3D Scene Generation](https://arxiv.org/abs/2607.03819)**  
  *Zhenyu Sun, Xiaohan Zhang, Qi Liu, Huan Wang*  
  `2026-07-04` · `cs.GR` · [abs](https://arxiv.org/abs/2607.03819) · [pdf](https://arxiv.org/pdf/2607.03819.pdf)
  > 💡 针对第一人称视角下几何失真与视角不一致，提出一致性增强扩散模型和互信息深度损失优化3D高斯，生成高质量文本驱动场景。

  <details><summary>Abstract</summary>

  Challenges remain in ego-centric 3D scene generation due to limited view overlap and the dominant influence of individual perspectives on scene interpretation. These factors hinder the creation of viewpoint-consistent and semantically aligned visual content, as well as the construction of accurate geometric structures. In this paper, we propose CGGS, a text-to-3D framework aiming to enhance 3D-content-awareness and address geometric distortions in ego-centric scene generation. Firstly, the Ego-centric Generator is proposed by fine-tuning a Multi-View Latent Diffusion Model with consistency-augmented loss to generate consistent, high-fidelity 2D content aligned with textual descriptions. Then, Layout Decorator leverages optical flow and point-track correspondence to estimate depth, therefore producing dense point clouds as coarse layouts from the ego-centric 2D priors. Building on this initialization, Geometric Refiner is proposed to enhance 3D Gaussian reconstruction via an entropy-based Mutual Information Depth Loss (MID) combined with a hierarchical optimization scheme for improving visual quality and geometric structure. Comprehensive experiments demonstrate that \textcolor{softred}{CGGS} outperforms previous methods in generating coherent and accurate text-driven 3D scenes. Project page: https://cggs-26.github.io/cggs26/.

  </details>

## 2026-07-04

- **[X-Splat: Gaussian Splatting for 3D CBCT Generation from Single Panoramic Radiograph](https://arxiv.org/abs/2607.02099)**  
  *Tomasz Szczepański, Szymon Płotka, Michal K. Grzeszczyk, Tomasz Trzciński, Arkadiusz Sitek*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.02099) · [pdf](https://arxiv.org/pdf/2607.02099.pdf)
  > 💡 首个高斯泼溅框架从单张全景X光片生成3D牙科CBCT，利用采集几何初始化可调各向异性高斯，优于NeRF和GAN基线。

  <details><summary>Abstract</summary>

  Generating a 3D dental volume from a single panoramic radiograph (PXR) could provide a low-radiation alternative to Cone-Beam Computed Tomography (CBCT), but the problem is highly underdetermined: panoramic acquisition integrates 3D attenuation along curved X-ray paths into a 2D image, leaving depth-resolved anatomy unobserved. Existing implicit and generative approaches often produce oversmoothed geometry or anatomically inconsistent hallucinations, lacking geometry-driven supervision and relying on smooth representations unable to precisely localize sharp anatomical boundaries. We propose X-Splat, the first Gaussian Splatting framework for generating CBCT-like 3D dental volumes from a single PXR. X-Splat uses the known panoramic acquisition geometry as a generation scaffold: learnable anisotropic Gaussian primitives are initialized along the X-ray paths that formed the input image and adjusted in a single feed-forward pass, constrained by Beer-Lambert reprojection and multi-view radiographic training supervision. A lightweight residual refiner adds dataset-level anatomical priors without overriding the geometry already resolved by the Gaussians. We train on synthetic PXR-CBCT pairs, enabling direct volumetric supervision without paired real scans. We further introduce segmentation-based geometry-aware metrics, providing the first evaluation of PXR-based generation over maxillofacial anatomy. X-Splat outperforms NeRF- and GAN-based baselines, recovering individual teeth, cortical boundaries, and alveolar structure, including the mandibular canal which prior methods fail to reconstruct. Code will be available at https://github.com/tomek1911/X-Splat

  </details>

- **[PixGS: Pixel-Space Diffusion for Direct 3D Gaussian Splat Generation](https://arxiv.org/abs/2607.01803)**  
  *Duy Cao, Phong Nguyen-Ha*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.01803) · [pdf](https://arxiv.org/pdf/2607.01803.pdf)
  > 💡 提出PixGS像素空间扩散直接生成3D高斯泼溅，避免潜在压缩伪影，实现快速高质量3D内容生成。

  <details><summary>Abstract</summary>

  Recent advances in 3D content generation from text or images have achieved impressive results, yet view inconsistency from 2D generators and the scarcity of high-quality 3D data remain significant bottlenecks. Existing solutions typically adapt large-scale pre-trained text-to-image latent diffusion models to generate 3D Gaussian Splats (3DGS). However, these approaches often rely on training complex cascade pipelines that are computationally expensive and scalability-limited. Most critically, the quality of generated 3D assets is inherently constrained by each component capacity and compressed latent space, leading to decoding artifacts and accumulated errors. To address these limitations, we propose PixGS, a single-stage pipeline for direct high-quality 3DGS generation, which leverages recent advances in pixel-space diffusion to bypass lossy latent compression while still benefiting from the vast 2D generative priors. By directly denoising 3D Gaussian attributes at each timestep, our method enables precise, splat-level regularization of both appearance and geometry. Furthermore, we introduce a comprehensive supervision strategy that incorporates surface normals, depth, and high-frequency structural information, which is often overlooked in prior works. Experiments demonstrate that PixGS outperforms current state-of-the-art methods while maintaining a fast inference speed (1s on a single A100 GPU), offering a robust and efficient alternative to multi-stage generation pipelines.

  </details>

## 2026-07-02

- **[DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889)**  
  *Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha, Dooyoung Kim, Eunjae Shin, Benjamin Busam, Woontack Woo*  
  `2026-07-01` · `cs.CV` · [abs](https://arxiv.org/abs/2607.00889) · [pdf](https://arxiv.org/pdf/2607.00889.pdf)
  > 💡 提出深度感知3D语义场景图生成方法，用深度引导滤波和概率高斯节点改进对象表示，聚合时空证据及世界模型先验优化关系，在召回率上显著提升。

  <details><summary>Abstract</summary>

  We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single projected point. To mitigate relational sparsity from frame-wise inference, our framework further aggregates spatiotemporal evidence across object pairs and refines relations using contextual priors derived from a world model (V-JEPA 2). Experiments on the 3DSSG and ReplicaSSG datasets demonstrate state-of-the-art (SoTA) performance in both object and predicate prediction, while producing temporally consistent scene structures. In particular, our method improves triplet recall by 77.4% and predicate recall by 23.2% over prior SoTA approaches, making it suitable for robotic manipulation and AR applications. Our code and models are open-sourced.

  </details>

## 2026-07-01

- **[DriveWeaver: Point-Conditioned Video Inpainting for Controllable Vehicle Insertion in Autonomous Driving Simulation](https://arxiv.org/abs/2606.31918)**  
  *Junzhe Jiang, Zipei Ma, Zijie Pan, Li Zhang*  
  `2026-06-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.31918) · [pdf](https://arxiv.org/pdf/2606.31918.pdf)
  > 💡 提出基于点云条件视频修复的DriveWeaver，解决车辆插入光照不一致与3D资产依赖问题，实现高质量、可泛化的实时渲染。

  <details><summary>Abstract</summary>

  A pivotal step in autonomous driving simulation involves inserting foreground vehicles with predefined trajectories into simulated scenes. This process enhances scene diversity and facilitates the creation of various corner cases for testing and improving autonomous driving models. However, existing methods often rely on pre-reconstructed 3D assets, which frequently lead to lighting inconsistencies between the inserted foreground and the background. Moreover, the reliance on limited, manually-curated 3D assets hinders large-scale deployment. To address these challenges, we propose DriveWeaver, a novel framework for controllable vehicle insertion in autonomous driving simulation. Specifically, for a masked target insertion area, DriveWeaver performs video inpainting conditioned on vehicle point clouds to generate high-quality, temporally consistent vehicles. This video-inpainting-based approach ensures seamless blending between the foreground and background, while the readily available point cloud conditions enable superior generalization. To support long-term generation, we further design a global-to-local hierarchical inpainting strategy, ensuring the consistent identity and appearance of the inserted vehicles. Meanwhile, we extract explicit 3D Gaussian representations of the inserted vehicles through an urban reconstruction pipeline to enable real-time rendering for autonomous driving simulation. Extensive experiments across diverse datasets demonstrate that our method outperforms existing baselines in visual realism and geometric consistency, providing a robust tool for scalable autonomous driving scene augmentation.

  </details>

## 2026-06-30

- **[IBRSteG: Learning a Generalizable Steganography Framework for 3D Gaussian Splatting](https://arxiv.org/abs/2606.30024)**  
  *Fanye Kong, Hongyu Xia, Yu Zheng, Boyang Gong, Jie Zhou, Jiwen Lu*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30024) · [pdf](https://arxiv.org/pdf/2606.30024.pdf)
  > 💡 针对3DGS隐写难以泛化问题，提出IBRSteG框架，利用GAS网络学习场景无关的嵌入函数，实现高容量、安全的隐写且无需逐场景微调。

  <details><summary>Abstract</summary>

  Recent advances in deep learning have notably improved steganographic message hiding. However, designing a generalizable steganographic approach for 3D Gaussian Splatting (3DGS) that can embed meaningful 3D scene content remains challenging. In this paper, we propose IBRSteG, a generalizable framework for 3DGS steganography that enables undetectable concealment of secret scenes within a steganographic scene. Unlike existing approaches whose parameter generation is rigidly coupled with the specific scene, we formulate 3D steganography as a feed-forward 3D Gaussian embedding process that generalizes across different 3DGS scenes. To realize this, we introduce GAS (Gaussian Attributes Steganographer), a network that learns a scene-independent embedding function by injecting the attributes of secret 3D Gaussian points into a cover scene, thereby directly reconstructing the steganographic scenes without per-scene finetuning or optimization. By transforming 3D Gaussian into these structured attributes, these attributes are compatible with 2D learning paradigms and benefit from their structured nature, thereby enhancing generalization to unseen 3DGS scenes. Extensive experiments on established datasets demonstrate that IBRSteG can effectively conceal different scenes with high visual quality, and achieves superior capacity and security. Code is available at https://github.com/LingXiang2023/IBRSteG.

  </details>

## 2026-06-29

- **[CoIn: Comprehensive 2D-3D Inpainting with Gaussian Splatting Guidance](https://arxiv.org/abs/2606.27584)**  
  *Hana Kim, Minje Kim, Tae-Kyun Kim*  
  `2026-06-25` · `cs.CV` · [abs](https://arxiv.org/abs/2606.27584) · [pdf](https://arxiv.org/pdf/2606.27584.pdf)
  > 💡 针对3D修复依赖精确分割掩码的问题，提出CoIn框架，利用GS引导的双向一致性管道，实现灵活掩码的物体移除与插入，性能领先。

  <details><summary>Abstract</summary>

  3D scene inpainting is essential for reconstructing areas corrupted by occlusions or limited viewpoints. While recent methods leverage Gaussian Splatting (GS) for efficient 3D editing, they often depend on precise multi-view segmentation masks and are inherently constrained to object removal tasks. We propose CoIn, a novel framework that bridges 2D inpainting models and 3DGS through a multi-stage consistency pipeline. Our approach first generates initial inpainted images using a diffusion model, enabling the use of arbitrary-shaped masks and diverse tasks like object insertion. We then introduce Reference Adaptive GS with Feature Attention to reconstruct a coarse 3D scene by adaptively weighing towards a reference view (2D -> 3D). This 3D representation provides geometric guidance to the diffusion process via GS-based Reference Feature Warping, ensuring multi-view consistency (3D -> 2D). Finally, a Texture-Enhancing Discriminator refines the 3D scene to achieve high photometric realism (2D -> 3D). Experiments show that CoIn, effectively leveraging bidirectional information flow, achieves state-of-the-art performance and effectively handles both object removal and object insertion with flexible mask input.

  </details>

## 2026-06-26

- **[SatSplatDiff: Geometry-preserving generative refinement for high-fidelity satellite Gaussian Splatting](https://arxiv.org/abs/2606.27223)**  
  *Jiyong Kim, Shuang Song, Ronjgun Qin*  
  `2026-06-25` · `cs.CV` · [abs](https://arxiv.org/abs/2606.27223) · [pdf](https://arxiv.org/pdf/2606.27223.pdf)
  > 💡 卫星高斯泼溅因视角受限导致立面空洞和保真度低，提出单目深度监督与阴影引导生成细化，几何误差降18%，视觉保真度提28-45%。

  <details><summary>Abstract</summary>

  Gaussian Splatting has been recently explored for satellite 3D reconstruction, demonstrating flexibility and efficiency in representing radiometrically diverse satellite scenes. However, the limited top viewpoint of satellite imagery results in insufficient supervision on building facades, leaving surface holes and degraded visual fidelity. Generative refinement, which leverages pretrained generative priors to iteratively refine and update the rendered images used as supervision targets, has recently been investigated to improve the visual fidelity of Gaussian-rendered images. However, since these models refine each view independently, the resulting images can generate hallucinations and break photo-consistency, leading to geometric degradation. To address these limitations, we propose SatSplatDiff, which aims to minimize geometric degradation prevalent in generative refinement. Building on photogrammetric DSM initialization and 2DGS-based shadow casting established in our prior work SatSplat, we first introduce monocular depth supervision and multi-scale geometric refinement to establish a geometrically accurate and well-regularized surface representation. We then apply shadow-guided generative refinement, where geometrically calculated shadow maps guide the Gaussians to maintain consistency with the underlying geometry, improving visual fidelity while reducing geometric degradation. Extensive evaluations on the IARPA2016 and DFC2019 datasets demonstrate state-of-the-art performance, reducing geometric MAE by up to 18% and improving visual fidelity (FID-CLIP) by 28-45% over existing baselines. Our method delivers up to 5x resolution enhancement with minimal hallucination and sensor-consistent appearance, demonstrating seamless cross-tile consistency and strong scalability for large-scale reconstruction. Source code is available at https://github.com/GDAOSU/SatSplatDiff

  </details>

- **[PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views](https://arxiv.org/abs/2606.27071)**  
  *Zhisong Xu, Takeshi Oishi*  
  `2026-06-25` · `cs.CV` · [abs](https://arxiv.org/abs/2606.27071) · [pdf](https://arxiv.org/pdf/2606.27071.pdf)
  > 💡 针对旋转主导弱视差下稀疏全景图重建难题，提出无SfM框架，结合几何引导扩散补全与3DGS优化，提升稳定性。

  <details><summary>Abstract</summary>

  Panoramic sensing offers wide field-of-view coverage, yet 3D reconstruction from sparse panoramas remains challenging under rotation-dominant, weak-parallax motion. In such regimes, SfM/SLAM initialization is often ill-conditioned and unreliable. We present PanoImager, an SfM-free framework that combines feed-forward pose/depth priors, geometry-conditioned diffusion view completion, and depth-guided 3DGS optimization. Given only a few panoramic images, PanoImager decomposes them into local perspective views, synthesizes auxiliary observations to enrich sparse evidence, and stabilizes Gaussian optimization for improved cross-view consistency. Experiments on multiple benchmarks show improved stability under extreme sparsity, suggesting PanoImager as an offline/background component for map refinement when SfM/SLAM fails to initialize.

  </details>

## 2026-06-24

- **[MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)**  
  *Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24301) · [pdf](https://arxiv.org/pdf/2606.24301.pdf)
  > 💡 利用多视图图像和LiDAR点云引导的3D生成模型，通过高斯泼溅体素过滤提升几何精度与网格质量。

  <details><summary>Abstract</summary>

  Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment. However, most existing vehicle generation methods fail to fully exploit multimodal sensors i.e. multi-view images and LiDAR point clouds) and rely on neural rendering based reconstruction, leading to low-quality mesh. Recently, native 3D generative models have made significant progress, yet they are not built for arbitrary multi-view inputs and often struggle with in-the-wild driving images. In this work, we present MM-TRELLIS, a multi-modal version of TRELLIS for in-the-wild 3D vehicle generation that integrates LiDAR and image sensors from autonomous driving datasets into native 3D generative models. Specifically, multi-view images are cycled as conditioning inputs, while LiDAR point clouds provide test-time guidance to ensure geometric accuracy and cross-view consistency. During denoising, we first align the guidance point cloud with the model priors, then enforce consistency between the generated geometry and the guidance point cloud. Finally, we introduce a voxel filtering strategy based on the opacity of 3D Gaussian Splatting to suppress floaters and produce clean meshes. Comprehensive experiments on Waymo dataset demonstrate our method outperforms existing methods in high-fidelity 3D vehicle generation. Code is available at https://github.com/HongliXiao/MM-TRELLIS.

  </details>

- **[3DCarGen: Scalable 3D Car Generation via 3D-consistent Multi-view Synthesis](https://arxiv.org/abs/2606.24257)**  
  *Hongli Xiao, Youjian Zhang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24257) · [pdf](https://arxiv.org/pdf/2606.24257.pdf)
  > 💡 提出3DCarGen，利用3D一致多视图合成与高斯泼溅重建，从单视图生成高质量3D车辆，解决几何不一致问题。

  <details><summary>Abstract</summary>

  High-quality 3D vehicle assets are essential for autonomous driving simulation. Although multi-view diffusion-based paradigms enable controllable single-image reconstruction, they typically produce limited viewpoints and exhibit cross-view geometric inconsistencies, thereby reducing reconstruction fidelity in real-world scenarios. In this work, we introduce 3DCarGen, a scalable single-view 3D car generation framework designed for real-world images by synthesizing an arbitrary number of 3D-consistent multi-view images. Specifically, given a single image as input, we first synthesize a set of images from fixed viewpoints. These images are then fed into a feed-forward reconstruction model, resulting in a coarse 3D representation based on 3D Gaussian Splatting. Conditioned on this explicit 3D prior, our multi-view diffusion model generates 3D-consistent images from arbitrary camera viewpoints. We further extend a fast mesh reconstruction algorithm by incorporating color-normal joint optimization to recover detailed and coherent 3D vehicle models from the synthesized dense views. Extensive experiments on synthetic and real-world datasets demonstrate that our approach achieves robust geometric consistency and reconstruction fidelity compared to existing methods. Code and models will be released.

  </details>

- **[FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation](https://arxiv.org/abs/2606.24876)**  
  *Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24876) · [pdf](https://arxiv.org/pdf/2606.24876.pdf)
  > 💡 从视频扩散潜码直接解码三角形splats，通过新参数化与窗口函数提升梯度流，实现更高几何精度。

  <details><summary>Abstract</summary>

  Generating explorable 3D scenes from a single image requires strong generative priors and accurate geometric representations suitable for downstream use. Current video diffusion models offer high-quality generation and implicitly encode multi-view geometric structure in latent space. However, existing feedforward latent scene decoders typically output volumetric 3D Gaussians that lack a well-defined surface, limiting their use in simulation or standard graphics pipelines. This motivates decoding surface-aligned primitives that are not only renderable but also closer to explicit geometric assets. We ask whether compressed video diffusion latents can be mapped directly to explicit surface primitives in a single pass. To this end, we introduce FLAT and, for the first time, show that triangle splats can be decoded directly from video diffusion latents. Compared with decoding 3D Gaussians, predicting flat primitives is notoriously more challenging due to high sensitivity to primitive orientations, oftentimes leading to poor gradient flow. FLAT solves with two key ingredients: a ray-centered rotation parameterization for triangle regression and a novel product window function that improves gradient flow during differentiable triangle rendering. On standard benchmarks, FLAT achieves significantly better geometric accuracy while maintaining competitive visual quality compared to state-of-the-art feedforward baselines. We further show that a lightweight test-time refinement step converts the predicted triangle soup into a fully opaque, game-engine-ready representation that supports real-time rendering. By evaluating 3DGS, 2DGS, and triangle splatting variants under an identical training setup, we provide the first systematic analysis of representation tradeoffs in feedforward scene generation. The project page is available at https://flat-splat.github.io

  </details>

## 2026-06-23

- **[Lighting-Consistent Object Transfer Across Radiance Fields](https://arxiv.org/abs/2606.22481)**  
  *Nicolás Violante, George Kopanas, Linus Franke, Julien Philip, George Drettakis*  
  `2026-06-21` · `cs.GR` · [abs](https://arxiv.org/abs/2606.22481) · [pdf](https://arxiv.org/pdf/2606.22481.pdf)
  > 💡 扩散模型协调不同3DGS场景间光照不一致的对象转移，利用异质数据集训练并通过后优化提升合成质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is widely used to capture and render real scenes. Compositing objects from one capture into another has applications in many domains, such as VFX, architecture and interior design, or marketing. However, extracting an object from a source scene and naively pasting it into a target scene will fail to produce realistic results due to the different lighting conditions between the two scenes. To address this problem, we introduce a diffusion model that harmonizes naively composited images with inconsistent lighting. The model is trained with a heterogeneous dataset of image pairs (inconsistent composite input, consistent output), combining synthetic, generated, and real data. Our complete 3D solution allows a user to extract an object from the source scene and composite it into the target scene. From this, the (inconsistent) views of the target scene with the composite object are rendered. Our diffusion model harmonizes each one of these views, which are finally consolidated in a 3DGS representation with a post-optimization step. Our method provides visually compelling results, making object transfer between 3DGS easy to use and significantly improving quality compared to previous methods.

  </details>

## 2026-06-18

- **[FlowObject: Flow Steering for Bridging Generative Priors and Reconstruction Fidelity](https://arxiv.org/abs/2606.19019)**  
  *Yuchen Rao, Xuqian Ren, Yinyu Nie, Sayan Deb Sarkar, Biao Zhang, Vincent Lepetit, Friedrich Fraundorfer*  
  `2026-06-17` · `cs.CV` · [abs](https://arxiv.org/abs/2606.19019) · [pdf](https://arxiv.org/pdf/2606.19019.pdf)
  > 💡 针对稀疏视图重建中生成先验与观测一致性矛盾，提出双空间引导流匹配和3DGS细化，实现高

  <details><summary>Abstract</summary>

  Recovering complete 3D representations of objects from few casual image captures remains a significant challenge. Recent 3D generative models, particularly those based on Flow-Matching (FM), can synthesize high-quality textured assets; however, they often suffer from ''synthetic bias'' where learned priors override observational evidence, alongside a lack of alignment with the observed instance. Conversely, optimization-based methods like 3D Gaussian Splatting (3DGS) provide high fidelity on visible surfaces but fail to reason about unobserved geometry. In this paper, we present FlowObject, a framework that reformulates sparse-view 3D reconstruction as a training-free, guided inverse problem. Our approach applies a dual-space guidance strategy to steer the Ordinary Differential Equation (ODE) trajectory of a flow-matching model, enabling the completion of unseen regions through learned generative priors while enforcing strict consistency with real-world observations. By integrating a 3DGS refinement stage, FlowObject further bridges the gap between ''synthetic-looking'' generative outputs and photorealistic reconstructions. Comprehensive benchmarks on synthetic and real-world datasets demonstrate that current state-of-the-art methods often struggle to achieve geometric completeness and observational consistency simultaneously, especially under severe occlusions. In contrast, our method significantly outperforms state-of-the-art generative models and optimization-based frameworks in both geometric completeness and view-dependent appearance fidelity.

  </details>

- **[Point-Cloud-Assistant Localized Statistical Channel Prediction by Tangent Gaussian Splatting](https://arxiv.org/abs/2606.18734)**  
  *Ye Xue, Yiheng Wang, Xinhua Shao, Qi Yan, Shutao Zhang, Tsung-Hui Chang*  
  `2026-06-17` · `eess.SP` · [abs](https://arxiv.org/abs/2606.18734) · [pdf](https://arxiv.org/pdf/2606.18734.pdf)
  > 💡 用切线高斯泼溅外推无线信道角度功率谱，结合点云几何实现未测量网格的准确预测，性能更优。

  <details><summary>Abstract</summary>

  Accurate, site-specific channel information is crucial for optimizing next-generation wireless networks. Among various approaches, localized statistical channel modeling (LSCM), which models the channel multipath angular power spectrum (APS) from the reference signal received power (RSRP) measurement, has emerged as a state-of-the-art method tailored for efficient network optimization. However, despite its effectiveness, LSCM cannot predict APS at the vast majority of locations where no measurements are available, which significantly restricts its applicability in large-scale, real-world scenarios. To address this challenge, we present \emph{point-cloud-assisted tangent Gaussian splatting} (PC-TGS), the first framework to \emph{extrapolate} APS to unmeasured outdoor grids by integrating sparse radio measurements with dense LiDAR-based geometry. PC-TGS represents environmental scatterers as anisotropic 3D Gaussians, initialized and refined through a relaxed-mean reparameterization of the raw point cloud. A tangent-plane projection accurately maps each Gaussian into the local angular domain, while a depth-aware electromagnetic splatting process aggregates their contributions. To ensure practical deployment, we derive a closed-form Gaussian-weighted average (GWA) for APS bin integration and provide a provable error bound. { Evaluations on a LiDAR-scanned city-scale dataset (5M points, 6,310 RSRP samples) demonstrate that PC-TGS achieves better APS and RSRP prediction performance compared to state-of-the-art baselines and faster inference time for APS extrapolation task. These results highlight the potential of PC-TGS to enable geometry-aware and data-efficient channel prediction in large-scale wireless digital twins.

  </details>

- **[GASE: Gaussian Splatting-Based Automated System for Reconstructing Embodied-Simulation Environments](https://arxiv.org/abs/2606.17520)**  
  *Jiawei Zhang, Yiming Yan, Chao Liang, Nuo Xu, Seson Sun, Qichen Zhang, Yuhao Xu, Yantai Yang, Yingqiao Wang, Qin Jin, Zhipeng Zhang*  
  `2026-06-16` · `cs.RO` · [abs](https://arxiv.org/abs/2606.17520) · [pdf](https://arxiv.org/pdf/2606.17520.pdf)
  > 💡 提出基于3DGS的自动化系统GASE，利用全景相机阵列和位姿策略高效构建仿真环境，分割精度提升10%以上并实现最优修补。

  <details><summary>Abstract</summary>

  Training embodied agents in the real world requires skilled operators and expensive hardware. Simulation environments offer a compelling alternative by enabling large-scale, cost-effective data augmentation. Consequently, rapidly constructing high-fidelity simulation scenes with a minimal sim-to-real gap has become a critical objective in robot learning. While reconstruction-based methods provide superior visual quality, current workflows are hindered by inefficient data acquisition and subpar foreground object extraction. We thus propose GASE, a highly automated system for simulation scene construction. GASE leverages multi-view video streams from panoramic camera arrays to enable rapid environment scanning. To ensure high-quality asset generation, our pipeline introduces a camera-pose-based strategy that robustly extracts objects across frames in the 2D domain, followed by high-fidelity scene inpainting. Foreground objects and the static background are then reconstructed independently and seamlessly imported into physics simulators for policy training. Extensive experiments demonstrate that GASE outperforms existing 3D Gaussian-based methods in segmentation accuracy by over 10\% while achieving state-of-the-art inpainting quality. Furthermore, real-robot deployments across manipulation and navigation tasks maintains a performance gap of less than 10\% compared to policies trained purely on real-world data. These results confirm that GASE provides an efficient and highly effective solution for bridging the sim-to-real gap. Code will be released.

  </details>

## 2026-06-10

- **[ABot-Earth 0.5: Generative 3D Earth Model](https://arxiv.org/abs/2606.09967)**  
  *Ming Qian, Tianjian Ouyang, Mingchao Sun, Zijian Wang, Jincheng Xiong, Jiarong Han, Yongchang Zhang, Jiawei Zhang, Xu Wang, Yu Liu, Luyang Tang, Fei Yu, Zengye Ge, Mengmeng Du, Yuan Liu, Nianfei Fan, Song Wang, Yingliang Peng, Chunxue Jia, Yang Liu, Shiying Zeng, Haozhe Shi, Junnan Lai, Hongyu Pan, Zheng Wu, Ning Guo, Mu Xu, Hang Zhang*  
  `2026-06-08` · `cs.CV` · [abs](https://arxiv.org/abs/2606.09967) · [pdf](https://arxiv.org/pdf/2606.09967.pdf)
  > 💡 利用3DGS生成模型，从卫星图像快速合成大规模真实3D场景，支持实时Web可视化与具身AI应用。

  <details><summary>Abstract</summary>

  We present ABot-Earth 0.5, a generative 3D framework designed to synthesize vast, seamless 3D environments from ubiquitous, geospatially referenced satellite imagery. To achieve this, we propose a novel generative model formulated directly with the 3D Gaussian Splatting (3DGS) representation. The model is trained on a diverse corpus of existing real-world urban reconstructions, learning to generate realistic geometry and textures. At inference, it synthesizes novel 3D scenes conditioned solely on satellite imagery at a scalable rate of under 10 minutes per square kilometer, while demonstrating exceptional realism. The framework is designed for accessibility, with integrated hierarchical level-of-detail (LOD) structures that permit real-time, interactive visualization on web-based map engines. This high-fidelity simulation sandbox effectively mitigates the sim-to-real domain gap, enabling critical downstream Embodied AI applications like closed-loop UAV navigation. By providing an ultra-low-cost and high-efficiency solution, ABot-Earth 0.5 significantly lowers the technical and financial barriers to large-scale 3D reconstruction and empowers the future of global digital earth visualization.

  </details>

## 2026-06-09

- **[Leveraging NeRF-Rendered Images for 3D Gaussian Splatting](https://arxiv.org/abs/2606.09034)**  
  *Mizuki Morikawa, Yuta Shimizu, Chunyu Li, Yusuke Monno, Masatoshi Okutomi*  
  `2026-06-08` · `cs.CV` · [abs](https://arxiv.org/abs/2606.09034) · [pdf](https://arxiv.org/pdf/2606.09034.pdf)
  > 💡 利用街景NeRF渲染图像辅助3DGS训练，移除瞬态物体并添加鸟瞰视图，结合扩散增强，兼顾渲染速度与质量。

  <details><summary>Abstract</summary>

  Neural radiance field (NeRF) and 3D Gaussian splatting (3DGS) are two mainstream approaches for novel view synthesis. They often show complementary performance, i.e., 3DGS demonstrating faster rendering speed and NeRF demonstrating higher rendering quality. Motivated by this, we propose leveraging NeRF-rendered images for 3DGS. Specifically, we target street scenes and utilize a pre-trained street-specific NeRF method to produce training images for a target 3DGS method. In our 3DGS training, NeRF-rendered images are used to remove transient objects in street-level input views and to generate bird's-eye views as additional views, inheriting the higher-quality rendering of NeRF into 3DGS. We further incorporate a diffusion-based image enhancement to improve the image quality of the additional views. Experimental results on one synthetic and two real datasets demonstrate that our proposed method improves street-scene rendering while preserving the speed of 3DGS and the quality of NeRF.

  </details>

- **[LEGS: Laplacian-Enhanced Gaussian Splatting with a Nonlinear Weighted Loss](https://arxiv.org/abs/2606.07932)**  
  *Yongfei Guo, Qizhou Huo, Xuan Sun, Yuanhao Gong*  
  `2026-06-06` · `cs.CV` · [abs](https://arxiv.org/abs/2606.07932) · [pdf](https://arxiv.org/pdf/2606.07932.pdf)
  > 💡 用二阶拉普拉斯非线性加权损失替代一阶梯度，增强高斯溅射的结构感知，渲染质量提升达1.68dB。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has become an efficient explicit representation for radiance field reconstruction and real-time novel view synthesis. However, its standard photometric loss treats flat and structure-rich regions similarly, which may limit the recovery of sharp contours and fine details. Edge-Guided Gaussian Splatting (EGGS) improves structure awareness through edge-guided weighting, but mainly relies on first-order gradient responses and linear weighting. In this paper, we propose LEGS, a Laplacian-Enhanced Gaussian Splatting method with a nonlinearly weighted loss. LEGS replaces first-order gradient guidance with second-order Laplacian structural guidance and maps the normalized Laplacian response into pixel-wise weights through nonlinear response-to-weight functions. The proposed loss improves structure-aware Gaussian optimization while keeping the original 3DGS rendering pipeline unchanged. Experiments on the full Tanks\&Temples and Mip-NeRF360 datasets show that LEGS improves peak signal-to-noise ratio (PSNR) by up to 1.68 dB over 3DGS and up to 0.52 dB over EGGS. Incorporating the proposed second-order nonlinear weighting strategy into FastGS and FasterGS further improves PSNR by up to 1.69 dB, demonstrating its effectiveness as a general loss-level extension for Gaussian Splatting pipelines with potential applications in AR/VR, immersive visualization, and real-time 3D content generation.

  </details>

## 2026-06-06

- **[Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image](https://arxiv.org/abs/2606.02068)**  
  *Kaidi Zhang, Guanxu Zhu*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.02068) · [pdf](https://arxiv.org/pdf/2606.02068.pdf)
  > 💡 利用点图初始化MPI和一步扩散优化，实现比3DGS快30.7%、模型缩小85.2%的轻量级新视角合成。

  <details><summary>Abstract</summary>

  Recently, novel view synthesis has witnessed remarkable progress, with mainstream methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) delivering impressive results. However, these approaches often struggle to balance rendering speed and model size, and their optimization-based training can be highly time-consuming. Furthermore, they typically rely on dense observations, often failing to produce satisfactory results under sparse-view conditions. Although feed-forward reconstruction significantly reduces the optimization time of 3DGS, its pixel-aligned formulation generates millions of Gaussians from a single image, severely limiting its practical deployment on mobile devices. To address these limitations, we revisit the Multiplane Image(MPI) representation, which represents scenes using a compact set of planar layers for efficient novel view synthesis. Leveraging recent advances in visual foundation models, we utilize predicted point maps for reliable geometric initialization, followed by differentiable optimization. To address the issues of holes and artifacts in sparsely initialized MPI, we introduce one-step diffusion, which participates in both the differentiable optimization of MPI and the postprocessing of rendering results. Compared with a representative GS-based method, our approach is 30.7% faster and uses only 14.8% of its model size, while achieving competitive synthesis quality on front-view scenarios

  </details>

- **[DeblurNVS: Geometric Latent Diffusion for Novel View Synthesis from Sparse Motion-Blurred Images](https://arxiv.org/abs/2606.01315)**  
  *Changyue Shi, Wangbo Yu, Chaoran Feng, Li Yuan*  
  `2026-05-31` · `cs.CV` · [abs](https://arxiv.org/abs/2606.01315) · [pdf](https://arxiv.org/pdf/2606.01315.pdf)
  > 💡 从稀疏运动模糊图像合成新视图，提出几何潜在扩散恢复结构表征，无需逐场景优化。

  <details><summary>Abstract</summary>

  Novel view synthesis (NVS) is a fundamental problem in computer vision and graphics. Recent advances in neural radiance fields (NeRF), 3D Gaussian Splatting (3DGS), and generative view synthesis have substantially improved its quality. Yet most methods still rely on clean observations, where image structures and cross-view geometric cues are well preserved. Motion blur breaks this assumption by corrupting local details and weakening multi-view correspondences. Such blur commonly arises from camera shake, scene motion, or finite exposure in practical capture. Blur-aware NVS methods address this degradation by modeling image formation, but their reliance on costly per-scene optimization limits efficient and generalizable sparse-view synthesis. To address this, we propose DeblurNVS, a novel framework for synthesizing high-fidelity novel views directly from sparse motion-blurred images, without requiring per-scene optimization. DeblurNVS restores the intermediate geometric representations needed for multi-view reasoning, enabling blurred inputs to recover reliable structure and correspondence cues. The restored representations are then combined with target camera information to synthesize the target-view representation and reconstruct a sharp RGB novel view. To enable the large-scale training, we construct a motion-blurred NVS dataset from DL3DV-10K using interpolation-based finite-exposure blur synthesis. Extensive experiments demonstrate that DeblurNVS outperforms existing baselines on synthetic motion-blur benchmarks and generalizes to real motion-blurred scenes, producing perceptually sharper and structurally more stable novel views while avoiding costly per-scene optimization. Project page: https://github.com/PKU-YuanGroup/DeblurNVS.

  </details>

- **[Optimizing 3D Gaussian Splatting via Point Cloud Upsampling](https://arxiv.org/abs/2606.00450)**  
  *Adrian Ramlal, Yan Song Hu, John S. Zelek*  
  `2026-05-30` · `cs.CV` · [abs](https://arxiv.org/abs/2606.00450) · [pdf](https://arxiv.org/pdf/2606.00450.pdf)
  > 💡 利用多种点云上采样和深度引导方法优化3DGS初始化，提升重建质量，并给出场景适应性选择建议。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a technique for creating and rendering 3D scenes, however its performance depends heavily on the quality of initial seed points. To improve 3DGS initialization, this study presents and evaluates several point cloud upsampling approaches: linear interpolation, triangular interpolation, spline-based surface reconstruction, moving least squares surface fitting, and Voronoi-based point generation. Additionally, this research introduces a depth-guided point lifting method that leverages depth maps to maintain geometric consistency with Structure-from-Motion (SfM) reconstructions. Through extensive experiments on the Mip-NeRF360 and Replica datasets, the proposed methods demonstrate improvements in reconstruction quality across diverse scene types. Results indicate that different upsampling strategies excel in different scenarios: surface reconstruction methods perform better with organic, detailed scenes, while simpler interpolation approaches are more suited for scenes dominated by piecewise-smooth geometries. In comparison, the depth-guided approach shows promise for adding geometry-aware points across the entire scene, importantly in texture-less regions. These findings, which provide preliminary practical guidelines for selecting appropriate upsampling methods based on scene characteristics and computational constraints, advances the understanding of how point cloud initialization affects 3DGS quality.

  </details>

## 2026-05-30

- **[TrackRef3D: Multi-View Consistent Track-then-Label for Open-World Referring Segmentation in 3D Gaussian Splatting](https://arxiv.org/abs/2605.26576)**  
  *Yuyang Tan, Renhe Zhang, Hang Zhang, Ao Li, Xin Tan*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26576) · [pdf](https://arxiv.org/pdf/2605.26576.pdf)
  > 💡 针对3DGS指代分割的多视图不一致和泛化差问题，TrackRef3D提出轨迹感知语义共识与

  <details><summary>Abstract</summary>

  Referring 3D Gaussian Splatting (R3DGS), which utilizes natural language for 3D object segmentation, has emerged as a crucial capability for embodied AI. However, existing methods typically rely on expensive per-scene manual annotation and per-view pseudo mask generation, which suffer from multi-view inconsistency and poor generalization to varying query specificities. To address this, we present TrackRef3D, a fully automatic pipeline that achieves open-world referring segmentation in 3D Gaussian Splatting (3DGS) without manual annotation by introducing a multi-view consistent track-then-label paradigm that fundamentally decouples object discovery from semantic grounding. Specifically, we propose a Trajectory-Aware Semantic Consensus Module (TSCM) which aggregates cross-view predictions via synonymous clustering and trajectory-aware voting to establish a canonical semantic identity, thereby ensuring multi-view consistency. Furthermore, we employ a visibility-aware description generation strategy to mitigate ambiguity and propose a Hybrid Training Strategy (HTS) that jointly optimizes coarse category semantics and fine-grained referential cues to ensure robustness under varying query specificities using a multi-positive contrastive objective. Extensive experiments on benchmarks demonstrate that TrackRef3D achieves state-of-the-art performance.

  </details>

- **[CodecSplat: Ultra-Compact Latent Coding for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.25563)**  
  *Pengpeng Yu, Runqing Jiang, Qi Zhang, Dingquan Li, Jing Wang, Yulan Guo*  
  `2026-05-25` · `cs.CV` · [abs](https://arxiv.org/abs/2605.25563) · [pdf](https://arxiv.org/pdf/2605.25563.pdf)
  > 💡 针对前馈3DGS场景表示不紧凑，提出CodecSplat对中间2D特征进行熵编码，避免压缩不规则高斯基元，比特率降低一个数量级。

  <details><summary>Abstract</summary>

  While feed-forward 3D Gaussian splatting reconstructs renderable Gaussian primitives from sparse context views without per-scene optimization, existing pipelines do not provide a compact scene representation for storage or transmission. A natural solution is to apply existing 3DGS compression methods to the generated Gaussian primitives. However, this approach operates on the final irregular 3D representation and is decoupled from the internal feature-to-Gaussian generation process, which limits compression efficiency. To address this, we introduce CodecSplat, an ultra-compact latent coding framework for feed-forward 3D Gaussian splatting. CodecSplat first encodes an intermediate 2D Gaussian-generation feature into an entropy-coded scene bitstream. At the decoder, the latent feature is reconstructed and used to predict depth and Gaussian parameters, which are then mapped to 3D Gaussian primitives. Note that, by integrating compression into the feed-forward Gaussian generation pipeline, CodecSplat avoids inefficient compression over irregular 3D Gaussian primitives and allows the codec to exploit the structured intermediate feature representation. We instantiate CodecSplat on a feed-forward Gaussian splatting backbone with depth-guided multi-view feature refinement and a hierarchical learned feature codec. On DL3DV and RealEstate10K datasets, CodecSplat achieves 23.56-26.36 dB and 24.76-27.05 dB PSNR with only 20.00-107.77 KiB and 3.37-12.51 KiB per scene, respectively. This is roughly one order of magnitude smaller than compressing feed-forward generated Gaussian primitives, while preserving controllable rate-distortion behavior.

  </details>

- **[GlowGS: Generative Semantic Feature Learning for 3D Gaussian Splatting in Nighttime Glow Scenes](https://arxiv.org/abs/2605.23602)**  
  *Beibei Lin, Xiao Cao, Jingyuan Guo, Robby T. Tan*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23602) · [pdf](https://arxiv.org/pdf/2605.23602.pdf)
  > 💡 针对夜间发光场景3DGS缺乏结构特征，利用扩散模型和视觉基础模型生成并学习语义特征，提升渲染质量。

  <details><summary>Abstract</summary>

  Existing 3DGS methods effectively render high-quality novel views in clear-day scenes. However, they struggle with night scenes, particularly in glow regions, due to the lack of structural features such as textures and edges, which are key cues for splatting-based reconstruction. To address this problem, we leverage a diffusion model and a Vision Foundation Model (VFM) to compensate for missing structural cues. Our method consists of two key novel ideas: semantic feature generation and novel-view semantic learning. First, semantic feature generation produces high-quality semantic features as implicit structural cues for novel views. Specifically, a diffusion model synthesizes novel views with unknown camera poses from training views, while a VFM evaluates their quality. Once high-quality novel views are identified, the VFM extracts robust features to construct the semantic feature bank. Second, novel-view semantic learning enables 3DGS to optimize rendered novel views without requiring ground truth. It achieves this by extracting semantic features from a rendered novel view, searching the feature bank for the most similar features, and minimizing their distance. This process enforces implicit structural constraints, ensuring semantically coherent, artifact-free rendered views. Extensive experiments demonstrate the effectiveness of our GlowGS in generating semantically accurate 3D views, showing significant improvements over existing methods.

  </details>

- **[Flow-based Gaussian Splatting for Continuous-Scale Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2605.22147)**  
  *Jiangwei Mo, Xi Lu, Hanlin Wu*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22147) · [pdf](https://arxiv.org/pdf/2605.22147.pdf)
  > 💡 针对遥感图像超分推理慢且缺乏连续尺度灵活性，提出FlowGS，结合流匹配与2D高斯泼溅实现高效任意尺度重建。

  <details><summary>Abstract</summary>

  High-resolution remote sensing images (RSIs) are crucial for Earth observation applications, yet acquiring them is often limited by sensor constraints and costs. In recent years, generative super-resolution (SR) methods, particularly diffusion models, have made significant progress. However, they typically require slow iterative inference with 40--1000 steps and exhibit limited flexibility in continuous-scale SR settings. To address these issues, we propose FlowGS, a generative reconstruction framework for arbitrary-scale SR of RSIs. FlowGS models the high-frequency detail representations between high- and low-resolution images and learns a continuous probability flow from noise to detail priors via flow matching (FM) constrained by shortcut consistency, thereby reducing generative complexity and improving inference efficiency. Additionally, we employ 2D Gaussian splatting to construct a continuous feature field, thereby enabling flexible reconstruction at arbitrary query locations. Experimental results show that FlowGS delivers competitive perceptual quality compared with existing methods in both continuous-scale and fixed-scale SR settings, with substantially improved inference efficiency.

  </details>

- **[Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction](https://arxiv.org/abs/2605.22420)**  
  *Henry Che, Jingkang Wang, Yun Chen, Ze Yang, Sivabalan Manivasagam, Raquel Urtasun*  
  `2026-05-21` · `cs.CV` · [abs](https://arxiv.org/abs/2605.22420) · [pdf](https://arxiv.org/pdf/2605.22420.pdf)
  > 💡 针对大视角下城市重建质量退化，提出扩散引导的通用增强器GenRe，快速修复3D高斯表示，实现鲁棒泛化。

  <details><summary>Abstract</summary>

  Urban scene reconstruction from real-world observations has emerged as a powerful tool for self-driving development and testing. While current neural rendering approaches achieve high-fidelity rendering along the recorded trajectories, their quality degrades significantly under large viewpoint shifts, limiting the applicability for closed-loop simulation. Recent works have shown promising results in using diffusion models to enhance quality at these challenging viewpoints and distill improvements back into 3D representations. However, they often require costly per-scene optimization, and the distilled representations remain fragile and fail to generalize beyond limited synthesized views. To address these limitations, we propose GenRe, a novel diffusion-guided generalizable enhancer for urban scene reconstruction. GenRe takes as input any pretrained 3D Gaussian representation and fixes the deficiencies within a few minutes. By learning to distill generative priors across diverse scenes, GenRe produces robust and high-fidelity representation efficiently that generalizes reliably to challenging unseen viewpoints (e.g., lane change). Experiments show that GenRe outperforms existing methods in both quality and efficiency and benefits various downstream tasks, enabling robust and scalable sensor simulation for autonomous driving.

  </details>

- **[CAdam: Context-Adaptive Moment Estimation for 3D Gaussian Densification in Generative Distillation](https://arxiv.org/abs/2605.20872)**  
  *SeungJeh Chung, Geonho Park, Misong Kim, HyeongYeop Kang*  
  `2026-05-20` · `cs.LG` · [abs](https://arxiv.org/abs/2605.20872) · [pdf](https://arxiv.org/pdf/2605.20872.pdf)
  > 💡 生成蒸馏中3DGS稠密化困境，CAdam利用梯度一阶矩与信噪比门控分离信号噪声，减少85-97%高斯点。

  <details><summary>Abstract</summary>

  Adaptive densification is the engine of 3D Gaussian Splatting (3DGS). However, when transposed to the optimization-based Generative Distillation paradigm, this reconstruction-native mechanism reveals fundamental limitations, resulting in inefficient representations cluttered with redundant primitives. We diagnose this failure as a Densification Dilemma stemming from the stochastic nature of generative guidance: the standard magnitude-based accumulation indiscriminately aggregates transient noise alongside geometric signals, making it difficult to strike a balance between over-densification and under-fitting. To resolve this, we introduce Context-Adaptive Moment Estimation (CAdam), a novel framework that reinterprets densification as a statistically grounded signal verification problem. CAdam leverages the first moment of gradients to exploit the interference principle, where stochastic fluctuations cancel out via destructive interference while consistent geometric drifts accumulate via constructive interference, effectively disentangling the underlying signal from the generative noise floor. This is further augmented by a quantile-based context awareness and an intrinsic Signal-to-Noise Ratio (SNR) gating mechanism, which ensure robust adaptation across optimization stages and enable the soft termination of densification. Extensive experiments across diverse objectives (SDS, ISM, VFDS) and strong generative 3DGS backbones show that CAdam reduces Gaussian count by 85%-97% relative to standard densification while preserving overall comparable perceptual quality. These results highlight signal-aware density control as a practical way to improve memory efficiency in optimization-based generative distillation.

  </details>

- **[Feed-Forward Gaussian Splatting from Sparse Aerial Views](https://arxiv.org/abs/2605.19949)**  
  *Dongli Wu, Zhuoxiao Li, Tongyan Hua, Yinrui Ren, Xiaobao Wei, Rongjun Qin, Wufan Zhao*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.19949) · [pdf](https://arxiv.org/pdf/2605.19949.pdf)
  > 💡 从稀疏航拍视图重建城市场景，AnyCity通过几何潜码与气动补全令牌生成门控残差更新，实现一致且秒级的前馈3D高斯重建。

  <details><summary>Abstract</summary>

  Reconstructing large-scale urban scenes from sparse aerial views is a crucial yet challenging task. Due to biased top-down and shallow-oblique camera poses, sparse aerial captures exhibit strong evidence imbalance: roofs and open regions are repeatedly observed, while facades, distant buildings, and occluded structures receive little multi-view support. Existing feed-forward 3D Gaussian Splatting methods directly regress a deterministic representation from sparse inputs, but this often leads to ghosting, melted facades, and stretched textures. Recent pseudo-view and video-based generative reconstruction methods use additional supervision or generative priors. However, they often lack a clear separation between observed geometry and prior-driven content, which can lead to plausible but inconsistent structures. We propose AnyCity, an observation-grounded generative reconstruction framework for sparse aerial urban scenes. AnyCity first predicts an observation-supported geometry latent to anchor reliable structures, and then uses scaffold-conditioned aerial completion tokens to predict a gated residual update for weakly constrained content before Gaussian decoding. During training, dense-to-sparse distillation transfers structural cues from dense-view reconstruction, while an aerial-adapted video diffusion prior provides fine-grained urban appearance cues through gated token conditioning. Observation-preserving objectives keep the refined representation consistent with input-supported geometry. At inference time, AnyCity reconstructs the final 3D Gaussian scene from sparse aerial views in a single feed-forward pass, achieving coherent urban novel-view synthesis with second-level inference. Experiments on synthetic, aerial-domain, UAV-textured, and real-world scenes show consistent improvements over feed-forward baselines.

  </details>

- **[GaussianZoom: Progressive Zoom-in Generative 3D Gaussian Splatting with Geometric and Semantic Guidance](https://arxiv.org/abs/2605.18252)**  
  *Jiale Shi, Jiarui Hu, Zesong Yang, Kaixuan Luan, Hujun Bao, Zhaopeng Cui*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18252) · [pdf](https://arxiv.org/pdf/2605.18252.pdf)
  > 💡 针对低分辨率输入的极距放大渲染，提出渐进式3D高斯泼溅，结合几何一致建模与多尺度语义推理，实现高质量多视图一致放大。

  <details><summary>Abstract</summary>

  We introduce GaussianZoom, a generative zoom-in 3D reconstruction system with an iterative progressive framework that combines geometry-consistent scene modeling and multi-scale semantic reasoning to enable high-fidelity extreme zoom-in rendering from low-resolution inputs. To achieve this, we develop a novel multi-view consistent super-resolution module with depth-based feature warping and VLM-driven detail synthesis, ensuring accurate multi-view correspondence while enriching fine-scale appearance beyond the observed resolution. To support zooming across large magnification ranges, we further introduce a new expandable continuous Level-of-Detail hierarchy that dynamically modulates Gaussian visibility for smooth, alias-free cross-scale rendering. Experiments on Mip-NeRF360 and Tanks\&Temples demonstrate that GaussianZoom achieves superior perceptual quality, multi-view consistency, and robustness under extreme magnification, establishing a strong baseline for generative zoom-in 3D scene reconstruction.

  </details>

- **[Eff-WRFGS: Efficient Wireless Radiance Field Using 3D Gaussian Splatting](https://arxiv.org/abs/2605.15324)**  
  *Chenghong Bian, Meng Hua, Deniz Gunduz*  
  `2026-05-14` · `eess.SP` · [abs](https://arxiv.org/abs/2605.15324) · [pdf](https://arxiv.org/pdf/2605.15324.pdf)
  > 💡 针对无线信道建模效率问题，提出基于3DGS的可学习mask剪枝法，实现44倍存储压缩与7倍渲染加速。

  <details><summary>Abstract</summary>

  Wireless channel modeling is a key building block for next-generation wireless systems. Predicting the channel state information (CSI) across different transmitter locations can substantially reduce the pilot and feedback overhead of conventional channel estimation. We propose Eff-WRFGS, an efficient wireless radiance field modeling framework built upon 3D Gaussian Splatting. Eff-WRFGS introduces a learnable mask for each 3D Gaussian primitive to indicate its importance, which guides the pruning of less significant primitives for more efficient rendering. The model is trained using a weighted combination of rendering and regularization losses, allowing a flexible trade-off between rendering quality and efficiency. Numerical results on the $\text{NeRF}^2$ dataset demonstrate that Eff-WRFGS achieves up to 44$\times$ storage reduction and 7$\times$ rendering speed-up with only marginal quality degradation. Moreover, initializing the Gaussian primitives from a 3D point cloud of the scene further improves the entire quality-efficiency trade-off.

  </details>

- **[PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135)**  
  *Adil Qureshi, Dongki Jung, Jaehoon Choi, Dinesh Manocha*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.14135) · [pdf](https://arxiv.org/pdf/2605.14135.pdf)
  > 💡 对稀疏视图室内场景，提出全景补全和平面感知注意力引导，无需训练扩散模型，实现高质量新视角合成，PSNR提升17.8%。

  <details><summary>Abstract</summary>

  We present PanoPlane, an approach for high-fidelity sparse-view indoor novel view synthesis that reconstructs closed room geometry via panoramic scene completion. Unlike perspective-based methods that generate training views from limited fields of view, PanoPlane leverages $360^{\circ}$ panoramic completion to condition the generative process on the full spatial layout. We propose Layout Anchored Attention Steering, a training-free mechanism that steers attention within the diffusion model's internal representation toward scene's detected planar surfaces at inference time. By directing each unobserved region's attention toward geometrically consistent observed content, our method replaces unconstrained hallucination with grounded surface extrapolation. The resulting panoramic completions provide supervision for 3D Gaussian Splatting, enabling accurate novel-view synthesis across unobserved regions from as few as three input views. Experiments on Replica, ScanNet++, and Matterport3D demonstrate state-of-the-art novel view synthesis quality across 3, 6, and 9 input views, achieving up to $+17.8\%$ improvement in PSNR over the current state-of-the-art baseline without any training or fine-tuning of the diffusion model.

  </details>

- **[OCH3R: Object-Centric Holistic 3D Reconstruction](https://arxiv.org/abs/2605.13018)**  
  *Yi Du, Yang You, Xiang Wan, Leonidas Guibas*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13018) · [pdf](https://arxiv.org/pdf/2605.13018.pdf)
  > 💡 提出OCH3R，用Transformer单次前向从单图同时预测所有物体6D姿态与3D高斯重建，实现全前馈且与物体数无关的快速高保真重建。

  <details><summary>Abstract</summary>

  Object-centric scene understanding is a fundamental challenge in computer vision. Existing approaches often rely on multi-stage pipelines that first apply pre-trained segmentors to extract individual objects, followed by per-object 3D reconstruction. Such methods are computationally expensive, fragile to segmentation errors, and scale poorly with scene complexity. We introduce OCH3R, a unified framework for Object-Centric Holistic 3D Reconstruction from a single RGB image. OCH3R performs one forward pass to simultaneously predict all object instances with their 6D poses and detailed 3D reconstructions. The key idea is a transformer architecture that predicts per-pixel attributes, including CLIP-based category embeddings, metric depth, normalized object coordinates (NOCS), and a fixed number of 3D Gaussians representing each object. To supervise these Gaussian reconstructions, we transform them into canonical space using the predicted 6D poses and align them with pre-rendered canonical ground truth, avoiding costly per-image Gaussian label generation. On standard indoor benchmarks, OCH3R achieves state-of-the-art performance across monocular depth estimation, open-vocabulary semantic segmentation, and RGB-only category-level 6D pose estimation, while producing high-fidelity, editable per-object reconstructions. Crucially, inference is fully feed-forward and scales independently of the number of objects, offering orders-of-magnitude speedups over conventional multi-stage pipelines in cluttered scenes.

  </details>

- **[GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://arxiv.org/abs/2605.12399)**  
  *Xiao Cao, Yuze Li, Youmin Zhang, Jiayu Song, Cheng Yan, Wen Li, Lixin Duan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12399) · [pdf](https://arxiv.org/pdf/2605.12399.pdf)
  > 💡 针对稀疏视图下3DGS渲染特征受损导致跨视角检索错误，提出GeoQuery框架，用深度映射构建几何对齐代理查询和局部窗口注意力，实现鲁棒重建。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a prominent paradigm for 3D reconstruction and novel view synthesis. However, it remains vulnerable to severe artifacts when trained under sparse-view constraints. While recent methods attempt to rectify artifacts in rendered views using image diffusion models, they typically rely on multi-view self-attention to retrieve information from reference images. We observe that this mechanism often fails when the rendered novel views output by 3DGS are heavily corrupted: damaged query features lead to erroneous cross-view retrieval, resulting in inconsistent rendering refinement. To address this, we propose GeoQuery, a geometry-guided diffusion framework that integrates generative priors with explicit geometric cues via a novel Geometry-guided Cross-view Attention (GCA) mechanism. First, by leveraging predicted depth maps and camera poses, we construct a geometry-induced correspondence field to sample reference features, forming a geometry-aligned proxy query that replaces the corrupted rendering features. Furthermore, we design a new cross-view feature aggregation pipeline, in which we restrict the cross-view attention to a local window around each proxy query to effectively retrieve useful features while suppressing spurious matches. GeoQuery can be seamlessly integrated into existing diffusion-based pipelines, enabling robust reconstruction even under extreme view sparsity. Extensive experiments on sparse-view novel view synthesis and rendering artifact removal demonstrate the effectiveness of our approach.

  </details>

- **[PoseCompass: Intelligent Synthetic Pose Selection for Visual Localization](https://arxiv.org/abs/2605.12144)**  
  *Yanan Zhou, Zhaoyan Qian, Yanli Li, Nan Yang, Zhongliang Guo, Dong Yuan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12144) · [pdf](https://arxiv.org/pdf/2605.12144.pdf)
  > 💡 针对APR数据质量与冗余问题，提出PoseCompass智能姿态选择管道，融合三类评分机制，实现3倍加速与53.8%误差降低。

  <details><summary>Abstract</summary>

  In visual localization, Absolute Pose Regression (APR) enables real-time 6-DoF camera pose inference from single images, yet critically depends on fine-tuning data quality and coverage. While recent methods leverage 3D Gaussian Splatting (3DGS) for novel view synthesis-based data augmentation, random sampling generates redundant views and noisy samples from poorly reconstructed regions. To mitigate this research gap, we propose PoseCompass, an intelligent pose selection pipeline for 3DGS-based APR. PoseCompass formulates synthetic pose selection and derives a value-based pose ranking mechanism to identify informative poses. The ranking integrates three dimensions: Localization Difficulty, favoring challenging regions; Coverage Novelty, exploring under-sampled areas; and Rendering Observability, filtering artifacts and noise. PoseCompass then generates trajectory-constrained candidates, selects the top-K ranked poses, and synthesizes views using 3DGS with lightweight diffusion-based alignment. Finally, the pose regressor is fine-tuned on mixed real and synthetic data. We evaluate PoseCompass on 7-Scenes, where it reduces adaptation time from 15.2 to 5.1 minutes, a 3x speedup, while cutting median pose errors by 53.8 percent and significantly outperforming random baselines.

  </details>

- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424)**  
  *Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11424) · [pdf](https://arxiv.org/pdf/2605.11424.pdf)
  > 💡 稀疏视图下3DGS退化，VidSplat利用几何引导视频扩散先验迭代合成视角，实现鲁棒场景重建。

  <details><summary>Abstract</summary>

  Gaussian Splatting has achieved remarkable progress in multi-view surface reconstruction, yet it exhibits notable degradation when only few views are available. Although recent efforts alleviate this issue by enhancing multi-view consistency to produce plausible surfaces, they struggle to infer unseen, occluded, or weakly constrained regions beyond the input coverage. To address this limitation, we present VidSplat, a training-free generative reconstruction framework that leverages powerful video diffusion priors to iteratively synthesize novel views that compensate for missing input coverage, and thereby recover complete 3D scenes from sparse inputs. Specifically, we tackle two key challenges that enable the effective integration of generation and reconstruction. First, for 3D consistent generation, we elaborate a training-free, stage-wise denoising strategy that adaptively guides the denoising direction toward the underlying geometry using the rendered RGB and mask images. Second, to enhance the reconstruction, we develop an iterative mechanism that samples camera trajectories, explores unobserved regions, synthesizes novel views, and supplements training through confidence weighted refinement. VidSplat performs robustly to sparse input and even a single image. Extensive experiments on widely used benchmarks demonstrate our superior performance in sparse-view scene reconstruction.

  </details>

- **[PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266)**  
  *Zachary Lee, Maxwell Jacobson, Yexiang Xue*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.11266) · [pdf](https://arxiv.org/pdf/2605.11266.pdf)
  > 💡 3DGS缺乏物理理解，提出可微物理仿真耦合3D高斯，用物理目标引导形状优化，生成视觉逼真且物理功能正确的结构。

  <details><summary>Abstract</summary>

  Recent advances in Gaussian Splatting have enabled fast, high-fidelity 3D scene generation, yet these methods remain purely visual and lack an understanding of how shapes behave in the physical world. We introduce Physics-Guided 3D Gaussian Splatting (PG-3DGS), a framework that couples differentiable physics simulation with 3D Gaussian representations to generate 3D structures satisfying physics functionalities. By allowing physical objectives to guide the shape optimization process alongside visual losses, our approach produces geometries that are not only photometrically accurate but also physically functional. The model learns to adjust shapes so that the generated objects exhibit physically meaningful behaviors, for example, teapots that can pour and airplanes that can generate lift, without sacrificing visual quality. Experiments on pouring and aerodynamic lift tasks show that PG-3DGS improves physical functionality while preserving visual quality. In addition to simulation gains, bench-top physical lift tests with 3D-printed aircraft (Cessna, B-2 Spirit, and paper plane) under identical airflow conditions show higher scale-measured lift for PG-3DGS, generated structures than an appearance-matching baseline in all three cases. Our unified framework connects appearance-based reconstruction with physics-based reasoning, enabling end-to-end generation of 3D structures that both look realistic and function correctly.

  </details>

- **[ConFixGS: Learning to Fix Feedforward 3D Gaussian Splatting with Confidence-Aware Diffusion Priors in Driving Scenes](https://arxiv.org/abs/2605.09688)**  
  *Rui Song, Tianhui Cai, Markus Gross, Xingcheng Zhou, Zewei Zhou, Zhiyu Huang, Olaf Wysocki, Jiaqi Ma*  
  `2026-05-10` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09688) · [pdf](https://arxiv.org/pdf/2605.09688.pdf)
  > 💡 针对前馈3DGS在驾驶稀疏视图中的修复问题，ConFixGS利用置信度感知扩散先验和重投影交叉检查生成伪目标，显著提升新视角合成质量。

  <details><summary>Abstract</summary>

  Feedforward 3D Gaussian Splatting (3DGS) often struggles in trajectory-based sparse-view driving scenes. Existing Gaussian repair methods mainly target optimization-based 3DGS, while diffusion-based repair is typically restricted to iterative refinement near observed viewpoints, leaving feedforward 3DGS repair underexplored. We propose ConFixGS, a plug-and-play method that learns to fix feedforward 3DGS with confidence-aware diffusion priors. Starting from a pretrained feedforward model, ConFixGS generates diffusion-enhanced local pseudo-targets and validates them through reprojection-based cross-checking against support views. The resulting dense confidence maps guide refinement, enhancing reliable details while suppressing hallucinated or inconsistent evidence. On Waymo, nuScenes, and KITTI, ConFixGS improves challenging novel view synthesis, with PSNR gains of up to 3.68 dB and FID reduced by nearly half. Our results highlight confidence-aware fusion of generative priors and support-view consistency as a key principle for robust feedforward 3D driving scene reconstruction.

  </details>

- **[Generative 3D Gaussians with Learned Density Control](https://arxiv.org/abs/2605.16355)**  
  *Runjie Yan, Yan-Pei Cao, Peng Wang, Ding Liang, Yuan-Chen Guo*  
  `2026-05-08` · `cs.GR` · [abs](https://arxiv.org/abs/2605.16355) · [pdf](https://arxiv.org/pdf/2605.16355.pdf)
  > 💡 提出密度采样高斯，用可学习八叉树密度控制替代固定网格，实现自适应渲染基元与生成建模的统一，单图3D生成SOTA。

  <details><summary>Abstract</summary>

  We present Density-Sampled Gaussians (DeG), a novel 3D representation designed to bridge the gap between adaptive rendering primitives and scalable generative modeling. Unlike existing approaches that constrain 3D Gaussians to fixed voxel grids or arrays, DeG models Gaussian centers as samples from a learnable probability density function defined over an octree. This formulation provides a rigorous mathematical framework for adaptive density control: by jointly optimizing the spatial density and Gaussian attributes under rendering supervision, our model naturally concentrates primitives in regions of high geometric complexity. We achieve this via a new render loss contribution gradient that serves as a fully differentiable analogue to the discrete densification and pruning heuristics used in standard Gaussian Splatting. The resulting representation is highly flexible, supporting variable-resolution decoding from a single latent code by simply adjusting the sampling budget. To enable generative synthesis, we train a latent diffusion model on DeG. We identify a critical challenge in applying diffusion to unordered set-structured latents, which can significantly slow convergence, and propose VecSeq, a canonical re-indexing mechanism that anchors latent tokens to a deterministic 3D Sobol sequence. This transforms the ambiguous set-generation problem into a robust sequence modeling task. Extensive experiments demonstrate that our pipeline achieves state-of-the-art quality in single-image-to-3D generation, combining the structural adaptivity of unstructured primitives with the training stability of grid-based methods.

  </details>

- **[Sparse-to-Complete: From Sparse Image Captures to Complete 3D Scenes](https://arxiv.org/abs/2605.05664)**  
  *Yiyang Shen, Yin Yang, Kun Zhou, Tianjia Shao*  
  `2026-05-07` · `cs.CV` · [abs](https://arxiv.org/abs/2605.05664) · [pdf](https://arxiv.org/pdf/2605.05664.pdf)
  > 💡 针对稀疏输入场景，提出S2C-3D框架，利用扩散模型修复、视图一致性采样和轨迹规划实现完整高保真3D重建。

  <details><summary>Abstract</summary>

  We introduce S2C-3D, a novel sparse-view 3D reconstruction framework for high-fidelity and complete scene reconstruction from as few as six to eight images. Our framework features three components: a specialized diffusion model for scene-specific image restoration, a training-free view-consistency conditioned sampling process in the diffusion model for refined Gaussian optimization, and a camera trajectory planning scheme to ensure comprehensive scene coverage. The specialized diffusion model is developed by finetuning a pretrained architecture on the input views and their corresponding degraded counterparts. The adaptation to the scene distribution allows the model to repair Gaussian renderings while effectively eliminating domain gaps. Meanwhile, the trajectory planning scheme optimizes scene coverage by connecting each newly sampled camera to its two nearest neighbors. By iteratively constructing paths and retaining only those that significantly enhance visibility, the scheme establishes a trajectory that covers the entire scene. To address multi-view conflicts, the view-consistency conditioned sampling process quantifies the consistency between neighboring repaired images. This information is injected as a condition into the sampling process of the frozen diffusion model, facilitating the generation of view-consistent images without additional training. Consequently, our approach produces high-fidelity 3D Gaussians that are robust to artifacts. Experimental results demonstrate that S2C-3D outperforms state-of-the-art methods, constructing high-quality scenes that are free from missing regions, blurring, or other artifacts with very sparse inputs. The source code and data are available at https://gapszju.github.io/S2C-3D.

  </details>

- **[TAIL-Safe: Task-Agnostic Safety Monitoring for Imitation Learning Policies](https://arxiv.org/abs/2605.01195)**  
  *Riad Ahmed, Momotaz Begum*  
  `2026-05-02` · `cs.RO` · [abs](https://arxiv.org/abs/2605.01195) · [pdf](https://arxiv.org/pdf/2605.01195.pdf)
  > 💡 模仿学习策略部署不安全，提出Lipschitz连续Q函数定义安全集，结合3DGS数字孪生，实现任务无关的安全监控与恢复。

  <details><summary>Abstract</summary>

  Recent imitation learning (IL) algorithms such as flow-matching and diffusion policies demonstrate remarkable performance in learning complex manipulation tasks. However, these policies often fail even when operating within their training distribution due to extreme sensitivity to initial conditions and irreducible approximation errors that lead to compounding drift. This makes it unsafe to deploy IL policies in the field where out-of-distribution scenarios are prevalent. A prerequisite for safe deployment is enabling the policy to determine whether it can execute a task the way it was learned from demonstrations. This paper presents TAIL-Safe, a principled approach to identify, for a trained IL policy, a safe set from where the policy empirically succeeds in completing the learned task. We propose a Lipschitz-continuous Q-value function that maps state-action pairs to a long-term safety score based on three short-term task-agnostic criteria: visibility, recognizability, and graspability. The zero-superlevel set of this function characterizes an empirical control invariant set over state-action pairs. When the nominal policy proposes an action outside this set, we apply a recovery mechanism inspired by Nagumo's theorem that uses gradient ascent to the Q-function to steer the policy back to safety. To learn this Q-function, we construct a high-fidelity digital twin using Gaussian Splatting that enables systematic collection of failure data without risk to physical hardware. Experiments with a Franka Emika robot demonstrate that flow-matching policies, which fail under run-time perturbations, achieve consistent task success when guided by the proposed TAIL-Safe.

  </details>

- **[SandSim: Curve-Guided Gaussian Splatting for Reconstructing Sand Painting Processes](https://arxiv.org/abs/2604.27572)**  
  *Yilin Wang, Haojie Huang, Chen Li, Yang Li, Changbo Wang, Chenhui Li*  
  `2026-04-30` · `cs.GR` · [abs](https://arxiv.org/abs/2604.27572) · [pdf](https://arxiv.org/pdf/2604.27572.pdf)
  > 💡 针对单图沙画过程重建缺乏结构连贯问题，提出曲线引导高斯表示和各向异性基元，联合优化几何

  <details><summary>Abstract</summary>

  Sand painting is a process-driven art where visual appearance emerges from granular accumulation. Given a single image, reconstructing a plausible sand painting process requires modeling coherent stroke structures and material-dependent effects. Existing methods, including stroke-based optimization and diffusion-based video synthesis, often lack structural coherence and material consistency, leading to unrealistic drawing sequences. We present SandSim, a framework that reconstructs a sand painting process from a single image. We introduce a curve-guided Gaussian representation that models strokes as sequences of anisotropic primitives along continuous trajectories, whose smooth kernels capture the soft boundaries of sand strokes and enable coherent stroke formation. We further adopt a subtractive compositing scheme to model light attenuation during sand accumulation. We incorporate a semantic-guided planning module for scene decomposition and drawing order inference. Our framework jointly optimizes stroke geometry and appearance and can be integrated with a physics-based simulator for interactive sand dynamics and editing. Experiments show that our method produces temporally coherent and visually realistic results, achieving improved reconstruction quality and perceptual fidelity compared to existing approaches.

  </details>

- **[Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2604.27422)**  
  *Wongi Park, Jordan A. James, Myeongseok Nam, Minjae Lee, Soomok Lee, Sang-Hyun Lee, William J. Beksi*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.27422) · [pdf](https://arxiv.org/pdf/2604.27422.pdf)
  > 💡 针对无约束场景稀疏视图含干扰物问题，引入扩散模型参考引导细化及伪视图生成与稀疏感知复制，高质量3D渲染性能提升显著。

  <details><summary>Abstract</summary>

  We propose a 3D novel sparse-view synthesis framework for unconstrained real-world scenarios that contain distractors. Unlike existing methods that primarily perform novel-view synthesis from a sparse set of constrained images without transient elements or leverage unconstrained dense image collections to enhance 3D representation in real-world scenarios, our method not only effectively tackles sparse unconstrained image collections, but also shows high-quality 3D rendering results. To do this, we introduce reference-guided view refinement with a diffusion model using a transient mask and a reference image to enhance the 3D representation and mitigate artifacts in rendered views. Furthermore, we address sparse regions in the Gaussian field via pseudo-view generation along with a sparsity-aware Gaussian replication strategy to amplify Gaussians in the sparse regions. Extensive experiments on publicly available datasets demonstrate that our methodology consistently outperforms existing methods (e.g., PSNR - 17.2%, SSIM - 10.8%, LPIPS - 4.0%) and provides high-fidelity 3D rendering results. This advancement paves the way for realizing unconstrained real-world scenarios without labor-intensive data acquisition. Our project page is available at $\href{https://robotic-vision-lab.github.io/SaveWildGS/}{here}$

  </details>

- **[GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning](https://arxiv.org/abs/2604.25459)**  
  *Yufei Jia, Heng Zhang, Ziheng Zhang, Junzhe Wu, Mingrui Yu, Zifan Wang, Dixuan Jiang, Zheng Li, Chenyu Cao, Zhuoyuan Yu, Xun Yang, Haizhou Ge, Yuchi Zhang, Jiayuan Zhang, Zhenbiao Huang, Tianle Liu, Shenyu Chen, Jiacheng Wang, Bin Xie, Xuran Yao, Xiwa Deng, Guangyu Wang, Jinzhi Zhang, Lei Hao, Zhixing Chen, Yuxiang Chen, Anqi Wang, Hongyun Tian, Yiyi Yan, Zhanxiang Cao, Yizhou Jiang, Hanyang Shao, Yue Li, Lu Shi, Bokui Chen, Wei Sui, Hanqing Cui, Yusen Qin, Ruqi Huang, Lei Han, Tiancai Wang, Guyue Zhou*  
  `2026-04-28` · `cs.RO` · [abs](https://arxiv.org/abs/2604.25459) · [pdf](https://arxiv.org/pdf/2604.25459.pdf)
  > 💡 提出高通量视觉仿真框架，集成并行物理引擎与3DGS渲染，实现10^4 FPS及自动Real2Sim，加速视觉机器人学习。

  <details><summary>Abstract</summary>

  Embodied AI research is undergoing a shift toward vision-centric perceptual paradigms. While massively parallel simulators have catalyzed breakthroughs in proprioception-based locomotion, their potential remains largely untapped for vision-informed tasks due to the prohibitive computational overhead of large-scale photorealistic rendering. Furthermore, the creation of simulation-ready 3D assets heavily relies on labor-intensive manual modeling, while the significant sim-to-real physical gap hinders the transfer of contact-rich manipulation policies. To address these bottlenecks, we propose GS-Playground, a multi-modal simulation framework designed to accelerate end-to-end perceptual learning. We develop a novel high-performance parallel physics engine, specifically designed to integrate with a batch 3D Gaussian Splatting (3DGS) rendering pipeline to ensure high-fidelity synchronization. Our system achieves a breakthrough throughput of 10^4 FPS at 640x480 resolution, significantly lowering the barrier for large-scale visual RL. Additionally, we introduce an automated Real2Sim workflow that reconstructs photorealistic, physically consistent, and memory-efficient environments, streamlining the generation of complex simulation-ready scenes. Extensive experiments on locomotion, navigation, and manipulation demonstrate that GS-Playground effectively bridges the perceptual and physical gaps across diverse embodied tasks. Project homepage: https://gsplayground.github.io.

  </details>

- **[Power Foam: Unifying Real-Time Differentiable Ray Tracing and Rasterization](https://arxiv.org/abs/2604.24994)**  
  *Shrisudhan Govindarajan, Daniel Rebain, Dor Verbin, Kwang Moo Yi, Anish Prabhu, Andrea Tagliasacchi*  
  `2026-04-27` · `cs.GR` · [abs](https://arxiv.org/abs/2604.24994) · [pdf](https://arxiv.org/pdf/2604.24994.pdf)
  > 💡 将V

  <details><summary>Abstract</summary>

  We introduce a differentiable 3D representation that unifies the ray tracing capabilities of foam-based ray tracing with the efficiency of modern rasterization pipelines. While prior foam representations enable constant-time ray traversal through an explicit volumetric partition of space, their potentially unbounded cells hinder efficient tile-based rasterization. We address this limitation by generalizing Voronoi foams to bounded power diagrams with controllable cell extents, enabling spatially bounded primitives without requiring expensive Delaunay triangulations during training. We further introduce an oriented surface formulation that explicitly models interfaces between interior and exterior regions, and decouple geometry from appearance by embedding differentiable texture directly on these surfaces. Together, these contributions yield a representation that preserves state-of-the-art ray tracing efficiency while achieving rasterization performance competitive with current generation 3DGS, providing a practical path toward unified real-time differentiable rendering.

  </details>

- **[GS-DOT: Gaussian splatting-based image reconstruction for diffuse optical tomography](https://arxiv.org/abs/2604.23675)**  
  *Jingjing Jiang*  
  `2026-04-26` · `eess.IV` · [abs](https://arxiv.org/abs/2604.23675) · [pdf](https://arxiv.org/pdf/2604.23675.pdf)
  > 💡 首次将高斯散点引入光子扩散领域，用各向异性高斯基元优化拟合点扩散函数实现高精度重建，降低内存。

  <details><summary>Abstract</summary>

  This work presents GS-DOT, a novel image reconstruction framework based on Gaussian Splatting (GS) for diffuse optical tomography (DOT). Inspired by GS for rendering applications, absorption coefficients are represented as a sparse sum of anisotropic Gaussian primitives optimized to fit measured time-resolved point-spread functions through analytic gradients and Adam optimization. This is the first adaptation of GS algorithms in the photon diffusion regime, where the ray transport function is replaced by the diffusion functions to enable accurate modeling of light transport in highly scattering media. Validation on synthetic tissue models demonstrate high accuracy in localization and quantification of reconstructed absorption maps for both clean and noisy signals. GS-DOT has demonstrated high robustness to noise and showed a huge reduction in memory demand.

  </details>

- **[DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction](https://arxiv.org/abs/2604.21518)**  
  *Shiyan Su, Ruyi Zha, Danli Shi, Hongdong Li, Xuelian Cheng*  
  `2026-04-23` · `eess.IV` · [abs](https://arxiv.org/abs/2604.21518) · [pdf](https://arxiv.org/pdf/2604.21518.pdf)
  > 💡 稀疏视角CT重建中神经表示有伪影，提出DiffNR框架利用扩散先验和单步扩散模型SliceFixer修复，显著提升PSNR并保持高效优化。

  <details><summary>Abstract</summary>

  Neural representations (NRs), such as neural fields and 3D Gaussians, effectively model volumetric data in computed tomography (CT) but suffer from severe artifacts under sparse-view settings. To address this, we propose DiffNR, a novel framework that enhances NR optimization with diffusion priors. At its core is SliceFixer, a single-step diffusion model designed to correct artifacts in degraded slices. We integrate specialized conditioning layers into the network and develop tailored data curation strategies to support model finetuning. During reconstruction, SliceFixer periodically generates pseudo-reference volumes, providing auxiliary 3D perceptual supervision to fix underconstrained regions. Compared to prior methods that embed CT solvers into time-consuming iterative denoising, our repair-and-augment strategy avoids frequent diffusion model queries, leading to better runtime performance. Extensive experiments show that DiffNR improves PSNR by 3.99 dB on average, generalizes well across domains, and maintains efficient optimization.

  </details>

- **[FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038)**  
  *Haitao Huang, Shin-Fang Chng, Huangying Zhan, Qingan Yan, Yi Xu*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20038) · [pdf](https://arxiv.org/pdf/2604.20038.pdf)
  > 💡 针对测试时优化耗时且视图不一致问题，提出前馈框架结合跨视图正则化，实现稀疏视图3D编辑，极大加速推理。

  <details><summary>Abstract</summary>

  Recent advances in text-guided image editing and 3D Gaussian Splatting (3DGS) have enabled high-quality 3D scene manipulation. However, existing pipelines rely on iterative edit-and-fit optimization at test time, alternating between 2D diffusion editing and 3D reconstruction. This process is computationally expensive, scene-specific, and prone to cross-view inconsistencies. We propose a feed-forward framework for cross-view consistent 3D scene editing from sparse views. Instead of enforcing consistency through iterative 3D refinement, we introduce a cross-view regularization scheme in the image domain during training. By jointly supervising multi-view edits with geometric alignment constraints, our model produces view-consistent results without per-scene optimization at inference. The edited views are then lifted into 3D via a feedforward 3DGS model, yielding a coherent 3DGS representation in a single forward pass. Experiments demonstrate competitive editing fidelity and substantially improved cross-view consistency compared to optimization-based methods, while reducing inference time by orders of magnitude.

  </details>

- **[Asset Harvester: Extracting 3D Assets from Autonomous Driving Logs for Simulation](https://arxiv.org/abs/2604.18468)**  
  *Tianshi Cao, Jiawei Ren, Yuxuan Zhang, Jaewoo Seo, Jiahui Huang, Shikhar Solanki, Haotian Zhang, Mingfei Guo, Haithem Turki, Muxingzi Li, Yue Zhu, Sipeng Zhang, Zan Gojcic, Sanja Fidler, Kangxue Yin*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.18468) · [pdf](https://arxiv.org/pdf/2604.18468.pdf)
  > 💡 用稀疏视图多视图生成和3D高斯提升，将自动驾驶日志中的稀疏对象观测转为完整仿真资产

  <details><summary>Abstract</summary>

  Closed-loop simulation is a core component of autonomous vehicle (AV) development, enabling scalable testing, training, and safety validation before real-world deployment. Neural scene reconstruction converts driving logs into interactive 3D environments for simulation, but it does not produce complete 3D object assets required for agent manipulation and large-viewpoint novel-view synthesis. To address this challenge, we present Asset Harvester, an image-to-3D model and end-to-end pipeline that converts sparse, in-the-wild object observations from real driving logs into complete, simulation-ready assets. Rather than relying on a single model component, we developed a system-level design for real-world AV data that combines large-scale curation of object-centric training tuples, geometry-aware preprocessing across heterogeneous sensors, and a robust training recipe that couples sparse-view-conditioned multiview generation with 3D Gaussian lifting. Within this system, SparseViewDiT is explicitly designed to address limited-angle views and other real-world data challenges. Together with hybrid data curation, augmentation, and self-distillation, this system enables scalable conversion of sparse AV object observations into reusable 3D assets.

  </details>

- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268)**  
  *Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.14268) · [pdf](https://arxiv.org/pdf/2604.14268.pdf)
  > 💡 提出多模态世界模型HY-World 2.0，从文本/图像/视频生成3DGS场景，通过四阶段流程与多项创新实现开源最优性能。

  <details><summary>Abstract</summary>

  We introduce HY-World 2.0, a multi-modal world model framework that advances our prior project HY-World 1.0. HY-World 2.0 accommodates diverse input modalities, including text prompts, single-view images, multi-view images, and videos, and produces 3D world representations. With text or single-view image inputs, the model performs world generation, synthesizing high-fidelity, navigable 3D Gaussian Splatting (3DGS) scenes. This is achieved through a four-stage method: a) Panorama Generation with HY-Pano 2.0, b) Trajectory Planning with WorldNav, c) World Expansion with WorldStereo 2.0, and d) World Composition with WorldMirror 2.0. Specifically, we introduce key innovations to enhance panorama fidelity, enable 3D scene understanding and planning, and upgrade WorldStereo, our keyframe-based view generation model with consistent memory. We also upgrade WorldMirror, a feed-forward model for universal 3D prediction, by refining model architecture and learning strategy, enabling world reconstruction from multi-view images or videos. Also, we introduce WorldLens, a high-performance 3DGS rendering platform featuring a flexible engine-agnostic architecture, automatic IBL lighting, efficient collision detection, and training-rendering co-design, enabling interactive exploration of 3D worlds with character support. Extensive experiments demonstrate that HY-World 2.0 achieves state-of-the-art performance on several benchmarks among open-source approaches, delivering results comparable to the closed-source model Marble. We release all model weights, code, and technical details to facilitate reproducibility and support further research on 3D world models.

  </details>

- **[Dehaze-then-Splat: Generative Dehazing with Physics-Informed 3D Gaussian Splatting for Smoke-Free Novel View Synthesis](https://arxiv.org/abs/2604.13589)**  
  *Boss Chen, Hanqing Wang*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13589) · [pdf](https://arxiv.org/pdf/2604.13589.pdf)
  > 💡 针对逐帧去雾导致多视图不一致问题，提出融合物理先验与MCMC密度化的3DGS方法，提升新视图合成质量。

  <details><summary>Abstract</summary>

  We present Dehaze-then-Splat, a two-stage pipeline for multi-view smoke removal and novel view synthesis developed for Track~2 of the NTIRE 2026 3D Restoration and Reconstruction Challenge. In the first stage, we produce pseudo-clean training images via per-frame generative dehazing using Nano Banana Pro, followed by brightness normalization. In the second stage, we train 3D Gaussian Splatting (3DGS) with physics-informed auxiliary losses -- depth supervision via Pearson correlation with pseudo-depth, dark channel prior regularization, and dual-source gradient matching -- that compensate for cross-view inconsistencies inherent in frame-wise generative processing. We identify a fundamental tension in dehaze-then-reconstruct pipelines: per-image restoration quality does not guarantee multi-view consistency, and such inconsistency manifests as blurred renders and structural instability in downstream 3D reconstruction.Our analysis shows that MCMC-based densification with early stopping, combined with depth and haze-suppression priors, effectively mitigates these artifacts. On the Akikaze validation scene, our pipeline achieves 20.98\,dB PSNR and 0.683 SSIM for novel view synthesis, a +1.50\,dB improvement over the unregularized baseline.

  </details>

- **[Rethinking Image-to-3D Generation with Sparse Queries: Efficiency, Capacity, and Input-View Bias](https://arxiv.org/abs/2604.13905)**  
  *Zhiyuan Xu, Jiuming Liu, Yuxin Chen, Masayoshi Tomizuka, Chenfeng Xu, Chensheng Peng*  
  `2026-04-15` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13905) · [pdf](https://arxiv.org/pdf/2604.13905.pdf)
  > 💡 用稀疏3D锚点查询和扩展算子生成3D高斯原语，降低输入视图偏差，显著提升效率与容量。

  <details><summary>Abstract</summary>

  We present SparseGen, a novel framework for efficient image-to-3D generation, which exhibits low input-view bias while being significantly faster. Unlike traditional approaches that rely on dense volumetric grids, triplanes, or pixel-aligned primitives, we model scenes with a compact sparse set of learned 3D anchor queries and a learned expansion operator that decodes each transformed query into a small local set of 3D Gaussian primitives. Trained under a rectified-flow reconstruction objective without 3D supervision, our model learns to allocate representation capacity where geometry and appearance matter, achieving significant reductions in memory and inference time while preserving multi-view fidelity. We introduce quantitative measures of input-view bias and utilization to show that sparse queries reduce overfitting to conditioning views while being representationally efficient. Our results argue that sparse set-latent expansion is a principled, practical alternative for efficient 3D generative modeling.

  </details>

- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578)**  
  *Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu*  
  `2026-04-12` · `cs.CV` · [abs](https://arxiv.org/abs/2604.10578) · [pdf](https://arxiv.org/pdf/2604.10578.pdf)
  > 💡 利用视频扩散模型的时间先验与3DGS耦合，以恢复-优化范式生成全局一致的3D室内场景，显著提升长距离探索质量。

  <details><summary>Abstract</summary>

  The growing demand for Embodied AI and VR applications has highlighted the need for synthesizing high-quality 3D indoor scenes from sparse inputs. However, existing approaches struggle to infer massive amounts of missing geometry in large unseen areas while maintaining global consistency, often producing locally plausible but globally inconsistent reconstructions. We present Rein3D, a framework that reconstructs full 360-degree indoor environments by coupling explicit 3D Gaussian Splatting (3DGS) with temporally coherent priors from video diffusion models. Our approach follows a "restore-and-refine" paradigm: we employ a radial exploration strategy to render imperfect panoramic videos along trajectories starting from the origin, effectively uncovering occluded regions from a coarse 3DGS initialization. These sequences are restored by a panoramic video-to-video diffusion model and further enhanced via video super-resolution to synthesize high-fidelity geometry and textures. Finally, these refined videos serve as pseudo-ground truths to update the global 3D Gaussian field. To support this task, we construct PanoV2V-15K, a dataset of over 15K paired clean and degraded panoramic videos for diffusion-based scene restoration. Experiments demonstrate that Rein3D produces photorealistic and globally consistent 3D scenes and significantly improves long-range camera exploration compared with existing baselines.

  </details>

- **[FreeScale: Scaling 3D Scenes via Certainty-Aware Free-View Generation](https://arxiv.org/abs/2604.10512)**  
  *Chenhan Jiang, Yu Chen, Qingwen Zhang, Jifei Song, Songcen Xu, Dit-Yan Yeung, Jiankang Deng*  
  `2026-04-12` · `cs.CV` · [abs](https://arxiv.org/abs/2604.10512) · [pdf](https://arxiv.org/pdf/2604.10512.pdf)
  > 💡 利用场景重建与确定性感知自由视角采样，将有限真实图像转化为高质量训练数据，显著提升NVS与3DGS性能。

  <details><summary>Abstract</summary>

  The development of generalizable Novel View Synthesis (NVS) models is critically limited by the scarcity of large-scale training data featuring diverse and precise camera trajectories. While real-world captures are photorealistic, they are typically sparse and discrete. Conversely, synthetic data scales but suffers from a domain gap and often lacks realistic semantics. We introduce FreeScale, a novel framework that leverages the power of scene reconstruction to transform limited real-world image sequences into a scalable source of high-quality training data. Our key insight is that an imperfect reconstructed scene serves as a rich geometric proxy, but naively sampling from it amplifies artifacts. To this end, we propose a certainty-aware free-view sampling strategy identifying novel viewpoints that are both semantically meaningful and minimally affected by reconstruction errors. We demonstrate FreeScale's effectiveness by scaling up the training of feedforward NVS models, achieving a notable gain of 2.7 dB in PSNR on challenging out-of-distribution benchmarks. Furthermore, we show that the generated data can actively enhance per-scene 3D Gaussian Splatting optimization, leading to consistent improvements across multiple datasets. Our work provides a practical and powerful data generation engine to overcome a fundamental bottleneck in 3D vision. Project page: https://mvp-ai-lab.github.io/FreeScale.

  </details>

- **[SIC3D: Style Image Conditioned Text-to-3D Gaussian Splatting Generation](https://arxiv.org/abs/2604.08760)**  
  *Ming He, Zhixiang Chen, Steve Maddock*  
  `2026-04-09` · `cs.CV` · [abs](https://arxiv.org/abs/2604.08760) · [pdf](https://arxiv.org/pdf/2604.08760.pdf)
  > 💡 文本到3D生成缺乏可控性，提出SIC3D两阶段管线，用VSSD损失和缩放正则化实现风格迁移，提升几何与纹理保真度。

  <details><summary>Abstract</summary>

  Recent progress in text-to-3D object generation enables the synthesis of detailed geometry from text input by leveraging 2D diffusion models and differentiable 3D representations. However, the approaches often suffer from limited controllability and texture ambiguity due to the limitation of the text modality. To address this, we present SIC3D, a controllable image-conditioned text-to-3D generation pipeline with 3D Gaussian Splatting (3DGS). There are two stages in SIC3D. The first stage generates the 3D object content from text with a text-to-3DGS generation model. The second stage transfers style from a reference image to the 3DGS. Within this stylization stage, we introduce a novel Variational Stylized Score Distillation (VSSD) loss to effectively capture both global and local texture patterns while mitigating conflicts between geometry and appearance. A scaling regularization is further applied to prevent the emergence of artifacts and preserve the pattern from the style image. Extensive experiments demonstrate that SIC3D enhances geometric fidelity and style adherence, outperforming prior approaches in both qualitative and quantitative evaluations.

  </details>

- **[PR-IQA: Partial-Reference Image Quality Assessment for Diffusion-Based Novel View Synthesis](https://arxiv.org/abs/2604.04576)**  
  *Inseong Choi, Siwoo Lee, Seung-Hun Nam, Soohwan Song*  
  `2026-04-06` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04576) · [pdf](https://arxiv.org/pdf/2604.04576.pdf)
  > 💡 针对扩散生成视图的质量评估难题，提出PR-IQA利用部分参考图进行交叉注意力质量补全，有效筛选高置信区域提升3DGS重建。

  <details><summary>Abstract</summary>

  Diffusion models are promising for sparse-view novel view synthesis (NVS), as they can generate pseudo-ground-truth views to aid 3D reconstruction pipelines like 3D Gaussian Splatting (3DGS). However, these synthesized images often contain photometric and geometric inconsistencies, and their direct use for supervision can impair reconstruction. To address this, we propose Partial-Reference Image Quality Assessment (PR-IQA), a framework that evaluates diffusion-generated views using reference images from different poses, eliminating the need for ground truth. PR-IQA first computes a geometrically consistent partial quality map in overlapping regions. It then performs quality completion to inpaint this partial map into a dense, full-image map. This completion is achieved via a cross-attention mechanism that incorporates reference-view context, ensuring cross-view consistency and enabling thorough quality assessment. When integrated into a diffusion-augmented 3DGS pipeline, PR-IQA restricts supervision to high-confidence regions identified by its quality maps. Experiments demonstrate that PR-IQA outperforms existing IQA methods, achieving full-reference-level accuracy without ground-truth supervision. Thus, our quality-aware 3DGS approach more effectively filters inconsistencies, producing superior 3D reconstructions and NVS results. The project page is available at https://kakaomacao.github.io/pr-iqa-project-page/.

  </details>

- **[M2StyleGS: Multi-Modality 3D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2604.03773)**  
  *Xingyu Miao, Xueqi Qiu, Haoran Duan, Yawen Huang, Xian Wu, Jingjing Deng, Yang Long*  
  `2026-04-04` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03773) · [pdf](https://arxiv.org/pdf/2604.03773.pdf)
  > 💡 利用3DGS与CLIP多模态知识，通过特征对齐和损失函数实现灵活文本图像输入下的实时3D风格迁移，一致性提升32.92%。

  <details><summary>Abstract</summary>

  Conventional 3D style transfer methods rely on a fixed reference image to apply artistic patterns to 3D scenes. However, in practical applications such as virtual or augmented reality, users often prefer more flexible inputs, including textual descriptions and diverse imagery. In this work, we introduce a novel real-time styling technique M2StyleGS to generate a sequence of precisely color-mapped views. It utilizes 3D Gaussian Splatting (3DGS) as a 3D presentation and multi-modality knowledge refined by CLIP as a reference style. M2StyleGS resolves the abnormal transformation issue by employing a precise feature alignment, namely subdivisive flow, it strengthens the projection of the mapped CLIP text-visual combination feature to the VGG style feature. In addition, we introduce observation loss, which assists in the stylized scene better matching the reference style during the generation, and suppression loss, which suppresses the offset of reference color information throughout the decoding process. By integrating these approaches, M2StyleGS can employ text or images as references to generate a set of style-enhanced novel views. Our experiments show that M2StyleGS achieves better visual quality and surpasses the previous work by up to 32.92% in terms of consistency.

  </details>

- **[CGHair: Compact Gaussian Hair Reconstruction with Card Clustering](https://arxiv.org/abs/2604.03716)**  
  *Haimin Luo, Srinjay Sarkar, Albert Mosella-Montoro, Francisco Vicente Carrasco, Fernando De la Torre*  
  `2026-04-04` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03716) · [pdf](https://arxiv.org/pdf/2604.03716.pdf)
  > 💡 针对高开销头发重建，以聚类股线为卡片和共享纹理码本，

  <details><summary>Abstract</summary>

  We present a compact pipeline for high-fidelity hair reconstruction from multi-view images. While recent 3D Gaussian Splatting (3DGS) methods achieve realistic results, they often require millions of primitives, leading to high storage and rendering costs. Observing that hair exhibits structural and visual similarities across a hairstyle, we cluster strands into representative hair cards and group these into shared texture codebooks. Our approach integrates this structure with 3DGS rendering, significantly reducing reconstruction time and storage while maintaining comparable visual quality. In addition, we propose a generative prior accelerated method to reconstruct the initial strand geometry from a set of images. Our experiments demonstrate a 4-fold reduction in strand reconstruction time and achieve comparable rendering performance with over 200x lower memory footprint.

  </details>

- **[VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping](https://arxiv.org/abs/2604.02696)**  
  *Yuhan Zhu, Yanyu Zhang, Jie Xu, Wei Ren*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.02696) · [pdf](https://arxiv.org/pdf/2604.02696.pdf)
  > 💡 变分贝叶斯框架将地图与位姿追踪概率化，利用共轭先验闭式更新，解决初始化敏感与漂移问题。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has shown promising results for 3D scene modeling using mixtures of Gaussians, yet its existing simultaneous localization and mapping (SLAM) variants typically rely on direct, deterministic pose optimization against the splat map, making them sensitive to initialization and susceptible to catastrophic forgetting as map evolves. We propose Variational Bayesian Gaussian Splatting SLAM (VBGS-SLAM), a novel framework that couples the splat map refinement and camera pose tracking in a generative probabilistic form. By leveraging conjugate properties of multivariate Gaussians and variational inference, our method admits efficient closed-form updates and explicitly maintains posterior uncertainty over both poses and scene parameters. This uncertainty-aware method mitigates drift and enhances robustness in challenging conditions, while preserving the efficiency and rendering quality of existing 3DGS. Our experiments demonstrate superior tracking performance and robustness in long sequence prediction, alongside efficient, high-quality novel view synthesis across diverse synthetic and real-world scenes.

  </details>

- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207)**  
  *Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01207) · [pdf](https://arxiv.org/pdf/2604.01207.pdf)
  > 💡 用网格引导3DGS编辑，通过多视图锚点合成、有形几何锚定和上下文视频掩蔽，实现高保真部件级场景变换，保持结构完整性。

  <details><summary>Abstract</summary>

  We present TRACE, a mesh-guided 3DGS editing framework that achieves automated, high-fidelity scene transformation. By anchoring video diffusion with explicit 3D geometry, TRACE uniquely enables fine-grained, part-level manipulatio--such as local pose shifting or component replacemen--while preserving the structural integrity of the central subject, a capability largely absent in existing editing methods. Our approach comprises three key stages: (1) Multi-view 3D-Anchor Synthesis, which leverages a sparse-view editor trained on our MV-TRACE datase--the first multi-view consistent dataset dedicated to scene-coherent object addition and modificatio--to generate spatially consistent 3D-anchors; (2) Tangible Geometry Anchoring (TGA), which ensures precise spatial synchronization between inserted meshes and the 3DGS scene via two-phase registration; and (3) Contextual Video Masking (CVM), which integrates 3D projections into an autoregressive video pipeline to achieve temporally stable, physically-grounded rendering. Extensive experiments demonstrate that TRACE consistently outperforms existing methods especially in editing versatility and structural integrity.

  </details>

- **[SVGS: Single-View to 3D Object Editing via Gaussian Splatting](https://arxiv.org/abs/2603.28126)**  
  *Pengcheng Xue, Yan Tian, Qiutao Song, Ziyi Wang, Linyang He, Weiping Ding, Mahmoud Hassaballah, Karen Egiazarian, Wei-Fa Yang, Leszek Rutkowski*  
  `2026-03-30` · `cs.CV` · [abs](https://arxiv.org/abs/2603.28126) · [pdf](https://arxiv.org/pdf/2603.28126.pdf)
  > 💡 提出基于3D高斯泼溅的单视图编辑方法，利用多视图扩散模型保证一致性并显著提升编辑效率。

  <details><summary>Abstract</summary>

  Text-driven 3D scene editing has attracted considerable interest due to its convenience and user-friendliness. However, methods that rely on implicit 3D representations, such as Neural Radiance Fields (NeRF), while effective in rendering complex scenes, are hindered by slow processing speeds and limited control over specific regions of the scene. Moreover, existing approaches, including Instruct-NeRF2NeRF and GaussianEditor, which utilize multi-view editing strategies, frequently produce inconsistent results across different views when executing text instructions. This inconsistency can adversely affect the overall performance of the model, complicating the task of balancing the consistency of editing results with editing efficiency. To address these challenges, we propose a novel method termed Single-View to 3D Object Editing via Gaussian Splatting (SVGS), which is a single-view text-driven editing technique based on 3D Gaussian Splatting (3DGS). Specifically, in response to text instructions, we introduce a single-view editing strategy grounded in multi-view diffusion models, which reconstructs 3D scenes by leveraging only those views that yield consistent editing results. Additionally, we employ sparse 3D Gaussian Splatting as the 3D representation, which significantly enhances editing efficiency. We conducted a comparative analysis of SVGS against existing baseline methods across various scene settings, and the results indicate that SVGS outperforms its counterparts in both editing capability and processing speed, representing a significant advancement in 3D editing technology. For further details, please visit our project page at: https://amateurc.github.io/svgs.github.io.

  </details>

- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053)**  
  *Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni*  
  `2026-03-26` · `cs.CV` · [abs](https://arxiv.org/abs/2603.25053) · [pdf](https://arxiv.org/pdf/2603.25053.pdf)
  > 💡 针对3DGS野外重建伪影问题，用几何感知视频生成器结合高斯原语缓冲细化，实现高质量实时重建。

  <details><summary>Abstract</summary>

  We present GaussFusion, a novel approach for improving 3D Gaussian splatting (3DGS) reconstructions in the wild through geometry-informed video generation. GaussFusion mitigates common 3DGS artifacts, including floaters, flickering, and blur caused by camera pose errors, incomplete coverage, and noisy geometry initialization. Unlike prior RGB-based approaches limited to a single reconstruction pipeline, our method introduces a geometry-informed video-to-video generator that refines 3DGS renderings across both optimization-based and feed-forward methods. Given an existing reconstruction, we render a Gaussian primitive video buffer encoding depth, normals, opacity, and covariance, which the generator refines to produce temporally coherent, artifact-free frames. We further introduce an artifact synthesis pipeline that simulates diverse degradation patterns, ensuring robustness and generalization. GaussFusion achieves state-of-the-art performance on novel-view synthesis benchmarks, and an efficient variant runs in real time at 15 FPS while maintaining similar performance, enabling interactive 3D applications.

  </details>

