# Nikko Rush
# 6/21/2017

# region Imports
import sys

import PyQt5.QtWidgets as QtWidgets
import matplotlib
matplotlib.use("Qt5Agg")

import exception_handler
import data
from frames.preprocessor_controller import PreprocessorController
from frames.VisualizerWidget import VisualizerWidget
from ui import main_window
# endregion

"""
GUI creation
"""


class Application(QtWidgets.QMainWindow):

    def __init__(self, data_manager=None):
        super(Application, self).__init__()

        self.ui = main_window.Ui_mainWindow()
        self.ui.setupUi(self)

        self.main_widget = self.ui.main_widget
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self._data_manager = data_manager

        self._preprocess_widget = None
        self._load_preprocessor()

        self._visualizer_widget = None
        if self._data_manager is not None:
            self._load_visualizer()

        self._init_menu()

    def _load_preprocessor(self):
        self._preprocess_widget = PreprocessorController(self.main_widget, self._preprocessor_callback)
        self.ui.tabWidget.insertTab(0, self._preprocess_widget, "Preprocessor")

    def _load_visualizer(self):
        self._visualizer_widget = VisualizerWidget(self.main_widget, self._data_manager)
        self.ui.tabWidget.insertTab(1, self._visualizer_widget, "Visualizer")

    def _init_menu(self):
        self.ui.actionOpen.triggered.connect(self._open_visualization)

    def set_data(self, new_data):
        self._data_manager = new_data

        if self._visualizer_widget is not None:
            self.ui.tabWidget.removeTab(1)

        self._load_visualizer()

    def _processed_file(self, fname):
        data_manager = data.load_data(fname)
        assert data_manager is not None
        self.set_data(data_manager)

    def _preprocessor_callback(self, return_code):
        if return_code == 0:
            self._processed_file(self._preprocess_widget.output_name)

    def _open_visualization(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        dialog.setNameFilters(["Processed data file (*.p)", "All files (*)"])
        dialog.exec()

        fnames = dialog.selectedFiles()
        if fnames:
            self._preprocess_widget.output_name(fnames[0])


def is_square_matrix(a):
    return a.shape[0] == a.shape[1]


def main(fname):
    # pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open("data.p", 'rb'))
    # pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open(fname, 'rb'))
    # assert is_square_matrix(pmi)
    # assert is_square_matrix(ts_correlation)

    # gui(fname)
    # The actual time deltas should be pulled from the preprocessor and used here

    data_manager = data.load_data(fname)
    # if data_manager is not None:
    #     data_manager.x_values = x_vals

    qApp = QtWidgets.QApplication(sys.argv)
    window = Application(data_manager)
    window.show()
    qApp.exec()


if __name__ == "__main__":
    main(".\processed_data\keywords_data.p")
