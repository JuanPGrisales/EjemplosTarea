import random

class colegio:
    def __init__(self):
        
        self.diccionarioEstudiantes = {}

    def calcularSumaNotasEstudiantes(self):
        _listaNotasEstudiantes = self.listarNotaEstudiantes() # Notas de los estudiantes  
        _sumaNotasEstudiantes = sum(_listaNotasEstudiantes) # sumar las notas de los estudiantes
        return _sumaNotasEstudiantes

    def listarNotaEstudiantes(self):
        _listaNotaEstudiantes = []
        for identificadorEstudiante in self.diccionarioEstudiantes:
            # print(estudiante.calcularNotaTotal()) # imprimir nota total estudiante
            _notaTotalEstudiante = self.diccionarioEstudiantes[identificadorEstudiante].calcularNotaTotal()     # ingresar nota total en una lista
            _listaNotaEstudiantes.append(_notaTotalEstudiante)  
        return _listaNotaEstudiantes

    def contarCantidadEstudiantes(self):
        _listaEstudiantes = self.diccionarioEstudiantes # necesito una lista de estudiantes
        _cantidadEstudiantes = len(_listaEstudiantes) # necesito contar los elementos la lista estudiantes
        return _cantidadEstudiantes

    def reportarInfoEstudiantes(self):       
       for _identificadorEstudiante in self.diccionarioEstudiantes: 
           estudianteTemporal = self.diccionarioEstudiantes[_identificadorEstudiante]
           print(estudianteTemporal.nombre)# imprime nombre del estudiante
           tamañoDiccionarioCursos = len(self.diccionarioEstudiantes[_identificadorEstudiante].diccionarioCursos)
           for i in range(0,tamañoDiccionarioCursos):
                _identificadorCurso = 'Curso' + str(i)
                _notaTotalCurso = estudianteTemporal.diccionarioCursos[_identificadorCurso].calcularNotaTotal()
                _textobonito = "La nota total del {0} es {1}"
                print(_textobonito.format(_identificadorCurso,_notaTotalCurso)) # imprime la nota total del curso
           print("El promedio del estudiante es ", estudianteTemporal.calcularNotaTotal()) # imprime el promedio del estudiante 
           if(estudianteTemporal.calcularNotaTotal()>3):
               print("El estudiante aprobo")
           else:
               print("El estudiante no aprobo")
            
class estudiante:
    def __init__(self,_nombre):
        self.nombre = _nombre
        self.diccionarioCursos = {}

    def calcularNotaTotal(self):
        _notaTotal = 0
        for _idCurso in self.diccionarioCursos:
            _notaTotalCurso = self.diccionarioCursos[_idCurso].calcularNotaTotal() 
            _notaTotal += _notaTotalCurso
        return _notaTotal / len(self.diccionarioCursos)
    

class curso:
    def __init__(self):
        self.listaNotaTareas = [0]*5

    def calcularNotaTotal(self):
        _notaTareas = sum(self.listaNotaTareas)/len(self.listaNotaTareas)
        _notaTotal= (self.notaExamen*0.2) + (self.notaFinal*0.2) + (_notaTareas*0.6) # Nota total del curso
        return _notaTotal

#comienzo
gemelli = colegio()


for i in range(100):
    _nombreEstudiante = "Estudiante" + str(i)
    gemelli.diccionarioEstudiantes[_nombreEstudiante] = (estudiante(_nombreEstudiante))
    for j in range(5):
        _identificadorCurso = "Curso" + str(j)
        gemelli.diccionarioEstudiantes[_nombreEstudiante].diccionarioCursos[_identificadorCurso] = curso()
        gemelli.diccionarioEstudiantes[_nombreEstudiante].diccionarioCursos[_identificadorCurso].notaExamen = random.randint(0,50) / 10
        gemelli.diccionarioEstudiantes[_nombreEstudiante].diccionarioCursos[_identificadorCurso].notaFinal = random.randint(0,50) / 10
        _listaNotaTareas = gemelli.diccionarioEstudiantes[_nombreEstudiante].diccionarioCursos[_identificadorCurso].listaNotaTareas
        for _posicionNotaTarea in range(len(_listaNotaTareas)):
            gemelli.diccionarioEstudiantes[_nombreEstudiante].diccionarioCursos[_identificadorCurso].listaNotaTareas[_posicionNotaTarea] = random.randint(0,50) / 10

sumaNotasEstudiantes = gemelli.calcularSumaNotasEstudiantes()
cantidadEstudiantes = gemelli.contarCantidadEstudiantes()
promedioColegio = sumaNotasEstudiantes / cantidadEstudiantes

gemelli.reportarInfoEstudiantes() # imprimir reporte por cada estudiante
print("El promedio del colegio es: ", promedioColegio)
