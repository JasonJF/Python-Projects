#adapted from https://www.youtube.com/watch?v=spALaS5BFX8

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os, sys
import time





# Function to convert string to datetime
# mtime = os.path.stat().st_mtime
# timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
def convert(date_time):
    format = '"%d/%m/%Y %H:%M:%S"' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
   
    return datetime_str
   
# Driver code
# date_time = 'Dec 4 2018 10:07AM'
# print(convert(date_time))

plt.style.use('bmh')
df = pd.read_csv('BIM_Temp.csv')
mpl.get_backend()
#All
x = df['DateTime']
y_milli = df['EraTemperatureMilliDegC']
y_map = map(lambda num: (num/1000),y_milli) #convert from milli degrees to degrees
y = list(y_map)                             #unpack the map object

print((x[0]))
# print(convert(x[0]))
print(timestamp_str)
# print(y)

#Line Graph

# plt.xlabel('Time', fontsize=18)
# plt.ylabel('ERA Temp', fontsize=16)
# # plt.scatter(x, y)
# plt.plot(x, y)

# plt.show()