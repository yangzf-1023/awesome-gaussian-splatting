# Relighting / Material / BRDF

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---







## 2026-07-14

- **[SalientGS: Unified SfM-to-3DGS with Importance-Guided MCMC Gaussian Allocation](https://arxiv.org/abs/2607.11285)**  
  *Tianyu Xiong, Rui Li, Suning Ge, Jiaqi Yang*  
  `2026-07-13` · `cs.CV` · [abs](https://arxiv.org/abs/2607.11285) · [pdf](https://arxiv.org/pdf/2607.11285.pdf)
  > 💡 提出统一SfM到3DGS流水线，用重要性引导MCMC高斯分配重新分配容量到欠拟合区域，实现快速高质量重建。

  <details><summary>Abstract</summary>

  Reconstructing 3D scenes from unordered images remains bottlenecked by expensive Structure-from-Motion (SfM) preprocessing and frozen pose interfaces. We present SalientGS, a unified SfM-to-3D Gaussian Splatting (3DGS) pipeline. Its central contribution is importance-guided Markov Chain Monte Carlo (MCMC) Gaussian allocation, which aggregates multi-view residuals into per-Gaussian underfit and redundancy signals. These signals define a smooth importance-weighted sampling distribution that biases both birth and relocation toward underfit regions. This reallocates capacity from well-fit areas without altering the underlying stochastic gradient Langevin dynamics (SGLD). SalientGS achieves end-to-end reconstruction in 15 minutes with state-of-the-art perceptual quality. The supplementary material provides dedicated sections for Per-Scene Qualitative Comparisons and Per-Image Learned Perceptual Image Patch Similarity (LPIPS) Analysis, including failure cases. Code and evaluation scripts are available at https://github.com/Six-Bit-TX/SalientGS.

  </details>

## 2026-07-04

- **[InvSplat: Inverse Feed-Forward Scene Splatting](https://arxiv.org/abs/2607.02301)**  
  *Polina Karpikova, Wenjing Bian, Haofei Xu, Hendrik Lensch, Andreas Geiger*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.02301) · [pdf](https://arxiv.org/pdf/2607.02301.pdf)
  > 💡 逆渲染中，前馈预测带材质属性的3D高斯表示，联合估计几何与反射率，提升多视图一致性和重光照性能。

  <details><summary>Abstract</summary>

  Inverse rendering aims to recover both 3D geometry and physically meaningful material properties from images, enabling applications such as relighting and novel view synthesis. Optimization-based methods achieve high fidelity but require costly per-scene fitting, while image-space learning-based approaches often suffer from multi-view inconsistencies and lack an explicit 3D representation for stable novel view rendering. We present a feed-forward multi-view reconstruction framework for inverse rendering that directly predicts a structured 3D Gaussian representation with intrinsic material attributes. Each Gaussian primitive is parameterized by mean, normal, opacity, rotation, scale, albedo, metallic, and roughness, enabling a disentangled and physically grounded scene representation. Our model integrates priors from a material estimation network with a multi-view 3D reconstruction backbone, allowing joint prediction of geometry and reflectance parameters in a single forward pass. Experiments on synthetic and real-world datasets demonstrate improved multi-view consistency compared to 2D baselines, accurate material recovery, and stable novel view rendering. Our representation further supports physically-based relighting and more faithful modeling of view-dependent effects compared to existing RGB-based feed-forward reconstruction methods. Our project webpage is: $\href{https://poliik.github.io/invsplat/}{\text{https://poliik.github.io/invsplat/}}$.

  </details>

## 2026-06-30

- **[AEGIR: Modeling Area Emitters for Indoor Inverse Rendering using Gaussian Splatting](https://arxiv.org/abs/2606.28635)**  
  *Mohamed Shawky Sabae, Philipp Langsteiner, Jan-Niklas Dihlmann, Hendrik Lensch*  
  `2026-06-26` · `cs.CV` · [abs](https://arxiv.org/abs/2606.28635) · [pdf](https://arxiv.org/pdf/2606.28635.pdf)
  > 💡 通过显式建模局部面光源与可微延迟渲染，实现室内场景的精确光照分解和光传输模拟。

  <details><summary>Abstract</summary>

  Inverse rendering requires separating illumination from surface materials, which is highly ambiguous due to their tight coupling in observed images. While Gaussian Splatting is efficient for novel view synthesis, existing relightable methods approximate scene lighting using discrete point lights, global environment maps, or implicit representations. By ignoring the physical spatial extent of real-world emitters, these approaches produce incorrect light attenuation and unrealistic shadows. We present AEGIR (Area Emitters for Gaussian Inverse Rendering), a framework that explicitly models local area emitters within a relightable Gaussian Splatting representation. Joint optimization of emitters, materials, and geometry is challenging due to flexible emitter parameterization, which increases both the number of parameters and the ambiguity between illumination and materials. We address this by introducing a differentiable deferred rendering pipeline that integrates multiple importance sampling with targeted regularization. As a result, AEGIR accurately simulates local light transport and achieves more consistent decomposition. Experiments show that explicit area emitters improve illumination reconstruction and enhance downstream tasks, including novel view synthesis, controlled relighting, and virtual object insertion, particularly in scenes with complex local lighting.

  </details>

## 2026-06-19

- **[Building Drift: Documenting On-Site Construction Adaptations Across Material Lifecycles](https://arxiv.org/abs/2606.19609)**  
  *Ritik Batra, Martin Tamke, Tom Svilans, Jan Hüls, Amritansh Kwatra, Steven J. Jackson, Thijs Roumen, Mette Ramsgaard Thomsen*  
  `2026-06-17` · `cs.HC` · [abs](https://arxiv.org/abs/2606.19609) · [pdf](https://arxiv.org/pdf/2606.19609.pdf)
  > 💡 提出建筑漂移概念和分类法，用Pentimento工具结合视频与3D高斯泼溅记录现场适应，促进回收材料循环利用。

  <details><summary>Abstract</summary>

  In a circular economy for construction, reclaimed materials carry prior lives of use and go on to have post-lives in future buildings. Yet working with such materials introduces unpredictability that requires on-site improvisation, making their reuse challenging to document and scale across building lifetimes. Without documentation, the on-site adaptations that make construction with reclaimed materials possible leave collaborators, evaluators, and inheritors without the information they need to continue, assess, and reuse materials. We call the collective deviation of the physical state from the digital model through these adaptations "building drift." Through a case study, ReShelter, a reclaimed timber pavilion constructed in the forest, we develop a taxonomy for building drift that characterizes the collective deviation across building lifetimes: Tending the Site, Foraging for Fit, Interpreting the Material, Marking Measurements, and Coordinating Across Communities. To put our taxonomy for building drift into practice, we present Pentimento, a documentation tool that leverages video documentation and 3D Gaussian Splatting to spatially, temporally, and semantically represent on-site adaptations in relation to the designed model. Pentimento enables each stakeholder to navigate material histories in ways that reduce barriers to material reuse. Together, these contributions open pathways towards computational tools that support the on-site improvisation essential to construction with reclaimed materials, enabling more sustainable cycles of recovery, repair, and reuse.

  </details>

## 2026-06-16

- **[Continuous Splatting meets Retinex: Continuous Gaussian Splatting and Implicit Reflectance Modeling for Low-Light Image Enhancement](https://arxiv.org/abs/2606.16159)**  
  *Yuhan Chen, Yicui Shi, Guofa Li, Wenxuan Yu, Ying Fang, Guangrui Bai, Wenbo Chu, Keqiang Li*  
  `2026-06-15` · `cs.CV` · [abs](https://arxiv.org/abs/2606.16159) · [pdf](https://arxiv.org/pdf/2606.16159.pdf)
  > 💡 提出CGS-Retinex，融合连续高斯溅

  <details><summary>Abstract</summary>

  Low-light image enhancement aims to recover clear images from low-illumination observations and is crucial for high-level downstream vision tasks. However, existing methods frequently encounter color distortion and structural artifacts when balancing global smooth illumination adjustment and local high-frequency detail recovery. To address these issues, we propose CGS-Retinex as the first low-light image enhancement framework based on explicit-implicit joint modeling. Our framework deeply integrates continuous Gaussian splatting with Retinex theory. Specifically, we represent the image grid as a continuous parameter field and propose a continuous Gaussian renderer to estimate the spatially continuous global illumination distribution. This approach fundamentally eliminates grid artifacts caused by discrete Gaussian sampling. Furthermore, we introduce an implicit neural representation to model reflectance independently. We leverage shallow high-frequency features to guide the network in accurately reconstructing degraded texture details. Within the Retinex framework, we incorporate physics-inspired brightness consistency constraints and illumination smoothness regularization to enable explicit illumination and implicit reflectance to maintain proper exposure and achieve high-fidelity recovery of high-frequency structures and colors. Extensive experiments demonstrate that CGS-Retinex significantly suppresses dark-region noise and overexposure while achieving exceptional high-frequency structural fidelity and color restoration by precisely decoupling illumination and texture. This work establishes a novel continuous physical representation paradigm for low-light image enhancement.

  </details>

## 2026-06-11

- **[Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Collection](https://arxiv.org/abs/2606.11894)**  
  *Yuto Furutani, Takashi Otonari, Kaede Shiohara, Toshihiko Yamasaki*  
  `2026-06-10` · `cs.CV` · [abs](https://arxiv.org/abs/2606.11894) · [pdf](https://arxiv.org/pdf/2606.11894.pdf)
  > 💡 针对前馈3DGS在复杂光照和瞬态物体场景中的困难，提出WildCity数据集及模型学习跨视角外观一致性并去除瞬态内容。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting (3DGS) removes the need for time-consuming per-scene optimization required by traditional 3DGS. However, existing feed-forward approaches struggle with real-world photo collections that include diverse lighting conditions and transient objects. In this paper, we present Wild3R, a feed-forward approach for unconstrained sparse photo collections. The main bottleneck is the lack of training data that provides multiple viewpoints, a variety of illuminations, and transient variations necessary for learning robust scene representations. To address this, we introduce the WildCity dataset, which comprises 200 scenes, 170 lighting conditions, and transient objects, resulting in 337,500 images in total. By leveraging the dataset, our model learns appearance consistency across viewpoints conditioned on reference views, while removing transient content. Extensive experiments demonstrate that our method outperforms existing feed-forward approaches and achieves results competitive with prior per-scene optimization-based methods.

  </details>

## 2026-05-30

- **[F-RNG: Feed-Forward Relightable Neural Gaussians](https://arxiv.org/abs/2605.25975)**  
  *Guangming Fu, Jiahui Fan, Jian Yang, Miloš Hašan, Beibei Wang*  
  `2026-05-25` · `cs.GR` · [abs](https://arxiv.org/abs/2605.25975) · [pdf](https://arxiv.org/pdf/2605.25975.pdf)
  > 💡 基于LRM和IDM，用潜插值几何合成与先验蒸馏，从稀疏视角高效生成可重照明的3D高斯资产。

  <details><summary>Abstract</summary>

  Capturing relightable 3D assets from real-world objects is a widely researched problem. Several per-scene optimization-based methods, based on 3D Gaussian splatting (3DGS), support relighting; however, they usually require dense input views, and their overfitting nature makes it difficult to generalize across scenes. Unlike per-scene optimization methods, generalized feed-forward models can directly reconstruct Gaussians from sparse input views. However, the resulting assets have baked-in illumination and cannot be easily used for relighting. In this paper, we present F-RNG, a feed-forward framework that directly generates relightable 3DGS assets from sparse-view inputs. Training such a model from scratch can require massive data and computing resources, and it is especially challenging to generate relightable assets in a feed-forward manner with acceptable cost. We develop F-RNG upon an existing large reconstruction model (LRM) to extract relightable representations, while also utilizing priors from an intrinsic decomposition model (IDM). Specifically, we first introduce a latent-interpolated fine-grained geometry synthesis to enhance the LRM's geometry representation. Second, we propose a prior-guided relightable appearance distillation to extract relightable neural representations by incorporating IDM priors. Finally, a universal neural renderer enables flexible and high-fidelity relighting. F-RNG requires neither re-training nor fine-tuning of the underlying LRMs, thus can automatically benefit from better LRMs and IDMs in the future. With only small networks that can be trained with affordable data and computational resources, F-RNG avoids the repetitive inference of large models under different light conditions. By comparison to the state-of-the-art LRM-based relighting method, F-RNG achieves ~25x faster relighting, as well as superior quality (~+2.0 dB).

  </details>

- **[FieryGS: In-the-Wild Fire Synthesis with Physics-Integrated Gaussian Splatting](https://arxiv.org/abs/2605.00177)**  
  *Qianfan Shen, Ningxiao Tao, Qiyu Dai, Tianle Chen, Minghan Qin, Yongjie Zhang, Mengyu Chu, Wenzheng Chen, Baoquan Chen*  
  `2026-04-30` · `cs.GR` · [abs](https://arxiv.org/abs/2605.00177) · [pdf](https://arxiv.org/pdf/2605.00177.pdf)
  > 💡 集成物理燃烧模拟与3DGS，结合大模型推理材料，实现无需手动调参的真实可控火焰合成。

  <details><summary>Abstract</summary>

  We consider the problem of synthesizing photorealistic, physically plausible combustion effects in in-the-wild 3D scenes. Traditional CFD and graphics pipelines can produce realistic fire effects but rely on handcrafted geometry, expert-tuned parameters, and labor-intensive workflows, limiting their scalability to the real world. Recent scene modeling advances like 3D Gaussian Splatting (3DGS) enable high-fidelity real-world scene reconstruction, yet lack physical grounding for combustion. To bridge this gap, we propose FieryGS, a physically-based framework that integrates physically-accurate and user-controllable combustion simulation and rendering within the 3DGS pipeline, enabling realistic fire synthesis for real scenes. Our approach tightly couples three key modules: (1) multimodal large-language-model-based physical material reasoning, (2) efficient volumetric combustion simulation, and (3) a unified renderer for fire and 3DGS. By unifying reconstruction, physical reasoning, simulation, and rendering, FieryGS removes manual tuning and automatically generates realistic, controllable fire dynamics consistent with scene geometry and materials. Our framework supports complex combustion phenomena -- including flame propagation, smoke dispersion, and surface carbonization -- with precise user control over fire intensity, airflow, ignition location and other combustion parameters. Evaluated on diverse indoor and outdoor scenes, FieryGS outperforms all comparative baselines in visual realism, physical fidelity, and controllability. Project page can be found at https://pku-vcl-geometry.github.io/FieryGS/.

  </details>

