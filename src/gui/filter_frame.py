from tkinter import ttk

from ..img_proc import filters

class FilterFrame(ttk.Frame):
    def __init__(self, master, filter, filter_list):
        super().__init__(master)
        self.filter_list = filter_list
        self.filter = filter
        self.columnconfigure(2)
        name_label = ttk.Label(master=self, text=filter.name)
        name_label.grid(row=0, column=0, columnspan=2)
        self.params = {}
        for i, key in enumerate(filter.params):
            param_name_label = ttk.Label(master=self, text=key)
            param_name_label.grid(row=i+1, column=0)
            self.params[key] = ttk.Entry(master=self, width=5)
            self.params[key].grid(row=i+1, column=1)

        self.add_button = ttk.Button(master=self, text="Add", command=self.add_button_command)
        self.add_button.grid(row=len(filter.params)+1, column=0, columnspan=2)

    def add_button_command(self):
        self.filter_list.objects.append(self.filter(**{key: float(value.get()) for key, value in self.params.items()}))
        self.filter_list.update_self()
        