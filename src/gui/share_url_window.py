from tkinter import Frame, ttk

from ..web_interface import request_juno_cam_img

class ShareURLWindow(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("imjo")
        self.columnconfigure(index=2)
        self.rowconfigure(index=2)
        self.label = ttk.Label(self, text="Enter the share URL")
        self.label.grid(column=0, row=0)
        self.url_entry = ttk.Entry(self, width=80)
        self.url_entry.grid(column=0, row=1)
        self.go_button = ttk.Button(self, text="Go", command=self.go_pressed)
        self.go_button.grid(column=1, row=1)
    
    def go_pressed(self):
        # Make the call
        request_juno_cam_img(self.url_entry.get())
        # Go to the next scene
        