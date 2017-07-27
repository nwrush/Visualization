# Nikko Rush
# 7/2/2017

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from frames.VisualizerFrame import VisualizerFrame

class MatplotlibFrame(VisualizerFrame):
    """Frame specifically for displaying matplotlib graphs"""

    def __init__(self, figure, master=None, data_manager=None):
        super(MatplotlibFrame, self).__init__(master=master, data_manager=data_manager)

        """Creates a canvas that can contains the given matplotlib figure, rooted to the given master or a new root if None"""
        self.canvas = FigureCanvasTkAgg(figure, master=self.frame)

        self.figure = figure
        self.axes = figure.gca()

        self._allow_redraw = True
        self._redraw_requested = False

    def pack_canvas(self, **kwargs):
        self.canvas.get_tk_widget().pack(**kwargs)
    def grid_canvas(self, **kwargs):
        self.canvas.get_tk_widget().grid(**kwargs)

    def redraw(self):
        if self._allow_redraw:
            self.canvas.draw()
        else:
            self._redraw_requested = True

    def allow_redraw(self):
        self._allow_redraw = True
        if self._redraw_requested:
            self.redraw()

    def prevent_redraw(self):
        self._allow_redraw = False
        self._redraw_requested = False