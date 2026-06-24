# Editing / Stylization / Watermark

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---







## 2026-06-24

- **[Geometry-Aware Style Transfer in 3D Gaussian Splatting](https://arxiv.org/abs/2606.24144)**  
  *Min Hyeok Bang, Jun Hyeong Kim, Seung-Wook Kim, Se-Ho Lee*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24144) · [pdf](https://arxiv.org/pdf/2606.24144.pdf)
  > 💡 针对3DGS风格迁移忽视几何结构的局限，提出解耦优化与几何感知对比特征匹配，实现外观与几何同步迁移并显著提升效果。

  <details><summary>Abstract</summary>

  In this paper, we present a novel geometry-aware style transfer framework for 3D Gaussian splatting (3DGS) that simultaneously transfers appearance attributes and geometric structures. Unlike prior works that primarily focus on color-based stylization and often overlook structural adaptation, our method explicitly incorporates geometry adaptation through a decoupled optimization scheme that alternately updates color and geometry parameters. This strategy alleviates potential interference between color and geometry updates, leading to stable and consistent scene-level geometry transformation. The decoupled optimization is enabled by the proposed geometry-aware contrastive feature matching (GCFM). GCFM integrates RGB, depth, and edge cues into a contrastive objective and is employed in both optimization phases to effectively transfer structural characteristics from style images to Gaussian primitives. Extensive experiments show that our approach achieves superior performance in both qualitative fidelity and quantitative metrics, significantly outperforming existing 3DGS-based stylization methods. Our code is available at \href{https://github.com/oweixx/gast}{https://github.com/oweixx/gast}.

  </details>

## 2026-06-23

- **[From Uncertainty to Stability and Fidelity: Guiding Sparse-View 3D Gaussian Splatting with Fisher Information](https://arxiv.org/abs/2606.20842)**  
  *Junbao Zhou, Qingshan Xu, Yuan Zhou, Xiaolong Shen, Beier Zhu, Kesen Zhao, Yiming Zeng, Chen Bai, Cheng Lu, Hanwang Zhang*  
  `2026-06-18` · `cs.CV` · [abs](https://arxiv.org/abs/2606.20842) · [pdf](https://arxiv.org/pdf/2606.20842.pdf)
  > 💡 利用Fisher信息指导立体增强与不确定性正则化，减少随机性，提升稀疏视图3DGS的稳定性和渲染保真度。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has emerged as a promising technique for novel view synthesis. However, 3DGS requires dense input views to achieve high-quality rendering. In sparse-view scenarios, 3DGS often prones to overfitting, resulting in noticeable artifacts and degraded rendering quality. Previous methods explore to address this issue by introducing additional priors (e.g. depth priors) or integrating regularization techniques (e.g. Dropout). However, these methods are often applied without principled guidance. In particular, prior-based augmentation typically samples novel viewpoints randomly, while Dropout-based regularization randomly removes Gaussians. The compounded randomness introduces uncertainty and instability, limiting the fidelity of novel view synthesis. In this paper, we propose a novel method for sparse-view 3DGS that incorporates Fisher Information to quantitatively guide the utilization of geometric priors and regularization. Specifically, our method comprises two key components: (1) Stereo augmentation with Fisher Information. By leveraging Fisher Information, we actively select most informative supporting views and use depth priors to curate reliable pseudo ground truths, which reduces randomness in augmentation and improves stability and rendering fidelity; (2) Uncertainty-aware regularization. We reduce the instability of Dropout-based regularization by using Fisher Information to quantitatively measure the uncertainty of each 3D Gaussian, and adaptively adjust the removal probability, leading to more stable and effective regularization. With these two components, our method effectively mitigates overfitting and improves the stability of optimization in sparse-view 3DGS, resulting in superior rendering fidelity. Extensive experiments show that our method achieves state-of-the-art performance in sparse-view novel view synthesis benchmarks.

  </details>

## 2026-06-10

- **[GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning](https://arxiv.org/abs/2606.10612)**  
  *Haoliang Han, Ziyuan Luo, Renjie Wan*  
  `2026-06-09` · `cs.CV` · [abs](https://arxiv.org/abs/2606.10612) · [pdf](https://arxiv.org/pdf/2606.10612.pdf)
  > 💡 针对3DGS模型溯源问题，提出属性统计与编辑模拟辅助LLM推理的框架，构建可解释有向图，无需训练。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is a powerful technique for creating high-fidelity 3D assets. However, the widespread sharing and iterative modification of 3DGS models across digital platforms create pressing challenges for intellectual property protection and forensic traceability. To address this, we propose GaussTrace, a novel framework for constructing directed provenance graphs for 3DGS models. GaussTrace formulates provenance analysis as an evidence-based reasoning problem. It builds upon attribute-wise statistical profiling of 3DGS parameters to capture intrinsic properties. Moreover, we introduce hypothesis-driven editing simulations of common operations to provide auxiliary evidence for plausible transformation pathways. These statistical and simulated cues jointly enable a Large Language Model (LLM) to perform structured Chain-of-Thought (CoT) reasoning, yielding directional provenance inferences and explainable edge reasons. Experimental results demonstrate that GaussTrace effectively constructs evolutionary relationships among diverse 3DGS models, delivering accurate, interpretable, and robust provenance graphs without requiring model training or access to editing histories. Project page: https://haolianghan.github.io/GaussTrace.

  </details>

## 2026-06-09

- **[MaterialClusterGS: Palette-Based Material Decomposition and Physically-Based Relighting with 2D Gaussian Splatting](https://arxiv.org/abs/2606.09018)**  
  *Hao Zhang, Ang Li, Boyan Du, Junke Zhu, Fei Zhu, Meng Gai, Zhangjin Huang, Guoping Wang, Sheng Li*  
  `2026-06-08` · `cs.GR` · [abs](https://arxiv.org/abs/2606.09018) · [pdf](https://arxiv.org/pdf/2606.09018.pdf)
  > 💡 用调色板基材质分解和连续空间材质场解决高斯逆渲染材质欠约束问题，实现物理可重光照与编辑。

  <details><summary>Abstract</summary>

  We present MaterialClusterGS, a palette-based material decomposition framework for 2D Gaussian Splatting that enables physically based relighting and material editing. Existing Gaussian inverse rendering methods typically assign independent BRDF parameters to individual primitives. While flexible, this local fitting strategy makes material recovery highly under-constrained: shadows, indirect illumination, geometric errors, and visibility residuals can be absorbed into thousands of slightly different local material estimates. Meanwhile, recent palette-based appearance methods operate solely in RGB space without modeling physical materials or illumination. To bridge this gap, we represent scene materials using a compact global palette of shared BRDF prototypes assigned via a continuous spatial material field. Without shared material structure, editing one region does not propagate consistently to others of the same material, making per-primitive decompositions impractical for editing. We jointly optimize the material field, palette prototypes, and environment lighting under a physically based rendering objective. The resulting framework recovers compact, spatially coherent attributes directly usable for material editing, relighting, and transfer.

  </details>

- **[GraspFoM: Towards Reconstruction-Driven Robotic Grasping with 3D Foundation Priors](https://arxiv.org/abs/2606.08440)**  
  *Dongli Wu, Xiaobao Wei, Hao Wang, Qiaochu Dong, Ying Li, Qingpo Wuwu, Ming Lu, Wufan Zhao*  
  `2026-06-07` · `cs.RO` · [abs](https://arxiv.org/abs/2606.08440) · [pdf](https://arxiv.org/pdf/2606.08440.pdf)
  > 💡 利用SAM

  <details><summary>Abstract</summary>

  Robotic grasping is a fundamental capability in robotic manipulation. Yet grasping remains challenging under partial observations. Reliable grasping depends on both local contact cues and object-level 3D structure. Existing geometry-aware grasping methods recognize the value of reconstruction, but they typically treat geometry as an intermediate prediction rather than a reusable object prior for grasping. In this paper, we present GraspFoM, a unified framework that leverages 3D foundation priors (SAM3D) to build a shared 3D object latent for both reconstruction and grasp pose prediction. Built on this shared object latent, we introduce an anchor-initialized truncated pose-reasoning diffuser that predicts continuous and multimodal grasp poses without directly relying on discrete grasp candidates. We further investigate the interaction between reconstruction and grasping through a reconstruction-aware scorer and a residual latent updater. Reconstruction provides grounded geometric cues, while grasp supervision refines the shared object latent toward grasp-relevant affordances. GraspFoM jointly predicts grasp poses and reconstructs high-fidelity 3D assets in mesh and 3DGS forms. Comprehensive experiments demonstrate that GraspFoM achieves state-of-the-art results on both reconstruction and grasping. Notably, these improvements require only a small number of additional trainable parameters. Component-wise ablation studies also demonstrate the contribution of each component.

  </details>

## 2026-06-06

- **[MLP Splatting: Object-Centric Neural Fields](https://arxiv.org/abs/2606.03877)**  
  *Shinjeong Kim, Yuzhou Cheng, Xin Kong, Paul H. J. Kelly, Andrew J. Davison*  
  `2026-06-02` · `cs.CV` · [abs](https://arxiv.org/abs/2606.03877) · [pdf](https://arxiv.org/pdf/2606.03877.pdf)
  > 💡 以紧凑MLP光场基元替代高斯基元，实现高效场景分解和新视图合成，内存和渲染速度显著优于语义3DGS。

  <details><summary>Abstract</summary>

  3D representations are fundamental to scene rendering, understanding, and interaction. Recent approaches, such as 3D Gaussian Splatting and Neural Radiance Fields, achieve impressive photorealistic novel-view synthesis, but lack the ability to easily decompose scene elements into a few primitives, requiring additional segmentation or grouping for object-level manipulation. We present MLP-Splatting, a method that enables scene decomposition via a few expressive light-field primitives while providing photorealistic novel-view synthesis. MLP-Splatting models each primitive as an independent compact MLP with localized spatial support that predicts radiance and opacity. In contrast to low-level Gaussian primitives or a single global radiance field, our neural primitives provide greater expressive capacity while remaining spatially localized. Rendering is performed through efficient sparse volumetric compositing over ray-primitive interactions. Our primitives are supervised using RGB supervision alone, which yields primitives that represent local scene regions often corresponding to objects or object parts, enabling interactive object-level editing without segmentation masks by selecting a handful of primitives. Our method, augmented with optional semantic feature distillation, enables open-vocabulary scene interaction and open-set instant segmentation. Compared to state-of-the-art methods, we achieve substantially lower memory usage (1/15$\times$) and faster rendering (3$\times$), as we show in our experiments compared to semantic 3DGS methods. Project Page: https://shinjeongkim.com/mlp-splatting

  </details>

## 2026-06-01

- **[Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419)**  
  *Nicholas Fry, Eric Dexheimer, Kirill Mazur, Paul H. J. Kelly, Andrew J. Davison*  
  `2026-05-29` · `cs.CV` · [abs](https://arxiv.org/abs/2605.31419) · [pdf](https://arxiv.org/pdf/2605.31419.pdf)
  > 💡 提出基于可微三角形splatting的密集RGB-D SLAM，实现跟踪与建图，支持在线网格编辑，几何性能优于基线。

  <details><summary>Abstract</summary>

  We present a dense RGB-D SLAM system using differentiable triangles as the 3D map representation. While 3D Gaussian Splatting has emerged as the leading method for novel-view synthesis, triangles remain the standard primitive for traditional rendering hardware, game engines, and downstream tasks requiring explicit geometry such as simulation, collision, and editing. Recent offline methods have demonstrated that an unstructured 'triangle soup' can be optimised into a photorealistic mesh via Delaunay triangulation across a set of posed images. Building upon this insight, we present the first dense SLAM system to employ Triangle Splatting to perform both tracking and mapping through online differentiable rendering of a triangle soup. The map can be converted into a connected mesh on-the-fly via restricted Delaunay triangulation, enabling new online capabilities such as mesh deformation and collision checking. On Replica and TUM-RGBD, our system outperforms baselines on 3D geometry, matches the camera-tracking accuracy, and enables online mesh-based scene editing.

  </details>

## 2026-05-30

- **[Boosting Zero-Shot 3D Style Transfer with 2D Pre-trained Priors](https://arxiv.org/abs/2605.30065)**  
  *Xin Dong, Yunzhi Teng, Wenfeng Deng, Yansong Tang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30065) · [pdf](https://arxiv.org/pdf/2605.30065.pdf)
  > 💡 融合2D预训练解码器与特征高斯泼溅，解决数据稀缺问题，实现高质量零样本3D风格迁移。

  <details><summary>Abstract</summary>

  In this work, we focus on zero-shot 3D style transfer that can generate multi-view consistent stylized views of the 3D scene given an arbitrary style image. We primarily tackle the issue of data scarcity in 3D style transfer, which arises when each model is trained on only a single scene, thereby limiting the number of available content images. This scarcity significantly hampers stylization performance, as model optimization relies on a sufficient number of content-style image pairs to provide supervisory signals. Our core idea is to integrate a decoder pre-trained on large-scale 2D image datasets into the 3D style transfer pipeline, thereby leveraging the prior knowledge encoded in the decoder from learning over numerous content-style image pairs. Our method combines feature Gaussian splatting and deferred stylization, enabling high-quality stylization with the data-sufficient decoder network while ensuring view consistency by unifying view-dependent operations into a view-invariant process. Experiments demonstrate that our Data-Sufficient StyleGaussian (DS-StyleGaussian) model outperforms existing zero-shot 3D style transfer methods in terms of visual quality across various datasets. This work also suggests that 2D pre-training can serve as a strong enhancement for 3D tasks, bridging the data gap between 2D and 3D.

  </details>

- **[BitC-3DGS: High-Capacity 3D Gaussian Splatting Watermarking via Bit Compression](https://arxiv.org/abs/2605.29583)**  
  *Yuquan Bi, Baosheng Yu, Yingke Lei, Jianwei Yang, Hongsong Wang, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29583) · [pdf](https://arxiv.org/pdf/2605.29583.pdf)
  > 💡 现有3DGS水印受限于77位容量，提出BitC-3DGS位压缩方案，通过双分支架构与硬消息采样实现128位高容量水印。

  <details><summary>Abstract</summary>

  High-capacity watermarking is necessary for 3D Gaussian Splatting (3DGS) assets to embed rich information (e.g., ownership, provenance, and authentication codes), enabling reliable identification and integrity verification in large-scale 3D asset pipelines. Existing bit-to-token watermarking methods based on a pre-trained text encoder are limited to 77-bit messages due to CLIP's fixed 77-token context length, as tokens beyond this limit are unsupported by learned positional embeddings. To address this limitation, we introduce BitC-3DGS, a bit-compression framework that encodes multiple message bits per token. It employs a bit-compressed tokenization scheme that encodes multiple bits within the same chunk into a single semantic token. To enable recovery of the compressed information, it further introduces a dual-branch architecture for joint chunk decompression and bit decoding, along with a hard-message sampling strategy to improve combinatorial coverage during decoder training. Extensive experiments on the Blender and LLFF datasets demonstrate the effectiveness of BitC-3DGS for high-capacity watermarking, achieving high message recovery accuracy and rendering fidelity. For example, it supports 128-bit message capacity with recovery accuracy comparable to that of 64-bit messages in recent state-of-the-art methods.

  </details>

- **[Learning Structural Latent Points for Efficient Visual Representations in Robotic Manipulation](https://arxiv.org/abs/2605.21258)**  
  *Yicheng Jiang, Jiaxu Wang, Junhao He, Zesen Gan, Junhao Li, Qiang Zhang, Jingkai Sun, Jiahang Cao, Mingyuan Sun, Xiangyu Yue, Qiming Shao*  
  `2026-05-20` · `cs.RO` · [abs](https://arxiv.org/abs/2605.21258) · [pdf](https://arxiv.org/pdf/2605.21258.pdf)
  > 💡 针对隐式和显式表示的缺陷，提出结构潜点混合表示，通过潜变量变分自编码器正则化，在机器人操作任务上取得一致性能提升。

  <details><summary>Abstract</summary>

  Current 3D-aware pretraining methods for embodied perception and manipulation are largely built on differentiable rendering frameworks, producing either fully implicit neural fields or fully explicit geometric primitives. Implicit representations, while expressive, lack explicit structural cues, whereas explicit ones preserve geometry but suffer from resolution limits and weak generalization. To address these limitations, we propose a novel pretraining framework that learns a hybrid representation-structural latent points. Specifically, we insert a point-wise latent variational autoencoder into the latent space of a point-cloud autoencoder, jointly regularizing point-wise features and coordinates toward a Gaussian prior. The resulting compact latent preserves coarse structural tendencies, which do not encode precise geometry but capture richer rough shape and semantic information, effectively combining the expressiveness of implicit representations with the structural priors of explicit ones. In addition, informed by shared design choices in prior work, we develop a streamlined, efficient 3DGS-based rendering pipeline that is deliberately kept lightweight, improving efficiency while leaving greater representational capacity to the front-end latent module. Extensive evaluations on RLBench, ManiSkill2, and a real-robot platform demonstrate consistent gains in task success, sample efficiency, and robustness to viewpoint and scene variations over strong baselines. Ablation studies further confirm that each component of our framework is critical to overall performance.

  </details>

- **[GLUT: 3D Gaussian Lookup Table for Continuous Color Transformation](https://arxiv.org/abs/2605.19889)**  
  *Danna Xue, David Serrano-Lozano, Shaolin Su, Javier Vazquez-Corral*  
  `2026-05-19` · `cs.GR` · [abs](https://arxiv.org/abs/2605.19889) · [pdf](https://arxiv.org/pdf/2605.19889.pdf)
  > 💡 针对3D LUT离散化导致容量-内存权衡和不可解释性，提出基于可学习3D高斯原语的连续显式颜色变换

  <details><summary>Abstract</summary>

  3D Lookup Tables (3D LUTs) are widely used for color mapping, but their grid-based representation requires discretizing the RGB space, leading to a capacity-memory trade-off that becomes prohibitive when storing large numbers of LUTs. Recent approaches adopt implicit neural representations to improve scalability, yet their black-box nature limits interpretability and hinders intuitive, localized editing. In this paper, we propose Gaussian LUT (GLUT), a continuous and explicit color representation that models color transformations using a set of learnable 3D Gaussian primitives. By avoiding fixed-resolution grids, GLUT achieves flexible representational capacity while maintaining a compact memory footprint. Its explicit, spatially localized formulation further enables both accurate modeling and interpretability. Building on this representation, we introduce a compact conditional generator (CGLUT) that predicts GLUT parameters for multiple LUT instances, encoding diverse color styles in a single framework to enable smooth and controllable LUT style blending. Moreover, GLUT supports efficient, user-friendly editing by allowing localized adjustments to specific color regions without global retraining. Experimental results demonstrate that our approach outperforms prior neural LUT representations in both accuracy and efficiency, while offering improved interpretability and interactive control.

  </details>

- **[RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting](https://arxiv.org/abs/2605.18263)**  
  *Ji Shi, Xianghua Ying, Bowei Xing, Ruohao Guo, Wenzhen Yue*  
  `2026-05-18` · `cs.CV` · [abs](https://arxiv.org/abs/2605.18263) · [pdf](https://arxiv.org/pdf/2605.18263.pdf)
  > 💡 针对半透明镜面场景，将高斯几何占据与光学透明度解耦，通过混合渲染和梯度门控实现高保真反射与清晰透射的实时渲染。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables real-time novel view synthesis with high visual quality. However, existing methods struggle with semi-transparent specular surfaces that exhibit both complex reflections and clear transmission, often producing blurry reflections or overly occluded transmission. To address this, we present RT-Splatting, a framework that disentangles each Gaussian's geometric occupancy from its optical opacity. This factorization yields a unified surface-volume scene representation with a single set of Gaussian primitives. Our hybrid renderer interprets this representation both as a surface to capture high-frequency reflections and as a volume to preserve clear transmission. To mitigate the ambiguity in jointly optimizing reflection and transmission, we introduce Specular-Aware Gradient Gating, which suppresses misleading gradients from highly specular regions into the transmission branch, effectively reducing distracting floaters. Experiments on challenging semi-transparent scenes show that RT-Splatting achieves state-of-the-art performance, delivering high-fidelity reflections and clear transmission with real-time rendering. Moreover, our factorization naturally enables flexible scene editing. The project page is available at https://sjj118.github.io/RT-Splatting.

  </details>

- **[Robust Prior-Guided Segmentation for Editable 3D Gaussian Splatting](https://arxiv.org/abs/2605.16065)**  
  *Raushan Joshi, Jean-Yves Guillemaut*  
  `2026-05-15` · `cs.CV` · [abs](https://arxiv.org/abs/2605.16065) · [pdf](https://arxiv.org/pdf/2605.16065.pdf)
  > 💡 提出先验引导分割，利用SAM-HQ生成精确掩码并多视图一致分配标签，实现高精度可编辑3DGS。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3D-GS) enables real-time 3D scene reconstruction but lacks robust segmentation for editing tasks such as object removal, extraction, and recoloring. Existing approaches that lift 2D segmentations to the 3D domain suffer from view inconsistencies and coarse masks. In this paper, we propose a novel framework that leverages the Segment Anything Model High Quality (SAM-HQ) to generate accurate 2D masks, addressing the limitations of the standard SAM in boundary fidelity and fine-structure preservation. To achieve robust 3D segmentation of any target object in a given scene, we introduce a prior-guided label reassignment method that assigns labels to 3D Gaussians by enforcing multiview consistency with learned priors. Our approach achieves state-of-the-art segmentation accuracy and enables interactive, real-time object editing while maintaining high visual fidelity. Qualitative results demonstrate superior boundary preservation and practical utility in Virtual Reality (VR) and robotics, advancing 3D scene editing.

  </details>

- **[GuardMarkGS: Unified Ownership Tracing and Edit Deterrence for 3D Gaussian Splatting](https://arxiv.org/abs/2605.12919)**  
  *Utae Jeong, Jaewan Choi, Junseok Lee, Jongheon Jeong, Sang Ho Yoon, ByoungSoo Koh, Sangpil Kim*  
  `2026-05-13` · `cs.CV` · [abs](https://arxiv.org/abs/2605.12919) · [pdf](https://arxiv.org/pdf/2605.12919.pdf)
  > 💡 首个针对3DGS的统一保护框架，联合场景水印与对抗编辑阻止，平衡了所有权追踪、编辑阻止和渲染质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is becoming a practical representation for novel view synthesis, but its growing adoption, together with rapid advances in instruction-driven 3DGS editing, also exposes a dual copyright risk: once a 3DGS-based asset is released, it can be used without permission and manipulated through 3D editing. Existing protection methods address only one side of this problem. Watermarking can trace ownership after unauthorized use, but it cannot prevent malicious editing. Adversarial edit-deterrence methods can disrupt editing, but they do not provide evidence of ownership. To the best of our knowledge, we present the first unified protection framework for 3DGS that jointly optimizes ownership tracing and unauthorized editing deterrence. Our framework combines a scene-wide watermarking objective over all Gaussians with an adversarial objective for edit deterrence. The adversarial branch combines latent-anchor separation, denoising-trajectory diversion, and cross-attention diversion to divert the editing trajectory, while an update-saliency-motivated Gaussian selection strategy assigns stronger adversarial updates to mask-selected Gaussians, improving the balance among watermark recovery, edit deterrence, and rendering fidelity. Experiments on scenes from Mip-NeRF 360 and Instruct-NeRF2NeRF demonstrate that the proposed framework achieves a favorable balance among bit accuracy, edit deterrence, and rendering quality. These results suggest that practical copyright protection of 3DGS-based assets can be more effectively addressed by integrating ownership tracing and unauthorized editing deterrence into a single optimization framework.

  </details>

- **[BEA-GS: BEyond RAdiance Supervision in 3DGS for Precise Object Extraction](https://arxiv.org/abs/2605.09662)**  
  *Alessio Mazzucchelli, Maria Naranjo-Almeida, Jorge Bustos-Sanchez, Mariella Dimiccoli, Francesc Moreno-Noguer, Jordi Sanchez-Riera, Adrian Penate-Sanchez*  
  `2026-05-10` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09662) · [pdf](https://arxiv.org/pdf/2605.09662.pdf)
  > 💡 针对3DGS对象提取边界不精确问题，提出几何优化与不可见高斯调整损失，实现最佳边界分割。

  <details><summary>Abstract</summary>

  Most Gaussian Splatting techniques that provide a 3D semantic representation of the scene do not optimize the underlying 3D geometry, making object-level editing or asset extraction challenging. Recent methods, such as COBGS, Trace3D, ObjectGS, acknowledge this limitation and propose approaches that modify the scene's geometry to represent the underlying semantics. We advance this concept further by proposing a novel solution that provides near perfect boundaries in object extraction. We do so by introducing two new losses in the optimization that take care of: 1) a loss that modifies the geometry of visible Gaussians to respect semantic boundaries, and 2) a loss that adjusts the geometry of non-visible Gaussians that appear once the object is extracted. Our first loss propagates gradients directly through the rasterization, allowing for seamless integration within the optimization of the Gaussian parameters. The second loss also propagates gradients to Gaussian parameters but does so without passing through the rasterization, enabling modification of the scene's geometry even when little transmittance reaches a Gaussian (partial or non-visible). Exhaustive comparisons with 12 state of the art methods across 4 datasets, using six metrics, demonstrate that our approach produces overall the best boundary segmentation to date.

  </details>

- **[Relightable Gaussian Splatting for Virtual Production Using Image-Based Illumination](https://arxiv.org/abs/2605.09024)**  
  *Adrian Azzarelli, Nantheera Anantrasirichai, James Pollock, David R. Bull*  
  `2026-05-09` · `cs.CV` · [abs](https://arxiv.org/abs/2605.09024) · [pdf](https://arxiv.org/pdf/2605.09024.pdf)
  > 💡 针对虚拟制作中LED墙照明耦合问题，提出高斯溅射重照明框架，利用背景图像条件化与图元参数化实现高质量高效重渲染。

  <details><summary>Abstract</summary>

  Virtual production (VP) use LED walls to provide both background imagery and image-based lighting. While this enables on-set compositing, it couples lighting to background and scene appearance, limiting flexibility for downstream editing. In addition, inverse rendering conventionally relies on physically-based rendering to estimates 3D geometry and lighting, using environment maps. However, these maps are typically low-resolution and assume far-field lighting. In VP, with near-field and high-resolution image-based lighting, this can lead to inaccuracies and introduce complexities when editing. Addressing this, we propose a VP-specific framework for 3D reconstruction and relighting using Gaussian Splatting. This uses the known background imagery to condition the relighting process. This avoids relying on environment maps and reduces compositing to a background-image editing task. To realize our framework, we introduce a process (and associated dataset) that captures real VP scenes under varying background content and illumination conditions. This data is used to decompose a 3D scene into fixed appearance and variable lighting components. The variable lighting process simulates light transport by parameterizing each primitive with a UV coordinate, intensity value and resolution modifier. Using mipmaps, these directly sample the background texture in image space - implicitly capturing reflections and refractions without physically-based rendering. Combined with the fixed appearance component, this allows us to render relit scenes using a Gaussian Splatting rasterizer. Compared to baselines, our approach achieves higher-quality 3D reconstruction and controllable relighting. The method is efficient (<3 GB RAM, <5 GB VRAM, <2 hours training, ~35 FPS) and supports rendering useful arbitrary output variables including depth, lighting intensity, lighting color, and unlit renders.

  </details>

- **[GOR-IS: 3D Gaussian Object Removal in the Intrinsic Space](https://arxiv.org/abs/2605.00498)**  
  *Yonghao Zhao, Yupeng Gao, Jian Yang, Jin Xie, Beibei Wang*  
  `2026-05-01` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00498) · [pdf](https://arxiv.org/pdf/2605.00498.pdf)
  > 💡 通过内在空间分解与光传输建模，解决3DGS物体移除中光照不一致和非朗伯表面问题，实现物理与视觉连贯修复。

  <details><summary>Abstract</summary>

  Recent advances in Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have made it standard practice to reconstruct 3D scenes from multi-view images. Removing objects from such 3D representations is a fundamental editing task that requires complete and seamless inpainting of occluded regions, ensuring consistency in geometry and appearance. Although existing methods have made notable progress in improving inpainting consistency, they often neglect global lighting effects, leading to physically implausible results. Moreover, these methods struggle with view-dependent non-Lambertian surfaces, where appearance varies across viewpoints, leading to unreliable inpainting. In this paper, we present 3D Gaussian Object Removal in the Intrinsic Space (GOR-IS), a novel framework for physically consistent and visually coherent 3D object removal. Our approach decomposes the scene into intrinsic components and explicitly models light transport to maintain global lighting effects consistency. Furthermore, we introduce an intrinsic-space inpainting module that operates directly in the material and lighting domains, effectively addressing the challenges posed by non-Lambertian surfaces. Extensive experiments on both synthetic and real-world datasets demonstrate that our framework substantially improves the physical consistency and visual coherence of object removal, outperforming existing methods by 13% in perceptual similarity (LPIPS) and 2dB in peak signal-to-noise ratio (PSNR). Code is publicly available at https://applezyh.github.io/GOR-IS-project-page/

  </details>

- **[Point Group Symmetry of Polyhedral Diagrams in Graphic Statics](https://arxiv.org/abs/2604.25695)**  
  *Yefan Zhi, Yao Lu, Masoud Akbarzadeh*  
  `2026-04-28` · `cs.CG` · [abs](https://arxiv.org/abs/2604.25695) · [pdf](https://arxiv.org/pdf/2604.25695.pdf)
  > 💡 针对图形静力学中多面体图对称性易破坏问题，引入点群并约束等边长度，实现对称保持与优化。

  <details><summary>Abstract</summary>

  Symmetry is an implicit objective in structural form-finding that often reconciles efficiency and aesthetics. This paper identifies the symmetry of polyhedral diagrams in three-dimensional graphic statics (3DGS) as point groups and formulates them as constraints, enabling the optimization and manipulation of polyhedral diagrams that preserve such symmetry. 3DGS has been an efficient and effective tool for the form-finding of funicular structures. However, when modifying complex diagrams for design exploration or optimization, one can easily break the symmetry of the reciprocal design input, rendering the result undesirable for practical use. To address this problem, this paper investigates symmetry transformations and introduces point groups, an abstract algebra tool commonly used in crystallography to represent the symmetry and equivalence between a network of atoms (points with labels). It then discusses the hierarchy of symmetry in the geometry types of a polyhedral diagram, and proposes the constraint of symmetry through edge lengths. Based on the crystal symmetry search algorithm by spglib and pymatgen, a fast fingerprinting algorithm is developed to identify the point group of a polyhedral diagram and sort equivalent edges into sets. Finally, the paper shows that the necessary and sufficient condition for preserving the point group symmetry is that each set of edges has the same length. This constraint is compatible with the algebraic formulation of 3DGS and effectively preserves symmetry while reducing the dimension of the solution space. The method is implemented in the PolyFrame 2 plug-in for Rhino and Grasshopper.

  </details>

- **[TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing](https://arxiv.org/abs/2604.19571)**  
  *Yanhui Chen, Jiahong Li, Jingchao Wang, Junyi Lin, Zixin Zeng, Yang Shi*  
  `2026-04-21` · `cs.CV` · [abs](https://arxiv.org/abs/2604.19571) · [pdf](https://arxiv.org/pdf/2604.19571.pdf)
  > 💡 针对语言驱动3DGS编辑中2D与3D语义对应缺失，提出多视图不平衡语义传输方法显式建模对应关系并抑制编辑泄露，提升局部编辑精度和结构一致性。

  <details><summary>Abstract</summary>

  Language-driven 3D Gaussian Splatting (3DGS) editing provides a more convenient approach for modifying complex scenes in VR/AR. Standard pipelines typically adopt a two-stage strategy: first editing multiple 2D views, and then optimizing the 3D representation to match these edited observations. Existing methods mainly improve view consistency through multi-view feature fusion, attention filtering, or iterative recalibration. However, they fail to explicitly address a more fundamental issue: the semantic correspondence between edited 2D evidence and 3D Gaussians. To tackle this problem, we propose TransSplat, which formulates language-driven 3DGS editing as a multi-view unbalanced semantic transport problem. Specifically, our method establishes correspondences between visible Gaussians and view-specific editing prototypes, thereby explicitly characterizing the semantic relationship between edited 2D evidence and 3D Gaussians. It further recovers a cross-view shared canonical 3D edit field to guide unified 3D appearance updates. In addition, we use transport residuals to suppress erroneous edits in non-target regions, mitigating edit leakage and improving local control precision. Qualitative and quantitative results show that, compared with existing 3D editing methods centered on enhancing view consistency, TransSplat achieves superior performance in local editing accuracy and structural consistency.

  </details>

- **[Instant Colorization of Gaussian Splats](https://arxiv.org/abs/2604.17155)**  
  *Daniel Lieber, Alexander Mock, Nils Wandel*  
  `2026-04-18` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17155) · [pdf](https://arxiv.org/pdf/2604.17155.pdf)
  > 💡 针对将2D信息高效映射回3D高斯场景的任务，用法方程求解加权最小二乘，实现快速重光照、特征增强和语义分割。

  <details><summary>Abstract</summary>

  Gaussian Splatting has recently become one of the most popular frameworks for photorealistic 3D scene reconstruction and rendering. While current rasterizers allow for efficient mappings of 3D Gaussian splats onto 2D camera views, this work focuses on mapping 2D image information (e.g. color, neural features or segmentation masks) efficiently back onto an existing scene of Gaussian splats. This 'opposite' direction enables applications ranging from scene relighting and stylization to 3D semantic segmentation, but also introduces challenges, such as view-dependent colorization and occlusion handling. Our approach tackles these challenges using the normal equation to solve a visibility-weighted least squares problem for every Gaussian and can be implemented efficiently with existing differentiable rasterizers. We demonstrate the effectiveness of our approach on scene relighting, feature enrichment and 3D semantic segmentation tasks, achieving up to an order of magnitude speedup compared to gradient descent-based baselines.

  </details>

- **[Neural Gabor Splatting: Enhanced Gaussian Splatting with Neural Gabor for High-frequency Surface Reconstruction](https://arxiv.org/abs/2604.15941)**  
  *Haato Watanabe, Nobuyuki Umetani*  
  `2026-04-17` · `cs.CV` · [abs](https://arxiv.org/abs/2604.15941) · [pdf](https://arxiv.org/pdf/2604.15941.pdf)
  > 💡 使用轻量MLP增强高斯基元建模颜色变化，配合频率感知稠密化策略，实现高频表面的高效精确重建。

  <details><summary>Abstract</summary>

  Recent years have witnessed the rapid emergence of 3D Gaussian splatting (3DGS) as a powerful approach for 3D reconstruction and novel view synthesis. Its explicit representation with Gaussian primitives enables fast training, real-time rendering, and convenient post-processing such as editing and surface reconstruction. However, 3DGS suffers from a critical drawback: the number of primitives grows drastically for scenes with high-frequency appearance details, since each primitive can represent only a single color, requiring multiple primitives for every sharp color transition. To overcome this limitation, we propose neural Gabor splatting, which augments each Gaussian primitive with a lightweight multi-layer perceptron that models a wide range of color variations within a single primitive. To further control primitive numbers, we introduce a frequency-aware densification strategy that selects mismatch primitives for pruning and cloning based on frequency energy. Our method achieves accurate reconstruction of challenging high-frequency surfaces. We demonstrate its effectiveness through extensive experiments on both standard benchmarks, such as Mip-NeRF360 and High-Frequency datasets (e.g., checkered patterns), supported by comprehensive ablation studies.

  </details>

- **[SSD-GS: Scattering and Shadow Decomposition for Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2604.13333)**  
  *Iris Zheng, Guojun Tang, Alexander Doronin, Paul Teal, Fang-Lue Zhang*  
  `2026-04-14` · `cs.CV` · [abs](https://arxiv.org/abs/2604.13333) · [pdf](https://arxiv.org/pdf/2604.13333.pdf)
  > 💡 针对现有3DGS重光照中阴影与散射建模不足，提出四项物理分解模型，实现

  <details><summary>Abstract</summary>

  We present SSD-GS, a physically-based relighting framework built upon 3D Gaussian Splatting (3DGS) that achieves high-quality reconstruction and photorealistic relighting under novel lighting conditions. In physically-based relighting, accurately modeling light-material interactions is essential for faithful appearance reproduction. However, existing 3DGS-based relighting methods adopt coarse shading decompositions, either modeling only diffuse and specular reflections or relying on neural networks to approximate shadows and scattering. This leads to limited fidelity and poor physical interpretability, particularly for anisotropic metals and translucent materials. To address these limitations, SSD-GS decomposes reflectance into four components: diffuse, specular, shadow, and subsurface scattering. We introduce a learnable dipole-based scattering module for subsurface transport, an occlusion-aware shadow formulation that integrates visibility estimates with a refinement network, and an enhanced specular component with an anisotropic Fresnel-based model. Through progressive integration of all components during training, SSD-GS effectively disentangles lighting and material properties, even for unseen illumination conditions, as demonstrated on the challenging OLAT dataset. Experiments demonstrate superior quantitative and perceptual relighting quality compared to prior methods and pave the way for downstream tasks, including controllable light source editing and interactive scene relighting. The source code is available at: https://github.com/irisfreesiri/SSD-GS.

  </details>

- **[BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields](https://arxiv.org/abs/2604.08410)**  
  *Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Jiacheng Lin, Kailun Yang, Zhiyong Li, Yaonan Wang*  
  `2026-04-09` · `cs.CV` · [abs](https://arxiv.org/abs/2604.08410) · [pdf](https://arxiv.org/pdf/2604.08410.pdf)
  > 💡 利用3DGS场景表示，通过语言解析和三角几何约束定位功能点，实现零样本可解释的灵巧

  <details><summary>Abstract</summary>

  In unstructured environments, functional dexterous grasping calls for the tight integration of semantic understanding, precise 3D functional localization, and physically interpretable execution. Modular hierarchical methods are more controllable and interpretable than end-to-end VLA approaches, but existing ones still rely on predefined affordance labels and lack the tight semantic--pose coupling needed for functional dexterous manipulation. To address this, we propose BLaDA (Bridging Language to Dexterous Actions in 3DGS fields), an interpretable zero-shot framework that grounds open-vocabulary instructions as perceptual and control constraints for functional dexterous manipulation. BLaDA establishes an interpretable reasoning chain by first parsing natural language into a structured sextuple of manipulation constraints via a Knowledge-guided Language Parsing (KLP) module. To achieve pose-consistent spatial reasoning, we introduce the Triangular Functional Point Localization (TriLocation) module, which utilizes 3D Gaussian Splatting as a continuous scene representation and identifies functional regions under triangular geometric constraints. Finally, the 3D Keypoint Grasp Matrix Transformation Execution (KGT3D+) module decodes these semantic-geometric constraints into physically plausible wrist poses and finger-level commands. Extensive experiments on complex benchmarks demonstrate that BLaDA significantly outperforms existing methods in both affordance grounding precision and the success rate of functional manipulation across diverse categories and tasks. Code will be publicly available at https://github.com/PopeyePxx/BLaDA.

  </details>

- **[ColorGradedGaussians: Palette-Based Color Grading for 3D Gaussian Splatting via View-Space Sparse Decomposition](https://arxiv.org/abs/2604.01551)**  
  *Cheng-Kang Ted Chao, Yotam Gingold*  
  `2026-04-02` · `cs.GR` · [abs](https://arxiv.org/abs/2604.01551) · [pdf](https://arxiv.org/pdf/2604.01551.pdf)
  > 💡 通过视空间稀疏分解和逆重心坐标几何损失，实现实时调色板编辑，提升3DGS场景色彩编辑质量。

  <details><summary>Abstract</summary>

  Professional color editing requires precise control over both color (hue and saturation) and lightness, ideally through separate, independent controls. We present a real-time interactive color editing framework for 3D Gaussian Splatting (3DGS) that enables palette-based recoloring, per-palette tone curves for color-aware lightness adjustment, and accurate pixel-level constraints -- capabilities unavailable in prior palette-based 3DGS methods. Existing approaches decompose colors at the primitive level, optimizing per-Gaussian palette weights before splatting. However, sparse primitive-level weights do not guarantee sparse pixel-level decompositions after alpha-blending, causing palette edits to affect unintended regions and degrading editing quality. We address this through view-space palette decomposition, splatting weights instead of colors to optimize the observable appearance of the scene. We introduce a geometric loss using inverse barycentric coordinates to enforce consistent sparsity patterns, ensuring similar colors share similar decompositions. Our approach achieves superior editing quality compared to primitive-space methods, enabling professional color grading workflows for 3DGS scenes with real-time interaction.

  </details>

- **[AdvSplat: Adversarial Attacks on Feed-Forward Gaussian Splatting Models](https://arxiv.org/abs/2603.23686)**  
  *Yiran Qiao, Yiren Lu, Yunlai Zhou, Rui Yang, Linlin Hou, Yu Yin, Jing Ma*  
  `2026-03-24` · `cs.CV` · [abs](https://arxiv.org/abs/2603.23686) · [pdf](https://arxiv.org/pdf/2603.23686.pdf)
  > 💡 首次系统研究前馈式3DGS的对抗攻击，提出白盒与基于频域参数化的黑盒方法，揭示模型脆弱性。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) is increasingly recognized as a powerful paradigm for real-time, high-fidelity 3D reconstruction. However, its per-scene optimization pipeline limits scalability and generalization, and prevents efficient inference. Recently emerged feed-forward 3DGS models address these limitations by enabling fast reconstruction from a few input views after large-scale pretraining, without scene-specific optimization. Despite their advantages and strong potential for commercial deployment, the use of neural networks as the backbone also amplifies the risk of adversarial manipulation. In this paper, we introduce AdvSplat, the first systematic study of adversarial attacks on feed-forward 3DGS. We first employ white-box attacks to reveal fundamental vulnerabilities of this model family. We then develop two improved, practically relevant, query-efficient black-box algorithms that optimize pixel-space perturbations via a frequency-domain parameterization: one based on gradient estimation and the other gradient-free, without requiring any access to model internals. Extensive experiments across multiple datasets demonstrate that AdvSplat can significantly disrupt reconstruction results by injecting imperceptible perturbations into the input images. Our findings surface an overlooked yet urgent problem in this domain, and we hope to draw the community's attention to this emerging security and robustness challenge.

  </details>

