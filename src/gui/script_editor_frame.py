from tkinter import ttk, Text, filedialog, Toplevel, Label

class ScriptEditorFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.text_editor = Text(self, height=20)
        self.rowconfigure(index=2)
        self.columnconfigure(index=2)
        self.text_editor.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.save_script_button = ttk.Button(self, text="Save Script", command=self.open_directory)
        self.save_script_button.grid(row=1, column=0)
        self.load_script_button = ttk.Button(self, text="Load Script", command=self.load_script)
        self.load_script_button.grid(row=1, column=1)
        self.filepath = ""
        self.name_entry = None
        self.ask_name_frame = None

    def open_directory(self):
        """
        Opens a filedialog to save the entire script to
        """
        self.filepath = filedialog.askdirectory(title="Save Script")
        
        self.ask_name_frame = Toplevel(master=self)
        Label(master=self.ask_name_frame, text="Enter a name for your script").grid(row=0, column=0)
        self.name_entry = ttk.Entry(master=self.ask_name_frame)
        self.name_entry.grid(row=1, column=0)
        save_button = ttk.Button(master=self.ask_name_frame, text="Save", command=self.save_script)
        save_button.grid(row=1, column=1)

    def save_script(self):
        """
        CALL OPEN_DIRECTORY INSTEAD OF THIS
        Saves the script given the filepath and name
        """
        with open(f"{self.filepath}/{self.name_entry.get()}.py", "w") as f:
            f.write(self.get_script())
        self.ask_name_frame.destroy()

    def load_script(self):
        """
        Opens a filedialog to open a script and populate the script editor
        """
        filetypes = (
            ('python scripts', '*.py'),
        )
        file = filedialog.askopenfile(title="Load Script", filetypes=filetypes)
        self.text_editor.delete("1.0", "end")
        self.text_editor.insert("1.0", file.read())
    
    def get_script(self) -> str:
        """
        Returns
        -------
        `str` of the entire script editor
        """
        return self.text_editor.get("1.0", "end")