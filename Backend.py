import sys
from ast import literal_eval
import os
import time
import numpy
import pandas
from PyQt5 import QtGui, QtWidgets, uic
import Benchmarking_input  # import the GUI layout
import Benchmarking_output  # import the GUI layout
import wmicAPI  # import stuff for usb
import save_state  # Creates savefile.json and initializes it, saves to it, and loads from it.

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


        # initialize globals here
        self.globalVariables = 0
        self.devices = wmicAPI.getDevices()
        self.radio_index = 0
        self.prev_radio_index = 0
        self.ButtonGroup = QtWidgets.QButtonGroup()
        self.ButtonGroup.addButton(self.ui.radioButton_1, 0)
        self.ButtonGroup.addButton(self.ui.radioButton_2, 1)
        self.ButtonGroup.addButton(self.ui.radioButton_3, 2)
        self.ButtonGroup.addButton(self.ui.radioButton_4, 3)
        self.initDevices()
        self.loadTest()


        # All event connections will go here:
        self.ui.runButton.pressed.connect(self.runButtonPressed)
        self.ui.runButton.released.connect(self.runButtonReleased)
        self.ui.refresh.clicked.connect(self.initDevices)
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider_2))
        self.ButtonGroup.buttonClicked[int].connect(self.radioButtonClick)
        self.ui.saveButton.clicked.connect(self.saveTest)

    def initDevices(self):
        #initializes the combo box with all connected devices

        self.devices = wmicAPI.getDevices() #get the updated list of devices

        for i in range(self.ui.comboBox.count(), 1, -1): #remove the current list
            self.ui.comboBox.removeItem(i)

        if len(self.devices):
            for i in range(0, len(self.devices['DeviceID'])): #update with new list
                self.ui.comboBox.addItem(str(self.devices['DeviceID'][i]) + "  " + str(self.devices['VolumeName'][i]))

    def addText(self,string):
        self.ui.log.appendPlainText(string)

    def sliderText(self, slider):
        #update the slider text when it moves
        num = numpy.power(2, slider.value())
        txt = (str(num) + " KB") if num < 1024 else (str(int(num/1024)) + " MB")

        if slider == self.ui.horizontalSlider:
            if slider.value() > self.ui.horizontalSlider_2.value():
                self.ui.horizontalSlider_2.setValue(slider.value())
            self.ui.sliderLabelMin.setText(txt)
            self.addText("Lowest Block Size: " + txt)
        elif slider == self.ui.horizontalSlider_2:
            if slider.value() < self.ui.horizontalSlider.value():
                self.ui.horizontalSlider.setValue(slider.value())
            self.ui.sliderLabelMax.setText(txt)
            self.addText("Highest Block Size: " + txt)

    def radioButtonClick(self):
        self.radioIndex()
        self.saveTest(self.prev_radio_index)
        self.loadTest()
        self.enableTextbox()

    def saveTest(self, index=None):
        if index is None:
            index = self.radio_index

        if index == 0:
            test_name = self.ui.lineEdit_1.text()
        elif index == 1:
            test_name = self.ui.lineEdit_2.text()
        elif index == 2:
            test_name = self.ui.lineEdit_3.text()
        elif index == 3:
            test_name = self.ui.lineEdit_4.text()
        else:
            pass
        slider_min = self.ui.horizontalSlider.value()
        slider_max = self.ui.horizontalSlider_2.value()
        read_checkbox = self.ui.readCheckBox.isChecked()
        write_checkbox = self.ui.writeCheckBox.isChecked()
        save_state.save_state(index, test_name, slider_min, slider_max, read_checkbox, write_checkbox)
        self.addText("\r\nSaved Test: " + test_name)

    def loadTest(self):
        name, slider_min, slider_max, read_checkbox, write_checkbox = save_state.load_radio_button(self.radio_index)

        self.ui.horizontalSlider.setValue(int(slider_min))
        self.ui.horizontalSlider_2.setValue(int(slider_max))
        self.ui.readCheckBox.setChecked(literal_eval(read_checkbox))
        self.ui.writeCheckBox.setChecked(literal_eval(write_checkbox))

    def radioIndex(self):
        self.prev_radio_index = self.radio_index
        self.radio_index = [self.ButtonGroup.buttons()[x].isChecked() for x in
                            range(len(self.ButtonGroup.buttons()))].index(True)

    def enableTextbox(self):
        self.ui.lineEdit_1.setEnabled(False)
        self.ui.lineEdit_2.setEnabled(False)
        self.ui.lineEdit_3.setEnabled(False)
        self.ui.lineEdit_4.setEnabled(False)

        if self.radio_index == 0:
            self.ui.lineEdit_1.setEnabled(True)
        elif self.radio_index == 1:
            self.ui.lineEdit_2.setEnabled(True)
        elif self.radio_index == 2:
            self.ui.lineEdit_3.setEnabled(True)
        elif self.radio_index == 3:
            self.ui.lineEdit_4.setEnabled(True)
        else:
            pass

    def runButtonPressed(self):
        # helper function to display 'running' while running application
        self.ui.runButton.setText("Running")

    def runButtonReleased(self):
        GUI_out.show()

class OutputUi(QtWidgets.QMainWindow, Benchmarking_output.Ui_MainWindow):

    def __init__(self):
        #initialization functions go here (including globals for this file):
        QtWidgets.QMainWindow.__init__(self)
        self.ui_2 = Benchmarking_output.Ui_MainWindow()
        self.ui_2.setupUi(self)
        pixmap = QtGui.QPixmap('Resources/demo_graph.png')
        self.ui_2.Graph.setPixmap(pixmap)#.scaled(550,225))

    def setParameters(self):
        self.ui_2.deviceName.setText("boooobs")
        self.ui_2.size.setText("boooobs")
        self.ui_2.serialNumber.setText("boooobs")
        self.ui_2.mountPoint.setText("boooobs")
        self.ui_2.format.setText("boooobs")
        self.ui_2.freeSpace.setText("boooobs")

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