name="makeyourvideo_256"

ckpt='checkpoints/makeyourvideo_256_v1/model.ckpt'
config='configs/inference_256_v1.0.yaml'

prompt_dir="prompts/"
res_dir="results"

CUDA_VISIBLE_DEVICES=0 python3 scripts/evaluation/inference_videorerendering.py \
--seed 123 \
--ckpt_path $ckpt \
--config $config \
--savedir $res_dir/$name \
--n_samples 1 \
--bs 1 --height 256 --width 256 \
--unconditional_guidance_scale 7.5 \
--ddim_steps 50 \
--ddim_eta 1.0 \
--prompt_dir $prompt_dir \
--video_length 16 \
--frame_stride 2 \
--save_cond

## inference using single node with multi-GPUs:
# CUDA_VISIBLE_DEVICES=2,3,4,5,6,7 python3 -m torch.distributed.launch \
# --nproc_per_node=6 --nnodes=1 --master_addr=127.0.0.1 --master_port=23456 --node_rank=0 \
# scripts/evaluation/ddp_wrapper.py \
# --module 'inference_videorerendering' \
# --seed 123 \
# --ckpt_path $ckpt \
# --config $config \
# --savedir $res_dir/$name \
# --n_samples 3 \
# --bs 1 --height 256 --width 256 \
# --unconditional_guidance_scale 7.5 \
# --ddim_steps 50 \
# --ddim_eta 1.0 \
# --prompt_dir $prompt_dir \
# --video_length 16 \
# --frame_stride 2 \
# --save_cond