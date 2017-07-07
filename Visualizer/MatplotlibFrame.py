# Nikko Rush
# 7/2/2017

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from VisualizerFrame import VisualizerFrame

class MatplotlibFrame(VisualizerFrame):
    """Frame specifically for displaying matplotlib graphs"""

    def __init__(self, figure, master=None):
        super(MatplotlibFrame, self).__init__(master=master)

        """Creates a canvas that can contains the given matplotlib figure, rooted to the given master or a new root if None"""
        self.canvas = FigureCanvasTkAgg(figure, master=self.frame)

        self.figure = figure
        self.axes = figure.gca()

    def pack_canvas(self, **kwargs):
        self.canvas.get_tk_widget().pack(**kwargs)
    def grid_canvas(self, **kwargs):
        self.canvas.get_tk_widget().grid(**kwargs)

    def redraw(self):
        self.canvas.draw()
