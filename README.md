## **Make-Your-Video**
> **Make-Your-Video: Customized Video Generation Using Textual and Structural Guidance**
>
>
> <a href=''><img src='https://img.shields.io/badge/arXiv--red'></a> <a href='https://doubiiu.github.io/projects/Make-Your-Video/'><img src='https://img.shields.io/badge/Project-Video-Green'></a>

## **Abstract**
TL;DR: Make-Your-Video is a customized video generation model with both text and motion structure (depth) control. It inherits rich visual concepts from image LDM and supports longer video inference.
>Creating a vivid video from the event or scenario in our imagination is a truly fascinating experience. Recent advancements in text-to-video synthesis have unveiled the potential to achieve this with prompts only. While text is convenient in conveying the overall scene context, it may be insufficient to control precisely. In this paper, we explore customized video generation by utilizing text as context description and motion structure (e.g. frame-wise depth) as concrete guidance.
Our method, dubbed Make-Your-Video, involves joint-conditional video generation using a Latent Diffusion Model that is pre-trained for still image synthesis and then promoted for video generation with the introduction of temporal modules. This two-stage learning scheme not only reduces the computing resources required, but also improves the performance by transferring the rich concepts available in image datasets solely into video generation. Moreover, we use a simple yet effective causal attention mask strategy to enable longer video synthesis, which mitigates the potential quality degradation effectively.
Experimental results show the superiority of our method over existing baselines, particularly in terms of temporal coherence and fidelity to users' guidance. In addition, our model enables several intriguing applications that demonstrate potential for practical usage.

## **Method Overview**
<!-- <p align="center">
<img src="./assets/overview_dark.jpg#gh-dark-mode-only" width="100%"/>
<img src="./assets/overview.jpg#gh-light-mode-only" width="100%"/>
</p> -->
![](./assets/overview.jpg#gh-light-mode-only)
![](./assets/overview_black.png#gh-dark-mode-only)

## **Results (Please check the [project page](https://doubiiu.github.io/projects/Make-Your-Video/) for more results)**
### Depth-conditioned text-to-video generation (16 frames)
<table class="center" style="text-align:center;">
  <td colspan="2">"Three red tomatos on the brunch"</td>
  <td colspan="2">"Mature man standing on a train. he is typing on his smart phone"</td>
  <td colspan="2">"Pyro sparklers ice fire celebration fireworks"</td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16_depth/007451_007500__14878396.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16/007451_007500__14878396.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16_depth/009201_009250__19064863.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16/009201_009250__19064863.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16_depth/002401_002450__17741461.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_16/002401_002450__17741461.mp4" />
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
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32_depth/069301_069350__27453052.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32/069301_069350__27453052.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32_depth/027551_027600__1039433363.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32/027551_027600__1039433363.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32_depth/096701_096750__34693771.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video_32/096701_096750__34693771.mp4" />
  </td>
</tr>
</table >


## **Applications**
### Real-life scene to video
<table class="center" style="text-align:center;">
  <td colspan="4">"A dam discharging water"</td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/dam_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/dam_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/dam_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/dam_lvdm.mp4" />
  </td>

</tr>
  <td colspan="4">"A futuristic rocket ship on a launchpad, with sleek design, glowing lights"
  </td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/rocket_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/rocket_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/rocket_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/real-life/rocket_lvdm.mp4" />
  </td>
</tr>
			   		<tr style="font-weight: bolder;">
						<td>Real-life scene</td>
						<td>Ours</td>
						<td>Text2Video-zero+CtrlNet</td>
						<td>LVDM<sub>Ext</sub>+Adapter</td>
			   		</tr>
</table >

### 3D scene modeling to video
<table class="center" style="text-align:center;">
  <td colspan="4">"A train on the rail, 2D cartoon style"</td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/train_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/train_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/train_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/train_lvdm.mp4" />
  </td>

</tr>
  <td colspan="4">"A Van Gogh style painting on drawing board in park, some books on the picnic blanket, photorealistic"
  </td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/book_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/book_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/book_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/book_lvdm.mp4" />
  </td>
</tr>

</tr>
  <td colspan="4">"A Chinese ink wash landscape painting"
  </td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/mountain_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/mountain_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/mountain_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/3dmodeling/mountain_lvdm.mp4" />
  </td>
</tr>
			   		<tr style="font-weight: bolder;">
						<td>Real-life scene</td>
						<td>Ours</td>
						<td>Text2Video-zero+CtrlNet</td>
						<td>LVDM<sub>Ext</sub>+Adapter</td>
			   		</tr>
</table >

### Video re-rendering
<table class="center" style="text-align:center;">
  <td colspan="6">"A tiger walks in the forest, photorealistic"</td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/bear_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/bear_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/bear_sddepth.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/bear_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/bear_lvdm.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/bear_tav.mp4" />
  </td>
</tr>
  <td colspan="6">"An origami boat moving on the sea"
  </td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/boat_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/boat_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/boat_sddepth.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/boat_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/boat_lvdm.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/boat_tav.mp4" />
  </td>
</tr>

</tr>
  <td colspan="6">"A camel walking on the snow field, Miyazaki Hayao anime style"
  </td>
  <tr>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/camel_input.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/camel_ours.mp4" />
  </td>

  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/camel_sddepth.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/camel_t2vzero.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/camel_lvdm.mp4" />
  </td>
  <td>
    <video autoplay="" loop="" muted="" playsinline="" width="170" src="./assets/video-rerendering/camel_tav.mp4" />
  </td>
</tr>
			   		<tr style="font-weight: bolder;">
						<td>Original video</td>
						<td>Ours</td>
						<td>SD-Depth</td>
						<td>Text2Video-zero+CtrlNet</td>
						<td>LVDM<sub>Ext</sub>+Adapter</td>
						<td>Tune-A-Video</td>
			   		</tr>
</table >


## **Changelog**
- 2023.06.01 Create this repo and launch the project webpage.

<!-- ## **Citation**

```

```
-->
## **Acknowledgement**
We gratefully acknowledge the Visual Geometry Group of University of Oxford for collecting the [WebVid-10M](https://m-bain.github.io/webvid-dataset/) dataset and follow the corresponding terms of access.
