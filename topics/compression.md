# Compression / Compact / Efficient Storage

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---

## 2026-05-30

- **[RxGS: Receiver-Generalizable 3D Gaussian Splatting for Radio-Frequency Data Synthesis](https://arxiv.org/abs/2605.24290)**  
  *Kang Yang, Mani Srivastava*  
  `2026-05-22` · `cs.NI` · [abs](https://arxiv.org/abs/2605.24290) · [pdf](https://arxiv.org/pdf/2605.24290.pdf)
  > 💡 针对固定接收器的RF合成问题，提出两阶段3DGS框架，共享几何并条件化学习辐射，首次实现单模型泛化至任意接收器。

  <details><summary>Abstract</summary>

  Radio-frequency (RF) data synthesis predicts the received signal given transmitter and receiver positions, and is essential for wireless applications. Recent 3D Gaussian Splatting (3DGS)-based methods achieve efficient synthesis at any transmitter but only for a fixed receiver. Therefore, supporting $N$ receivers in one scene requires $N$ independent models and precludes prediction at unseen receivers. We present RxGS, which achieves receiver-generalizable synthesis within a single unified model. Our key insight is that scene geometry is receiver-independent while directional radiance is not: a first stage learns shared 3D Gaussian geometry, and a second stage freezes it and learns directional radiance conditioned on receiver position. A global conditioning branch captures shared receiver-dependent effects across the scene, while a local branch models per-scatterer variations from the receiver's geometry and occlusion. A multi-receiver CUDA rasterizer further batches rendering across all $N$ receivers. Evaluated across various RF datasets, RxGS matches or improves over per-receiver baselines with a single shared model and generalizes to receivers unseen during training within the scene, cutting training cost by up to $45\times$, inference cost by $7.6\times$, and storage by $N\times$.

  </details>

- **[AIR: Amortized Image Reconstruction Framework for Self-Supervised Feed-Forward 2D Gaussian Splatting](https://arxiv.org/abs/2605.20820)**  
  *Zhaojie Zeng, Yuesong Wang, Yawei Luo, Tao Guan*  
  `2026-05-20` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20820) · [pdf](https://arxiv.org/pdf/2605.20820.pdf)
  > 💡 提出自监督前馈AIR框架，用阶段式残差网络和预测-优化-蒸馏策略实现2D高斯泼溅，消除逐图像优化，编码仅需160-300ms。

  <details><summary>Abstract</summary>

  2D Gaussian splatting provides an efficient explicit representation for image reconstruction, but existing methods still require costly per-image iterative optimization or rely on handcrafted priors for primitive allocation. We present AIR, a self-supervised feed-forward framework that amortizes iterative Gaussian fitting into a single network pass, eliminating per-image test-time optimization. AIR adopts a stage-wise residual architecture that progressively predicts additional Gaussian primitives from reconstruction residuals, together with an explicit Stage Control mechanism that activates new primitives only in under-reconstructed regions. A Predict--Optimize--Distill training strategy stabilizes multi-stage prediction by distilling short-horizon optimized Gaussian increments back into the predictor. The stabilized predictor is then jointly finetuned across stages and equipped with an image-adaptive quantizer for compact Gaussian storage. Experiments on Kodak and DIV2K show that AIR achieves better reconstruction quality than representative Gaussian-based baselines while reducing encoding time to 160--300\,ms. Code: https://github.com/whoiszzj/AIR.git

  </details>

- **[OP2GS: Object-Aware 3D Gaussian Splatting with Dual-Opacity Primitives](https://arxiv.org/abs/2605.20044)**  
  *Guiyu Liu, Niklas Vaara, Janne Mustaniemi, Juho Kannala, Janne Heikkilä*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.20044) · [pdf](https://arxiv.org/pdf/2605.20044.pdf)
  > 💡 通过双不透明度原语分离视觉重建与实例占用，解决3DGS中标签污染问题，实现高效对象感知表示。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) provides an explicit and efficient scene representation, but its primitives lack inherent object-level identity, hindering downstream tasks such as open-vocabulary scene understanding. Existing methods typically address this by either distilling high-dimensional feature embeddings into Gaussians or by lifting 2D mask labels into 3D via heuristic refinement. However, feature-based approaches incur heavy storage and decoding overhead, while lifting-based pipelines remain vulnerable to label contamination: Gaussians necessary for appearance reconstruction often receive incorrect object labels during 2D-to-3D projection. We propose OP2GS, an object-aware Gaussian representation that augments each primitive with an explicit instance identity and a dedicated instance opacity $σ^{*}$ for object-mask rendering. The original opacity $σ$ remains responsible for visual reconstruction, while $σ^{*}$ models whether a Gaussian should contribute to a particular object mask. This dual-opacity formulation decouples visual existence from instance occupancy: mislabeled Gaussians can remain available for image rendering while becoming transparent in the object-mask branch. To learn this representation, we introduce a random object loss that optimizes the 1D instance occupancy field using the standard transmittance-based visibility of 3DGS. Semantic descriptors are then attached at the object level through multi-view aggregation, eliminating per-Gaussian feature storage. Compared with feature-training approaches, OP2GS achieves competitive open-vocabulary performance while significantly reducing computational overhead. Compared with training-free pipelines, it leverages physically consistent occupancy learning to resolve visibility ambiguities.

  </details>

- **[MMGS: 10$\times$ Compressed 3DGS through Optimal Transport Aggregation based on Multi-view Ranking](https://arxiv.org/abs/2605.19304)**  
  *Beizhen Zhao, Sicheng Yu, Ziran Yin, Dongxu Shen, Hao Wang*  
  `2026-05-19` · `cs.CV` · [abs](https://arxiv.org/abs/2605.19304) · [pdf](https://arxiv.org/pdf/2605.19304.pdf)
  > 💡 针对3DGS冗余基元问题，提出多视角排序和全局最优传输聚合，实现10倍压缩与加速，保持高保真渲染。

  <details><summary>Abstract</summary>

  While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction, it suffers from significant overhead due to massive redundant primitives. Existing compression methods typically rely on local sampling or fixed pruning thresholds, which often struggle to balance redundancy reduction with high-fidelity rendering. To address this, we propose a novel framework that formulates Gaussian optimization as a global geometric distribution matching problem. Specifically, our approach integrates three components: (1) we introduce a multi-view 3D Gaussian contribution ranking mechanism that filters primitives using geometric consistency instead of local heuristics; (2) we propose a global Optimal Transport (OT)-based aggregation algorithm that merges redundant primitives while preserving the underlying geometry; and (3) we design an OT-based densification operator that maintains the Gaussian's distributional properties for stable optimization. Our approach achieves state-of-the-art rendering quality with only \textbf{10$\%$} primitives and \textbf{10$\times$} accelerated training speeds compared to vanilla 3DGS.

  </details>

- **[Efficient Sparse-to-Dense Visual Localization via Compact Gaussian Scene Representation and Accelerated Dense Pose Estimation](https://arxiv.org/abs/2605.17777)**  
  *Zizhuo Li, Songchu Deng, Linfeng Tang, Jiayi Ma*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.17777) · [pdf](https://arxiv.org/pdf/2605.17777.pdf)
  > 💡 提出无颜色解耦特征场和密集匹配浓缩策略，消除94%冗余存储并加速19倍，实现高效内存与计算的稀疏到密集视觉定位。

  <details><summary>Abstract</summary>

  This letter presents LiteLoc, a novel and efficient localizer built on 3D Gaussian Splatting (3DGS). The previous state-of-the-art (SoTA) sparse-to-dense localizer, STDLoc, has shown remarkable localization capability but suffers from severe storage redundancy and computational latency. By revisiting its design decisions, we derive two simple yet highly effective improvements that cumulatively make LiteLoc much more efficient in both memory and computation, while also being easier to train. One key observation is that the color field, inherited directly from Feature 3DGS, is functionally useless for localization. Yet, its reconstruction of high-frequency photometric details necessitates excessive Gaussian primitives, resulting in a tightly coupled color-feature representation with significant memory overhead and sub-optimal feature field optimization. To resolve this, we propose a color-free decoupled feature field that constructs a compact Gaussian scene representation by retaining only task-essential feature attributes, thereby eliminating approximately 94% of redundant storage with no loss of localization-relevant information. We further find that the primary computational bottleneck lies in the dense Perspective-n-Point (PnP) solver, where most matches contribute saturated geometric constraints with diminishing accuracy gains. Accordingly, we propose a condensing strategy that distills dense matches into a subset of 5% representative matches, enabling a nearly 19-fold speedup in robust estimation with negligible performance drop. Extensive experiments show that LiteLoc surpasses STDLoc in multiple scenes with considerable efficiency benefits, opening up exciting prospects for latency-sensitive visual localization.

  </details>

- **[A Single Atlas is All You Need: Decoder-Side Gaussian Splatting for Immersive Video](https://arxiv.org/abs/2605.17002)**  
  *Dawid Mieloch, Stuart Perry*  
  `2026-05-16` · `cs.GR` · [abs](https://arxiv.org/abs/2605.17002) · [pdf](https://arxiv.org/pdf/2605.17002.pdf)
  > 💡 解码端3DGS替代深度估计，用压缩纹理和元数据推断场景，压缩提升质量，带宽降十倍，视图间抖动从17.2dB降至6.4dB。

  <details><summary>Abstract</summary>

  Immersive video delivery is bottlenecked by pixel-rate constraints, making the transmission of high-resolution depth maps or explicit 3D volumetric data expensive. Decoder-Side Depth Estimation (DSDE) shifts depth computation to the client, but struggles with complex geometries, inter-view flickering, and non-Lambertian reflections. Conversely, 3D Gaussian Splatting (3DGS) offers state-of-the-art view synthesis, but transmitting splats (or their projected 2D maps) incurs prohibitive bandwidth costs and is poorly aligned with standard video codecs. We propose Decoder-Side Gaussian Splatting (DSGS), a framework that natively replaces the depth-estimation stage of DSDE with feed-forward 3DGS inference, optimizing volumetric scenes entirely on the decoder side from compressed textures and metadata. A central, counterintuitive finding is that lossy compression acts as an implicit low-pass filter stabilizing feed-forward splat prediction: compressed bitstreams exceed lossless quality while shrinking tenfold. Under extreme view sparsity (one 2D atlas comprising 4 input views), DSGS achieves a +5.79 dB BD-PSNR and +0.054 BD-SSIM gain over the DSDE anchor while reducing maximum inter-view Delta IV-PSNR from 17.2 dB to 6.4 dB, minimizing the domain shift between transmitted and virtual viewports.

  </details>

- **[Smart target point control for Gaussian Splatting methods](https://arxiv.org/abs/2605.16158)**  
  *Pratik Singh Bisht, Andreas Kolb*  
  `2026-05-15` · `cs.GR` · [abs](https://arxiv.org/abs/2605.16158) · [pdf](https://arxiv.org/pdf/2605.16158.pdf)
  > 💡 针对GS方法启发式密集化导致不公平比较，提出目标点控制方案，调整超参数跟踪二次计数轨迹，实现公平评估。

  <details><summary>Abstract</summary>

  Standard Gaussian splatting methods rely on heuristic densification and pruning to adaptively allocate primitives during training, and the resulting Gaussian count strongly influences both reconstruction quality and runtime. This makes comparisons across methods fragile: improvements can stem from higher representational capacity rather than algorithmic design. A common and naive workaround for this is hard-stopping or budgeting densification/pruning once a target count is reached, which biases training because different methods hit the cap at different times, yielding non-uniform densify/prune exposure across views and uneven point distributions. We propose a target point control scheme that preserves the standard densification window and cadence, but adjusts only the existing densification and opacity-culling hyper-parameters to track a quadratic target count trajectory. This quota-governor reaches the desired count by 15k iterations without abrupt cutoffs, ensuring that all methods and views receive equal densification and pruning cycles, enabling fairer, capacity-matched evaluation.

  </details>

- **[Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors](https://arxiv.org/abs/2605.14629)**  
  *Julien Zouein, Vibhoothi Vibhoothi, François Pitié, Anil Kokaram*  
  `2026-05-14` · `eess.IV` · [abs](https://arxiv.org/abs/2605.14629) · [pdf](https://arxiv.org/pdf/2605.14629.pdf)
  > 💡 利用AV1运动向量实现高效密集匹配，生成8倍密集点云，提升3DGS重建质量和减少63%训练时间。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a prominent framework for real-time, photorealistic scene reconstruction, offering significant speed-ups over Neural Radiance Fields (NeRF). However, the fidelity of 3DGS representations remains heavily dependent on the quality of the initial point cloud. While standard Structure-from-Motion (SfM) pipelines using COLMAP provide adequate initialisation, they often suffer from high computational costs and sparsity in textureless regions, which degrades subsequent reconstruction accuracy and convergence speed. In this work, we introduce an AV1-based feature detection and matching pipeline that significantly reduces SfM processing overhead. By leveraging motion vectors inherent to the AV1 video codec, we bypass computationally expensive exhaustive matching while maintaining geometric robustness. Our pipeline produces substantially denser point clouds, with up to eight times as many points as classical SfM. We demonstrate that this enhanced initialisation directly improves 3DGS performance, yielding an 9-point increase in VMAF and a 63% average reduction in training time required to reach baseline quality. The project page: https://sigmedia.tv/AV1-3DGS.github.io/

  </details>

- **[Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600)**  
  *Lovre Antonio Budimir, Yushi Guan, Steve Ryhner, Sven Lončarić, Nandita Vijaykumar*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13600) · [pdf](https://arxiv.org/pdf/2605.13600.pdf)
  > 💡 针对3D语言高斯溅射高存储与渲染代价，提出稀疏码本提升解耦优化，实现400倍训练加速和3倍内存节省且精度持平。

  <details><summary>Abstract</summary>

  3D Language Gaussian Splatting (3DLGS) augments 3D Gaussian Splatting with language-aligned visual features for open-vocabulary 3D scene understanding. A core challenge is efficiently associating high-dimensional vision-language embeddings with millions of 3D Gaussians while preserving efficient feature rendering for text-based querying. Existing methods either store dense features directly on Gaussians, causing high storage costs and slow rendering, or learn compact representations through expensive per-scene optimization with repeated feature rasterization. No existing method simultaneously achieves fast 3D semantic reconstruction, efficient storage, and fast rendering. We propose SCOUP (Sparse COde UPlifting), which addresses all three by decoupling language representation learning from 3D Gaussian optimization. Rather than working directly in 3D, we learn sparse codebook-based representations entirely using features associated with 2D image regions, associating each region with a sparse set of codebook coefficients. We then uplift these coefficients to 3D Gaussians with our weighted sparse aggregation using Gaussian-to-pixel associations, where each Gaussian accumulates coefficients over codebook atoms across views. Top-$K$ filtering then extracts the most dominant multi-view coefficients per Gaussian, enabling efficient storage and fast rendering. Our method achieves up to $400\times$ training speedup while being $3\times$ more memory efficient during training compared to the state-of-the-art in rendering speed. Across multiple benchmarks, SCOUP matches or outperforms existing methods in open-vocabulary querying accuracy.

  </details>

- **[HarmoGS: Robust 3D Gaussian Splatting in the Wild via Conflict-Aware Gradient Harmonization](https://arxiv.org/abs/2605.13073)**  
  *Yulei Kang, Tianze Zhu, Jian-Fang Hu, Jianhuang Lai, Wei-Shi Zheng*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.13073) · [pdf](https://arxiv.org/pdf/2605.13073.pdf)
  > 💡 针对野外场景中瞬态干扰和外观不一致问题，提出语义一致性掩码与冲突感知梯度协调，实现高质量渲染。

  <details><summary>Abstract</summary>

  In-the-wild 3D Gaussian Splatting remains challenging due to transient distractors and illumination-induced cross-view appearance inconsistencies. Existing methods mainly rely on image-level masking to suppress unreliable supervision, but masking alone cannot fully eliminate residual occlusions or resolve illumination-induced inconsistencies, both of which can introduce conflicting cross-view gradients. These unresolved conflicts may destabilize Gaussian optimization and lead to visible reconstruction artifacts. We propose a conflict-aware 3DGS framework that addresses this problem from both image-space supervision and gradient-level optimization. Semantic Consistency-Guided Masking learns pixel-wise consistency scores to adaptively refine prior masks and suppress unreliable supervision before gradient formation. A dual-view Conflict-Aware Gradient Harmonization strategy further reconciles view-specific gradients by mutually rotating them into an orthogonal configuration, reducing negative directional interference across views. We also introduce conflict-aware densification and pruning to stabilize Gaussian growth and remove persistently conflicting primitives. Extensive experiments on standard in-the-wild benchmarks demonstrate that our method achieves state-of-the-art rendering quality under complex transient distractors and cross-view inconsistencies.

  </details>

- **[Disambiguating 2D-3D Correspondences in Gaussian Splatting-based Feature Fields for Visual Localization](https://arxiv.org/abs/2605.07351)**  
  *Miso Lee, Sangeek Hyun, Yerim Jeon, Jae-Pil Heo*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07351) · [pdf](https://arxiv.org/pdf/2605.07351.pdf)
  > 💡 原始GSFFs中2D-3D对应存在多对一歧义，SplitGS-Loc利用混合高斯分裂和组成权重实现精确一对一匹配，提升定位精度。

  <details><summary>Abstract</summary>

  While Gaussian Splatting-based Feature Fields (GSFFs) have shown promise for visual localization, this paper highlights that photometrically optimized GSFFs are inherently ill-suited for 2D-3D matching. The volumetric extent of each Gaussian induces many-to-one pixel-to-point mappings that destabilize PnP-based pose estimation, while photometric optimization gives rise to superfluous Gaussians devoid of multi-view consistency. To address these issues, we propose SplitGS-Loc, a localization-specialized GSFFs construction framework that disambiguates 2D-3D correspondences by exploiting Gaussian attributes. Our key design, Mixture-of-Gaussians-based splitting, decomposes each Gaussian into smaller Gaussians, replacing ambiguous many-to-one with precise one-to-one correspondences. In parallel, we exploit composition weights from GS rasterization to select Gaussians that significantly and consistently contribute across multiple views and aggregate discriminative features through strong pixel-Gaussian associations, enforcing multi-view consistency. The resulting compact yet discriminative feature fields enable stable PnP convergence, achieving state-of-the-art performance on localization benchmarks. Extensive experiments validate that SplitGS-Loc extends the utility of photometric GSFFs to accurate and efficient localization by exploiting Gaussian attributes, without per-scene training or iterative pose refinement.

  </details>

- **[High-Fidelity Surface Splatting-Based 3D Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.07254)**  
  *Nandhana Sunil, Abhirami R Iyer, Avirup Mandal*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07254) · [pdf](https://arxiv.org/pdf/2605.07254.pdf)
  > 💡 针对多视图重建中高频细节缺失，提出紧凑多项式核与随机拉普拉斯正则化，实现更精确几何和清晰渲染。

  <details><summary>Abstract</summary>

  Multi-view mesh reconstruction remains a core challenge in computer graphics and vision, especially for recovering high-frequency geometry from sparse observations. Recent methods such as 3D Gaussian Splatting (3DGS) and Neural Radiance Fields (NeRF) rely on post-processing for mesh extraction, thereby limiting joint optimization of geometry and appearance. Implicit Moving Least Squares (IMLS) instead enables direct conversion of point clouds into signed distance and texture fields, supporting end-to-end reconstruction and rendering. However, existing IMLS formulations use exponential kernels that struggle with high-frequency detail. We introduce a compact polynomial kernel with local support and greater flexibility, allowing better control over frequency content and improved geometric fidelity. To further enhance fine details, we incorporate stochastic regularization with Laplacian filtering. Together, these improve the preservation of high-frequency structure while maintaining stable optimization. Experiments show state-of-the-art performance in both surface reconstruction and rendering, yielding more accurate geometry and sharper visuals from multi-view data.

  </details>

- **[Multi-Scale Gaussian-Language Map for Zero-shot Embodied Navigation and Reasoning](https://arxiv.org/abs/2605.01736)**  
  *Sixian Zhang, Yiyao Wang, Xinhang Song, Keming Zhang, Zijian Xu, Shuqiang Jiang*  
  `2026-05-03` · `cs.CV` · [abs](https://arxiv.org/abs/2605.01736) · [pdf](https://arxiv.org/pdf/2605.01736.pdf)
  > 💡 提出多尺度高斯-语言地图，整合显式几何与实例/区域语义，以双模态接口支持零样本具身导航与推理。

  <details><summary>Abstract</summary>

  Understanding the geometric and semantic structure of environments is essential for embodied navigation and reasoning. Existing semantic mapping methods trade off between explicit geometry and multi-scale semantics, and lack a native interface for large models, thus requiring additional training of feature projection for semantic alignment. To this end, we propose the multi-scale Gaussian-Language Map (GLMap), which introduces three key designs: (1) explicit geometry, (2) multi-scale semantics covering both instance and region concepts, and (3) a dual-modality interface where each semantic unit jointly stores a natural language description and a 3D Gaussian representation. The 3D Gaussians enable compact storage and fast rendering of task-relevant images via Gaussian splatting. To enable efficient incremental construction, we further propose a Gaussian Estimator that analytically derives Gaussian parameters from dense point clouds without gradient-based optimization. Experiments on ObjectNav, InstNav, and SQA tasks show that GLMap effectively enhances target navigation and contextual reasoning, while remaining compatible with large-model-based methods in a zero-shot manner. The code is available at https://github.com/sx-zhang/GLMap.

  </details>

- **[2D-SuGaR: Surface-Aware Gaussian Splatting for Geometrically Accurate Mesh Reconstruction](https://arxiv.org/abs/2605.00569)**  
  *Prajwal Gupta C. R., Divyam Sheth, Jinjoo Ha, Mirela Ostrek, Justus Thies*  
  `2026-05-01` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00569) · [pdf](https://arxiv.org/pdf/2605.00569.pdf)
  > 💡 针对2DGS对初始化敏感问题，引入单目深度和法线先验，提出深度引导初始化和聚类裁剪，实现高精度网格重建和新视角合成。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a powerful technique for generating photorealistic renderings of a scene in real-time. However, the volumetric nature of 3DGS limits its ability to accurately capture surface geometry. To address this, 2D Gaussian Splatting (2DGS) was proposed to enable view-consistent and geometrically accurate surface reconstruction from multi-view images. However, 2DGS can be sensitive to the initialization of the Gaussian primitives. Reliance on Structure-from-Motion (SfM) initializations, which can produce poor estimates on challenging image sets, may lead to subpar results. In this work, we enhance 2DGS by incorporating monocular depth and normal priors to improve both geometric accuracy and robustness. We propose a depth-guided initialization strategy for Gaussians and introduce a clustering-based technique for pruning degenerate Gaussians. We evaluate our method on the DTU dataset, where it achieves state-of-the-art results in mesh reconstruction while preserving high-quality novel view synthesis.

  </details>

- **[MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching](https://arxiv.org/abs/2604.26799)**  
  *Shuzhao Xie, Junchen Ge, Weixiang Zhang, Jiahang Liu, Chen Tang, Yunpeng Bai, Shijia Ge, Jingyan Jiang, Yuzhi Huang, Fengnian Yang, Cong Zhang, Xiaoyi Fan, Zhi Wang*  
  `2026-04-29` · `cs.CV` · [abs](https://arxiv.org/abs/2604.26799) · [pdf](https://arxiv.org/pdf/2604.26799.pdf)
  > 💡 提出大小感知后训练压缩方法，联合剪枝、八叉树几何

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression methods still rely on many coupled hyperparameters across pruning, transformation, quantization, and entropy coding, making it difficult to control the final compressed size and fully exploit the rate-distortion trade-off. We propose MesonGS++, a size-aware post-training codec for 3D Gaussian compression. On the codec side, MesonGS++ combines joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization with entropy coding. On the configuration side, it treats the reserve ratio and bit-width allocation as the dominant rate-distortion knobs and jointly optimizes them under a target storage budget via discrete sampling and 0--1 integer linear programming. We further propose a linear size estimator and a CUDA parallel quantization operator to accelerate the hyperparameter searching process. Extensive experiments show that MesonGS++ achieves over 34$\times$ compression while preserving rendering fidelity, outperforming state-of-the-art post-training methods and accurately meeting target size budgets. Remarkably, without any training, MesonGS++ can even surpass the PSNR of vanilla 3DGS at a 20$\times$ compression rate on the Stump scene. Our code is available at https://github.com/mmlab-sigs/mesongs_plus

  </details>

- **[Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training](https://arxiv.org/abs/2604.20046)**  
  *Yangming Zhang, Jian Xu, Chaojian Li, Kunxiong Zhu, Wei Niu, Gagan Agrawal, Yang Katie Zhao, Jian Wang, Yingyan Celine Lin, Miao Yin*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20046) · [pdf](https://arxiv.org/pdf/2604.20046.pdf)
  > 💡 针对3DGS训练内存峰值问题，提出迭代生长与剪枝的内存受限框架，以低内存实现高质量渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized novel view synthesis with high-quality rendering through continuous aggregations of millions of 3D Gaussian primitives. However, it suffers from a substantial memory footprint, particularly during training due to uncontrolled densification, posing a critical bottleneck for deployment on memory-constrained edge devices. While existing methods prune redundant Gaussians post-training, they fail to address the peak memory spikes caused by the abrupt growth of Gaussians early in the training process. To solve the training memory consumption problem, we propose a systematic memory-bounded training framework that dynamically optimizes Gaussians through iterative growth and pruning. In other words, the proposed framework alternates between incremental pruning of low-impact Gaussians and strategic growing of new primitives with an adaptive Gaussian compensation, maintaining a near-constant low memory usage while progressively refining rendering fidelity. We comprehensively evaluate the proposed training framework on various real-world datasets under strict memory constraints, showing significant improvements over existing state-of-the-art methods. Particularly, our proposed method practically enables memory-efficient 3DGS training on NVIDIA Jetson AGX Xavier, achieving similar visual quality with up to 80% lower peak training memory consumption than the original 3DGS.

  </details>

- **[OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem](https://arxiv.org/abs/2604.19127)**  
  *Byunghyun Kim*  
  `2026-04-21` · `cs.GR` · [abs](https://arxiv.org/abs/2604.19127) · [pdf](https://arxiv.org/pdf/2604.19127.pdf)
  > 💡 将UV映射重释为容量分配问题，用一维最优传输排序全局分配高斯，提升UV利用率和渲染质量。

  <details><summary>Abstract</summary>

  UV-parameterized Gaussian Splatting (UVGS) maps an unstructured set of 3D Gaussians to a regular UV tensor, enabling compact storage and explicit control of representation capacity. Existing UVGS, however, uses a deterministic spherical pro- jection to assign Gaussians to UV locations. Because this mapping ignores the global Gaussian distribution, it often leaves many UV slots empty while causing frequent collisions in dense regions. We reinterpret UV mapping as a capacity-allocation problem under a fixed UV budget and propose OT-UVGS, a lightweight, separable one-dimensional optimal-transport-inspired mapping that globally couples assignments while preserving the original UVGS representation. The method is implemented with rank-based sorting, has O(N log N) complexity for N Gaussians, and can be used as a drop-in replacement for spherical UVGS. Across 184 object-centric scenes and the Mip-NeRF dataset, OT-UVGS consistently improves peak signal-to-noise ratio (PSNR), structural similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) under the same UV resolution and per-slot capacity (K=1). These gains are accompanied by substantially better UV utilization, including higher non-empty slot ratios, fewer collisions, and higher Gaussian retention. Our results show that revisiting the mapping alone can unlock a significant fraction of the latent capacity of UVGS.

  </details>

- **[GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow](https://arxiv.org/abs/2604.15612)**  
  *Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, Hyun Myung*  
  `2026-04-17` · `cs.RO` · [abs](https://arxiv.org/abs/2604.15612) · [pdf](https://arxiv.org/pdf/2604.15612.pdf)
  > 💡 针对单目SLAM缺乏几何线索，用光流引导高斯运动场对齐，结合归一化误差优化，提升渲染与跟踪精度。

  <details><summary>Abstract</summary>

  Gaussian splatting has recently gained traction as a compelling map representation for SLAM systems, enabling dense and photo-realistic scene modeling. However, its application to monocular SLAM remains challenging due to the lack of reliable geometric cues from monocular input. Without geometric supervision, mapping or tracking could fall in local-minima, resulting in structural degeneracies and inaccuracies. To address this challenge, we propose GaussianFlow SLAM, a monocular 3DGS-SLAM that leverages optical flow as a geometry-aware cue to guide the optimization of both the scene structure and camera poses. By encouraging the projected motion of Gaussians, termed GaussianFlow, to align with the optical flow, our method introduces consistent structural cues to regularize both map reconstruction and pose estimation. Furthermore, we introduce normalized error-based densification and pruning modules to refine inactive and unstable Gaussians, thereby contributing to improved map quality and pose accuracy. Experiments conducted on public datasets demonstrate that our method achieves superior rendering quality and tracking accuracy compared with state-of-the-art algorithms. The source code is available at: https://github.com/url-kaist/gaussianflow-slam.

  </details>

- **[GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens](https://arxiv.org/abs/2604.15284)**  
  *Roni Itkin, Noam Issachar, Yehonatan Keypur, Xingyu Chen, Anpei Chen, Sagie Benaim*  
  `2026-04-16` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15284) · [pdf](https://arxiv.org/pdf/2604.15284.pdf)
  > 💡 现有前馈3DGS局部分配冗余且缺乏全局一致性；提出GlobalSplat，先学习紧凑全局潜在场景表示再解码，实现少高斯、低内存、快速推理。

  <details><summary>Abstract</summary>

  The efficient spatial allocation of primitives serves as the foundation of 3D Gaussian Splatting, as it directly dictates the synergy between representation compactness, reconstruction speed, and rendering fidelity. Previous solutions, whether based on iterative optimization or feed-forward inference, suffer from significant trade-offs between these goals, mainly due to the reliance on local, heuristic-driven allocation strategies that lack global scene awareness. Specifically, current feed-forward methods are largely pixel-aligned or voxel-aligned. By unprojecting pixels into dense, view-aligned primitives, they bake redundancy into the 3D asset. As more input views are added, the representation size increases and global consistency becomes fragile. To this end, we introduce GlobalSplat, a framework built on the principle of align first, decode later. Our approach learns a compact, global, latent scene representation that encodes multi-view input and resolves cross-view correspondences before decoding any explicit 3D geometry. Crucially, this formulation enables compact, globally consistent reconstructions without relying on pretrained pixel-prediction backbones or reusing latent features from dense baselines. Utilizing a coarse-to-fine training curriculum that gradually increases decoded capacity, GlobalSplat natively prevents representation bloat. On RealEstate10K and ACID, our model achieves competitive novel-view synthesis performance while utilizing as few as 16K Gaussians, significantly less than required by dense pipelines, obtaining a light 4MB footprint. Further, GlobalSplat enables significantly faster inference than the baselines, operating under 78 milliseconds in a single forward pass. Project page is available at https://r-itk.github.io/globalsplat/

  </details>

- **[GS4City: Hierarchical Semantic Gaussian Splatting via City-Model Priors](https://arxiv.org/abs/2604.11401)**  
  *Qilin Zhang, Jinyu Zhu, Olaf Wysocki, Benjamin Busam, Boris Jutzi*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11401) · [pdf](https://arxiv.org/pdf/2604.11401.pdf)
  > 💡 利用CityGML先验，通过双光线投射融合掩膜与2D预测，学习紧凑身份编码，提升城市语义分割精度达15.8 IoU点。

  <details><summary>Abstract</summary>

  Recent semantic 3D Gaussian Splatting (3DGS) methods primarily rely on 2D foundation models, often yielding ambiguous boundaries and limited support for structured urban semantics. While city models such as CityGML encode hierarchically organized semantics together with building geometry, these labels cannot be directly mapped to Gaussian primitives. We present GS4City, a hierarchical semantic Gaussian Splatting method that incorporates city-model priors for urban scene understanding. GS4City derives reliable image-aligned masks from Level of Detail (LoD) 3 CityGML models via two-pass raycasting, explicitly using parent-child relations to validate and recover fine-grained facade elements. It then fuses these geometry-grounded masks with foundation-model predictions to establish scene-consistent instance correspondences, and learns a compact identity encoding for each Gaussian under joint 2D identity supervision and 3D spatial regularization. Experiments on the TUM2TWIN and Gold Coast datasets show that GS4City effectively incorporates structured building semantics into Gaussian scene representations, outperforming existing 2D-driven semantic 3DGS baselines, including LangSplat and Gaga, by up to 15.8 IoU points in coarse building segmentation and 14.2 mIoU points in fine-grained semantic segmentation. By bridging structured city models and photorealistic Gaussian scene representations, GS4City enables semantically queryable and structure-aware urban reconstruction. Code is available at https://github.com/Jinyzzz/GS4City.

  </details>

- **[Naka-GS: A Bionics-inspired Dual-Branch Naka Correction and Progressive Point Pruning for Low-Light 3DGS](https://arxiv.org/abs/2604.11142)**  
  *Runyu Zhu, SiXun Dong, Zhiqiang Zhang, Qingxia Ye, Zhihua Xu*  
  `2026-04-13` · `cs.CV` · [abs](https://arxiv.org/abs/2604.11142) · [pdf](https://arxiv.org/pdf/2604.11142.pdf)
  > 💡 针对低光3DGS，提出仿生Naka校正网络与渐进点剪枝，提升重建质量与稳定性。

  <details><summary>Abstract</summary>

  Low-light conditions severely hinder 3D restoration and reconstruction by degrading image visibility, introducing color distortions, and contaminating geometric priors for downstream optimization. We present NAKA-GS, a bionics-inspired framework for low-light 3D Gaussian Splatting that jointly improves photometric restoration and geometric initialization. Our method starts with a Naka-guided chroma-correction network, which combines physics-prior low-light enhancement, dual-branch input modeling, frequency-decoupled correction, and mask-guided optimization to suppress bright-region chromatic artifacts and edge-structure errors. The enhanced images are then fed into a feed-forward multi-view reconstruction model to produce dense scene priors. To further improve Gaussian initialization, we introduce a lightweight Point Preprocessing Module (PPM) that performs coordinate alignment, voxel pooling, and distance-adaptive progressive pruning to remove noisy and redundant points while preserving representative structures. Without introducing heavy inference overhead, NAKA-GS improves restoration quality, training stability, and optimization efficiency for low-light 3D reconstruction. The proposed method was presented in the NTIRE 3D Restoration and Reconstruction (3DRR) Challenge, and outperformed the baseline methods by a large margin. The code is available at https://github.com/RunyuZhu/Naka-GS

  </details>

- **[A 129FPS Full HD Real-Time Accelerator for 3D Gaussian Splatting](https://arxiv.org/abs/2604.10223)**  
  *Fang-Chi Chang, Tian-Sheuan Chang*  
  `2026-04-11` · `cs.AR` · [abs](https://arxiv.org/abs/2604.10223) · [pdf](https://arxiv.org/pdf/2604.10223.pdf)
  > 💡 针对3DGS在AR/VR设备上高计算与存储成本，提出低功耗硬件加速器及压缩管道，实现129F

  <details><summary>Abstract</summary>

  Rendering large-scale, unbounded scenes on AR/VR-class devices is constrained by the computation, bandwidth, and storage cost of 3D Gaussian Splatting (3DGS). We propose a low-power, low-cost 3DGS hardware accelerator that renders full-HD images in real time, together with a hardware-friendly compression pipeline that combines iterative Gaussian pruning and fine-tuning, progressive spherical harmonics (SH) degree reduction, and vector quantization of all SH coefficients and colors. The scheme achieves a $51.6\times$ model-size reduction with a 0.743 dB PSNR loss. The accelerator uses a frame-level pipeline that integrates point-based culling and projection with tile-based sorting and rasterization, skips zero-Jacobian matrix multiplications (reducing processing elements by 63\% and computation by 53\%), and adopts comparison-free tile-based sorting with deterministic latency. Implemented in a TSMC 28-nm process at 800 MHz, the design occupies $0.66~\text{mm}^2$ with 1.1438 M gates and 120 kB SRAM, consumes 0.219 W, and delivers 1219 Mpixels/J at 267.5 Mpixels/s, enabling 1080p at 129 FPS. Overall, it is $5.98\times$ smaller in area, $5.94\times$ higher throughput, and delivers $7.5\times$ higher energy efficiency than prior 3DGS accelerators.

  </details>

- **[PointSplat: Efficient Geometry-Driven Pruning and Transformer Refinement for 3D Gaussian Splatting](https://arxiv.org/abs/2604.09903)**  
  *Anh Thuan Tran, Jana Kosecka*  
  `2026-04-10` · `cs.CV` · [abs](https://arxiv.org/abs/2604.09903) · [pdf](https://arxiv.org/pdf/2604.09903.pdf)
  > 💡 提出3DGS中几何驱动剪枝与双分支Transformer精炼框架，减少内存依赖，无需逐场景优化即可保持高渲染质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has recently unlocked real-time, high-fidelity novel view synthesis by representing scenes using explicit 3D primitives. However, traditional methods often require millions of Gaussians to capture complex scenes, leading to significant memory and storage demands. Recent approaches have addressed this issue through pruning and per-scene fine-tuning of Gaussian parameters, thereby reducing the model size while maintaining visual quality. These strategies typically rely on 2D images to compute important scores followed by scene-specific optimization. In this work, we introduce PointSplat, 3D geometry-driven prune-and-refine framework that bridges previously disjoint directions of gaussian pruning and transformer refinement. Our method includes two key components: (1) an efficient geometry-driven strategy that ranks Gaussians based solely on their 3D attributes, removing reliance on 2D images during pruning stage, and (2) a dual-branch encoder that separates, re-weights geometric and appearance to avoid feature imbalance. Extensive experiments on ScanNet++ and Replica across varying sparsity levels demonstrate that PointSplat consistently achieves competitive rendering quality and superior efficiency without additional per-scene optimization.

  </details>

- **[DOC-GS: Dual-Domain Observation and Calibration for Reliable Sparse-View Gaussian Splatting](https://arxiv.org/abs/2604.06739)**  
  *Hantang Li, Qiang Zhu, Xiandong Meng, Debin Zhao, Xiaopeng Fan*  
  `2026-04-08` · `cs.CV` · [abs](https://arxiv.org/abs/2604.06739) · [pdf](https://arxiv.org/pdf/2604.06739.pdf)
  > 💡 针对稀疏视图3DGS过拟合伪影问题，提出双域观测校准框架，利用深度引导丢弃和暗通道先验提升可靠性。

  <details><summary>Abstract</summary>

  Sparse-view reconstruction with 3D Gaussian Splatting (3DGS) is fundamentally ill-posed due to insufficient geometric supervision, often leading to severe overfitting and the emergence of structural distortions and translucent haze-like artifacts. While existing approaches attempt to alleviate this issue via dropout-based regularization, they are largely heuristic and lack a unified understanding of artifact formation. In this paper, we revisit sparse-view 3DGS reconstruction from a new perspective and identify the core challenge as the unobservability of Gaussian primitive reliability. Unreliable Gaussians are insufficiently constrained during optimization and accumulate as haze-like degradations in rendered images. Motivated by this observation, we propose a unified Dual-domain Observation and Calibration (DOC-GS) framework that models and corrects Gaussian reliability through the synergy of optimization-domain inductive bias and observation-domain evidence. Specifically, in the optimization domain, we characterize Gaussian reliability by the degree to which each primitive is constrained during training, and instantiate this signal via a Continuous Depth-Guided Dropout (CDGD) strategy, where the dropout probability serves as an explicit proxy for primitive reliability. This imposes a smooth depth-aware inductive bias to suppress weakly constrained Gaussians and improve optimization stability. In the observation domain, we establish a connection between floater artifacts and atmospheric scattering, and leverage the Dark Channel Prior (DCP) as a structural consistency cue to identify and accumulate anomalous regions. Based on cross-view aggregated evidence, we further design a reliability-driven geometric pruning strategy to remove low-confidence Gaussians.

  </details>

- **[3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models](https://arxiv.org/abs/2604.05366)**  
  *Jae Joong Lee*  
  `2026-04-07` · `cs.CV` · [abs](https://arxiv.org/abs/2604.05366) · [pdf](https://arxiv.org/pdf/2604.05366.pdf)
  > 💡 针对3DGS和DUSt3R，利用随机旋转使参数服从Beta分布，实现免训练近最优Lloyd-Max量化，压缩数倍几乎无损。

  <details><summary>Abstract</summary>

  Every existing method for compressing 3D Gaussian Splatting, NeRF, or transformer-based 3D reconstructors requires learning a data-dependent codebook through per-scene fine-tuning. We show this is unnecessary. The parameter vectors that dominate storage in these models, 45-dimensional spherical harmonics in 3DGS and 1024-dimensional key-value vectors in DUSt3R, fall in a dimension range where a single random rotation transforms any input into coordinates with a known Beta distribution. This makes precomputed, data-independent Lloyd-Max quantization near-optimal, within a factor of 2.7 of the information-theoretic lower bound. We develop 3D, deriving (1) a dimension-dependent criterion that predicts which parameters can be quantized and at what bit-width before running any experiment, (2) norm-separation bounds connecting quantization MSE to rendering PSNR per scene, (3) an entry-grouping strategy extending rotation-based quantization to 2-dimensional hash grid features, and (4) a composable pruning-quantization pipeline with a closed-form compression ratio. On NeRF Synthetic, 3DTurboQuant compresses 3DGS by 3.5x with 0.02dB PSNR loss and DUSt3R KV caches by 7.9x with 39.7dB pointmap fidelity. No training, no codebook learning, no calibration data. Compression takes seconds. The code will be released (https://github.com/JaeLee18/3DTurboQuant)

  </details>

- **[GaussFly: Contrastive Reinforcement Learning for Visuomotor Policies in 3D Gaussian Fields](https://arxiv.org/abs/2604.05062)**  
  *Yuhang Zhang, Mingsheng Li, Yujing Shang, Zhuoyuan Yu, Chao Yan, Jiaping Xiao, Mir Feroskhan*  
  `2026-04-06` · `cs.RO` · [abs](https://arxiv.org/abs/2604.05062) · [pdf](https://arxiv.org/pdf/2604.05062.pdf)
  > 💡 利用3DGS重建场景和对比学习提取鲁棒特征，解决单目自主飞行策略的样本效率低与sim-to-real差距，实现零样本迁移。

  <details><summary>Abstract</summary>

  Learning visuomotor policies for Autonomous Aerial Vehicles (AAVs) relying solely on monocular vision is an attractive yet highly challenging paradigm. Existing end-to-end learning approaches directly map high-dimensional RGB observations to action commands, which frequently suffer from low sample efficiency and severe sim-to-real gaps due to the visual discrepancy between simulation and physical domains. To address these long-standing challenges, we propose GaussFly, a novel framework that explicitly decouples representation learning from policy optimization through a cohesive real-to-sim-to-real paradigm. First, to achieve a high-fidelity real-to-sim transition, we reconstruct training scenes using 3D Gaussian Splatting (3DGS) augmented with explicit geometric constraints. Second, to ensure robust sim-to-real transfer, we leverage these photorealistic simulated environments and employ contrastive representation learning to extract compact, noise-resilient latent features from the rendered RGB images. By utilizing this pre-trained encoder to provide low-dimensional feature inputs, the computational burden on the visuomotor policy is significantly reduced while its resistance against visual noise is inherently enhanced. Extensive experiments in simulated and real-world environments demonstrate that GaussFly achieves superior sample efficiency and asymptotic performance compared to baselines. Crucially, it enables robust and zero-shot policy transfer to unseen real-world environments with complex textures, effectively bridging the sim-to-real gap.

  </details>

- **[SparseSplat: Towards Applicable Feed-Forward 3D Gaussian Splatting with Pixel-Unaligned Prediction](https://arxiv.org/abs/2604.03069)**  
  *Zicheng Zhang, Xiangting Meng, Ke Wu, Wenchao Ding*  
  `2026-04-03` · `cs.CV` · [abs](https://arxiv.org/abs/2604.03069) · [pdf](https://arxiv.org/pdf/2604.03069.pdf)
  > 💡 针对前馈3DGS高斯冗余问题，提出熵采样自适应密度与高效点云网络，仅用22%高斯达到最优渲染质量。

  <details><summary>Abstract</summary>

  Recent progress in feed-forward 3D Gaussian Splatting (3DGS) has notably improved rendering quality. However, the spatially uniform and highly redundant 3DGS map generated by previous feed-forward 3DGS methods limits their integration into downstream reconstruction tasks. We propose SparseSplat, the first feed-forward 3DGS model that adaptively adjusts Gaussian density according to scene structure and information richness of local regions, yielding highly compact 3DGS maps. To achieve this, we propose entropy-based probabilistic sampling, generating large, sparse Gaussians in textureless areas and assigning small, dense Gaussians to regions with rich information. Additionally, we designed a specialized point cloud network that efficiently encodes local context and decodes it into 3DGS attributes, addressing the receptive field mismatch between the general 3DGS optimization pipeline and feed-forward models. Extensive experimental results demonstrate that SparseSplat can achieve state-of-the-art rendering quality with only 22% of the Gaussians and maintain reasonable rendering quality with only 1.5% of the Gaussians. Project page: https://victkk.github.io/SparseSplat-page/.

  </details>

- **[GS^2: Graph-based Spatial Distribution Optimization for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2604.01884)**  
  *Xianben Yang, Tao Wang, Yuxuan Li, Yi Jin, Haibin Ling*  
  `2026-04-02` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01884) · [pdf](https://arxiv.org/pdf/2604.01884.pdf)
  > 💡 针对3DGS

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has demonstrated breakthrough performance in novel view synthesis and real-time rendering. Nevertheless, its practicality is constrained by the high memory cost due to a huge number of Gaussian points. Many pruning-based 3DGS variants have been proposed for memory saving, but often compromise spatial consistency and may lead to rendering artifacts. To address this issue, we propose graph-based spatial distribution optimization for compact 3D Gaussian Splatting (GS\textasciicircum2), which enhances reconstruction quality by optimizing the spatial distribution of Gaussian points. Specifically, we introduce an evidence lower bound (ELBO)-based adaptive densification strategy that automatically controls the densification process. In addition, an opacity-aware progressive pruning strategy is proposed to further reduce memory consumption by dynamically removing low-opacity Gaussian points. Furthermore, we propose a graph-based feature encoding module to adjust the spatial distribution via feature-guided point shifting. Extensive experiments validate that GS\textasciicircum2 achieves a compact Gaussian representation while delivering superior rendering quality. Compared with 3DGS, it achieves higher PSNR with only about 12.5\% Gaussian points. Furthermore, it outperforms all compared baselines in both rendering quality and memory efficiency.

  </details>

- **[LG-HCC: Local Geometry-Aware Hierarchical Context Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2603.28431)**  
  *Xuan Deng, Xiandong Meng, Hengyu Man, Qiang Zhu, Tiange Zhang, Debin Zhao, Xiaopeng Fan*  
  `2026-03-30` · `cs.CV` · [abs](https://arxiv.org/abs/2603.28431) · [pdf](https://arxiv.org/pdf/2603.28431.pdf)
  > 💡 针对3DGS锚点剪枝与熵编码忽视几何依赖导致结构退化，提出LG-HCC利用邻域感知剪枝和几何引导卷积实现紧凑表征，存储压缩30.85倍且保持几何完整。

  <details><summary>Abstract</summary>

  Although 3D Gaussian Splatting (3DGS) enables high-fidelity real-time rendering, its prohibitive storage overhead severely hinders practical deployment. Recent anchor-based 3DGS compression schemes reduce gaussian redundancy through some advanced context models. However, they overlook explicit geometric dependencies, leading to structural degradation and suboptimal ratedistortion performance. In this paper, we propose a Local Geometry-aware Hierarchical Context Compression framework for 3DGS(LG-HCC) that incorporates inter-anchor geometric correlations into anchor pruning and entropy coding for compact representation. Specifically, we introduce an Neighborhood-Aware Anchor Pruning (NAAP) strategy, which evaluates anchor importance via weighted neighborhood feature aggregation and then merges low-contribution anchors into salient neighbors, yielding a compact yet geometry-consistent anchor set. Moreover, we further develop a hierarchical entropy coding scheme, in which coarse-to-fine priors are exploited through a lightweight Geometry-Guided Convolution(GG-Conv) operator to enable spatially adaptive context modeling and rate-distortion optimization. Extensive experiments show that LG-HCC effectively alleviates structural preservation issues,achieving superior geometric integrity and rendering fidelity while reducing storage by up to 30.85x compared to the Scaffold-GS baseline on the Mip-NeRF360 dataset

  </details>

- **[SpectralSplats: Robust Differentiable Tracking via Spectral Moment Supervision](https://arxiv.org/abs/2603.24036)**  
  *Avigail Cohen Rimon, Amir Mann, Mirela Ben Chen, Or Litany*  
  `2026-03-25` · `cs.CV` · [abs](https://arxiv.org/abs/2603.24036) · [pdf](https://arxiv.org/pdf/2603.24036.pdf)
  > 💡 用频域谱矩监督替代空间损失并引入频率退火，解决3DGS跟踪中梯度消失问题，实现鲁棒跟踪。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables real-time, photorealistic novel view synthesis, making it a highly attractive representation for model-based video tracking. However, leveraging the differentiability of the 3DGS renderer "in the wild" remains notoriously fragile. A fundamental bottleneck lies in the compact, local support of the Gaussian primitives. Standard photometric objectives implicitly rely on spatial overlap; if severe camera misalignment places the rendered object outside the target's local footprint, gradients strictly vanish, leaving the optimizer stranded. We introduce SpectralSplats, a robust tracking framework that resolves this "vanishing gradient" problem by shifting the optimization objective from the spatial to the frequency domain. By supervising the rendered image via a set of global complex sinusoidal features (Spectral Moments), we construct a global basin of attraction, ensuring that a valid, directional gradient toward the target exists across the entire image domain, even when pixel overlap is completely nonexistent. To harness this global basin without introducing periodic local minima associated with high frequencies, we derive a principled Frequency Annealing schedule from first principles, gracefully transitioning the optimizer from global convexity to precise spatial alignment. We demonstrate that SpectralSplats acts as a seamless, drop-in replacement for spatial losses across diverse deformation parameterizations (from MLPs to sparse control points), successfully recovering complex deformations even from severely misaligned initializations where standard appearance-based tracking catastrophically fails.

  </details>

