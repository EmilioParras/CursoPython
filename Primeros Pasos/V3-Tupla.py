miTupla2 = ("Emilio", 2, 3) #Las tuplas van con ()
miLista2 = list(miTupla2) #Una tupla se puede convertir en una lista

miLista = ["Emilio", 1, False] #Las listas van con []
miTupla = tuple(miLista) #Una lista se puede convertir en una tupla

"""----------------"""
print("Emilio" in miTupla)
print(miTupla.count(1))
print(len(miTupla))

print(miLista2[:])

tuplaFecha = (20, 2, 2004, "Emilio", "Parras")
dia, mes, anio, nombre, apellido = tuplaFecha

print(nombre)
print(apellido)
print(dia)
print(mes)
print(anio)


