# Nikko Rush
# 7/5/2017

from matplotlib.figure import Figure
import numpy as np
import tkinter as tk

from MatplotlibFrame import MatplotlibFrame

class TimeSeriesFrame(MatplotlibFrame):

    def __init__(self, master, data):
        super(TimeSeriesFrame, self).__init__(Figure(), master=master, data_manager=data)

        # The canvas is the matplotlib stuff
        #self.pack_canvas()
        self.grid_canvas(row=0, column=0)
        # The frame is the root of the "widget" everything else gets placed inside of it
        #self.pack_frame(side=tk.LEFT, expand=1)
        self.grid_frame(row=0, column=3, pady=(5, 0))

        self.correlation_label = tk.Label(master=self.frame, background="red")
        self.correlation_label.grid(row=0, column=1)
        self.correlation = tk.StringVar()
        self.correlation_label['textvariable'] = self.correlation

        self.data = data

        self._init_plot()

        self.series = None

    def _init_plot(self):
        self.axes.clear()
        self.axes.set_title("Time Series")
        self.axes.set_xlabel("Year")
        self.axes.set_ylabel("Frequency")

    def plot_series(self, y, name=None, redraw=True):
        self._add_series(y)
        self.axes.plot(self.data.x_values, y)
        if name is not None:
            self.axes.legend([name], loc="best")

        if redraw:
            self.redraw()

    def plot_idea_indexes(self, indexes, names=None):
        self.clear()

        index_names = []
        for index in indexes:
            self.plot_series(self.data.ts_matrix[index], redraw=False)
            index_names.append(self.data.idea_names[index])

        self.get_correlation()

        if names is not None:
            self.axes.legend(names, loc="best")
        else:
            self.axes.legend(index_names, loc="best")

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
        self._init_plot()
        self.redraw()

        self.correlation.set("")

    def select_relation_type(self, event):
        indexes = []
        for selected in event.selected_data:
            indexes.extend(selected[:2])

        self.clear()
        self.plot_idea_indexes(indexes)
