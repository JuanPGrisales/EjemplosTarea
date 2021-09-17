import random
import uuid 
import math
import polyHandler

class compañiaElectrica:
    def __init__(self, _mapaPais):
        self.pais = pais(_mapaPais) 
    def generarReporte(self):
        if(self.pais == None):
            print('No existe pais')
            return
        print('----------------------------Seccion Pais-------------------------')
        # a. Energía producida
        print('La energia producida es: ', self.pais.energiaProducida())
        # b. Energía consumida
        print('La energia consumida es: ', self.pais.energiaConsumida())
        # c. Delta de energía
        print('El delta de energia es: ', self.pais.deltaEnergia())
        # d. Número de clientes
        print('El numero de clientes es: ', self.pais.numeroClientes())
        # e. Cliente que más consumió
        print('El cliente que mas consumio es: ', self.pais.clienteMayorConsumo())
        # f. Cliente que menos consumió
        print('El cliente que menos consumio es: ', self.pais.clienteMenorConsumo())
        # g. # de sectores que no tienen energía (puntos extra si me pinta un mapita del país)
        print('El numero de sectores sin energia son: ', self.pais.sectoresSinEnergia())
        
        print('----------------------------Seccion Plantas-------------------------')
        for _planta in self.pais.listaPlantas:
            #a.	Nombre de cada planta (id)
            print('El nombre de la planta es: ', _planta.id)
            #b.	Energía generada
            print('La energia generada es de: ', _planta.energiaGenerada())
            #c.	Energía consumida
            print('La energia consumida es de: ', _planta.energiaConsumida(self.pais))
            #d.	Lista de id de Sectores a los que asisten
            print('Los sectores que asisten son: ', _planta.listaIDSectoresAsistidos)
            print('El tipo de la planta es: ', _planta.tipo)
            print('----------------------------------------------')
        
        print('----------------------------Seccion Sectores-------------------------')
        for _sector in self.pais.listaSectores:
            #a.	Nombre de cada sector (id)
            print('El nombre del sector es: ', _sector.id)
            #b.	Energía recibida
            print('La energia recibida del sector es de: ', _sector.energiaRecibida(self.pais.listaPlantas))
            #c.	Energía consumida
            print('La energia consumida del sector es de: ', _sector.energiaConsumida())
            #d.	# de transformadores
            print('El numero de transformadores es: ', len(_sector.listaTransformadores))
            #e.	Energía por transformador
            print('La energia por transformador es: ', _sector.energiaPorTransformador())
            #f.	Número de clientes
            print('El numero de clientes es: ', _sector.numeroClientes())
            #(Bonus)	Número de edificaciones
            print('El numero de edificaciones es: ', _sector.numeroEdificaciones())
            #g.	Energía promedio / cliente
            print('La energia consumida por cliente es de: ', _sector.energiaConsumidaCliente())
            #h.	Energía promedio / edificación
            print('La energia consumida por edificacion es de: ', _sector.energiaConsumidaEdificacion())
            print('----------------------------------------------')

