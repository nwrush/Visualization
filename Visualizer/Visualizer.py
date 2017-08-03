# Nikko Rush
# 6/21/2017

import functools
import pickle
import sys
import tkinter as tk
import tkinter.ttk as ttk

import PyQt5
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets

import matplotlib
matplotlib.use("Qt5Agg")

import data
from data import Data
from frames.TimeSeriesFrame import TimeSeriesFrame
from frames.PMIPlot import PMIPlot
from frames.ListFrame import ListFrame
from frames.RelationTypeFrame import RelationTypeFrame
from frames.TopRelations import TopRelations
from frames.preprocessor_controller import PreprocessorController
import menu

"""
GUI creation
"""

class Application(QtWidgets.QMainWindow):

    def __init__(self, data=None):
        super(Application, self).__init__()

        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.grid_layout = QtWidgets.QGridLayout(self.main_widget)
        self.setLayout(self.grid_layout)

        self.pmi = PMIPlot(self.main_widget, data)
        self.pmi.plot(sample=1000)
        self.grid_layout.addWidget(self.pmi, 0, 0)

        self.ts = TimeSeriesFrame(self.main_widget, data)
        self.grid_layout.addWidget(self.ts, 0, 1)

        self.pmi.add_select_listener(self.ts.plot_idea_indexes_event)


def create_visualizer(data, parent):
    ts = TimeSeriesFrame(parent=parent, data=data)

    pmi = PMIPlot(master=parent, data=data)
    pmi.plot(sample=1000)

    # idea_list = ListFrame(master=parent, data=data)
    # idea_list.add_items(data.idea_names.values())
    # idea_list.update_width()
    #
    # relation_types = RelationTypeFrame(master=parent, data=data)
    # relation_types.color_buttons(pmi.color_samples)
    # pmi.add_color_changed_listener(functools.partial(relation_types.color_changed, pmi))
    #
    # top_relation_1 = TopRelations(master=parent, data=data, position={"row": 1, "column": 1},
    #                               topic_index=0)
    # top_relation_2 = TopRelations(master=parent, data=data, position={"row": 1, "column": 2},
    #                               topic_index=1)
    #
    # pmi.add_select_listener(ts.plot_idea_indexes_event)
    # pmi.add_select_listener(top_relation_1.set_idea_event)
    # pmi.add_select_listener(top_relation_2.set_idea_event)
    # pmi.add_reset_listener(idea_list.clear_selection)
    # pmi.add_reset_listener(relation_types.clear_selection)
    # pmi.add_reset_listener(ts.clear)
    #
    # idea_list.add_select_listener(pmi.filter_relation)
    # idea_list.add_select_listener(top_relation_1.clear)
    # idea_list.add_select_listener(top_relation_2.clear)
    # idea_list.add_select_listener(ts.clear)
    # idea_list.add_select_listener(relation_types.clear_selection)
    #
    # relation_types.add_select_listener(pmi.filter_relation)
    # relation_types.add_select_listener(idea_list.clear_selection)


def gui(data_fname=None):
    x_vals = [i for i in range(1980, 2015)] # The actual time deltas should be pulled from the preprocessor and used here

    data_manager = None
    if data_fname is not None:
        data_manager = data.load_data(data_fname)
        if data_manager is not None:
            data_manager.x_values = x_vals

    root = tk.Tk()

    notebook = ttk.Notebook(master=root)
    notebook.pack()

    def exit_callback():
        root.quit()

    root.protocol("WM_DELETE_WINDOW", exit_callback)

    # Preprocessor Controller
    menubar = menu.Menubar(root, data_manager)
    root.config(menu=menubar)

    preprocessor_frame = tk.Frame(master=notebook)
    visualizer_frame = tk.Frame(master=notebook)

    def callback(controller, rtn_code):
        if rtn_code != 0:
            print("Error Running Preprocessor")
            return None

        print(controller.output_name)
        data_manager = data.load_data(controller.output_name)
        data_manager.x_values = x_vals
        create_visualizer(data_manager, visualizer_frame)

    def open_handler(fname):
        data_manager = data.load_data(fname)
        data_manager.x_values = x_vals
        create_visualizer(data_manager, visualizer_frame)
        print(len(visualizer_frame.children))

    menubar._open_handlers.add(open_handler)

    notebook.add(preprocessor_frame, text="Preprocessor")
    controller = PreprocessorController(master=preprocessor_frame, finished_callback=callback)

    notebook.add(visualizer_frame, text="Visualizer")

    if data_manager is not None:
        create_visualizer(data_manager, visualizer_frame)

    print(len(visualizer_frame.children))
    tk.mainloop()
    print("Boo")


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
    import tkinter.filedialog as fd
    print(fd.askopenfilename())

if __name__ == "__main__":
    # test()
    main("keywords_data.p")

    qApp = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    qApp.exec()

