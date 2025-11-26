edad = int(input("Introduce tu edad. "))
i = 0

while edad < 18 : 
    print("Debes ser mayor de edad.")
    edad = int(input("Introduce tu edad nuevamente. "))
    i = i+1

print(f"Ingresaste mal tu edad {i} veces.")
print(f"Edad : {edad}")