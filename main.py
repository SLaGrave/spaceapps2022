import logging
logging.getLogger().setLevel(logging.DEBUG)

from PIL import Image

from src import *

im = Image.open("pixmap.png")
im.show()

print(built_in_filters)

im2 = im.filter(built_in_filters[5]())
im2.show()
