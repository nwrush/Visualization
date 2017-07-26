# Nikko Rush
# 7/2/2017

import tkinter as tk

class VisualizerFrame(object):
    """Abstract class, please don't instantiate"""
    def __init__(self, master=None, data_manager=None):
        self.frame = tk.Frame(master=master)
        self.data = data_manager

        self.frame.config(bd=2, relief=tk.GROOVE)

    def pack_frame(self, **kwargs):
        self.frame.pack(**kwargs)
    def grid_frame(self, **kwargs):
        self.frame.grid(**kwargs)

