# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_carving_ui.ui'
#
# Created: Mon Jun 27 10:51:40 2011
#      by: pyside-uic 0.2.10 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_filecarvingWidget(object):
    def setupUi(self, filecarvingWidget):
        filecarvingWidget.setObjectName("filecarvingWidget")
        filecarvingWidget.resize(551, 470)
        self.verticalLayout = QtGui.QVBoxLayout(filecarvingWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.inputFile = QtGui.QLineEdit(filecarvingWidget)
        self.inputFile.setObjectName("inputFile")
        self.gridLayout_2.addWidget(self.inputFile, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(filecarvingWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(filecarvingWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.outputdir = QtGui.QLineEdit(filecarvingWidget)
        self.outputdir.setObjectName("outputdir")
        self.gridLayout_2.addWidget(self.outputdir, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtGui.QLabel(filecarvingWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox = QtGui.QComboBox(filecarvingWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fragmentSize = QtGui.QLineEdit(filecarvingWidget)
        self.fragmentSize.setObjectName("fragmentSize")
        self.gridLayout.addWidget(self.fragmentSize, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(filecarvingWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.incrementSize = QtGui.QLineEdit(filecarvingWidget)
        self.incrementSize.setObjectName("incrementSize")
        self.gridLayout.addWidget(self.incrementSize, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(filecarvingWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.offset = QtGui.QLineEdit(filecarvingWidget)
        self.offset.setObjectName("offset")
        self.gridLayout.addWidget(self.offset, 1, 2, 1, 1)
        self.blockgap = QtGui.QLineEdit(filecarvingWidget)
        self.blockgap.setObjectName("blockgap")
        self.gridLayout.addWidget(self.blockgap, 1, 3, 1, 1)
        self.label_4 = QtGui.QLabel(filecarvingWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label = QtGui.QLabel(filecarvingWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.resultList = QtGui.QListWidget(filecarvingWidget)
        self.resultList.setObjectName("resultList")
        self.verticalLayout.addWidget(self.resultList)
        self.progressBar = QtGui.QProgressBar(filecarvingWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.processButton = QtGui.QPushButton(filecarvingWidget)
        self.processButton.setObjectName("processButton")
        self.verticalLayout.addWidget(self.processButton)

        self.retranslateUi(filecarvingWidget)
        QtCore.QMetaObject.connectSlotsByName(filecarvingWidget)

    def retranslateUi(self, filecarvingWidget):
        filecarvingWidget.setWindowTitle(QtGui.QApplication.translate("filecarvingWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("filecarvingWidget", "Input File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("filecarvingWidget", "Output Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("filecarvingWidget", "Preprocessing: ", None, QtGui.QApplication.UnicodeUTF8))
        self.fragmentSize.setText(QtGui.QApplication.translate("filecarvingWidget", "512", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("filecarvingWidget", "Increment Size", None, QtGui.QApplication.UnicodeUTF8))
        self.incrementSize.setText(QtGui.QApplication.translate("filecarvingWidget", "512", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("filecarvingWidget", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.offset.setText(QtGui.QApplication.translate("filecarvingWidget", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.blockgap.setText(QtGui.QApplication.translate("filecarvingWidget", "16384", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("filecarvingWidget", "Block Gap", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("filecarvingWidget", "Fragment Size", None, QtGui.QApplication.UnicodeUTF8))
        self.processButton.setText(QtGui.QApplication.translate("filecarvingWidget", "Process", None, QtGui.QApplication.UnicodeUTF8))
