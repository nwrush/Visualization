# Nikko Rush
# 7/6/2017

import numpy as np
import tkinter as tk

from VisualizerFrame import VisualizerFrame
from ListBoxColumn import ListBoxColumn

class RelationTypeFrame(VisualizerFrame):

    def __init__(self, master, pmi, ts_correlation, idea_names):
        super(RelationTypeFrame, self).__init__(master=master)
        self.grid_frame(row=1, column=0, sticky="NWSE", padx=(0, 10))

        self.idea_names = idea_names

        self.title = tk.Label(master=self.frame, text="Strongest Relations")
        self.title.grid(row=0, columnspan=2, sticky="we")

        self.tryst_data, self.friends_data, self.head_data, self.arms_data = [], [], [], []

        self.tryst_list = ListBoxColumn(master=self.frame, ncolumns=3)
        self.tryst_list.add_yscrollbar()
        self.tryst_list.grid(row=1, column=0)
        self.tryst_list.add_select_handler(self._on_select)

        self.friends_list = ListBoxColumn(master=self.frame, ncolumns=3)
        self.friends_list.add_yscrollbar()
        self.friends_list.grid(row=1, column=1)
        self.friends_list.add_select_handler(self._on_select)

        self.head_list = ListBoxColumn(master=self.frame, ncolumns=3)
        self.head_list.add_yscrollbar()
        self.head_list.grid(row=2, column=0)
        self.head_list.add_select_handler(self._on_select)

        self.arms_list = ListBoxColumn(master=self.frame, ncolumns=3)
        self.arms_list.add_yscrollbar()
        self.arms_list.grid(row=2, column=1)
        self.arms_list.add_select_handler(self._on_select)

        self.data_mappings = {self.tryst_list: self.tryst_data, self.friends_list: self.friends_data, self.head_list: self.head_data, self.arms_list: self.arms_data}

        self._onselect_listeners = set()

        self._determine_relations(pmi, ts_correlation)


    def _determine_relations(self, pmi, ts_correlation):
        trysts, friends, head, arms = [], [], [], []
        num_ideas = pmi.shape[0]
        cnt = 0
        for i in range(0, num_ideas):
            for j in range(i+1, num_ideas):
                point_pmi = pmi[i, j]
                point_cor = ts_correlation[i, j]
                if np.isnan(point_pmi) or np.isnan(point_cor):
                    continue
                if np.isinf(point_pmi) or np.isinf(point_cor):
                    continue
                cnt += 1
                strength = point_pmi*point_cor

                if 0 <= point_pmi and point_cor < 0:
                    trysts.append((i,j,strength))
                elif 0 <= point_pmi and 0 <= point_cor:
                    friends.append((i, j, strength))
                elif point_pmi < 0 and point_cor < 0:
                    head.append((i, j, strength))
                elif point_pmi < 0 and 0 <= point_cor:
                    arms.append((i, j, strength))

        assert len(trysts) + len(friends) + len(head) + len(arms) == cnt

        self.add_trysts(trysts)
        self.add_friends(friends)
        self.add_head(head)
        self.add_arms(arms)

    def add_trysts(self, items, sort=True):
        if sort:
            items = self._sort_by_strength(items)

        self.tryst_data.extend(items)
        self.tryst_list.insert(tk.END, *self._get_output_repr(items))

    def add_friends(self, items, sort=True):
        if sort:
            items = self._sort_by_strength(items)

        self.friends_data.extend(items)
        self.friends_list.insert(tk.END, *self._get_output_repr(items))

    def add_head(self, items, sort=True):
        if sort:
            items = self._sort_by_strength(items)

        self.head_data.extend(items)
        self.head_list.insert(tk.END, *self._get_output_repr(items))

    def add_arms(self, items, sort=True):
        if sort:
            items = self._sort_by_strength(items)

        self.arms_data.extend(items)
        self.arms_list.insert(tk.END, *self._get_output_repr(items))

    def _get_output_repr(self, items):
        outputs = []
        for item in items:
            output = (round(item[2],4), self.idea_names[item[0]], self.idea_names[item[1]])
            outputs.append(output)
        return outputs

    def _sort_by_strength(self, data, strength_index=2):
        sorted_list = sorted(data, key=lambda item: abs(item[strength_index]))
        sorted_list.reverse()
        return sorted_list

    def clear_lists(self):
        self.tryst_list.delete(0, tk.END)
        self.friends_list.delete(0, tk.END)
        self.head_list.delete(0, tk.END)
        self.arms_list.delete(0, tk.END)

    def add_select_listener(self, func):
        self._onselect_listeners.add(func)

    def has_select_listener(self, func):
        return func in self._onselect_listeners

    def remove_select_listener(self, func):
        self._onselect_listeners.discard(func)

    def _on_select(self, event):
        for listener in self._onselect_listeners:
            data = self.data_mappings[event.ListBoxColumn]
            event.data = data
            listener(event)
