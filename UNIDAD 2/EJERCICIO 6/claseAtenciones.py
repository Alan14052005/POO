class Atencion:
    __dni : str
    __fechaAte: str
    __importe: float 
    
    def __init__(self, xdni, xfechaAte, ximporte):
        self.__dni = xdni
        self.__fechaAte = xfechaAte
        self.__importe = ximporte
        
    def getDni(self):
        return self.__dni
    def getFechaAte(self):
        return self.__fechaAte
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"ID:{self.__dni} - Fecha:{self.__fechaAte} - Importe:${self.__importe:.2f}"
