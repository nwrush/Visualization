# Nikko Rush
# 7/2/2017

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class MatplotlibFrame(object):
    """Frame specifically for displaying matplotlib graphs"""

    def __init__(self, figure, master=None):
        self.frame = tk.Frame(master=master)
        """Creates a canvas that can contains the given matplotlib figure, rooted to the given master or a new root if None"""
        self.canvas = FigureCanvasTkAgg(figure, master=self.frame)

        self.figure = figure
        self.axes = figure.gca()

    def pack_canvas(self, **kwargs):
        self.canvas.get_tk_widget().pack(**kwargs)

    def pack_frame(self, **kwargs):
        self.frame.pack(**kwargs)

    def redraw(self):
        self.canvas.draw()
