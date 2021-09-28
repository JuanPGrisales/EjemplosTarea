import uuid
import numpy as np
import matplotlib.pyplot as plt
import copy

class contrato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.serviciosContratados = {}        

class prestamo:
    def __init__(self, id, valor, tasaInteres):
        self.valorRestante = valor
        self.tasaInteres = tasaInteres
        self.valor = valor

    def cuota(self):       
        return (self.valorRestante * self.tasaInteres) / 12

class servicio:
    def __init__(self, nombre, precio, horas):
        self.precio = precio
        self.horas = horas
        self.horasTrabajadas = 0
        self.estado = 'Inicializado'

class empleado:
    def __init__(self, key, cargo, remuneracion, duracion):
        self.cargo = cargo
        self.remuneracion = remuneracion

class arriendo:
    def __init__(self, inmueble, renta, duracion):
        self.renta = renta

class compañiaProgramacion:
    def __init__(self):
        self.capital = 0
        self.contratos = {}
        self.prestamos = {}
        self.serviciosOfrecidos = {}
        self.empleados = {}
        self.arriendos = {}

    def tomarPrestamo(self, valor, tasaInteres):
        id = str(uuid.uuid4().hex)
        self.prestamos.update({id:prestamo(id, valor, tasaInteres)})      
        self.capital += valor # capital de la compañia aumenta por el valor 

    def calcularCuotaPrestamo(self, idPrestamo):
        numeroPagosPrestamo = 12
        cuotaPrestamoMes = (self.prestamos[idPrestamo].valorRestante * self.prestamos[idPrestamo].tasaInteres) / numeroPagosPrestamo
        return cuotaPrestamoMes
                
    def gastarDinero(self,valor):
        self.capital -= valor          

    def agregarServicioOfrecido(self, nombre, precio, horas):
        self.serviciosOfrecidos.update({nombre:servicio(nombre, precio, horas)})

    def emplear(self, cargo, remuneracion, duracion):
        key = str(uuid.uuid4().hex)
        self.empleados.update({key : empleado(key, cargo, remuneracion, duracion)})
        
    def arrendar(self, inmueble, renta, duracion):
        self.arriendos.update({inmueble:arriendo(inmueble, renta, duracion)})

    def licitar(self, nombre):
        self.contratos.update({nombre:contrato(nombre)}) 

    def agregarServicioContrato(self, idContrato, idServicioNuevo, idServicioContratado):
        self.contratos[idContrato].serviciosContratados.update({idServicioNuevo : self.serviciosOfrecidos[idServicioContratado]})

    def finalizarServicioContrato(self, idContrato, idServicioContratado):
        self.contratos[idContrato].serviciosContratados[idServicioContratado].estado = 'Finalizado'
        self.capital += self.contratos[idContrato].serviciosContratados[idServicioContratado].precio
            
    def graficarCompañiasEnMeses(self, compañiaEnMeses):
        #####################################
        pass


    def reportarInfo(self):
        print("----------------------Reporte Compañia----------------------")
        print("Los Ingresos del mes son: ", '${:,.2f}'.format(self.ingresos()))
        print("Los Egresos del mes son: ", '${:,.2f}'.format(self.egresos()))
        print("El capital del mes es: ", '${:,.2f}'.format(self.capital))
        print("El delta de dinero del mes es: ", '${:,.2f}'.format((self.ingresos() - self.egresos())))
        print("------------------------------------------------------------------")
        compañiaEnMeses = [self]
        for i in range(1, 13):
            compañiaEnMes = compañiaEnMeses[i - 1].pronosticarProximoMes()
            compañiaEnMeses.append(compañiaEnMes)
            print("Dentro de {0} meses;".format(i))
            print("Los Ingresos del mes seran: ", '${:,.2f}'.format(compañiaEnMes.ingresos()))
            print("Los Egresos del mes seran: ", '${:,.2f}'.format(compañiaEnMes.egresos()))
            print("El capital del mes sera: ", '${:,.2f}'.format(compañiaEnMes.capital))
            print("El delta de dinero del mes sera: ", '${:,.2f}'.format(compañiaEnMes.ingresos() - compañiaEnMes.egresos()))
            print("------------------------------------------------------------------")
            self.graficarCompañiasEnMeses(compañiaEnMeses)

    def pronosticarProximoMes(self):
        compañiaFutura = copy.deepcopy(self)
        numeroEmpleados = 0
        for _, empleado in compañiaFutura.empleados.items():
            if (empleado.cargo == 'Gerente'):
                numeroEmpleados += 1
            if (empleado.cargo == 'Programador'):
                numeroEmpleados += 1
            if (empleado.cargo == 'Diseñador'):
                numeroEmpleados += 1
        for _, contrato in compañiaFutura.contratos.items(): # por contrato 

            horasPronosticadasDisponiblesMesContrato = (numeroEmpleados * 240) / len(compañiaFutura.contratos) #las horas pronosticadas disponibles del mes por contrato = (numeroEmpleados * horas trabajadas) / numeroContratos
            for _, servicio in contrato.serviciosContratados.items(): # por servicio contratado 
                if (servicio.estado != 'Finalizado'): # si el estado del servicio no esta finalizado
                    if (horasPronosticadasDisponiblesMesContrato >= (servicio.horas - servicio.horasTrabajadas)): # si las horas pronosticadas disponibles del mes por contrato son mayores a la (duracion del servicio - horas trabajadas del servicio)
                        servicio.estado = 'Finalizado' # estado del servicio pasa a finalizado
                        servicio.horasTrabajadas += (servicio.horas - servicio.horasTrabajadas) # sumo horas trabajadas del servicio + (duracion del servicio - horas trabajadas del servicio)
                        horasPronosticadasDisponiblesMesContrato -= (servicio.horas - servicio.horasTrabajadas) # a las horas pronosticadas disponibles del mes por contrato - (duracion del servicio - horas trabajadas del servicio)
                    else: # si no
                        servicio.horasTrabajadas += horasPronosticadasDisponiblesMesContrato # a las horas trabajadas del servicio +  las horas pronosticadas disponibles del mes por contrato
                        horasPronosticadasDisponiblesMesContrato = 0 # las horas pronosticadas disponibles del mes por contrato = 0
        compañiaFutura.capital += compañiaFutura.ingresos() - compañiaFutura.egresos() # capital suma ingresos y resta egresos
        for _, prestamo in compañiaFutura.prestamos.items():
            prestamo.valorRestante -= prestamo.cuota() # valor restante de la deuda - pagoCuotaMes
        return compañiaFutura

    def ingresos(self):
        numeroEmpleados = 0
        for _, empleado in self.empleados.items():
            if (empleado.cargo == 'Gerente'):
                numeroEmpleados += 1
            if (empleado.cargo == 'Programador'):
                numeroEmpleados += 1
            if (empleado.cargo == 'Diseñador'):
                numeroEmpleados += 1
        calculoIngresos = 0
        horasTrabajadasEmpleadoMes = 240 * len(self.empleados)
        for _, contrato in self.contratos.items():
            tiempoPronosContratosMesDisponible = (numeroEmpleados * horasTrabajadasEmpleadoMes) / len(self.contratos)
            for _, servicioContratado in contrato.serviciosContratados.items():
                if (servicioContratado.estado != 'Finalizado'):
                    if (tiempoPronosContratosMesDisponible >= (servicioContratado.horas - servicioContratado.horasTrabajadas)):
                        calculoIngresos += servicioContratado.precio
                        tiempoPronosContratosMesDisponible -= servicioContratado.horas - servicioContratado.horasTrabajadas
                    else:
                        tiempoPronosContratosMesDisponible = 0
        return calculoIngresos

    def egresos(self):
        calculoEgresos = 0
        for _, empleado in self.empleados.items():
            calculoEgresos += empleado.remuneracion
        for _, arriendo in self.arriendos.items():
            calculoEgresos += arriendo.renta
        for _, prestamo in self.prestamos.items():
            calculoEgresos += prestamo.cuota() 
        return calculoEgresos

