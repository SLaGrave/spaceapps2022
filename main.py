# standard libs
from threading import Thread
import logging
logging.getLogger().setLevel(logging.DEBUG)

# 3rd-party libs

# custom libs
from src import *
from src.gui.main_window import MainWindow


if __name__ == "__main__":
    mwindow = MainWindow()
    mwindow.main_window()