# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relation_types_tabs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_relationTypes(object):
    def setupUi(self, relationTypes):
        relationTypes.setObjectName("relationTypes")
        relationTypes.resize(494, 373)
        self.verticalLayout = QtWidgets.QVBoxLayout(relationTypes)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(relationTypes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(relationTypes)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.friendsTab = QtWidgets.QWidget()
        self.friendsTab.setObjectName("friendsTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.friendsTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.friendsTable = QtWidgets.QTableWidget(self.friendsTab)
        self.friendsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.friendsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.friendsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.friendsTable.setCornerButtonEnabled(False)
        self.friendsTable.setObjectName("friendsTable")
        self.friendsTable.setColumnCount(3)
        self.friendsTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.friendsTable.setItem(0, 2, item)
        self.friendsTable.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.friendsTable)
        self.tabWidget.addTab(self.friendsTab, "")
        self.trystTab = QtWidgets.QWidget()
        self.trystTab.setObjectName("trystTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.trystTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.armsraceTable = QtWidgets.QTableWidget(self.trystTab)
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
        self.tabWidget.addTab(self.trystTab, "")
        self.headtoheadTab = QtWidgets.QWidget()
        self.headtoheadTab.setObjectName("headtoheadTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.headtoheadTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.headtoheadTable = QtWidgets.QTableWidget(self.headtoheadTab)
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
        self.horizontalLayout_3.addWidget(self.headtoheadTable)
        self.tabWidget.addTab(self.headtoheadTab, "")
        self.armsraceTab = QtWidgets.QWidget()
        self.armsraceTab.setObjectName("armsraceTab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.armsraceTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.trystTable = QtWidgets.QTableWidget(self.armsraceTab)
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
        self.horizontalLayout_4.addWidget(self.trystTable)
        self.tabWidget.addTab(self.armsraceTab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(relationTypes)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(relationTypes)

    def retranslateUi(self, relationTypes):
        _translate = QtCore.QCoreApplication.translate
        relationTypes.setWindowTitle(_translate("relationTypes", "Form"))
        self.label.setText(_translate("relationTypes", "Top Relations"))
        item = self.friendsTable.verticalHeaderItem(0)
        item.setText(_translate("relationTypes", "New Row"))
        item = self.friendsTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.friendsTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.friendsTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
        __sortingEnabled = self.friendsTable.isSortingEnabled()
        self.friendsTable.setSortingEnabled(False)
        item = self.friendsTable.item(0, 0)
        item.setText(_translate("relationTypes", "asd"))
        item = self.friendsTable.item(0, 1)
        item.setText(_translate("relationTypes", "asd"))
        item = self.friendsTable.item(0, 2)
        item.setText(_translate("relationTypes", "qwe"))
        self.friendsTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.friendsTab), _translate("relationTypes", "Friends"))
        item = self.armsraceTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.armsraceTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.armsraceTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trystTab), _translate("relationTypes", "Tryst"))
        item = self.headtoheadTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.headtoheadTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.headtoheadTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.headtoheadTab), _translate("relationTypes", "Head-To-Head"))
        item = self.trystTable.horizontalHeaderItem(0)
        item.setText(_translate("relationTypes", "Strength"))
        item = self.trystTable.horizontalHeaderItem(1)
        item.setText(_translate("relationTypes", "Relation 1"))
        item = self.trystTable.horizontalHeaderItem(2)
        item.setText(_translate("relationTypes", "Relation 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.armsraceTab), _translate("relationTypes", "Arms-Race"))
