#! /usr/bin/env python

# Script to run human parsing on an image

import argparse
import cv2
import os
import scipy.io

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Script to run human parser.')
    parser.add_argument('image', help='Path to image, e.g. ./path/to/image.jpg')
    args = parser.parse_args()

    filename = os.path.split(args.image)[1]

    # Copy image to JPPNet directory
    os.system('cp {} ./LIP_JPPNet/datasets/examples/images/'.format(args.image))

    # Create image list to run over
    os.system('echo /images/{} > ./LIP_JPPNet/datasets/examples/list/val.txt'.format(filename))

    # Change number of files to run over to 1
    os.system('sed -i -e \'s/NUM_STEPS = 6/NUM_STEPS = 1/g\' ./LIP_JPPNet/evaluate_parsing_JPPNet-s2.py')

    # Run JPPNet for human parsing
    os.system('cd LIP_JPPNet; python evaluate_parsing_JPPNet-s2.py; cd ..;')

    # Convert output to .mat
    img = cv2.imread('./LIP_JPPNet/output/parsing/val/{}'.format(os.path.splitext(filename)[0]+'.png'))
    seg_dict = {'segment':img[:,:,0]} # Only need one channel (R, G, or B)
    scipy.io.savemat('./output/{}'.format(os.path.splitext(filename)[0]+'.mat'), seg_dict)
