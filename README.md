# Diffusion-based Image Generation for In-distribution Data Augmentation in Surface Defect Detection #

The official PyTorch implementation discussed in the *Diffusion-based Image Generation for In-distribution Data Augmentation in Surface Defect Detection* paper. Accepted at the 19th International Conference on Computer Vision Theory and Applications (VISAPP 2024).

## Installation ##

1. Repository setup
* git clone `https://github.com/intelligolabs/in_and_out`

2. Enviroment setup (the scripts are tested with Pytorch 2.0.1. 1.12.1 is not tested but should work):
* `conda create -n in_and_out python=3.10`
* `conda activate in_and_out`
* `pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113`
* `cd sd_utilities/`
* `pip install --upgrade -r requirements.txt`
* `pip install xformers==0.0.20`
* `pip install bitsandbytes==0.38.1`
* `accelerate config`

## Part 1: Image generation with Stable Diffusion ##

Firstly, enter inside the `sd_utilities/` folder with the command:
* `cd sd_utilities/`

This folder, specifically, is a copy of the repository [sd-scripts](https://github.com/kohya-ss/sd-scripts) of [kohya-ss](https://github.com/kohya-ss).

Then:
1. To generate new images from the pretrain of SD, use the script `3_launch_generate_imgs.sh`. In particular:
    * Use the parameter `--ckpt` to specify the path of the SD model, set as default `models/sd-v1-5-pruned-noema-fp16.safetensors`
2. To finetune the pretrain of SD:
    * For each image in the dataset, create the corresponding label using the script `utils/generate_lbls.py`
        * The token that you specify must have the form `sks type_of_item`
        * Specifically, your dataset folder should then have the following structure:
            ```
            dataset_folder
                |-- img001.png
                |-- img001.txt
                |-- img002.png
                |-- img002.txt
                |-- img00N.png
                |-- img00N.txt
            ```
    * Since we are using the Deambooth technique, we need to generate at least 200 regularization images. In order to do this:
        * Generate 200 new images through the script `3_launch_generate_imgs.sh`, using the token `type_of_item`
        * Generate the corresponding labels using the script `utils/generate_lbls.py` and the token `type_of_item`
    * Put in the same folder your own images (and labels) and the regularization images (and labels)
    * Use the file `1_launch_finetuning.sh` to finetune the SD model
        * Check that all the parameters in `dataset_config.toml` are correct
    * Since we are also using the LoRA technique, use the file `2_launch_merge_lora.sh` to merge the weights
    * Use the file `3_launch_generate_imgs.sh` with the prompt `sks type_of_item` to generate the new images
        * Use the parameter `--ckpt` to specify the path of the finetuned SDLoRA model

### Links to technical documentation ###
Click [here](sd_utilities/_README.md) for the technical documentation.

## Part 2: Tests on the KolektorSDD2 dataset ##

For downloading the KolektorSDD2 dataset, launch the script `utils/ksdd2_dowloader.py`. The `main.py` file, on the other hand, shows the use of the dataset.

We would like to thank ViCoS Lab for the repository [mixed-segdec-net-comind2021](https://github.com/vicoslab/mixed-segdec-net-comind2021), and Jin-Hwa Kim for the repository [orthoad](https://github.com/jnhwkim/orthoad), for providing some of the scripts used to manage the dataset, and all the code.

## Authors ##
Luigi Capogrosso*, Federico Girella*, Francesco Taioli*, Michele Dalla Chiara, Muhammad Aqeel, Franco Fummi, Francesco Setti, and Marco Cristani

*Department of Engineering for Innovation Medicine, University of Verona, Italy*

`name.surname@univr.it`

*These authors contributed equally to this work.
