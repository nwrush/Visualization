# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relation_types.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_relationTypes(object):
    def setupUi(self, relationTypes):
        relationTypes.setObjectName("relationTypes")
        relationTypes.resize(415, 451)
        self.verticalLayout = QtWidgets.QVBoxLayout(relationTypes)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(relationTypes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.friendsButton = QtWidgets.QPushButton(relationTypes)
        self.friendsButton.setObjectName("friendsButton")
        self.horizontalLayout.addWidget(self.friendsButton)
        self.trystButton = QtWidgets.QPushButton(relationTypes)
        self.trystButton.setObjectName("trystButton")
        self.horizontalLayout.addWidget(self.trystButton)
        self.headtoheadButton = QtWidgets.QPushButton(relationTypes)
        self.headtoheadButton.setObjectName("headtoheadButton")
        self.horizontalLayout.addWidget(self.headtoheadButton)
        self.armsraceButton = QtWidgets.QPushButton(relationTypes)
        self.armsraceButton.setObjectName("armsraceButton")
        self.horizontalLayout.addWidget(self.armsraceButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.friendsTable = QtWidgets.QTableWidget(relationTypes)
        self.friendsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.friendsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.friendsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.friendsTable.setCornerButtonEnabled(False)
        self.friendsTable.setObjectName("friendsTable")
        self.friendsTable.setColumnCount(3)
        self.friendsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setHorizontalHeaderItem(2, item)
        self.friendsTable.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.friendsTable)
        self.armsraceTable = QtWidgets.QTableWidget(relationTypes)
        self.armsraceTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.armsraceTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.armsraceTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.armsraceTable.setCornerButtonEnabled(False)
        self.armsraceTable.setObjectName("armsraceTable")
        self.armsraceTable.setColumnCount(3)
        self.armsraceTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.armsraceTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.armsraceTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.armsraceTable.setHorizontalHeaderItem(2, item)
        self.armsraceTable.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.armsraceTable)
        self.headtoheadTable = QtWidgets.QTableWidget(relationTypes)
        self.headtoheadTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.headtoheadTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.headtoheadTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.headtoheadTable.setCornerButtonEnabled(False)
        self.headtoheadTable.setObjectName("headtoheadTable")
        self.headtoheadTable.setColumnCount(3)
        self.headtoheadTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.headtoheadTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.headtoheadTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.headtoheadTable.setHorizontalHeaderItem(2, item)
        self.headtoheadTable.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.headtoheadTable)
        self.trystTable = QtWidgets.QTableWidget(relationTypes)
        self.trystTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.trystTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.trystTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.trystTable.setCornerButtonEnabled(False)
        self.trystTable.setObjectName("trystTable")
        self.trystTable.setColumnCount(3)
        self.trystTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.trystTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.trystTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.trystTable.setHorizontalHeaderItem(2, item)
        self.trystTable.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.trystTable)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(relationTypes)
        QtCore.QMetaObject.connectSlotsByName(relationTypes)

    def retranslateUi(self, relationTypes):
        _translate = QtCore.QCoreApplication.translate
        relationTypes.setWindowTitle(_translate("relationTypes", "Form"))
        self.label.setText(_translate("relationTypes", "Top Relations"))
        self.friendsButton.setText(_translate("relationTypes", "Friends"))
        self.trystButton.setText(_translate("relationTypes", "Tryst"))
        self.headtoheadButton.setText(_translate("relationTypes", "Head-To-Head"))
        self.armsraceButton.setText(_translate("relationTypes", "Arms-Race"))
        item = self.friendsTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.friendsTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.friendsTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
        item = self.armsraceTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.armsraceTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.armsraceTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
        item = self.headtoheadTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.headtoheadTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.headtoheadTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
        item = self.trystTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.trystTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.trystTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
