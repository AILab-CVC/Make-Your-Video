import argparse, os, sys, glob
import datetime, time
import numpy as np
from omegaconf import OmegaConf
from tqdm import tqdm
from einops import rearrange, repeat
from collections import OrderedDict
import torch
import torchvision
from torch.utils.data import DataLoader
from pytorch_lightning import seed_everything
## note: decord should be imported after torch
from decord import VideoReader, cpu
sys.path.insert(1, os.path.join(sys.path[0], '..', '..'))
from lvdm.models.samplers.ddim import DDIMSampler
from utils.utils import instantiate_from_config, tensor_to_mp4


def get_filelist(data_dir, ext='*'):
    file_list = glob.glob(os.path.join(data_dir, '*.%s'%ext))
    file_list.sort()
    return file_list

def load_model_checkpoint(model, ckpt):
    state_dict = torch.load(ckpt, map_location="cpu")
    if "state_dict" in list(state_dict.keys()):
        state_dict = state_dict["state_dict"]
        try:
            model.load_state_dict(state_dict, strict=True)
        except:
            print('@Loading full checkpoint failed! Try to remove <depth_stage_model>')
            for k in list(state_dict.keys()):
                if k.startswith('depth_stage_model.'):
                    del state_dict[k]
            model.load_state_dict(state_dict, strict=False)
    else:
        # deepspeed
        new_pl_sd = OrderedDict()
        for key in state_dict['module'].keys():
            new_pl_sd[key[16:]]=state_dict['module'][key]
        model.load_state_dict(new_pl_sd)
    print('>>> model checkpoint loaded.')
    return model

def load_prompts(prompt_file):
    f = open(prompt_file, 'r')
    prompt_list = []
    for idx, line in enumerate(f.readlines()):
        l = line.strip()
        if len(l) != 0:
            prompt_list.append(l)
        f.close()
    return prompt_list

def load_data_prompts(data_dir, frame_stride, video_size=(256,256), video_frames=16):
    ## load prompts
    prompt_file = get_filelist(data_dir, 'txt')
    assert len(prompt_file) > 0, "Error: found NO prompt file!"
    ###### default prompt
    default_idx = 0
    default_idx = min(default_idx, len(prompt_file)-1)
    if len(prompt_file) > 1:
        print(f"Warning: multiple prompt files exist. The one {os.path.split(prompt_file[default_idx])[1]} is used.")
    ## only use the first one (sorted by name) if multiple exist
    prompt_list = load_prompts(prompt_file[default_idx])
    n_samples = len(prompt_list)

    ## load video
    file_list = get_filelist(data_dir, 'mp4')
    assert len(file_list) == n_samples, "Error: data and prompts are NOT paired!"
    data_list = []
    filename_list = []
    for idx in range(n_samples):
        vidreader = VideoReader(file_list[idx], ctx=cpu(0), width=video_size[1], height=video_size[0])
        #vidreader = VideoReader(file_list[idx], ctx=cpu(0))
        max_frames = len(vidreader)
        temp_stride = max_frames // video_frames if frame_stride == -1 else frame_stride
        if temp_stride * (video_frames-1) >= max_frames:
            filename = os.path.split(file_list[idx])[1]
            print(f'Warning: default frame stride is used because the input video clip {filename}:{max_frames} is not long enough.')
            temp_stride = max_frames // video_frames
        frame_indices = [temp_stride*i for i in range(video_frames)]
        frames = vidreader.get_batch(frame_indices)
        
        ## [t,h,w,c] -> [c,t,h,w]
        frame_tensor = torch.tensor(frames.asnumpy()).permute(3, 0, 1, 2).float()
        frame_tensor = (frame_tensor / 255. - 0.5) * 2
        data_list.append(frame_tensor)
        _, filename = os.path.split(file_list[idx])
        filename_list.append(filename)
        
    return filename_list, data_list, prompt_list


def save_results(prompt, samples, inputs, filename, realdir, fakedir, fps=8):
    prompt = prompt[0] if isinstance(prompt, list) else prompt
    ## save video
    videos = [inputs, samples]
    savedirs = [realdir, fakedir]
    for idx, video in enumerate(videos):
        if video is None:
            continue
        # b,c,t,h,w
        video = video.detach().cpu()
        video = torch.clamp(video.float(), -1., 1.)
        n = video.shape[0]
        video = video.permute(2, 0, 1, 3, 4) # t,n,c,h,w
        ## print(prompt, video.shape)
        frame_grids = [torchvision.utils.make_grid(framesheet, nrow=int(n), padding=0) for framesheet in video] #[3, 1*h, n*w]
        grid = torch.stack(frame_grids, dim=0) # stack in temporal dim [t, 3, h, n*w]
        grid = (grid + 1.0) / 2.0
        grid = (grid * 255).to(torch.uint8).permute(0, 2, 3, 1)
        path = os.path.join(savedirs[idx], filename)
        torchvision.io.write_video(path, grid, fps=fps, video_codec='h264', options={'crf': '10'})



