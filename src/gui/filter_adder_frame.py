from tkinter import ttk
import tkinter as tk

from ..img_proc import filters
from .filter_frame import FilterFrame

class FilterAdderFrame(ttk.Frame):
    def __init__(self, master, filter_list):
        super().__init__(master)
        for filter in filters:
            filter_frame = FilterFrame(master=self, filter=filter, filter_list=filter_list)
            filter_frame.pack(side=tk.LEFT)
        