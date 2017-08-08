# Nikko Rush
# 6/21/2017

import sys

import PyQt5
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets

import matplotlib
matplotlib.use("Qt5Agg")

import data
from frames.preprocessor_controller import PreprocessorController
from frames.VisualizerWidget import VisualizerWidget
from ui import main_window

"""
GUI creation
"""

def tmp_callback(*args):
    print(args)

class Application(QtWidgets.QMainWindow):

    def __init__(self, data_manager=None):
        super(Application, self).__init__()

        self.ui = main_window.Ui_mainWindow()
        self.ui.setupUi(self)

        self.main_widget = self.ui.main_widget
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self._preprocess_widget = PreprocessorController(self.main_widget, tmp_callback)
        self.ui.tabWidget.insertTab(0, self._preprocess_widget, "Preprocessor")

        self._visualizer_widget = VisualizerWidget(self.main_widget, data_manager)
        self.ui.tabWidget.insertTab(1, self._visualizer_widget, "Visualizer")


def is_square_matrix(a):
    return a.shape[0] == a.shape[1]


def main(fname):
    # pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open("data.p", 'rb'))
    #pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open(fname, 'rb'))
    #assert is_square_matrix(pmi)
    #assert is_square_matrix(ts_correlation)

    # gui(fname)
    # The actual time deltas should be pulled from the preprocessor and used here
    x_vals = [i for i in range(1980, 2015)]

    data_manager = data.load_data(fname)
    data_manager.x_values = x_vals

    qApp = QtWidgets.QApplication(sys.argv)
    window = Application(data_manager)
    window.show()
    qApp.exec()


def test():
    pass


if __name__ == "__main__":
    # test()
    main("keywords_data.p")
