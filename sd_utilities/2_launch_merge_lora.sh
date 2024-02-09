#!/bin/sh

python networks/merge_lora.py \
--sd_model models/sd-v1-5-pruned-noema-fp16.safetensors \
--models output/SD_MODEL_PATH.safetensors \
--save_to output/lora/SD_MODEL_W_LORA_PATH.safetensors \
--ratios 0.65 # How the weights are distributed between the two models.