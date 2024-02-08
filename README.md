## ___***Make-Your-Video: Customized Video Generation Using Textual and Structural Guidance***___

<div align="center">

 <a href='https://arxiv.org/abs/2306.00943'><img src='https://img.shields.io/badge/arXiv-2306.00943-b31b1b.svg'></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 <a href='https://doubiiu.github.io/projects/Make-Your-Video/'><img src='https://img.shields.io/badge/Project-Video-Green'></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




_**[Jinbo Xing](https://doubiiu.github.io/), [Menghan Xia*](https://menghanxia.github.io), [Yuxin Liu](), [Yuechen Zhang](https://julianjuaner.github.io/), [Yong Zhang](https://yzhang2016.github.io), [Yingqing He](https://github.com/YingqingHe), [Hanyuan Liu](https://github.com/hyliu), <br>[Haoxin Chen](), [Xiaodong Cun](https://vinthony.github.io/academic/), [Xintao Wang](https://xinntao.github.io/), [Ying Shan](https://scholar.google.com/citations?hl=en&user=4oXBp9UAAAAJ&view_op=list_works&sortby=pubdate), [Tien-Tsin Wong](https://www.cse.cuhk.edu.hk/~ttwong/myself.html)**_
<br><br>
(* corresponding author)

From CUHK and Tencent AI Lab.

IEEE TVCG 2024
</div>

## 🔆 Introduction
 Make-Your-Video is a customized video generation model with both text and motion structure (depth) control. It inherits rich visual concepts from image LDM and supports longer video inference.


## 🤗 **Applications**
### Real-life scene to video
<table class="center">
			   		<tr style="font-weight: bolder;text-align:center;">
						<td>Real-life scene</td>
						<td>Ours</td>
						<td>Text2Video-zero+CtrlNet</td>
						<td>LVDM<sub>Ext</sub>+Adapter</td>
			   		</tr>
  
  <tr>
  <td>
    <img src=assets/real-life_GIF/dam_input.gif width="170">
  </td>
  <td>
    <img src=assets/real-life_GIF/dam_ours.gif width="170">
  </td>

  <td>
    <img src=assets/real-life_GIF/dam_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/real-life_GIF/dam_lvdm.gif width="170">
  </td>
</tr>
<tr><td colspan="4">"A dam discharging water"</td></tr>
  

  <tr>
  <td>
    <img src=assets/real-life_GIF/rocket_input.gif width="170">
  </td>
  <td>
    <img src=assets/real-life_GIF/rocket_ours.gif width="170">
  </td>

  <td>
    <img src=assets/real-life_GIF/rocket_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/real-life_GIF/rocket_lvdm.gif width="170">
  </td>
</tr>
<tr><td colspan="4">"A futuristic rocket ship on a launchpad, with sleek design, glowing lights"</td></tr>
</table >

### 3D scene modeling to video
<table class="center">
			   		<tr style="font-weight: bolder;text-align:center;">
						<td>Real-life scene</td>
						<td>Ours</td>
						<td>Text2Video-zero+CtrlNet</td>
						<td>LVDM<sub>Ext</sub>+Adapter</td>
			   		</tr>
  
  <tr>
  <td>
    <img src=assets/3dmodeling_GIF/train_input.gif width="170">
  </td>
  <td>
    <img src=assets/3dmodeling_GIF/train_ours.gif width="170">
  </td>

  <td>
    <img src=assets/3dmodeling_GIF/train_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/3dmodeling_GIF/train_lvdm.gif width="170">
  </td>
</tr>
<tr><td colspan="4">"A train on the rail, 2D cartoon style"</td></tr>
  
  <tr>
  <td>
    <img src=assets/3dmodeling_GIF/book_input.gif width="170">
  </td>
  <td>
    <img src=assets/3dmodeling_GIF/book_ours.gif width="170">
  </td>

  <td>
    <img src=assets/3dmodeling_GIF/book_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/3dmodeling_GIF/book_lvdm.gif width="170">
  </td>
</tr>
<tr><td colspan="4">"A Van Gogh style painting on drawing board in park, some books on the picnic blanket, photorealistic"</td></tr>

</tr>
  
  <tr>
  <td>
    <img src=assets/3dmodeling_GIF/mountain_input.gif width="170">
  </td>
  <td>
    <img src=assets/3dmodeling_GIF/mountain_ours.gif width="170">
  </td>

  <td>
    <img src=assets/3dmodeling_GIF/mountain_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/3dmodeling_GIF/mountain_lvdm.gif width="170">
  </td>
</tr>
<tr><td colspan="4">"A Chinese ink wash landscape painting"</td></tr>
</table >

### Video re-rendering
<table class="center">
			   		<tr style="font-weight: bolder; text-align:center;">
						<td>Original video</td>
						<td>Ours</td>
						<td>SD-Depth</td>
						<td>Text2Video-zero+CtrlNet</td>
						<td>LVDM<sub>Ext</sub>+Adapter</td>
						<td>Tune-A-Video</td>
			   		</tr>
  
  <tr>
  <td>
    <img src=assets/video-rerendering_GIF/bear_input.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/bear_ours.gif width="170">
  </td>

  <td>
    <img src=assets/video-rerendering_GIF/bear_sddepth.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/bear_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/bear_lvdm.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/bear_tav.gif width="170">
  </td>
</tr>
  <tr><td colspan="6">"A tiger walks in the forest, photorealistic"</td></tr>
  
  <tr>
  <td>
    <img src=assets/video-rerendering_GIF/boat_input.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/boat_ours.gif width="170">
  </td>

  <td>
    <img src=assets/video-rerendering_GIF/boat_sddepth.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/boat_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/boat_lvdm.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/boat_tav.gif width="170">
  </td>
  </tr>
  <tr><td colspan="6">"An origami boat moving on the sea"</td></tr>

  
  <tr>
  <td>
    <img src=assets/video-rerendering_GIF/camel_input.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/camel_ours.gif width="170">
  </td>

  <td>
    <img src=assets/video-rerendering_GIF/camel_sddepth.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/camel_t2vzero.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/camel_lvdm.gif width="170">
  </td>
  <td>
    <img src=assets/video-rerendering_GIF/camel_tav.gif width="170">
  </td>
  </tr>
  <tr><td colspan="6">"A camel walking on the snow field, Miyazaki Hayao anime style"</td></tr>
</table >

## 🌟 **Method Overview**

![](./assets/overview.jpg#gh-light-mode-only)
![](./assets/overview_black.png#gh-dark-mode-only)


## 📝 Changelog
- __[2023.11.30]__: 🔥🔥 Release the main model.
- __[2023.06.01]__: 🔥🔥 Create this repo and launch the project webpage.
<br>


## 🧰 Models

|Model|Resolution|Checkpoint|
|:---------|:---------|:--------|
|MakeYourVideo256|256x256|[Hugging Face](https://huggingface.co/Doubiiu/Make-Your-Video/blob/main/model.ckpt)|

It takes approximately 13 seconds and requires a peak GPU memory of 20 GB to animate an image using a single NVIDIA A100 (40G) GPU.

## ⚙️ Setup

### Install Environment via Anaconda (Recommended)
```bash
conda create -n makeyourvideo python=3.8.5
conda activate makeyourvideo
pip install -r requirements.txt
```


## 💫 Inference 
### 1. Command line
1) Download the pre-trained depth estimation model from [Hugging Face](https://huggingface.co/Doubiiu/Make-Your-Video/blob/main/dpt_hybrid-midas-501f0c75.pt), and put the `dpt_hybrid-midas-501f0c75.pt` in `checkpoints/depth/dpt_hybrid-midas-501f0c75.pt`.
2) Download pretrained models via [Hugging Face](https://huggingface.co/Doubiiu/Make-Your-Video/blob/main/model.ckpt), and put the `model.ckpt` in `checkpoints/makeyourvideo_256_v1/model.ckpt`.
3) Input the following commands in terminal.
```bash
  sh scripts/run.sh
```





## 👨‍👩‍👧‍👦 Other Interesting Open-source Projects
[VideoCrafter1](https://github.com/AILab-CVC/VideoCrafter): Framework for high-quality video generation.

[DynamiCrafter](https://doubiiu.github.io/projects/DynamiCrafter/): Open-domain image animation methods using video diffusion priors.

Play with these projects in the same conda environement!
## 😉 Citation
```bib
@article{xing2023make,
  title={Make-Your-Video: Customized Video Generation Using Textual and Structural Guidance},
  author={Xing, Jinbo and Xia, Menghan and Liu, Yuxin and Zhang, Yuechen and Zhang, Yong and He, Yingqing and Liu, Hanyuan and Chen, Haoxin and Cun, Xiaodong and Wang, Xintao and others},
  journal={arXiv preprint arXiv:2306.00943},
  year={2023}
}
```


## 📢 Disclaimer
We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes.
****


## 🌞 **Acknowledgement**
We gratefully acknowledge the Visual Geometry Group of University of Oxford for collecting the [WebVid-10M](https://m-bain.github.io/webvid-dataset/) dataset and follow the corresponding terms of access.
