# Nikko Rush
# 7/2/2017

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from frames.VisualizerFrame import VisualizerFrame

class QMatplotlib(FigureCanvasQTAgg):
    """Frame specifically for displaying matplotlib graphs"""

    def __init__(self, figure=None, parent=None):
        self._figure = Figure(figsize=(6,5)) if figure is None else figure
        self._axes = self._figure.gca()

        super(QMatplotlib, self).__init__(self._figure)
        self.setParent(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.updateGeometry()

        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        self._allow_redraw = True
        self._redraw_requested = False

    @property
    def axes(self):
        return self._axes

    @property
    def canvas(self):
        return self._figure.canvas

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