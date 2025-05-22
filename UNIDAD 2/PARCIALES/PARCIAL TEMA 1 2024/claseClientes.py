class Cliente:
    __nombre: str
    __apellido: str
    __dni: int 
    __numTarjeta:int
    __saldoAnterior: int 
    
    def __init__(self, nombre, apellido, dni, numTarjeta, saldoAnterior):
        self.__nombre = nombre
        self.__apellido = apellido 
        self.__dni = dni
        self.__numTarjeta = numTarjeta
        self.__saldoAnterior = saldoAnterior
        
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido 
    def getDni(self):
        return self.__dni
    def getNumTarjeta(self):
        return self.__numTarjeta
    def getSaldoAnterior(self):
        return self.__saldoAnterior
    
    def __str__(self):
        return f"Nombre:{self.__nombre}  Apellido:{self.__apellido}  DNi:{self.__dni}  Numero de Tarjeta:{self.__numTarjeta}  saldo anterior:{self.__saldoAnterior}"
        
    