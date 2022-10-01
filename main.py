<<<<<<< HEAD


# standard libs
from threading import Thread
import logging
logging.getLogger().setLevel(logging.DEBUG)

# 3rd-party libs

# custom libs
from src import *
from src.gui.run import run_gui


if __name__ == "__main__":
    gui_thread = Thread(target=run_gui)
    gui_thread.start()

    # other processing here
    request_juno_cam_img("https://www.missionjuno.swri.edu/junocam/processing?id=13926")

    gui_thread.join()
