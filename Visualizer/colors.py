# Nikko Rush
# 7/25/2017

import math

import matplotlib.cm
import matplotlib.colors

class PMIColormap(matplotlib.colors.Colormap):

    def __init__(self, name, color, N=256):
        super(PMIColormap, self).__init__(name=name, N=N)
        self._base_color = color

        self._saturation_max = matplotlib.colors.rgb_to_hsv(color)[1]

    def _resample(self, lutsize):
        super(PMIColormap, self)._resample(lutsize)

    def _init(self):
        super(PMIColormap, self)._init()

    def __call__(self, dist, *args, **kwargs):
        hsv_value = matplotlib.colors.rgb_to_hsv(self._base_color)

        hsv_value[1] = self._saturation_max * dist

        rgb = matplotlib.colors.hsv_to_rgb(hsv_value)
        r,g,b = tuple(rgb)
        r = int(r)
        g = int(g)
        b = int(b)
        assert 0 <= r <= 255
        assert 0 <= g <= 255
        assert 0 <= b <= 255
        if kwargs['bytes']:
            return r, g, b, 255.0
        else:
            return r / 255, g / 255, b / 255, 1.0

if __name__ == "__main__":
    colors = [(0, 68, 27,),
              (127, 39, 4),
              (103, 0, 12),
              (8, 48, 107)]
    maps = [PMIColormap("PMIMap", c) for c in colors]
    norma = matplotlib.colors.Normalize(0, 1, clip=True)
    color_mappers = [cm.ScalarMappable(norm=norma, cmap="Greens"),
                     cm.ScalarMappable(norm=norma, cmap="Oranges"),
                     cm.ScalarMappable(norm=norma, cmap="Reds"),
                     cm.ScalarMappable(norm=norma, cmap="Blues")]

    print("Green")
    pass

