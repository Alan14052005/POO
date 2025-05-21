from claseGastos import Gasto
import csv 

class gestorGasto:
    __listaGasto: list
    
    def __init__(self):
        self.__listaGasto = []
        
    def getLista(self):
        return self.__listaGasto    
 
    def agregarGasto(self, unGasto):
        self.__listaGasto.append(unGasto)

    def cargaGasto(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\P.O tema 2\gastosAbril2025.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarGasto(Gasto(fila[0], fila[1],int(fila[2]), fila[3]))
        archivo.close()

    def contar(self, patente):
        acum = 0 
        longitud = len(self.__listaGasto)
        for i in range(longitud):
            if self.__listaGasto[i].getPatente()== patente:
                acum += self.__listaGasto[i].getImpGasto()
        return acum
    
    def mostrarDatos(self, patente):
        longitud = len(self.__listaGasto)
        for i in range(longitud):
            if self.__listaGasto[i].getPatente() == patente:
                print (f"{self.__listaGasto[i].getFecha()}      {self.__listaGasto[i].getImpGasto()}      {self.__listaGasto[i].getDescripcion()}")
    
    def inciso2(self, fecha):
        longitud = len(self.__listaGasto)
        for i in range(longitud):
            if self.__listaGasto[i].getFecha() == fecha:
                print (f"{self.__listaGasto[i].getDescripcion()}   importe del gasto:{self.__listaGasto[i].getImpGasto()}")
                
    def ordenar(self):
        self.__listaGasto.sort()
        for gasto in self.__listaGasto:
            print (gasto)
        
        
    def buscarPatente(self, fecha):
        encontrada = False
        i = 0 
        longitud = len(self.__listaGasto)
        while i < longitud and not encontrada:
            if self.__listaGasto[i].getFecha() == fecha:
                encontrada = True
                patente = self.__listaGasto[i].getPatente()
            else:
                i +=1 
        return patente
    
    def totalPagar(self, fecha):
        acum = 0 
        longitud = len(self.__listaGasto)
        encontrado = False
        i = 0
        while i < longitud and not encontrado:
            if fecha == self.__listaGasto[i].getFecha():
                encontrado = True
                patente = self.__listaGasto[i].getPatente()
        for i in range(longitud):
            if patente == self.__listaGasto[i].getPatente():
                acum += self.__listaGasto[i].getImpGasto()

        return acum
                
                  