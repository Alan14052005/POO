class Colectivo:
    __patente: str
    __marca: str
    __modelo: int
    __capacidad:int 
    __dniDelC: int  
    __consumoProm: int 
    
    def __init__(self, patente, marca, modelo, capacidad, dniDelC):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo 
        self.__capacidad = capacidad
        self.__dniDelC = dniDelC
        self.__consumoProm = 35
        
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getCapacidad(self):
        return self.__capacidad
    def getDniDelC(self):
        return self.__dniDelC
    def getConsumoProm(self):
        return self.__consumoProm
    
    def __str__(self):
        return f"Patente:{self.__patente} Marca:{self.__marca} Modelo:{self.__modelo} Capacidad:{self.__capacidad} Dni del chofer{self.__dniDelC}"
    