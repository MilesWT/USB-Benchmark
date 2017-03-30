import sys
import os
import time
import numpy
import pandas
from PyQt5 import QtGui, QtWidgets, uic
import Benchmarking_input # import the GUI layout
import Benchmarking_output # import the GUI layout
import wmicAPI # import stuff for usb
import save_state # Creates savefile.json and initializes it, saves to it, and loads from it.

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class InputUi(QtWidgets.QMainWindow, Benchmarking_input.Ui_MainWindow):

    def __init__(self):
        # Initialization functions go here (including globals for this file):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Benchmarking_input.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.refresh.setIcon(QtGui.QIcon('Resources/reload.png'))
        
        # Load test label names from savefile.json
        name1, name2, name3, name4 = save_state.load_all_names()
        self.ui.lineEdit_1.setText(name1)
        self.ui.lineEdit_2.setText(name2)
        self.ui.lineEdit_3.setText(name3)
        self.ui.lineEdit_4.setText(name4)

        # Initialize globals here
        self.globalVariables = 0
        self.devices = wmicAPI.getDevices()
        self.initDevices()

        # All event connections will go here:
        self.ui.runButton.pressed.connect(self.updateText)
        self.ui.refresh.clicked.connect(self.initDevices)
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider_2))
        self.ui.radioButton_1.toggled.connect(self.loadTest)
        self.ui.radioButton_2.toggled.connect(self.loadTest)
        self.ui.radioButton_3.toggled.connect(self.loadTest)
        self.ui.radioButton_4.toggled.connect(self.loadTest)
        self.ui.saveButton.clicked.connect(self.saveTest)

    def initDevices(self):
        # Iinitializes the combo box with all connected devices

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



    def saveTest(self):
        if self.ui.radioButton_1.isChecked():
            radio_index = 0
            test_name = self.ui.lineEdit_1.text()
        elif self.ui.radioButton_2.isChecked():
            radio_index = 1
            test_name = self.ui.lineEdit_2.text()
        elif self.ui.radioButton_3.isChecked():
            radio_index = 2
            test_name = self.ui.lineEdit_3.text()
        elif self.ui.radioButton_4.isChecked():
            radio_index = 3
            test_name = self.ui.lineEdit_4.text()
        else:
            pass
        slider_min = self.ui.horizontalSlider.value()
        slider_max = self.ui.horizontalSlider_2.value()
        read_checkbox = self.ui.readCheckBox.isChecked()
        write_checkbox = self.ui.writeCheckBox.isChecked()
        save_state.save_state(radio_index, test_name, slider_min, slider_max, read_checkbox, write_checkbox)

    def loadTest(self):
        if self.ui.radioButton_1.isChecked():
            radio_index = 0
        elif self.ui.radioButton_2.isChecked():
            radio_index = 1
        elif self.ui.radioButton_3.isChecked():
            radio_index = 2
        elif self.ui.radioButton_4.isChecked():
            radio_index = 3
        else:
            pass

        name, slider_min, slider_max, read_checkbox, write_checkbox = save_state.load_radio_button(radio_index)

        if self.ui.radioButton_1.isChecked():
            self.ui.lineEdit_1.setText(name)
        elif self.ui.radioButton_2.isChecked():
            self.ui.lineEdit_2.setText(name)
        elif self.ui.radioButton_3.isChecked():
            self.ui.lineEdit_3.setText(name)
        elif self.ui.radioButton_4.isChecked():
            self.ui.lineEdit_4.setText(name)
        else:
            pass

        self.ui.horizontalSlider.setValue(slider_min)
        self.ui.horizontalSlider_2.setValue(slider_max)
        self.ui.readCheckBox.setChecked(read_checkbox)
        self.ui.writeCheckBox.setChecked(write_checkbox)


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