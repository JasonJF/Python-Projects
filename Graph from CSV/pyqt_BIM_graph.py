import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import pandas as pd
import numpy as np
import datetime


app = QApplication(sys.argv)
pg.setConfigOption('background', 'w')
# pg.mkBrush(30, 255, 35, 255)
win = pg.plot()
pg.setConfigOptions(antialias=True)

#Get data from file
df = pd.read_csv('BIM.csv')


#store data in variables and format
x_raw = df['DateTime']
bim_P_Out_raw = df['EraBimPowerOutMilliV']
print(bim_P_Out_raw)
tempERA_raw = df['EraTemperatureMilliDegC']
tempURA_raw = df['UcTemperatureMilliDegC']



#dummy data
x1 = np.arange(10)
y1 = np.sin(x1)

xdict = dict(enumerate(x_raw))
# print([xdict.values()])
x_values = list(xdict.keys())

#convert to correct scale and units
tempURA_map = map(lambda num: (num/20),tempURA_raw)
bim_P_Out_map = map(lambda num: (num/1000),bim_P_Out_raw)
bim_P_Out = map(lambda x: (x * (-45.45) + 15), bim_P_Out_map)
# print(list(bim_P_Out))
tempURA = list(tempURA_map)
tempERA_map = map(lambda temp: (temp/1000),tempERA_raw) #convert from milli degrees to degrees
tempERA = list(tempERA_map)                             #unpack the map object

print(tempERA_raw)
# print(tempURA_raw)
# print(tempERA)
# print(tempURA)
# print(y)
#create graphs
g1 = pg.PlotDataItem(x_values, tempERA, pen = 'b')
g2 = pg.PlotDataItem(x_values, tempURA, pen = 'r')
g3 = pg.PlotDataItem(x_values, y = (list(bim_P_Out)), pen = 'g')
g4 = pg.PlotDataItem(x_values, tempURA, pen = 'r')
# bg1 = pg.BarGraphItem(x=x_values, y=y, height = y, width = 0.3, brush=pg.mkBrush(30, 255, 35, 255))
bg1 = pg.BarGraphItem(x=x1, height = y1, width = 0.3, brush = 'r')

def convertValues(m,x,c):
    return ((m * x) + c)


#add to plot
# win.addItem(bg1)
win.addItem(g1)
win.addItem(g2)
win.addItem(g3)
# win.addItem(g4)
# win.addItem(bg1)

status = app.exec_()
sys.exit(status)