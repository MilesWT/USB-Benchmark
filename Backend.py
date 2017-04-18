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
import matplotlib.ticker as mtick


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
        self.sliderText(self.ui.horizontalSlider)
        self.sliderText(self.ui.horizontalSlider_2)
        self.GUI_out = []

        # All event connections will go here:
        self.ui.runButton.pressed.connect(self.runButtonPressed)
        self.ui.runButton.released.connect(self.runButtonReleased)
        self.ui.refresh.clicked.connect(self.initDevices)
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.sliderText(self.ui.horizontalSlider_2))
        self.ButtonGroup.buttonClicked[int].connect(self.radioButtonClick)
        self.ui.saveButton.clicked.connect(self.saveTest)


    # def closeEvent(self, event):
    #
    #     quit_msg = "Are you sure you want to exit the program?"
    #     reply = QtGui.QMessageBox.question(self, 'Message',
    #                                        quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    #
    #     if reply == QtGui.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    def initDevices(self):
        # initializes the combo box with all connected devices

        self.devices = wmicAPI.getDevices()  # get the updated list of devices

        for i in range(self.ui.comboBox.count(), 1, -1):  # remove the current list
            self.ui.comboBox.removeItem(i)

        if len(self.devices):
            for i in range(0, len(self.devices['DeviceID'])):  # update with new list
                if str(self.devices['VolumeName'][i]) == '':
                    devName = '**No Name**'
                else:
                    devName = str(self.devices['VolumeName'][i])
                self.ui.comboBox.addItem(str(self.devices['DeviceID'][i]) + "   " + devName)
            self.ui.comboBox.setCurrentIndex(2)

    def addText(self, string):
        self.ui.log.appendPlainText(string)

    def sliderText(self, slider):
        # update the slider text when it moves
        num = numpy.power(2, slider.value())
        txt = (str(num) + " KB") if num < 1024 else (str(int(num / 1024)) + " MB")

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
        self.saveTest()


    def runButtonReleased(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if self.ui.comboBox.currentIndex() < 2: #if a usb device has not been selected
            msg.setText("Please select a valid USB Storage Device")
            msg.setWindowTitle("Selection Error")
            msg.exec()
        elif self.ui.writeCheckBox.isChecked() is not True and self.ui.readCheckBox.isChecked() is not True:
            msg.setText("Please Select Read and/or Write for Tests to be Run")
            msg.setWindowTitle("Selection Error")
            msg.exec()
        else:  #run
            serial_num = str(self.devices['VolumeSerialNumber'][int(self.ui.comboBox.currentIndex() - 2)])
            self.GUI_out = OutputUi()
            self.GUI_out.setParameters(serial_num)
            self.GUI_out.show()
            self.ui.runButton.setText("Run Test")


class OutputUi(QtWidgets.QMainWindow, Benchmarking_output.Ui_MainWindow):
    def __init__(self):
        # initialization functions go here (including globals for this file):
        QtWidgets.QMainWindow.__init__(self)
        self.ui_2 = Benchmarking_output.Ui_MainWindow()
        self.ui_2.setupUi(self)

        self.devices = wmicAPI.getDevices()  # get the updated list of devices

        print(self.devices)
        #pixmap = QtGui.QPixmap('Resources/demo_graph.png')
        #self.ui_2.Graph.setPixmap(pixmap)  # .scaled(550,225))

        #self.setParameters()

    def setParameters(self, serial_num):
        if len(self.devices):
            self.dev_num = self.devices['VolumeSerialNumber'].index(str(serial_num))
            # for i in range(0, len(self.devices['DeviceID'])): #update with new list
            # self.ui.comboBox.addItem(str(self.devices['DeviceID'][i]) + "  " + str(self.devices['VolumeName'][i]))
            if str(self.devices['VolumeName'][self.dev_num]) == '':
                self.ui_2.deviceName.setText('**No Name**')
            else:
                self.ui_2.deviceName.setText(str(self.devices['VolumeName'][int(self.dev_num)]))
            self.ui_2.size.setText(str(int(int(self.devices['Size'][int(self.dev_num)]) / (1024 * 1024))) + " MB")
            self.ui_2.serialNumber.setText(str(self.devices['VolumeSerialNumber'][int(self.dev_num)]))
            self.ui_2.mountPoint.setText(str(self.devices['DeviceID'][int(self.dev_num)]))
            self.ui_2.format.setText(str(self.devices['FileSystem'][int(self.dev_num)]))
            self.ui_2.freeSpace.setText(str(self.devices['Description'][int(self.dev_num)]))

            self.graphing()

    def graphing(self):
        #print(wmicAPI.writeBlock("G", 1000))
        qqq = ReadGraph(devices=self.devices,dev_num=self.dev_num)
        self.ui_2.gridLayout.addWidget(qqq)


# Plotting functions are created as separate classes
class ReadGraph(FigureCanvas):
    # prototype or creating a plot
    def __init__(self, devices=[], dev_num=0, parent=None, width=5, height=4, dpi=100):
        #fig = Figure(figsize=(width, height), dpi=dpi)

        fig = Figure()
        #fig.remove()
        fig.clf()

        self.file_size = 10 #10MB file
        self.block_size_data = []
        self.read_data = []
        self.write_data = []

        self.read = GUI_in.ui.readCheckBox.isChecked()
        self.write = GUI_in.ui.writeCheckBox.isChecked()

        #self.ax1.close()
        self.ax1 = fig.add_subplot(111)
        self.ax2 = fig.add_subplot(111)
        self.ax1.cla()
        self.ax2.cla()

        self.compute_initial_figure(devices, dev_num)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        # FigureCanvas.setSizePolicy(self,
        #                            QtWidgets.QSizePolicy.Expanding,
        #                            QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self, devices, dev_num):
        self.ax1.cla()
        self.ax2.cla()

        self.block_size_data, self.write_data, self.read_data = wmicAPI.benchmarkDevice(
            letterDrive=str(devices['DeviceID'][dev_num]).strip(':'),
            smallBlockSize=int(GUI_in.ui.horizontalSlider.value()),
            bigBlockSize=int(GUI_in.ui.horizontalSlider_2.value()),
            fileSize=int(self.file_size),
            write=bool(GUI_in.ui.writeCheckBox.isChecked()),
            read=bool(GUI_in.ui.readCheckBox.isChecked()))
        print(self.block_size_data)
        print(self.write_data)
        print(self.read_data)
        #print(GUI_in.ui.readCheckBox.isChecked())

        if self.read:
            self.ax1.plot(self.block_size_data, self.read_data, label='Read',color='b')
            self.ax1.set_xscale('log', basex=2)
            self.ax1.set_xlabel('Block Size (KB)')
            self.ax1.set_ylabel('Read Speed (sec)', color='b')
            self.ax1.xaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))

            if self.write:
                self.ax2 = self.ax1.twinx()
                self.ax2.plot(self.block_size_data, self.write_data, label='Write', color='r')
                self.ax2.set_ylabel('Write Speed (sec)', color='r')
        elif self.write:
            self.ax1.plot(self.block_size_data, self.write_data, label='Write', color='r')
            self.ax1.set_xscale('log', basex=2)
            self.ax1.set_xlabel('Block Size (KB)')
            self.ax1.set_ylabel('Write Speed (sec)', color='r')
            self.ax1.xaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))
        #self.ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%4f'))


if __name__ == '__main__':
    # This is the first operation  to be run on startup.
    app = QtWidgets.QApplication(sys.argv)
    GUI_in = InputUi()

    ui = Benchmarking_input.Ui_MainWindow()
    GUI_in.show()
    # GUI_out.show()
    sys.exit(app.exec_())
