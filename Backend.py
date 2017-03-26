import sys
import os
import time
import numpy
import pandas
from PyQt5 import QtGui, QtWidgets, uic
import Benchmarking_input #import the GUI layout
import Benchmarking_output #import the GUI layout

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class InputUi(QtWidgets.QMainWindow, Benchmarking_input.Ui_MainWindow):

    def __init__(self):
        #initialization functions go here (including globals for this file):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Benchmarking_input.Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize globals here
        self.globalVariables = 0

        # All event connections will go here:
        self.ui.runButton.pressed.connect(self.updateText)
        self.ui.horizontalSlider.valueChanged.connect(self.sliderText)

    def updateText(self):
        # helper function to display 'running' while running application
        self.ui.runButton.setText("Running")

    def sliderText(self):
        num = numpy.power(2, self.ui.horizontalSlider.value())
        txt = (str(num) + " KB") if num < 1024 else (str(int(num/1024)) + " MB")
        self.ui.sliderLabel.setText(txt)

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