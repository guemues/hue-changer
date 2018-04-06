
from cv2 import COLOR_HSV2RGB, COLOR_RGB2HSV, COLOR_BGR2RGB
import numpy as np
import matplotlib as mpl
import cv2


def change_in_range(texture, min_hue, max_hue):
    """
    Make images in between some hue ranges

    :type max_hue: int
    :type min_hue: int
    :type texture: ndarray
    """
    min_hue = int(min_hue / 2)
    max_hue = int(max_hue / 2)

    hsv_texture = cv2.cvtColor(texture, COLOR_RGB2HSV)
    hue_array = hsv_texture[:, :, 0]
    # saturation_array = hsv_texture[:, :, 1]
    # L_array = hsv_texture[:, :, 2]

    defined_hue_variance = max_hue - min_hue
    # defined_saturation_variance = max_saturation - min_saturation
    # defined_L_variance = max_L - min_L

    texture_hue_variance = np.max(hue_array) - np.min(hue_array)
    # texture_saturation_variance = np.max(hue_array) - np.min(hue_array)
    # texture_L_variance = np.max(hue_array) - np.min(hue_array)

    hue_array = (defined_hue_variance / texture_hue_variance) * (hue_array - np.min(hue_array)) + min_hue
    # saturation_array = (defined_saturation_variance / texture_saturation_variance) * (saturation_array - np.min(saturation_array)) + min_saturation
    # L_array = (defined_L_variance / texture_L_variance) * (L_array - np.min(L_array)) + min_L

    hsv_texture[:, :, 0] = np.mod(hue_array, 180)
    # hsv_texture[:, :, 1] = saturation_array
    # hsv_texture[:, :, 2] = L_array

    return cv2.cvtColor(hsv_texture, COLOR_HSV2RGB)


if __name__ == "__main__":
    mpl.use('TkAgg')
    import matplotlib.pyplot as plt
    t = cv2.imread('../uFPG2T.jpg')
    t = cv2.cvtColor(t, COLOR_BGR2RGB)

    plt.imshow(change_in_range(t, (-10.5071996 / 2), -2))
    plt.show()
    plt.savefig('../test.png')
