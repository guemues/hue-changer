### Hue Changer Package [![Build Status](https://travis-ci.org/guemues/hue-changer.svg?branch=master)](https://travis-ci.org/guemues/hue-changer)

You have a colorful image and you want to make it red. This package is for you. There is many more method to turn images to grayscale but there is no other package to turn images to other colors. With this package you can turn images a specific HUE ranges.


You can easily install the package via pip. This package only tested in python 3.6.

```
pip intall huechanger
```

**change_in_range** method is taking 3 channel numpy array as RGB image and return an RGB image with maximum hue and minumum hue

```python

url = "https://snag.gy/uFPG2T.jpg"
filename = url.split("/")[-1]
r = requests.get(url, timeout=1)

if r.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(r.content)

t = cv2.imread(filename)

MIN_HUE = 10
MAX_HUE = 30

t = cv2.cvtColor(t, COLOR_BGR2RGB)
new_image = change_in_range(t, MIN_HUE, MAX_HUE)


```


<img src="https://snag.gy/V25svq.jpg" width="200">

will be turn in to

<img src="https://snag.gy/kduXwj.jpg" width="200">

Enjoy with colors

To change images without any coding:
```
optional arguments:
  -h, --help     show this help message and exit
  --path PATH    Input file path
  --opath OPATH  Output file paht
  --min MIN      360 degree min HUE
  --max MAX      360 degree max HUE

```

```
python changer.py --path ./uFPG2T.jpg --opath out.png --min 10 --max 100
```



This python package is implemented for an EPFL cognitive science semester course project.
