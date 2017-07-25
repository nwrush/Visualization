# Nikko Rush
# 7/25/2017

import math

import matplotlib.cm
import matplotlib.colors

class PMIColormap(matplotlib.colors.Colormap):

    def __init__(self, name, color, N=256):
        super(PMIColormap, self).__init__(name=name, N=N)
        self._base_color = color

    def _resample(self, lutsize):
        super(PMIColormap, self)._resample(lutsize)

    def _init(self):
        super(PMIColormap, self)._init()

    def __call__(self, dist, *args, **kwargs):
        hsv_value = matplotlib.colors.rgb_to_hsv(self._base_color)

        hsv_value[1] = dist

        rgb = matplotlib.colors.hsv_to_rgb(hsv_value)
        r,g,b = tuple(rgb)
        assert 0 <= r <= 255
        assert 0 <= g <= 255
        assert 0 <= b <= 255
        if kwargs['bytes']:
            return r, g, b, 255.0
        else:
            return r / 255, g / 255, b / 255, 1.0

if __name__ == "__main__":
    colors = [(19,126,109),
              (207,98,117),
              (152,0,2),
              (68,142,228)]
    map = PMIColormap("PMIMap", colors)

    color = map((1,1))
    print(color)


