from PIL import Image
from PIL import ImageDraw
import os
from glob import glob
from pathlib import Path


shift = 42

result = list(Path(".").rglob("*.[jJ][pP][gG]"))

icon = Image.open("header.jpg")
x,y = icon.size

counter = 0

for file in result:
    im = Image.open(file)
    if((x,y) == im.size):
    	continue
    draw = ImageDraw.Draw(im)
    im.paste(icon, (0, shift, x, shift + y))
    im.save(file, format= 'JPEG', quality=100)
    counter = counter + 1
    print("Done : {}/{}".format(counter, len(result) - 1))
