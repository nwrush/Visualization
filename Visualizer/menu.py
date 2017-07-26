# Nikko Rush
# 7/22/17

import tkinter as tk
import tkinter.filedialog as filedialog

from menus import pmi_menu

class Menubar(tk.Menu):
    
    def __init__(self, root, data):
        super(Menubar, self).__init__(master=root)

        self._data = data
       
        self.filemenu = tk.Menu(master=self, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.open)

        self.editmenu = tk.Menu(master=self, tearoff=0)
        self.editmenu.add_command(label="Edit PMI", command=self.edit_pmi)

        self.add_cascade(label="File", menu=self.filemenu)
        self.add_cascade(label="Edit", menu=self.editmenu)

        self._open_handlers = set()
        
    def hello(self):
        print("hello")

    def open(self):
        value = filedialog.askopenfilename(parent=self)
        for func in self._open_handlers:
            func(value)

    def edit_pmi(self):
        pmi_menu.PMIMenu(self, self._data)
