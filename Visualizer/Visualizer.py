# Nikko Rush
# 6/21/2017

import pickle
import tkinter as tk
import tkinter.ttk as ttk

import matplotlib
matplotlib.use("TKAgg")

from data import Data
from frames.TimeSeriesFrame import TimeSeriesFrame
from frames.PMIPlot import PMIPlot
from frames.ListFrame import ListFrame
from frames.RelationTypeFrame import RelationTypeFrame
from frames.TopRelations import TopRelations

"""
GUI creation
"""

def create_preprocessor(parent):
    input_file = tk.Entry(master=parent)
    input_file.pack()
    data_output_dir = tk.Entry(master=parent)
    data_output_dir.pack()
    final_outut_dir = tk.Entry(master=parent)
    final_outut_dir.pack()
    mallet_bin_dir = tk.Entry(master=parent)
    mallet_bin_dir.pack()
    background_file = tk.Entry(master=parent)
    background_file.pack()
    group_by = ttk.LabelFrame(master=parent)
    group_by.pack()
    prefix = tk.Entry(master=parent)
    prefix.pack()
    num_ideas = tk.Entry(master=parent)
    num_ideas.pack()
    tokenize = tk.Checkbutton(master=parent)
    tokenize.pack()
    lemmatize = tk.Checkbutton(master=parent)
    lemmatize.pack()
    nostopwords = tk.Checkbutton(master=parent)
    nostopwords.pack()


def create_visualizer(data, parent):
    ts = TimeSeriesFrame(master=parent, data=data)

    pmi = PMIPlot(master=parent, data=data)
    pmi.plot(sample=1000)

    idea_list = ListFrame(master=parent, data=data)
    idea_list.add_items(data.idea_names.values())
    idea_list.update_width()

    relation_types = RelationTypeFrame(master=parent, data=data)
    relation_types.color_buttons(pmi.color_map)

    top_relation_1 = TopRelations(master=parent, data=data, position={"row": 1, "column": 1},
                                  topic_index=0)
    top_relation_2 = TopRelations(master=parent, data=data, position={"row": 1, "column": 2},
                                  topic_index=1)

    pmi.add_select_listener(ts.plot_idea_indexes_event)
    pmi.add_select_listener(top_relation_1.set_idea_event)
    pmi.add_select_listener(top_relation_2.set_idea_event)
    pmi.add_reset_listener(idea_list.clear_selection)
    pmi.add_reset_listener(relation_types.clear_selection)
    pmi.add_reset_listener(ts.clear)

    idea_list.add_select_listener(pmi.filter_relation)

    relation_types.add_select_listener(pmi.filter_relation)
    relation_types.add_select_listener(ts.select_relation_type)
    relation_types.add_select_listener(top_relation_1.set_idea_event)
    relation_types.add_select_listener(top_relation_2.set_idea_event)


def gui(pmi_matrix, ts_correlation, ts_matrix, idea_names):
    root = tk.Tk()

    notebook = ttk.Notebook(master=root)
    notebook.pack()

    def exit_callback():
        root.quit()

    root.protocol("WM_DELETE_WINDOW", exit_callback)

    x_vals = [i for i in range(1980, 2015)] # The actual time deltas should be pulled from the preprocessor and used here

    data_manager = Data(pmi_matrix, ts_correlation, ts_matrix, idea_names, x_vals)

    # Preprocessor Controller
    preprocessor_frame = tk.Frame(master=notebook)
    notebook.add(preprocessor_frame, text="Preprocessor")
    # Don't ask why, but you don't need to pack frames you place inside the notebook
    # probably because the notebook handles that for you
    visualizer_frame = tk.Frame(master=notebook)
    notebook.add(visualizer_frame, text="Visualizer")

    create_preprocessor(preprocessor_frame)
    create_visualizer(data_manager, visualizer_frame)

    tk.mainloop()
    print("Boo")


def is_square_matrix(a):
    return a.shape[0] == a.shape[1]


def main(fname):
    # pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open("data.p", 'rb'))
    pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open(fname, 'rb'))
    assert is_square_matrix(pmi)
    assert is_square_matrix(ts_correlation)

    gui(pmi, ts_correlation, ts_matrix, idea_names)

def test():
    parent = tk.Tk()
    p = ttk.Panedwindow(parent, orient=tk.VERTICAL)
    # first pane, which would get widgets gridded into it:
    f1 = ttk.Labelframe(p, text='Pane1', width=100, height=100)
    f2 = ttk.Labelframe(p, text='Pane2', width=100, height=100)  # second pane
    p.add(f1)
    p.add(f2)

    p.pack()

    tk.mainloop()

if __name__ == "__main__":
    # test()
    main("keywords_data.p")
