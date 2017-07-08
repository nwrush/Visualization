# Nikko Rush
# 7/5/2017

import math

from matplotlib.figure import Figure
import matplotlib.colors as colors
import numpy as np
import tkinter as tk

from MatplotlibFrame import MatplotlibFrame

class PMIPlot(MatplotlibFrame):

    def __init__(self, master, time_series_plot, pmi, ts_correlation, idea_names, ts_matrix):
        super(PMIPlot, self).__init__(Figure(), master=master)

        self.pack_canvas(side=tk.LEFT)
        #self.pack_frame(side=tk.LEFT, expand=1)
        self.grid_frame(row=0, column=1, sticky="WE")

        self.pmi = pmi
        self.ts_correlation = ts_correlation
        self.time_series_plot = time_series_plot
        self.idea_names = idea_names
        self.ts_matrix = ts_matrix
        self.num_ideas = len(idea_names)

        self.plot_data = None
        self.idea_indexes = None
        self.x_values = None
        self.y_values = None

        # TODO: Allow these to be set dynamically
        self.point_color = "Pink"
        self.selected_color = "Red"

        self._prev_selected_ind = None

        self._init_handlers()

    def _init_plot__(self):
        """Reset the axes for plotting"""
        self.axes.clear()
        self.axes.set_title("PMI vs. Cooccurrence")
        self.axes.set_xlabel("Prevalence Correlation")
        self.axes.set_ylabel("Cooccurrence")
        self.axes.set_xlim([-1.0, 1.0])

    def plot(self, sample=None):
        # Generate a list of all strictly upper triangular indexes
        points = []
        for i in range(0, self.num_ideas):
            for j in range(i+1, self.num_ideas):
                points.append((i,j))

        self._plot(points, sample)

    def _plot(self, points, sample=None):

        if sample is not None  and isinstance(sample, int):
            if 0 < sample and sample < len(points):
                indexes = np.random.choice(len(points), sample, replace=False)
                points = [points[i] for i in indexes]
                assert len(points) == sample

        xs, ys = [], []
        for i, j in points:
            if np.isnan(self.pmi[i, j]) or np.isnan(self.ts_correlation[i, j]):
                continue
            if np.isinf(self.pmi[i, j]) or np.isinf(self.ts_correlation[i, j]):
                continue

            xs.append(self.ts_correlation[i, j])
            ys.append(self.pmi[i, j])

        c = [self.point_color] * len(xs)

        self._init_plot__()
        plot = self.axes.scatter(xs, ys, color=c, picker=True)

        self.plot_data = plot
        self.idea_indexes = points
        self.x_values = xs
        self.y_values = ys

    def _init_handlers(self):
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('pick_event', self.on_select)

    def on_click(self, event):
        pass

    def on_select(self, event):
        ind = event.ind[0]

        if self._prev_selected_ind is not None:
            self.plot_data._facecolors[self._prev_selected_ind] = colors.to_rgba(self.point_color)
            self.plot_data._edgecolors[self._prev_selected_ind] = colors.to_rgba(self.point_color)

        if self._prev_selected_ind == ind:
            self.plot_data._facecolors[self._prev_selected_ind] = colors.to_rgba(self.point_color)
            self.plot_data._edgecolors[self._prev_selected_ind] = colors.to_rgba(self.point_color)
            self._prev_selected_ind = None

            self.time_series_plot.clear()
        else:
            self.plot_data._facecolors[ind] = colors.to_rgba(self.selected_color)
            self.plot_data._edgecolors[ind] = colors.to_rgba(self.selected_color)
            self._prev_selected_ind = ind

            self.set_time_series(ind)

        self.redraw()


    def set_time_series(self, index):
        i, j = self.idea_indexes[index]
        #row, col = get_row_col(self.ts_matrix.shape[0], index) TODO: Remove this if the correlation coef is correct
        row = i
        col = j

        self.time_series_plot.clear()
        self.time_series_plot.plot_series2(self.ts_matrix[row], self.ts_matrix[col], (self.idea_names[row], self.idea_names[col]))

        self.time_series_plot.get_correlation()

    def filter_by_selected(self, event, idea_numbers):
        widget = event.widget
        selecteditems = widget.curselection()

        selected_names = [widget.get(index) for index in selecteditems]
        idea_indexes = [idea_numbers[name] for name in selected_names]

        old_point = None
        if self._prev_selected_ind is not None:
            old_point = self.idea_indexes[self._prev_selected_ind]
        # You want to plot everything in both the rows and columns specified by idea_indexes
        # Take two passes over the matrixes
        points = set()
        for i in idea_indexes: # Row
            for j in range(i+1, self.num_ideas): # Col
                points.add((i,j))

        for j in idea_indexes:
            for i in range(0, j):
                points.add((i,j))

        self._plot(list(points))

        if old_point is not None:
            self._prev_selected_ind = None
            if old_point in self.idea_indexes:
                new_index = self.idea_indexes.index(old_point)
                self.on_select(type('',(object,),{"ind": [new_index]})())

        self.redraw()

    def filter_relation(self, event, idea_numbers):
        widget = event.widget
        selecteditems = widget.curselection()

        tmp = [widget.get(index) for index in selecteditems]
        idea_indexes = []
        for item in tmp:
            parts = item.split('|')
            idea_indexes.append(idea_numbers[parts[1].strip()])
            idea_indexes.append(idea_numbers[parts[2].strip()])

        old_point = None
        if self._prev_selected_ind is not None:
            old_point = self.idea_indexes[self._prev_selected_ind]
        # You want to plot everything in both the rows and columns specified by idea_indexes
        # Take two passes over the matrixes
        points = set()
        for i in idea_indexes:  # Row
            for j in range(i + 1, self.num_ideas):  # Col
                points.add((i, j))

        for j in idea_indexes:
            for i in range(0, j):
                points.add((i, j))

        self._plot(list(points))

        if old_point is not None:
            self._prev_selected_ind = None
            if old_point in self.idea_indexes:
                new_index = self.idea_indexes.index(old_point)
                self.on_select(type('', (object,), {"ind": [new_index]})())

        self.redraw()



def get_row_col(n, i):
    """
    Given the index of a data point of an nxn strictly upper triangular matrix (a_ij = 0 for i>=j),
    this will calculate the row and column indexes in the nxn matrix
    """
    row = n - 2 - math.floor(math.sqrt(-8 * i + 4 * n * (n - 1) - 7) / 2 - 0.5)
    col = i + row + 1 - n * (n - 1) / 2 + (n - row) * ((n - row) - 1) / 2
    return int(row), int(col)
