# Nikko Rush
# 6/14/2017

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np

import tkinter as tk
from tkinter import ttk

class DraggableRectangle:
    def __init__(self, rect):
        self.rect = rect
        self.press = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        #print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))
        self.rect.set_x(x0 + dx)
        self.rect.set_y(y0 + dy)

        self.rect.figure.canvas.draw()


    def on_release(self, event):
        'on release we reset the press data'
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)

colors = ["blue"] * 10
fig = plt.figure()
ax = fig.add_subplot(111)

root = tk.Tk()
root.wm_title("Banana")


x = np.random.rand(10)
y = np.random.rand(10)

scatter = ax.scatter(x, y, c = colors, picker= True)

def set_color(index):
    global colors
    colors = ["blue"] * 10
    colors[index] = "red"

def change_colors(index):
    global scatter, fig

    scatter._facecolors[index] = (1,0,0,1)
    fig.canvas.draw()
     

class MouseInteract:
    def __init__(self, canvas, plot):
        self.canvas = canvas
        self.plot = plot

        self.connect()

        self.press = None
        
    def connect(self):
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.canvas.mpl_connect('pick_event', self.on_select)

    def on_click(self, event):
        self.press = event.xdata, event.ydata

    def on_release(self, event):
        pass

    def on_motion(self, event):
        if self.press is None:
            return

    def on_select(self, event):
        ind = event.ind[0]
        
        self.plot._facecolors[ind] = (1,0,0,1)

        self.canvas.draw()


colors = ["blue"] * 10

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

interaction = MouseInteract(canvas, scatter)

tk.mainloop()
