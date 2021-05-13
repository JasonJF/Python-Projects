import pyvisa
import os
rm = pyvisa.ResourceManager()
inst = rm.open_resource('GPIB0::1::INSTR')

inst.values_format.is_binary = True
inst.values_format.datatype = 'B'
inst.values_format.is_big_endian = False
inst.values_format.container = bytearray

os.chdir(r"C:\Users\ProdTest\Documents\Test Results\REPAIRS\RGR\RSU\051")
#inst.write(':mmem:name "C:\eswScreen.wmf\"')
img = inst.query_values('MMEM:DATA? "C:\UR51S11.WMF"')

target = open(r"C:\Users\ProdTest\Documents\Test Results\REPAIRS\RGR\RSU\051\GR_URA051_S250.WMF", 'wb')
target.write(img)
target.close()
