# Nikko Rush
# 7/2/2017

import PyQt5.QtWidgets as QtWidgets


class VisualizerFrame(QtWidgets.QWidget):
    """Abstract class, please don't instantiate"""
    def __init__(self, parent=None, data_manager=None):
        super(VisualizerFrame, self).__init__(parent)
        self.data = data_manager
