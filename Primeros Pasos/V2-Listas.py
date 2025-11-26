miLista = ["Emilio"]
miLista2 = ["Silvia", "Julia", "Mariana"]

miLista = miLista + miLista2 #Concatenar listas

miLista.insert(2, "Damian") #Insertar en posicion 2

miLista.extend(["Pampa"]) #Se agrega al infal

print(miLista[:])  #Imprimir toda mi lista

miLista.pop() #Saco el ultimo elemento
print(miLista[:])