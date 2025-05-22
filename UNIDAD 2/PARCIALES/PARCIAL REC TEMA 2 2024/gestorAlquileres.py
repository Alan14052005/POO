import csv 
from claseAlquileres import Alquiler

class gestorAlquiler:
    __listaAlquiler: list
    
    def __init__(self):
        self.__listaAlquiler = []
        
    def getLista(self):
        return self.__listaAlquiler    
 
    def agregarAlquiler(self, unAlquiler):
        self.__listaAlquiler.append(unAlquiler)

    def cargaAlquiler(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL REC TEMA 2 2024\Alquiler.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarAlquiler(Alquiler(fila[0], fila[1],fila[2], int(fila[3]), int(fila[4])))
        archivo.close()

    def ordenar(self, gC):
        self.__listaAlquiler.sort()
        longitud = len(self.__listaAlquiler)
        for i in range(longitud):
            duraAlq = self.__listaAlquiler[i].getDuraAlq()/60
            importeporhora = gC.impxhora(self.__listaAlquiler[i].getId())
            print("hora     id cancha     duracion alquiler     importe por hora      importe alquiler")
            print(f"{self.__listaAlquiler[i].getHora()}          {self.__listaAlquiler[i].getId()}           {duraAlq}                            {importeporhora}               {importeporhora*duraAlq}")
            
    def incisob(self, id):
        acum = 0 
        longitud = len(self.__listaAlquiler)
        for i in range(longitud):
            if self.__listaAlquiler[i].getId()==id:
                acum += self.__listaAlquiler[i].getDuraAlq()
        print(f"el total de minutos es:{acum}")