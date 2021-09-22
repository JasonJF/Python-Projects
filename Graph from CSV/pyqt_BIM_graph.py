import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
import pyqtgraph as pg
import pandas as pd
import numpy as np
import datetime

from pyqtgraph.graphicsItems.PlotItem.PlotItem import PlotItem


app = QApplication(sys.argv)
pg.setConfigOption('background', 'w')
# win = pg.plot()
qgv = QGraphicsView()
# pItem = PlotItem()
graphWindow1 = PlotItem()
graphWindow2 = pg.ViewBox()

pg.setConfigOptions(antialias=True)

#Get data from file
df = pd.read_csv('output.csv')



#store data in variables and format
x_raw = df['DateTime']
bim_P_Out_raw = df['EraBimPowerOutMilliV']
print(bim_P_Out_raw)
tempERA_raw = df['EraTemperatureMilliDegC']
tempURA_raw = df['UcTemperatureMilliDegC']
bim_1_G_raw = df['EraBimPower1GHzMilliV']
xdict = dict(enumerate(x_raw))
# print([xdict.values()])
x_values = list(xdict.keys())

#convert to correct scale and units
tempURA_map = map(lambda num: (num/20),tempURA_raw)
bim_P_Out_map = map(lambda num: (num/1000),bim_P_Out_raw)
bim_1_G_map = map(lambda num: (num/1000),bim_1_G_raw)
bim_P_Out = map(lambda x: (x * (-45.45) + 15), bim_P_Out_map)
bim_1_G = map(lambda x: (x * (-45.45) + 15), bim_1_G_map)
bim_P_Out_L = list(bim_P_Out)
bim_1_G_L = list(bim_1_G)
p_Out_Min = min(bim_P_Out_L)
p_Out_Max = max(bim_P_Out_L)

print("Min value element : ",p_Out_Min)
print("Max value element : ",p_Out_Max)

#set axis of second plot
# win2 = pg.ViewBox()
# win.scene().addItem(win2)
# win.getAxis('right').linkToView(win2)
# win2.setXLink(win)
# win2.setYRange(-20,-10)

tempURA = list(tempURA_map)
tempERA_map = map(lambda temp: (temp/1000),tempERA_raw) #convert from milli degrees to degrees
tempERA = list(tempERA_map)                             #unpack the map object

#create graphs
g1 = pg.PlotDataItem(x_values, tempERA, pen = 'b')
g2 = pg.PlotDataItem(x_values, tempURA, pen = 'r')
g3 = pg.PlotDataItem(x_values, y = bim_P_Out_L, pen = 'g')
g4 = pg.PlotDataItem(x_values, y = bim_1_G_L, pen = 'y')

def convertValues(m,x,c):
    return ((m * x) + c)


#add to plot

# win.addItem(g1)
# win.addItem(g2)
# win2.addItem(g1)


#Testing section
scene = QGraphicsScene()
# qgv.setCentralWidget(scene)

qgv.setScene(scene)
# qgv.setFixedSize(600, 600)
qgv.setSceneRect(0,0,600,400)
qgv.show()

graphWindow1.showAxis('right')
graphWindow1.getAxis('right').linkToView(graphWindow2)
graphWindow2.setXLink(graphWindow1)
# graphWindow2.setGeometry(graphWindow1.getViewBox().sceneBoundingRect())
graphWindow2.setYRange(-20, -10)

graphWindow1.setMinimumSize(500,300)
graphWindow2.setMinimumSize(500,300)
graphWindow1.addItem(g1)
graphWindow1.addItem(g2)
graphWindow2.addItem(g3)
graphWindow2.addItem(g4)
# graphWindow1.plot(x_values, tempURA, pen = 'r')


scene.addItem(graphWindow1)
scene.addItem(graphWindow2)
# view = QGraphicsView(scene)
# view.show()




status = app.exec_()
sys.exit(status)