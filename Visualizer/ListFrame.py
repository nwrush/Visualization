# Nikko Rush
# 7/6/2017

import tkinter as tk

from VisualizerFrame import VisualizerFrame

class ListFrame(VisualizerFrame):
    """description of class"""
    def __init__(self, master):
        super(ListFrame, self).__init__(master)

        self.grid_frame(row=0, column=0, sticky="NWSE", padx=(0, 10))

        self.title = tk.Label(master=self.frame, text="Topics")
        self.title.pack(side=tk.TOP, fill=tk.X)

        self.list = tk.Listbox(master=self.frame, selectmode=tk.MULTIPLE)
        self.list.pack(side=tk.LEFT, fill=tk.Y, expand=1)

        self.scrollbar = tk.Scrollbar(master=self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list.yview)

        self.onselect_listeners = set()
        self.list.bind("<<ListboxSelect>>", self._on_select)

    def add_item(self, item, position=tk.END):
        self.list.insert(position, item)

    def add_items(self, items, position=tk.END):
        self.list.insert(position, *items)

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
        self.onselect_listeners.add(func)

    def has_select_listener(self, func):
        return func in self.onselect_listeners

    def remove_select_listener(self, func):
        self.onselect_listeners.discard(func)

    def _on_select(self, event):
        for listener in self.onselect_listeners:
            listener(event)


