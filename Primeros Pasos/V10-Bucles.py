"""for i in range(6) :
    print(f"Iteracion = {i}") #La f permite ver el valor de i

print("Sin la f delante.")
for i in range(6) :
    print("Iteracion = {i}")

print(" ")
for i in range(6,10,2) : #Va de 2 en 2, desde el 6 hasta el 9.
    print(f"Iteracion = {i}")"""

valido = False

email = input("Ingrese su email. ")

def verificarEmail(email) :
    for i in range(len(email)) :
        if email[i] == "@" :
            return True
        return False
    
if verificarEmail(email) :
    print("Email correcto.")
else :
    print("Email incorrecto vuelve a ingresarlo.")
    email = input("Ingrese su email")
    verificarEmail(email)