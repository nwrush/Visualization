# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'top_relations.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_topRelation(object):
    def setupUi(self, topRelation):
        topRelation.setObjectName("topRelation")
        topRelation.resize(324, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(topRelation)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.staticLabel = QtWidgets.QLabel(topRelation)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.staticLabel.setFont(font)
        self.staticLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.staticLabel.setObjectName("staticLabel")
        self.horizontalLayout.addWidget(self.staticLabel)
        self.relationName = QtWidgets.QLabel(topRelation)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.relationName.setFont(font)
        self.relationName.setText("")
        self.relationName.setObjectName("relationName")
        self.horizontalLayout.addWidget(self.relationName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(topRelation)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(topRelation)
        QtCore.QMetaObject.connectSlotsByName(topRelation)

    def retranslateUi(self, topRelation):
        _translate = QtCore.QCoreApplication.translate
        topRelation.setWindowTitle(_translate("topRelation", "Form"))
        self.staticLabel.setText(_translate("topRelation", "Selected Relation:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("topRelation", "Strength"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("topRelation", "Relation Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("topRelation", "Relation 2"))

