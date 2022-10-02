# standard libs
from threading import Thread
import logging
logging.getLogger().setLevel(logging.DEBUG)

from tkinter import *
from src.gui.share_url_window import ShareURLWindow

# 3rd-party libs

# custom libs
from src import *


if __name__ == "__main__":
    root = Tk()

    juan = ShareURLWindow(root)
    juan.grid()
    root.mainloop()