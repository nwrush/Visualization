# Nikko Rush
# 7/6/2017

import tkinter as tk

from frames.VisualizerFrame import VisualizerFrame

class ListFrame(VisualizerFrame):
    """description of class"""
    def __init__(self, master, data=None):
        super(ListFrame, self).__init__(master, data_manager=data)

        self.grid_frame(row=0, column=0, sticky="NWSE", padx=(0, 10))

        self.title = tk.Label(master=self.frame, text="Topics")
        self.title.pack(side=tk.TOP, fill=tk.X)

        self.list = tk.Listbox(master=self.frame, selectmode=tk.EXTENDED)
        self.list.pack(side=tk.LEFT, fill=tk.Y, expand=1)

        self.scrollbar = tk.Scrollbar(master=self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list.yview)

        self._onselect_listeners = set()
        self.list.bind("<<ListboxSelect>>", self._on_select)

    def add_item(self, item):
        all_items = list(self.list.get(0, tk.END))
        all_items.append(str(item))
        self._add_items(sorted(all_items))

    def add_items(self, items):
        all_items = list(self.list.get(0, tk.END))
        all_items.extend(map(str, items))
        self._add_items(sorted(all_items))

    def _add_items(self, items):
        self.clear_list()
        self.list.insert(0, *items)

    def remove_item(self, position):
        self.list.delete(position)

    def clear_list(self):
        self.list.delete(0, tk.END)

    def update_width(self):
        max_width = -1
        for item in self.list.get(0, tk.END):
            if len(str(item)) > max_width:
                max_width = len(str(item))

        self.list.config(width=max_width)

    def add_select_listener(self, func):
        self._onselect_listeners.add(func)

    def has_select_listener(self, func):
        return func in self._onselect_listeners

    def remove_select_listener(self, func):
        self._onselect_listeners.discard(func)

    def clear_selection(self):
        self.list.select_clear(0, tk.END)

    def _on_select(self, event):
        listbox = event.widget
        event.selected_indexes = [self.data.idea_numbers[listbox.get(index)] for index in event.widget.curselection()]

        for listener in self._onselect_listeners:
            listener(event)


