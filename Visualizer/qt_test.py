# Nikko Rush
# 8/1/2017

import sys

import PyQt5.QtWidgets as QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle("Test")

    layout = QtWidgets.QHBoxLayout(w)
    w.setLayout(layout)

    label = QtWidgets.QLabel("test", w)
    layout.addWidget(label)

    w.show()
    sys.exit(app.exec_())