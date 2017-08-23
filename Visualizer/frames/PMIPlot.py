# Nikko Rush
# 7/5/2017

import math

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui

import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np

import colors as visualizer_colors
from events import listener
from frames.MatplotlibFrame import QMatplotlib
from frames.VisualizerFrame import VisualizerFrame
from ui import pmi_control_panel_vert
from frames.matplotlib_util import Utils


def get_axis_limits(x_data, y_data):
    return


class PMIPlot(VisualizerFrame, Utils):
    def __init__(self, parent, data):
        super(PMIPlot, self).__init__(parent=parent, data_manager=data)

        self.layout = QtWidgets.QHBoxLayout(self)

        self._mpl_container = QtWidgets.QWidget(self)
        self._mpl_layout = QtWidgets.QHBoxLayout(self._mpl_container)
        self._old_mpl_width = self._mpl_container.width()

        self._mpl = QMatplotlib(parent=self._mpl_container)
        self._mpl_layout.addWidget(self._mpl)
        self._mpl.prevent_redraw()

        self.layout.addWidget(self._mpl_container)

        self.axes = self._mpl.axes
        self.canvas = self._mpl.canvas

        self._x_lim = [np.amin(data.ts_correlation), np.amax(data.ts_correlation)]
        self._y_lim = [np.amin(data.pmi), np.amax(data.pmi)]

        self._control_panel = QtWidgets.QWidget(self)
        self._control_panel_ui = pmi_control_panel_vert.Ui_pmi_control_panel()
        self._control_panel_ui.setupUi(self._control_panel)
        self.layout.addWidget(self._control_panel)

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
        self._prev_annotation = None

        self._on_select_listener = listener.Listener(self._change_selected_color, self._annotate_selected)
        self._on_reset_listener = listener.Listener(self._reset_graph)
        self._on_color_changed_listener = listener.Listener()

        self.on_select_clear_listener = listener.Listener(self._clear_selection)

        self._normalizer = colors.Normalize(vmin=0, vmax=1, clip=True)
        self._update_colors(self._colors)
        self.add_color_changed_listener(self._color_plot)

        self._setup_control_panel()

        self._mpl.allow_redraw()

    def resizeEvent(self, eve):
        super(PMIPlot, self).resizeEvent(eve)
        if eve.oldSize().width() == -1 or eve.oldSize().height() == -1:
            self._old_mpl_width = self._mpl_container.width()
            return

        # self._mpl.grow_plot(self._mpl_container.width()-self._old_mpl_width)
        self._mpl.set_plot_size(self._mpl_container.width())

    def _setup_control_panel(self):
        # self._gear_icon = images.load_image("gear-2-16.gif")
        control_panel_ui = self._control_panel_ui
        control_panel_ui.resetButton.clicked.connect(self._on_reset)

        self._color_legend()

    def _color_legend(self):
        for name in self.data.relation_types:
            label_name = name.lower().replace('-', '') + "Label"
            label = self._control_panel_ui.colorLabels.findChild(QtWidgets.QLabel, label_name)

            color = self.color_samples[name]

            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Window, QtGui.QColor(*color))
            label.setPalette(palette)

    def _init_plot_(self):
        """Reset the axes for plotting"""
        self.axes.clear()
        self.axes.set_title("PMI vs. Cooccurrence")
        self.axes.set_xlabel("Prevalence Correlation")
        self.axes.set_ylabel("Cooccurrence")
        self.axes.set_xlim(self._x_lim)
        self.axes.set_ylim(self._y_lim)

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
            r, g, b, a = mapper.to_rgba(0.7, bytes=True)
            self.color_samples[name] = (r, g, b, a)

        self._on_color_changed()
        self._mpl.redraw()

    def plot(self, sample=None):
        # Generate a list of all strictly upper triangular indexes
        self.sample_size = sample
        points = []
        for i in range(0, self.data.num_ideas):
            for j in range(i + 1, self.data.num_ideas):
                points.append((i, j))

        self._plot(points, sample)

    def _plot(self, points, sample=None):

        if sample is not None and isinstance(sample, int):
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
            distance = math.sqrt(x ** 2 + y ** 2)
            if x >= 0 and y >= 0:  # First quadrant, someone has to select zero
                colors.append(self.color_mappers[0].to_rgba(distance))
            elif x < 0 and y > 0:  # Second quadrant
                colors.append(self.color_mappers[1].to_rgba(distance))
            elif x < 0 and y < 0:  # Third quadrant
                colors.append(self.color_mappers[2].to_rgba(distance))
            elif x > 0 and y < 0:  # Fourth quadrant
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

    def _change_selected_color(self, eve):

        ind = self._get_point_index_from_event(eve)

        if self._prev_selected_ind == ind:
            return None

        if self._prev_selected_ind is not None:
            self.plot_data._edgecolors[self._prev_selected_ind] = self._point_colors[self._prev_selected_ind]

        self.plot_data._edgecolors[ind] = colors.to_rgba(self.selected_color)
        self._prev_selected_ind = ind

        self._mpl.redraw()

    def _annotate_selected(self, eve):
        ind = self._get_point_index_from_event(eve)

        if self._prev_annotation is not None:
            self._clear_selection()

        topic_1_name, topic_2_name = self.data.get_display_idea_names(self.idea_indexes[ind])

        x_cord, y_cord = self.x_values[ind], self.y_values[ind]
        text = "({0},\n{1})".format(topic_1_name, topic_2_name)
        print(text)
        offset = 0
        if x_cord > 0:
            offset = self._get_text_offset(text)

        self._prev_annotation = self.axes.annotate(s=text, xy=(self.x_values[ind] - offset, self.y_values[ind]),
                                                   annotation_clip=False)
        print((self.x_values[ind] - offset, self.y_values[ind]))
        self._mpl.redraw()

    def _get_text_offset(self, text):
        text_width = self._get_text_width(text)

        dis_data_trans = self.axes.transData.inverted()
        disp_pnt_1 = (0, 0)
        disp_pnt_2 = (text_width, 0)

        data_pnt_1, data_pnt_2 = dis_data_trans.transform([disp_pnt_1, disp_pnt_2])
        return data_pnt_2[0] - data_pnt_1[0]

    def _get_text_width(self, text):
        t = self.axes.text(0, 0, text)
        bb = t.get_window_extent(renderer=self._mpl.figure.canvas.get_renderer())
        width = bb.width
        t.remove()
        return width

    def _get_point_index_from_event(self, eve):
        if hasattr(eve, "ind"):
            return eve.ind[0]
        elif hasattr(eve, "selected_indexes"):
            a, b = tuple(eve.selected_indexes)
            if (a, b) in self.idea_indexes:
                return self.idea_indexes.index((a, b))
            elif (b, a) in self.idea_indexes:
                return self.idea_indexes.index((b, a))
            else:
                print("Selected indexes not found on PMI graph")
                return None

    def _clear_selection(self):
        if self._prev_annotation is not None:
            self._prev_annotation.remove()
            self._prev_annotation = None

    def filter_relation(self, eve):
        idea_indexes = eve.selected_indexes

        self._clear_selection()
        self._clear_filter()

        self._add_filter([self.data.idea_names[index] for index in idea_indexes])

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

        if hasattr(eve, "should_select") and eve.should_select:
            self._on_select_listener.invoke(eve)

        self._mpl.redraw()

    def _reset_graph(self):
        self._clear_selection()
        self.plot(sample=self.sample_size)
        self._clear_filter()
        self._mpl.redraw()

    def get_colors_hex(self):
        return ["#{:02x}{:02x}{:02x}".format(*rgb) for rgb in self._colors]

    def get_colors_rgb(self):
        return self._colors

    def _add_filter(self, names):
        self._control_panel_ui.filteredList.addItems(names)

    def _clear_filter(self):
        self._control_panel_ui.filteredList.clear()


def get_row_col(n, i):
    """
    Given the index of a data point of an nxn strictly upper triangular matrix (a_ij = 0 for i>=j),
    this will calculate the row and column indexes in the nxn matrix
    """
    row = n - 2 - math.floor(math.sqrt(-8 * i + 4 * n * (n - 1) - 7) / 2 - 0.5)
    col = i + row + 1 - n * (n - 1) / 2 + (n - row) * ((n - row) - 1) / 2
    return int(row), int(col)
