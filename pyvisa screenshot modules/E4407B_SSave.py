"""-----------------------------------------------------------------------------

Company     : Reutech Radar Systems
Name        : E4407B_SSave
Designer    : jfolding
Generated   : 17/05/2021
--------------------------------------------------------------------------------
Description:
Screenshot saving module for HP E4407B machines to be used with pyvisa

-----------------------------------------------------------------------------"""
import visa
import time
import os
os.add_dll_directory('C:\\Program Files (x86)\\Keysight\\IO Libraries Suite\\bin')
import pyvisa

from time import sleep

def saveScreenshot(instrument, fileLocation, fileName):
    # Connect to Instrument
    # rm = visa.ResourceManager()
    rm = pyvisa.ResourceManager('ktvisa32')  ##visa secondary location
    suffx = ".GIF"
    image = (fileName+suffx)
    E4407B = instrument
    saveLocation = (fileLocation+"/"+image)
    print(E4407B,saveLocation)
    # Setup Block Data
    E4407B.values_format.is_binary = True
    E4407B.values_format.datatype = 'B'
    E4407B.values_format.is_big_endian = False
    E4407B.values_format.container = bytearray
    # set timeout
    E4407B.timeout = 50000  ##important to prevent visa error especially on slow machines

    writeString = (":MMEMory:STORe:SCReen \"R:\{}\"".format(image))
    deleteString = (":MMEMory:DELete \"R:\{}\"".format(image))
    print(writeString)
    print(deleteString)

    # Set screenshot to reverse bitmap
    E4407B.write(':MMEM:SCR:BACK REV')
    sleep(1)

    ##Save screenshot
    E4407B.write(writeString)
    sleep(6)
    ##Copy block data to PC
    dname = (r"{}").format(saveLocation)
    fullname = (dname)
    ##print(dname)
    ##print(fullname)
    # warnings.filterwarnings("ignore",category=Warning)  # The read will produce a VI_SUCCESS_MAX_CNT warning so suppress
    img = E4407B.query_values(':MMEM:DATA? "R:\{}"'.format(image))
    sleep(6)
    target = open(dname, 'wb')
    target.write(img)
    target.close()
    print("{} saved.".format(saveLocation))

    ##Delete screenshot from ram
    E4407B.write(deleteString)

    E4407B.close()
    rm.close()

    # end of Untitled
