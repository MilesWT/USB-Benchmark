# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Benchmarking_input.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 509)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 141, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 3, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMaxLength(50)
        self.lineEdit_1.setFrame(False)
        self.lineEdit_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_2.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaxLength(50)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaxLength(50)
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaxLength(50)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QtCore.QRect(180, 50, 321, 41))
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setStyleSheet("color: rgb(255, 255, 0);\n"
"selection-color: rgb(85, 85, 255);\n"
"gridline-color: rgb(170, 255, 0);\n"
"border-color: rgb(170, 0, 0);")
        self.horizontalSlider.setMaximum(16)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.readCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.readCheckBox.setGeometry(QtCore.QRect(250, 150, 70, 17))
        self.readCheckBox.setChecked(True)
        self.readCheckBox.setObjectName("readCheckBox")
        self.writeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.writeCheckBox.setGeometry(QtCore.QRect(180, 150, 70, 17))
        self.writeCheckBox.setChecked(True)
        self.writeCheckBox.setObjectName("writeCheckBox")
        self.sliderLabelMin = QtWidgets.QLabel(self.centralwidget)
        self.sliderLabelMin.setGeometry(QtCore.QRect(180, 40, 47, 13))
        self.sliderLabelMin.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sliderLabelMin.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sliderLabelMin.setLineWidth(1)
        self.sliderLabelMin.setObjectName("sliderLabelMin")
        self.log = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(20, 320, 491, 151))
        self.log.setObjectName("log")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(180, 250, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(10, 200, 141, 41))
        self.saveButton.setObjectName("saveButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(10, 250, 141, 41))
        self.deleteButton.setObjectName("deleteButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 10, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 210, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setEnabled(True)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(180, 70, 321, 41))
        self.horizontalSlider_2.setMouseTracking(False)
        self.horizontalSlider_2.setMaximum(16)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setProperty("value", 16)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setInvertedAppearance(False)
        self.horizontalSlider_2.setInvertedControls(False)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.sliderLabelMax = QtWidgets.QLabel(self.centralwidget)
        self.sliderLabelMax.setGeometry(QtCore.QRect(470, 100, 51, 20))
        self.sliderLabelMax.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.sliderLabelMax.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sliderLabelMax.setLineWidth(1)
        self.sliderLabelMax.setObjectName("sliderLabelMax")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(420, 210, 91, 23))
        self.refresh.setObjectName("refresh")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 40, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 100, 101, 21))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 130, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 180, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 300, 491, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "USB Benchmarking"))
        self.radioButton.setText(_translate("MainWindow", "1"))
        self.radioButton_2.setText(_translate("MainWindow", "2"))
        self.radioButton_4.setText(_translate("MainWindow", "4"))
        self.radioButton_3.setText(_translate("MainWindow", "3"))
        self.lineEdit_1.setText(_translate("MainWindow", "Test 1"))
        self.lineEdit_1.setPlaceholderText(_translate("MainWindow", "Test 1"))
        self.lineEdit_2.setText(_translate("MainWindow", "Test 2"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Test 2"))
        self.lineEdit_4.setText(_translate("MainWindow", "Test 4"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Test 4"))
        self.lineEdit_3.setText(_translate("MainWindow", "Test 3"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Test 3"))
        self.label.setText(_translate("MainWindow", "Saved Tests"))
        self.label_2.setText(_translate("MainWindow", "Block Size"))
        self.readCheckBox.setText(_translate("MainWindow", "Read"))
        self.writeCheckBox.setText(_translate("MainWindow", "Write"))
        self.sliderLabelMin.setText(_translate("MainWindow", "1 KB"))
        self.log.setPlainText(_translate("MainWindow", "Logs/History\n"
""))
        self.runButton.setText(_translate("MainWindow", "Run Test"))
        self.saveButton.setText(_translate("MainWindow", "Save Test"))
        self.deleteButton.setText(_translate("MainWindow", "Delete Test"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-- Select USB Device --"))
        self.comboBox.setItemText(1, _translate("MainWindow", " "))
        self.sliderLabelMax.setText(_translate("MainWindow", "64 MB"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_5.setText(_translate("MainWindow", "Lowest Block Size"))
        self.label_7.setText(_translate("MainWindow", "Highest Block Size"))
        self.label_3.setText(_translate("MainWindow", "Tests To Run"))
        self.label_9.setText(_translate("MainWindow", "Device To Test"))

