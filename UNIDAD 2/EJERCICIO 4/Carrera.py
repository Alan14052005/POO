
class Carrera:
    __codigoCarrera: int 
    __nombre: str
    __titulo: str
    __duracion: str
    __nivel: str
    __codFacu: int 
    
    def __init__(self, codigoCarrera, nombre, titulo,duracion, nivel, codFacu):
        self.__codigoCarrera = codigoCarrera
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__nivel = nivel 
        self.__codFacu = codFacu
        
    def getCodigoCarrera(self):
        return self.__codigoCarrera   
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion   
    def getTitulo(self):
        return self.__titulo  
    def getCodFacu(self):
        return self.__codFacu 
    def getNivel(self):
        return self.__nivel
    
    def __lt__(self, otro): # operador que permite ordenar algo (ej de mayor a menor)    
        return self.__nombre < otro.getNombre()