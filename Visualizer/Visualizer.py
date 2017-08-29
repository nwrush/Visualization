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

        self.ui.tabWidget.tabCloseRequested.connect(self._close_tab)

        self.main_widget = self.ui.main_widget
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self._tabs = []

        self._init_menu()

        self._preprocess_widget = None
        self._load_preprocessor()

        self._tabs.append(self._preprocess_widget)

        if data_manager is not None:
            self._add_tab(data_manager, 1)

    def _load_preprocessor(self):
        self._preprocess_widget = PreprocessorController(self.main_widget, self._preprocessor_callback)
        self.ui.tabWidget.insertTab(0, self._preprocess_widget, "Preprocessor")

    def _load_visualizer(self):
        self._visualizer_widget = VisualizerWidget(self.main_widget, self._data_manager)
        self.ui.tabWidget.insertTab(1, self._visualizer_widget, self._data_manager.name)

    def _init_menu(self):
        # File Menu
        self.ui.actionOpen.triggered.connect(self._open_visualization)

        # Visualization Menu
        self.ui.tabWidget.currentChanged.connect(self._tab_changed)
        self.ui.actionSave_PMI.triggered.connect(self._save_pmi)
        self.ui.actionSave_TS.triggered.connect(self._save_ts)
        self.ui.actionSave_Both.triggered.connect(self._save_both)

    def _add_tab(self, tab_data, index):
        widget = VisualizerWidget(self.main_widget, tab_data)
        self.ui.tabWidget.insertTab(index, widget, tab_data.name)
        self._tabs = self._tabs[:index] + [widget] + self._tabs[index:]
        self.ui.tabWidget.setCurrentIndex(index)

    def _processed_file(self, fname):
        data_manager = data.load_data(fname)
        if data_manager is not None:
            self._add_tab(data_manager, len(self._tabs))

    def _preprocessor_callback(self, return_code):
        if return_code == 0:
            self._processed_file(self._preprocess_widget.output_name)

    def _open_visualization(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dialog.setNameFilters(["Processed data file (*.p)", "All Files (*)"])
        dialog.exec()

        fnames = dialog.selectedFiles()
        if fnames:
            for fname in fnames:
                self._processed_file(fname)

    def _tab_changed(self, index):
        if index >= len(self._tabs):
            self.ui.visualizationMenu.setEnabled(False)
        else:
            self.ui.visualizationMenu.setEnabled(isinstance(self._tabs[index], VisualizerWidget))

    def _save_pmi(self):
        self.ui.tabWidget.currentWidget().save_pmi()

    def _save_ts(self):
        self.ui.tabWidget.currentWidget().save_ts()

    def _save_both(self):
        self.ui.tabWidget.currentWidget().save_both()

    def _close_tab(self, index):
        self.ui.tabWidget.removeTab(index)
        del self._tabs[index]
        print(len(self._tabs))


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
    # data_manager.name = "Test"
    # if data_manager is not None:
    #     data_manager.x_values = x_vals

    qApp = QtWidgets.QApplication(sys.argv)
    window = Application(data_manager)
    window.show()
    qApp.exec()


if __name__ == "__main__":
    main(".\processed_data\keywords_data.p")
