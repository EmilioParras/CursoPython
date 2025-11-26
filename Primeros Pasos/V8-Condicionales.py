carreras = []
minimo = 3

while len(carreras) < minimo :
    carreras.append(input("Ingrese una carrera. ").lower()) #La carrera se agrega en minusculas.
    print("Faltan agregar " + str(minimo - len(carreras)) + " carreras.") #Importante el str() para concatenar

print(carreras[:])
carrera_seleccionada = input("Seleccione una carrera. ")

if carrera_seleccionada.lower() in carreras :
    print("Usted selecciono " + carrera_seleccionada) 
else :
    print("La carrea no existe.")