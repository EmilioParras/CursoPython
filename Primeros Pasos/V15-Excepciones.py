#Las excepciones son errores en tiempo de ejecucion. Cuando ocurren estos errores se cae todo el programa, cortando la ejecucion de las lineas debajo de la linea donde ocurre el error.

def suma (n1,n2) :
    return n1+n2

def resta (n1,n2) :
    return n1-n2

def multiplicacion (n1,n2) :
    return n1*n2

def division (n1,n2) :
    
    try : #Basicamente es decirle al programa INTENTA realizar esta operacion, si no podes ejecuta lo de dentro del except. 
        return n1/n2
    except ZeroDivisionError: #Si la excepcion por la que el programa cae no es la indicada luego del except, el programa caere igualmente.
        print("No se puede dividir por 0")
        return "Operacion erronea" #Importante devolver algo. Si no devolvera un none.


n1 = int(input("Ingrese un numero "))
n2 = int(input("Ingrese otro numero "))

operacion = input("Ingrese la operacion a realizar. (suma - resta - multiplicacion - division) ")

if (operacion == "suma") :
    print(suma(n1,n2))
elif (operacion == "resta") :
    print(resta(n1,n2))
elif(operacion == "multiplicacion") :
    print(multiplicacion(n1,n2))
elif(operacion == "division") :
    print(division(n1,n2))
else :
    print("Operacion no disponible.")

print("Continuamos guardando los datos del programa.")