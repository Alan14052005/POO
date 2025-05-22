class Cancha:
    __id : str 
    __tipopiso: str
    __importe : int 
    
    def __init__(self, id , tipopiso, importe):
        self.__id = id
        self.__tipopiso = tipopiso
        self.__importe = importe
        
    def getId(self):
        return self.__id
    def getTipoPiso(self):
        return self.__tipopiso
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"Id:{self.__id} tipo de piso:{self.__tipopiso} importe:{self.__importe}"        