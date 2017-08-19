# Nikko Rush
# 8/18/17


class Utils:
    def save_plot(self, fname):
        self._mpl.get_figure().savefig(fname)

    def get_supported_formats(self):
        return self._mpl.canvas.get_supported_filetypes()