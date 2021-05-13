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
pcbSer="EDMX"
suffx = (".GIF")
writename = (":MMEMory:STORe:SCReen \"R:\{}.GIF\"".format(pcbSer))
deletename = (":MMEMory:DELete \"R:\{}.GIF\"".format(pcbSer))
print(writename)
print(deletename)
#Set screenshot to reverse bitmap
E4407B.write(':MMEM:SCR:BACK REV')
sleep(1)
##Save screenshot to ram
E4407B.write(writename)
###E4407B.close()
##Copy block data to PC
dname = ("C:\Users\ProdTest\Documents\Test Results\FAT\RGR\EDM\Calvin_Khanyisile\GR_{}_SPUR11".format(pcbSer))
fullname = (dname+suffx)
print(dname)
print(fullname)
img = E4407B.query_values('MMEM:DATA? "R:\{}.GIF"'.format(pcbSer))
sleep(10)
target = open(fullname, 'wb')
target.write(img)
target.close()
print("{} saved.".format(fullname))

    


#Delete screenshot from ram
E4407B.write(deletename)
print("screenshot deleted")
E4407B.close()
rm.close()

# end of Untitled
