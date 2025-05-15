import csv
from claseBecas import Beca

class gestorBeca:
    __listaBeca: list
    
    def __init__(self):
        self.__listaBeca = []
        
    def agregarBeca(self, unaBeca):
        self.__listaBeca.append(unaBeca)

    def cargaBeca(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\EJERCICIO 5\becas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarBeca(Beca(int(fila[0]), fila[1],float(fila[2])))
        archivo.close()   
    
    def informarBene(self, tipobeca, gBene):
        i=0
        bandera = False
        rango = len(self.__listaBeca)
        while i < rango and not bandera:
            if self.__listaBeca[i].getTipo() == tipobeca:
                bandera = True
                cont = gBene.mostrar(self.__listaBeca[i].getId())
            else:
                i += 1 
        print(f"importe total que debe disponer la Secretaría:{self.__listaBeca[i].getImporte()*cont}")
                 