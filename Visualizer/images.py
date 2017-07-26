# Nikko Rush
# 7/26/2017

# Functions for loading images from disk

import os.path

import tkinter as tk

DEFAULT_IMG_ROOT = "Images"

def load_image(fname):
    path = os.path.join(DEFAULT_IMG_ROOT, fname)

    if not os.path.isfile(path):
        print("File {0} doesn't exist".format(path))
        return None

    return tk.PhotoImage(file=path)
