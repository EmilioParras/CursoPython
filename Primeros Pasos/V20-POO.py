class Auto() :

    puertas = 2
    ancho = 80
    largo = 130
    enMarcha = False

    def arrancar(self) : #Self -> this en java
        self.enMarcha = True

    def isEnMarcha(self) : 
        if(self.enMarcha) :
            return True
        else :
            return False

instanciaAuto = Auto()
instanciaAuto.arrancar()

print(instanciaAuto.isEnMarcha())
