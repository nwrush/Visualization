class MouseInteract:
    def __init__(self, canvas, plot, select_callback=None):
        self.canvas = canvas
        self.plot = plot

        self.connect()

        self.press = None
        self.prev_selected_ind = 0

        self._select_callback = select_callback
        
    def connect(self):
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.canvas.mpl_connect('pick_event', self.on_select)

    def on_click(self, event):
        print("ouch")
        self.press = event.xdata, event.ydata

    def on_release(self, event):
        pass

    def on_motion(self, event):
        if self.press is None:
            return

    def on_select(self, event):
        print("Selected something")
        ind = event.ind[0]

        self.plot._facecolors[self.prev_selected_ind] = (0,0,1,1)

        self.plot._facecolors[ind] = (1,0,0,1)

        if self._select_callback is not None:
            self._select_callback(event)

        self.canvas.draw()
        
        self.prev_selected_ind = ind
