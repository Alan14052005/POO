from claseMovimiento import Movimiento
import csv
import numpy as np

class gestorMovimiento:
    __incremento: int 
    __cantidad: int 
    __dimension : int 
    __listaAten: np.ndarray

    def __init__(self):
        self.__incremento = 8 
        self.__cantidad = 0 
        self.__dimension = 8
        self.__listaAten = np.empty(self.__dimension, dtype= Movimiento) 
        
    def cargarMovimiento(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL\MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarMovimiento(Movimiento(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4])))
        archivo.close()    
    
    def agregarMovimiento(self, unMovimiento):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaAten.resize(self.__dimension)
        self.__listaAten[self.__cantidad] = unMovimiento
        self.__cantidad += 1   
    
    def calcular(self, numCuenta):
        acum = 0 
        longitud = self.__cantidad
        for i in range(longitud) :
            if self.__listaAten[i].getNumeroDeCuenta() == numCuenta:
                if self.__listaAten[i].getTipoDeMovimiento() == 'C':
                    acum += self.__listaAten[i].getImporte()
                else:
                    acum -= self.__listaAten[i].getImporte() 
        return acum
    
    def mostrarDatos(self, numCuenta):
        longitud = self.__cantidad
        for i in range(longitud):
            if self.__listaAten[i].getNumeroDeCuenta() == numCuenta:       
                print(f"{self.__listaAten[i].getFecha()}                         {self.__listaAten[i].getDescripcion()}                      {self.__listaAten[i].getImporte()}                        {self.__listaAten[i].getTipoDeMovimiento()}")
            
    def ordenar(self):
        lista_valida = list(self.__listaAten[:self.__cantidad])  
        lista_valida.sort() 
        for movimiento in lista_valida:
            print(movimiento)
    
    def abril(self, numCuenta):
        longitud = self.__cantidad
        bandera = False
        for i in range(longitud):
            if self.__listaAten[i].getNumeroDeCuenta() == numCuenta:
                bandera = True
        return bandera
            