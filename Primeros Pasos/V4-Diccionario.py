#Clave : valor
miDiccionario = {"Argentina" : "Buenos Aires", "Alemania" : "Berlin", "Francia" : "Paris"}

#Formas de tomar una clave.
 #print(miDiccionario.get("Alemania"))
 #print(miDiccionario["Francia"]) 

miDiccionario["Italia"] = "Lisboa" #Agregar un dato -> [clave] - "Valor"

del miDiccionario["Alemania"] #Borrar [Clave]
miDiccionario["Italia"] = "Roma" #Actualizo el valor de la clave Italia a Roma


diccionarioVariado = {10 : "Messi", 7 : "El bicho", 11 : "Neymar JR", 29 : "Emilio Parras"}

tupla = ["Argentina", "Francia", "España"]
diccionario = {tupla[0] : "Buenos aires", tupla[1] : "Paris", tupla[2] : "Madrid"} #El valor de tupla[pos] sera el indicado luego de los :. 
                                                                                    #Argentina : Buenos Aires, Francia : Paris, España : Madrid

infoJordan = {"Numero" : 23, "Nombre" : "Michael", "Apellido" : "Jordan", "Equipo" : "Chicago Bulls", "Nacimiento" : {"Dia" : 23, "Mes" : 2, "Año" : 1967}, "Anillos" : {"Temporadas" : [91,92,93,96,97,98]} }
print(infoJordan["Anillos"])
print(infoJordan.keys())
print(infoJordan.values())
print(len(infoJordan))