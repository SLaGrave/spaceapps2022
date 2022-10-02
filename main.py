# standard libs
from threading import Thread
import logging
logging.getLogger().setLevel(logging.DEBUG)

from tkinter import *

# 3rd-party libs

# custom libs
from src import *


if __name__ == "__main__":
    root = Tk()

    juan = FilterList(root)
    juan.objects = ["test", "wow"]
    juan.update_self()
    juan.grid()
    root.mainloop()
