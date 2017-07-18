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

    def pack_canvas(self, **kwargs):
        self.canvas.get_tk_widget().pack(**kwargs)
    def grid_canvas(self, **kwargs):
        self.canvas.get_tk_widget().grid(**kwargs)
       
    def display_canvas(self, manager, **kwargs):
        if manager == "pack":
            return self.pack_canvas(**kwargs)
        elif manager == "grid":
            return self.grid_canvas(**kwargs)
        else:
            print("Invalid geometry manager")
        return None

    def redraw(self):
        self.canvas.draw()
