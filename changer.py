#!/usr/bin/env python

"""

This python file is created for change hue of the images
use min max and path arguments to specify your demanded.


"""

import argparse
import huechanger
import cv2

from cv2 import COLOR_BGR2RGB, COLOR_RGB2BGR

__author__ = "Orcun Gumus"

parser = argparse.ArgumentParser()

parser.add_argument('--path', dest='path', type=str, help='Input file path')
parser.add_argument('--opath', dest='opath', type=str, help='Output file paht')
parser.add_argument('--min', dest='min', type=int, help='360 degree min HUE')
parser.add_argument('--max', dest='max', type=int, help='360 degree max HUE')

args = parser.parse_args()

min = args.min
max = args.max

t = cv2.imread(args.path)
t = cv2.cvtColor(t, COLOR_BGR2RGB)

new_image = huechanger.change_in_range(t, min, max)
new_image = cv2.cvtColor(new_image, COLOR_RGB2BGR)
cv2.imwrite(args.opath, new_image)
