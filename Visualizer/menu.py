# Nikko Rush
# 7/22/17

import tkinter as tk
import tkinter.filedialog as filedialog

class Menubar(tk.Menu):
    
    def __init__(self, root):
        super(Menubar, self).__init__(master=root)
       
        self.filemenu = tk.Menu(master=self, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.open)

        self.add_cascade(label="File", menu=self.filemenu)

        self._open_handlers = set()
        
    def hello(self):
        print("hello")

    def open(self):
        value = filedialog.askopenfilename(parent=self)
        for func in self._open_handlers:
            func(value)
