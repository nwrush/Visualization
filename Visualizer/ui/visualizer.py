# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_visualizaerWidget(object):
    def setupUi(self, visualizaerWidget):
        visualizaerWidget.setObjectName("visualizaerWidget")
        visualizaerWidget.resize(845, 657)
        self.horizontalLayout = QtWidgets.QHBoxLayout(visualizaerWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(visualizaerWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(480, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(480, 16777215))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.pmiWidget = QtWidgets.QWidget(visualizaerWidget)
        self.pmiWidget.setObjectName("pmiWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.pmiWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout.addWidget(self.pmiWidget)
        self.tsWidget = QtWidgets.QWidget(visualizaerWidget)
        self.tsWidget.setObjectName("tsWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tsWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addWidget(self.tsWidget)

        self.retranslateUi(visualizaerWidget)
        QtCore.QMetaObject.connectSlotsByName(visualizaerWidget)

    def retranslateUi(self, visualizaerWidget):
        _translate = QtCore.QCoreApplication.translate
        visualizaerWidget.setWindowTitle(_translate("visualizaerWidget", "Form"))

