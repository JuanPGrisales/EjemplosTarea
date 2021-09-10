

aaaa = 0
listaNotas = {'Daniel' : 3,
               'JuanP' : 4,
               'Simon' : 5}


print(listaNotas)

print(aaaa)
print(listaNotas['JuanP'])

aaaa = 8

listaNotas['JuanP'] = 8

print(listaNotas['JuanP'])

listaNotas['JuanP'] += 4  
print(listaNotas['JuanP'])


listaNotas.pop('Daniel')
print(listaNotas)

listaNotas.update({'Jonathan' : 6})
print(listaNotas)
