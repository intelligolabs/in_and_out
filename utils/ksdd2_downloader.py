#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse

from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen


def main(args):
    zipurl = 'http://go.vicos.si/kolektorsdd2'

    if not os.path.isdir(args.out_path):
        os.makedirs(args.out_path)

    print('Downloading KolektorSDD2 dataset...')
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(args.out_path)
    print('Done!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and extract KolektorSDD2 dataset')
    parser.add_argument('--out_path', type=str, default='.', help='Output directory')

    args = parser.parse_args()
    main(args)
