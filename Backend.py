import sys
import os
import time
import numpy
import pandas
from PyQt5 import QtGui, QtWidgets, uic
import Benchmarking_input #import the GUI layout
import Benchmarking_output #import the GUI layout
import wmicAPI #import stuff for usb

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class InputUi(QtWidgets.QMainWindow, Benchmarking_input.Ui_MainWindow):

    def __init__(self):
        #initialization functions go here (including globals for this file):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Benchmarking_input.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.refresh.setIcon(QtGui.QIcon('Resources/reload.png'))

        # initialize globals here
        self.globalVariables = 0
        self.devices = wmicAPI.getDevices()
        self.initDevices()

        # All event connections will go here:
        self.ui.runButton.pressed.connect(self.updateText)
        self.ui.refresh.clicked.connect(self.initDevices)
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider_2))

        #self.ui.saveButton.clicked.connect(self.saveTest)

    def initDevices(self):
        #initializes the combo box with all connected devices

        self.devices = wmicAPI.getDevices() #get the updated list of devices

        for i in range(self.ui.comboBox.count(),1,-1): #remove the current list
            self.ui.comboBox.removeItem(i)

        if len(self.devices):
            for i in range(0, len(self.devices['DeviceID'])): #update with new list
                self.ui.comboBox.addItem(str(self.devices['DeviceID'][i]) + "  " + str(self.devices['VolumeName'][i]))

    def updateText(self):
        # helper function to display 'running' while running application
        self.ui.runButton.setText("Running")

    def sliderText(self, slider):
        #update the slider text when it moves
        num = numpy.power(2, slider.value())
        txt = (str(num) + " KB") if num < 1024 else (str(int(num/1024)) + " MB")

        if slider == self.ui.horizontalSlider:
            if slider.value() > self.ui.horizontalSlider_2.value():
                self.ui.horizontalSlider_2.setValue(slider.value())
            self.ui.sliderLabelMin.setText(txt)
            self.ui.log.appendPlainText("Lowest Block Size: "+txt)
        elif slider == self.ui.horizontalSlider_2:
            if slider.value() < self.ui.horizontalSlider.value():
                self.ui.horizontalSlider.setValue(slider.value())
            self.ui.sliderLabelMax.setText(txt)
            self.ui.log.appendPlainText("Highest Block Size: "+txt)



    #def saveTest(self):
   #     for rb in [self.ui.radioButton]


class OutputUi(QtWidgets.QMainWindow, Benchmarking_output.Ui_MainWindow):

    def __init__(self):
        #initialization functions go here (including globals for this file):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Benchmarking_output.Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == '__main__':
    # This is the first operation  to be run on startup.
    # AKA the 'Main' function
    app = QtWidgets.QApplication(sys.argv)
    GUI_in = InputUi()
    GUI_out = OutputUi()
    ui = Benchmarking_input.Ui_MainWindow()
    GUI_in.show()
    #GUI_out.show()
    sys.exit(app.exec_())