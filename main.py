import logging

logging.getLogger().setLevel(logging.DEBUG)

from PIL import Image

from src import *

d = request_juno_cam_img("https://www.missionjuno.swri.edu/junocam/processing?id=13926")

# Loop looks like this
# Load image
im = Image.open(d["thumbnail"])
# Run before
im = run_custom_before("./test.py", im)
# Run any filters



# Run after
im = run_custom_after("./test.py", im)
# Show it
im.show()