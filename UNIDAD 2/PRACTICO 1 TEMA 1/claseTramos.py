class Tramo:
    __ciudadOri: str
    __ciudadDest: str 
    __distrancia: int 
    __patenteC: str 
    
    def __init__(self, ciudadOri, ciudadDest, distancia, patenteC):
        self.__ciudadOri = ciudadOri
        self.__ciudadDest = ciudadDest
        self.__distrancia = distancia
        self.__patenteC = patenteC
        
    def getCiudadOri(self):
        return self.__ciudadOri
    def getCiudadDest(self):
        return self.__ciudadDest
    def getDistancia(self):
        return self.__distrancia
    def getPatenteC(self):
        return self.__patenteC
    
    def __str__(self):
        return f"Ciudad Origen: {self.__ciudadOri} ciudad destino: {self.__ciudadDest} distancia: {self.__distrancia} Patente del colectivo: {self.__patenteC}"
    
    def __gt__(self, otro):
        return self.__distrancia > otro
    
        