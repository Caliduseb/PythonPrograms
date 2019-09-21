import PIL
from PIL import Image
import numpy as np

name = str(input("input image > "))
img = Image.open(name + ".png", "r")
widht, height = img.size
Hochkant, Breit, Quadrat = False, False, False
if height > widht:
    Hochkant = True
if height < widht:
    Breit = True
if height == widht:
    Quadrat = True
    exit()

if Hochkant:
    print("hochkant")
    diff = int((height - widht)/2)
    Image2 = Image.new("RGB", (diff, height), "white")
    imga = np.hstack([Image2, img, Image2])
    imga = PIL.Image.fromarray([Image2, img, Image2])
    imga.save(name + '_Quadrat.jpg')

if Breit:
    diff = int((widht - height)/2)
    Image2 = Image.new("RGB", (widht, diff), "white")
    imgs_comb = np.vstack([Image2, img, Image2])
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save(name + '_Quadrat.jpg')
