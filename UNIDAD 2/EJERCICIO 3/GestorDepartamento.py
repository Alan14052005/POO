import csv 
from Departamento import depa
class GestorDepa:
    __depto: list
    
    def __init__(self):
        self.__depto = []
        
    def agregarDepto (self, depto):
        self.__depto.append(depto)
        
    def cargarDepto(self):
        archivo = open("Departamentos.csv")
        reader = csv.reader(archivo,delimiter = ';')
        bandera = True
        for fila in reader:  #permite saltar la primer linea del csv 
            if bandera: 
                bandera= not bandera 
            else: 
                unDepto = depa(int(fila[0]), fila[1])
                self.agregarDepto(unDepto)
        archivo.close()
      
    def agregarDatos(self, nrodepa): 
        for dep in self.__depto:
            if i.getNumero() == nrodepa:
                print(i.getNumero)
            else:
                print("no encontrado")    
                 