import pandas as pd
#libraries for plotting
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio



# print(fig)
# fig.show()
import numpy as np
np.random.seed(1)

import os

if not os.path.exists("images"):
    os.mkdir("images")

#Get data from file
df = pd.read_csv('output.csv')


#store data in variables and format
x_raw = df['DateTime']
bim_P_Out_raw = df['EraBimPowerOutMilliV']
# print(bim_P_Out_raw)
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

# print("Min value element : ",p_Out_Min)
# print("Max value element : ",p_Out_Max)


tempURA = list(tempURA_map)
tempERA_map = map(lambda temp: (temp/1000),tempERA_raw) #convert from milli degrees to degrees
tempERA = list(tempERA_map)                             #unpack the map object


#create plotly figure
# fig = px.line(tempERA, title="sample figure")

#export
# fig.write_image("images/BIM_graph.png")
def convertValues(m,x,c):
    return ((m * x) + c)


#creating subplots

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=x_values, y=tempERA, name="tempERA"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=x_values, y=tempURA, name="tempURA"),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(x=x_values, y=bim_P_Out_L, name="Bim P Out"),
    secondary_y=True,
)

fig.add_trace(
    go.Scatter(x=x_values, y=bim_1_G_L, name="Bim P 1Ghz"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="ERA Bims"
)

# Set x-axis title
fig.update_xaxes(title_text="Time")

# Set y-axes titles
fig.update_yaxes(title_text="Temperature <b>(deg)</b>", secondary_y=False)
fig.update_yaxes(title_text="Power <b>(dBm)</b>", secondary_y=True)

# fig.show()

#export
pio.write_image(fig, 'images/ERA_Bims.png', width=1000, height=600)
fig.write_image("images/multiple_figures_bim.png")
print("done")
