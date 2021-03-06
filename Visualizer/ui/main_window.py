# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Vis.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.main_widget = QtWidgets.QWidget(mainWindow)
        self.main_widget.setObjectName("main_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout.addWidget(self.tabWidget)
        mainWindow.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.openMenu = QtWidgets.QMenu(self.menubar)
        self.openMenu.setEnabled(True)
        self.openMenu.setObjectName("openMenu")
        self.visualizationMenu = QtWidgets.QMenu(self.menubar)
        self.visualizationMenu.setObjectName("visualizationMenu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setVisible(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_PMI = QtWidgets.QAction(mainWindow)
        self.actionSave_PMI.setObjectName("actionSave_PMI")
        self.actionSave_TS = QtWidgets.QAction(mainWindow)
        self.actionSave_TS.setObjectName("actionSave_TS")
        self.actionSave_Both = QtWidgets.QAction(mainWindow)
        self.actionSave_Both.setObjectName("actionSave_Both")
        self.actionSave = QtWidgets.QAction(mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.openMenu.addAction(self.actionOpen)
        self.openMenu.addAction(self.actionSave)
        self.visualizationMenu.addAction(self.actionSave_PMI)
        self.visualizationMenu.addAction(self.actionSave_TS)
        self.visualizationMenu.addAction(self.actionSave_Both)
        self.menubar.addAction(self.openMenu.menuAction())
        self.menubar.addAction(self.visualizationMenu.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.openMenu.setTitle(_translate("mainWindow", "File"))
        self.visualizationMenu.setTitle(_translate("mainWindow", "Visualization"))
        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.actionSave_PMI.setText(_translate("mainWindow", "Save PMI"))
        self.actionSave_TS.setText(_translate("mainWindow", "Save TS"))
        self.actionSave_Both.setText(_translate("mainWindow", "Save Both"))
        self.actionSave.setText(_translate("mainWindow", "Save"))
        self.actionSave.setShortcut(_translate("mainWindow", "Ctrl+S"))

