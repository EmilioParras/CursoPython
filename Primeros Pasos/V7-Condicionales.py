salario_presidente = int(input("Ingrese el salario del presidente. "))
salario_director = int(input("Ingrese el salario del director. "))
salario_jefeArea = int(input("Ingrese el salario del jefe de area. "))
salario_administrativo = int(input("Ingrese el salario del administrativo. "))

if salario_administrativo < salario_jefeArea < salario_director < salario_presidente :
    print("Saldos correctos.")
else :
    print("Salarios incorrectos.")   