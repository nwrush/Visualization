# Nikko Rush
# 7/6/2017

import random

import tkinter as tk


used_colors = set()
def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    
    if color not in used_colors:
        used_colors.add(color)
        return color
    else:
        return get_color()

class ColoredBox(object):
    """
    Randomly colored frame
    Default width/height of 100
    """

    def __init__(self, master, width=100, height=100):
        self.frame = tk.Frame(master=master, background=get_color(), width=width, height=height)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def grid(self, **kwargs):
        self.frame.grid(**kwargs)

    def set_color(self, color):
        self.frame.configure(background=color)

if __name__ == "__main__":
    root = tk.Tk()
    box = ColoredBox(root)
    box.pack(fill=tk.X)
    
    root.mainloop()

