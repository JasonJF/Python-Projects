import visa
rm = visa.ResourceManager()
print(rm.list_resources())
exa = rm.open_resource('TCPIP0::A-N9010A-60244::inst0::INSTR')
print(exa.query('*IDN?'))
exa.write("SYSTem:PRESet")
exa.write(":SENSe:FREQuency:RF:CENTer 1.2GHz")
exa.write("SENSe:FREQuency:SPAN 300MHz")
exa.write("DISPlay:WINDow:TRACe:Y:SCALe:RLEVel 10dBm")
exa.write("SENSe:BWIDth:RESolution 100kHz")

