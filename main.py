# standard libs
from threading import Thread
import logging
logging.getLogger().setLevel(logging.DEBUG)

# 3rd-party libs

# custom libs
from src import *
from src.gui.run import run_gui


if __name__ == "__main__":

    # data init

    
    run_gui()