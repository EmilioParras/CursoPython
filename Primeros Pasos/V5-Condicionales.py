print("Sistema de notas para alumnos")

nota_alumno = input("Introduce la nota del alumno: ") #Todo lo que se ingrese por input() python lo considera como texto. 
def evaluacion(nota) :
    resultado = "Desaprobado"
    if nota >= 4 :
        resultado = "Aprobado"
    if nota >= 7 :
        resultado = "Promocionado"
    return resultado

print(evaluacion(int(nota_alumno))) #int() pasa el valor del input() a un int si es posible.