# Nikko Rush
# 7/8/2017

import functools
import sys

windows, linux, osx = False, False, False
if sys.platform == 'win32':
    windows = True
elif sys.platform == 'linux':
    linux = True # Assume that a display exists, cause if one doesn't exist you should have crashed a long time ago
elif sys.platform == 'darwin':
    osx = True
else:
    print("Error: Unknown system platform type")

import tkinter as tk

class ListBoxColumn(tk.Frame):
    """Works more or less like a listbox, but with columns"""
    def __init__(self, ncolumns=1, master=None, cnf={}, listboxkwargs={}, **kw):
        super(ListBoxColumn, self).__init__(master=master, cnf=cnf, **kw);

        self.list = tk.Listbox()

        self.ncolumns = ncolumns
        self.lists = [tk.Listbox(self, exportselection=False, **listboxkwargs) for i in range(ncolumns)]

        for listBox in self.lists:
            listBox.pack(side=tk.LEFT, fill=tk.Y, expand=1)

            listBox.bind("<<ListboxSelect>>", self._on_select)
            if windows or osx:
                listBox.bind("<MouseWheel>", self._yscroll)
            else:
                listBox.bind("<Button-4>", functools.partial(self._yscroll, direction=-1))
                listBox.bind("<Button-5>", functools.partial(self._yscroll, direction=1))


        self.xscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lists[0].config(xscrollcommand=self.xscrollbar.set)
        self.xscrollbar.config(command=self._xscroll)

        self.yscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.lists[0].config(yscrollcommand=self.yscrollbar.set)
        self.yscrollbar.config(command=self._yscroll)

        self.select_handlers = list()

        self.add_select_handler(self._sync_selection)

    def show_xscrollbar(self):
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    def show_yscrollbar(self):
        self.yscrollbar.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def hide_xscrollbar(self):
        self._remove_scrollbar(self.xscrollbar)

    def hide_yscrollbar(self):
        self._remove_scrollbar(self.yscrollbar)

    def _remove_scrollbar(self, scrollbar):
        scrollbar.pack_forget()

    
    def activate(self, index):
        for listBox in self.lists:
            listBox.activate(index)

    def bbox(self, index):
        raise NotImplementedError

    def config(self, **options):
        for listBox in self.lists:
            listBox.config(**options)

    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for listBox in self.lists:
            listBox.delete(first, last)
    
    def get(self, first, last=None):
        for listBox in self.lists:
            listBox.get(first, last)

    def index(self, index):
        return self.lists[0].index(index)

    def insert(self, index, *elements):
        """
        Elements should be an iterable with atleast self.ncolumns items
        If an element that you try to add has fewer than self.ncolumns items it will be padded with empty strings
        """
        for element in elements:
            adding = list(element) + [' '] * (self.ncolumns - len(element))
            for item, listBox in zip(adding, self.lists):
                listBox.insert(index, item)

    def itemcget(self, index, option):
        return self.lists[0].itemcget(index, option)

    def nearest(self, y):
        return self.lists[0].nearest(y)

    def scan_dragto(self, x, y):
        raise NotImplementedError

    def see(self, index):
        for listBox in self.lists:
            listBox.see(index)

    def selection_anchor(self, index):
        for listBox in self.lists:
            listBox.select_anchor(index)

    def selection_clear(self, first, last=None):
        for listBox in self.lists:
            listBox.select_clear(first, last)

    def selection_includes(self, index):
        return self.lists[0].select_includes(index)

    def selection_set(self, first, last=None):
        for listBox in self.lists:
            listBox.select_set(first, last)

    select_anchor = selection_anchor
    select_clear = selection_clear
    select_includes = selection_includes
    select_set = selection_set

    def size(self):
        return self.lists[0].size()

    def xview(self, column, *extra):
        for listBox in self.lists:
            listBox.xview(column, *extra)

    def xview_moveto(self, fraction):
        for listBox in self.lists:
            listBox.xview_moveto(fraction)

    def xview_scroll(self, number, what):
        for listBox in self.lists:
            listBox.xview_scroll(number, what)
        return "break"

    def yview(self, *what):
        print("YView: " + str(what))
        for listBox in self.lists:
            listBox.yview(*what)

    def yview_moveto(self, fraction):
        for listBox in self.lists:
            listBox.yview_moveto(fraction)

    def yview_scroll(self, number, what):
        for listBox in self.lists:
            listBox.yview_scroll(number, what)
        return "break"

    def bind(self, sequence=None, func=None, add=None):
        def handler(event):
            event.ListBoxColumn = self
            func(event)

        for listBox in self.lists:
            listBox.bind(sequence, handler)

    def add_select_handler(self, handler):
        self.select_handlers.append(handler)

    def remove_select_handler(self, handler):
        self.select_handlers.remove(handler)

    def _on_select(self, event):
        for func in self.select_handlers:
            event.ListBoxColumn = self
            func(event)

    def _sync_selection(self, event):
        selected = event.widget.curselection()

        self.select_clear(0, tk.END)
        for index in selected:
            self.select_set(index)

    def set_width(self):
        for listBox in self.lists:
            self._update_width(listBox)

    def _update_width(self, listBox):
        max_width = -1
        for item in listBox.get(0, tk.END):
            if len(str(item)) > max_width:
                max_width = len(str(item))

        listBox.config(width=max_width)

    def _tmp(self, *args):
        return self._yscroll(args[0])

    def _yscroll(self, event, direction=None):
        if windows:
            return self.yview_scroll(int(event.delta / -120), "units")
        elif linux:
            return self.yview_scroll(direction, "units")
        elif osx:
            return self.yview_scroll(int(event.delta), "units")


    def _xscroll(self, event):
        return self.xview_scroll(int(event.delta/-120), "units")