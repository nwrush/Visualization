# Nikko Rush
# 7/5/2017

import numpy as np
import PyQt5.QtWidgets as QtWidgets

from frames.VisualizerFrame import VisualizerFrame
from frames.MatplotlibFrame import QMatplotlib
from frames.matplotlib_util import Utils


import matplotlib.patches as mpatches


class TimeSeriesFrame(VisualizerFrame, Utils):
    def __init__(self, parent, data):
        super(TimeSeriesFrame, self).__init__(parent=parent, data_manager=data)

        self.layout = QtWidgets.QVBoxLayout(self)

        self._mpl = QMatplotlib(parent=self)
        self.axes = self._mpl.axes

        self.layout.addWidget(self._mpl)

        self.data = data

        self._init_plot()

        self.series = None
        self._has_data = False

    def _init_plot(self):
        self.axes.clear()
        self._has_data = False
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

        self._has_data = True

    def plot_idea_indexes_event(self, event):
        self.plot_idea_indexes(event.selected_indexes)

    def plot_idea_indexes(self, indexes, names=None):
        self.clear()

        index_names = []
        for index in indexes:
            self.plot_series(self.data.ts_matrix[index], redraw=False)
            index_names.append(self.data.get_display_idea_names(index))

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
        self._correlation_data.set(round(correlation[0, 1], 5))

    def clear(self):
        self.series = None
        self._init_plot()
        self._mpl.redraw()

        # self._correlation_data.set(0)

    def select_relation_type(self, event):
        self.plot_idea_indexes(event.selected_indexes)
