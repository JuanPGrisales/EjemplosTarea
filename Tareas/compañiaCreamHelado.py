import random

class compañiaHelados:
    def __init__(self):    
        self.clientes = {}
        self.ordenes = []

    def calcularGanancias(self):
        valorOrdenes = 0
        costoProduccion = 0
        valorOrden = 0
        for orden in self.ordenes:
            if (orden == 'Cono'):
                valorOrden = 5
                cantidadProduccion = 100      
            if (orden == 'Vaso'):
                valorOrden = 6
                cantidadProduccion = 200      
            if (orden == 'Litro'):
                valorOrden = 7
                cantidadProduccion = 300      
            valorOrdenes += valorOrden
            costoProduccion += cantidadProduccion
        return valorOrdenes - (costoProduccion*0.03)
    
    def reportar(self):
        print("Las ganancias de la compañia son: ", '${:,.2f}'.format(self.calcularGanancias()))
        
class cliente:
    def __init__(self, clienteNumnero):
        self.tiposHelado = ['Cono','Vaso','Litro']

    def hacerOrden(self):
        return random.choice(self.tiposHelado)
    

#comienzo
compañiaCreamHelado = compañiaHelados() 

# generar 100 clientes que ordenen helados aleatorios
for i in range(0, 100):
    clienteNumero = "Cliente" + str(i)
    compañiaCreamHelado.clientes[clienteNumero] = cliente(clienteNumero)
    tipoOrden = compañiaCreamHelado.clientes[clienteNumero].hacerOrden()
    compañiaCreamHelado.ordenes.append(tipoOrden)
compañiaCreamHelado.reportar() # reportar las ganancias