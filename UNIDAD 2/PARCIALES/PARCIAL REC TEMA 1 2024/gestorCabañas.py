import csv 
import numpy as np
from claseCabañas import Cabaña

class gestorCabaña:
    __incremento: int 
    __cantidad: int 
    __dimension : int 
    __listaCabaña: np.ndarray
    
    def __init__(self):
        self.__incremento = 10
        self.__cantidad = 0 
        self.__dimension = 10
        self.__listaCabaña = np.empty(self.__dimension, dtype= Cabaña) 
        
    def cargarCabaña(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL REC TEMA 1 2024\Cabañas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarCabaña(Cabaña(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]),int(fila[4])))
        archivo.close()    
    
    def agregarCabaña(self, unaCabaña):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaCabaña.resize(self.__dimension)
        self.__listaCabaña[self.__cantidad] = unaCabaña
        self.__cantidad += 1
        
    def incisoa(self, cant, gR):
        for i in range(self.__cantidad):
            bandera = gR.verificarReserva(self.__listaCabaña[i].getNumero())
            if self.__listaCabaña[i] >= cant and not bandera:
                print(self.__listaCabaña[i].getNumero())
    
    def buscarImporte(self, numcabaña):
        encontrado = False
        i = 0 
        importe = None
        while i < self.__cantidad and not encontrado:
            if self.__listaCabaña[i].getNumero() == numcabaña:
                encontrado = True
                importe = self.__listaCabaña[i].getImportDia()
            else:
                i +=1
        return importe  
        
            