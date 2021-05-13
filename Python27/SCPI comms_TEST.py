import visa
import time
import os
from time import sleep


# Connect to Instrument
rm = visa.ResourceManager()
CXA = rm.open_resource('TCPIP0::A-N9000A-30993::inst0::INSTR')


#Setup Block Data
CXA.values_format.is_binary = True
CXA.values_format.datatype = 'B'
CXA.values_format.is_big_endian = False
CXA.values_format.container = bytearray
#Setup directories
os.chdir(r"C:\Users\ProdTest\Documents\Test Results\FAT\RGR\UPCONVERTERS\091")
pcbSer="TEST"
suffx = ("_TEST.png")
writename = (":MMEMory:STORe:SCReen \"D:\Users\Instrument.A-N9000A-30993\Documents\SA\screen\{}.png\"".format(pcbSer))
deletename = (":MMEMory:DELete \"D:\Users\Instrument.A-N9000A-30993\Documents\SA\screen\{}.png\"".format(pcbSer))
##print(deletename)
#Set screenshot to reverse bitmap
CXA.write(':MMEMory:STORe:SCReen:THEMe FMONochrome')
####CXA.write(':MMEMory:STORe:SCReen "D:\Users\Instrument.A-N9000A-30993\Documents\SA\screen\TEST.png"')
##Save screenshot to ram
CXA.write(writename)
##Copy block data to PC
dname = ("C:\Users\ProdTest\Documents\Test Results\FAT\RGR\GR_{}".format(pcbSer))
fullname = (dname+suffx)
##print(dname)
##print(fullname)
img = CXA.query_values('MMEM:DATA? "D:\Users\Instrument.A-N9000A-30993\Documents\SA\screen\{}.png\"'.format(pcbSer))
sleep(0.5)
target = open(fullname, 'wb')
target.write(img)
target.close()
print("{} saved.".format(fullname))

##Delete screenshot from ram
CXA.write(deletename)

CXA.close()
rm.close()

# end of Untitled


