# Compression / Compact / Efficient Storage

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---












## 2026-07-21

- **[QIRF Quantum-Inspired Non-Orthogonal Function-Space Compression for 3D Gaussian Splatting](https://arxiv.org/abs/2607.18067)**  
  *Shizeng Jiang, Hao Zhang, Xuerui Ma, Ying Hu, Tao Zhang*  
  `2026-07-20` · `cs.CV` · [abs](https://arxiv.org/abs/2607.18067) · [pdf](https://arxiv.org/pdf/2607.18067.pdf)
  > 💡 利用量子启发非正交函数压缩，通过重叠矩阵和密度矩阵选择子空间，减少高斯数量71.7%，提升渲染速度34.3%。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves high-quality real-time rendering by representing a scene with a large collection of anisotropic Gaussian primitives. However, complex scenes often require millions of Gaussians, resulting in substantial storage and rendering costs. Existing compression methods mainly reduce redundancy through primitive-wise pruning, attribute quantization, clustering, or neural coding, while redundancy caused by strongly overlapping and non-orthogonal Gaussian basis functions remains largely unexplored. We present QIRF, a quantum-inspired non-orthogonal function-space compression method for 3D Gaussian Splatting. QIRF models neighboring Gaussian primitives as a local non-orthogonal basis and formulates primitive reduction as a subspace-aware selection problem. Specifically, an analytic Gaussian overlap matrix and a radiance-response density matrix are constructed to characterize functional redundancy and rendering relevance. Generalized eigendecomposition is then used to identify the dominant local subspace and select representative Gaussian primitives. An RRDM-based response model and detail-aware safeguarding further preserve visually important high-frequency structures under aggressive pruning. Experiments on 13 scenes from Mip-NeRF 360, Tanks and Temples, and Deep Blending show that QIRF reduces the Gaussian count and raw PLY storage by 71.7 percent on average, corresponding to approximately 3.54 times compression, while maintaining reconstruction quality comparable to 3DGS and achieving a marginal average PSNR improvement of 0.10 dB. QIRF also improves the average rendering speed over 3DGS by 34.3 percent. These results suggest that non-orthogonal function-space redundancy is an important yet underexplored source of representational redundancy in explicit Gaussian radiance fields.

  </details>

- **[TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting](https://arxiv.org/abs/2607.16838)**  
  *Shanshan Pan, Jiale Chen, Yilin Liu, Hui Huang*  
  `2026-07-18` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16838) · [pdf](https://arxiv.org/pdf/2607.16838.pdf)
  > 💡 针对3DGS平面重建缺乏拓扑连接导致碎片化问题，TopoGS通过引入平面与拓扑约束及全局2D拓扑关系，生成连贯精准的3D场景。

  <details><summary>Abstract</summary>

  Extracting structured, parametric 3D representations from raw images remains a fundamental challenge in computer vision and graphics. While recent advancements in the 3D Gaussian Splatting (3DGS) pipeline integrate planar primitives to yield compact and editable geometry, these approaches typically treat planes as isolated, discrete sets. This lack of topological connectivity hinders robust geometric reasoning, leading to fragmented reconstructions and misaligned boundaries that fall short of the precision for rigorous spatial analysis and professional design workflows. To address this, we introduce TopoGS, the first 3DGS framework to explicitly integrate both planar and topological constraints for coherent 3D reconstruction. Specifically, we extract global 2D topological relationships from multi-view image segmentations and anchor Gaussian primitives to these structural elements. This formulation enables the joint optimization of plane parameters, rendering fidelity, and topological adjacency. By enforcing strict multi-view consistency alongside these topological constraints, our method significantly mitigates geometric misalignments and produces connected, structured 3D models. Extensive evaluations on the ScanNet++ dataset demonstrate that TopoGS achieves state-of-the-art performance, providing a highly robust solution for generating accurate, topologically sound, and visually faithful scene representations.

  </details>

- **[SPARE-GS: Structural Parsimony and Resource Efficiency for 3D Gaussian Splatting](https://arxiv.org/abs/2607.16624)**  
  *Zhang Chen, Shuai Wan, Fuzheng Yang, Jiazhi Xia, Weiyao Lin, Junhui Hou*  
  `2026-07-18` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16624) · [pdf](https://arxiv.org/pdf/2607.16624.pdf)
  > 💡 针对3DGS原语过多问题，提出全局预算约束优化框架，动态调整原语分布，降低高斯数和训练时间并提升质量。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) achieves high-fidelity novel view synthesis in real-time; however its training efficiency and representation compactness are hindered by excessive primitive proliferation. To address this challenge, we formulate the structural evolution of 3DGS as a global budget-constrained optimization problem and derive an optimality condition, which requires the marginal utility of structural resources to be balanced across spatial regions under a finite primitive budget. Based on this formulation, we propose SPARE-GS, a general plug-and-play framework that dynamically aligns the distribution of 3D Gaussian primitives with regional representational demand. SPARE-GS estimates capacity-normalized regional demand, assigns adaptive target quotas, and uses regional budget deviations to coordinate densification, pruning and adaptive termination toward a more balanced structural allocation. Extensive experiments across standard, accelerated, and structure-enhanced 3DGS pipelines demonstrate that SPARE-GS reduces the Gaussian count and training time by an average of 30.38% and 23.81%, respectively, while improving the average PSNR. Moreover, the resulting compact representations reduce downstream processing time and improve the rate-distortion performance of diverse compression and pruning methods, demonstrating the broad applicability of global structural budget regulation.

  </details>

- **[SaaF: Scene-Specific Ambiguity-Aware 3D Language Fields towards Interactive Real-World Object Retrieval](https://arxiv.org/abs/2607.16309)**  
  *Yuga Yano, Daiju Kanaoka, Hakaru Tamukoh, Yasutomo Kawanishi*  
  `2026-07-14` · `cs.CV` · [abs](https://arxiv.org/abs/2607.16309) · [pdf](https://arxiv.org/pdf/2607.16309.pdf)
  > 💡 针对3D语言场特征压缩和查询歧义问题，提出度量学习构建判别性且模糊感知的统一特征空间，提升交互式物体检索准确率。

  <details><summary>Abstract</summary>

  We propose Scene-specific Ambiguity-aware 3D Language Fields (SaaF), a novel Gaussian Splatting-based 3D language field designed for interactive object retrieval in a given real-world scene. Interactive object retrieval using natural language is a crucial capability for service robots operating in complex real-world environments. While recent 3D language field methods for object retrieval establish associations between rendered pixels and autoencoder-compressed CLIP features, they suffer from two limitations: (1) reduced discriminability among similar objects due to feature compression, and (2) poor handling of ambiguous queries, often resulting in unstable or incorrect retrieval. To address these limitations, SaaF introduces a metric learning strategy to construct a unified feature space that is both instance-discriminative and ambiguity-aware. (i) To enhance instance-level visual discrimination, SaaF employs metric learning that pulls image features from multiple viewpoints of the same object closer together in the feature space. (ii) To establish ambiguity awareness, the model jointly trains on multiple text labels generated by the proposed method from each tracked object image sequence, including ambiguous descriptions, to learn the semantic relationships between ambiguous and specific features in a target scene. This feature space enables fine-grained visual understanding while allowing the system to estimate query ambiguity and interactively request clarification when needed. Experimental results demonstrate that SaaF not only improves retrieval accuracy over previous methods but also robustly detects and handles ambiguity in the user text queries under open-vocabulary settings.

  </details>

## 2026-07-17

- **[Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513)**  
  *Amir Said, Randall Rauwendaal*  
  `2026-07-16` · `cs.CV` · [abs](https://arxiv.org/abs/2607.14513) · [pdf](https://arxiv.org/pdf/2607.14513.pdf)
  > 💡 针对3DGS球谐系数数据量大问题，采用GPU并行纹理压缩编码，实现高效压缩与低视觉损失。

  <details><summary>Abstract</summary>

  Techniques for modeling 3D scenes from image collections, such as 3D Gaussian Splatting (3DGS), are capable of generating high-quality novel views by leveraging graphics primitives with view-dependent appearance. In 3DGS, spherical harmonic (SH) are employed to model view-dependent color, resulting in a large number of SH coefficients per primitive and large memory requirements. While compression approaches have been proposed to mitigate this problem, they do not exploit the capabilities of modern Graphics Processing Units (GPUs) for parallel decoding and rendering. In this paper, we propose a method for compressing SH color coefficients using texture compression schemes specifically designed for efficient parallel GPU decoding and supported by dedicated hardware acceleration. It is shown that those methods can compress color coefficients more effectively than 2D textures by exploiting the fact that primitives can be locally grouped and reordered according to color. Furthermore, we introduce a bit-rate control strategy that preserves random access, enabling large-scale parallelization without compromising rendering performance. Experimental results using BC1 and BC7 texture compression formats show that GPU-based decompression can be achieved with negligible or imperceptible degradation in the visual quality of rendered 3DGS scenes.

  </details>

## 2026-07-16

- **[Bake It Till You Make It: Ultrafast Spatial Texture-Atlas Splatting](https://arxiv.org/abs/2607.13808)**  
  *Neel Kelkar, Simon Niedermayr, Kaloian Petkov, Klaus Engel, Rüdiger Westermann*  
  `2026-07-15` · `cs.CV` · [abs](https://arxiv.org/abs/2607.13808) · [pdf](https://arxiv.org/pdf/2607.13808.pdf)
  > 💡 针对3DGS外观参数化开销大，提出解耦辐射表示结合空间hash网格烘焙纹理贴图，实现5倍加速的实时4K渲染。

  <details><summary>Abstract</summary>

  Recent extensions of 3D Gaussian Splatting (3DGS) capture fine color details using hash-grid-based appearance parameterization but incur high computational cost during fragment rendering. We introduce a decoupled radiance representation that models low-frequency geometry and view dependent appearance features with 2D surfels while representing high-frequency textures via a view-independent spatial hash grid that is baked into a compact texture atlas. By including sparsity-enhancing optimizations that penalize semi-transparency and per-primitive falloff, our method aggressively prunes insignificant surfels and achieves significantly faster and sparser reconstructions than prior work. Exploiting geometric sparsity and efficient GPU texture mapping, our approach achieves up to a fivefold speedup over 3DGS while preserving state-of-the-art visual fidelity, enabling real-time 4K rendering at 60 FPS on consumer hardware.

  </details>

## 2026-07-15

- **[SpeedyGS: Content-Aware 3D Gaussian Splatting Compression via Two-Stage Optimization](https://arxiv.org/abs/2607.12656)**  
  *Junteng Zhang, Tong Chen, Yuxin Zhao, Yibo Shi, Jing Wang, Zhan Ma*  
  `2026-07-14` · `eess.SP` · [abs](https://arxiv.org/abs/2607.12656) · [pdf](https://arxiv.org/pdf/2607.12656.pdf)
  > 💡 针对3DGS解码慢问题，提出内容感知两阶段优化，联合自适应量化剪枝与率代理，结合稀疏八叉树令牌和局部自回归熵编码，实现160倍压缩及9倍优化加速。

  <details><summary>Abstract</summary>

  Recent progress in compressing large-scale 3D Gaussian Splatting (3DGS) data has substantially reduced storage footprint, network transmission bandwidth, and memory traffic to GPU caches before rendering. Yet decoding with advanced 3DGS codecs still takes seconds, making them unsuitable for interactive applications. To systematically address this challenge, we propose SpeedyGS, a Content-Aware 3DGS Compressor that separately optimizes the structural formation and statistical coding. First, in structural formation, we jointly optimize adaptive quantization and pruning under a unified rate-distortion objective, where the rate term is replaced by a lightweight rate proxy that estimates entropy coding cost of the next stage, thereby efficiently regulating Gaussian density and precision to yield a compact scene representation. Then, in the statistical coding phase, Gaussian geometry is converted into sparse octree tokens and subsequently undergoes multi-stage coding, while Gaussian attributes are serialized into a 1D token stream for entropy coding via a complexity-controllable local autoregressive model. SpeedyGS achieves a favorable balance among optimization efficiency, compression performance, decoding latency, and rendering speed. Compared to vanilla 3DGS, SpeedyGS achieves up to 160$\times$ model size reduction with negligible quality degradation across common datasets. Compared to state-of-the-art compression methods, it also offers significantly faster decoding and accelerates optimization by 9$\times$ on consumer-grade hardware. To further reduce decoding overhead, the statistical coding stage also supports channel-wise, fixed-length coding for Gaussian as a simpler alternative, enabling SpeedyGS to better adapt to the underlying application and reduce decoding latency to nearly zero.

  </details>

## 2026-07-14

- **[CoSAG: Compact Semantic Anchor Gaussians via Training-Free Rate-Distortion Coding](https://arxiv.org/abs/2607.10237)**  
  *Yuang Jia, Jinlong Wang, Junhong Lin, Ruiting Dai, Wei Gao*  
  `2026-07-11` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10237) · [pdf](https://arxiv.org/pdf/2607.10237.pdf)
  > 💡 通过空间锚点与无训练率失真编码压缩开放词汇3D高斯场，存储减少37-76倍且精度更优

  <details><summary>Abstract</summary>

  Open-vocabulary 3D scene understanding is commonly achieved by embedding 2D vision-language features such as CLIP into a 3D Gaussian Splatting scene, turning it into a text-queryable semantic field. However, attaching a high-dimensional feature to each of millions of Gaussians inflates a single scene to gigabytes, which makes storage and deployment the real bottleneck of these fields. Existing compact methods each learn and ship a per-scene codec, an autoencoder, a quantized codebook, or a distilled feature field, entangling field construction with field storage and never compressing the per-Gaussian assignment that holds the bulk of the cost. We argue that construction and storage should be decoupled, and that storage is a rate-distortion problem over the per-Gaussian binding to a small anchor table, a structure no prior open-vocabulary method compresses. We present CoSAG, which constructs the field without any per-scene training through a closed-form transmittance-weighted lift, spatially grounded semantic anchors, and multi-view denoising, and stores it with a spatially predictive entropy coder that ships no decoder. Because the anchors are spatially grounded, the binding is predictable and therefore highly compressible. The transmittance-weighted lift and multi-view denoising yield a clean, view-consistent assignment, so the entropy coder spends almost no rate on correcting noise and instead codes only the residual against its spatial prediction. CoSAG reaches sub-megabyte storage while matching or exceeding the state of the art across the 2D-rendered, 3D-selection, and dense-LSeg protocols, reducing field size by 37 to 76x relative to LangSplatV2 at higher accuracy.

  </details>

## 2026-07-07

- **[Real-Time LiDAR Gaussian Splatting SLAM](https://arxiv.org/abs/2607.04127)**  
  *Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu*  
  `2026-07-05` · `cs.CV` · [abs](https://arxiv.org/abs/2607.04127) · [pdf](https://arxiv.org/pdf/2607.04127.pdf)
  > 💡 将G-ICP配准与球形光栅化高斯建图紧耦合，利用LiDAR几何先验优化地图并实时反馈提升跟踪鲁棒性，实现86.78% F-score的实时SLAM。

  <details><summary>Abstract</summary>

  We present a real-time LiDAR-based framework for Gaussian Splatting SLAM that tightly couples fast G-ICP registration with spherical rasterization-based dense mapping for large-scale sequences. Leveraging LiDAR geometry rather than appearance, we reuse tracking-estimated local covariances to initialize Gaussians with range-aware scales and to derive surface normals for geometry-aware map optimization. We further introduce a covariance-derived geometry score that measures local complexity and drives pruning in planar regions and selective densification in structurally rich areas, while optimized Gaussians and LiDAR-specific confidence cues are fed back to improve tracking robustness. On the Newer College dataset, our method achieves an F-score of 86.78\% using purely online trajectories at real-time speed ($>$20 FPS), and additional experiments on other datasets confirm its stability and scalability.

  </details>

- **[Provable Pruning for Efficient 3D Gaussian Splatting via Coresets](https://arxiv.org/abs/2607.02721)**  
  *Waseem Mousa, Alaa Maalouf*  
  `2026-07-02` · `cs.CV` · [abs](https://arxiv.org/abs/2607.02721) · [pdf](https://arxiv.org/pdf/2607.02721.pdf)
  > 💡 通过敏感性加权子集实现对3DGS的可证明剪枝，在激进压缩下达到SOTA且无需或极少微调。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) enables high-quality real-time novel-view synthesis, but practical scenes often contain millions of Gaussians, making compression essential for deployment on limited hardware. Existing reduction methods are effective but mostly heuristic: they provide no multiplicative approximation guarantee for the rendered objective, and thus rely heavily on costly post-pruning finetuning to recover quality. We ask a basic question: can a 3DGS scene be provably replaced by a much smaller weighted subset (coreset) while preserving the objective of interest? We first show that, in the unrestricted setting, no non-trivial multiplicative 3DGS coreset exists. We then show that multiplicative guarantees are not impossible, but resolution-dependent. For a prescribed rendering resolution, such as representative views or grids of views/rays, we provide the first weighted coreset construction theorem for 3DGS. The construction samples Gaussians by sensitivity: provable importance scores measuring each Gaussian's role in the full-scene objective. Finally, under explicit validity and log-transmittance stability assumptions, we turn this objective guarantee into a rendering guarantee. Empirically, our method is strongest where deployment needs it most: aggressive compression with no or minimal recovery compute. In prune-only and very short finetuning regimes, it achieves state-of-the-art performance, showing that principled importance estimation can be both theoretically meaningful and practically useful. Open-source code is available at https://github.com/waseem-m/3dgs_provable_coresets.

  </details>

## 2026-07-02

- **[Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164)**  
  *Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben, Steve Petruzza, Qi Wu, Will Usher, Sidharth Kumar*  
  `2026-07-01` · `cs.LG` · [abs](https://arxiv.org/abs/2607.01164) · [pdf](https://arxiv.org/pdf/2607.01164.pdf)
  > 💡 针对隐式表示非结构体积需存网格限制压缩的问题，提出基于3D高斯的显式标量场表示，消除网格需求，压缩率更高且性能全面领先。

  <details><summary>Abstract</summary>

  Recent work has shown that implicit neural representations (INRs) can be trained to effectively compress structured and unstructured volume data, allowing for direct data querying with a reduced memory footprint. However, as existing INRs for unstructured volumes do not encode geometry, they require partial mesh storage for later sampling, limiting achievable compression. At the same time, novel view synthesis methods have shown that explicit collections of 3D Gaussians can be used to accurately visualize volume data. In this work, we introduce an explicit model for volume data compression based on 3D Gaussian primitives. We reinterpret collections of 3D Gaussians as an explicit representation of a scalar field and use a sampling strategy that reconstructs scalar values at spatial locations through weighted aggregation of intersecting Gaussians. We develop optimized CUDA-accelerated pipelines for structured and unstructured model sampling, loss functions that encourage accurate domain encoding by our models, and a novel sampling-error based densification strategy. Our explicit formulation naturally encodes domain geometry, eliminating the need for mesh storage in unstructured volumes and introducing significantly higher compression opportunities. Compared to existing INRs, we demonstrate that our explicit model achieves competitive reconstruction quality with significant training speedups on structured volumes, while markedly outperforming in all metrics on unstructured volumes.

  </details>

## 2026-06-30

- **[Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436)**  
  *Sicheng Yu, Dongxu Shen, Beizhen Zhao, Guanzhi Ding, Hao Wang*  
  `2026-06-29` · `cs.CV` · [abs](https://arxiv.org/abs/2606.30436) · [pdf](https://arxiv.org/pdf/2606.30436.pdf)
  > 💡 通过运动自适应混合跟踪和生命周期管理高斯映射，解决千米级室外场景中单目3DGS SLAM的长期跟踪漂移和内存爆炸问题。

  <details><summary>Abstract</summary>

  Scaling monocular 3D Gaussian Splatting (3DGS) SLAM to kilometer-level outdoor environments poses two tightly coupled challenges: fragile long-term pose tracking and excessive memory overhead during large-scale mapping. In this paper, we propose KiloGS-SLAM, a highly efficient and robust monocular 3DGS-SLAM system that jointly addresses both bottlenecks. Since high-fidelity scene reconstruction fundamentally relies on drift-free camera poses, we first introduce a motion-adaptive hybrid tracking module. This module features a condition-triggered three-tier solving pipeline. It dynamically switches between Essential matrix and PnP models to handle geometric degeneracies. An on-demand foundation model can also be activated to rescue the trajectory from catastrophic drift. To ensure the system can sustain these long trajectories without memory exhaustion, we subsequently design a lifecycle-managed Gaussian mapping strategy. By integrating probabilistic initialization with chunk-based multi-view densification and pruning, this full-pipeline optimization effectively reduces primitive redundancy while preserving high-frequency details. Together, the robust tracking guarantees the geometric foundation required for accurate mapping, while the memory-efficient lifecycle-managed mapping enables large-scale operation. Extensive experiments across three challenging outdoor datasets demonstrate that our approach achieves state-of-the-art tracking accuracy and rendering quality, successfully scaling to sequences of over 10,000 frames on a single GPU.

  </details>

## 2026-06-24

- **[Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM](https://arxiv.org/abs/2606.24796)**  
  *Leshu Li, Jie Peng, Yang Zhao*  
  `2026-06-23` · `cs.CV` · [abs](https://arxiv.org/abs/2606.24796) · [pdf](https://arxiv.org/pdf/2606.24796.pdf)
  > 💡 3DGS-SLAM内存持续增长，提出渲染面积感知剪枝策略，减少60%内存并提升2倍速度。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views. For SLAM in large-scale scenes, such as autonomous driving, 3DGS-SLAM faces a critical limitation: memory consumption increases continuously over time as Gaussian points accumulate, leading to poor memory efficiency and limiting its applicability. In this work, we propose a rendering-area-aware pruning strategy that selectively removes Gaussians based on their contribution to the effective rendering area, rather than solely relying on Gaussian-level heuristics such as opacity or gradient magnitude. This perspective directly targets the sources of memory redundancy, effectively reducing the peak memory footprint of 3DGS-SLAM during runtime. Evaluations on the EuRoC and KITTI datasets demonstrate that our method consistently outperforms existing pruning approaches in large-scale outdoor scenes, achieving over 60% memory reduction and more than 2 times FPS improvement while preserving localization and mapping accuracy. These results highlight rendering-area-aware pruning as a promising direction for scaling 3DGS-SLAM to real-world autonomous driving scenarios. Our code is publicly available at https://github.com/UMN-ZhaoLab/Pocket-SLAM.git.

  </details>

## 2026-06-09

- **[Path-Traced Inverse Rendering with Global Illumination in 3D Gaussian Fields](https://arxiv.org/abs/2606.09606)**  
  *Junke Zhu, Hao Zhang, Yutian Zhu, Ang Li, Chenxiao Hu, Meng Gai, Fei Zhu, Zhangjin Huang, Sheng Li*  
  `2026-06-08` · `cs.GR` · [abs](https://arxiv.org/abs/2606.09606) · [pdf](https://arxiv.org/pdf/2606.09606.pdf)
  > 💡 现有逆渲染因管线不匹配忽略间接光照，提出无splatting的路径追踪框架，用路径空间等价模型统一前后向传播，实现全局光照下材质优化与高质量渲染。

  <details><summary>Abstract</summary>

  Ray tracing enables 3D Gaussian fields to serve as a representation for physically based light transport. Faithful inverse rendering requires forward rendering and backward optimization to be defined within a consistent light-transport pipeline. Existing inverse rendering methods estimate G-buffers via splatting and optimize materials in screen space, tying the recovered properties to a rasterization-based pipeline. This pipeline mismatch, together with simplified rendering equations that neglect indirect illumination, often leads to inconsistent shading, visible artifacts, and inaccurate material-lighting estimation under path-traced rendering. Therefore, we propose a splatting-free path-traced inverse rendering framework for 3D Gaussian fields, where forward light transport and backward gradient propagation are defined within a unified ray-tracing pipeline. Our key idea is to define a path-space equivalent interaction model for overlapping Gaussian primitives, under which Monte-Carlo-based path tracing is unbiased for the induced light-transport integral, while pathwise gradients are replayed over the same ray-traced interactions rather than splatting-derived screen-space buffers. The framework optimizes materials and a compact Spherical-Gaussian environment under the full rendering equation with ray-traced visibility and multi-bounce light transport. Extensive experiments demonstrate competitive material inversion and improved path-traced rendering quality, producing more plausible shadows, reflections, and relighting results under global illumination.

  </details>

## 2026-06-06

- **[ZipSplat: Fewer Gaussians, Better Splats](https://arxiv.org/abs/2606.05102)**  
  *Alexander Veicht, Sunghwan Hong, Dániel Baráth, Marc Pollefeys*  
  `2026-06-03` · `cs.CV` · [abs](https://arxiv.org/abs/2606.05102) · [pdf](https://arxiv.org/pdf/2606.05102.pdf)
  > 💡 用聚类压缩视觉token为场景token，解耦高斯放置与像素网格，实现更少高斯更优质量，无需真值位姿。

  <details><summary>Abstract</summary>

  Feed-forward 3D Gaussian Splatting methods reconstruct a scene from posed or pose-free images in a single forward pass, yet current approaches predict one Gaussian per input pixel, tying the representation budget to camera resolution rather than scene complexity. A flat wall and a richly textured object thus produce equally many Gaussians despite very different geometric needs. We propose ZipSplat, a token-based feed-forward model that decouples Gaussian placement from the pixel grid. A multi-view backbone extracts dense visual tokens, and k-means clustering compresses them into a compact set of scene tokens. Cross- and self-attention refine these tokens, and a lightweight MLP decodes each into a group of Gaussians with unconstrained 3D positions. Because clustering is applied at inference, a single trained model spans the quality-efficiency curve without retraining. ZipSplat operates without ground-truth poses or intrinsics, yet sets a new state of the art on DL3DV and RealEstate10K with ${\sim}6{\times}$ fewer Gaussians than pixel-aligned methods, surpassing the best pose-free baseline by 2.1dB and 1.2dB PSNR, respectively. It further generalizes zero-shot to Mip-NeRF360 and ScanNet++, outperforming all comparable baselines. Our project page is at ${\href{https://veichta.com/zipsplat}{https://veichta.com/zipsplat}}$.

  </details>

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

