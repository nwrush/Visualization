# Nikko Rush
# 7/5/2017

import math
import tkinter as tk
import tkinter.ttk as ttk

import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
from matplotlib.figure import Figure

import colors as visualizer_colors
import images
from events import listener
from frames.MatplotlibFrame import MatplotlibFrame
from menus import pmi_menu

class PMIPlot(MatplotlibFrame):

    def __init__(self, master, data):
        super(PMIPlot, self).__init__(Figure(), master=master, data_manager=data)
        self.grid_frame(row=0, column=1, sticky="WE")

        self.prevent_redraw()

        self.pack_canvas(side=tk.LEFT)

        self._control_panel = tk.Frame(master=self.frame, padx=10, pady=0)
        self._control_panel.pack(side=tk.RIGHT, expand=1, anchor=tk.N)

        self._init_handlers()

        self.plot_data = None
        self.idea_indexes = None
        self.x_values = None
        self.y_values = None
        self.sample_size = None

        # TODO: Allow these to be set dynamically
        self.selected_color = "Black"
        # Colors should be a list of four matplotlib color maps or rgb tuples
        self._colors = ["Greens",
                        "Oranges",
                        "Reds",
                        "Blues"]

        
        self._prev_selected_ind = None

        self._on_select_listener = listener.Listener(self._change_selected_color, self._add_selection)
        self._on_reset_listener = listener.Listener(self._reset_graph)
        self._on_color_changed_listener = listener.Listener()
        self.on_select_clear_listener = listener.Listener(self._clear_selection)

        self._normalizer = colors.Normalize(vmin=0, vmax=1, clip=True)
        self._update_colors(self._colors)
        self.add_color_changed_listener(self._color_plot)

        self._create_control_panel()

        self.allow_redraw()

    def _create_control_panel(self):
        self._gear_icon = images.load_image("gear-2-16.gif")
        self._settings = tk.Button(master=self._control_panel, text="Test", image=self._gear_icon, command=pmi_menu.create_factory(self))
        self._settings.pack(anchor=tk.NW)
        
        # Color Samples
        self._color_sample_frame = tk.Frame(master=self._control_panel, borderwidth=2, relief=tk.RIDGE)
        self._color_sample_frame.pack(side=tk.TOP, expand=1, fill=tk.X, anchor=tk.N, pady=10)

        label = tk.Label(master=self._color_sample_frame, text="Legend:")
        label.pack(side=tk.TOP, expand=1, fill=tk.X, padx=2, pady=2)

        sample_labels = dict()
        for mapper, name in zip(self.color_mappers, self.data.relation_types):
            sample = tk.Label(master=self._color_sample_frame, background=self.color_samples[name], text=name)
            sample.pack(side=tk.TOP, expand=1, fill=tk.X, padx=2)
            sample_labels[name] = sample

        def recolor_labels():
            for name, sample in sample_labels.items():
                sample['background']=self.color_samples[name]

        self.add_color_changed_listener(recolor_labels)
        
        self._reset_graph_btn = tk.Button(master=self._control_panel, text="Reset Graph", command=self._on_reset)
        self._reset_graph_btn.pack(side=tk.TOP, pady=10)
        
        self._filter_by_header = tk.Label(master=self._control_panel, text="Filtered by: ")
        self._filter_by_header.pack(side=tk.TOP)
        self._filter_by_data = tk.StringVar()
        self._filter_by_label = tk.Label(master=self._control_panel, textvariable=self._filter_by_data, justify=tk.LEFT)
        self._filter_by_label.pack(side=tk.TOP)

        self._seperator = ttk.Separator(master=self._control_panel, orient=tk.HORIZONTAL)
        self._seperator.pack(side=tk.TOP, expand=1, fill=tk.X, pady=(5,10))
        
        self._selected_header = tk.Label(master=self._control_panel, text="Selected Relations: ")
        self._selected_header.pack(side=tk.TOP)
        self._selected_data = tk.StringVar()
        self._selected_label = tk.Label(master=self._control_panel, textvariable=self._selected_data, justify=tk.LEFT)
        self._selected_label.pack(side=tk.TOP)

    def _init_plot_(self):
        """Reset the axes for plotting"""
        self.axes.clear()
        self.axes.set_title("PMI vs. Cooccurrence")
        self.axes.set_xlabel("Prevalence Correlation")
        self.axes.set_ylabel("Cooccurrence")
        self.axes.set_xlim([-1.0, 1.0])

    def _update_colors(self, color_spec):
        """
        Takes a sequence of 4 color tuples, builds the color maps, if
        the plot data isn't none will modify the plot colors
        """
        
        self._colors = color_spec

        self._color_maps = [visualizer_colors.PMIColormap("PMIFriend", color_spec[0]),
                            visualizer_colors.PMIColormap("PMITryst", color_spec[1]),
                            visualizer_colors.PMIColormap("PMIHeadToHead", color_spec[2]),
                            visualizer_colors.PMIColormap("PMIArmsRace", color_spec[3])]

        self.color_mappers = [cm.ScalarMappable(norm=self._normalizer, cmap=self._color_maps[0]),
                              cm.ScalarMappable(norm=self._normalizer, cmap=self._color_maps[1]),
                              cm.ScalarMappable(norm=self._normalizer, cmap=self._color_maps[2]),
                              cm.ScalarMappable(norm=self._normalizer, cmap=self._color_maps[3])]

        self.color_samples = dict()
        for mapper, name in zip(self.color_mappers, self.data.relation_types):
            r,g,b,a = mapper.to_rgba(0.7, bytes=True)
            hex = "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
            self.color_samples[name] = hex

        self._on_color_changed()
        self.redraw()

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

        self._init_plot_()
        self.plot_data = self.axes.scatter(xs, ys, picker=True)

        self.idea_indexes = points
        self.x_values = xs
        self.y_values = ys

        self._color_plot()

    def _color_plot(self):
        colors = []
        for x, y in zip(self.x_values, self.y_values):
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
        self.plot_data.set_color(colors)
        self._point_colors = colors

    def _init_handlers(self):
        self.canvas.mpl_connect('button_press_event', self._on_click)
        self.canvas.mpl_connect('pick_event', self._on_select)

    def _on_click(self, event):
        pass

    # Event listener functions
    def add_select_listener(self, func):
        self._on_select_listener.add(func)

    def has_select_listener(self, func):
        return self._on_select_listener.has_handler(func)

    def remove_select_listener(self, func):
        self._on_select_listener.remove(func)

    def add_reset_listener(self, func):
        self._on_reset_listener.add(func)

    def has_reset_listener(self, func):
        return self._on_reset_listener.has_handler(func)

    def remove_reset_listener(self, func):
        self._on_reset_listener.remove(func)

    def add_color_changed_listener(self, func):
        self._on_color_changed_listener.add(func)

    def has_color_changed_listener(self, func):
        return self._on_color_changed_listener.has_handler(func)

    def remove_color_changed_listener(self, func):
        self._on_color_changed_listener.remove(func)

    def _on_select(self, event):
        i, j = self.idea_indexes[event.ind[0]]
        event.selected_indexes = (i, j)
        self._on_select_listener.invoke(event)

    def _on_reset(self):
        self._on_reset_listener.invoke_empty()

    def _on_color_changed(self):
        self._on_color_changed_listener.invoke_empty()

    def _change_selected_color(self, event):
        
        if hasattr(event, "ind"):
            ind = event.ind[0]
        elif hasattr(event, "selected_indexes"):
            ind = self.idea_indexes.index(tuple(event.selected_indexes))

        if self._prev_selected_ind == ind:
            return None

        if self._prev_selected_ind is not None:
            self.plot_data._edgecolors[self._prev_selected_ind] = self._point_colors[self._prev_selected_ind]

        self.plot_data._edgecolors[ind] = colors.to_rgba(self.selected_color)
        self._prev_selected_ind = ind

        self.redraw()

    def filter_relation(self, event):
        idea_indexes = event.selected_indexes

        self._clear_selection()

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

        if hasattr(event, "should_select") and event.should_select:
            self._on_select_listener.invoke(event)

        self.redraw()

    def _reset_graph(self):
        self.plot(sample=self.sample_size)
        self._filter_by_data.set("")
        self._selected_data.set("")
        self.redraw()

    def _add_selection(self, event):
        names = self.data.get_idea_names(event.selected_indexes)
        self._selected_data.set("\n".join(names))

    def _clear_selection(self):
        self._selected_data.set("")
    
    def get_colors_hex(self):
        return ["#{:02x}{:02x}{:02x}".format(*rgb) for rgb in self._colors]

    def get_colors_rgb(self):
        return self._colors


            
def get_row_col(n, i):
    """
    Given the index of a data point of an nxn strictly upper triangular matrix (a_ij = 0 for i>=j),
    this will calculate the row and column indexes in the nxn matrix
    """
    row = n - 2 - math.floor(math.sqrt(-8 * i + 4 * n * (n - 1) - 7) / 2 - 0.5)
    col = i + row + 1 - n * (n - 1) / 2 + (n - row) * ((n - row) - 1) / 2
    return int(row), int(col)
