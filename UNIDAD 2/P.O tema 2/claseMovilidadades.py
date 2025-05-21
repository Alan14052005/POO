class Movilidad: 
    __patente: str
    __tipo: str
    __capCarga: int 
    __impMensual: int
    __marca: str
    __modelo: str 
    
    def __init__(self, patente, tipo, capCarga, impMensual, marca, modelo):
        self.__patente = patente
        self.__tipo = tipo
        self.__capCarga = capCarga
        self.__impMensual = impMensual
        self.__marca = marca
        self.__modelo = modelo
        
    def getPatente(self):
        return self.__patente
    def getTipo(self):
        return self.__tipo
    def getCapCarga(self):
        return self.__capCarga
    def getImpMensual(self):
        return self.__impMensual
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    
    def __str__(self):
        return f"Patente:{self.__patente} Tipo:{self.__tipo} capacidad de carga:{self.__capCarga} importe mensual por patente:{self.__impMensual} marca:{self.__marca} modelo:{self.__modelo}"
    
    