def save_results_seperate(prompt, samples, inputs, filename, realdir, fakedir, fps=10):
    prompt = prompt[0] if isinstance(prompt, list) else prompt
    ## save video
    videos = [inputs, samples]
    savedirs = [realdir, fakedir]
    for idx, video in enumerate(videos):
        if video is None:
            continue
        # b,c,t,h,w
        video = video.detach().cpu()
        video = torch.clamp(video.float(), -1., 1.)
        n = video.shape[0]
        for i in range(n):
            grid = video[i,...]
            grid = (grid + 1.0) / 2.0
            grid = (grid * 255).to(torch.uint8).permute(1, 2, 3, 0) #thwc
            path = os.path.join(savedirs[idx], f'{filename.split(".")[0]}_sample{i}.mp4')
            torchvision.io.write_video(path, grid, fps=fps, video_codec='h264', options={'crf': '10'})

def get_latent_z(model, videos):
    b, c, t, h, w = videos.shape
    x = rearrange(videos, 'b c t h w -> (b t) c h w')
    z = model.encode_first_stage(x)
    z = rearrange(z, '(b t) c h w -> b c t h w', b=b, t=t)
    return z

def depth_guided_synthesis(args, model, prompts, videos, noise_shape, n_samples=1, ddim_steps=50, ddim_eta=1., \
                        unconditional_guidance_scale=1.0, unconditional_guidance_scale_temporal=None, negative_prompt=False, **kwargs):
    ddim_sampler = DDIMSampler(model)
    cond_depth = model.get_batch_depth(videos, noise_shape[3:])  #[-1,1]
    cond_depth_origin  = None
    if args.save_cond:
        cond_depth_origin = model.get_batch_depth(videos, (args.height, args.width))  #[-1,1]

    batch_size = noise_shape[0]
    ## get condition embeddings (support single prompt only)
    if isinstance(prompts, str):
        prompts = [prompts]
    cond_emb = model.get_learned_conditioning(prompts)
    cond = {"c_concat": [cond_depth], "c_crossattn": [cond_emb]}
    
    if unconditional_guidance_scale != 1.0:
        if negative_prompt:
            # prompts = batch_size * ["ugly, boring, bad anatomy, blurry, poor lighting, dull, unclear, monochrome, lowres, worst quality, low quality"]
            prompts = batch_size * ["monochrome, lowres, worst quality, low quality"]
        else:
            prompts = batch_size * [""]
        uc_emb = model.get_learned_conditioning(prompts)
        uc = {"c_concat": [cond_depth], "c_crossattn": [uc_emb]}
    else:
        uc = None
    
    x_T = None
    batch_variants = []
    for _ in range(n_samples):
        if ddim_sampler is not None:
            samples, _ = ddim_sampler.sample(S=ddim_steps,
                                            conditioning=cond,
                                            batch_size=noise_shape[0],
                                            shape=noise_shape[1:],
                                            verbose=False,
                                            unconditional_guidance_scale=unconditional_guidance_scale,
                                            unconditional_conditioning=uc,
                                            eta=ddim_eta,
                                            temporal_length=noise_shape[2],
                                            conditional_guidance_scale_temporal=unconditional_guidance_scale_temporal,
                                            x_T=x_T,
                                            **kwargs
                                            )        
        ## reconstruct from latent to pixel space
        batch_images = model.decode_first_stage(samples)
        batch_variants.append(batch_images)
    ## variants, batch, c, t, h, w
    batch_variants = torch.stack(batch_variants)
    return batch_variants.permute(1, 0, 2, 3, 4, 5), cond_depth_origin

