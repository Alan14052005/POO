class Caja_de_ahorro:
    _nroCuenta: int
    _cuil: str 
    _apellido:str
    _nombre:str
    _saldo: float

    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self._nroCuenta = nroCuenta
        self._cuil = cuil
        self._apellido = apellido
        self._nombre = nombre
        self._saldo = saldo 

    def mostrar_info(self):
        return f"\nnroCuenta:{self._nroCuenta}\ncuil:{self._cuil}, \napellido:{self._apellido}\nnombre:{self._nombre}\nsaldo:{self._saldo} "

    def depositar(self, deposito:float):
        if deposito >= 0:
            self._saldo = float(self._saldo)
            self._saldo += deposito
            print (f"SU SALDO SE ACTUALIZO A: {self._saldo}")
        else:
            print("saldos negativos no se permiten")     

    def extraer(self, extraccion:float):
        self._saldo = float(self._saldo)
        if self._saldo > extraccion:
            self._saldo -= extraccion
            print (f"SU SALDO SE ACTUALIZO A: {self._saldo}")
        else:
            print("no tienes suficiente saldo")
            
             # Lista para nombres ya que NumPy esta pensado para datos numericos especialmente, aunque es posible no es lo que se recomienda
            
            
            
            
