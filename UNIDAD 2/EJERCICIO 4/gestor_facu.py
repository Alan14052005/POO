import numpy as np
import csv
from Facultad import facultad

class gestorFacu:
    __cantidad: int
    __dimension: int 
    __incremento: int 
    __ArreFacu: np.array
    
    def __init__(self, dimension = 10 , incremento= 1 ):
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento
        self.__ArreFacu = np.empty(dimension, dtype= facultad)
    
    def agregarFacu(self, unaFacu):
        if  self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__ArreFacu.resize(self.__dimension)
        self.__ArreFacu[self.__cantidad]=unaFacu
        self.__cantidad += 1 
    
    def cargarFacu(self):
        with open (r"C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\EJERCICIO 4\Facultades.csv") as archivoFacu:
            reader = csv.reader(archivoFacu, delimiter = ";")
            next(reader)
            for facu in reader:
                    unaFacultad = facultad(int(facu[0]), facu[1], facu[2], facu[3], facu[4])
                    self.agregarFacu(unaFacultad)
        archivoFacu.close()

    def mostrarFacultades(self):
        for i in range(self.__cantidad):
            print(self.__ArreFacu[i])
#00000000000000000000000000000000000000000 CARGA 00000000000000000000000000000000000000000000000000000000000000000000000000000000

    def mostrarFacu(self, gc): #inciso 2 
        for i in range(self.__cantidad):
            print("En esta facultad hay{}".format(gc.cantidad(self.__ArreFacu[i].getCodigoFacu())))
    
    def mostrarNombreCarre(self, id): #inciso 1 
        i = 0 
        encontrado = False
        while i< self.__cantidad and not encontrado: 
            if int(self.__ArreFacu[i].getCodigoFacu) == int(id):
                aux = self.__ArreFacu[i].getNombre
                encontrado= True
            else:
                i+=1
        return aux 
    
    def buscarFacultad(self, nombre ):# inciso 3 
        i = 0 
        aux = -1
        encontrado = False 
        while i< self.__cantidad and not encontrado: 
            if self.__ArreFacu[i].getNombre == nombre:
                aux = int(self.__ArreFacu[i].getCodigoFacu())
                encotnrado = True
            else:
                i += 1 
        return aux 