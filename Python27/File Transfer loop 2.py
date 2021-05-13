import pyvisa
import os
from time import sleep
rm = pyvisa.ResourceManager()
inst = rm.open_resource('GPIB0::1::INSTR')

inst.values_format.is_binary = True
inst.values_format.datatype = 'B'
inst.values_format.is_big_endian = False
inst.values_format.container = bytearray

os.chdir(r"C:\Users\ProdTest\Documents\Test Results\REPAIRS\RGR\RSU")
#inst.write(':mmem:name "C:\eswScreen.wmf\"')
x = 1
while (x<=9):
    fname = ("C:\Users\ProdTest\Documents\Test Results\REPAIRS\RGR\RSU\GR_URA051_S{}.WMF".format(x))
   
    
    img = inst.query_values('MMEM:DATA? "C:\URA51S{}.WMF"'.format(x))
    sleep(0.5)
    target = open(fname, 'wb'.format(x))
    target.write(img)
    target.close()
    print("{} saved.".format(fname))
    x = x+1
    