def run_inference(args, gpu_num, gpu_no):
    ## model config
    config = OmegaConf.load(args.config)
    model_config = config.pop("model", OmegaConf.create())
    
    ## set use_checkpoint as False as when using deepspeed, it encounters an error "deepspeed backend not set"
    model_config['params']['unet_config']['params']['use_checkpoint'] = False
    model = instantiate_from_config(model_config)
    model = model.cuda(gpu_no)

    assert os.path.exists(args.ckpt_path), "Error: checkpoint Not Found!"
    model = load_model_checkpoint(model, args.ckpt_path)
    model.eval()

    ## run over data
    assert (args.height % 16 == 0) and (args.width % 16 == 0), "Error: image size [h,w] should be multiples of 16!"
    assert args.bs == 1, "Current implementation only support [batch size = 1]!"
    ## latent noise shape
    h, w = args.height // 8, args.width // 8
    # channels = model.model.channels
    channels = model.model.diffusion_model.out_channels
    n_frames = args.video_length
    print(f'Inference with {n_frames} frames')
    noise_shape = [args.bs, channels, n_frames, h, w]

    realdir = os.path.join(args.savedir, "input")
    fakedir = os.path.join(args.savedir, "samples")
    os.makedirs(realdir, exist_ok=True)
    os.makedirs(fakedir, exist_ok=True)
    if args.save_cond:
        conddir = os.path.join(args.savedir, "conds")
        os.makedirs(conddir, exist_ok=True)
    
    ## prompt file setting
    assert os.path.exists(args.prompt_dir), "Error: prompt file Not Found!"
    filename_list, data_list, prompt_list = load_data_prompts(args.prompt_dir, args.frame_stride, \
                                                            video_size=(args.height, args.width), video_frames=n_frames)
    num_samples = len(prompt_list)
    samples_split = num_samples // gpu_num
    print('Prompts testing [rank:%d] %d/%d samples loaded.'%(gpu_no, samples_split, num_samples))
    #indices = random.choices(list(range(0, num_samples)), k=samples_per_device)
    indices = list(range(samples_split*gpu_no, samples_split*(gpu_no+1)))
    prompt_list_rank = [prompt_list[i] for i in indices]
    data_list_rank = [data_list[i] for i in indices]
    filename_list_rank = [filename_list[i] for i in indices]

    start = time.time()
    with torch.no_grad(), torch.cuda.amp.autocast():
        for idx, indice in tqdm(enumerate(range(0, len(prompt_list_rank), args.bs)), desc='Sample Batch'):
            prompts = prompt_list_rank[indice:indice+args.bs]
            videos = data_list_rank[indice:indice+args.bs]
            filenames = filename_list_rank[indice:indice+args.bs]
            if isinstance(videos, list):
                videos = torch.stack(videos, dim=0).to("cuda")
            else:
                videos = videos.unsqueeze(0).to("cuda")

            batch_samples, batch_conds = depth_guided_synthesis(args, model, prompts, videos, noise_shape, args.n_samples, args.ddim_steps, args.ddim_eta, \
                                                args.unconditional_guidance_scale, args.unconditional_guidance_scale_temporal, args.negative_prompt)

            ## save each example individually
            for nn, samples in enumerate(batch_samples):
                ## samples : [n_samples,c,t,h,w]
                prompt = prompts[nn]
                filename = filenames[nn]
                #save_results(prompt, samples, videos, filename, realdir, fakedir, fps=8)
                save_results_seperate(prompt, samples, None, filename, realdir, fakedir, fps=8)

                if args.save_cond and batch_conds is not None:
                    cond = batch_conds[nn:nn+1]
                    tensor_to_mp4(video=cond.detach().cpu(), savepath=os.path.join(conddir, filename), fps=8)

    print(f"Saved in {args.savedir}. Time used: {(time.time() - start):.2f} seconds")

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--savedir", type=str, default=None, help="results saving path")
    parser.add_argument("--ckpt_path", type=str, default=None, help="checkpoint path")
    parser.add_argument("--config", type=str, help="config (yaml) path")
    parser.add_argument('--save_cond', action='store_true', default=False, help='saving the conditional input')
    parser.add_argument("--prompt_dir", type=str, default=None, help="a data dir containing videos and prompts")
    parser.add_argument("--n_samples", type=int, default=1, help="num of samples per prompt",)
    parser.add_argument("--ddim_steps", type=int, default=50, help="steps of ddim if positive, otherwise use DDPM",)
    parser.add_argument("--ddim_eta", type=float, default=1.0, help="eta for ddim sampling (0.0 yields deterministic sampling)",)
    parser.add_argument("--bs", type=int, default=1, help="batch size for inference")
    parser.add_argument("--height", type=int, default=512, help="image height, in pixel space")
    parser.add_argument("--width", type=int, default=512, help="image width, in pixel space")
    parser.add_argument("--frame_stride", type=int, default=-1, help="frame extracting from input video")
    parser.add_argument("--unconditional_guidance_scale", type=float, default=7.5, help="prompt classifier-free guidance")
    parser.add_argument("--unconditional_guidance_scale_temporal", type=float, default=None, help="temporal consistency guidance")
    parser.add_argument("--seed", type=int, default=123, help="seed for seed_everything")
    parser.add_argument("--depth_provided", action='store_true', default=False, help="the input is depth instead of video") #
    parser.add_argument("--video_length", type=int, default=16, help="video length")
    parser.add_argument("--save_input", action='store_true', default=False, help="store input for showing")
    parser.add_argument("--negative_prompt", action='store_true', default=False, help="negative prompt")
    return parser


if __name__ == '__main__':
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    print("@CoVideoGen cond-Inference: %s"%now)
    parser = get_parser()
    args = parser.parse_args()

    seed_everything(args.seed)
    rank, gpu_num = 0, 1
    run_inference(args, gpu_num, rank)