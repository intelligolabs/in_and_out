#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse


def main(args):
    input_dir = args.input_dir
    token = args.token

    # List all files in the input directory.
    files = sorted(os.listdir(input_dir))

    for f in files:
        # Check if the file is an image.
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Create a text file with the specified text.
            base_name = os.path.splitext(f)[0]
            text_file_path = os.path.join(input_dir, f"{base_name}.txt")

            # Write the user-specified text to the text file.
            with open(text_file_path, 'w') as text_file:
                text_file.write(token)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, help="Input directory")
    parser.add_argument("--token", type=str, help="Output directory")
    args = parser.parse_args()

    main(args)
