import sys  

import Modulos.moduloCosto as mC

from Modulos.moduloCosto import *


edificio1 = mC.edificiogen(100,8) 
print("Costo por edificio " +str(edificio1.costos()))

edificio2 = edificiogen(100) 
print("Costo por edificio " +str(edificio2.costos()))


edificio3 = edificiopis(10000,3,8)  
print("Costo por edificio " +str(edificio3.costos()))


edificio4 = edificiocan(10000,3,8)  
print("Costo por edificio " +str(edificio4.costos()))

print(getVersion())