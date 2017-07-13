# Nikko Rush
# 7/5/2017

import math
import tkinter as tk

import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
from matplotlib.figure import Figure

from frames.MatplotlibFrame import MatplotlibFrame

class PMIPlot(MatplotlibFrame):

    def __init__(self, master, data):
        super(PMIPlot, self).__init__(Figure(), master=master, data_manager=data)
        self.grid_frame(row=0, column=1, sticky="WE")

        self.pack_canvas(side=tk.LEFT)

        self.plot_data = None
        self.idea_indexes = None
        self.x_values = None
        self.y_values = None
        self.sample_size = None

        # TODO: Allow these to be set dynamically
        self.selected_color = "Black"
        self.normalizer = colors.Normalize(vmin=0, vmax=1)
        self.color_mappers = [cm.ScalarMappable(norm=self.normalizer, cmap="Reds"),
                              cm.ScalarMappable(norm=self.normalizer, cmap="Greens"),
                              cm.ScalarMappable(norm=self.normalizer, cmap="Oranges"),
                              cm.ScalarMappable(norm=self.normalizer, cmap="Blues")]

        self._prev_selected_ind = None

        self._init_handlers()

        self._on_select_listeners = set()
        self.add_select_listener(self._change_selected_color)

        self._on_reset_listeners = set()
        self.add_reset_listener(self._reset_graph)

        self._control_panel = tk.Frame(master=self.frame, padx=10, pady=20)
        self._control_panel.pack(side=tk.RIGHT, expand=1, anchor=tk.N)

        self.color_map = dict()
        self._color_samples = self._get_color_samples(self._control_panel)

        self._reset_graph_btn = tk.Button(master=self._control_panel, text="Reset Graph", command=self._on_reset)
        self._reset_graph_btn.pack(side=tk.TOP, pady=10)

        self._filter_by_header = tk.Label(master=self._control_panel, text="Filtered by: ")
        self._filter_by_header.pack(side=tk.TOP)
        self._filter_by_data = tk.StringVar()
        self._filter_by_label = tk.Label(master=self._control_panel, textvariable=self._filter_by_data, justify=tk.LEFT)
        self._filter_by_label.pack(side=tk.TOP)

    def _init_plot__(self):
        """Reset the axes for plotting"""
        self.axes.clear()
        self.axes.set_title("PMI vs. Cooccurrence")
        self.axes.set_xlabel("Prevalence Correlation")
        self.axes.set_ylabel("Cooccurrence")
        self.axes.set_xlim([-1.0, 1.0])

    def plot(self, sample=None):
        # Generate a list of all strictly upper triangular indexes
        self.sample_size = sample
        points = []
        for i in range(0, self.data.num_ideas):
            for j in range(i+1, self.data.num_ideas):
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
            if np.isnan(self.data.pmi[i, j]) or np.isnan(self.data.ts_correlation[i, j]):
                continue
            if np.isinf(self.data.pmi[i, j]) or np.isinf(self.data.ts_correlation[i, j]):
                continue

            xs.append(self.data.ts_correlation[i, j])
            ys.append(self.data.pmi[i, j])

        self._point_colors = self._get_colors(xs, ys)
        self._init_plot__()
        plot = self.axes.scatter(xs, ys, color=self._point_colors, picker=True)

        self.plot_data = plot
        self.idea_indexes = points
        self.x_values = xs
        self.y_values = ys

    def _get_colors(self, xs, ys):
        colors = []
        for x, y in zip(xs, ys):
            distance = math.sqrt(x**2 + y**2)
            if x >= 0 and y >= 0: # First quadrant, someone has to select zero
                colors.append(self.color_mappers[0].to_rgba(distance))
            elif x < 0 and y > 0: # Second quadrant
                colors.append(self.color_mappers[1].to_rgba(distance))
            elif x < 0 and y < 0: # Third quadrant
                colors.append(self.color_mappers[2].to_rgba(distance))
            elif x > 0 and y < 0: # Fourth quadrant
                colors.append(self.color_mappers[3].to_rgba(distance))
            else:
                print("Fail")
        return colors

    def _get_color_samples(self, parent):
        frame = tk.Frame(master=parent, borderwidth=2, relief=tk.RIDGE)
        frame.pack(side=tk.TOP, expand=1, fill=tk.X, anchor=tk.N, pady=10)

        label = tk.Label(master=frame, text="Legend:")
        label.pack(side=tk.TOP, expand=1, fill=tk.X, padx=2, pady=2)

        bck_r, bck_g, bck_b = parent.winfo_rgb(parent['background'])
        bck_r /= 256
        bck_g /= 256
        bck_b /= 256
        for mapper, name in zip(self.color_mappers, self.data.relation_types):
            r, g, b, a = mapper.to_rgba(0.7, bytes=True)
            r = int(r * (a/255) + bck_r * (1 - a/255))
            g = int(g * (a / 255) + bck_g * (1 - a / 255))
            b = int(b * (a / 255) + bck_b * (1 - a / 255))
            hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
            sample = tk.Label(master=frame, background=hex_color, text=name)
            sample.pack(side=tk.TOP, expand=1, fill=tk.X, padx=2)
            self.color_map[name] = hex_color

        return frame

    def _init_handlers(self):
        self.canvas.mpl_connect('button_press_event', self._on_click)
        self.canvas.mpl_connect('pick_event', self._on_select)

    def _on_click(self, event):
        pass

    def add_select_listener(self, func):
        self._on_select_listeners.add(func)

    def has_select_listener(self, func):
        return func in self._on_select_listeners

    def remove_select_listener(self, func):
        self._on_select_listeners.discard(func)

    def add_reset_listener(self, func):
        self._on_reset_listeners.add(func)

    def has_reset_listener(self, func):
        return func in self._on_reset_listeners

    def remove_reset_listener(self, func):
        self._on_reset_listeners.discard(func)

    def _on_select(self, event):
        i, j = self.idea_indexes[event.ind[0]]
        event.selected_indexes = (i, j)
        for func in self._on_select_listeners:
            func(event)

    def _on_reset(self):
        for func in self._on_reset_listeners:
            func()

    def _change_selected_color(self, event):
        ind = event.ind[0]

        if self._prev_selected_ind is not None:
            self.plot_data._edgecolors[self._prev_selected_ind] = self._point_colors[self._prev_selected_ind]

        if self._prev_selected_ind == ind:
            self.plot_data._edgecolors[self._prev_selected_ind] = self._point_colors[self._prev_selected_ind]
            self._prev_selected_ind = None

        else:
            self.plot_data._edgecolors[ind] = colors.to_rgba(self.selected_color)
            self._prev_selected_ind = ind

        self.redraw()

    def filter_relation(self, event):
        idea_indexes = event.selected_indexes

        selected_names = [self.data.idea_names[index] for index in idea_indexes]
        self._filter_by_data.set("\n".join(selected_names))

        old_point = None
        if self._prev_selected_ind is not None:
            old_point = self.idea_indexes[self._prev_selected_ind]
        # You want to plot everything in both the rows and columns specified by idea_indexes
        # Take two passes over the matrixes
        points = set()
        for i in idea_indexes:  # Row
            for j in range(i + 1, self.data.num_ideas):  # Col
                points.add((i, j))

        for j in idea_indexes:
            for i in range(0, j):
                points.add((i, j))

        self._plot(list(points))

        if old_point is not None:
            self._prev_selected_ind = None
            if old_point in self.idea_indexes:
                new_index = self.idea_indexes.index(old_point)
                self._on_select(type('', (object,), {"ind": [new_index]})())

        self.redraw()

    def _reset_graph(self):
        self.plot(sample=self.sample_size)
        self._filter_by_data.set("")
        self.redraw()

def get_row_col(n, i):
    """
    Given the index of a data point of an nxn strictly upper triangular matrix (a_ij = 0 for i>=j),
    this will calculate the row and column indexes in the nxn matrix
    """
    row = n - 2 - math.floor(math.sqrt(-8 * i + 4 * n * (n - 1) - 7) / 2 - 0.5)
    col = i + row + 1 - n * (n - 1) / 2 + (n - row) * ((n - row) - 1) / 2
    return int(row), int(col)
