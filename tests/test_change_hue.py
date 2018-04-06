import cv2
from cv2 import COLOR_BGR2HSV, COLOR_BGR2RGB, COLOR_RGB2HSV
from huechanger import change_in_range
import requests


def test_change_hue():

    url = "https://snag.gy/uFPG2T.jpg"
    filename = url.split("/")[-1]
    r = requests.get(url, timeout=1)

    assert r.status_code == 200

    with open(filename, 'wb') as f:
        f.write(r.content)

    t = cv2.imread(filename)

    MAX_HUE = 30
    MIN_HUE = 10

    t = cv2.cvtColor(t, COLOR_BGR2RGB)
    hue_changed = change_in_range(t, MIN_HUE, MAX_HUE)
    hue_changed = cv2.cvtColor(hue_changed, COLOR_RGB2HSV)
    hue_values = hue_changed[:, :, 0]

    assert hue_values.shape[0] * hue_values.shape[1] == t.shape[0] * t.shape[1]

