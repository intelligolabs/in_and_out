#!/bin/sh

accelerate launch \
--config_file=configs/accelerate_config.yaml \
train_network.py \
--dataset_config=configs/dataset_config.toml \
--config_file=configs/training_config.toml