# Nikko Rush
# 7/2/2017

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class MatplotlibFrame(object):
    """Frame specifically for displaying matplotlib graphs"""

    def __init__(self, figure, master=None):
        self.canvas = FigureCanvasTkAgg(figure, master)

        self.figure = figure
        self.axes = figure.gca()

    def pack(self, **args):
        self.canvas.get_tk_widget().pack(*args)
