import csv
import numpy as np
from claseMovimientos import Movimiento

class gestorMovimiento:
    __incremento: int 
    __cantidad: int 
    __dimension : int 
    __listaMovimiento: np.ndarray
    
    def __init__(self):
        self.__incremento = 10
        self.__cantidad = 0 
        self.__dimension = 10
        self.__listaMovimiento = np.empty(self.__dimension, dtype= Movimiento) 
        
    def cargarMovimiento(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL TEMA 1 2024\MovimientosAbril2024.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarMovimiento(Movimiento(int(fila[0]), fila[1], fila[2], fila[3],int(fila[4])))
        archivo.close()    
    
    def agregarMovimiento(self, unMovimiento):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaMovimiento.resize(self.__dimension)
        self.__listaMovimiento[self.__cantidad] = unMovimiento
        self.__cantidad += 1

    def mostrarDatos(self, numTarjeta, saldoAnterior):
        for i in range(self.__cantidad):
            if self.__listaMovimiento[i].getNumTarjeta() == numTarjeta:
                print(f"Fecha:{self.__listaMovimiento[i].getFecha()}      Descripcion:{self.__listaMovimiento[i].getDescripcion()}          Importe:{self.__listaMovimiento[i].getImporte()}         Tipo de Movimiento:{self.__listaMovimiento[i].getTipoMov()}")
                if self.__listaMovimiento[i].getTipoMov() == 'C':
                    saldoAnterior += self.__listaMovimiento[i].getImporte()
                else:
                    saldoAnterior -= self.__listaMovimiento[i].getImporte()
                print(f"saldo Actualizado:{saldoAnterior}")
                
    def buscarMovimientos(self, numTarjeta):
        bandera = False
        i = 0 
        while i < self.__cantidad and not bandera:
            if self.__listaMovimiento[i].getNumTarjeta() == numTarjeta:
                bandera = True
            else:
                i += 1
        return bandera
    
    def ordenar(self):
        self.__listaMovimiento[:self.__cantidad].sort()
        longitud = self.__cantidad
        for i in range(longitud):
            print(self.__listaMovimiento[i])