from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


class MainWindow:
    """Primary window for ImJo Editor."""
    def __init__(self):
        self.script_name = ""

    def get_script(self):
        script_name = askopenfilename()

    def save_img(self):
        pass

    def main_window(self):
        """Initialize the GUI and start the loop."""
        mainwindow = Tk()

        # center on the screen
        window_width = 1200
        window_height = 800
        screen_width = mainwindow.winfo_screenwidth()
        screen_height = mainwindow.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        mainwindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # create main frames
        img_frm = Frame(mainwindow, bg='cyan', width=2*window_width//3, height=2*window_height//3, pady=3)
        code_frm = Frame(mainwindow, bg='green', width=window_width//3, height=2*window_height//3, pady=3)
        fx_frm = Frame(mainwindow, bg='yellow', width=2*window_width//3, height=window_height//3, pady=3)
        other_frm = Frame(mainwindow, bg='magenta', width=window_width//3, height=window_height//3, pady=3)

        # layout the frames
        mainwindow.grid_rowconfigure(1, weight=1)
        mainwindow.grid_rowconfigure(0, weight=1)

        img_frm.grid(row=0, column=0, sticky="ew")
        code_frm.grid(row=0, column=1, sticky="nsew")
        fx_frm.grid(row=1, column=0, sticky="ew")
        other_frm.grid(row=1, column=1, sticky="ew")

        img_frm.grid()
        ttk.Label(other_frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(other_frm, text="Run", command=mainwindow.destroy).grid(column=0, row=0)
        ttk.Button(other_frm, text="Save", command=self.save_img).grid(column=0, row=1)
        ttk.Button(other_frm, text="Select Script", command=self.get_script).grid(column=0, row=2)

        mainwindow.title(self.script_name)

        mainwindow.mainloop()