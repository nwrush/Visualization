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
        pmi_control_panel.resize(623, 200)
        pmi_control_panel.setMaximumSize(QtCore.QSize(16777215, 200))
        self.horizontalLayout = QtWidgets.QHBoxLayout(pmi_control_panel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(pmi_control_panel)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.filteredList = QtWidgets.QListWidget(self.groupBox_2)
        self.filteredList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filteredList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.filteredList.setObjectName("filteredList")
        self.verticalLayout_3.addWidget(self.filteredList)
        self.resetButton = QtWidgets.QPushButton(self.groupBox_2)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout_3.addWidget(self.resetButton)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(pmi_control_panel)
        QtCore.QMetaObject.connectSlotsByName(pmi_control_panel)

    def retranslateUi(self, pmi_control_panel):
        _translate = QtCore.QCoreApplication.translate
        pmi_control_panel.setWindowTitle(_translate("pmi_control_panel", "Form"))
        self.groupBox_2.setTitle(_translate("pmi_control_panel", "Filtered By"))
        self.resetButton.setText(_translate("pmi_control_panel", "Reset"))

