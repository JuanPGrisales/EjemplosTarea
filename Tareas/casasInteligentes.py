import uuid
import random

class compañiaEdificacionesInteligentes:

    def __init__(self):
        self.dict_Inmobiliarios = {}
    
    def reportarInfoIngresos(self):
        print("---------------GANANCIA TOTAL-----------------")
        print("Fue de: ", self.gananciaTotal())
        print("---------------TOTAL AIRE AUTOMATICO-----------------")
        print("Fue de: ", self.contarAire())
        print("---------------TOTAL AGUA AUTOMATICA-----------------")
        print("Fue de: ", self.contarAgua())
        print("---------------TOTAL ELECTRICIDAD AUTOMATICA-----------------")
        print("Fue de: ", self.contarElectricidad())
        print("---------------INMOBILIARIOS-----------------")
        for _id, _inmobiliario in self.dict_Inmobiliarios.items():
            print("El id del inmobiliario es: ", _id)
            print("El gasto total del imobiliario es: ", _inmobiliario.gastoTotal())
            print("--------------------------------------------")
        
    def generar(self):
        for _ in range(100):
            idInmobiliaria = str(uuid.uuid4().hex)
            self.dict_Inmobiliarios[idInmobiliaria] = inmobiliario(idInmobiliaria) #genero 100 edificaciones aleatoriamente

    def gananciaTotal(self):
        _calculo = 0
        for _, _inmobiliario in self.dict_Inmobiliarios.items():
            _calculo += _inmobiliario.gastoTotal()
        return _calculo

    def contarAire(self):
        _cuenta = 0
        for _, _inmobiliario in self.dict_Inmobiliarios.items():
            if ("Aire Automatico" in _inmobiliario.listaTiposSubsistemas):
                _cuenta += 1
        return _cuenta
    
    def contarAgua(self):
        _cuenta = 0
        for _, _inmobiliario in self.dict_Inmobiliarios.items():
            if ("Agua Automatica" in _inmobiliario.listaTiposSubsistemas):
                _cuenta += 1
        return _cuenta

    def contarElectricidad(self):
        _cuenta = 0
        for _, _inmobiliario in self.dict_Inmobiliarios.items():
            if ("Electricidad Automatica" in _inmobiliario.listaTiposSubsistemas):
                _cuenta += 1
        return _cuenta

class inmobiliario:
    
    def __init__(self, _id):
        self.id = _id
        _tipos = ("casa","edifcio")
        self.tipo = random.choice(_tipos)
        self.listaTiposSubsistemas = []
        _tiposSubsistemas = ("Aire Automatico", "Agua Automatica", "Electricidad Automatica")
        for _tipo in _tiposSubsistemas:
            deboagregar = random.choice((True,False))
            if(deboagregar):
                self.listaTiposSubsistemas.append(_tipo)
      
    def gastoTotal(self):
        _precio = 0
        for _tipoSubsistema in self.listaTiposSubsistemas:
            if (_tipoSubsistema == "Aire Automatico"): 
                if(self.tipo == "edificio"):
                    _precio += 200*2
                elif(self.tipo == "casa"):
                    _precio += 200
            elif (_tipoSubsistema == "Agua Automatica"): 
                if(self.tipo == "edificio"):
                    _precio += 100*2
                elif(self.tipo == "casa"):
                    _precio += 100
            elif (_tipoSubsistema == "Electricidad Automatica"): 
                if(self.tipo == "edificio"):
                    _precio += 300*2
                elif(self.tipo == "casa"):
                    _precio += 300
        return _precio
        
#comienzo
davoDomotica = compañiaEdificacionesInteligentes()
davoDomotica.generar()
davoDomotica.reportarInfoIngresos()
