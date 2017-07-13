# Nikko Rush
# 6/21/2017

import pickle

import matplotlib

import tkinter as tk
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

def gui(pmi_matrix, ts_correlation, ts_matrix, idea_names):
    print(matplotlib.get_backend())
    root = tk.Tk()

    def exit_callback():
        root.quit()

    root.protocol("WM_DELETE_WINDOW", exit_callback)

    x_vals = [i for i in range(1980, 2015)]

    data_manager = Data(pmi_matrix, ts_correlation, ts_matrix, idea_names, x_vals)

    ts = TimeSeriesFrame(master=root, data=data_manager)
    pmi = PMIPlot(master=root, data=data_manager)

    idea_list = ListFrame(master=root, data=data_manager)
    idea_list.add_items(idea_names.values())
    idea_list.update_width()

    relation_types = RelationTypeFrame(master=root, data=data_manager)

    top_relation_1 = TopRelations(master=root, data=data_manager, position={"row":1, "column":1}, topic_index=0)
    top_relation_1.set_idea_index(0)

    top_relation_2 = TopRelations(master=root, data=data_manager, position={"row":1, "column":2}, topic_index=1)
    top_relation_2.set_idea_index(10)

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

    pmi.plot(sample=1000)

    tk.mainloop()
    print("Boo")

def is_square_matrix(a):
    return a.shape[0] == a.shape[1]

def main(fname):
    # pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open("data.p", 'rb'))
    pmi, ts_correlation, ts_matrix, idea_names = pickle.load(open(fname, 'rb'))
    assert is_square_matrix(pmi)
    assert is_square_matrix(ts_correlation)

    """
    idea_names: maps the index of an idea/keyword to the text name of it
    idea_numbers: maps idea_name or keyword or whatever -> relevant index
    """
    gui(pmi, ts_correlation, ts_matrix, idea_names)

if __name__ == "__main__":
    print(matplotlib.get_backend())
    main("keywords_data.p")
