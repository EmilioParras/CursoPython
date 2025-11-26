#Podemos capturar varias excepciones poniendo una debajo de la otra de la siguiente manera.
#Lo que pongamos dentro de la clausala finally se va a ejecutar salte o no una excepcion.

def division() :

    try : 
        n1 = float(input("Ingrese el primer numero. "))
        n2 = float(input("Ingrese el segundo numero. "))
        print ("El resultado es " + str(n1/n2))

    except ZeroDivisionError :
        print("No es posible dividir por 0.")
    except ValueError :
        print("Ingrese valores validos.")
    finally : 
        print("Ejecucion finalizada.")
    

division()