class Movimiento:
    __numTarjeta: int 
    __fecha: str
    __descripcion: str
    __tipoMov: str
    __importe: int 
    
    def __init__(self, numTarjeta, fecha, descripcion, tipoMov, importe):
        self.__numTarjeta = numTarjeta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoMov = tipoMov
        self.__importe = importe 
        
    def getNumTarjeta(self):
        return self.__numTarjeta
    def getFecha(self):
        return self.__fecha
    def getDescripcion(self):
        return self.__descripcion
    def getTipoMov(self):
        return self.__tipoMov
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"Numero de Tarjeta:{self.__numTarjeta}  Fecha:{self.__fecha}  Descripcion:{self.__descripcion}  Tipo de movimiento:{self.__tipoMov}  Importe:{self.__importe}"
    
    def __lt__(self, otro):
        return self.__numTarjeta < otro.getNumTarjeta()
         