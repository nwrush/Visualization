# Nikko Rush
# 7/2/2017
# The Tk window root

import tkinter as tk
from tkinter import ttk

class Window(object):
    """description of class"""

    def __init__(self):
        self.root = tk.Tk()

        self.root.protocol("WM_DELETE_WINDOW", self.__close_window_callback)

    def start(self):
        self.root.mainloop()

    def __close_window_callback(self):
        self.root.quit()
        self._close()

    def _close(self):
        """Called after quiting tk"""
        pass


if __name__ == "__main__":
    window = Window()
    window.start()