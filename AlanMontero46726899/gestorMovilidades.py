#Montero Alan 46726899
from claseMovilidades import Movilidad
import csv
import numpy as np

class gestorMovilidad:
    __incremento: int 
    __cantidad: int 
    __dimension : int 
    __listaMovilidad: np.ndarray
    
    def __init__(self):
        self.__incremento = 4
        self.__cantidad = 0 
        self.__dimension = 4
        self.__listaMovilidad = np.empty(self.__dimension, dtype= Movilidad) 
        
    def cargarMovilidad(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\AlanMontero46726899\movilidades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarMovilidad(Movilidad(fila[0], fila[1], int(fila[2]), float(fila[3]), fila[4], fila[5]))
        archivo.close()    
    
    def agregarMovilidad(self, unaMovilidad):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaMovilidad.resize(self.__dimension)
        self.__listaMovilidad[self.__cantidad] = unaMovilidad
        self.__cantidad += 1
        
#-0-0-0-0-0-0--0

    def incisoA(self, patente, gG):
        i = 0 
        encontrado = False
        gastos = 0 
        longitud = self.__cantidad
        while i < longitud and not encontrado:
            if self.__listaMovilidad[i].getPatente() == patente:
                encontrado = True 
                gastos = gG.calcular(self.__listaMovilidad[i].getPatente())
            else:
                i +=1 
                
        if encontrado == True:
            print(f"patente{self.__listaMovilidad[i].getPatente()}           tipo:{self.__listaMovilidad[i].getTipo()}       cap de carga:{self.__listaMovilidad[i].getCapDeCarga()} ")
            print(f"importe mensual de patente:{self.__listaMovilidad[i].getImporteMxP()}       marca{self.__listaMovilidad[i].getMarca()}         modelo:{self.__listaMovilidad[i].getModelo()}")
            print("Gastos")
            print("fechas:                      importe                        descripcion")
            gG.mostrarDatos(patente)
            print(f"Total de gastos:{gastos}             patente:{patente}")
        else: 
            print("Mensaje de error")
            
    def otrosDatos(self, patente):
        longitud = self.__cantidad
        for i in range(longitud):
           if self.__listaMovilidad[i].getPatente() == patente: 
                print(f"patente:{patente}   marca{self.__listaMovilidad[i].getMarca()}     modelo:{self.__listaMovilidad[i].getModelo()}")