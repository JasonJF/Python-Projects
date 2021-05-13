import visa
rm = visa.ResourceManager()
print(rm.list_resources())

pwr = "-15"
my_instrument = rm.open_resource('ASRL4::INSTR')
print(my_instrument.query('*IDN?'))
##
power_command = ("pow {}dBm".format(pwr))
my_instrument.write(power_command)
##my_instrument.write("freq:star 9.2GHz;stop 10GHz;step 100kHz;mode swe")
##my_instrument.write("swe:dwel 0.001")
##my_instrument.write("init:cont on")
my_instrument.write("SYST:COMM:GTL")
##raw_input('Press ENTER to exit')
##
