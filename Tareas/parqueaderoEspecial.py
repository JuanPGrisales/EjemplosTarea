import random

class parqueadero:
    def __init__(self):
        self.listaCarros = []
        self.listaMotos = []

    def reportarIngresos(self):
        _ingresosParqueaderos = (len(self.listaCarros)*10000) + (len(self.listaMotos)*5000)
        print("Las ganancias del parqueadero del primer dia son de: ", _ingresosParqueaderos)

    def generarVehiculos(self,_numeroVehiculos):
        for i in range(_numeroVehiculos):
            _tipoVehiculo = random.choice(['moto','carro'])
            if(_tipoVehiculo == 'moto'):
                if(len(self.listaMotos) < 50):
                    self.listaMotos.append(vehiculo(_tipoVehiculo)) 
            if(_tipoVehiculo == 'carro'):
                if(len(self.listaCarros) < 100):
                    self.listaCarros.append(vehiculo(_tipoVehiculo)) 

class vehiculo:
    def __init__(self,_tipoVehiculo):
        pass


#comienzo
parqueaderoEspecial = parqueadero()

parqueaderoEspecial.generarVehiculos(100)

parqueaderoEspecial.reportarIngresos()
