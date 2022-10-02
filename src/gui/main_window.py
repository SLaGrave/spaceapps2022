from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from turtle import update
from PIL import ImageTk, Image


class MainWindow:
    """Primary window for ImJo Editor."""
    def __init__(self, img_filename):
        self.mainwindow = Tk()
        # self.mainwindow.resizable(False, False)
        self.img_filename = img_filename

        # center on the screen
        screen_width = self.mainwindow.winfo_screenwidth()
        screen_height = self.mainwindow.winfo_screenheight()
        self.mainwindow.geometry("%dx%d" % (screen_width, screen_height))

        # create main frames
        img_frm =   Frame(self.mainwindow, bg='cyan')
        code_frm =  Frame(self.mainwindow, bg='green')
        fx_frm =    Frame(self.mainwindow, bg='yellow')
        other_frm = Frame(self.mainwindow, bg='magenta')

        # Give 2/3 of row space and 2/3 of column space to image layout
        self.mainwindow.grid_rowconfigure(0, weight=2)
        self.mainwindow.grid_rowconfigure(1, weight=1)
        self.mainwindow.grid_columnconfigure(0, weight=2)
        self.mainwindow.grid_columnconfigure(1, weight=1)
        

        img_frm.grid(row=0, column=0, sticky="nsew")
        code_frm.grid(row=0, column=1, sticky="nsew")
        fx_frm.grid(row=1, column=0, sticky="nsew")
        other_frm.grid(row=1, column=1, sticky="nsew")



        # === CODE FRAME ===
        # create a canvas
        scroll_canvas = Canvas(code_frm)
        scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # add a scrollbar

        # configure canvas with scrollbar

        # create a frame inside the canvas
        # 

        #

        # for thing in range(0, 100):
        #     Button(code_frm, text=f'Button {thing} Yo!').grid(row=thing,column=0, pady=10, padx=10)

        # === \CODE FRAME === 


        # put elements in other frame
        self.script_name = StringVar(fx_frm, "not ImJo")
        self.l = Label(fx_frm, textvariable=self.script_name).grid(column=0, row=3)

        ttk.Button(other_frm, text="Run", command=self.mainwindow.destroy).grid(column=0, row=0)
        ttk.Button(other_frm, text="Save", command=self.save_img).grid(column=0, row=1)
        ttk.Button(other_frm, text="Select Script", command=self.get_script).grid(column=0, row=2)


        # create a canvas for image
        img_frm.update()
        image = Image.open(self.img_filename)
        imwidth  = image.width
        imheight = image.height
        
        img_frm.update()
        imfrmwidth =  img_frm.winfo_width()
        imfrmheight = img_frm.winfo_height()

        # find which one constricts the image, using a fixed aspect ratio
        # if the frame is wider than the image, constrict by height
        if(imfrmwidth/imfrmheight > imwidth/imheight):
            imwidth = int(imwidth * imfrmheight/imheight)
            imheight = imfrmheight
        else:
            imheight = int(imheight * imfrmwidth/imwidth)
            imwidth = imfrmwidth

        img_canv = Canvas(img_frm, bg='darkgray')
        img_canv.image = ImageTk.PhotoImage(image.resize((imwidth, imheight), Image.ANTIALIAS))
        img_canv.create_image(0, 0, image=img_canv.image, anchor='nw')
        img_canv.pack(side=TOP, fill=BOTH, expand=1)

        print(imfrmwidth, imfrmheight)
        print(imwidth, imheight)



        self.mainwindow.title(self.script_name.get())

    def get_script(self):
        self.script_name.set(askopenfilename())


    def save_img(self):
        pass

    def main_window(self):
        """Initialize the GUI and start the loop."""
        

        self.mainwindow.mainloop()