# standard libs
from threading import Thread
import logging

logging.getLogger().setLevel(logging.DEBUG)

<<<<<<< HEAD
# 3rd-party libs

# custom libs
from src import *
from src.gui.main_window import MainWindow


if __name__ == "__main__":
    mwindow = MainWindow("assets/jov1.png")
    mwindow.main_window()
=======
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
>>>>>>> 7ea10716c3016d50e9c4dad482078953a39f16ba
