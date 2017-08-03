# Nikko Rush
# 7/5/2017

import tkinter as tk
from PyQt5 import QtWidgets

import numpy as np
from matplotlib.figure import Figure

from frames.VisualizerFrame import VisualizerFrame
from frames.MatplotlibFrame import QMatplotlib


class TimeSeriesFrame(VisualizerFrame):

    def __init__(self, parent, data):
        super(TimeSeriesFrame, self).__init__(parent=parent, data_manager=data)

        self.layout = QtWidgets.QVBoxLayout(self)

        self._mpl = QMatplotlib(parent=self)
        self.axes = self._mpl.axes

        self.layout.addWidget(self._mpl)

        self.data = data

        self._init_plot()

        self.series = None

        # self._create_control_panel()

    def _create_control_panel(self):
        self._control_panel = tk.Frame(master=self.frame, padx=10, pady=20)
        self._control_panel.pack(side=tk.RIGHT, expand=1, anchor=tk.N)

        self._correlation_header = tk.Label(self._control_panel, text="Correlation:")
        self._correlation_header.pack(side=tk.TOP)

        self._correlation_data = tk.DoubleVar()

        self._correlation_label = tk.Label(self._control_panel, textvariable=self._correlation_data)
        self._correlation_label.pack(side=tk.TOP)


    def _init_plot(self):
        self.axes.clear()
        self.axes.set_title("Time Series")
        self.axes.set_xlabel("Year")
        self.axes.set_ylabel("Frequency")
        self.axes.set_ylim([0, 1])

    def plot_series(self, y, name=None, redraw=True):
        self._add_series(y)
        self.axes.plot(self.data.x_values, y)
        if name is not None:
            self.axes.legend([name], loc="best")

        if redraw:
            self.redraw()

    def plot_idea_indexes_event(self, event):
        self.plot_idea_indexes(event.selected_indexes)

    def plot_idea_indexes(self, indexes, names=None):
        self.clear()

        index_names = []
        for index in indexes:
            self.plot_series(self.data.ts_matrix[index], redraw=False)
            index_names.append(self.data.idea_names[index])

        # self.get_correlation()

        if names is not None:
            self.axes.legend(names, loc="best")
        else:
            self.axes.legend(index_names, loc="best")

        self._mpl.redraw()

    def _add_series(self, data):
        if self.series is None:
            self.series = np.copy(data)
        else:
            self.series = np.column_stack((self.series, data))

    def get_correlation(self):
        correlation = np.corrcoef(self.series, rowvar=False)
        self._correlation_data.set(round(correlation[0,1], 5))

    def clear(self):
        self.series = None
        self._init_plot()
        self._mpl.redraw()

        # self._correlation_data.set(0)

    def select_relation_type(self, event):
        self.plot_idea_indexes(event.selected_indexes)
