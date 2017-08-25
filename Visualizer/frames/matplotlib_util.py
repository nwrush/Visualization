# Nikko Rush
# 8/18/17

from PyQt5.QtWidgets import QMessageBox


class Utils:
    def save_plot(self, fname):
        self._mpl.get_figure().savefig(fname)

    def confirm_on_empty(self, name):
        if not self._has_data:
            reply = QMessageBox.question(self, "Confrim Save Plot",
                                         "{0} plot is empty\nAre you sure you want to save it?".format(name),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            return int(reply) == QMessageBox.Yes
        return True

    def get_supported_formats(self):
        return self._mpl.canvas.get_supported_filetypes()
