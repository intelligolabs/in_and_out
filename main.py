#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from torch.utils.data import DataLoader

from data.ksdd2 import KolektorSDD2

def main(args):
    # Dataset.
    print('Loading KolektorSDD2 training set...')
    train_data = KolektorSDD2(dataroot=args.dataset_path, split='train', scale='half', debug=False)
    print('Number of samples:', len(train_data))

    print('Loading KolektorSDD2 test set...')
    test_data = KolektorSDD2(dataroot=args.dataset_path, split='test', scale='half', debug=False)
    print('Number of samples:', len(test_data))
    
    # DataLoader.
    train_loader = DataLoader(train_data, batch_size=4, shuffle=True, num_workers=4)
    test_loader = DataLoader(test_data, batch_size=4, shuffle=False, num_workers=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test the KolektorSDD2 dataset')
    parser.add_argument('--dataset_path', type=str, default='.', help='Path to the KolektorSDD2 dataset')

    args = parser.parse_args()
    main(args)
