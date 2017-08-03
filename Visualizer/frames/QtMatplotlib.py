# Nikko Rush
# 8/2/2017

import sys

import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from numpy import arange, sin, pi

class QMatplotlib(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)

        self.get_initial()

        FigureCanvasQTAgg.__init__(self, self.figure)
        self.setParent(parent)

        FigureCanvasQTAgg.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)

    def get_initial(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s, 'r')

class Application(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.main_widget = QtWidgets.QWidget(self)

        layout = QtWidgets.QVBoxLayout(self.main_widget)
        graph = QMatplotlib(parent=self.main_widget)
        layout.addWidget(graph)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

def test():
    import sys
    from PyQt5 import QtWidgets

    """
    ZetCode PyQt4 tutorial 

    In this example, we create a skeleton
    of a calculator using a QtGui.QGridLayout.

    author: Jan Bodnar
    website: zetcode.com 
    last edited: July 2014
    """

    class Example(QtWidgets.QWidget):

        def __init__(self):
            super(Example, self).__init__()

            self.initUI()

        def initUI(self):

            grid = QtWidgets.QGridLayout()
            self.setLayout(grid)

            names = ['Cls', 'Bck', '', 'Close',
                     '7', '8', '9', '/',
                     '4', '5', '6', '*',
                     '1', '2', '3', '-',
                     '0', '.', '=', '+']

            positions = [(i, j) for i in range(5) for j in range(4)]

            for position, name in zip(positions, names):

                if name == '':
                    continue
                button = QtWidgets.QPushButton(name)
                grid.addWidget(button, *position)

            self.move(300, 150)
            self.setWindowTitle('Calculator')
            self.show()

    def main():
        app = QtWidgets.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())

    main()

if __name__ == "__main__":
    qApp = QtWidgets.QApplication(sys.argv)
    window = Application()

    window.show()
    sys.exit(qApp.exec_())
    # test()