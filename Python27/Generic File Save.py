import visa
import time
import os
from time import sleep


# Connect to Instrument
rm = visa.ResourceManager()
E4407B = rm.open_resource('GPIB0::15::INSTR')


#Setup Block Data
E4407B.values_format.is_binary = True
E4407B.values_format.datatype = 'B'
E4407B.values_format.is_big_endian = False
E4407B.values_format.container = bytearray
#Setup directories
##os.chdir(r"C:\Users\ProdTest\Documents\Test Results\FAT\RGR\UPCONVERTERS\088")
pcbSer="UPC088"
suffx = ("_output.WMF")
writename = (":MMEMory:STORe:SCReen \"R:\{}.WMF\"".format(pcbSer))
deletename = (":MMEMory:DELete \"R:\{}.WMF\"".format(pcbSer))
#print(deletename)
#Set screenshot to reverse bitmap
E4407B.write(':MMEM:SCR:BACK REV')
##Save screenshot to ram
E4407B.write(writename)
##Copy block data to PC
dname = ("C:\Users\ProdTest\Documents\Test Results\FAT\RGR\GR_{}".format(pcbSer))
fullname = (dname+suffx)
##print(dname)
##print(fullname)
img = E4407B.query_values('MMEM:DATA? "R:\{}.WMF"'.format(pcbSer))
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
