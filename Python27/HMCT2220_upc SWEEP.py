import visa
from time import sleep
rm = visa.ResourceManager()
#print(rm.list_resources())

my_instrument = rm.open_resource('ASRL5::INSTR')
E4407B = rm.open_resource('GPIB0::18::INSTR')
#print(my_instrument.query('*IDN?'))
##
s = 1150
measDone = 0
while (s<=1250):
    my_instrument.write("freq {}MHz;pow 4.5dBm;outp on;freq:mode cw".format(s))
    print("frequency is {}MHz".format(s))
    ##my_instrument.write("freq:star 1.15GHz;stop 1.25GHz;step 10MHz;mode swe")
    ##my_instrument.write("swe:dwel 0.001")
    ##my_instrument.write("init:cont OFF")
    E4407B.write('*OPC?')
    while (measDone == 0):
        print("measurement in progress..")
        sleep(5)
        measDone = (E4407B.read())
        print(measDone)
    
         
    raw_input('Press ENTER to Step')
    s=s+10
    measDone = 0 
    ##
