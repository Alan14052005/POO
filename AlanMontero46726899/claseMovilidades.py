#Montero Alan 46726899
class Movilidad:
    __patente: str
    __tipo: str
    __capDeCarga: int
    __importeMxP: float
    __marca: str
    __modelo: str
    
    def __init__(self, patente, tipo, capDeCarga, importeMxP, marca, modelo):
        self.__patente = patente
        self.__tipo = tipo
        self.__capDeCarga = capDeCarga
        self.__importeMxP = importeMxP
        self.__marca = marca
        self.__modelo = modelo
        
    def getPatente(self):
        return self.__patente
    def getTipo(self):
        return self.__tipo
    def getCapDeCarga(self):
        return self.__capDeCarga
    def getImporteMxP(self):
        return self.__importeMxP
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    
    def __str__(self):
        return f"Patente:{self.__patente} tipo:{self.__tipo} capacidad de carga:{self.__capDeCarga} importe mensual por patente{self.__importeMxP} marca:{self.__marca} modelo:{self.__modelo}"
    
    
        