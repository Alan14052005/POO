class Tarjetasube:
    __saldo: float
    __numero: int 

    def __init__(self, sld, nro):
        self.__saldo = sld
        self.__numero = nro

    def consultar_Saldo(self):
        return self.__saldo 
    
    def getNumero (self):
        return self.__numero
    
    def __str__(self):
        return f"La tarjeta número {self.__numero} tiene ${self.__saldo}"

    def cargarSaldo(self,imp):
        if imp > 0:
            self.__saldo+=imp
            
    def pagar_pasaje(self, imp):
        aux=-1
        if imp <= self.__saldo:
            self.__saldo -= imp
            aux=1
        return aux


