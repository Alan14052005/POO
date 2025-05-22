import numpy as np 
from claseColectivo import Colectivo
import csv 

class gestorColectivo:
    __incremento: int 
    __cantidad: int 
    __dimension : int 
    __listaColec: np.ndarray

    def __init__(self):
        self.__incremento = 4
        self.__cantidad = 0 
        self.__dimension = 4
        self.__listaColec = np.empty(self.__dimension, dtype= Colectivo)    
    
    def cargarColectivo(self):
        i=0 
        cantidad_a_cargar = int(input("Ingrese la cantidad de colectivos: "))
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PRACTICO 1 TEMA 1\colectivos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            if i < cantidad_a_cargar:
                self.agregarColectivo(Colectivo(fila[0], fila[1], int(fila[2]),int(fila[3]),int(fila[4])))
                i += 1 
        archivo.close()    
    
    def agregarColectivo(self, unColectivo):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaColec.resize(self.__dimension)
        self.__listaColec[self.__cantidad] = unColectivo
        self.__cantidad += 1     
        
    def mostrar(self):
        longitud = self.__cantidad
        for i in range(longitud):
            print(self.__listaColec[i])    
    
    def buscarPatente(self, DNI, gT):
        i = 0 
        bandera = False
        while i < self.__cantidad and bandera==False:
            if self.__listaColec[i].getDniDelC() == DNI:
                bandera = True
                patente =  self.__listaColec[i].getPatente()
                gT.listado(patente)
            else:
                i += 1 
 
            

               