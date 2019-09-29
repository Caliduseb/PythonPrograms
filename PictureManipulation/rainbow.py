from PIL import Image, ImageDraw

he = 500

mode = input("rb | bg | all\n> ")

image = Image.new('RGB', (he,he), color='white')
d = ImageDraw.Draw(image)

for height in range(he):
    for i in range(he):
        if mode == "rb":
            d.point((i,height), (int(i * (255/he)), 0 , int(height * (255/he))))
        elif mode == "bg":
            d.point((i,height), (0, int(((255/he)*((height**2)+i**2)**0.5)/2) , int(height * (255/he))))
        elif mode == "all":
            d.point((i,height), (int(i * (255/he)), int(((255/he)*((height**2)+i**2)**0.5)/2) , int(height * (255/he))))

image.save("test.png")
