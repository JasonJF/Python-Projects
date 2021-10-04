'''
Filename: u:\Projects\Coding\Python Projects\Graph from CSV\BIM_to_PDF_Script\exctract_BIM_data.py
Path: u:\Projects\Coding\Python Projects\Graph from CSV\BIM_to_PDF_Script
Created Date: Thursday, September 23rd 2021, 11:01:45 am
Author: JasonJF

Copyright (c) 2021 Your Company
'''
# from BIM_to_PDF_Script.plot_BIM_graphs import generate_Plots
# from BIM_to_PDF_Script.plot_BIM_graphs import generate_Plots
import pandas as pd
from plot_BIM_graphs import *
import os

def extract_BIM_Data():
    #Get data from file
    # df = pd.read_csv('../BIM Logs/cleanBIM.csv')
    print(os.getcwd())
    df = pd.read_csv(os.getcwd() +'/BIM Logs/cleanBIM.csv')      #use this line when running from main.py

    #store data in variables and format
    x_raw = df['DateTime']
    bim_P_Out_raw = df['EraBimPowerOutMilliV']
    tempERA_raw = df['EraTemperatureMilliDegC']
    tempURA_raw = df['UcTemperatureMilliDegC']
    bim_1_G_raw = df['EraBimPower1GHzMilliV']
    tx_in_raw = df['UcBimTxInputMilliV']
    tx_out_raw = df['UcBimTxOutputMilliV']
    bim_i_raw = df['RxBimIChannelMilliV']
    bim_q_raw = df['RxBimQChannelMilliV']
    # print(x_raw[0])
    xdict = dict(enumerate(x_raw))
    x_values = list(xdict.keys())
    x_strings = list(map(lambda x: str(x), x_raw))


    #Convert / Format Data
    def convertValues(m,x,c):
        return ((m * x) + c)

    tempURA = list(map(lambda num: (num/20),tempURA_raw))
    tempERA = list(map(lambda num: (num/1000),tempERA_raw))
    bim_P_Out = list(map(lambda x: ((x/1000) * (-45.45) + 15), bim_P_Out_raw))
    bim_P_Out_func = list(map(lambda x: convertValues((-45.45), (x/1000), 15), bim_P_Out_raw))
    bim_1_G = list(map(lambda x: convertValues((-45.45), (x/1000), 15), bim_1_G_raw))
    tx_in = list(map(lambda x: convertValues((1/(-22*2.786)), (x), 25), tx_in_raw))
    tx_out = list(map(lambda x: convertValues((-24.8614817), (x/1000), 58.5), tx_out_raw))
    bim_i = list(map(lambda num: (num/1000),bim_i_raw))
    bim_q = list(map(lambda num: (num/1000),bim_q_raw))

    #getting maximum and minimum
    # max_ERA_Temp = max(tempERA)
    # max_ERA_index = tempERA.index(max_ERA_Temp)
    # print(max_ERA_Temp)
    # print(max_ERA_index)


    # print(xdict[0])
    # print(max(tempERA))
    # print(tempURA[0])
    # print(bim_P_Out[0])
    # print(bim_P_Out_func[0])
    # print(tx_in[0])

    #Plot Data

    era = {
        "plotName": "Temp vs BIM P out & BIM 1 Ghz",
        "x_values": x_values,
        "time": xdict,
        "era_temps": tempERA,
        "ura_temps": tempURA,
        "y1_values": bim_P_Out,
        "y1_name": "BIM P Out",
        "y2_values": bim_1_G,
        "y2_name": "BIM 1 Ghz",
        "right_axis_title": "Power",
        "right_axis_unit": "(dBm)"
    }
    tx_bims = {
        "plotName": "Temp vs TX_In & TX_Out",
        "x_values": x_values,
        "time": xdict,
        "era_temps": tempERA,
        "ura_temps": tempURA,
        "y1_values": tx_in,
        "y1_name": "TX_IN",
        "y2_values": tx_out,
        "y2_name": "TX_OUT",
        "right_axis_title": "Power",
        "right_axis_unit": "(dBm)"
    }
    iq_bims = {
        "plotName": "Temp vs IQ BIMS",
        "x_values": x_values,
        "time": xdict,
        "era_temps": tempERA,
        "ura_temps": tempURA,
        "y1_values": bim_i,
        "y1_name": "BIM I",
        "y2_values": bim_q,
        "y2_name": "BIM Q",
        "right_axis_title": "Voltage",
        "right_axis_unit": "(V)"
    }
    #Call the plotting function
    generate_Plots(era)
    generate_Plots(tx_bims)
    generate_Plots(iq_bims)