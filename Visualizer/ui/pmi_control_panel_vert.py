# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pmi_control_panel_vert.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pmi_control_panel(object):
    def setupUi(self, pmi_control_panel):
        pmi_control_panel.setObjectName("pmi_control_panel")
        pmi_control_panel.resize(258, 415)
        self.verticalLayout = QtWidgets.QVBoxLayout(pmi_control_panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(pmi_control_panel)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.filteredList = QtWidgets.QListWidget(self.groupBox)
        self.filteredList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.filteredList.setWordWrap(False)
        self.filteredList.setObjectName("filteredList")
        self.verticalLayout_4.addWidget(self.filteredList)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.resetButton = QtWidgets.QPushButton(pmi_control_panel)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)
        self.line = QtWidgets.QFrame(pmi_control_panel)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.colorLabels = QtWidgets.QGroupBox(pmi_control_panel)
        self.colorLabels.setEnabled(True)
        self.colorLabels.setFlat(False)
        self.colorLabels.setObjectName("colorLabels")
        self.gridLayout = QtWidgets.QGridLayout(self.colorLabels)
        self.gridLayout.setObjectName("gridLayout")
        self.colorLabelsLayout = QtWidgets.QGridLayout()
        self.colorLabelsLayout.setObjectName("colorLabelsLayout")
        self.headtoheadLabel = QtWidgets.QLabel(self.colorLabels)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.headtoheadLabel.setFont(font)
        self.headtoheadLabel.setAutoFillBackground(True)
        self.headtoheadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headtoheadLabel.setObjectName("headtoheadLabel")
        self.colorLabelsLayout.addWidget(self.headtoheadLabel, 1, 0, 1, 1)
        self.trystLabel = QtWidgets.QLabel(self.colorLabels)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trystLabel.setFont(font)
        self.trystLabel.setAutoFillBackground(True)
        self.trystLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.trystLabel.setObjectName("trystLabel")
        self.colorLabelsLayout.addWidget(self.trystLabel, 0, 0, 1, 1)
        self.friendsLabel = QtWidgets.QLabel(self.colorLabels)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.friendsLabel.setFont(font)
        self.friendsLabel.setAutoFillBackground(True)
        self.friendsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.friendsLabel.setObjectName("friendsLabel")
        self.colorLabelsLayout.addWidget(self.friendsLabel, 0, 1, 1, 1)
        self.armsraceLabel = QtWidgets.QLabel(self.colorLabels)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.armsraceLabel.setFont(font)
        self.armsraceLabel.setAutoFillBackground(True)
        self.armsraceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.armsraceLabel.setObjectName("armsraceLabel")
        self.colorLabelsLayout.addWidget(self.armsraceLabel, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.colorLabelsLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.colorLabels)

        self.retranslateUi(pmi_control_panel)
        QtCore.QMetaObject.connectSlotsByName(pmi_control_panel)

    def retranslateUi(self, pmi_control_panel):
        _translate = QtCore.QCoreApplication.translate
        pmi_control_panel.setWindowTitle(_translate("pmi_control_panel", "Form"))
        self.groupBox.setTitle(_translate("pmi_control_panel", "Filtered By"))
        self.resetButton.setText(_translate("pmi_control_panel", "Reset"))
        self.colorLabels.setTitle(_translate("pmi_control_panel", "Legend"))
        self.headtoheadLabel.setText(_translate("pmi_control_panel", "Head-To-Head"))
        self.trystLabel.setText(_translate("pmi_control_panel", "Tryst"))
        self.friendsLabel.setText(_translate("pmi_control_panel", "Friends"))
        self.armsraceLabel.setText(_translate("pmi_control_panel", "Arms-Race"))

