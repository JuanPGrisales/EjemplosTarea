import uuid uuid.uuid4()
import random

class coworking():
    def __init__(self,_listaOficinas):
        self.listaOficinas = _listaOficinas

    def generarReporte(self):
        for _oficina in self.listaOficinas:
            print("----------")
            print("Oficina #: ", self.listaOficinas.index(_oficina))
            if(_oficina.propietario != None):
                print("El identificador de la empresa es: ", _oficina.propietario.identificador)
            else:
                print("Esta oficina esta desocupada")
            print("El costo de la oficina es: ", _oficina.costo())
            print("La renta de la oficina es: ", _oficina.renta())
        print("------COWORKING-------")
        print("Costos: ", self.costo())# Anunciar costos coworking
        print("Ingresos: ", self.ingresos())
        print("Puestos potenciales ocupados: " + self.puestosOcupados())

    def generarEmpresas(self,_numeroEmpresas):
        for i in range(_numeroEmpresas):
            _empresa = empresa()
            for _oficina in self.listaOficinas:
                tienePropietario = _oficina.propietario == None
                cabeEmpresa =_oficina.numeroPuestos >= _empresa.numeroEmpleados
                puedePagar = _empresa.capital >= _oficina.renta()
                if(tienePropietario & cabeEmpresa & puedePagar):
                    self.listaOficinas[self.listaOficinas.index(_oficina)].propietario = _empresa
                    break
    
    def costo(self):
        _numeroPuestosTotales = 0
        for _oficina in self.listaOficinas:
            _numeroPuestosTotales += _oficina.numeroPuestos
        _costo = (_numeroPuestosTotales*500000) + 10000000
        return _costo

    def ingresos(self):
        _ingresos = 0
        for _oficina in self.listaOficinas:
            _ingresos += _oficina.costo()
        return _ingresos    
    
    def puestosOcupados(self):
        _puestosOcupados = 0
        _puestosTotales =  0 
        for _oficina in self.listaOficinas:
            _puestosTotales += _oficina.numeroPuestos
            if(_oficina.propietario != None):
                _puestosOcupados += _oficina.propietario.numeroEmpleados
        _puestosPotenciales = str(_puestosOcupados) + '/' + str(_puestosTotales)
        return _puestosPotenciales
            

class empresa():
    def __init__(self):
        self.identificador = uuid.uuid4()
        self.capital = random.randint(1000000,100000000) 
        self.numeroEmpleados = random.randint(2,10)


class oficina():
    def __init__(self,_vistaExterior, _numeroPuestos, _numeroPuestosPremium, _espacioAbierto):
        self.propietario = None
        self.vistaExterior = _vistaExterior
        self.numeroPuestos = _numeroPuestos
        self.numeroPuestosPremium = _numeroPuestosPremium
        self.espacioAbierto = _espacioAbierto
    
    def costo(self):
        _costo = (self.numeroPuestos*500000) + (self.numeroPuestosPremium*200000)
        return _costo

    def renta(self):
        multVista = 0
        multEspacio = 0
        if(self.vistaExterior):
            multVista = 1
        if(self.espacioAbierto):
            multEspacio = 1
        _renta = (multVista*1000000) - (multEspacio*1000000) + (self.numeroPuestos*600000) + (self.numeroPuestosPremium*200000)
        if(self.propietario == None):
            _renta=0
        return _renta
  

#comienzo
listaOficinas = [
    oficina(False, 2, 0, False),
    oficina(False, 2, 0, False),
    oficina(False, 2, 0, False),
    oficina(False, 3, 0, False),
    oficina(False, 3, 0, False),
    oficina(False, 5, 0, False),
    oficina(False, 8, 0, False),
    oficina(False, 8, 0, False)
    ]
for i in range(6):
    listaOficinas.append(oficina(False, 6, 0, False))

coworkingEspecial = coworking(listaOficinas)

coworkingEspecial.generarEmpresas(20)

coworkingEspecial.generarReporte()
