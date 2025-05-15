class Paciente:
    __dniP:str
    __nombre: str
    __unidad: int 
    
    def __init__(self, xdniP,xnombre,xunidad):
        self.__dniP = xdniP
        self.__nombre = xnombre
        self.__unidad = xunidad
        
    def getDni(self):
        return self.__dniP
    def getNombre(self):
        return self.__nombre
    def getUnidad(self):
        return self.__unidad
    
    def __str__(self):
        return f"DNI:{self.__dniP} - NOMBRE:{self.__nombre} - UNIDAD:{self.__unidad}"

    def __lt__(self, otro ):
        return (self.getUnidad(), self.getNombre()) < (otro.getUnidad(), otro.getNombre())