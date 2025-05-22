class Alquiler:
    __nombre: str
    __id : str
    __hora: str 
    __minuto: int 
    __duraAlq: int 
    
    def __init__(self, nombre, id, hora, minuto, duraAlq):
        self.__nombre = nombre
        self.__id = id
        self.__hora = hora
        self.__minuto = minuto
        self.__duraAlq = duraAlq
        
    def getNombre(self):
        return self.__nombre
    def getId(self):
        return self.__id
    def getHora(self):
        return self.__hora
    def getMinuto(self):
        return self.__minuto
    def getDuraAlq(self):
        return self.__duraAlq
    
    def __str__(self):
        return f"nombre:{self.__nombre} hora:{self.__hora} minuto:{self.__minuto} duracion del alquiler:{self.__duraAlq}"
    
    def __gt__(self, otro):   
        if self.__hora > otro.getHora():
            result = True
        elif self.__hora == otro.getHora():
            result = self.__minuto > otro.getMinuto()
        else:
            result = False
        return result
    
    