# Nikko Rush
# 6/21/2017

# region Imports
import logging
import platform
import sys

FORMAT = "%(asctime)s %(levelname)8s:[%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=FORMAT,
                    datefmt='%m-%d %H:%M:%S',
                    filename='./Visualizer.log',
                    filemode='w')

import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import matplotlib
matplotlib.use("Qt5Agg")

import exception_handler
import data
from frames.preprocessor_controller import PreprocessorController
from frames.VisualizerWidget import VisualizerWidget
from ui import main_window
# endregion

logging.info("Application Startup")
logging.info(platform.uname())
logging.info(platform.platform())
logging.info(platform.python_version())

version = platform.win32_ver()
if not version[0] == '':
    logging.info(version)

version = platform.mac_ver()
if not version[0] == '':
    logging.info(version)

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
        self.ui.actionSave.triggered.connect(self._save_visualization)

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

    def _save_visualization(self):
        current_tab = self._tabs[self.ui.tabWidget.currentIndex()]
        if isinstance(current_tab, PreprocessorController):
            return

        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dialog.setNameFilters(["Processed data file (*.p)", "All Files (*)"])
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dialog.setDefaultSuffix(".p")
        dialog.exec()

        fname = dialog.selectedFiles()[0]
        success = current_tab.save_data(fname)
        if not success:
            QtWidgets.QMessageBox.about(self, "Save Error",
                                        "An error occured saving the file\nCheck the log for more details")

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
        if isinstance(self._tabs[index], PreprocessorController):
            return
        self.ui.tabWidget.removeTab(index)
        del self._tabs[index]
        
    def kill_preprocessor(self):
        self._preprocess_widget.kill()


def is_square_matrix(a):
    return a.shape[0] == a.shape[1]


def main(fname=None):
    data_manager = None
    if fname is not None:
        data_manager = data.load_data(fname)

    qApp = QtWidgets.QApplication(sys.argv)
    logging.info(qApp.primaryScreen().physicalSize())
    window = Application(data_manager)
    window.show()
    qApp.exec()
    logging.info("Goodbye")


if __name__ == "__main__":
    main()