#comienzo
compañiaNoxiun = compañiaProgramacion()

compañiaNoxiun.tomarPrestamo(25000000, 0.1589) # Para comenzar, la compañía tomo un préstamo de 25 millones
compañiaNoxiun.gastarDinero(25000000) # los cuales fueron todos utilizados de inmediato par establecerse.

 # •	La compañía agrega los siguientes productos:
compañiaNoxiun.agregarServicioOfrecido('Arquitectura de Sistemas', 5000000, 320)# o	Arquitectura de sistemas: 5 millones (160 horas / mes, 2 meses)
compañiaNoxiun.agregarServicioOfrecido('Diseño Marca', 5000000, 320)# o	Diseño de marca: 5 millones (160 horas / mes, 2 meses)
compañiaNoxiun.agregarServicioOfrecido('Implementacion de Planos', 5000000, 320)# o	Implementación de planos (arquitecturas, aplicaciones o páginas web): 5 millones (160 horas / mes, 2 meses)
compañiaNoxiun.agregarServicioOfrecido('Diseño Web', 2500000, 160)# o	Diseño web: 2.5 millones / 10 páginas (80 horas / mes, 2 meses)
compañiaNoxiun.agregarServicioOfrecido('Implementacion Web', 2500000, 160)# o	Implementación web: 2.5 millones/10 páginas (80 horas / mes, 2 meses)
compañiaNoxiun.agregarServicioOfrecido('Diseño Modulo', 5000000, 320)# o	Diseño modulo: 5 millones (Nota: diseño + implementación como notado arriba es 5 millones ósea 5+5=10) (160 horas / mes, 2 meses)
compañiaNoxiun.agregarServicioOfrecido('SAM', 1500000, 32)# o	SAM: 1.5 millones / mes (32 horas / mes)
compañiaNoxiun.agregarServicioOfrecido('Diseño Basico', 500000, 20)# o	Diseño básico: 500 mil pesos (logo, icono, o 15 segundos de video) (20 horas / semana, 1 semana)

