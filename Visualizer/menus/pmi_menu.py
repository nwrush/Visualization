# Nikko Rush
# 7/25/2017

import tkinter as tk
import tkinter.colorchooser
import tkinter.ttk as ttk

def rgb_to_luma(r, g, b):
    luminance = 0.2126*r + 0.7152*g + 0.0722*b

def create(parent):
    return PMIMenu(parent)

def create_factory(parent):
    def func():
        create(parent)
    return func

class PMIMenu(object):
    
    def __init__(self, parent):
        self._window = tk.Toplevel(master=parent.frame)
        self._window.title("PMI Graph Settings")

        self._parent = parent
        self._data = parent.data

        self._color_settings = ttk.LabelFrame(master=self._window, text="Colors")
        self._color_settings.pack()

        self._colors = []
        for index, relation in enumerate(self._data.relation_types):
            label = tk.Label(master=self._color_settings, text="{0} Color".format(relation))
            btn = tk.Button(master=self._color_settings, text="Get Color", command=self._get_color_button(index))
            label.grid(row=index, column=0, sticky="we")
            btn.grid(row=index, column=1)

            parent_color = self._parent._colors[index]
            self._colors.append([label, btn, parent_color]) # Use a better default here

        self._window.protocol("WM_DELETE_WINDOW", self.on_exit)
        
    def _get_color_button(self, index):
        def func():
            rgb, hex = tk.colorchooser.askcolor()

            self._colors[index][2] = rgb

            sample = self._colors[index][0]
            sample.config(background=hex)

            r, g, b = rgb
            # https://en.wikipedia.org/wiki/Relative_luminance
            # ITU-R BT.709 Primaries
            luma = (0.2126*r + 0.7152*g + 0.0722*b)/255
            if luma >= 0.5:
                sample.config(fg="Black")
            else:
                sample.config(fg="White")

        return func

    def on_exit(self):
        for index, color in enumerate(self._colors):
            _, _, rgb = color
            
            self._parent._colors[index] = rgb
        
        self._window.destroy()
