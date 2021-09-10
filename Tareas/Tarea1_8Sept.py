
# -El colegio presenta 5 cursos.

# 




# Cada curso se compone por:
#    A. Examen 20%
#    B. Tareas: 60%
#       - 5 tareas independientes
#    C. Final: 20%











# Generar 100 estudiantes aleatoriamente


listaEstudiantesColegio = [] 

# -Imprima un reporte por cada estudiante que tenga la siguiente informacion:
#    A. Nombre del estudiante
#    B. Nota de cada curso
#    C. Promedio del estudiante
#    D. Si aprobo o no (aprueba si el promedio es mas de 60%)

def reportarInfoEstudiantes(_listaEstudiantesColegio):
  
  
  ########################################################################################################################################################################
  pass

def calcularPromedioColegio():
  
  _promedioColegio = 0 

  for estudiante in _listaEstudiantesColegio:
    
    

  # conseguir lista de los estudiantes
  # acceder a las notas totales de los estudiantes
  # hacer un promedio de las notas totales de los estudiantes
  

  # listaEstudiantesColegio(estudiante)
  # estudiante.calcularNotaTotal()

  _promedioColegio = sumaNotasEstudiantes() / len(listaEstudiantesColegio)

  
  ########################################################################################################################################################################
  return _promedioColegio


def sumaNotasEstudiantes():
  _sumaTotalNotas = 0


  return _sumaTotalNotas




listaEstudiantesColegio = []

########################################################################################################################################################################

# -Imprima un reporte por cada estudiante que tenga la siguiente informacion:
#    A. Nombre del estudiante
#    B. Nota de cada curso
#    C. Promedio del estudiante
#    D. Si aprobo o no (aprueba si el promedio es mas de 60%)
reportarInfoEstudiantes(listaEstudiantesColegio)


# -Al finalizar imprima el promedio del colegio
print("EL promedio del Colegio es: " + str(calcularPromedioColegio()))
