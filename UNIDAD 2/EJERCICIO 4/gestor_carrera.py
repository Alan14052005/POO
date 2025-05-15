import numpy as np 
import csv
from Carrera import Carrera

class GestorCarrera:
    __cantidad: int
    __dimension: int  
    __incremento: int  
    __ArreCarre: np.array
    
    def __init__(self, dimension = 10 , incremento=1):
        self.__cantidad=0
        self.__dimension = dimension
        self.__ArreCarre = np.empty(dimension,dtype=object)
        
    def agregarCarrera(self, unaCarrera):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__ArreCarre= np.resize(self.__dimension)
            self.__ArreCarre[self.__cantidad]=unaCarrera
            self.__cantidad += 1 
            
    def cargarCarrera(self):
        saltear = False
        with open (r"C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\EJERCICIO 4\Carreras.csv") as archivoCarre:
            reader = csv.reader(archivoCarre, delimiter = ";")
            next(reader)
            for carre in reader:
                    unaCarre = Carrera(int(carre[0]), carre[1], carre[2], carre[3], carre[4], int(carre[5]))
                    self.agregarCarrera(unaCarre)
            archivoCarre.close()

#0000000000000000000000000000000000000000000000 CARGA 0000000000000000000000000000000000000000000000000000000000000000000000000000

    def buscarCarrera(self, nombre):# iniciso 1 
        i = 0 
        aux = -1
        encontrado = False
        print(self.__ArreCarre) 
        while i< self.__cantidad and not encontrado:
            if self.__ArreCarre[i].getNombre()== nombre:
                aux = self.__ArreCarre[i].getCodFacu()
                encontrado = True
            else: 
                i += 1 
        return  aux 

    def cantidad(self,id):#parte del inciso 2 
        cant=0
        for i in range (self.__cantidad):
            if self.__ArreCarre[i].getCodigoFacu()==id:
                cant=cant+1
        return cant


    def listarOrdenado(self, aux):#iniciso 3 
        cant= 0 
        for i in range (self.__cantidad):
            if self.__ArreCarre[i].getCodigoFacu()==aux:
                print("nombre{}, duracion{}".format(self.__ArreCarre.getNombre, self.__ArreCarre[i].getDuracion))
                
    def ordenar (self):# inciso 3
        self.__ArreCarre.sort() #sirve para ordenar una lista (o arreglo) en su lugar
        