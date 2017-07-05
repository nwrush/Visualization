# Nikko Rush
# 7/2/2017

import tkinter as tk

class Frame(object):
    def __init__(self, master=None):
        self.frame = tk.Frame(master=master)

        self.frame.pack()

