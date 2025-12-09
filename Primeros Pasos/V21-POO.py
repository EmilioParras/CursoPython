class Auto() :

    def __init__(self) : # Constructor
        self.__ruedas = 4 # Como el this.ruedas en java. 
        self.__puertas = 4 # Los guines bajos encapsulan el atributo. No se puede modificar desde fuera de la clase.
        self.__largo = 120
        self.__ancho = 80
        self.__enMarcha = False
        self.__gasolina = 100
        self.__puertaCerradas = True
        self.__aceite = 100

    def datos(self) :
        print("El coche tiene", self.__ruedas, "ruedas.", "Un largo de", self.__largo, "centimetros y un ancho de", self.__ancho, "centimetros.")

    def arrancar(self) :
        self.__enMarcha = self.__chequeoGeneral()

        if (self.__enMarcha == True) :
            print("Arrancando.")
        else :
            print("Error en el chequeo.")
    
    def __chequeoPuertas(self) :
        if(self.__puertaCerradas == True) :
            return True
        else :
            return False
    
    def __chequeoGasolina(self) :
        if(self.__gasolina > 0) :
            return True
        else :
            return False
    
    def __chequeoAceite(self) :
        if(self.__aceite > 0) :
            return True
        else :
            return False
    
    def __chequeoGeneral(self) :
        if (self.__chequeoAceite() and self.__chequeoGasolina() and self.__chequeoPuertas()) :
            return True
        else :
            return False
        

auto = Auto()

auto.datos()
auto.arrancar()