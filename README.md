# Awesome Gaussian Splatting

[![Daily arXiv Update](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml/badge.svg)](https://github.com/yangzf-1023/awesome-gaussian-splatting/actions/workflows/daily-update.yml)
![Last Updated](https://img.shields.io/badge/dynamic/json?label=Last%20Updated&query=%24.last_updated&url=https%3A%2F%2Fraw.githubusercontent.com%2Fyangzf-1023%2Fawesome-gaussian-splatting%2Fmain%2Fdata%2Fmeta.json)

A curated, **auto-updated** list of papers related to **Gaussian Splatting (3DGS / 4DGS / Dynamic GS / Streaming GS / GS Compression / ...)** on [arXiv](https://arxiv.org/).

> The crawler runs **every day at 01:30 UTC** via GitHub Actions, fetches the latest submissions from arXiv, filters by Gaussian-Splatting-related keywords, and appends new entries to this README.

---

## How it works

- **Source**: arXiv API (`http://export.arxiv.org/api/query`)
- **Scope**: categories `cs.CV`, `cs.GR`, `cs.LG`, `cs.AI`, `eess.IV`
- **Filter keywords**: `gaussian splatting`, `3dgs`, `4dgs`, `3d gaussian`, `4d gaussian`, `gaussian splat`
- **Dedup**: by arXiv ID, persisted in `data/seen.json`
- **Schedule**: daily at `01:30 UTC` (≈ 09:30 Beijing)
- You can also trigger it manually from the **Actions** tab.

## Repository structure

```
.
├── .github/workflows/daily-update.yml   # GitHub Actions schedule
├── scripts/fetch_arxiv.py               # arXiv crawler & README updater
├── data/seen.json                       # dedup cache
├── data/meta.json                       # last-updated timestamp
└── README.md                            # this file (auto-edited below the marker)
```

## Manual run (locally)

```bash
pip install -r requirements.txt
python scripts/fetch_arxiv.py
```

## Contributing

Found a missing paper? Open an issue or PR — manual entries above the auto-generated marker are preserved.

## License

[MIT](LICENSE)

---

<!-- AUTO-GENERATED-START -->

### 2026-05-29 (UTC) — 14 new paper(s)

- **[Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342)**  
  *Shangjie Xue, Jesse Dill, Dhruv Ahuja, Frank Dellaert, Panagiotis Tsiotras, Danfei Xu*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30342) · [pdf](https://arxiv.org/pdf/2605.30342.pdf)

- **[Supercharging Thermal Gaussian Splatting with Depth Estimation](https://arxiv.org/abs/2605.30328)**  
  *Manoj Biswanath, Chenxin Cai, Hannah Schieber, Daniel Roth, Benjamin Busam*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30328) · [pdf](https://arxiv.org/pdf/2605.30328.pdf)

- **[MonoPhysics: Estimating Geometry, Appearance, and Physical Parameters from Monocular Videos](https://arxiv.org/abs/2605.30320)**  
  *Daniel Rho, Jun Myeong Choi, Matthew Thornton, Biswadip Dey, Roni Sengupta*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30320) · [pdf](https://arxiv.org/pdf/2605.30320.pdf)

- **[City-Mesh3R: Simulation-Ready City-Scale 3D Mesh Reconstruction from Multi-View Images](https://arxiv.org/abs/2605.30310)**  
  *Sayan Paul, Sourav Ghosh, Siddharth Katageri, Soumyadip Maity, Sanjana Sinha, Brojeshwar Bhowmick*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30310) · [pdf](https://arxiv.org/pdf/2605.30310.pdf)

- **[PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions](https://arxiv.org/abs/2605.30268)**  
  *Omer Benishu, Gal Fiebelman, Sagie Benaim*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30268) · [pdf](https://arxiv.org/pdf/2605.30268.pdf)

- **[Boosting Zero-Shot 3D Style Transfer with 2D Pre-trained Priors](https://arxiv.org/abs/2605.30065)**  
  *Xin Dong, Yunzhi Teng, Wenfeng Deng, Yansong Tang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.30065) · [pdf](https://arxiv.org/pdf/2605.30065.pdf)

- **[FRUC: Feedforward Dynamic Scene Reconstruction from Uncalibrated Collaborative Driving Views](https://arxiv.org/abs/2605.29997)**  
  *Yihang Tao, Yu Guo, Zhengru Fang, Haonan An, Yuguang Fang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29997) · [pdf](https://arxiv.org/pdf/2605.29997.pdf)

- **[DVSM: Decoder-only View Synthesis Model Done Right](https://arxiv.org/abs/2605.29891)**  
  *Cheng Sun, Jaesung Choe, Min-Hung Chen, Ryo Hachiuma, Yu-Chiang Frank Wang*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29891) · [pdf](https://arxiv.org/pdf/2605.29891.pdf)

- **[DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](https://arxiv.org/abs/2605.29879)**  
  *Luzhou Ge, Xiangyu Zhu, Jinyan Liu, Xuesong Li*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29879) · [pdf](https://arxiv.org/pdf/2605.29879.pdf)

- **[BitC-3DGS: High-Capacity 3D Gaussian Splatting Watermarking via Bit Compression](https://arxiv.org/abs/2605.29583)**  
  *Yuquan Bi, Baosheng Yu, Yingke Lei, Jianwei Yang, Hongsong Wang, Jie Gui, Yuan Yan Tang, James Tin-Yau Kwok*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29583) · [pdf](https://arxiv.org/pdf/2605.29583.pdf)

- **[Learning Representations from 3D Gaussian Splats](https://arxiv.org/abs/2605.29549)**  
  *Julia Farganus, Krzysztof Żurawicki, Arkadiusz Gaweł, Weronika Jakubowska, Halina Kwaśnicka*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29549) · [pdf](https://arxiv.org/pdf/2605.29549.pdf)

- **[Comparative evaluation of photogrammetric reconstruction methods and 3D Gaussian Splatting for road surface roughness analysis](https://arxiv.org/abs/2605.29452)**  
  *Marouane Elmegdar, Teng Xiao*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29452) · [pdf](https://arxiv.org/pdf/2605.29452.pdf)

- **[FreeForm: Reduced-Order Deformable Simulation from Particle-Based Skinning Eigenmodes](https://arxiv.org/abs/2605.29318)**  
  *Donglai Xiang, Vismay Modi, Rishit Dagli, Ty Trusty, Gilles Daviet, Anka He Chen, Nicholas Sharp, David I. W. Levin*  
  `2026-05-28` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29318) · [pdf](https://arxiv.org/pdf/2605.29318.pdf)

- **[Eulerian Gaussian Splatting using Hashed Probability Pyramids](https://arxiv.org/abs/2605.29136)**  
  *Mia Gaia Polansky, George Kopanas, Stephan Garbin, Todd Zickler, Dor Verbin*  
  `2026-05-27` · `cs.CV` · [abs](https://arxiv.org/abs/2605.29136) · [pdf](https://arxiv.org/pdf/2605.29136.pdf)


<!-- AUTO-GENERATED-END -->
