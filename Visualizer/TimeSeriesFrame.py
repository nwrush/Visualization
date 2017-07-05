# Nikko Rush
# 7/5/2017

from matplotlib.figure import Figure
import tkinter as tk

from MatplotlibFrame import MatplotlibFrame

class TimeSeriesFrame(MatplotlibFrame):

    def __init__(self, master, x_vals=None):
        super(TimeSeriesFrame, self).__init__(Figure(), master=master)

        self.pack_canvas()
        self.pack_frame(side=tk.RIGHT, expand=1)

        self._x_values = x_vals

        self.__init_plot__()

        self.series = list()

    def __init_plot__(self):
        self.axes.set_title("Time Series")
        self.axes.set_xlabel("Year")
        self.axes.set_ylabel("Frequency")

    def set_x_values(self, values):
        self._x_values = values
    def get_x_values(self):
        return self._x_values

    def plot_series(self, y, name=None):
        self.series.append(y)
        self.axes.plot(self._x_values, y)
        if name is not None:
            self.axes.legend([name], loc="best")
        self.redraw()

    def plot_series2(self, y1, y2, name=None):
        self.series.append(y1)
        self.series.append(y2)
        self.axes.plot(self._x_values, y1)
        self.axes.plot(self._x_values, y2)

        if name is not None:
            assert len(name) >= 2
            self.axes.legend(name, loc="best")

        self.redraw()

    def clear(self):
        self.series = []
        self.axes.lines = []
