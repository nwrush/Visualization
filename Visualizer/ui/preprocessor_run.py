# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preprocessor_run.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_preprocessorRun(object):
    def setupUi(self, preprocessorRun):
        preprocessorRun.setObjectName("preprocessorRun")
        preprocessorRun.resize(414, 87)
        self.verticalLayout = QtWidgets.QVBoxLayout(preprocessorRun)
        self.verticalLayout.setObjectName("verticalLayout")
        self.runPreprocessor = QtWidgets.QPushButton(preprocessorRun)
        self.runPreprocessor.setObjectName("runPreprocessor")
        self.verticalLayout.addWidget(self.runPreprocessor)
        self.progressBar = QtWidgets.QProgressBar(preprocessorRun)
        self.progressBar.setEnabled(False)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(preprocessorRun)
        QtCore.QMetaObject.connectSlotsByName(preprocessorRun)

    def retranslateUi(self, preprocessorRun):
        _translate = QtCore.QCoreApplication.translate
        preprocessorRun.setWindowTitle(_translate("preprocessorRun", "Form"))
        self.runPreprocessor.setText(_translate("preprocessorRun", "Run Preprocessor"))

