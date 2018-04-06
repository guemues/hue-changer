#!/usr/bin/env python

"""

This python file is created for change hue of the images
use min max and path arguments to specify your demanded.


"""

import argparse
import huechanger
import matplotlib.pyplot as plt
import cv2

from cv2 import COLOR_BGR2RGB

__author__ = "Orcun Gumus"

parser = argparse.ArgumentParser()

parser.add_argument('--path', dest='path', type=str, help='Input file path')
parser.add_argument('--opath', dest='opath', type=str, help='Output file paht')
parser.add_argument('--min', dest='min', type=int, help='360 degree min HUE')
parser.add_argument('--max', dest='max', type=int, help='360 degree max HUE')

args = parser.parse_args()

min = args.min / 2
max = args.max / 2

t = cv2.imread(args.path)
t = cv2.cvtColor(t, COLOR_BGR2RGB)

plt.imshow(huechanger.change_in_range(t, min, max))
plt.savefig(args.opath)