class planta:
    def __init__(self, _listaSectores, _mapaPais):
        self.id = uuid.uuid4()
        self.posicion = polyHandler.get_random_point_in_polygon(_mapaPais) #para que sirva con poligono, se debe generar punto aleatorio dentro del poligono
        self.listaIDSectoresAsistidos = []
        for _sector in _listaSectores:
            _coordenadasPlanta = self.posicion
            _coordernadasSector = _sector.posicion
            _diferenciaPosiciones = math.sqrt( (_coordenadasPlanta.x - _coordernadasSector[0])**2 + (_coordenadasPlanta.x - _coordernadasSector[1])**2 )
            if (_diferenciaPosiciones <= 2500): # si esta a 2500 km de planta
                self.listaIDSectoresAsistidos.append(_sector.id) # agregar id sector a lista id sectores asistidos
        _tipos = ('HidroElectrica', 'Eolica', 'Solar')
        self.tipo = random.choice(_tipos)
    
    def cantidadSectores(self):
        _numeroSectoresAsistidos = len(self.listaIDSectoresAsistidos)
        return _numeroSectoresAsistidos

    def energiaGenerada(self):
        _eficiencia = 0
        if(self.tipo == 'HidroElectrica'):
            _eficiencia = 0.6 
        if(self.tipo == 'Eolica'):
            _eficiencia = 0.7 
        if(self.tipo == 'Solar'):
            _eficiencia = 0.3 
        return 2500*_eficiencia

    def energiaConsumida(self, _pais):
        _calculoEnergiaConsumida = 0
        for _IDSectorAsistido in self.listaIDSectoresAsistidos:
            _posicionSectorAsistido = -1
            for _posicionSector, _sector in enumerate(_pais.listaSectores): 
                if _sector.id == _IDSectorAsistido:
                    _posicionSectorAsistido = _posicionSector
                    break
            _calculoEnergiaConsumida += _pais.listaSectores[_posicionSectorAsistido].energiaConsumida()
        # calculo la suma de energia consumida en cada uno de los sectores asistidos 
        return _calculoEnergiaConsumida

class cliente:
    def __init__(self):
        self.consumo = random.randint(1,3)
        self.id = uuid.uuid4()

class edificacion:
    def __init__(self):
        self.listaClientes = []
        for i in range(random.randint(1,20)):
            self.listaClientes.append(cliente())

class transformador:
    def __init__(self):
        self.listaEdificaciones = []
        for i in range(random.randint(10,12)):
            self.listaEdificaciones.append(edificacion())

class sector:
    def __init__(self, _mapaSector):
        self.mapaSector = _mapaSector
        self.id = uuid.uuid4()
        self.posicion = (random.randint(0,7000), random.randint(0,7000))
        self.listaTransformadores = []
        for i in range(random.randint(10,15)):
            self.listaTransformadores.append(transformador())

    def tieneEnergia(self, _listaPlantas):
        # saber _posicionPlanta
        for _planta in _listaPlantas:
            _coordenadasPlanta = _planta.posicion
            _coordernadasSector = self.posicion
            _diferenciaPosiciones = math.sqrt( (_coordenadasPlanta.x - _coordernadasSector[0])**2 + (_coordenadasPlanta.y - _coordernadasSector[1])**2 )
            return _diferenciaPosiciones <= 2500
        
    def energiaRecibida(self, _listaPlantas):
        _acometidaSector = 0
        for _planta in _listaPlantas:
            if(_planta.cantidadSectores() != 0):
                _acometidaSector += _planta.energiaGenerada() / _planta.cantidadSectores()
            else:
                _acometidaSector += 0
        return _acometidaSector

    def energiaConsumida(self):
        _consumoEnergia = 0 # suma de clientes por sector 
        for _transformador in self.listaTransformadores:
            for _edificacion in _transformador.listaEdificaciones:
                for _cliente in _edificacion.listaClientes:
                    _consumoEnergia += _cliente.consumo
        return _consumoEnergia

    def energiaPorTransformador(self):
        _consumoEnergiaTransformador = 0 
        for _transformador in self.listaTransformadores:
            for _edificacion in _transformador.listaEdificaciones:
                for _cliente in _edificacion.listaClientes:
                    _consumoEnergiaTransformador += _cliente.consumo
        _consumoEnergiaTransformador = _consumoEnergiaTransformador / len(self.listaTransformadores)   

        return _consumoEnergiaTransformador

    def numeroEdificaciones(self):
        _cantidadEdificaciones = 0
        for _transformador in self.listaTransformadores:
            _cantidadEdificaciones = len(_transformador.listaEdificaciones)
        return _cantidadEdificaciones

    def numeroClientes(self):
        _cantidadClientes = 0
        for _transformador in self.listaTransformadores:
            for _edificacion in _transformador.listaEdificaciones:
                _cantidadClientes += len(_edificacion.listaClientes)
                break
        return _cantidadClientes

    def energiaConsumidaCliente(self):
        _consumoEnergiaCliente = 0 
        for _transformador in self.listaTransformadores:
            for _edificacion in _transformador.listaEdificaciones:
                for _cliente in _edificacion.listaClientes:
                    _consumoEnergiaCliente += _cliente.consumo
        _consumoEnergiaCliente = _consumoEnergiaCliente / self.numeroClientes() 
        return _consumoEnergiaCliente

    def energiaConsumidaEdificacion(self):
        _consumoEnergiaEdificacion = 0 
        for _transformador in self.listaTransformadores:
            for _edificacion in _transformador.listaEdificaciones:
                for _cliente in _edificacion.listaClientes:
                    _consumoEnergiaEdificacion += _cliente.consumo
        _consumoEnergiaEdificacion = _consumoEnergiaEdificacion / len(_transformador.listaEdificaciones) 
        return _consumoEnergiaEdificacion
        
