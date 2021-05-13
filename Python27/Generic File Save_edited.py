import visa
import time
import os
from time import sleep


# Connect to Instrument
rm = visa.ResourceManager()
E4407B = rm.open_resource('GPIB0::18::INSTR')


#Setup Block Data
E4407B.values_format.is_binary = True
E4407B.values_format.datatype = 'B'
E4407B.values_format.is_big_endian = False
E4407B.values_format.container = bytearray
#Setup directories
##os.chdir(r"C:\Users\ProdTest\Documents\Test Results\FAT\RGR\UPCONVERTERS\088")
pcbSer="UPC088"
suffx = ("_output.WMF")
writename = (":MMEM:STOR:SCR \"D:\myScreen2.png\"")
deletename = (":MMEMory:DELete \"D:\myScreen2.png\"")
#print(deletename)
#Set screenshot to reverse bitmap
#E4407B.write(':MMEM:STOR:SCR:THEM:FMON')
##Save screenshot to ram
E4407B.write(writename)
##Copy block data to PC
dname = ("C:\Users\ProdTest\Desktop\myScreen.png")
fullname = (dname)
##print(dname)
##print(fullname)
img = E4407B.query_values('MMEM:DATA? \"D:\myScreen2.png\"')
sleep(0.5)
target = open(fullname, 'wb')
target.write(img)
target.close()
print("{} saved.".format(fullname))

    


##Delete screenshot from ram
E4407B.write(deletename)

E4407B.close()
rm.close()

# end of Untitled
