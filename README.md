### Hue Changer Package

You have a colorful image and you want to make it red. This package is for you. There is many more method to turn images to grayscale but there is no other package to turn images to other colors. With this package you can turn images a specific HUE ranges.


You can easily install the package via pip. This package only tested in python 3.6.

```
pip intall huechanger
```


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


This python package is implemented for an EPFL cognitive science semester course project.
