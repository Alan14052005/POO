import csv 
from clasePacientes import Paciente

class gestorPaciente:
    __listaPaciente: list
    
    def __init__(self):
        self.__listaPaciente = []
        
    def getLista(self):
        return self.__listaPaciente
    
#0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0  
 
    def agregarPaciente(self, unPaciente):
        self.__listaPaciente.append(unPaciente)

    def cargaPaciente(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\EJERCICIO 6\pacientes.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarPaciente(Paciente(int(fila[0]), fila[1], fila[2]))
        archivo.close()

#0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0  
    
    def buscarNombre(self, dni):
        for paciente in self.__listaPaciente:
            if paciente.getDni() == dni:
                NyA = paciente.getNombre()
        return NyA
    
    def listarSinAtencion(self, gA):
        for paciente in self.__listaPaciente:
            if gA.buscarDni(paciente.getDni())== False:
                print(f"El paciente {paciente.getNombre()} no tuvo atenciones.")
    
    def ordenarPaciente(self):
        self.__listaPaciente.sort()
        for paciente in self.__listaPaciente:
            print(paciente) 