# Nikko Rush
# 7/2/2017

import tkinter as tk

class VisualizerFrame(object):
    """Abstract class, please don't instantiate"""
    def __init__(self, master=None, data_manager=None):
        self.frame = tk.Frame(master=master)
        self.data = data_manager

    def pack_frame(self, **kwargs):
        self.frame.pack(**kwargs)

    def grid_frame(self, **kwargs):
        self.frame.grid(**kwargs)

    def display_frame(self, manager, **kwargs):
        if manager == "grid":
            return self.grid_frame(**kwargs)
        elif manager == "pack":
            return self.pack_frame(**kwargs)
        else:
            print("Invalid geometry manager")
        return None

