from cv2.cv2 import COLOR_BGR2GRAY, COLOR_HSV2RGB, COLOR_BGR2HSV, COLOR_RGB2HSV
from numpy import ndarray

import cv2.cv2
import numpy as np
import matplotlib as mpl


def change_in_range(texture, min_hue, max_hue):
    """
    Make images in between some hue ranges

    :type max_hue: int
    :type min_hue: int
    :type texture: ndarray
    """
    hsv_texture = cv2.cvtColor(texture, COLOR_RGB2HSV)
    hue_array = hsv_texture[:, :, 0]
    defined_hue_variance = max_hue - min_hue - 1
    texture_hue_variance = np.max(hue_array) - np.min(hue_array)
    hue_array = (defined_hue_variance / texture_hue_variance) * (hue_array - np.min(hue_array)) + min_hue + 1
    hsv_texture[:, :, 0] = np.mod(hue_array, 180)
    return cv2.cvtColor(hsv_texture, COLOR_HSV2RGB)


if __name__ == "__main__":
    mpl.use('TkAgg')
    import matplotlib.pyplot as plt
    t = cv2.imread('uFPG2T.jpg')
    plt.imshow(change_in_range(t, 10, 30))
    plt.show()
    print()
