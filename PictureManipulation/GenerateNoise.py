import random
from PIL import Image, ImageDraw


def CreatePic(name, width, height):
    he = width
    wi = height
    im = Image.new('RGB', (he, wi), color="white")
    d = ImageDraw.Draw(im)

    for h in range(he):
        for w in range(wi):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            d.point((h, w), fill=(red, green, blue))
        im.save(name + ".png")


CreatePic(input("name > "), int(input("width > ")), int(input("height > ")))
