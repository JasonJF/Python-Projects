from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

import pandas as pd
import datetime

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        ## MY CODE ##

        df = pd.read_csv('BIM_Temp.csv')
        
        #All
        win = pg.GraphicsWindow()
        x = df['DateTime']
        xdict = dict(enumerate(x))
        # print([xdict.values()])
        x_values = list(xdict.keys())
        y_milli = df['EraTemperatureMilliDegC']
        tempURA_dict = df['UcTemperatureMilliDegC']
        tempURA_map = map(lambda num: (num/1000),tempURA_dict)
        tempURA = list(tempURA_map)
        y_map = map(lambda num: (num/1000),y_milli) #convert from milli degrees to degrees
        y = list(y_map)                             #unpack the map object

        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        # plot = win.addPlot(axisItems={'bottom': stringaxis})
        # curve = plot.plot([xdict.keys()],y)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        # print(xdict)
        # self.graphWidget.plot(x_values, y)
        self.graphWidget.plot(x_values,tempURA)
        # self.graphWidget.addPlot(x_values, y)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()