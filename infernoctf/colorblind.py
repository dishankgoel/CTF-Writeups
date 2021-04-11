from PIL import Image

im = Image.open('colorblind.png')

pixles = list(im.getdata())

print(pixles, len(pixles))