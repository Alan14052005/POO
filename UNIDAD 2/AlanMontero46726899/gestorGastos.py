#Montero Alan 46726899
import csv
from claseGastos import Gasto

class gestorGasto:
    __listaGasto: list
    
    def __init__(self):
        self.__listaGasto = []
        
    def getLista(self):
        return self.__listaGasto    
 
    def agregarGasto(self, unGasto):
        self.__listaGasto.append(unGasto)

    def cargaGasto(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\AlanMontero46726899\gastosAbril2025.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarGasto(Gasto(fila[0], fila[1],float(fila[2]), fila[3]))
        archivo.close()
    
    def calcular(self, patente):
        acum = 0 
        longitud = len(self.__listaGasto)
        for i in range(longitud):
            if self.__listaGasto[i].getPatente() == patente:
                acum += self.__listaGasto[i].getImpDeGasto()
        return acum
    
    def mostrarDatos(self, patente):
        longitud = len(self.__listaGasto)
        for i in range(longitud):
            if self.__listaGasto[i].getPatente()==patente:
                print (f"{self.__listaGasto[i].getFecha()}            {self.__listaGasto[i].getImpDeGasto()}                {self.__listaGasto[i].getDescripcion()}")
                
    def gastos(self, fecha):
        i = 0 
        encontrado = False
        longitud = len(self.__listaGasto)
        while i < longitud and not encontrado:
            if self.__listaGasto[i].getFecha() == fecha:
                encontrado = True
                print (f"Gastos producidos ese dia:{self.__listaGasto[i].getDescripcion()}         total general a pagar:{self.__listaGasto[i].getImpDeGasto()}")
            else: 
                i += 1
    
    def ordenar(self):  
        self.__listaGasto.sort() 
        longitud = len(self.__listaGasto)
        for i in range(longitud):
            print(self.__listaGasto[i])
    
    def mostrarDato(self, fecha, gM):
        i = 0 
        encontrada = False
        acum = 0
        longitud = len(self.__listaGasto)
        while i < longitud and not encontrada:
                if self.__listaGasto[i].getFecha() == fecha:
                    encontrada = True
                    patente = self.__listaGasto[i].getPatente()
                    gM.otrosDatos(patente)
                else:
                    i += 1 
                for j in range(longitud):
                    if self.__listaGasto[j].getPatente() == patente:
                        acum += self.__listaGasto[j].getImpDeGasto()
                print(f"Total a pagar: {acum}")