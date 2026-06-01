# Editing / Stylization / Watermark

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---


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

