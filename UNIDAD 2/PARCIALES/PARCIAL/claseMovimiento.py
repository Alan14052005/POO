class Movimiento:
    __numeroDeCuenta: int
    __fecha: str
    __descripcion: str
    __tipoDeMovimiento: str
    __importe: float
    
    def __init__(self, numeroDeCuenta, fecha, descripcion, tipoDeMovimiento, importe):
        self.__numeroDeCuenta = numeroDeCuenta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoDeMovimiento = tipoDeMovimiento
        self.__importe = importe 
        
    def getNumeroDeCuenta(self):
        return self.__numeroDeCuenta
    def getFecha(self):
        return self.__fecha
    def getDescripcion (self):
        return self.__descripcion
    def getTipoDeMovimiento(self):
        return self.__tipoDeMovimiento
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"Numero de Cuenta:{self.__numeroDeCuenta} Fecha:{self.__fecha} Descripcion:{self.__descripcion} tipo de movimiento:{self.__tipoDeMovimiento} importe:{self.__importe}"
    
    def __lt__(self, otro):
        return self.getNumeroDeCuenta() < otro.getNumeroDeCuenta()