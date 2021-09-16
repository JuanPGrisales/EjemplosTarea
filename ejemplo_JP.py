import random
import uuid 

class compañiaElectrica:
    def __init__(self, _mapaPais):
        self.pais = pais(_mapaPais) 
    def generarReporte(self):
        if(self.pais == None):
            print('No existe pais')
            return
        print('-----Seccion Pais----')
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
        
        print('-----Seccion Plantas----')
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
            print('----------------')
        
        print('-----Seccion Sectores----')
        for _sector in self.pais.listaSectores:
            #a.	Nombre de cada sector (id)
            print('El nombre del sector es: ', _sector.id)
            #b.	Energía recibida
            print('La energia recibida del sector es de: ', _sector.energiaRecibida())
            #c.	Energía consumida
            print('La energia consumida del sector es de: ', _sector.energiaConsumida())
            #d.	# de transformadores
            print('El numero de transformadores es: ', len(_sector.listaTransformadores))
            #e.	Energía por transformador
            print('La energia por transformador es: ', _sector.energiaPorTransformador())
            #f.	Número de clientes
            print('El numero de clientes es: ', _sector.numeroClientes())
            #g.	Energía promedio / cliente
            print('La energia consumida por cliente es de: ', _sector.energiaConsumidaCliente())
            #h.	Energía promedio / edificación
            print('La energia consumida por edificacion es de: ', _sector.energiaConsumidaEdificacion())
            print('----------------')

class planta:
    def __init__(self):
        self.id = uuid.uuid4()
        self.listaIDSectoresAsistidos = [] 
        _tipos = ('HidroElectrica', 'Eolica', 'Solar')
        self.tipo = random.choice(_tipos)
    
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

class transformador:
    def __init__(self):
        self.listaEdificaciones = []



class sector:
    def __init__(self):
        self.id = uuid.uuid4()
        self.listaTransformadores = []
        for i in range(random.randint(10,15)):
            self.listaTransformadores.append(transformador())

    def energiaRecibida(self):
        #############################
        return
    def energiaConsumida(self):
        ##############################
        return 0
    def energiaPorTransformador(self):
        ##############################
        return
    def numeroClientes(self):
        ##############################
        return
    def energiaConsumidaCliente(self):
        ##############################
        return
    def energiaConsumidaEdificacion(self):
        ##############################
        return
        

class pais:
    def __init__(self, _mapaPais):
        self.mapaPais = _mapaPais
        self.listaPlantas = []
        for i in range(random.randint(2,4)):
            self.listaPlantas.append(planta())
        self.listaSectores = [] 
        for i in range(random.randint(20,30)):
            self.listaSectores.append(sector())

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
            _calculoNumeroClientes = _sector.numeroClientes()
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
        
        #####################################
        return
    def clienteMayorConsumo(self):
        
        #####################################
        return
        

#comienzo
_mapaPais = [[0,0], [0,35000], [35000,35000], [35000,0]]
cec = compañiaElectrica(_mapaPais)
cec.generarReporte()
