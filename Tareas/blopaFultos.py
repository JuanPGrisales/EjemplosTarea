import random

class blopaFulano:
    def __init__(self):    
        self.petotos = {}
        self.ordenesFultos = []

    def calcularGanancias(self):
        valorOrdenesFulto = 0
        costoProduccionFulto = 0
        valorOrdenFulto = 0
        for ordenFulto in self.ordenesFultos:
            if (ordenFulto == 'Gloc'):
                valorOrdenFulto = 6
                cantidadProduccionFulto = 170   
            if (ordenFulto == 'Pater'):
                valorOrdenFulto = 5
                cantidadProduccionFulto = 90      
            if (ordenFulto == 'Por 1200 blatos'):
                valorOrdenFulto = 7
                cantidadProduccionFulto = 250
            if (ordenFulto == 'Otter'):
                valorOrdenFulto = 4
                cantidadProduccionFulto = 80      
            valorOrdenesFulto += valorOrdenFulto
            costoProduccionFulto += cantidadProduccionFulto
        return valorOrdenesFulto - (costoProduccionFulto*0.03)
    
    def reportarGanancias(self):
        print("Las ganancias de la blopa de Fultos son: ", (self.calcularGanancias()))
        
class petoto:
    def __init__(self, petotoNumero):
        self.tiposFultos = ['Gloc','Pater','Por 1200 blatos', 'Otter']

    def ordenarFulto(self):
        return random.choice(self.tiposFultos)
    

#comienzo
blopaFultos = blopaFulano() 

# -generar 80 petotos que ordenen fultos aleatorios
for i in range(1, 81):
    petotoNumero = "Petoto" + str(i)
    blopaFultos.petotos[petotoNumero] = petoto(petotoNumero)
    tipoFulto = blopaFultos.petotos[petotoNumero].ordenarFulto()
    blopaFultos.ordenesFultos.append(tipoFulto)
blopaFultos.reportarGanancias() # -reportar las ganancias