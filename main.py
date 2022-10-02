# standard libs
from threading import Thread
import logging

from src.gui.script_editor_frame import ScriptEditorFrame
logging.getLogger().setLevel(logging.DEBUG)

from tkinter import *
from tkinter import ttk

# 3rd-party libs

# custom libs
from src import *
from src.gui.run import run_gui


if __name__ == "__main__":
    root = Tk()

    juan = ScriptEditorFrame(root)
    juan.grid()
    root.mainloop()