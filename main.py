import logging

logging.getLogger().setLevel(logging.DEBUG)

from PIL import Image

from src import *


im = combine_rgb("pixmap", mode="RGB", scale=(1, 0.3, 5))
im.filter(filters[0](radius=5))
im.show()
