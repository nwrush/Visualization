# Nikko Rush
# 7/6/2017

import numpy as np
import tkinter as tk

from VisualizerFrame import VisualizerFrame

class RelationTypeFrame(VisualizerFrame):

    def __init__(self, master, pmi, ts_correlation, idea_names):
        super(RelationTypeFrame, self).__init__(master=master)
        self.grid_frame(row=1, column=0, sticky="NWSE", padx=(0, 10))

        self.idea_names = idea_names

        self.title = tk.Label(master=self.frame, text="Strongest Relations")
        self.title.grid(row=0, columnspan=2, sticky="we")

        self.tryst_data, self.friends_data, self.head_data, self.arms_data = [], [], [], []

        self.tryst_list = tk.Listbox(master=self.frame, selectmode=tk.EXTENDED)
        self.tryst_list.grid(row=1, column=0)
        self.tryst_list.bind("<<ListboxSelect>>", self._on_select)

        self.friends_list = tk.Listbox(master=self.frame, selectmode=tk.EXTENDED)
        self.friends_list.grid(row=1, column=1)
        self.friends_list.bind("<<ListboxSelect>>", self._on_select)

        self.head_list = tk.Listbox(master=self.frame, selectmode=tk.EXTENDED)
        self.head_list.grid(row=2, column=0)
        self.head_list.bind("<<ListboxSelect>>", self._on_select)

        self.arms_list = tk.Listbox(master=self.frame, selectmode=tk.EXTENDED)
        self.arms_list.grid(row=2, column=1)
        self.arms_list.bind("<<ListboxSelect>>", self._on_select)

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

    def add_trysts(self, items):
        self.tryst_data.extend(items)
        self.tryst_list.insert(tk.END, *self._get_string_repr(items))

    def add_friends(self, items):
        self.friends_data.extend(items)
        self.friends_list.insert(tk.END, *self._get_string_repr(items))

    def add_head(self, items):
        self.head_data.extend(items)
        self.head_list.insert(tk.END, *self._get_string_repr(items))

    def add_arms(self, items):
        self.arms_data.extend(items)
        self.arms_list.insert(tk.END, *self._get_string_repr(items))

    def _get_string_repr(self, items):
        strings = []
        for item in items:
            s = "{0:.4f} | {1} | {2}".format(item[2], self.idea_names[item[0]], self.idea_names[item[1]])
            strings.append(s)
        return strings

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
            listener(event)
