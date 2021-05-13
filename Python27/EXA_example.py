import visa
rm = visa.ResourceManager()
print(rm.list_resources())

exa = rm.open_resource('TCPIP0::A-N9010A-60244::inst0::INSTR')
print(exa.query('*IDN?'))
exa.write(':TRACe:MODE MAXHold')

exa.write('')
