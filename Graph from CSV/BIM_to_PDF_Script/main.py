'''
Filename: u:\Projects\Coding\Python Projects\Graph from CSV\BIM_to_PDF_Script\main.py
Path: u:\Projects\Coding\Python Projects\Graph from CSV\BIM_to_PDF_Script
Created Date: Thursday, September 23rd 2021, 9:20:46 am
Author: JasonJF

Copyright (c) 2021 Your Company
'''
##Rinse the BIM file
# from CSV_parsing.basic_read_csv import rinseBimCSV
from basic_read_csv import *
from exctract_BIM_data import *

#Clean up the BIM file
rinseBimCSV()

#Extract data from the cleanBIM.csv
extract_BIM_Data()