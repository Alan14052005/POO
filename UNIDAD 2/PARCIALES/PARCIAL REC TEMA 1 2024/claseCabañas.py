class Cabaña:
    __numero: int 
    __cantHab: int 
    __cantCamaG: int 
    __cantCamaC: int 
    __importdia: int
    
    def __init__(self, numero, cantHab, cantCamaG, cantCamac, importdia):
        self.__numero = numero
        self.__cantHab = cantHab
        self.__cantCamaC = cantCamac
        self.__cantCamaG = cantCamaG
        self.__importdia = importdia
        
    def getNumero(self):
        return self.__numero
    def getCantHab(self):
        return self.__cantHab
    def getCantCamaG(self):
        return self.__cantCamaG
    def getCantCamaC(self):
        return self.__cantCamaC
    def getImportDia(self):
        return self.__importdia
    
    def __str__(self):
        return f"Numero:{self.__numero} cantidad de habitaciones:{self.__cantHab} cantidadad de camas grandes:{self.__cantCamaG} cantidad de camas chicas:{self.__cantCamaC} importe por dia:{self.__importdia}"
    
    def __ge__(self, otro):
        capacidad = self.__cantCamaG *2 + self.__cantCamaC
        return capacidad >= otro  