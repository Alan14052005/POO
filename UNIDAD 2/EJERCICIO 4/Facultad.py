class facultad:
    __codigoFacu: int 
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    
    def __init__(self, codigoFacu, nombre, direccion, localidad, telefono):
        self.__codigoFacu = codigoFacu
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
    
    def __str__(self):
        return "ID: {} - Nombre:{} - Direccion:{} - Localidad:{} - Telefono:{}". format(self.__codigoFacu, self.__nombre, self.__direccion, self.__localidad, self.__telefono)
    
    
    def getCodigoFacu(self):
        return self.__codigoFacu   
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getLocalidad(self):
        return self.__localidad
    def getTelefono(self):
        return self.__telefono
        