# Medical / Surgical

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---


## 2026-06-23

- **[Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525)**  
  *Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang*  
  `2026-06-21` · `cs.CV` · [abs](https://arxiv.org/abs/2606.22525) · [pdf](https://arxiv.org/pdf/2606.22525.pdf)
  > 💡 稀疏视角CT中投影优化误导体积退化，提出LADES以退火丢弃和早停抑制退化并提升体积保真度。

  <details><summary>Abstract</summary>

  Sparse-view computed tomography is a severely ill-posed inverse problem, where recent 3D Gaussian Splatting methods offer an efficient explicit representation for tomographic reconstruction. However, we find that projection-domain optimization can be misleading in this setting: the rendered projections may continue to improve while the reconstructed volume deteriorates. We identify this failure mode as Projection-Volume Fidelity Divergence (PVFD), a representation-level optimization drift caused by anisotropic Gaussian deformation and view-specific primitive co-adaptation under sparse Radon constraints. To characterize this behavior, we introduce geometry- and volume-level diagnostics that measure needle-like Gaussian degeneration and the stability of the voxelized density field. Based on these observations, we propose LADES, a ground-truth-free optimization controller for sparse-view Gaussian tomography. LADES combines Linearly Annealed Dropout, which applies strong stochastic masking in early training to disrupt premature primitive co-adaptation and gradually restores full capacity for structural consolidation, with Structure-Aware Early Stopping, which terminates densification according to the saturation of Gaussian population growth rather than validation PSNR. Experiments on sparse-view CT reconstruction show that LADES improves volumetric fidelity, suppresses structural degeneration, and substantially reduces training time while maintaining competitive projection accuracy. These results suggest that robust Gaussian-based tomography requires monitoring and controlling volumetric structure, rather than optimizing projection fit alone.

  </details>

## 2026-05-30

- **[Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction](https://arxiv.org/abs/2604.27552)**  
  *Jian Lin, Jiancheng Fang, Shaoyu Wang, Changan Lai, Yikun Zhang, Yang Chen, Qiegen Liu*  
  `2026-04-30` · `cs.CV` · [abs](https://arxiv.org/abs/2604.27552) · [pdf](https://arxiv.org/pdf/2604.27552.pdf)
  > 💡 针对超稀疏视角CBCT中3DGS高频细节丢失问题，提出融合小波变换的

  <details><summary>Abstract</summary>

  While 3D Gaussian splatting (3DGS) offers explicit and efficient scene representations for cone-beam computed tomography reconstruction, conventional photometric optimization inherently suffers from spectral bias under ultra sparse-view conditions, leading to over-smoothing and a loss of high-frequency anatomical details. Since wavelet transforms provide rich high-frequency information and have been widely utilized to enhance sparse reconstruction, this work integrates wavelet multi-resolution analysis with 3DGS. To circumvent the mathematical mismatch between the strict non-negativity of physical X-ray attenuation and the bipolar nature of high-frequency wavelet coefficients, we propose Residual Gaussian Splatting (RGS). Methodologically, we introduce a spectrally-decoupled Gaussian representation that stratifies the volumetric field into a geometric base component and a residual detail component. This decomposition systematically transforms explicit high-frequency fitting into a physically consistent, implicit residual compensation task. Furthermore, we devise a spectral-spatial collaborative optimization strategy to coordinate the interplay between geometric anchoring and texture refinement, effectively preventing spectral crosstalk. Extensive experiments on clinical datasets demonstrate that RGS enables the reconstructed images to capture highly refined geometric textures. It successfully resolves the trade-off between artifact suppression and detail preservation, yielding superior visual fidelity in complex trabecular and vascular structures compared to existing neural rendering baselines.

  </details>

- **[Multivariate Gaussian NeRF for Wide Field-of-View Ultrasound Reconstruction](https://arxiv.org/abs/2604.24187)**  
  *Patris Valera, Magdalena Wysocki, Felix Duelmer, Mohammad Farid Azampour, Sebastian Herz, Stefan Wörz, Nassir Navab*  
  `2026-04-27` · `cs.CV` · [abs](https://arxiv.org/abs/2604.24187) · [pdf](https://arxiv.org/pdf/2604.24187.pdf)
  > 💡 针对凸探头超声宽视野重建的伪影和混叠，采用多元高斯NeRF建模光束几何与各向异性高斯，实现抗混叠连续神经表示及高质量新视角合成。

  <details><summary>Abstract</summary>

  Wide Field-of-View (WFoV) reconstruction enhances 3D ultrasound imaging by providing valuable anatomical context for segmentation models and visualization. Clinical ultrasound volumes are predominantly acquired using convex probes, which generate expanding, diverging acoustic beams to maximize anatomical coverage. Stitching these sweeps together traditionally introduces significant compounding artifacts and aliasing due to depth-dependent resolution changes. Here, we introduce Ultra-Wide-NeRF, a Multivariate 3D Gaussian (MVG) NeRF-based method for WFoV ultrasound reconstruction. By explicitly modeling the complex beam geometry using distance-dependent convex volumetric sampling and anisotropic 3D Gaussians, our method inherently mitigates these compounding artifacts and provides anti-aliasing. Beyond simply reconstructing a static 3D grid, our NeRF-based approach yields a continuous neural representation of the tissue, enabling the synthesis of high-fidelity novel views from arbitrary virtual trajectories. We validate Ultra-Wide-NeRF for intracardiac echocardiography on phantom and porcine datasets, demonstrating that our method expands the spatial context important in intraoperative navigation. Code will be open-sourced upon publication.

  </details>

