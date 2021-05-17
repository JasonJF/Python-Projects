import visa
import time
import os
os.add_dll_directory('C:\\Program Files (x86)\\Keysight\\IO Libraries Suite\\bin')
from E4407B_SSave import * #screenshot module for specific machine
# start of Untitled

# rm = visa.ResourceManager()
# rm = pyvisa.ResourceManager('ktvisa32') ##visa secondary location
# E4407B = rm.open_resource('GPIB1::1::INSTR')

def saveSpurs(instrument, fileLocation, fileName):
    x = 150
    while (x<=250):
        
        fname = (fileName + "{}".format(x))
        saveScreenshot(instrument,fileLocation,fname)
        print("{} saved.".format(fname))    
        x = x+10
        # raw_input('Press enter to cont..') #Python 2.7
        input('Press enter to cont..') #Python 3
    

# E4407B.close()
# rm.close()

# end of Untitled
