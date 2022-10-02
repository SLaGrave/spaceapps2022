from tkinter import BOTH, LEFT, RIGHT, W, Y, Button, Frame, Label, ttk, Text,Scrollbar, VERTICAL, Canvas

class FilterList(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.objects = list()

        self.canvas = Canvas(self)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.new_frame = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.new_frame, anchor="nw")
        
        self.update_self()

    def update_self(self):
        for widget in self.new_frame.winfo_children():
            widget.destroy()
        
        def magic(o):
            def magic2():
                self.objects.remove(o)
                self.update_self()
            return magic2
        self.new_frame.columnconfigure(2)
        self.new_frame.rowconfigure(len(self.objects))
        for idx, obj in enumerate(self.objects):
            Button(self.new_frame, text="-", command=magic(obj)).grid(row=idx, column=0)
            Label(self.new_frame, text=str(obj), anchor="w", justify=LEFT).grid(sticky = W, row=idx, column=1)
