# Nikko Rush
# 7/2/2017

import tkinter as tk

class Frame(object):
    """Abstract class, please don't instantiate"""
    def __init__(self, master=None):
        self.frame = tk.Frame(master=master)

    def pack_frame(self, **kwargs):
        self.frame.pack(**kwargs)
    def grid_frame(self, **kwargs):
        self.frame.grid(**kwargs)

