# Nikko Rush
# 7/6/2017

import functools
import tkinter as tk

import numpy as np

from frames.VisualizerFrame import VisualizerFrame
from widgets.ListBoxColumn import ListBoxColumn


class RelationTypeFrame(VisualizerFrame):

    def __init__(self, master, data):
        super(RelationTypeFrame, self).__init__(master=master, data_manager=data)
        self.grid_frame(row=1, column=0, sticky="NWSE", padx=(0, 10))

        self.header = tk.Frame(master=self.frame)
        self.header.pack(side=tk.TOP, expand=1)

        self.title = tk.Label(master=self.header, text="Strongest Relations")
        self.title.grid(row=0, columnspan=4, sticky="we")

        self.data = data

        self.types = ["Tryst", "Friends", "Head-To-Head", "Arms-Race"]
        self.buttons = self._create_buttons()

        self.tryst_data, self.friends_data, self.head_data, self.arms_data = [], [], [], []
        self.list_data = [[] for i in self.types]
        self.lists = self._create_lists()

        self.active_index = None

        self._onselect_listeners = set()

        self._determine_relations()

        self._set_active_index(0)

    def _create_buttons(self):
        buttons = []
        for i, name in enumerate(self.types):
            btn = tk.Button(master=self.header, text=name, command=functools.partial(self._set_active, name))
            btn.grid(row=1, column=i, sticky="we")
            buttons.append(btn)
        return buttons

    def _create_lists(self):
        lists = []
        for i, name in enumerate(self.types):
            listbox = ListBoxColumn(master=self.frame, ncolumns=3)
            listbox.add_yscrollbar()
            listbox.set_width()
            listbox.add_select_handler(self._on_select)
            lists.append(listbox)
        return lists

    def _determine_relations(self):
        pmi = self.data.pmi
        ts_correlation = self.data.ts_correlation
        trysts, friends, head, arms = [], [], [], []
        num_ideas = self.data.num_ideas
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

        self._add_to_list(trysts, 0, sort=True, top=25)
        self._add_to_list(friends, 1, sort=True, top=25)
        self._add_to_list(head, 2, sort=True, top=25)
        self._add_to_list(arms, 3, sort=True, top=25)

    def _add_to_list(self, items, index, sort=True, top=None):
        data = self.list_data[index]
        listbox = self.lists[index]
        if sort:
            items = self._sort_by_strength(items)

        if top is not None:
            items = items[:top]

        data.extend(items)
        listbox.insert(tk.END, *self._get_output_repr(items))

    def _get_output_repr(self, items):
        outputs = []
        for item in items:
            output = (round(item[2],4), self.data.idea_names[item[0]], self.data.idea_names[item[1]])
            outputs.append(output)
        return outputs

    def _sort_by_strength(self, data, strength_index=2):
        sorted_list = sorted(data, key=lambda item: abs(item[strength_index]))
        sorted_list.reverse()
        return sorted_list

    def clear_lists(self):
        for listbox in self.lists:
            listbox.delete(0, tk.END)

    def add_select_listener(self, func):
        self._onselect_listeners.add(func)

    def has_select_listener(self, func):
        return func in self._onselect_listeners

    def remove_select_listener(self, func):
        self._onselect_listeners.discard(func)

    def _on_select(self, event):
        data = self.list_data[self.active_index]
        selected_indexes = []
        for index in event.ListBoxColumn.curselection():
            selected_indexes.extend(data[index][:2])

        event.selected_indexes = selected_indexes

        for listener in self._onselect_listeners:
            listener(event)

    def _set_active(self, name):
        index = self.types.index(name)
        return self._set_active_index(index)

    def _set_active_index(self, index):
        if self.active_index is not None:
            self.lists[self.active_index].pack_forget()

        self.lists[index].pack()
        self.active_index = index
