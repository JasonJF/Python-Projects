import visa
import time
import os
from time import sleep


# Connect to Instrument
rm = visa.ResourceManager()
E4407B = rm.open_resource('GPIB0::1::INSTR')

E4407B.write(':DISPlay:WINDow:TRACe:Y:SCALe:RLEV 12')
E4407B.write(':SENSe:FREQuency:STARt 5GHz')
E4407B.write(':SENSe:FREQuency:STOp 21GHz')
E4407B.write(':SENSe:BANDwidth:RESolution 100kHz')
E4407B.write(':SENSe:BWIDth:VIDeo:RATio 0.3')
##E4407B.write(':CALCulate:MARKer:PEAK:SEARch:MODE PARameter|MAXimum')

