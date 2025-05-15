class Cabaña:
    __numero : int
    __cantHabitaciones: int 
    __cantCamaG: int 
    __cantCamC: int 
    __impxdia: float
    
    def __inti__(self, numero, cantHabitaciones, cantCamaG, cantCamC, impxdia):
        self.__numero = numero
        self.__cantHabitaciones = cantHabitaciones
        self.__cantCamaG = cantCamaG
        self.__cantCamC = cantCamC
        self.__impxdia = impxdia
        
    def getNumero(self):
        return self.__numero
    def getCantHabitaciones(self):
        return self.__cantHabitaciones
    def getCantCamaG(self):
        return self.__cantCamaG
    def getcantCamC(self):
        return self.__cantCamC
    def getImpxDia(self):
        return self.__impxdia
    
    def __str__(self):
        return f"Numero:{self.__numero} cantidad de habitaciones:{self.__cantHabitaciones} cantidad de camas grandes{self.__cantCamaG} cantidad de camas chicas{self.__cantCamC} importe por dia{self.__impxdia}"
    
    
    