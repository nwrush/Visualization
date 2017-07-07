# Nikko Rush
# 7/5/2017

from matplotlib.figure import Figure
import numpy as np
import tkinter as tk

from MatplotlibFrame import MatplotlibFrame

class TimeSeriesFrame(MatplotlibFrame):

    def __init__(self, master, x_vals=None):
        super(TimeSeriesFrame, self).__init__(Figure(), master=master)

        # The canvas is the matplotlib stuff
        #self.pack_canvas()
        self.grid_canvas(row=0, column=0)
        # The frame is the root of the "widget" everything else gets placed inside of it
        #self.pack_frame(side=tk.LEFT, expand=1)
        self.grid_frame(row=1, column=1, pady=(5, 0))

        self.correlation_label = tk.Label(master=self.frame, background="red")
        self.correlation_label.grid(row=0, column=1)
        self.correlation = tk.StringVar()
        self.correlation.set(str(float(0)))
        self.correlation_label['textvariable'] = self.correlation

        self._x_values = x_vals

        self.__init_plot__()

        self.series = None

        def test(event):
            self.correlation_label.grid_forget()

        self.frame.bind("<Button-1>", test)

    def __init_plot__(self):
        self.axes.set_title("Time Series")
        self.axes.set_xlabel("Year")
        self.axes.set_ylabel("Frequency")

    def set_x_values(self, values):
        self._x_values = values
    def get_x_values(self):
        return self._x_values

    def plot_series(self, y, name=None):
        self._add_series(y)
        self.axes.plot(self._x_values, y)
        if name is not None:
            self.axes.legend([name], loc="best")
        self.redraw()

    def plot_series2(self, y1, y2, name=None):
        self._add_series(y1)
        self._add_series(y2)
        self.axes.plot(self._x_values, y1)
        self.axes.plot(self._x_values, y2)

        if name is not None:
            assert len(name) >= 2
            self.axes.legend(name, loc="best")

        self.redraw()

    def _add_series(self, data):
        if self.series is None:
            self.series = np.copy(data)
        else:
            self.series = np.column_stack((self.series, data))

    def get_correlation(self):
        correlation = np.corrcoef(self.series, rowvar=False)
        self.correlation.set("Correlation = {0:.5f}".format(correlation[0,1]))

    def clear(self):
        self.series = None
        self.axes.lines = []
