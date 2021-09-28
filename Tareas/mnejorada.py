import random

class compañiaHelados:
    def __init__(self):
        self.ordenes = []
        self.tiposHelado = ['Cono', 'Vaso', 'Litro']

    def ganancias(self):
        ingresos = 0
        cantidadProduccion = 0
        for orden in self.ordenes:
            if (orden == 'Cono'):
                ingresos += 5
                cantidadProduccion += 100      
            if (orden == 'Vaso'):
                ingresos += 6
                cantidadProduccion += 200
            if (orden == 'Litro'):
                ingresos += 7
                cantidadProduccion += 300
        return ingresos - cantidadProduccion * 0.03

    def ordenarHeladoAlteatorioCliente(self):
        tipoHeladoAleatorioCliente = random.choice(self.tiposHelado) # generar tipo helado aleatorio
        self.ordenes.append(tipoHeladoAleatorioCliente) # darle helado al cliente con idCliente

    def reportar(self):
        print("Las ganancias de la compañia son: ", '${:,.2f}'.format(self.ganancias()))

#comienzo
compañiaCreamHelado = compañiaHelados() 

# generar 100 clientes que ordenen helados aleatorios
for i in range(1, 101):
    compañiaCreamHelado.ordenarHeladoAlteatorioCliente()
compañiaCreamHelado.reportar() # reportar las ganancias