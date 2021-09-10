#Punto6

data = '3asdassdasdasfasfasf5asdassdasdasfasfasf7asdassdasdasfasfasf23'
listData = data.split('asdassdasdasfasfasf')

print(listData)

#punto14

import datetime

date1 = datetime.datetime(2014, 7, 2)
date2 = datetime.datetime(2012, 8, 11)

diff = date1 - date2
print(diff)

#punto27

print(','.join(listData))


#punto41

dire = 'C:/Users/Juan Grisales/Desktop/Repos/Ejemplo/'

import os.path

check = os.path.isfile(dire)

if(check):
    print('Si')
else:
    print('No')


#punto47

import multiprocessing

numCpu = multiprocessing.cpu_count()

print(numCpu)



#punto49

import os

all = os.listdir(dire)
print(all)



#punto 


dirArch = 'C:/Users/Juan Grisales/Desktop/AAA.txt'

arch = open(dirArch, 'r')
contenido = arch.read()
print(contenido)
arch.close()


dirArch = 'C:/Users/Juan Grisales/Desktop/AAA.txt'
with open(dirArch,'r') as arch:
    content = arch.read()    
    print(content)



#punto 

with open('../Daniel.txt','w') as newArch:
    newArch.write('Olarte')


with open('../Daniel.txt','a') as newArch:
    newArch.write('Blasche')


#punto

import matplotlib.pyplot as graphLib
import numpy as multiArr

x = multiArr.array(range(10))
y = x + 1

graphLib.plot(x,y)

#graphLib.show()

#request

import requests 
busq = requests.get('https://translate.google.com/')
print(busq)





 