# •	La compañía emplea los siguientes empleados, todos con una duracion de 12 meses:
compañiaNoxiun.emplear('Gerente', 1500000, 12) # o	Gerente: 1.5 millones / mes
compañiaNoxiun.emplear('Programdor', 1500000, 12)    # o	Programador: 1.5 millones / mes
compañiaNoxiun.emplear('Diseñador', 1500000, 12)    # o	Diseñador: 1.5 millones/mes
compañiaNoxiun.emplear('Contadora', 500000, 12)    # o	Contadora: 500 mil / mes
compañiaNoxiun.emplear('Abogada', 500000, 12)    # o	Abogada: 500 mil / mes

# •	La compañía arrienda una oficina por 2500000 con una duracion de 12 meses:
compañiaNoxiun.arrendar('Oficina', 2500000, 12)

# La compañía tiene un contrato existente de 80 millones que tiene los siguientes artículos:
compañiaNoxiun.licitar('Animalapp') # Licitar contrato

compañiaNoxiun.agregarServicioContrato('Animalapp', 'DM0', 'Diseño Marca')# o	Diseño (5 millones)
compañiaNoxiun.agregarServicioContrato('Animalapp', 'IP0', 'Implementacion de Planos') # implementación de arquitectura (5 millones)
compañiaNoxiun.agregarServicioContrato('Animalapp', 'DW0', 'Diseño Web')# o	Diseño web (2.5 millones)
compañiaNoxiun.agregarServicioContrato('Animalapp', 'IW0', 'Implementacion Web') # implementación web (2.5 millones)    
for i in range(1, 7):
    compañiaNoxiun.agregarServicioContrato('Animalapp', 'DM' + str(i), 'Diseño Modulo')# 6 módulos diseñados (30 millones)
    compañiaNoxiun.agregarServicioContrato('Animalapp', 'IP' + str(i), 'Implementacion de Planos') # 6 módulos de implementación de arquitectura (30 millones)

compañiaNoxiun.agregarServicioContrato('Animalapp', 'DW1', 'Diseño Web')# o	Diseño web (2.5 millones)
compañiaNoxiun.agregarServicioContrato('Animalapp', 'IW1', 'Implementacion Web') # implementación web (2.5 millones)    

# o	NOTA: De este contrato se han completado todos los artículos menos 5 módulos extras con diseño e implementación (50 millones faltantes)

compañiaNoxiun.finalizarServicioContrato('Animalapp', 'DM0')
compañiaNoxiun.finalizarServicioContrato('Animalapp', 'IP0')
compañiaNoxiun.finalizarServicioContrato('Animalapp', 'DW0')
compañiaNoxiun.finalizarServicioContrato('Animalapp', 'IW0')
compañiaNoxiun.finalizarServicioContrato('Animalapp', 'DM1')
compañiaNoxiun.finalizarServicioContrato('Animalapp', 'IP1')
compañiaNoxiun.finalizarServicioContrato('Animalapp', 'DW1')
compañiaNoxiun.finalizarServicioContrato('Animalapp', 'IW1')

# o	NOTA: De los otros 30 millones que fueron pagados, 10 fueron utilizados y 10 están guardados en el banco, exequibles.
compañiaNoxiun.gastarDinero(20000000)

# Se acaba de firmar otro contrato con otra empresa por 34 millones que incluye:
compañiaNoxiun.licitar('CoproInge')
compañiaNoxiun.agregarServicioContrato('CoproInge', 'DM0', 'Diseño Modulo')# o	Diseño (5 millones)
compañiaNoxiun.agregarServicioContrato('CoproInge', 'IP0', 'Implementacion de Planos') # implementación de arquitectura (5 millones)
compañiaNoxiun.agregarServicioContrato('CoproInge', 'DW0', 'Diseño Web')# o	Diseño web (2.5 millones)
compañiaNoxiun.agregarServicioContrato('CoproInge', 'IW0', 'Implementacion Web') # implementación web (2.5 millones)    
compañiaNoxiun.agregarServicioContrato('CoproInge', 'DM1', 'Diseño Modulo')# o	Diseño (5 millones)
compañiaNoxiun.agregarServicioContrato('CoproInge', 'IP1', 'Implementacion de Planos') # implementación de arquitectura (5 millones)
for i in range(6):
    compañiaNoxiun.agregarServicioContrato('CoproInge', 'SAM' + str(i), 'SAM') # o	SAM (6 Meses) (9 Millones) (Comienza al final del resto)

compañiaNoxiun.reportarInfo()

# compañiaNoxiun.generarContratos(5)
######################################
# compañiaNoxiun.reportarInfo()
######################################