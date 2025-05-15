#Montero Alan 46726899
class Gasto:
    __patente: str
    __fecha: str
    __impDeGasto: float
    __descripcion: str
    
    def __init__(self, patente, fecha, impDeGasto, descripcion):
        self.__patente = patente
        self.__fecha = fecha
        self.__impDeGasto = impDeGasto
        self.__descripcion = descripcion
        
    def getPatente(self):
        return self.__patente
    def getFecha(self):
        return self.__fecha
    def getImpDeGasto(self):
        return self.__impDeGasto
    def getDescripcion(self):
        return self.__descripcion
    
    def __str__(self):
        return f"patente:{self.__patente} Fecha:{self.__fecha} importe de gasto:{self.__impDeGasto} descripcion:{self.__descripcion }"
    
    def __lt__(self, other):
        return (self.__fecha, self.__patente) < (other.__fecha, other.__patente)