import csv
import numpy as np
from claseCanchas import Cancha

class gestorCancha:
    __incremento: int 
    __cantidad: int 
    __dimension : int 
    __listaCancha: np.ndarray
    
    def __init__(self):
        self.__incremento = 6
        self.__cantidad = 0 
        self.__dimension = 6
        self.__listaCancha = np.empty(self.__dimension, dtype= Cancha) 
        
    def cargarCancha(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL REC TEMA 2 2024\Canchas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarCancha(Cancha(fila[0], fila[1], int(fila[2])))
        archivo.close()    
    
    def agregarCancha(self, unaCancha):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaCancha.resize(self.__dimension)
        self.__listaCancha[self.__cantidad] = unaCancha
        self.__cantidad += 1
        
    def impxhora(self, id):
        i = 0 
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__listaCancha[i].getId() == id:
                encontrado = True
                imporxhora = self.__listaCancha[i].getImporte()
            else:
                i += 1 
        return imporxhora

