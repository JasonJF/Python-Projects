import pyqtgraph as pg
import numpy as np
import pandas as pd

df = pd.read_csv('BIM_Temp.csv')

#All
x = df['DateTime']
y_milli = df['EraTemperatureMilliDegC']
y_map = map(lambda num: (num/1000),y_milli) #convert from milli degrees to degrees
y = list(y_map)  #unpack the map 

#x = np.random.normal(size=1000)
#y = np.random.normal(size=1000)
pg.plot(y,pen='r')  ## setting pen=None disables line drawing
