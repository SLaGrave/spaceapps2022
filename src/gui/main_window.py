from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from turtle import update
from PIL import ImageTk, Image
from src.gui.filter_adder_frame import FilterAdderFrame

from src.gui.filter_list import FilterList
from src.img_proc.custom_parser import run_custom_after, run_custom_before
from .script_editor_frame import ScriptEditorFrame
from ..img_proc import filters

class MainWindow:
    """Primary window for ImJo Editor."""
    def __init__(self, img_filename):
        self.mainwindow = Tk()
        self.mainwindow.state("zoomed")
        # self.mainwindow.resizable(False, False)
        self.img_filename = img_filename

        # center on the screen
        screen_width = self.mainwindow.winfo_screenwidth()
        screen_height = self.mainwindow.winfo_screenheight()
        self.mainwindow.geometry("%dx%d" % (screen_width, screen_height))

        # create main frames
        self.img_frame =   Frame(self.mainwindow, bg='cyan')
        code_frm = ttk.Notebook(self.mainwindow)
        self.script_editor = ScriptEditorFrame(self.mainwindow)
        self.filter_list = FilterList(self.mainwindow)
        code_frm.add(self.script_editor, text="Script")
        code_frm.add(self.filter_list, text="Filters")
        fx_frm = FilterAdderFrame(self.mainwindow, self.filter_list)
        other_frm = Frame(fx_frm, bg='magenta')

        # Give 2/3 of row space and 2/3 of column space to image layout
        self.mainwindow.rowconfigure(2)
        self.mainwindow.columnconfigure(2)
        self.mainwindow.grid_rowconfigure(0, weight=4)
        self.mainwindow.grid_rowconfigure(1, weight=1)
        self.mainwindow.grid_columnconfigure(0, weight=2)
        self.mainwindow.grid_columnconfigure(1, weight=1)

        self.img_frame.grid(row=0, column=0, sticky="nsew")
        code_frm.grid(row=0, column=1, sticky="nsew")
        fx_frm.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=50, pady=50)
        other_frm.pack(side=RIGHT)

        # put elements in other frame
        #self.script_name = StringVar(fx_frm, "not ImJo")
        #self.l = Label(fx_frm, textvariable=self.script_name).grid(column=0, row=3)

        ttk.Button(other_frm, text="Run", command=self.run_command).grid(column=0, row=0)
        ttk.Button(other_frm, text="Save", command=self.save_img).grid(column=0, row=1)
        ttk.Button(other_frm, text="Select Script", command=self.get_script).grid(column=0, row=2)


        # create a canvas for image
        self.img_frame.update()
        self.image = Image.open(self.img_filename)
        self.imwidth  = self.image.width
        self.imheight = self.image.height
        
        self.img_frame.update()
        imfrmwidth =  self.img_frame.winfo_width()
        imfrmheight = self.img_frame.winfo_height()

        # find which one constricts the image, using a fixed aspect ratio
        # if the frame is wider than the image, constrict by height
        if(imfrmwidth/imfrmheight > self.imwidth/self.imheight):
            self.imwidth = int(self.imwidth * imfrmheight/self.imheight)
            self.imheight = imfrmheight
        else:
            self.imheight = int(self.imheight * imfrmwidth/self.imwidth)
            self.imwidth = imfrmwidth

        self.img_canv = Canvas(self.img_frame, bg='darkgray')
        self.img_canv.image = ImageTk.PhotoImage(self.image.resize((self.imwidth, self.imheight), Image.ANTIALIAS), master=self.img_canv)
        self.img_canv.create_image(0, 0, image=self.img_canv.image, anchor='nw')
        self.img_canv.pack(side=TOP, fill=BOTH, expand=1)

        print(imfrmwidth, imfrmheight)
        print(self.imwidth, self.imheight)



        self.mainwindow.title("dijon")

    def get_script(self):
        self.script_name.set(askopenfilename())


    def save_img(self):
        pass

    def run_command(self):
        self.image = run_custom_before("./test.py", self.image)
        self.image = run_custom_after("./test.py", self.image)
        self.img_canv.image = ImageTk.PhotoImage(self.image.resize((self.imwidth, self.imheight), Image.ANTIALIAS), master=self.img_canv)
        self.img_canv.create_image(0, 0, image=self.img_canv.image, anchor='nw')