# Nikko Rush
# 7/10/2017

import numpy as np
import tkinter as tk

from ListBoxColumn import ListBoxColumn
from VisualizerFrame import VisualizerFrame

class TopRelations(VisualizerFrame):
    
    def __init__(self, master, data, position={}, topic_index=0):
        super(TopRelations, self).__init__(master, data_manager=data)
        self.grid_frame(**position)

        self.title_text = tk.StringVar()
        self.title_text.set("Selected Relation: ")
        self.title = tk.Label(master=self.frame, textvariable=self.title_text)
        self.title.pack()

        self.listbox = ListBoxColumn(master=self.frame, ncolumns=3)
        self.listbox.pack()

        self._index = topic_index

    def set_idea_name(self, name):
        return self.set_idea_index(self.data.idea_numbers[name])

    def set_idea_index(self, index):
        strengths = []
        pmi, ts_cor = self.data.pmi, self.data.ts_correlation
        for i in range(0, self.data.num_ideas):
            for j in range(i+1, self.data.num_ideas):
                if i != index and j != index:
                    continue
                point_pmi = pmi[i, j]
                point_cor = ts_cor[i, j]
                if np.isnan(point_pmi) or np.isnan(point_cor):
                    continue
                if np.isinf(point_pmi) or np.isinf(point_cor):
                    continue

                strength = point_pmi * point_cor
                type = self._get_point_type(point_pmi, point_cor)

                other_topic_name = self.data.idea_names[i if i != index else j]
                self._insert_sorted(strengths, (round(strength, 3), type, other_topic_name), sort_index=0)

        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, *strengths)

        # Update the frame title
        self.title_text.set("Selected Relation: "+ self.data.idea_names[index])

    def _get_point_type(self, point_pmi, point_cor):
        if 0 <= point_pmi and point_cor < 0:
            return "Tryst"
        elif 0 <= point_pmi and 0 <= point_cor:
            return "Friends"
        elif point_pmi < 0 and point_cor < 0:
            return "Head-To-Head"
        elif point_pmi < 0 and 0 <= point_cor:
            return "Arms-Race"

    def _insert_sorted(self, items, item, sort_index=0):
        index = 0
        for index in range(len(items)):
            list_item = items[index]

            if item[sort_index] >= list_item[sort_index]:
                break
        items.insert(index, item)

    def set_idea_event(self, event):
        self.set_idea_index(event.selected_indexes[self._index])
