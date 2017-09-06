# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'topics_list.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_topicsList(object):
    def setupUi(self, topicsList):
        topicsList.setObjectName("topicsList")
        topicsList.resize(642, 730)
        self.verticalLayout = QtWidgets.QVBoxLayout(topicsList)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(topicsList)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.filterText = QtWidgets.QLineEdit(topicsList)
        self.filterText.setObjectName("filterText")
        self.verticalLayout.addWidget(self.filterText)
        self.listWidget = QtWidgets.QListView(topicsList)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(topicsList)
        QtCore.QMetaObject.connectSlotsByName(topicsList)

    def retranslateUi(self, topicsList):
        _translate = QtCore.QCoreApplication.translate
        topicsList.setWindowTitle(_translate("topicsList", "Form"))
        self.label.setText(_translate("topicsList", "Topics"))

