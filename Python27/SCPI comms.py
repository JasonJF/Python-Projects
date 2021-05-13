import visa
from time import sleep


rm = visa.ResourceManager()
instList=(rm.list_resources())

instName = rm.open_resource('TCPIP0::inst0::INSTR')
print (instName.query('*IDN?'))

##for elem in instList:
####    instName = rm.open_resource('TCPIP0::A-N9000A-30993::inst0::INSTR')
####    print (instName.query('*IDN?'))
##    sleep(1)
##           
##    print elem
