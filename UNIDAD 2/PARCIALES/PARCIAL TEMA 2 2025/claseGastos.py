class Gasto:
    __patente: str
    __fecha: str
    __impGasto: int
    __descripcion: str 
    
    def __init__(self, patente, fecha, impGasto, descripcion):
        self.__patente = patente
        self.__fecha = fecha
        self.__impGasto = impGasto
        self.__descripcion = descripcion
        
    def getPatente(self): 
        return self.__patente
    def getFecha(self):
        return self.__fecha
    def getImpGasto(self):
        return self.__impGasto
    def getDescripcion (self):
        return self.__descripcion
    
    def __str__(self):
        return f"Patente:{self.__patente} fecha:{self.__fecha} Importe del gasto:{self.__impGasto} descripcion:{self.__descripcion}"
    

        
    def __lt__(self, otro):   
        resultado = None
        if self.__patente == otro.getPatente():
            resultado = self.__patente.lower() < otro.getPatente().lower()
        else:
            resultado = self.__fecha.lower() < otro.getFecha().lower()
        return resultado     