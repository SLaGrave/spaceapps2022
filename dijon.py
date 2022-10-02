# standard libs
import logging
logging.getLogger().setLevel(logging.DEBUG)

from tkinter import *

# 3rd-party libs

# custom libs
from src import *


if __name__ == "__main__":
    root = Tk()

    url = ShareURLWindow(root)
    url.pack()
    
    root.mainloop()
