class Cliente:
    __nombre:str
    __apellido:str
    __dni:int 
    __numeroDeCuenta:int
    __saldoAnterior:float 
    
    def __init__(self, xnombre, xapellido, xdni,xnumeroDeCuenta, xsaldoAnterior):
        self.__nombre = xnombre
        self.__apellido = xapellido
        self.__dni = xdni
        self.__numeroDeCuenta = xnumeroDeCuenta
        self.__saldoAnterior = xsaldoAnterior
        
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getNumeroDeCuenta(self):
        return self.__numeroDeCuenta
    def getSaldoAnterior(self):
        return self.__saldoAnterior
    
    def __str__(self):
        return f"Nombre:{self.__nombre} Apellido:{self.__apellido} DNI:{self.__dni} Numero de cuenta:{self.__numeroDeCuenta} Saldo Anterior:{self.__saldoAnterior}"