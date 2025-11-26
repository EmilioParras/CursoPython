nota = int(input("Introduce tu nota: "))

def calificacion(nota) :
    if nota < 4 :
        print("Desaprobado.")
    elif nota >= 4 and nota <=6 : 
        print("Aprobado")
    elif nota >= 7 and nota <= 10: 
        print("Promocionado.")    

calificacion(nota)