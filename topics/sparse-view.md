# Sparse-View / Few-shot / Generalizable

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---









## 2026-07-14

- **[HyperGS: Fast and Generalizable Gaussian Video Representation](https://arxiv.org/abs/2607.11500)**  
  *Fatimah Zohra, Chen Zhao, Shuming Liu, Yahya Al Malallah, Bernard Ghanem*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.11500) · [pdf](https://arxiv.org/pdf/2607.11500.pdf)
  > 💡 现有高斯视频表示依赖逐视频优化，HyperGS用分解时空Transformer和前馈预测实现零样本泛化，编码速度提升数万倍。

  <details><summary>Abstract</summary>

  Gaussian Splatting has emerged as an effective representation for video, but existing methods rely on per-video optimization. This leads to slow encoding and limits generalization across videos. To amortize this optimization, we propose HyperGS, a feedforward, optimization-free approach that directly predicts Gaussian representations from any video in a single forward pass, speeding up encoding and decoding by orders of magnitude while generalizing to out-of-distribution videos at higher resolutions. In HyperGS, we design a factorized spatiotemporal Transformer to extract tokens from video, and a learnable query-based Transformer to obtain 8-parameter Gaussian representations for each video frame. We find that naively predicting Gaussians across diverse videos induces a needle-like degeneration that collapses training, and address this with a rank-based geometric regularizer whose strength adapts dynamically to stabilize optimization. HyperGS achieves encoding at $10^4$--$10^5\times$ the speed of per-video Gaussian optimization at matched reconstruction quality while generalizing zero-shot to $720p$ video, enabling higher-resolution rendering without re-encoding. HyperGS improves PSNR by +2.9--3.1 dB over the prior video encoders on K400, SSv2, and UCF101 at a smaller video representation size. By predicting explicit 2D Gaussians in a single forward pass, HyperGS combines the fast, flexible rendering of Gaussian Splatting with the speed and generalization of feedforward prediction, advancing Gaussians as a practical direction for fast and generalizable video representation.

  </details>

- **[AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling](https://arxiv.org/abs/2607.10995)**  
  *Yingji Zhong, Dave Zhenyu Chen, Fuzhao Ou, Youyu Chen, Zhihao Li, Lanqing Hong, Dan Xu*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10995) · [pdf](https://arxiv.org/pdf/2607.10995.pdf)
  > 💡 针对长序列3DGS冗余计算，提出不对称架构解耦几何与外观，粗粒度几何与细粒度外观分支交互，大幅提升效率。

  <details><summary>Abstract</summary>

  Recent generalizable 3D Gaussian Splatting models have advanced long-sequence novel view synthesis (NVS), but at the cost of substantial redundant computation. We identify that the redundancy can be mitigated based on two observations: (i) high-precision geometry is not strictly required for high-quality NVS; (ii) appearance learning is generally easier than geometry recovery. Motivated by these insights, we propose an asymmetric architecture that decouples geometry and appearance modeling. The geometry branch processes coarse-grained tokens with most of the parameters for multi-view reconstruction, while the appearance branch operates on fine-grained tokens to capture details using significantly fewer parameters. The two branches interact through bilateral connections, enabling mutual guidance for their respective tasks. This task-aware asymmetry reduces the computational redundancy and allocates the computation more judiciously, thereby increasing parameter efficiency and enabling smaller models to achieve strong performance. On 32-view 960P inputs, our model matches optimization-based methods while delivering nearly 800x speedup, and surpasses the zero-shot performance of state-of-the-art generalizable models with markedly fewer parameters and reduced training/inference overhead, achieving an overall efficiency improvement.

  </details>

- **[MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792)**  
  *Jinqian Yang, Yichen Wu, Wanhua Li, Haokun Lin, Renzhen Wang, Xiangchu Feng, Xixi Jia*  
  `2026-07-12` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10792) · [pdf](https://arxiv.org/pdf/2607.10792.pdf)
  > 💡 针对稀疏视图几何伪影，提出基于语义对应和多属性一致性损失的MAC-Splat框架，在ScanNet++上PSNR提升超4.5dB。

  <details><summary>Abstract</summary>

  Reconstructing high-fidelity 3D scenes from sparse-views remains a central problem in generalizable neural rendering. Existing generalizable 3D Gaussian Splatting (3DGS) methods often exhibit geometric artifacts in sparse-view settings, since supervision based solely on 2D photometric losses cannot resolve depth and correspondence ambiguities. To address this issue, we propose MAC-Splat, a training framework built around direct 3D consistency supervision. MAC-Splat builds on the MASt3R geometric backbone and a frozen DINOv3 encoder to obtain semantically informed 2D correspondences, which serve as geometric anchors for 3D supervision. Using these anchors, we define the Multi-Attribute Consistency (MAC) loss. This objective jointly regularizes the 3D attributes of matched Gaussians, including their position, shape, and appearance, by enforcing agreement in a common world coordinate frame. The formulation is robust to outliers and respects the geometry of covariance matrices, which leads to stable training under sparse-view conditions. Experiments on ScanNet++ show that MAC-Splat outperforms strong baselines, with particularly large gains under different overlap regimes. In particular, it improves average PSNR over Splatt3R by more than 4.5 dB, reduces LPIPS, and maintains performance as the camera pose gap increases. These results indicate that a direct, multi-attribute 3D consistency objective, when combined with high-quality correspondences, is effective for addressing the ill-posed sparse-view reconstruction problem.

  </details>

## 2026-07-07

- **[Sparse-View Surface Reconstruction using Gaussian Splatting through High-Confidence Depth Propagation with Normal Priors](https://arxiv.org/abs/2607.03765)**  
  *Liang Han, Bangcai Wei, Junsheng Zhou, Yu-Shen Liu, Zhizhong Han*  
  `2026-07-04` · `cs.CV` · [abs](https://arxiv.org/abs/2607.03765) · [pdf](https://arxiv.org/pdf/2607.03765.pdf)
  > 💡 针对稀疏视图表面重建，提出法线引导的高置信深度传播与异常深度边缘感知正则化，显著提升几何质量。

  <details><summary>Abstract</summary>

  3D reconstruction from sparse views is a challenging task in 3D computer vision. Recent studies on 3D Gaussian Splatting (3DGS) have achieved remarkable results with sparse views in novel view synthesis, yet reconstructing high-quality geometric surfaces from sparse views remains a challenge, due to the limited geometry clues and the discreteness of Gaussians. In this paper, we propose a novel 3DGS-based method for high-fidelity surface reconstruction from sparse views. Our key insight is to introduce a normal-guided depth propagation approach, which can extend depth information from high-confidence regions to constrain the depth in low-confidence areas. Additionally, we propose an abnormal depth edge-aware regularization to address depth discontinuities caused by the discreteness of Gaussians. Extensive experiments on DTU and Tanks-and-Temples datasets demonstrate that our method outperforms the state-of-the-art methods in sparse view surface reconstruction. Project page: https://hanl2010.github.io/DP-GS.

  </details>

## 2026-07-04

- **[The Turning Point of 3D Plant Phenotyping: 3D Foundation Models Enable Minute-to-Second Cross-Crop Reconstruction and Beyond](https://arxiv.org/abs/2607.01753)**  
  *Hanyue Jia, Wei Zhou, Wenbo Zhou, Yanan Li, Hao Lu, Tingting Wu*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.01753) · [pdf](https://arxiv.org/pdf/2607.01753.pdf)
  > 💡 用3D基础模型和3D高斯泼溅将植物表型重建从分钟级加速到秒级，保持高精度。

  <details><summary>Abstract</summary>

  3D plant phenotyping is notoriously known to be procedure-complicated and of low throughput due to the extensive multi-view imaging, the fragile 3D reconstruction pipeline, and the additional cost from reconstructed geometry to phenotypic extraction. These limitations are further amplified in low-cost data acquisition, where smartphone videos or sparsely sampled multi-view images provide limited view overlap and self-occlusion. In this work, we show that the conventional 3D plant phenotyping pipeline could be streamlined and significantly accelerated with 3D Foundation Models (3DFMs), and particularly, present one of the first cross-crop 3D phenotyping frameworks powered by 3DFMs. The framework replaces COLMAP-style sparse initialization with 3DFM-based feed-forward geometric recovery, combines geometry-constrained 3D Gaussian Splatting for dense reconstruction, enables few-view reconstruction through iterative view synthesis and refinement, and converts reconstructed geometry into measurable organs through 2D-to-3D semantic transfer, metric scale recovery, and organ instance separation. We further construct a cross-crop dataset with smartphone-based image acquisition, diverse plant morphologies, and manual annotations for segmentation and phenotypic evaluation. Experiments across 26 plant sequences show that 3D Foundation Models reduce the average reconstruction time from 6.52 minutes to 1.58 seconds while maintaining high reconstruction quality and phenotyping accuracy. These results suggest a fresh technical route for high-throughput 3D plant phenotyping, from low-cost image acquisition to fast reconstruction, perception, scale recovery, and phenotypic measurement.

  </details>

- **[Bridging 3D Gaussians and Semantic Occupancy for Comprehensive Open-Vocabulary Scene Understanding from Unposed Images](https://arxiv.org/abs/2607.01633)**  
  *Hu Zhu, Bohan Li, Xianda Guo, Yanlun Peng, Zheng Zhu, Xin Jin, Wenjun Zeng, Chang Wen Chen*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.01633) · [pdf](https://arxiv.org/pdf/2607.01633.pdf)
  > 💡 针对无位姿图像，提出COVScene，将可渲染3D高斯与语义占据场可微耦合，统一实现开放词汇语义分割与占据预测。

  <details><summary>Abstract</summary>

  Comprehensive 3D scene understanding from sparse, unposed images requires a model to recover renderable geometry, open-vocabulary semantics, and free/occupied 3D space without relying on external camera calibration. Recent feed-forward Gaussian methods improve pose-free reconstruction and semantic rendering, but their Gaussian primitives are mainly optimized through image-space objectives and remain weakly constrained in unobserved regions. We propose \textit{COVScene}, a pose-free semantic Gaussian framework that couples renderable Gaussian primitives with a dense semantic occupancy field through differentiable volumetric lifting. Instead of converting Gaussians to voxels only at evaluation time, COVScene lifts the predicted semantic Gaussians inside the training computation graph, so volumetric regularization provides gradients to Gaussian opacity, geometry, and semantic features. The framework combines a semantic-aware Geometry Transformer, multi-task Gaussian decoding, geometric foundation distillation, and occupancy entropy regularization to support novel view synthesis, open-vocabulary semantic querying, and semantic occupancy prediction within a single representation. Experiments on ScanNet and ScanNet++ show that COVScene maintains competitive rendering quality, improves open-vocabulary segmentation, and achieves stronger semantic occupancy prediction than the self-supervised baseline without direct voxel-level supervision.

  </details>

## 2026-06-30

- **[Learning to Adaptively Allocate Gaussians for Arbitrary-Scale Image Super-Resolution](https://arxiv.org/abs/2606.29400)**  
  *Giulio Federico, Giuseppe Amato, Claudio Gennaro, Fabio Carrara, Marco Di Benedetto*  
  `2026-06-28` · `cs.CV` · [abs](https://arxiv.org/abs/2606.29400) · [pdf](https://arxiv.org/pdf/2606.29400.pdf)
  > 💡 通过神经路由动态分配高斯密度和层次指针卷积，实现高效任意尺度图像超分辨率，克服均匀处理冗余并达到SOTA。

  <details><summary>Abstract</summary>

  In computer graphics, visual content is continuously warped, zoomed and resampled. This occurs when engines upscale frames, users zoom into 3D scenes, or foveated VR applies varying scaling. Handling these transformations requires Arbitrary-Scale Super-Resolution (ASR). Traditional models, designed for fixed scales, typically predict at a lower integer scale (e.g., x4) and rely on sub-optimal interpolation for continuous resolutions, compromising quality. Furthermore, most methods process pixels uniformly. Since fine details are sparse, this creates overhead; efficiency dictates concentrating resources only where structural complexity demands it. While implicit models and Gaussian Splatting (GS) enable continuous representation, GS is advantageous due to adaptive densification. However, transitioning GS into a feed-forward model for ASR is non-trivial. Standard GS optimization needs high-resolution gradients to drive primitive growth, which are unavailable during inference. Thus, the network must autonomously predict GS densification from low-resolution inputs. To solve this, we propose QuADA-GS. After encoding inputs into a latent space, a Neural Routing Architecture evaluates local complexity to distribute a global budget, assigning specific upsampling factors to features to avoid redundant processing. Features are dynamically densified based on these factors, forming an irregular topology decoded into 2D Gaussian primitives. To coordinate features before decoding, we introduce Hierarchical Pointer Convolution. This non-grid operator achieves O(1) neighbor lookup complexity, facilitating efficient spatial communication and bypassing dense bottlenecks. Experiments show QuADA-GS achieves state-of-the-art ASR performance, maintaining low latency and a lean memory footprint.

  </details>

## 2026-06-29

- **[StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321)**  
  *Jia-Chen Zhao, Beiqi Chen, Xinyang Chen, Guangcong Wang, Liqiang Nie*  
  `2026-06-26` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28321) · [pdf](https://arxiv.org/pdf/2606.28321.pdf)
  > 💡 针对未标定稀疏视图，提出结构化表示解耦几何、语义和纹理，实现通用3D高斯重建，显著提升跨数据集性能。

  <details><summary>Abstract</summary>

  We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction framework that operates directly on uncalibrated images without requiring camera parameters. Existing methods either rely on per-scene optimization or assume known camera poses, and often entangle geometry and appearance within a unified backbone, limiting reconstruction fidelity and generalization. Our key idea is to adopt a structured representation that organizes geometry, semantic, and texture cues with explicit roles in the reconstruction process. Specifically, we introduce a pixel-aligned feature injection mechanism to enable accurate texture modeling from 2D observations, incorporate semantic-aware priors to improve global consistency, and design a camera alignment strategy to prevent information leakage and improve generalization. Experiments show that our method significantly outperforms prior approaches on challenging benchmarks. On DL3DV, our method achieves 28.045 PSNR, surpassing AnySplat (22.377) by +5.67 dB. In cross-dataset evaluation, our method achieves +1.94 dB over AnySplat on ACID and +1.72 dB on RealEstate10K. Project page: https://structsplat.github.io Code: https://github.com/J-C-Zhao/StructSplat

  </details>

## 2026-06-19

- **[VisDom: Sparse Novel View Synthesis with Visible Domain Constraint](https://arxiv.org/abs/2606.20531)**  
  *Mariia Gladkova*, Tarun Yenamandra*, Edmond Boyer, Robert Maier, Tony Tung, Daniel Cremers*  
  `2026-06-18` · `cs.CV` · [abs](https://arxiv.org/abs/2606.20531) · [pdf](https://arxiv.org/pdf/2606.20531.pdf)
  > 💡 针对稀疏视图新视图合成中过拟合与几何模糊，提出可见域约束，基于多视图可见性过滤，提升NeRF/GS重建质量。

  <details><summary>Abstract</summary>

  Sparse novel view synthesis (NVS) remains challenging due to the ambiguity of recovering 3D geometry from few input views. While NeRF- and Gaussian Splatting (GS)-based methods perform well with dense supervision, they often overfit in sparse settings, producing floating artifacts and inconsistent geometry. Silhouette consistency is commonly used as a regularizer, but it remains insufficient, as silhouette-consistent regions can extend beyond the true object geometry. We introduce VisDom, a learning-free geometric constraint that augments classical carving-based visual hull reconstruction by enforcing a minimum multi-view visibility requirement. Specifically, we define a visible domain as the subset of 3D space observed by at least $K$ views and use it as an additional filtering criterion on top of standard silhouette-based reconstruction. This provides a stronger spatial prior in sparse-view settings. We integrate VisDom into both implicit (NeRF) and explicit (GS) pipelines by restricting volumetric sampling and guiding Gaussian placement during optimization. Experiments on three challenging datasets show consistent improvements in sparse-view NVS, enabling high-quality object-centric reconstruction from as few as four input images. Our method is domain-agnostic, requires only silhouettes, and introduces no learned parameters, making it a simple complement to existing approaches. Applying VisDom on top of GaussianObject further improves performance on Omni3D and MipNeRF360, while matching or surpassing it at 22 $\times$ lower training cost.

  </details>

## 2026-06-16

- **[Dehaze-GaussianImage: Zero-Shot Dehazing via Efficient 2D Gaussian Splatting Representation](https://arxiv.org/abs/2606.16163)**  
  *Yuhan Chen, Wenxuan Yu, Guofa Li, Kunyang Huang, Ying Fang, Yicui Shi, Wenbo Chu, Keqiang Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16163) · [pdf](https://arxiv.org/pdf/2606.16163.pdf)
  > 💡 用2D高斯泼溅零样本去雾，嵌入大气散射模型实现几何解耦，以最少参数达到SOTA。

  <details><summary>Abstract</summary>

  Existing single image dehazing methods are often constrained by computational redundancy in pixel-level optimization and the lack of physical interpretability in implicit neural networks. These limitations hinder the balance between representation efficiency and reconstruction fidelity. To address these issues, we propose Dehaze-GaussianImage, the first zero-shot framework that introduces 2D Gaussian Splatting (2DGS) into the image dehazing domain to break the traditional pixel-grid processing paradigm. Distinct from static convolutional neural networks (CNNs) or Transformers, our approach models hazy images as continuous and dynamically evolvable anisotropic Gaussian fields. Specifically, we propose a novel reconstruction-decoupling zero-shot learning strategy that embeds the atmospheric scattering model into the Gaussian parameter space. This strategy drives Gaussian primitives to adaptively split, clone, and prune during optimization, achieving geometric-level decoupling of the transmission medium and clear textures. Furthermore, explicit structure-preserving constraints are introduced to suppress artifacts commonly caused by traditional physical priors. Experimental results demonstrate that the proposed method achieves state-of-the-art (SOTA) performance in a fully unsupervised manner with minimal parameters, highlighting the potential of explicit Gaussian representation for low-level vision tasks.

  </details>

## 2026-06-06

- **[Unpaired RGB-Thermal Gaussian-Splatting Using Visual Geometric Transformers](https://arxiv.org/abs/2606.05491)**  
  *Jean Cordonnier, Chenghao Xu, Olga Fink, Malcolm Mielle*  
  `2026-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2606.05491) · [pdf](https://arxiv.org/pdf/2606.05491.pdf)
  > 💡 用VGGT独立估计位姿后Procrustes对齐，实现未配对RGB-热成像的多模态3DGS渲染，兼顾热像合成与RGB保真。

  <details><summary>Abstract</summary>

  Multi-modal novel view synthesis (NVS) combining RGB and thermal imagery enables precise 3D scene reconstruction with visual and thermal information. However, existing methods typically rely on precisely calibrated RGB-thermal image pairs or stereo setups, limiting scalability and practical deployment. To address this, we introduce a framework for unpaired RGB-thermal NVS that leverages VGGT, a 3D feed-forward transformer architecture, to independently estimate camera poses for each modality. The pose sets are then aligned using the Procrustes algorithm with a cross-modal feature matcher, enabling joint registration without paired calibration. Building on this alignment, we further propose a multi-modal 3D Gaussian Splatting approach that learns directly from unpaired RGB and thermal images. Experiments on diverse scenes demonstrate that our method achieves competitive performance in thermal view synthesis while maintaining RGB fidelity. Moreover, we show that existing reconstruction approaches can produce modality-specific reconstructions that lack cross-modal consistency. We thus introduce a benchmarking framework to rigorously evaluate both per-modality image synthesis and the multi-modal coherence of reconstructed scenes.

  </details>

- **[$\text{VG}^2$GT: Voxel-Gaussian Splatting Visual Geometry Grounded Transformer](https://arxiv.org/abs/2606.01573)**  
  *Yibin Zhao, Yihan Pan, Jun Nan, Wenli Yang, Liwei Chen, Jianjun Yi*  
  `2026-06-01` · `cs.CV` · [abs](https://arxiv.org/abs/2606.01573) · [pdf](https://arxiv.org/pdf/2606.01573.pdf)
  > 💡 利用冻结视觉基础模型与多尺度可微分体素模块，从体素特征回归高斯原语，实现几何准确

  <details><summary>Abstract</summary>

  Gaussian splatting has shown strong potential for 3D reconstruction and novel view synthesis. However, most existing methods require accurate camera parameters and per-scene optimization, while feed-forward methods with pixel-aligned Gaussian primitives often suffer from artifacts and non-uniform primitives. In this paper, we propose $\text{VG}^2$GT, a Voxel-Gaussian Splatting Visual Geometry-Grounded Transformer. $\text{VG}^2$GT leverages a frozen pretrained visual foundation model (VFM), incorporates a multi-scale differentiable voxel module to enhance geometric understanding, and directly splits and regresses Gaussian primitive parameters from voxel features. During training, depth maps are supervised through stochastic solid volume rendering, enabling geometrically accurate Gaussian scene reconstruction while keeping the visual foundation model fully frozen. This design enables $\text{VG}^2$GT to be seamlessly plugged into any patch-feature-based VFM, while substantially reducing the required training cost. $\text{VG}^2$GT outperforms current state-of-the-art methods on widely used DTU, Replica, TAT, and ScanNet datasets.

  </details>

## 2026-05-30

- **[ArtSplat: Feed-Forward Articulated 3D Gaussian Splatting from Sparse Multi-State Uncalibrated Views](https://arxiv.org/abs/2605.24304)**  
  *Inseo Lee, Yoonji Kim, Eugene Sohn, Jiwoong Lee, Jungmin You, Joonseok Lee, Jin-Hwa Kim*  
  `2026-05-23` · `cs.CV` · [abs](https://arxiv.org/abs/2605.24304) · [pdf](https://arxiv.org/pdf/2605.24304.pdf)
  > 💡 针对稀疏多状态未标定视图关节物体重建，提出ArtSplat前馈框架，利用每像素关节图和跨状态注意力，实现快速几何与关节参数联合估计。

  <details><summary>Abstract</summary>

  Articulated object reconstruction from sparse-view images is an ill-posed problem that requires simultaneous inference of geometry and underlying articulation structure. Existing methods for articulated object reconstruction based on NeRF and 3D Gaussian Splatting (3DGS) typically rely on dense views or strong priors (e.g., depth maps, joint types, predefined number of joints) and require costly per-object optimization. In this paper, we propose ArtSplat, the first feed-forward framework for articulated 3D Gaussian Splatting. It reconstructs both geometry and joint parameters from sparse multi-view images across multiple articulation states in a single forward pass. To address the challenges of single-pass articulated reconstruction, we introduce a per-pixel joint map representation that enables the integration of joint parameter estimation into the feed-forward pipeline. We further propose a Cross-State Attention (CSA) mechanism with state tokens, which effectively captures discrete motion across input states. Experiments on 68 articulated objects from PartNet-Mobility, including both single- and multi-joint configurations, demonstrate that ArtSplat achieves competitive performance in both geometry and joint estimation, while being over 400 times faster than baselines.

  </details>

- **[LangFlash: Feed-forward 3D Language Gaussian Splatting from Sparse Unposed Images](https://arxiv.org/abs/2605.23287)**  
  *Yilong Liu, Wanhua Li, Chen Zhu-Tian, Hanspeter Pfister*  
  `2026-05-22` · `cs.CV` · [abs](https://arxiv.org/abs/2605.23287) · [pdf](https://arxiv.org/pdf/2605.23287.pdf)
  > 💡 提出前馈框架LangFlash，从稀疏无位姿图像直接预测三维高斯语义场，实现低延迟重建和一致语义理解。

  <details><summary>Abstract</summary>

  We present LangFlash, a feed-forward framework for 3D Language Gaussian Splatting that reconstructs 3D scenes parameterized by Gaussian primitives enriched with language-aligned semantic features from sparse unposed multi-view images. Unlike optimization-based 3D methods, LangFlash directly predicts the geometry and semantics in a single forward pass, enabling low-latency 3D reconstruction and language-consistent scene understanding. To support large-scale training, we enriched the RealEstate10k dataset with coherent and dense semantic information for 3D semantic supervision. Furthermore, we propose a sparse semantic encoding scheme that combines a global semantic dictionary with locally varying per-primitive weights, preserving high-level linguistic information, while reducing representation complexity. Experimental results show that LangFlash achieves superior novel view synthesis and semantic consistency compared with previous methods. This study establishes a new paradigm for pose-free, language-grounded 3D scene reconstruction, advancing generalizable 3D vision and multimodal scene understanding. Demo is available at https://liylo.github.io/langflash.github.io/.

  </details>

- **[PairDropGS: Paired Dropout-Induced Consistency Regularization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.12072)**  
  *Hantang Li, Qiang Zhu, Xiandong Meng, Xingtao Wang, Debin Zhao, Xiaopeng Fan*  
  `2026-05-12` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12072) · [pdf](https://arxiv.org/pdf/2605.12072.pdf)
  > 💡 现有dropout方法忽略不一致性导致不稳定；提出成对dropout一致性正则化，约束低频结构，提升稀疏视图3DGS重建质量与训练稳定性。

  <details><summary>Abstract</summary>

  Dropout-based sparse-view 3D Gaussian Splatting (3DGS) methods alleviate overfitting by randomly suppressing Gaussian primitives during training. Existing methods mainly focus on designing increasingly sophisticated dropout strategies, while they overlook the resulting inconsistencies among different dropped Gaussian subsets. This oversight often leads to unstable reconstruction and suboptimal Gaussian representation learning.In this paper, we revisit dropout-based sparse-view 3DGS from a consistency regularization perspective and propose PairDropGS, a Paired Dropout-induced Consistency Regularization framework for sparse-view Gaussian splatting. Specifically, PairDropGS first constructs a pair of the dropped Gaussian subsets from a shared Gaussian field and designs a low-frequency consistency regularization to constrain their low-frequency rendered structures. This design encourages the shared Gaussian field to preserve stable scene layout and coarse geometry under different random dropouts, while avoiding excessive constraints on ambiguous high-frequency details. Moreover, we introduce a progressive consistency scheduling strategy to gradually strengthen the consistency regularization during training for stability and robustness of reconstruction. Extensive experiments on widely-used sparse-view benchmarks demonstrate that PairDropGS achieves superior training stability, significantly outperforms existing dropout-based 3DGS methods in reconstruction quality, while exhibiting the simplicity and plug-and-play nature for improving dropout-based optimization.

  </details>

- **[AdaptSplat: Adapting Vision Foundation Models for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2605.10239)**  
  *Mingwei Xing, Xinliang Wang, Yifeng Shi*  
  `2026-05-11` · `cs.CV` · [abs](https://arxiv.org/abs/2605.10239) · [pdf](https://arxiv.org/pdf/2605.10239.pdf)
  > 💡 针对前馈3DGS跨域泛化差和高频保真不足，提出仅1.5M参数的频率保持适配器FPA，利用浅层高频先验提升性能。

  <details><summary>Abstract</summary>

  This work explores a simple yet powerful lightweight adapter design for feed-forward 3D Gaussian Splatting (3DGS). Existing methods typically apply complex, architecture-specific designs on top of the generic pipeline of image feature extraction $\rightarrow$ multi-view interaction $\rightarrow$ feature decoding. However, constrained by the scale bottleneck of 3D training data and the low-pass filtering effect of deep networks, these methods still fall short in cross-domain generalization and high-frequency geometric fidelity. To address these problems, we propose AdaptSplat, which demonstrates that without complex component engineering, introducing a single adapter of only 1.5M parameters into the generic architecture is sufficient to achieve superior performance. Specifically, we design a lightweight Frequency-Preserving Adapter (FPA) that extracts direction-aware high-frequency structural priors from the shallow features of a powerful vision foundation model backbone, and seamlessly integrates them into the generic pipeline via high-frequency positional encodings and adaptive residual modulation. This effectively compensates for the high-frequency attenuation caused by over-smoothing in deep features, improving the fitting accuracy of Gaussian primitives on complex surfaces and sharp boundaries. Extensive experiments demonstrate that AdaptSplat achieves state-of-the-art feed-forward reconstruction performance on multiple standard benchmarks, with stable generalization across domains. Code available at: https://github.com/xmw666/AdaptSplat.

  </details>

- **[SplatWeaver: Learning to Allocate Gaussian Primitives for Generalizable Novel View Synthesis](https://arxiv.org/abs/2605.07287)**  
  *Yecong Wan, Fan Li, Mingwen Shao, Wangmeng Zuo*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07287) · [pdf](https://arxiv.org/pdf/2605.07287.pdf)
  > 💡 针对固定高斯原语分配忽略空间复杂度问题，提出动态分配的SplatWeaver，通过专家与路由实现区域自适应，

  <details><summary>Abstract</summary>

  Generalizable novel view synthesis aims to render unseen views from uncalibrated input images without requiring per-scene optimization. Recent feed-forward approaches based on 3D Gaussian Splatting have achieved promising efficiency and rendering quality. However, most of them assign a fixed number of Gaussians to each pixel or voxel, ignoring the spatially varying complexity of real-world scenes. Such uniform allocation often wastes Gaussian primitives in smooth regions while providing insufficient capacity for fine structures, complex geometry, and high-frequency details. This motivates us to predict region-dependent primitive cardinalities rather than impose a fixed primitive budget everywhere, enabling a more expressive 3D scene representation. Therefore, we propose SplatWeaver, a generalizable novel view synthesis framework that is able to dynamically allocate Gaussian primitives over different regions in a feed-forward manner. Specifically, SplatWeaver introduces cardinality Gaussian experts and a pixel-level routing scheme, wherein each expert specializes in producing a specific number of primitives from 0 to M, and the routing scheme coordinates these experts to adaptively determine how many Gaussian primitives should be allocated to each spatial location. Moreover, SplatWeaver incorporates a high-frequency prior with attendant guidance module and routing regularization to stabilize expert selection and promote complexity-aware allocation. By leveraging high-frequency cues, the routing process is encouraged to assign more Gaussian primitives to fine structures and textured regions, while suppressing redundancy in smooth areas. Extensive experiments across diverse scenarios show that SplatWeaver consistently outperforms state-of-the-art methods, delivering more faithful novel-view renderings with fewer Gaussian primitives. Project Page: https://yecongwan.github.io/SplatWeaver/

  </details>

- **[SatSurfGS: Generalizable 2D Gaussian Splatting for Sparse-View Satellite Surface Reconstruction](https://arxiv.org/abs/2605.07181)**  
  *Min Chen, Wei Guo, Bin Wang, Wen Li, Tong Fang, Jinbo Zhang, Junqi Zhao, Hong Kuang, Han Hu, Xuming Ge, Qing Zhu, Bo Xu*  
  `2026-05-08` · `cs.CV` · [abs](https://arxiv.org/abs/2605.07181) · [pdf](https://arxiv.org/pdf/2605.07181.pdf)
  > 💡 针对稀疏视图卫星表面重建中多视角匹配空间异质问题，提出基于2DGS的可泛化方法，通过粗到细属性预测和三级局部几何可靠性建模提升重建精度与效率。

  <details><summary>Abstract</summary>

  Sparse-view satellite image surface reconstruction remains highly challenging, fundamentally because the reliability of multi-view matching under satellite imaging conditions is strongly spatially heterogeneous. Affected by large photometric differences, weak textures, and repetitive textures, multi-view geometric constraints are often sparse, unevenly distributed, and locally unreliable. Although 2D Gaussian Splatting (2DGS) is more suitable than 3D Gaussian Splatting (3DGS) for the explicit representation of continuous surfaces, research on generalizable feed-forward 2DGS frameworks for sparse-view satellite surface reconstruction is still lacking. To address this issue, we propose SatSurfGS, a generalizable sparse-view surface reconstruction method for satellite imagery based on 2DGS. The proposed method builds a coarse-to-fine Gaussian attribute prediction framework and explicitly models local geometric reliability at three levels: feature learning, Gaussian parameter estimation, and training optimization. Specifically, we propose a confidence-aware monocular multi-view feature fusion module to adaptively integrate monocular priors and multi-view matching features according to local confidence; a cross-stage self-consistency residual guidance module to stabilize stage-wise Gaussian parameter refinement using the residual between the rendered height map from the previous stage and the current-stage MVS height map, together with confidence information; and a confidence bidirectional routing loss to achieve differentiated allocation of geometric and appearance supervision. Experiments on satellite datasets show that the proposed method achieves improved rendering quality, surface reconstruction accuracy, cross-dataset generalization, and inference efficiency compared with representative generalizable baselines and competitive per-scene optimization methods.

  </details>

- **[VVGT: Visual Volume-Grounded Transformer](https://arxiv.org/abs/2604.12217)**  
  *Yuxuan Wang, Qibiao Li, Youcheng Cai*  
  `2026-04-14` · `cs.GR` · [abs](https://arxiv.org/abs/2604.12217) · [pdf](https://arxiv.org/pdf/2604.12217.pdf)
  > 💡 现有体可视化可扩展性差，提出前馈双Transformer网络VVGT，用体几何强制机制将体数据映射为3DGS，实现快速高质量免逐场景优化。

  <details><summary>Abstract</summary>

  Volumetric visualization has long been dominated by Direct Volume Rendering (DVR), which operates on dense voxel grids and suffers from limited scalability as resolution and interactivity demands increase. Recent advances in 3D Gaussian Splatting (3DGS) offer a representation-centric alternative; however, existing volumetric extensions still depend on costly per-scene optimization, limiting scalability and interactivity. We present VVGT (Visual Volume-Grounded Transformer), a feed-forward, representation-first framework that directly maps volumetric data to a 3D Gaussian Splatting representation, advancing a new paradigm for volumetric visualization beyond DVR. Unlike prior feed-forward 3DGS methods designed for surface-centric reconstruction, VVGT explicitly accounts for volumetric rendering, where each pixel aggregates contributions along a ray. VVGT employs a dual-transformer network and introduces Volume Geometry Forcing, an epipolar cross-attention mechanism that integrates multi-view observations into distributed 3D Gaussian primitives without surface assumptions. This design eliminates per-scene optimization while enabling accurate volumetric representations. Extensive experiments show that VVGT achieves high-quality visualization with orders-of-magnitude faster conversion, improved geometric consistency, and strong zero-shot generalization across diverse datasets, enabling truly interactive and scalable volumetric visualization. The code will be publicly released upon acceptance.

  </details>

- **[SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction](https://arxiv.org/abs/2604.08370)**  
  *Chensheng Dai, Shengjun Zhang, Min Chen, Yueqi Duan*  
  `2026-04-09` · `cs.CV` · [abs](https://arxiv.org/abs/2604.08370) · [pdf](https://arxiv.org/pdf/2604.08370.pdf)
  > 💡 针对稀疏视图表面重建，提出基于奈奎斯特采样定理的前馈框架，高效生成可泛化高斯surfel表示，实现快速精确重建。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has demonstrated impressive performance in 3D scene reconstruction. Beyond novel view synthesis, it shows great potential for multi-view surface reconstruction. Existing methods employ optimization-based reconstruction pipelines that achieve precise and complete surface extractions. However, these approaches typically require dense input views and high time consumption for per-scene optimization. To address these limitations, we propose SurfelSplat, a feed-forward framework that generates efficient and generalizable pixel-aligned Gaussian surfel representations from sparse-view images. We observe that conventional feed-forward structures struggle to recover accurate geometric attributes of Gaussian surfels because the spatial frequency of pixel-aligned primitives exceeds Nyquist sampling rates. Therefore, we propose a cross-view feature aggregation module based on the Nyquist sampling theorem. Specifically, we first adapt the geometric forms of Gaussian surfels with spatial sampling rate-guided low-pass filters. We then project the filtered surfels across all input views to obtain cross-view feature correlations. By processing these correlations through a specially designed feature fusion network, we can finally regress Gaussian surfels with precise geometry. Extensive experiments on DTU reconstruction benchmarks demonstrate that our model achieves comparable results with state-of-the-art methods, and predict Gaussian surfels within 1 second, offering a 100x speedup without costly per-scene training.

  </details>

- **[3D Gaussian Splatting for Annular Dark Field Scanning Transmission Electron Microscopy Tomography Reconstruction](https://arxiv.org/abs/2604.04693)**  
  *Beiyuan Zhang, Hesong Li, Ruiwen Shao, Ying Fu*  
  `2026-04-06` · `cs.CV` · [abs](https://arxiv.org/abs/2604.04693) · [pdf](https://arxiv.org/pdf/2604.04693.pdf)
  > 💡 针对ADF-STEM稀疏视角重建伪影问题，提出DenZa-Gaussian，用标量场denza建模散射，引入γ和傅里叶损失实现高保真重建。

  <details><summary>Abstract</summary>

  Analytical Dark Field Scanning Transmission Electron Microscopy (ADF-STEM) tomography reconstructs nanoscale materials in 3D by integrating multi-view tilt-series images, enabling precise analysis of their structural and compositional features. Although integrating more tilt views improves 3D reconstruction, it requires extended electron exposure that risks damaging dose-sensitive materials and introduces drift and misalignment, making it difficult to balance reconstruction fidelity with sample preservation. In practice, sparse-view acquisition is frequently required, yet conventional ADF-STEM methods degrade under limited views, exhibiting artifacts and reduced structural fidelity. To resolve these issues, in this paper, we adapt 3D GS to this domain with three key components. We first model the local scattering strength as a learnable scalar field, denza, to address the mismatch between 3DGS and ADF-STEM imaging physics. Then we introduce a coefficient $γ$ to stabilize scattering across tilt angles, ensuring consistent denza via scattering view normalization. Finally, We incorporate a loss function that includes a 2D Fourier amplitude term to suppress missing wedge artifacts in sparse-view reconstruction. Experiments on 45-view and 15-view tilt series show that DenZa-Gaussian produces high-fidelity reconstructions and 2D projections that align more closely with original tilts, demonstrating superior robustness under sparse-view conditions.

  </details>

- **[Diff3R: Feed-forward 3D Gaussian Splatting with Uncertainty-aware Differentiable Optimization](https://arxiv.org/abs/2604.01030)**  
  *Yueh-Cheng Liu, Jozef Hladký, Matthias Nießner, Angela Dai*  
  `2026-04-01` · `cs.CV` · [abs](https://arxiv.org/abs/2604.01030) · [pdf](https://arxiv.org/pdf/2604.01030.pdf)
  > 💡 通过可微优化层和不确定性模型，将前馈预测与测试时优化结合，提升3DGS渲染质量与鲁棒性。

  <details><summary>Abstract</summary>

  Recent advances in 3D Gaussian Splatting (3DGS) present two main directions: feed-forward models offer fast inference in sparse-view settings, while per-scene optimization yields high-quality renderings but is computationally expensive. To combine the benefits of both, we introduce Diff3R, a novel framework that explicitly bridges feed-forward prediction and test-time optimization. By incorporating a differentiable 3DGS optimization layer directly into the training loop, our network learns to predict an optimal initialization for test-time optimization rather than a conventional zero-shot result. To overcome the computational cost of backpropagating through the optimization steps, we propose computing gradients via the Implicit Function Theorem and a scalable, matrix-free PCG solver tailored for 3DGS optimization. Additionally, we incorporate a data-driven uncertainty model into the optimization process by adaptively controlling how much the parameters are allowed to change during optimization. This approach effectively mitigates overfitting in under-constrained regions and increases robustness against input outliers. Since our proposed optimization layer is model-agnostic, we show that it can be seamlessly integrated into existing feed-forward 3DGS architectures for both pose-given and pose-free methods, providing improvements for test-time optimization.

  </details>

- **[AA-Splat: Anti-Aliased Feed-forward Gaussian Splatting](https://arxiv.org/abs/2603.29394)**  
  *Taewoo Suh, Sungpyo Kim, Jongmin Park, Munchurl Kim*  
  `2026-03-31` · `cs.CV` · [abs](https://arxiv.org/abs/2603.29394) · [pdf](https://arxiv.org/pdf/2603.29394.pdf)
  > 💡 前馈3DGS在变分辨率下产生锯齿，AA-Splat通过OBBL双组件实现抗锯齿，PSNR提升5.4~7.5dB。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting (FF-3DGS) emerges as a fast and robust solution for sparse-view 3D reconstruction and novel view synthesis (NVS). However, existing FF-3DGS methods are built on incorrect screen-space dilation filters, causing severe rendering artifacts when rendering at out-of-distribution sampling rates. We firstly propose an FF-3DGS model, called AA-Splat, to enable robust anti-aliased rendering at any resolution. AA-Splat utilizes an opacity-balanced band-limiting (OBBL) design, which combines two components: a 3D band-limiting post-filter integrates multi-view maximal frequency bounds into the feed-forward reconstruction pipeline, effectively band-limiting the resulting 3D scene representations and eliminating degenerate Gaussians; an Opacity Balancing (OB) to seamlessly integrate all pixel-aligned Gaussian primitives into the rendering process, compensating for the increased overlap between expanded Gaussian primitives. AA-Splat demonstrates drastic improvements with average 5.4$\sim$7.5dB PSNR gains on NVS performance over a state-of-the-art (SOTA) baseline, DepthSplat, at all resolutions, between $4\times$ and $1/4\times$. Code will be made available.

  </details>

