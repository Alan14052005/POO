class Reserva:
    __numReserva: int 
    __nomPerRes: str
    __numCabaña :int 
    __fechaIniHos: str
    __cantHuesp: int 
    __cantDias: int 
    __impSeña: float
    
    def __init__(self, numReserva, nomPerRes, numCabaña, fechaIniHos, cantHuesp, cantDias, impSeña):
        self.__numReserva = numReserva
        self.__nomPerRes = nomPerRes
        self.__numCabaña = numCabaña
        self.__fechaIniHos = fechaIniHos
        self.__cantHuesp = cantHuesp
        self.__cantDias = cantDias
        self.__impSeña = impSeña
        
    def getNumReserva(self):
        return self.__numReserva
    def getNomPerRes(self):
        return self.__nomPerRes
    def getNumCabaña(self):
        return self.__numCabaña
    def getFechaIniHos(self):
        return self.__fechaIniHos
    def getCantHuesp(self):
        return self.__cantHuesp
    def getCantDias(self):
        return self.__cantDias
    def getImpSeña(self):
        return self.__impSeña
    
    def __str__(self):
        return f"Numero de reserva:{self.__numReserva} Nombre de la persona que reservo:{self.__nomPerRes} Numero de cabaña:{self.__numCabaña} fecha de inicio de hospedaje{self.__fechaIniHos} cantidad de huespedes{self.__cantHuesp} cantidad de dias:{self.__cantDias} importe de la seña:{self.__impSeña}"