class pais:
    def __init__(self, _mapaPais):
        self.mapaPais = _mapaPais
        self.listaSectores = []
        _numeroSectores = random.randint(20,30)
        _splitPolys = polyHandler.splitPolygon(_mapaPais, _numeroSectores)
        polyHandler.paintPoligons(_splitPolys)
        for i in range(_numeroSectores):
            self.listaSectores.append(sector(_splitPolys[i]))
        self.listaPlantas = []
        for i in range(random.randint(2,4)):
            self.listaPlantas.append(planta(self.listaSectores, _mapaPais))

    def energiaProducida(self):
        _calculoEnergiaProducida = 0
        for _planta in self.listaPlantas:
            _calculoEnergiaProducida += _planta.energiaGenerada()
        return _calculoEnergiaProducida

    def energiaConsumida(self):
        _calculoEnergiaConsumida = 0
        for _sector in self.listaSectores:
            _calculoEnergiaConsumida += _sector.energiaConsumida()
        return _calculoEnergiaConsumida
         
    def deltaEnergia(self):
        _calculoDeltaEnergia = self.energiaProducida() - self.energiaConsumida()
        return _calculoDeltaEnergia

    def numeroClientes(self):
        _calculoNumeroClientes = 0
        for _sector in self.listaSectores:
            _calculoNumeroClientes += _sector.numeroClientes()
        return _calculoNumeroClientes

    def clienteMayorConsumo(self):
        _IDClienteMayorConsumo = ''
        _consumoMayorCliente = float('-inf')
        for _sector in self.listaSectores:
            for _transformador in _sector.listaTransformadores:
                for _edificacion in _transformador.listaEdificaciones:
                    for _cliente in _edificacion.listaClientes:
                        if(_cliente.consumo > _consumoMayorCliente):
                            _consumoMayorCliente = _cliente.consumo
                            _IDClienteMayorConsumo = _cliente.id
        return "{0}:${1}".format(_IDClienteMayorConsumo,_consumoMayorCliente) 

    def clienteMenorConsumo(self):
        _IDClienteMenorConsumo = ''
        _consumoMenorCliente = float('inf')
        for _sector in self.listaSectores:
            for _transformador in _sector.listaTransformadores:
                for _edificacion in _transformador.listaEdificaciones:
                    for _cliente in _edificacion.listaClientes:
                        if(_cliente.consumo < _consumoMenorCliente):
                            _consumoMenorCliente = _cliente.consumo
                            _IDClienteMenorConsumo = _cliente.id
        return "{0}:${1}".format(_IDClienteMenorConsumo,_consumoMenorCliente) 

    def sectoresSinEnergia(self):
        _numeroSectoresSinEnergia = 0
        for _sector in self.listaSectores:
            if(not _sector.tieneEnergia(self.listaPlantas)):
                _numeroSectoresSinEnergia += 1
        return _numeroSectoresSinEnergia
     

#comienzo
_mapaPais = polyHandler.generatePolygon()
cec = compañiaElectrica(_mapaPais)
cec.generarReporte()
