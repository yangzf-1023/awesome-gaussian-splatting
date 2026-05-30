# Relighting / Material / BRDF

All Gaussian-Splatting papers in this topic, auto-collected from arXiv. Newest first.

[← Back to main index](../README.md)

---

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

