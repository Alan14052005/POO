class Reserva:
    __numReserva: int 
    __nombreReserva: str
    __numCabaña: int 
    __fechaIni: str
    __cantHuespedes:int 
    __cantDias: int 
    __importe: int
    
    def __init__(self, numReserva, nombreReserva, numCabaña, fechaIni, cantHuespedes, cantDias, importe):
        self.__numReserva = numReserva
        self.__nombreReserva = nombreReserva
        self.__numCabaña = numCabaña
        self.__fechaIni = fechaIni
        self.__cantHuespedes = cantHuespedes
        self.__cantDias = cantDias
        self.__importe = importe
        
    def getNumReserva(self):
        return self.__numReserva
    def getNombreReserva(self):
        return self.__nombreReserva
    def getNumCabaña(self):
        return self.__numCabaña
    def getFechaIni(self):
        return self.__fechaIni
    def getCantHuespedes(self):
        return self.__cantHuespedes
    def getCantDias(self):
        return self.__cantDias
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"Numero de reserva:{self.__numReserva} Nombre de la persona que reservo:{self.__nombreReserva}  numero de cabaña:{self.__numCabaña}  fecha de inicio:{self.__fechaIni} cantidad de huespedes:{self.__cantHuespedes}  cantidad de dias:{self.__cantDias}  importe de la seña:{self.__importe}"