#! /usr/bin/env python
import argparse
import os

# Script to run pose estimation on an image

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image', type=str, help='input image')
    parser.add_argument('--output', type=str, default='.', help='output image')
    args = parser.parse_args()

    # Run pose estimation
    os.chdir('keras_Realtime_MultiPerson_Pose_Estimation/')
    os.system('./extract_keypoints.py --image {} --output {}'.format(args.image, args.output))
    
