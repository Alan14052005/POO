class depa:
    __numero: str
    __nombre: str
    
    def __init__(self, numero, nombre):
        self.__numero=numero
        self.__nombre=nombre
        
    def getNumero(self):
        return self.__numero
    
    def setNumero(self, otronum):
        self.__numero=otronum

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, otronom):
        self.__nombre=otronom
    
 