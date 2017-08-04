# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pmi_control_panel_horiz.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pmi_control_panel(object):
    def setupUi(self, pmi_control_panel):
        pmi_control_panel.setObjectName("pmi_control_panel")
        pmi_control_panel.resize(655, 124)
        self.horizontalLayout = QtWidgets.QHBoxLayout(pmi_control_panel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(pmi_control_panel)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.line_2 = QtWidgets.QFrame(pmi_control_panel)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.pushButton = QtWidgets.QPushButton(pmi_control_panel)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.line = QtWidgets.QFrame(pmi_control_panel)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.legendBox = QtWidgets.QGroupBox(pmi_control_panel)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.legendBox.setFont(font)
        self.legendBox.setObjectName("legendBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.legendBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.legendBox)

        self.retranslateUi(pmi_control_panel)
        QtCore.QMetaObject.connectSlotsByName(pmi_control_panel)

    def retranslateUi(self, pmi_control_panel):
        _translate = QtCore.QCoreApplication.translate
        pmi_control_panel.setWindowTitle(_translate("pmi_control_panel", "Form"))
        self.groupBox_2.setTitle(_translate("pmi_control_panel", "Filtered By"))
        self.pushButton.setText(_translate("pmi_control_panel", "Reset"))
        self.legendBox.setTitle(_translate("pmi_control_panel", "Legend"))

