import logging

logging.getLogger().setLevel(logging.DEBUG)

from PIL import Image

from src import *

# Loop looks like this
# Load image
im = Image.open("pixmap.png")
# Run before
im = run_custom_before("./test.py", im)
# Run any filters
im = im.filter(filters[0]())
# Run after
im = run_custom_after("./test.py", im)
# Show it
im.show()