# Others

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---



## 2026-07-14

- **[DP-Splat: Bayesian Nonparametric Complexity Control for Gaussian Splatting](https://arxiv.org/abs/2607.10912)**  
  *Aqi Dong*  
  `2026-07-12` · `cs.CV` · [abs](https://arxiv.org/abs/2607.10912) · [pdf](https://arxiv.org/pdf/2607.10912.pdf)
  > 💡 用截断棍棒狄利克雷过程替代固定混合权重，实现高斯溅射组件数量自适应，理论保证单调性和截断误差，性能匹配且组件减少5.9-7.6倍。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting represents scenes as finite mixtures of anisotropic Gaussians whose number of components $K$ is set by heuristic density control or user caps. Variational Bayes Gaussian Splatting (VBGS) recast splat fitting as conjugate variational inference, but $K$ remains fixed. We replace the finite symmetric Dirichlet over mixture weights with a truncated stick-breaking Dirichlet-process prior -- and, as a theory-backed alternative, a sparse overfitted finite Dirichlet -- so that the number of occupied components adapts to the data while every update remains a closed-form coordinate-ascent step; a natural-gradient stochastic variant makes the per-step cost independent of the number of points. We give an exact monotonicity guarantee, a rigorous truncation-error bound correcting an anti-conservative large-$α$ approximation in common use, and an honest account of what the fitted number of components estimates. Empirically: (i) the effective complexity $\hat{K}$ adapts to scene complexity and recovers the true $K$ within $\pm 1$ on well-separated synthetic data with regime-appropriate concentration; (ii) a deconfounded comparison shows the DP prior's contribution is complexity selection, not per-component efficiency -- converged DP fits exceed single-pass fixed-$K$ VBGS by +2.7 dB at matched budgets yet tie an equally converged fixed-$K$ baseline, and on 3D scenes DP-Splat matches or exceeds VBGS's held-out color prediction with 5.9-7.6x fewer components; (iii) the posterior-predictive color variance is well calibrated on model-matched synthetic data; and (iv) the ordering suggested by exact-posterior asymptotics reverses under mean-field coordinate ascent: the DP prior resists over-splitting while the sparse finite mixture saturates its truncation, a gap between variational practice and posterior asymptotics documented across three orders of magnitude in $N$.

  </details>

## 2026-06-18

- **[Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement](https://arxiv.org/abs/2606.17985)**  
  *Yuhan Chen, Wenxuan Yu, Guofa Li, Fuchen Li, Kunyang Huang, Yicui Shi, Ying Fang, Wenbo Chu, Keqiang Li*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17985) · [pdf](https://arxiv.org/pdf/2606.17985.pdf)
  > 💡 针对非均匀光照下曝光失衡与色偏问题，提出高斯光场散射驱动的视觉Transformer，用各向异性高斯基嵌入物理先验，实现SOTA无监督

  <details><summary>Abstract</summary>

  Existing unsupervised low-light image enhancement methods often encounter local exposure imbalance and color distortion under complex non-uniform illumination. In addition, most Vision Transformers lack an explicit mechanism for modeling the physical priors of illumination degradation. To address these limitations, we propose GLFS, a Gaussian light field splatting-based Vision Transformer that integrates continuous physical illumination modeling from Gaussian splatting into the Transformer architecture. In GLFS, scene illumination is represented by a superposition of anisotropic Gaussian basis functions. Physics-guided biases are introduced into self-attention to adaptively infer a spatial gain field, enabling accurate and uniform restoration under complex illumination. To reduce color bias and structural degradation during enhancement, a color-vector angular loss and a luminance-edge loss are further developed. These losses enforce hue consistency and improve the structural fidelity of local details. Extensive ablation studies and quantitative evaluations show that GLFS provides clear advantages in illumination correction and detail preservation. It achieves state-of-the-art performance and offers a new representation paradigm for low-light image enhancement.

  </details>

- **[GSPan: A Continuous Gaussian Primitive Representation for Arbitrary-Scale Pansharpening](https://arxiv.org/abs/2606.17722)**  
  *Fangyi Li, Xiaoyuan Yang, Yixiao Li, Zongyang Sui, Kangqing Shen, Gemine Vivone*  
  `2026-06-16` · `cs.CV` · [abs](https://arxiv.org/abs/2606.17722) · [pdf](https://arxiv.org/pdf/2606.17722.pdf)
  > 💡 提出用二维高斯溅射连续表示残差细节，结合双流层次交互与空间-光谱注意力，实现无需重训的任意尺度全色锐化并加速推理。

  <details><summary>Abstract</summary>

  Pansharpening aims to generate high-resolution multispectral (HRMS) images by fusing low-resolution multispectral (LRMS) and panchromatic (PAN) observations. Most existing deep learning methods treat pansharpening as fixed-grid prediction, which limits scale adaptation. To address this, we propose GSPan, a framework that introduces 2D Gaussian Splatting (GS) into pansharpening. Instead of directly predicting pixels, GSPan represents band-wise residual details as continuous and learnable 2D Gaussian primitives. We design a Dual-Stream Hierarchical Interaction (DSHI) architecture with a Spatial-Spectral Interactive Attention (SSIA) module to estimate these primitives from complementary PAN and MS observations. The predicted primitives are rendered as a residual detail field and injected into the upsampled MS image. This continuous representation allows GSPan to render fused images on arbitrary target sampling grids without scale-specific retraining. It further enables a Scale-Decoupled Asymmetric Inference (SDAI) strategy, which estimates primitives at a reduced resolution and renders the fused image at the target resolution for efficient large-scene pansharpening. Experiments on QuickBird, GaoFen-2, WorldView-3, and WorldView-3-4K datasets show that GSPan delivers state-of-the-art fusion performance. Moreover, SDAI markedly accelerates inference, achieving a favorable trade-off between computational efficiency and fusion quality. Our results demonstrate the potential of continuous Gaussian residual representations as a flexible and scale-decoupled alternative to fixed-grid prediction.

  </details>

## 2026-05-30

- **[OctCGS: Octree-Contextual Gaussian Splatting with Explicit Multi-Order Propagation Modeling for Channel Knowledge Map Construction](https://arxiv.org/abs/2605.22961)**  
  *Jinghan Zhang, Xitao Gong, Qi Wang, Richard A. Stirling-Gallacher, Giuseppe Caire*  
  `2026-05-21` · `eess.SP` · [abs](https://arxiv.org/abs/2605.22961) · [pdf](https://arxiv.org/pdf/2605.22961.pdf)
  > 💡 八叉树上下文高斯溅射联合建模多阶传播，实现信道知识图构建，降低误差达0.88 dB MAE。

  <details><summary>Abstract</summary>

  Channel knowledge maps (CKMs) learn the relation between transmitter (Tx) and receiver (Rx) positions and channel knowledge to support environment-aware wireless communications. Implicit neural methods can model continuous channel variation but often incur high training and inference cost, while existing Gaussian-splatting-based CKM methods improve efficiency yet still compress wireless multipath interactions into aggregated scattering representations. Consequently, explicit modeling of multi-bounce wireless propagation remains absent from CKM construction. We propose OctCGS, an octree-contextual Gaussian splatting framework that explicitly models the order of bounce jointly over Tx/Rx positions and carrier frequencies. OctCGS partitions the environment into a multi-resolution octree and anchors one Gaussian primitive to each leaf node. Rather than having each Gaussian independently encode all multi-path propagations, it models complex electromagnetic interactions among scatterers through tree attention over the octree hierarchy with controlled complexity. Experiments on simulated benchmarks show that OctCGS achieves a 2.99 dB channel-gain mean absolute error (MAE) and 0.065 channel gain normalized mean absolute error (NMAE), outperforming the strongest baseline by 0.88 dB MAE and 0.021 NMAE.

  </details>

- **[Conflict-Aware Active Perception and Control in 3D Gaussian Splatting Fields via Control Barrier Functions](https://arxiv.org/abs/2605.20566)**  
  *Amirhossein Mollaei Khass, Athanasios Cosse, Vivek Pandey, Nader Motee*  
  `2026-05-19` · `cs.RO` · [abs](https://arxiv.org/abs/2605.20566) · [pdf](https://arxiv.org/pdf/2605.20566.pdf)
  > 💡 在3DGS场中采用控制障碍函数与风险感知信息增益，通过二次规划平衡冲突的安全与感知目标，提升安全性和信息采集效率

  <details><summary>Abstract</summary>

  Active perception in uncertain environments requires robots to navigate safely while acquiring informative observations to reduce map uncertainty. These objectives inherently conflict, as informative viewpoints often lie near uncertain regions with higher collision risk. To address this challenge, we develop a conflict-aware active perception and control framework for robotic systems operating in environments represented by 3D Gaussian Splatting (3DGS). Safety is enforced using a Control Barrier Function (CBF) derived from an Average Value-at-Risk AV@R collision-risk metric that accounts for geometric uncertainty and guarantees forward invariance of a safe set. To improve perception, we propose a risk-aware Expected Information Gain (EIG) formulation for selecting the next-best-view and introduce perception barrier functions that align the camera orientation with the local information-ascent direction. To obtain a tractable formulation for these conflicting safety and perception objectives, we propose a unified safety-critical, perception-aware quadratic program that enforces safety as a hard constraint while relaxing perception constraints through slack variables. Simulation results demonstrate that the proposed method improves both safety and information acquisition compared to existing 3DGS-based approaches.

  </details>

- **[A Geometric Algebra-Informed 3DGS Framework for Wireless Channel Prediction](https://arxiv.org/abs/2605.19065)**  
  *Jingzhou Shen, Tianya Zhao, Xuyu Wang*  
  `2026-05-18` · `cs.NI` · [abs](https://arxiv.org/abs/2605.19065) · [pdf](https://arxiv.org/pdf/2605.19065.pdf)
  > 💡 采用几何代数注意力机制与3D高斯泼溅，显式建模射线-物体交互，实现高精度无线信道预测。

  <details><summary>Abstract</summary>

  In this paper, we introduce Geometric Algebra-Informed 3D Gaussian Splatting (GAI-GS), a framework for wireless modeling that couples 3D Gaussian splatting with a geometric algebra-based attention mechanism to explicitly model ray-object interactions in complex propagation environments. GAI-GS encodes joint spatial-electromagnetic (EM) relations into token representations, enabling scene-level aggregation within a unified, end-to-end neural architecture. This design grounds wireless ray propagation in electromagnetic principles, allowing token interactions to model key effects such as multipath, attenuation, and reflection/diffraction. Through extensive evaluations on multiple real-world indoor datasets, GAI-GS consistently surpasses current baselines across various wireless tasks.

  </details>

- **[ReorgGS: Equivalent Distribution Reorganization for 3D Gaussian Splatting](https://arxiv.org/abs/2605.08739)**  
  *Luchao Wang, Kaimin Liao, Qian Ren, Hua Wang, Zhi Chen, Yaohua Tang*  
  `2026-05-09` · `cs.CV` · [abs](https://arxiv.org/abs/2605.08739) · [pdf](https://arxiv.org/pdf/2605.08739.pdf)
  > 💡 针对3DGS参数化退化问题，通过等价分布重组重采样中心与协方差，改善梯度可访问性并抑制漂浮物，提升拟合质量。

  <details><summary>Abstract</summary>

  A converged 3D Gaussian Splatting (3DGS) model may approximate the target scene while remaining poorly parameterized for further optimization. We identify this failure mode as \emph{parameterization degeneration}: high-opacity floaters attenuate gradients to true surfaces through alpha compositing, and redundant overlapping clusters create strongly coupled parameter blocks with nearly collinear Jacobian responses. These effects explain why continued optimization can plateau even when the model still contains removable artifacts. We propose ReorgGS, an equivalent distribution reorganization method for converged 3DGS models. ReorgGS treats the existing Gaussian set as an empirical probability field, resamples centers from it, estimates local anisotropic covariances with kNN, initializes low opacity, and continues optimization with the original 3DGS renderer and loss. Unlike opacity reset, which only rescales opacity on the old overlap graph, ReorgGS rebuilds centers, covariances, and visibility structure, thereby changing the graph itself. Our analysis shows that distributional equivalence is not optimization equivalence. The reorganized model preserves scene support while improving gradient accessibility under alpha compositing and reducing opacity-weighted overlap, thereby weakening local parameter coupling during subsequent optimization. Under the same additional optimization budget, ReorgGS improves fitting quality at a fixed Gaussian count, suppresses persistent floaters, and reduces rendering overhead from redundant overlap.

  </details>

- **[VkSplat: High-Performance 3DGS Training in Vulkan Compute](https://arxiv.org/abs/2605.00219)**  
  *Jingxiang Chen, Mohamed Ibrahim, Yang Liu*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2605.00219) · [pdf](https://arxiv.org/pdf/2605.00219.pdf)
  > 💡 使用Vulkan计算管线优化3DGS训练，实现3.3倍加速和33%显存降低，并兼容多厂商GPU。

  <details><summary>Abstract</summary>

  We present VkSplat, a high-performance, cross-vendor 3D Gaussian Splatting (3DGS) training pipeline implemented fully in Vulkan compute, addressing performance and compatibility limitation of existing training pipelines. With various optimizations, we achieve $3.3\times$ speed and $33\%$ VRAM reduction over CUDA+PyTorch baseline, maintaining quality, and demonstrating compatibility across GPU vendors. To the best of our knowledge, this is the first fully-Vulkan-based 3DGS training pipeline that achieves state-of-the-art performance. Code: \href{https://github.com/harry7557558/vksplat}{https://github.com/harry7557558/vksplat}

  </details>

- **[GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds](https://arxiv.org/abs/2604.20155)**  
  *Ao Gao, Jingyu Gong, Xin Tan, Zhizhong Zhang, Lizhuang Ma, Yuan Xie*  
  `2026-04-22` · `cs.CV` · [abs](https://arxiv.org/abs/2604.20155) · [pdf](https://arxiv.org/pdf/2604.20155.pdf)
  > 💡 提出无蒸馏插件GSCompleter，以生成-注册替代修复-蒸馏，实现快速度量感知的3DGS补全，提升质量和效率。

  <details><summary>Abstract</summary>

  3D Gaussian Splatting (3DGS) has revolutionized high-fidelity neural rendering with its explicit representation and efficiency. However, reconstructing scenes from sparse viewpoints suffers from severe geometric voids and floaters due to limited coverage. Current scene completion methods typically rely on an iterative "Repair-then-Distill" paradigm, which is computationally intensive, prone to unstable optimization, and susceptible to overfitting. To address these limitations, we propose GSCompleter, a distillation-free plugin that shifts scene completion to a stable "Generate-then-Register" workflow. Specifically, GSCompleter synthesizes visually plausible 2D reference images and explicitly lifts them into 3D Gaussian primitives with a consistent metric scale via a robust Stereo-Anchor View Selection mechanism. These newly generated primitives are then seamlessly integrated into the global scene using a novel Ray-Constrained Registration strategy. By replacing unstable distillation with rapid geometric registration, GSCompleter exhibits superior 3DGS completion performance across three benchmarks, enhancing both quality and efficiency over various baselines and achieving new state-of-the-art (SOTA) results.

  </details>

- **[GeGS-PCR: Effective and Robust 3D Point Cloud Registration with Two-Stage Color-Enhanced Geometric-3DGS Fusion](https://arxiv.org/abs/2604.17721)**  
  *Jiayi Tian, Haiduo Huang, Tian Xia, Wenzhe Zhao, Pengju Ren*  
  `2026-04-20` · `cs.CV` · [abs](https://arxiv.org/abs/2604.17721) · [pdf](https://arxiv.org/pdf/2604.17721.pdf)
  > 💡 针对低重叠点云注册难题，融合几何、颜色

  <details><summary>Abstract</summary>

  We address the challenge of point cloud registration using color information, where traditional methods relying solely on geometric features often struggle in low-overlap and incomplete scenarios. To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration. Our approach incorporates a dedicated color encoder that enhances color features by extracting multi-level geometric and color data from the original point cloud. We introduce the \textbf{Ge}ometric-3D\textbf{GS} module, which encodes the local neighborhood information of colored superpoints to ensure a globally invariant geometric-color context. Leveraging LORA optimization, we maintain high performance while preserving the expressiveness of 3DGS. Additionally, fast differentiable rendering is utilized to refine the registration process, leading to improved convergence. To further enhance performance, we propose a joint photometric loss that exploits both geometric and color features. This enables strong performance in challenging conditions with extremely low point cloud overlap. We validate our method by colorizing the Kitti dataset as ColorKitti and testing on both Color3DMatch and Color3DLoMatch datasets. Our method achieves state-of-the-art performance with \textit{Registration Recall} at 99.9\%, \textit{Relative Rotation Error} as low as 0.013, and \textit{Relative Translation Error} as low as 0.024, improving precision by at least a factor of 2.

  </details>

