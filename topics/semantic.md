# Semantic / Scene Understanding

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---


## 2026-06-30

- **[Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors](https://arxiv.org/abs/2606.30638)**  
  *Jameel Hassan, Yasiru Ranasinghe, Vishal Patel*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30638) · [pdf](https://arxiv.org/pdf/2606.30638.pdf)
  > 💡 利用离散2D检测器和多视图

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

  </details>

- **[Rectifying Mask via Entropy for Distractor-Free 3DGS in Ambiguous Scenarios](https://arxiv.org/abs/2606.29496)**  
  *Wongi Park, Jiyeon Lim, Minjae Lee, Myeongseok Nam, Seongjun Choi, Jungwoo Kim, Soomok Lee, William J. Beksi, SangHyun Lee*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29496) · [pdf](https://arxiv.org/pdf/2606.29496.pdf)
  > 💡 用熵感知自适应掩膜和密度控制解决颜色或语义模糊场景中的干扰物问题，实现无干扰新视角合成。

  <details><summary>Abstract</summary>

  We present RefineSplat, a systematic framework that effectively constructs transient masks to identify diverse ambiguous distractors. To do this, we qualitatively and quantitatively analyze issues and propose a novel entropy-aware adaptive masking method. Unlike existing approaches that struggle to distinguish transient elements from static scenes due to color or semantic ambiguity, RefineSplat captures ambiguous distractors leveraging entropy and instance masks. Furthermore, we propose a simple yet effective entropy-aware density control to align Gaussians in ambiguous scenarios considering Entropy-aware positional gradients. Additionally, to rigorously validate our method, we first create and release the Ambiguous wild dataset, including 18 scenes where distractors and static scenes are hard to distinguish due to color or semantic resemblances. Experimental results on various datasets demonstrate that RefineSplat shows state-of-the-art performance, showing distractor-free novel view synthesis.

  </details>

- **[RefGlass-GS: A UAV-Enabled Fusion Framework for Photorealistic, Semantic and Interactive Digitization of Reflective Glass Facades via Gaussian Splatting](https://arxiv.org/abs/2606.28826)**  
  *Zhenyu Liang, Xiao Zhang, Boyu Wang, Zhaolun Liang, Ang Li, Jeff Chak Fu Chan, Mingzhu Wang, Jack C. P. Cheng*  
  `2026-06-27` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28826) · [pdf](https://arxiv.org/pdf/2606.28826.pdf)
  > 💡 针对反光玻璃幕墙数字化难题，提出RefGlass-GS融合框架，通过个体面板分割、视角优化和反射MLP增强高斯泼

  <details><summary>Abstract</summary>

  Existing digitization of buildings with reflective glass facades suffers from geometric reconstruction distortion, unrealistic view-dependent texture rendering, and difficulties in object-based semantic enhancement. Therefore, we propose RefGlass-GS, a fusion framework that enables end-to-end UAV-based photorealistic, semantic, and interactive digitization of reflective glass facades. The contributions include: (1) proposing an individual glass panel segmentation method based on maximum a posteriori estimation with structural regularities, robust to severe reflection and background interference; (2) formulating a UAV viewpoint planning optimization function that maximizes the coverage of view-dependent appearance for sufficient data capture; (3) developing an optimized Gaussian Splatting framework with a Reflection MLP, a novel deferred shading function, and two enhanced regularization terms for effective modeling of high-frequency near-field reflections; (4) introducing a standardized data organization paradigm for structuring GS-based representations into object-based models, facilitating interactive facility management on digital twin platforms. Experiments on real-world reflective glass facade scenes validate the effectiveness and superiority of the proposed method. Specifically, the glass panel segmentation achieves an improvement of 0.1927 in mIoU over SOTA methods, and only our method enables instance-level panel extraction. The UAV view planning improves novel view synthesis for reflective facades by 13.15 dB in PSNR compared to commercially used nap-of-the-object planning methods. The RefGlass-GS modeling outperforms SOTA Gaussian Splatting approaches for reflective scenes with an average improvement of 5.08 dB in PSNR.

  </details>

## 2026-05-30

- **[Comparative evaluation of photogrammetric reconstruction methods and 3D Gaussian Splatting for road surface roughness analysis](https://arxiv.org/abs/2605.29452)**  
  *Marouane Elmegdar, Teng Xiao*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29452) · [pdf](https://arxiv.org/pdf/2605.29452.pdf)
  > 💡 比较COLMAP等四种重建法评估路面粗糙度，3DGS噪声大但可捕获不规则，开源管道适于低成本监测。

  <details><summary>Abstract</summary>

  Image-based 3D reconstruction offers a low-cost alternative to traditional sensor-based techniques for road surface assessment. This study compares four reconstruction pipelines--COLMAP, Meshroom, Metashape, and 3D Gaussian Splatting (3DGS)--to evaluate their ability to estimate road surface roughness from smartphone imagery. All point clouds were processed in CloudCompare using a consistent workflow involving orientation alignment, segmentation, normal estimation, and roughness computation at neighborhood radiuses of 0.2, 0.4, and 0.6 model units. The results show that COLMAP provides the highest sensitivity to micro-texture, while Meshroom yields balanced reconstructions with moderate roughness variation. Metashape produces the smoothest geometry due to its internal filtering, and 3DGS captures visible irregularities but exhibits higher noise and lower density. The comparison demonstrates that open-source pipelines are viable for relative roughness evaluation, offering a practical approach for low-cost pavement monitoring.

  </details>

- **[Uncertainty-Aware Gaussian Map for Vision-Language Navigation](https://arxiv.org/abs/2605.26503)**  
  *Jianzhe Gao, Rui Liu, Yuxuan Xu, Tongtong Cao, Yingxue Zhang, Zhanguang Zhang, Sida Peng, Yi Yang, Wenguan Wang*  
  `2026-05-26` · `cs.CV` · [abs](https://arxiv.org/abs/2605.26503) · [pdf](https://arxiv.org/pdf/2605.26503.pdf)
  > 💡 提出感知不确定性（几何、语义、外观）问题，通过语义高斯地图建模并扩展为3D价值地图，提升视觉语言导航可靠性。

  <details><summary>Abstract</summary>

  Vision-Language Navigation (VLN) requires an agent to navigate 3D environments following natural language instructions. During navigation, existing agents commonly encounter perceptual uncertainty, such as insufficient evidence for reliable grounding or ambiguity in interpreting spatial cues, yet they typically ignore such information when predicting actions. In this work, we explicitly model three forms of perceptual uncertainty (i.e., geometric, semantic, and appearance uncertainty) and integrate them into the agent's observation space to enable informed decision-making. Concretely, our agent first constructs a Semantic Gaussian Map (SGM), composed of differentiable 3D Gaussian primitives initialized from panoramic observations, that encodes both the geometric structure and semantic content of the environment. On top of SGM, geometric uncertainty is estimated through variational perturbations of Gaussian position and scale to assess structural reliability; semantic uncertainty is captured by perturbing Gaussian semantic attributes to reveal ambiguous interpretations; and appearance uncertainty is characterized by Fisher Information, which measures the sensitivity of rendered observations to Gaussian-level variations. These uncertainties are incorporated into SGM, extending it into a unified 3D Value Map, which grounds them as affordances and constraints that support reliable navigation. Comprehensive evaluations across multiple VLN benchmarks show the effectiveness of our agent.

  </details>

- **[Uncovering and Shaping the Latent Representation of 3D Scene Topology in Vision-Language Models](https://arxiv.org/abs/2605.07148)**  
  *Haoming Wang, Wei Gao*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07148) · [pdf](https://arxiv.org/pdf/2605.07148.pdf)
  > 💡 通过跨场景线性特征提取分离被语义掩盖的3D场景拓扑潜表征，并引入Dirichlet能量正则化提升VLM空间推理达12.1%。

  <details><summary>Abstract</summary>

  Decades of cognitive science establish that humans navigate environments by forming cognitive maps, defined as allocentric and topology-preserving representations of 3D space. While modern Vision-Language Models (VLMs) demonstrate emergent spatial reasoning from 2D egocentric inputs, it remains unclear whether they construct an analogous 3D internal representation. In this paper, we demonstrate that current VLMs do possess a latent topological map of 3D scenes, but it is heavily overshadowed by non-geometric visual semantics, such as color and shape. By isolating this spatial subspace through cross-scene linear feature extraction, we extract a clean spatial subspace that causally controls the model's spatial outputs. We mathematically shape this latent representation and prove its correspondence to the Laplacian eigenmaps of the scene's 3D Gaussian-kernel graph, converging to the physical 3D space in the continuous limit. Motivated by this geometric identification, we further introduce a mathematically principled latent regularization method for VLMs, based on Dirichlet energy. Applying this single-term regularizer to a minimal 500-step supervised VLM fine-tuning (SFT) on simple synthetic data yields significant improvements on real-world spatial benchmarks, outperforming standard SFT and competitive baselines by up to 12.1\% in spatial tasks involving scene topology understanding. Source code is available at https://github.com/pittisl/vlm-latent-shaping

  </details>

- **[OpenGaFF: Open-Vocabulary Gaussian Feature Field with Codebook Attention](https://arxiv.org/abs/2605.06088)**  
  *Kunyi Li, Michael Niemeyer, Sen Wang, Stefano Gasperini, Nassir Navab, Federico Tombari*  
  `2026-05-07` · `cs.CV` · [abs](https://arxiv.org/abs/2605.06088) · [pdf](https://arxiv.org/pdf/2605.06088.pdf)
  > 💡 通过高斯特征场和码本注意力增强几何-语义耦合，实现开放词汇3D场景中一致且可解释的语义分割。

  <details><summary>Abstract</summary>

  Understanding open-vocabulary 3D scenes with Gaussian-based representations remains challenging due to fragmented and spatially inconsistent semantic predictions across multi-view observations. In this paper, we present OpenGaFF, a novel framework for open-vocabulary 3D scene understanding built upon 3D Gaussian Splatting. At the core of our method is a Gaussian Feature Field that models semantics as a continuous function of Gaussian geometry and appearance. By explicitly conditioning semantic predictions on geometric structure, this formulation strengthens the coupling between geometry and semantics, leading to improved spatial coherence across similar structures in 3D space. To further enforce object-level semantic consistency, we introduce a structured codebook that serves as a set of shared semantic primitives. Furthermore, a codebook-guided attention mechanism is proposed to retrieve language features via similarity matching between query embeddings and learned codebook entries, enabling robust open-vocabulary reasoning while reducing intra-object feature variance. Extensive experiments on standard 2D and 3D open-vocabulary benchmarks demonstrate that our method consistently outperforms prior approaches, achieving improved segmentation quality, stronger 3D semantic consistency and a semantically interpretable codebook that provides insight into the learned representation.

  </details>

- **[Ilov3Splat: Instance-Level Open-Vocabulary 3D Scene Understanding in Gaussian Splatting](https://arxiv.org/abs/2605.04506)**  
  *Binh Long Nguyen, Kien Nguyen, Sridha Sridharan, Clinton Fookes, Peyman Moghadam*  
  `2026-05-06` · `cs.CV` · [abs](https://arxiv.org/abs/2605.04506) · [pdf](https://arxiv.org/pdf/2605.04506.pdf)
  > 💡 用多分辨率哈希嵌入增强Gaussian splats的CLIP特征和实例特征场，实现无需标注的开放词汇实例分割。

  <details><summary>Abstract</summary>

  We introduce Ilov3Splat, a novel framework for instance-level open-vocabulary 3D scene understanding built on 3D Gaussian Splatting (3D-GS). Most prior work depends on 2D rendering-based matching or point-level semantic association, which undermines cross-view consistency, lacks coherent instance-level reasoning, and limits precision in downstream 3D tasks. To address these limitations, our method jointly optimizes scene geometry and semantic representations by augmenting Gaussian splats with view-consistent feature fields. Specifically, we leverage multi-resolution hash embedding to efficiently encode language-aligned CLIP features, enabling dense and coherent language grounding in 3D space. We further train an instance feature field using contrastive loss over SAM masks, supporting fine-grained object distinction across views. At inference time, CLIP-encoded queries are matched against the learned features, followed by two-stage 3D clustering to retrieve relevant Gaussian groups. This enables our framework to identify arbitrary objects in 3D scenes based on natural language descriptions, without requiring category supervision or manual annotations. Experiments on standard benchmarks demonstrate that Ilov3Splat outperforms prior open-vocabulary 3D-GS methods in both object selection and instance segmentation, offering a flexible and accurate solution for language-driven 3D scene understanding. Project page: https://csiro-robotics.github.io/Ilov3Splat.

  </details>

- **[NRGS: Neural Regularization for Robust 3D Semantic Gaussian Splatting](https://arxiv.org/abs/2604.22439)**  
  *Zaiyan Yang, Xinpeng Liu, Heng Guo, Jinglei Shi, Zhanyu Ma, Fumio Okura*  
  `2026-04-24` · `cs.CV` · [abs](https://arxiv.org/abs/2604.22439) · [pdf](https://arxiv.org/pdf/2604.22439.pdf)
  > 💡 针对多视图不一致特征导致的3D语义场噪声，提出方差感知条件MLP直接校正高斯语义，提升鲁棒性和精度。

  <details><summary>Abstract</summary>

  We propose a neural regularization method that refines the noisy 3D semantic field produced by lifting multi-view inconsistent 2D features, in order to obtain an accurate and robust 3D semantic Gaussian Splatting. The 2D features extracted from vision foundation models suffer from multi-view inconsistency due to a lack of cross-view constraints. Lifting these inconsistent features directly into 3D Gaussians results in a noisy semantic field, which degrades the performance of downstream tasks. Previous methods either focus on obtaining consistent multi-view features in the preprocessing stage or aim to mitigate noise through improved optimization strategies, often at the cost of increased preprocessing time or expensive computational overhead. In contrast, we introduce a variance-aware conditional MLP that operates directly on the 3D Gaussians, leveraging their geometric and appearance attributes to correct semantic errors in 3D space. Experiments on different datasets show that our method enhances the accuracy of lifted semantics, providing an efficient and effective approach to robust 3D semantic Gaussian Splatting.

  </details>

- **[NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706)**  
  *Yi He, Tao Wang, Yi Jin, Congyan Lang, Yidong Li, Haibin Ling*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.14706) · [pdf](https://arxiv.org/pdf/2604.14706.pdf)
  > 💡 利用掩码方差识别边界模糊高斯，通过RBF插值与多分辨率哈希编码构建连续特征场并联合NeRF优化，显著提升3DGS分割边界精度。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) have enabled highly efficient and photorealistic novel view synthesis. However, segmenting objects accurately in 3DGS remains challenging due to the discrete nature of Gaussian representations, which often leads to aliasing and artifacts at object boundaries. In this paper, we introduce NG-GS, a novel framework for high-quality object segmentation in 3DGS that explicitly addresses boundary discretization. Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis. We then apply radial basis function (RBF) interpolation to construct a spatially continuous feature field, enhanced by multi-resolution hash encoding for efficient multi-scale representation. A joint optimization strategy aligns 3DGS with a lightweight NeRF module through alignment and spatial continuity losses, ensuring smooth and consistent segmentation boundaries. Extensive experiments on NVOS, LERF-OVS, and ScanNet benchmarks demonstrate that our method achieves state-of-the-art performance, with significant gains in boundary mIoU. Code is available at https://github.com/BJTU-KD3D/NG-GS.

  </details>

- **[Scene-Agnostic Object-Centric Representation Learning for 3D Gaussian Splatting](https://arxiv.org/abs/2604.09045)**  
  *Tsuheng Hsu, Guiyu Liu, Juho Kannala, Janne Heikkilä*  
  `2026-04-10` · `cs.CV` · [abs](https://arxiv.org/abs/2604.09045) · [pdf](https://arxiv.org/pdf/2604.09045.pdf)
  > 💡 提出场景无关的物体编码本，将物体中心学习引入3DGS，解决场景依赖问题并提升跨场景泛化能力。

  <details><summary>Abstract</summary>

  Recent works on 3D scene understanding leverage 2D masks from visual foundation models (VFMs) to supervise radiance fields, enabling instance-level 3D segmentation. However, the supervision signals from foundation models are not fundamentally object-centric and often require additional mask pre/post-processing or specialized training and loss design to resolve mask identity conflicts across views. The learned identity of the 3D scene is scene-dependent, limiting generalizability across scenes. Therefore, we propose a dataset-level, object-centric supervision scheme to learn object representations in 3D Gaussian Splatting (3DGS). Building on a pre-trained slot attention-based Global Object Centric Learning (GOCL) module, we learn a scene-agnostic object codebook that provides consistent, identity-anchored representations across views and scenes. By coupling the codebook with the module's unsupervised object masks, we can directly supervise the identity features of 3D Gaussians without additional mask pre-/post-processing or explicit multi-view alignment. The learned scene-agnostic codebook enables object supervision and identification without per-scene fine-tuning or retraining. Our method thus introduces unsupervised object-centric learning (OCL) into 3DGS, yielding more structured representations and better generalization for downstream tasks such as robotic interaction, scene understanding, and cross-scene generalization.

  </details>

- **[Indoor Asset Detection in Large Scale 360° Drone-Captured Imagery via 3D Gaussian Splatting](https://arxiv.org/abs/2604.05316)**  
  *Monica Tang, Avideh Zakhor*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05316) · [pdf](https://arxiv.org/pdf/2604.05316.pdf)
  > 💡 针对无人机360°图像重建的3DGS场景，提出3D物体码本结合语义与空间信息进行多视角掩码关联，检测性能提升显著。

  <details><summary>Abstract</summary>

  We present an approach for object-level detection and segmentation of target indoor assets in 3D Gaussian Splatting (3DGS) scenes, reconstructed from 360° drone-captured imagery. We introduce a 3D object codebook that jointly leverages mask semantics and spatial information of their corresponding Gaussian primitives to guide multi-view mask association and indoor asset detection. By integrating 2D object detection and segmentation models with semantically and spatially constrained merging procedures, our method aggregates masks from multiple views into coherent 3D object instances. Experiments on two large indoor scenes demonstrate reliable multi-view mask consistency, improving F1 score by 65% over state-of-the-art baselines, and accurate object-level 3D indoor asset detection, achieving an 11% mAP gain over baseline methods.

  </details>

