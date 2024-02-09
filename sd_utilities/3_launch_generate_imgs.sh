#!/bin/sh

alfa='10'
ratio=1.0
images_per_prompt=5

lora_path=output/lora/SD_MODEL_W_LORA_PATH.safetensors

out_root=generated_imgs/$alfa
mkdir $out_root

python gen_img_diffusers.py \
--ckpt $lora_path \
--outdir $out_root \
--xformers \
--fp16 \
--images_per_prompt $images_per_prompt \
--prompt 'TOKEN(s)' \
--H 512 \
--W 512 \
--seed 1234