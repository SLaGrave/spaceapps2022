# standard libs
from threading import Thread
import logging
logging.getLogger().setLevel(logging.DEBUG)

from tkinter import *
from tkinter import ttk
from src.gui.share_url_window import ShareURLWindow

# 3rd-party libs

# custom libs
from src import *
from src.gui.run import run_gui


if __name__ == "__main__":
    root = Tk()

    juan = ShareURLWindow(root)
    juan.grid()
    root.mainloop()