from claseMovilidadades import Movilidad
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
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\P.O tema 2\movilidades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarMovilidad(Movilidad(fila[0], fila[1], int(fila[2]), int(fila[3]), fila[4], fila[5]))
        archivo.close()    
    
    def agregarMovilidad(self, unaMovilidad):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaMovilidad.resize(self.__dimension)
        self.__listaMovilidad[self.__cantidad] = unaMovilidad
        self.__cantidad += 1
    
    def inciso1(self, patente, gG):
        encontrado = False
        i = 0 
        while i < self.__cantidad and not encontrado:
            if self.__listaMovilidad[i].getPatente() == patente:
                encontrado = True
                acum = gG.contar(patente)
                print (acum)
            else: 
                i += 1
        if encontrado:
            print(f"Patente:{patente}        tipo:{self.__listaMovilidad[i].getTipo()}             capacidad de carga:{self.__listaMovilidad[i].getCapCarga()}")
            print(f"importe mensual de la patente:{self.__listaMovilidad[i].getImpMensual()}  marca:{self.__listaMovilidad[i].getMarca()}             modelo:{self.__listaMovilidad[i].getModelo()}")
            print("gastos")
            print("Fecha          importe         descripcion")
            gG.mostrarDatos(patente)
            print(f"total de gastos de la patente:{patente} es {acum}")
        else:
            print("Patente no encontrada")
    
    def inciso3(self, fecha, gG):
        patente = gG.buscarPatente(fecha)
        acum = gG.totalPagar(fecha)
        for i in range(self.__cantidad):
            if patente == self.__listaMovilidad[i].getPatente():
                print(f"patente:{self.__listaMovilidad[i].getPatente()} marca:{self.__listaMovilidad[i].getMarca()} modelo:{self.__listaMovilidad[i].getModelo()}")
                print (acum)