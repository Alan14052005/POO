from claseTramos import Tramo
import csv 

class gestorTramo:
    __listaTramos: list
    
    def __init__(self):
        self.__listaTramos = []
        
    def getListaTramo(self):
        return self.__listaTramos
    
    def agregarTramo(self, unTramo):
        self.__listaTramos.append(unTramo)

    def cargaTramo(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PRACTICO 1 TEMA 1\tramos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarTramo(Tramo(fila[0], fila[1], int(fila[2]),fila[3]))
        archivo.close()
    
    def listado (self, patente):
        acum = 0 
        longitud = len(self.__listaTramos)
        for i in range(longitud):
            if self.__listaTramos[i].getPatenteC() == patente:
                acum += self.__listaTramos[i].getDistancia()
                print(f"Ciudad Origen:{self.__listaTramos[i].getCiudadOri()} Ciudad Origen:{self.__listaTramos[i].getCiudadDest()} Kilometros recorridos:{self.__listaTramos[i].getDistancia()}")
        print(f" cantidad total de km recorridos:{acum}")

    def mostrarDatos(self):
        patentes_procesadas = set()
        longitud = len(self.__listaTramos)
        for i in range(longitud):
            patente = self.__listaTramos[i].getPatenteC()
            if patente not in patentes_procesadas:
                acum = 0 
                for j in range(longitud):
                    if self.__listaTramos[j].getPatenteC() == patente:
                        acum += self.__listaTramos[j].getDistancia()
                print (f"Colectivo:{self.__listaTramos[i].getPatenteC()} kilometros recorridos:{acum} gasto estimado:{acum*35/100}")
                patentes_procesadas.add(patente)      
            
    def listar(self, distancia):
        for tramo in self.__listaTramos:
            if tramo > distancia:
                print(f"Ciudad Origen: {tramo.getCiudadOri()}  Ciudad Destino: {tramo.getCiudadDest()}  Patente: {tramo.getPatenteC()}")
                    