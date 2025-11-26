#Continue -> Pasa a la siguiente iteracion del bucle

i = 0
for letra in "Hola todo bien?" :
    if letra == " " :
        continue
    i = i+1

print("Total de caracteres " + str(i))

#Pass -> Devuelve null

class miClase :
    pass

#Else -> En el caso de abajo, el ese se ejecuta una vez termine de recorrer el bucle.
        # El break corta el bucle en caso de encontrar el @.

email = input/("Ingrese su email, por favor.")

for i in email :
    if i == "@" :
        arroba = True
        break
else :
    arooba = False

print(arroba)