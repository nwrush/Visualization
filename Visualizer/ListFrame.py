# Nikko Rush
# 7/6/2017

import tkinter as tk

from Frame import Frame

class ListFrame(Frame):
    """description of class"""
    def __init__(self, master):
        super(ListFrame, self).__init__(master)

        self.grid_frame(row=0,  column=0)

        self.list = tk.Listbox(master=self.frame)
        self.list.pack(side=tk.LEFT, expand=1)

        self.list.insert(tk.END, "bite me")
        

