# Nikko Rush
# 7/2/2017

import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class QMatplotlib(FigureCanvasQTAgg):
    """Frame specifically for displaying matplotlib graphs"""

    def __init__(self, figure=None, parent=None, width=None, height=None, dpi=None):

        if figure is not None:
            self._figure = figure
        else:
            if width or height or dpi is None:
                self._figure = Figure()
            else:
                self._figure = Figure(figsize=(width, height), dpi=dpi)

        self._axes = self._figure.gca()

        super(QMatplotlib, self).__init__(self._figure)
        self.setParent(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self._set_size()
        self.updateGeometry()

        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        self._allow_redraw = True
        self._redraw_requested = False

    def _set_size(self):
        fig_w, fig_h = map(int, self._figure.get_size_inches() * self._figure.dpi)
        self.setMaximumSize(fig_w, fig_h)
        self.setMinimumSize(fig_w, fig_h)

    @property
    def axes(self):
        return self._axes

    @property
    def canvas(self):
        return self._figure.canvas

    def get_figure(self):
        return self._figure

    def redraw(self):
        if self._allow_redraw:
            self.draw()
        else:
            self._redraw_requested = True

    def allow_redraw(self):
        self._allow_redraw = True
        if self._redraw_requested:
            self.redraw()

    def prevent_redraw(self):
        self._allow_redraw = False
        self._redraw_requested = False

    def grow_plot(self, delta):
        size = self.figure.get_size_inches()
        size[0] = size[0] + delta/self.figure.dpi
        self.figure.set_size_inches(size)
        # self._set_size()
        # self.updateGeometry()
        self.redraw()

    def set_plot_size(self, width):
        size = self.figure.get_size_inches()
        size[0] = width/self.figure.dpi
        self.figure.set_size_inches(size)
