## **Make-Your-Video**
> **Make-Your-Video: Customized Video Generation Using Textual and Structural Guidance**
>
>
> <a href='https://arxiv.org/abs/2306.00943'><img src='https://img.shields.io/badge/arXiv-2306.00943-red'></a> <a href='https://doubiiu.github.io/projects/Make-Your-Video/'><img src='https://img.shields.io/badge/Project-Video-Green'></a>

## **Abstract**
TL;DR: Make-Your-Video is a customized video generation model with both text and motion structure (depth) control. It inherits rich visual concepts from image LDM and supports longer video inference.
>Creating a vivid video from the event or scenario in our imagination is a truly fascinating experience. Recent advancements in text-to-video synthesis have unveiled the potential to achieve this with prompts only. While text is convenient in conveying the overall scene context, it may be insufficient to control precisely. In this paper, we explore customized video generation by utilizing text as context description and motion structure (e.g. frame-wise depth) as concrete guidance.
Our method, dubbed Make-Your-Video, involves joint-conditional video generation using a Latent Diffusion Model that is pre-trained for still image synthesis and then promoted for video generation with the introduction of temporal modules. This two-stage learning scheme not only reduces the computing resources required, but also improves the performance by transferring the rich concepts available in image datasets solely into video generation. Moreover, we use a simple yet effective causal attention mask strategy to enable longer video synthesis, which mitigates the potential quality degradation effectively.
Experimental results show the superiority of our method over existing baselines, particularly in terms of temporal coherence and fidelity to users' guidance. In addition, our model enables several intriguing applications that demonstrate potential for practical usage.


<!-- ## **Results (Please check the [project page](https://doubiiu.github.io/projects/Make-Your-Video/) for more results)**
### Depth-conditioned text-to-video generation (16 frames)
<table class="center" style="text-align:center;">
  <td colspan="2">"Three red tomatos on the brunch"</td>
  <td colspan="2">"Mature man standing on a train. he is typing on his smart phone"</td>
  <td colspan="2">"Pyro sparklers ice fire celebration fireworks"</td>
  <tr>
  <td>
    https://user-images.githubusercontent.com/58986949/115314310-805b2780-a1a7-11eb-8558-648a367ea231.mp4
  </td>
  <td>
    <img src=assets/t2v-001.gif width="170">
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16_depth/009201_009250__19064863.mp4"></video>
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16/009201_009250__19064863.mp4"></video>
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16_depth/002401_002450__17741461.mp4"></video>
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16/002401_002450__17741461.mp4"></video>
  </td>
</tr>
</table >

### Longer video inference (32 frames)
<table class="center" style="text-align:center;">
  <td colspan="2">"Professional male potter working with clay on potter's wheel in workshop, studio. handmade, art and handicraft concept"</td>
  <td colspan="2">"Whole coconut isolated on black background"</td>
  <td colspan="2">"Burning grass of the field in thailand"</td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32_depth/069301_069350__27453052.mp4"></video>
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32/069301_069350__27453052.mp4"></video>
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32_depth/027551_027600__1039433363.mp4"></video>
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32/027551_027600__1039433363.mp4"></video>
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32_depth/096701_096750__34693771.mp4"></video>
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32/096701_096750__34693771.mp4"></video>
  </td>
</tr>
</table > -->


## **Applications**
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

## **Method Overview**

![](./assets/overview.jpg#gh-light-mode-only)
![](./assets/overview_black.png#gh-dark-mode-only)
## **Changelog**
- 2023.06.01 Create this repo and launch the project webpage.

<!-- ## **Citation**

```

```
-->
## **Acknowledgement**
We gratefully acknowledge the Visual Geometry Group of University of Oxford for collecting the [WebVid-10M](https://m-bain.github.io/webvid-dataset/) dataset and follow the corresponding terms of access.
