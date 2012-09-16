# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_carving_ui.ui'
#
# Created: Sun Sep 16 18:34:21 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_filecarvingWidget(object):
    def setupUi(self, filecarvingWidget):
        filecarvingWidget.setObjectName("filecarvingWidget")
        filecarvingWidget.resize(500, 568)
        filecarvingWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalLayout_4 = QtGui.QVBoxLayout(filecarvingWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtGui.QTabWidget(filecarvingWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_general = QtGui.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_general)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.srcdstLayout = QtGui.QGridLayout()
        self.srcdstLayout.setObjectName("srcdstLayout")
        self.inputFile = QtGui.QLineEdit(self.tab_general)
        self.inputFile.setEnabled(True)
        self.inputFile.setText("")
        self.inputFile.setObjectName("inputFile")
        self.srcdstLayout.addWidget(self.inputFile, 1, 0, 1, 1)
        self.inputFileButton = QtGui.QPushButton(self.tab_general)
        self.inputFileButton.setObjectName("inputFileButton")
        self.srcdstLayout.addWidget(self.inputFileButton, 1, 1, 1, 1)
        self.outputDirButton = QtGui.QPushButton(self.tab_general)
        self.outputDirButton.setObjectName("outputDirButton")
        self.srcdstLayout.addWidget(self.outputDirButton, 3, 1, 1, 1)
        self.outputDir = QtGui.QLineEdit(self.tab_general)
        self.outputDir.setEnabled(True)
        self.outputDir.setText("")
        self.outputDir.setObjectName("outputDir")
        self.srcdstLayout.addWidget(self.outputDir, 3, 0, 1, 1)
        self.fsInfo = QtGui.QLabel(self.tab_general)
        self.fsInfo.setObjectName("fsInfo")
        self.srcdstLayout.addWidget(self.fsInfo, 2, 0, 1, 1)
        self.outputDirInfo = QtGui.QLabel(self.tab_general)
        self.outputDirInfo.setObjectName("outputDirInfo")
        self.srcdstLayout.addWidget(self.outputDirInfo, 4, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.srcdstLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_15 = QtGui.QLabel(self.tab_general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.recoverfiletypes = QtGui.QComboBox(self.tab_general)
        self.recoverfiletypes.setEditable(False)
        self.recoverfiletypes.setObjectName("recoverfiletypes")
        self.horizontalLayout.addWidget(self.recoverfiletypes)
        self.label_16 = QtGui.QLabel(self.tab_general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.strength = QtGui.QSpinBox(self.tab_general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strength.sizePolicy().hasHeightForWidth())
        self.strength.setSizePolicy(sizePolicy)
        self.strength.setMinimum(1)
        self.strength.setMaximum(100)
        self.strength.setObjectName("strength")
        self.horizontalLayout.addWidget(self.strength)
        self.showResults = QtGui.QCheckBox(self.tab_general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showResults.sizePolicy().hasHeightForWidth())
        self.showResults.setSizePolicy(sizePolicy)
        self.showResults.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.showResults.setObjectName("showResults")
        self.horizontalLayout.addWidget(self.showResults)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.imageView = QtGui.QGraphicsView(self.tab_general)
        self.imageView.setObjectName("imageView")
        self.verticalLayout_2.addWidget(self.imageView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressLabel = QtGui.QLabel(self.tab_general)
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout_2.addWidget(self.progressLabel)
        self.progressBar = QtGui.QProgressBar(self.tab_general)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.duration = QtGui.QLabel(self.tab_general)
        self.duration.setObjectName("duration")
        self.horizontalLayout_2.addWidget(self.duration)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtGui.QLabel(self.tab_general)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.maxCPUs = QtGui.QComboBox(self.tab_general)
        self.maxCPUs.setObjectName("maxCPUs")
        self.horizontalLayout_3.addWidget(self.maxCPUs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.actionLayout = QtGui.QHBoxLayout()
        self.actionLayout.setObjectName("actionLayout")
        self.classifyButton = QtGui.QPushButton(self.tab_general)
        self.classifyButton.setObjectName("classifyButton")
        self.actionLayout.addWidget(self.classifyButton)
        self.reassembleButton = QtGui.QPushButton(self.tab_general)
        self.reassembleButton.setEnabled(False)
        self.reassembleButton.setObjectName("reassembleButton")
        self.actionLayout.addWidget(self.reassembleButton)
        self.processButton = QtGui.QPushButton(self.tab_general)
        self.processButton.setObjectName("processButton")
        self.actionLayout.addWidget(self.processButton)
        self.verticalLayout_2.addLayout(self.actionLayout)
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_preprocessing = QtGui.QWidget()
        self.tab_preprocessing.setObjectName("tab_preprocessing")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_preprocessing)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtGui.QGroupBox(self.tab_preprocessing)
        self.groupBox_3.setObjectName("groupBox_3")
        self.fsLayout = QtGui.QGridLayout(self.groupBox_3)
        self.fsLayout.setObjectName("fsLayout")
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.fsLayout.addWidget(self.label, 0, 0, 1, 1)
        self.fragmentSize = QtGui.QLineEdit(self.groupBox_3)
        self.fragmentSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fragmentSize.setObjectName("fragmentSize")
        self.fsLayout.addWidget(self.fragmentSize, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.fsLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.offset = QtGui.QLineEdit(self.groupBox_3)
        self.offset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.offset.setObjectName("offset")
        self.fsLayout.addWidget(self.offset, 0, 4, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.fsLayout.addWidget(self.label_14, 0, 5, 1, 1)
        self.partitionOffset = QtGui.QLineEdit(self.groupBox_3)
        self.partitionOffset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.partitionOffset.setObjectName("partitionOffset")
        self.fsLayout.addWidget(self.partitionOffset, 0, 6, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_preprocessing)
        self.groupBox_2.setObjectName("groupBox_2")
        self.fragmentizerLayout = QtGui.QGridLayout(self.groupBox_2)
        self.fragmentizerLayout.setObjectName("fragmentizerLayout")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.fragmentizerLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.blockGap = QtGui.QLineEdit(self.groupBox_2)
        self.blockGap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blockGap.setObjectName("blockGap")
        self.fragmentizerLayout.addWidget(self.blockGap, 0, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.fragmentizerLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.minimumFragmentSize = QtGui.QLineEdit(self.groupBox_2)
        self.minimumFragmentSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minimumFragmentSize.setObjectName("minimumFragmentSize")
        self.fragmentizerLayout.addWidget(self.minimumFragmentSize, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtGui.QLabel(self.tab_preprocessing)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.preprocessing = QtGui.QComboBox(self.tab_preprocessing)
        self.preprocessing.setObjectName("preprocessing")
        self.gridLayout_2.addWidget(self.preprocessing, 0, 1, 1, 1)
        self.blockStatus = QtGui.QComboBox(self.tab_preprocessing)
        self.blockStatus.setObjectName("blockStatus")
        self.gridLayout_2.addWidget(self.blockStatus, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_preprocessing)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.resultTable = QtGui.QTableView(self.tab_preprocessing)
        self.resultTable.setObjectName("resultTable")
        self.verticalLayout_3.addWidget(self.resultTable)
        self.tabWidget.addTab(self.tab_preprocessing, "")
        self.tab_reassembly = QtGui.QWidget()
        self.tab_reassembly.setObjectName("tab_reassembly")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_reassembly)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidgetReassembly = QtGui.QTabWidget(self.tab_reassembly)
        self.tabWidgetReassembly.setObjectName("tabWidgetReassembly")
        self.tabVideo = QtGui.QWidget()
        self.tabVideo.setObjectName("tabVideo")
        self.layoutWidget = QtGui.QWidget(self.tabVideo)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 460, 95))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.minPicSize = QtGui.QLineEdit(self.layoutWidget)
        self.minPicSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.minPicSize.setObjectName("minPicSize")
        self.gridLayout.addWidget(self.minPicSize, 0, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.similarityVideo = QtGui.QLineEdit(self.layoutWidget)
        self.similarityVideo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.similarityVideo.setObjectName("similarityVideo")
        self.gridLayout.addWidget(self.similarityVideo, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.headerSize = QtGui.QLineEdit(self.layoutWidget)
        self.headerSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.headerSize.setObjectName("headerSize")
        self.gridLayout.addWidget(self.headerSize, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.extractSize = QtGui.QLineEdit(self.layoutWidget)
        self.extractSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.extractSize.setObjectName("extractSize")
        self.gridLayout.addWidget(self.extractSize, 1, 3, 1, 1)
        self.tabWidgetReassembly.addTab(self.tabVideo, "")
        self.tabJpeg = QtGui.QWidget()
        self.tabJpeg.setObjectName("tabJpeg")
        self.layoutWidget_2 = QtGui.QWidget(self.tabJpeg)
        self.layoutWidget_2.setGeometry(QtCore.QRect(19, 10, 431, 95))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_18 = QtGui.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)
        self.similarityJpeg = QtGui.QLineEdit(self.layoutWidget_2)
        self.similarityJpeg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.similarityJpeg.setObjectName("similarityJpeg")
        self.gridLayout_3.addWidget(self.similarityJpeg, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.layoutWidget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
        self.headerSize_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.headerSize_2.setEnabled(False)
        self.headerSize_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.headerSize_2.setObjectName("headerSize_2")
        self.gridLayout_3.addWidget(self.headerSize_2, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.tabWidgetReassembly.addTab(self.tabJpeg, "")
        self.verticalLayout.addWidget(self.tabWidgetReassembly)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtGui.QLabel(self.tab_reassembly)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.outputformat = QtGui.QComboBox(self.tab_reassembly)
        self.outputformat.setObjectName("outputformat")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.outputformat)
        self.label_2 = QtGui.QLabel(self.tab_reassembly)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.assemblyMethod = QtGui.QComboBox(self.tab_reassembly)
        self.assemblyMethod.setObjectName("assemblyMethod")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.assemblyMethod)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.fileTable = QtGui.QTableView(self.tab_reassembly)
        self.fileTable.setObjectName("fileTable")
        self.horizontalLayout_11.addWidget(self.fileTable)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_reassembly, "")
        self.verticalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(filecarvingWidget)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidgetReassembly.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(filecarvingWidget)

    def retranslateUi(self, filecarvingWidget):
        filecarvingWidget.setWindowTitle(QtGui.QApplication.translate("filecarvingWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.inputFileButton.setText(QtGui.QApplication.translate("filecarvingWidget", "&Data Source", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirButton.setText(QtGui.QApplication.translate("filecarvingWidget", "&Export Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.fsInfo.setText(QtGui.QApplication.translate("filecarvingWidget", "FS Info: ", None, QtGui.QApplication.UnicodeUTF8))
        self.outputDirInfo.setText(QtGui.QApplication.translate("filecarvingWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("filecarvingWidget", "Files to recover", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("filecarvingWidget", "Strength", None, QtGui.QApplication.UnicodeUTF8))
        self.showResults.setText(QtGui.QApplication.translate("filecarvingWidget", "Show Results:", None, QtGui.QApplication.UnicodeUTF8))
        self.progressLabel.setText(QtGui.QApplication.translate("filecarvingWidget", "progressLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.duration.setText(QtGui.QApplication.translate("filecarvingWidget", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("filecarvingWidget", "Max CPUs:", None, QtGui.QApplication.UnicodeUTF8))
        self.classifyButton.setText(QtGui.QApplication.translate("filecarvingWidget", "&Classify", None, QtGui.QApplication.UnicodeUTF8))
        self.reassembleButton.setText(QtGui.QApplication.translate("filecarvingWidget", "&Reassemble", None, QtGui.QApplication.UnicodeUTF8))
        self.processButton.setText(QtGui.QApplication.translate("filecarvingWidget", "&Process (do it all)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QtGui.QApplication.translate("filecarvingWidget", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("filecarvingWidget", "File System Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("filecarvingWidget", "Block Size [Bytes]", None, QtGui.QApplication.UnicodeUTF8))
        self.fragmentSize.setText(QtGui.QApplication.translate("filecarvingWidget", "512", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("filecarvingWidget", "Offset [Bytes]", None, QtGui.QApplication.UnicodeUTF8))
        self.offset.setText(QtGui.QApplication.translate("filecarvingWidget", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("filecarvingWidget", "Partition Offset [ignored]", None, QtGui.QApplication.UnicodeUTF8))
        self.partitionOffset.setText(QtGui.QApplication.translate("filecarvingWidget", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("filecarvingWidget", "Fragmentizer Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("filecarvingWidget", "Block Gap [Sector]", None, QtGui.QApplication.UnicodeUTF8))
        self.blockGap.setText(QtGui.QApplication.translate("filecarvingWidget", "32", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("filecarvingWidget", "Minimum Fragment Size [Sector]", None, QtGui.QApplication.UnicodeUTF8))
        self.minimumFragmentSize.setStatusTip(QtGui.QApplication.translate("filecarvingWidget", "Minimum fragment size in blocks", None, QtGui.QApplication.UnicodeUTF8))
        self.minimumFragmentSize.setText(QtGui.QApplication.translate("filecarvingWidget", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("filecarvingWidget", "Preprocessing: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("filecarvingWidget", "Block status: ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_preprocessing), QtGui.QApplication.translate("filecarvingWidget", "Preprocessing", None, QtGui.QApplication.UnicodeUTF8))
        self.minPicSize.setText(QtGui.QApplication.translate("filecarvingWidget", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("filecarvingWidget", "MinPicSize (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("filecarvingWidget", "Similarity", None, QtGui.QApplication.UnicodeUTF8))
        self.similarityVideo.setText(QtGui.QApplication.translate("filecarvingWidget", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("filecarvingWidget", "Header Size (bytes)", None, QtGui.QApplication.UnicodeUTF8))
        self.headerSize.setStatusTip(QtGui.QApplication.translate("filecarvingWidget", "Size of the header in bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.headerSize.setText(QtGui.QApplication.translate("filecarvingWidget", "256", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("filecarvingWidget", "Extract Size (kB)", None, QtGui.QApplication.UnicodeUTF8))
        self.extractSize.setStatusTip(QtGui.QApplication.translate("filecarvingWidget", "Size of the subfragment to forward to the decoder", None, QtGui.QApplication.UnicodeUTF8))
        self.extractSize.setText(QtGui.QApplication.translate("filecarvingWidget", "90", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetReassembly.setTabText(self.tabWidgetReassembly.indexOf(self.tabVideo), QtGui.QApplication.translate("filecarvingWidget", "Video", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("filecarvingWidget", "Similarity", None, QtGui.QApplication.UnicodeUTF8))
        self.similarityJpeg.setText(QtGui.QApplication.translate("filecarvingWidget", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("filecarvingWidget", "Header Size (bytes)", None, QtGui.QApplication.UnicodeUTF8))
        self.headerSize_2.setStatusTip(QtGui.QApplication.translate("filecarvingWidget", "Size of the header in bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.headerSize_2.setText(QtGui.QApplication.translate("filecarvingWidget", "256", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetReassembly.setTabText(self.tabWidgetReassembly.indexOf(self.tabJpeg), QtGui.QApplication.translate("filecarvingWidget", "JPEG", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("filecarvingWidget", "Output Format:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("filecarvingWidget", "Assembly Method", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reassembly), QtGui.QApplication.translate("filecarvingWidget", "Reassembly", None, QtGui.QApplication.UnicodeUTF8))

