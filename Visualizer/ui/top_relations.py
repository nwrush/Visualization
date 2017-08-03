# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'top_relations.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_topRelations(object):
    def setupUi(self, topRelations):
        topRelations.setObjectName("topRelations")
        topRelations.resize(341, 401)
        self.verticalLayout = QtWidgets.QVBoxLayout(topRelations)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(topRelations)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.friendsButton = QtWidgets.QPushButton(topRelations)
        self.friendsButton.setObjectName("friendsButton")
        self.horizontalLayout.addWidget(self.friendsButton)
        self.trystButton = QtWidgets.QPushButton(topRelations)
        self.trystButton.setObjectName("trystButton")
        self.horizontalLayout.addWidget(self.trystButton)
        self.headtoheadButton = QtWidgets.QPushButton(topRelations)
        self.headtoheadButton.setObjectName("headtoheadButton")
        self.horizontalLayout.addWidget(self.headtoheadButton)
        self.armsraceButton = QtWidgets.QPushButton(topRelations)
        self.armsraceButton.setObjectName("armsraceButton")
        self.horizontalLayout.addWidget(self.armsraceButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(topRelations)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(topRelations)
        QtCore.QMetaObject.connectSlotsByName(topRelations)

    def retranslateUi(self, topRelations):
        _translate = QtCore.QCoreApplication.translate
        topRelations.setWindowTitle(_translate("topRelations", "Form"))
        self.label.setText(_translate("topRelations", "Top Relations"))
        self.friendsButton.setText(_translate("topRelations", "Friends"))
        self.trystButton.setText(_translate("topRelations", "Tryst"))
        self.headtoheadButton.setText(_translate("topRelations", "Head-To-Head"))
        self.armsraceButton.setText(_translate("topRelations", "Arms-Race"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("topRelations", "Strength"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("topRelations", "Relation 1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("topRelations", "Relation 2"))

