from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


class MainWindow:
    """Primary window for ImJo Editor."""
    def __init__(self):
        self.script_name = ""

        self.mainwindow = Tk()

        # center on the screen
        window_width = 1200
        window_height = 800
        screen_width = self.mainwindow.winfo_screenwidth()
        screen_height = self.mainwindow.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.mainwindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # create main frames
        img_frm = Frame(self.mainwindow, bg='cyan', width=2*window_width//3, height=2*window_height//3, pady=3)
        code_frm = Frame(self.mainwindow, bg='green', width=window_width//3, height=2*window_height//3, pady=3)
        fx_frm = Frame(self.mainwindow, bg='yellow', width=2*window_width//3, height=window_height//3, pady=3)
        other_frm = Frame(self.mainwindow, bg='magenta', width=window_width//3, height=window_height//3, pady=3)

        img_frm.pack()

        # layout the frames
        self.mainwindow.grid_rowconfigure(1, weight=1)
        self.mainwindow.grid_rowconfigure(0, weight=1)

        img_frm.grid(row=0, column=0, sticky="ew")
        code_frm.grid(row=0, column=1, sticky="nsew")
        fx_frm.grid(row=1, column=0, sticky="ew")
        other_frm.grid(row=1, column=1, sticky="ew")

        # put elements in other frame
        self.l = ttk.Label(fx_frm, text="hello world").grid(column=0, row=3)
        # self.l.configure(text=self.script_name)
        ttk.Button(other_frm, text="Run", command=self.mainwindow.destroy).grid(column=0, row=0)
        ttk.Button(other_frm, text="Save", command=self.save_img).grid(column=0, row=1)
        ttk.Button(other_frm, text="Select Script", command=self.get_script).grid(column=0, row=2)


        # create a canvas for image
        canvas_for_image = Canvas(img_frm, bg='green', height=1000, width=1000, borderwidth=0, highlightthickness=0)
        canvas_for_image.grid(row=0, column=0, sticky='nesw', padx=0, pady=0)
        image = Image.open('assets/rick1.png')
        canvas_for_image.image = ImageTk.PhotoImage(image.resize((1000, 1000), Image.ANTIALIAS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')


        self.mainwindow.title(self.script_name)

    def get_script(self):
        self.script_name = askopenfilename()


    def save_img(self):
        pass

    def main_window(self):
        """Initialize the GUI and start the loop."""
        

        self.mainwindow.mainloop()