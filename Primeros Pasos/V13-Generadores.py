#Generadores -> Estructuras que extraen valor de una funcion, estos valores se almacenan en objetos iterables.

#Generador con funcion tradicional

def generadorPares(limite) :
    num = 1
    lista = []

    while num < limite :
        lista.append(num*2)
        num = num+1

    return lista

print(generadorPares(10))

#Generador de pares con un GENERADOR

def generador(limite) :
    num = 1

    while num < limite :
        yield num * 2
        num = num+1

pares = generador(10)

def test() :
    for i in range(1,11) :
        yield i

for numero in test() :
    print(numero)