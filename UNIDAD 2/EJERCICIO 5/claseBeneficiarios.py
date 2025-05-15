class Beneficiario:
    __dni: int
    __nombre: str
    __apellido: str
    __carrera: str
    __siglaFacu: str
    __añoCursa: int 
    __promedio: int
    __idBeca: int 
    
    def __init__(self, xdni, xnombre, xapellido, xcarrera, xsiglaFacu, xañoCursa, xpromedio, xidBeca):
        self.__dni = xdni
        self.__nombre = xnombre
        self.__apellido = xapellido
        self.__carrera = xcarrera
        self.__siglaFacu = xsiglaFacu
        self.__añoCursa = xañoCursa
        self.__promedio = xpromedio
        self.__idBeca = xidBeca
        
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCarrera(self):
        return self.__carrera
    def getSiglaFacu(self):
        return self.__siglaFacu
    def getAñoCursa(self):
        return self.__añoCursa
    def getPromedio(self):
        return self.__promedio
    def getIdBeca(self):
        return self.__idBeca
    
    def __str__(self):
        return f"SIGLOFACU:{self.__siglaFacu} DNI:{self.__dni} NOMBRE:{self.__nombre}APELLIDO:{self.__apellido} CARRERA:{self.__carrera} ANOCURSA:{self.__añoCursa} PORMEDIO:{self.__promedio}{self.__idBeca}"
    
    def __lt__(self, otro):
        return self.getSiglaFacu() > otro.getSiglaFacu()
        