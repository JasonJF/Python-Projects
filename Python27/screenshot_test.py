import visa
import time
# start of Untitled

rm = visa.ResourceManager()
E4407B = rm.open_resource('GPIB0::1::INSTR')
x = 150
while (x<=250):
    
    fname = ("\"C:\URAS{}.WMF\"".format(x))
    cname = (":MMEMory:STORe:SCReen {}".format(fname))   
    E4407B.write(cname)
    print(cname)
    print("{} saved.".format(fname))    
    x = x+10
    raw_input('Press enter to cont..')
    

E4407B.close()
rm.close()

# end of Untitled
