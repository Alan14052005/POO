class Beca:
    __id: int
    __tipo: str
    __importe: float
    
    def __init__(self, xid, xtipo, ximporte):
        self.__id = xid
        self.__tipo = xtipo
        self.__importe = ximporte
        
    def getId(self):
        return self.__id
    def getTipo(self):
        return self.__tipo
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"ID:{self.__id} TIPO:{self.__tipo} IMPORTE:{self.__importe}"