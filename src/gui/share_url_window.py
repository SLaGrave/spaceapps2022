from tkinter import Frame, ttk
import webbrowser

from .main_window import MainWindow
from ..web_interface import request_juno_cam_img

class ShareURLWindow(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("dijon")
        self.columnconfigure(index=2)
        self.rowconfigure(index=4)
        self.explain_label = ttk.Label(self, text="DIJON is a tool to download and edit images of Jupiter from NASA's JunoCam.\nThese images can be obtained from https://www.missionjuno.swri.edu/junocam/processing.\nSelect the image you want, click 'Share Link', and paste that below.")
        self.explain_label.grid(column=0, row=0)
        self.open_button = ttk.Button(self, text="Open SWRI link", command=lambda: webbrowser.open("https://www.missionjuno.swri.edu/junocam/processing"))
        self.open_button.grid(column=0, row=1)
        self.label = ttk.Label(self, text="\nEnter the share URL")
        self.label.grid(column=0, row=2)
        self.url_entry = ttk.Entry(self, width=80)
        self.url_entry.grid(column=0, row=3)
        self.go_button = ttk.Button(self, text="Go", command=self.go_pressed)
        self.go_button.grid(column=1, row=3)
        self.filename_dict = None
    
    def go_pressed(self):
        # Make the call
        self.filename_dict = request_juno_cam_img(self.url_entry.get())
        print(self.filename_dict)
        m = MainWindow(self.filename_dict["imageset"], self.filename_dict["rgb_base"])
        