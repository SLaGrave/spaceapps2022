from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from turtle import update
from PIL import ImageTk, Image


class MainWindow:
    """Primary window for ImJo Editor."""
    def __init__(self):
        self.mainwindow = Tk()
        self.mainwindow.resizable(False, False)

        # center on the screen
        screen_width = self.mainwindow.winfo_screenwidth()
        screen_height = self.mainwindow.winfo_screenheight()
        self.mainwindow.geometry("%dx%d" % (screen_width, screen_height))

        # create main frames
        img_frm = Frame(self.mainwindow, bg='cyan', width=2*screen_width//3, height=2*screen_height//3)
        code_frm = Frame(self.mainwindow, bg='green', width=screen_width//3, height=2*screen_height//3, pady=3)
        fx_frm = Frame(self.mainwindow, bg='yellow', width=2*screen_width//3, height=screen_height//3, pady=3)
        other_frm = Frame(self.mainwindow, bg='magenta', width=screen_width//3, height=screen_height//3, pady=3)

        img_frm.pack()

        # layout the frames
        self.mainwindow.grid_rowconfigure(1, weight=1)
        self.mainwindow.grid_rowconfigure(0, weight=1)

        img_frm.grid(row=0, column=0, sticky="nsew")
        code_frm.grid(row=0, column=1, sticky="nsew")
        fx_frm.grid(row=1, column=0, sticky="nsew")
        other_frm.grid(row=1, column=1, sticky="nsew")

        # put elements in other frame
        self.script_name = StringVar(fx_frm, "Hello World")
        self.l = Label(fx_frm, textvariable=self.script_name).grid(column=0, row=3)

        ttk.Button(other_frm, text="Run", command=self.mainwindow.destroy).grid(column=0, row=0)
        ttk.Button(other_frm, text="Save", command=self.save_img).grid(column=0, row=1)
        ttk.Button(other_frm, text="Select Script", command=self.get_script).grid(column=0, row=2)


        # create a canvas for image
        image = Image.open('assets/rick1.png')
        imwidth  = image.width
        imheight = image.height



        canvas_for_image = Canvas(img_frm, bg='green', height=imheight, width=imwidth, borderwidth=0, highlightthickness=0)
        canvas_for_image.grid(row=0, column=0, sticky='nesw', padx=0, pady=0)

        canvas_for_image.image = ImageTk.PhotoImage(image.resize((imwidth, imheight), Image.ANTIALIAS))
        canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')


        self.mainwindow.title(self.script_name)

    def get_script(self):
        self.script_name = askopenfilename()


    def save_img(self):
        pass

    def main_window(self):
        """Initialize the GUI and start the loop."""
        

        self.mainwindow.mainloop()