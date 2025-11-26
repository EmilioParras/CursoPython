def getCiudades(*ciudades) : #El * indica que recibe una TUPLA de cantidad indeterminada.
    for elemento in ciudades :
        #for subElemento in elemento :
        yield from elemento

ciudadesDevueltas = getCiudades("Madrid", "Barcelona", "Buenos aires", "Jujuy")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))