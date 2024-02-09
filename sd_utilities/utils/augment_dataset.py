#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse

from PIL import Image


def main(args):
    input_dir = args.input_dir
    output_dir = args.output_dir

    # Create the output directory if it doesn't exist.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory.
    files = sorted(os.listdir(input_dir))

    id_counter = 0
    for f in files:
        # Check if the file is a an image.
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Open the image.
            image_path = os.path.join(input_dir, f)
            img = Image.open(image_path)

            # Crop the image.
            # cropped_img = img.crop((10, 10, img.width - 10, img.height - 10))

            # Resize the image.
            # resized_img = img.resize((int(img.width * 0.4), int(img.height * 0.4)))

            # Horizontal flip.
            hflipped_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

            # Vertical flip.
            vflipped_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

            # Save the images.
            img.save(os.path.join(output_dir, f"{id_counter}.jpg"))

            # id_counter += 1
            # cropped_img.save(os.path.join(output_dir, f"{id_counter}.jpg"))

            # id_counter += 1
            # resized_img.save(os.path.join(output_dir, f"{id_counter}.jpg"))

            id_counter += 1
            hflipped_img.save(os.path.join(output_dir, f"{id_counter}.jpg"))

            id_counter += 1
            vflipped_img.save(os.path.join(output_dir, f"{id_counter}.jpg"))

            # Close the images.
            img.close()
            # cropped_img.close()
            # resized_img.close()
            hflipped_img.close()
            vflipped_img.close()

            id_counter += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, help="Input directory")
    parser.add_argument("--output_dir", type=str, help="Output directory")
    args = parser.parse_args()

    main(args)
