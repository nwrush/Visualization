# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preprocessor_form.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_preprocessorForm(object):
    def setupUi(self, preprocessorForm):
        preprocessorForm.setObjectName("preprocessorForm")
        preprocessorForm.resize(500, 370)
        self.formLayout = QtWidgets.QFormLayout(preprocessorForm)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.optionBox = QtWidgets.QComboBox(preprocessorForm)
        self.optionBox.setObjectName("optionBox")
        self.optionBox.addItem("")
        self.optionBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.optionBox)
        self.label_2 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputFile = QtWidgets.QLineEdit(preprocessorForm)
        self.inputFile.setObjectName("inputFile")
        self.horizontalLayout.addWidget(self.inputFile)
        self.inputFileBtn = QtWidgets.QPushButton(preprocessorForm)
        self.inputFileBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.inputFileBtn.setObjectName("inputFileBtn")
        self.horizontalLayout.addWidget(self.inputFileBtn)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_7 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.outputDir = QtWidgets.QLineEdit(preprocessorForm)
        self.outputDir.setObjectName("outputDir")
        self.horizontalLayout_2.addWidget(self.outputDir)
        self.outputDirBtn = QtWidgets.QPushButton(preprocessorForm)
        self.outputDirBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.outputDirBtn.setObjectName("outputDirBtn")
        self.horizontalLayout_2.addWidget(self.outputDirBtn)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.finalDir = QtWidgets.QLineEdit(preprocessorForm)
        self.finalDir.setObjectName("finalDir")
        self.horizontalLayout_3.addWidget(self.finalDir)
        self.finalDirBtn = QtWidgets.QPushButton(preprocessorForm)
        self.finalDirBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.finalDirBtn.setObjectName("finalDirBtn")
        self.horizontalLayout_3.addWidget(self.finalDirBtn)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bckFile = QtWidgets.QLineEdit(preprocessorForm)
        self.bckFile.setObjectName("bckFile")
        self.horizontalLayout_4.addWidget(self.bckFile)
        self.bckFileBtn = QtWidgets.QPushButton(preprocessorForm)
        self.bckFileBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bckFileBtn.setObjectName("bckFileBtn")
        self.horizontalLayout_4.addWidget(self.bckFileBtn)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.malletDir = QtWidgets.QLineEdit(preprocessorForm)
        self.malletDir.setObjectName("malletDir")
        self.horizontalLayout_5.addWidget(self.malletDir)
        self.malletDirBtn = QtWidgets.QPushButton(preprocessorForm)
        self.malletDirBtn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.malletDirBtn.setObjectName("malletDirBtn")
        self.horizontalLayout_5.addWidget(self.malletDirBtn)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label_3 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.groupBox = QtWidgets.QComboBox(preprocessorForm)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.addItem("")
        self.groupBox.addItem("")
        self.groupBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.groupBox)
        self.label_8 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.prefix = QtWidgets.QLineEdit(preprocessorForm)
        self.prefix.setObjectName("prefix")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.prefix)
        self.label_9 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.numIdeas = QtWidgets.QLineEdit(preprocessorForm)
        self.numIdeas.setObjectName("numIdeas")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.numIdeas)
        self.line = QtWidgets.QFrame(preprocessorForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_13 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_10 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.tokenizeBox = QtWidgets.QCheckBox(preprocessorForm)
        self.tokenizeBox.setText("")
        self.tokenizeBox.setObjectName("tokenizeBox")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.tokenizeBox)
        self.label_11 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lemmatizeBox = QtWidgets.QCheckBox(preprocessorForm)
        self.lemmatizeBox.setText("")
        self.lemmatizeBox.setObjectName("lemmatizeBox")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lemmatizeBox)
        self.label_12 = QtWidgets.QLabel(preprocessorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.stopwordBox = QtWidgets.QCheckBox(preprocessorForm)
        self.stopwordBox.setText("")
        self.stopwordBox.setObjectName("stopwordBox")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.stopwordBox)

        self.retranslateUi(preprocessorForm)
        QtCore.QMetaObject.connectSlotsByName(preprocessorForm)
        preprocessorForm.setTabOrder(self.optionBox, self.inputFile)
        preprocessorForm.setTabOrder(self.inputFile, self.outputDir)
        preprocessorForm.setTabOrder(self.outputDir, self.finalDir)
        preprocessorForm.setTabOrder(self.finalDir, self.bckFile)
        preprocessorForm.setTabOrder(self.bckFile, self.malletDir)
        preprocessorForm.setTabOrder(self.malletDir, self.groupBox)
        preprocessorForm.setTabOrder(self.groupBox, self.prefix)
        preprocessorForm.setTabOrder(self.prefix, self.numIdeas)
        preprocessorForm.setTabOrder(self.numIdeas, self.tokenizeBox)
        preprocessorForm.setTabOrder(self.tokenizeBox, self.lemmatizeBox)
        preprocessorForm.setTabOrder(self.lemmatizeBox, self.stopwordBox)
        preprocessorForm.setTabOrder(self.stopwordBox, self.finalDirBtn)
        preprocessorForm.setTabOrder(self.finalDirBtn, self.inputFileBtn)
        preprocessorForm.setTabOrder(self.inputFileBtn, self.bckFileBtn)
        preprocessorForm.setTabOrder(self.bckFileBtn, self.outputDirBtn)
        preprocessorForm.setTabOrder(self.outputDirBtn, self.malletDirBtn)
        preprocessorForm.setTabOrder(self.malletDirBtn, self.outputDir)
        preprocessorForm.setTabOrder(self.outputDir, self.outputDirBtn)
        preprocessorForm.setTabOrder(self.outputDirBtn, self.finalDir)
        preprocessorForm.setTabOrder(self.finalDir, self.finalDirBtn)
        preprocessorForm.setTabOrder(self.finalDirBtn, self.inputFile)
        preprocessorForm.setTabOrder(self.inputFile, self.inputFileBtn)
        preprocessorForm.setTabOrder(self.inputFileBtn, self.malletDir)
        preprocessorForm.setTabOrder(self.malletDir, self.malletDirBtn)
        preprocessorForm.setTabOrder(self.malletDirBtn, self.bckFile)
        preprocessorForm.setTabOrder(self.bckFile, self.bckFileBtn)

    def retranslateUi(self, preprocessorForm):
        _translate = QtCore.QCoreApplication.translate
        preprocessorForm.setWindowTitle(_translate("preprocessorForm", "Form"))
        self.label.setText(_translate("preprocessorForm", "Option"))
        self.optionBox.setItemText(0, _translate("preprocessorForm", "Keywords"))
        self.optionBox.setItemText(1, _translate("preprocessorForm", "Topics"))
        self.label_2.setText(_translate("preprocessorForm", "Input File"))
        self.inputFileBtn.setText(_translate("preprocessorForm", "..."))
        self.label_7.setText(_translate("preprocessorForm", "Output Directory"))
        self.outputDirBtn.setText(_translate("preprocessorForm", "..."))
        self.label_6.setText(_translate("preprocessorForm", "Final Output Directory"))
        self.finalDirBtn.setText(_translate("preprocessorForm", "..."))
        self.label_5.setText(_translate("preprocessorForm", "Background File"))
        self.bckFileBtn.setText(_translate("preprocessorForm", "..."))
        self.label_4.setText(_translate("preprocessorForm", "Mallet Bin Directory"))
        self.malletDirBtn.setText(_translate("preprocessorForm", "..."))
        self.label_3.setText(_translate("preprocessorForm", "Group By"))
        self.groupBox.setItemText(0, _translate("preprocessorForm", "Year"))
        self.groupBox.setItemText(1, _translate("preprocessorForm", "Month"))
        self.groupBox.setItemText(2, _translate("preprocessorForm", "Quarter"))
        self.label_8.setText(_translate("preprocessorForm", "Prefix"))
        self.label_9.setText(_translate("preprocessorForm", "Number of Ideas"))
        self.label_13.setText(_translate("preprocessorForm", "Advanced Options"))
        self.label_10.setText(_translate("preprocessorForm", "Tokenize"))
        self.label_11.setText(_translate("preprocessorForm", "Lemmatize"))
        self.label_12.setText(_translate("preprocessorForm", "No Stop Words"))

