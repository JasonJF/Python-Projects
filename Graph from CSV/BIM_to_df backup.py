import pandas as pd

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


tempURA = list(tempURA_map)
tempERA_map = map(lambda temp: (temp/1000),tempERA_raw) #convert from milli degrees to degrees
tempERA = list(tempERA_map)                             #unpack the map object

def convertValues(m,x,c):
    return ((m * x) + c)


#add to plot
