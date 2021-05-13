import visa
import time
# start of Untitled

rm = visa.ResourceManager()
E4407B = rm.open_resource('GPIB0::1::INSTR')

##E4407B.write('*RST')
E4407B.write(':MMEMory:SCReen:BACKground NORMal|REVERSE')
#E4407B.write(':SENSe:FREQuency:STARt 9GHZ')
##E4407B.write(':SENSe:FREQuency:STOP 10.2GHZ')
##E4407B.close()
##rm.close()


