# raise nos permite lanzar nuestras propias excepciones personalizadas.

import math

def calcularRaizCuadrada(num) :
    if num < 0 :
        raise ValueError("El numero no puede ser negativo.")
    else :
        return math.sqrt(num)
    
num1 = int(input("Ingrese un numero"))

try :
    print(calcularRaizCuadrada(num1))
except ValueError as ErrorDeNumeroNegativo : 
    print (ErrorDeNumeroNegativo)

print("Finalizo.")