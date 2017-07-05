# Nikko Rush
# 7/5/2017

import math

from matplotlib.figure import Figure
import matplotlib.colors as colors
import numpy as np
import tkinter as tk

from MatplotlibFrame import MatplotlibFrame

class PMIPlot(MatplotlibFrame):

    def __init__(self, master, time_series_plot, idea_names, ts_matrix):
        super(PMIPlot, self).__init__(Figure(), master=master)

        self.pack_canvas()
        self.pack_frame(side=tk.LEFT, expand=1)

        self.time_series_plot = time_series_plot
        self.idea_names = idea_names
        self.ts_matrix = ts_matrix

        self.plot_data = None
        self.x_values = None
        self.y_values = None

        # Allow these to be set dynamically
        self.point_color = "Pink"
        self.selected_color = "Red"

        self.__prev_selected_ind = None

        self.__init_plot__()
        self.__init_handlers()

    def __init_plot__(self):
        self.axes.set_title("PMI vs. Cooccurrence")
        self.axes.set_xlabel("Prevalence Correlation")
        self.axes.set_ylabel("Cooccurrence")
        self.axes.set_xlim([-1.0, 1.0])

    def plot(self, pmi, ts_correlation, sample=None):
        num_ideas = pmi.shape[0]
        xs, ys = [], []
        for i in range(num_ideas):
            for j in range(i + 1, num_ideas):
                if np.isnan(pmi[i, j]) or np.isnan(ts_correlation[i, j]):
                    continue
                if np.isinf(pmi[i, j]) or np.isinf(ts_correlation[i, j]):
                    continue
                xs.append(ts_correlation[i, j])
                ys.append(pmi[i, j])

        if sample is None or not isinstance(sample, int):
            # Don't sample from the points
            plot_x = xs
            plot_y = ys
        else:
            # Do sample
            if sample < 0 or sample > len(xs):
                sample = num_ideas
            plot_x = np.random.choice(xs, sample, replace=False)
            plot_y = np.random.choice(ys, sample, replace=False)

        c = [self.point_color] * len(plot_x)

        plot = self.axes.scatter(plot_x, plot_y, color=c, picker=True)

        self.plot_data = plot
        self.x_values = plot_x
        self.y_values = plot_y


    def __init_handlers(self):
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('pick_event', self.on_select)

    def on_click(self, event):
        pass

    def on_select(self, event):
        ind = event.ind[0]

        if self.__prev_selected_ind is not None:
            self.plot_data._facecolors[self.__prev_selected_ind] = colors.to_rgba(self.point_color)
            self.plot_data._edgecolors[self.__prev_selected_ind] = colors.to_rgba(self.point_color)

        self.plot_data._facecolors[ind] = colors.to_rgba(self.selected_color)
        self.plot_data._edgecolors[ind] = colors.to_rgba(self.selected_color)

        self.set_time_series(ind)

        self.redraw()

        self.__prev_selected_ind = ind

    def set_time_series(self, index):
        row, col = get_row_col(self.ts_matrix.shape[0], index)

        self.time_series_plot.clear()

        self.time_series_plot.plot_series(self.ts_matrix[row])
        self.time_series_plot.plot_series(self.ts_matrix[col])

        self.time_series_plot.plot_series2(self.ts_matrix[row], self.ts_matrix[col])


def get_row_col(n, i):
    """
    Given the index of a data point of an nxn strictly upper triangular matrix (a_ij = 0 for i>=j),
    this will calculate the row and column indexes in the nxn matrix
    """
    row = n - 2 - math.floor(math.sqrt(-8 * i + 4 * n * (n - 1) - 7) / 2 - 0.5)
    col = i + row + 1 - n * (n - 1) / 2 + (n - row) * ((n - row) - 1) / 2
    return int(row), int(col)
