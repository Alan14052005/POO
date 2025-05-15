import csv 
from claseBeneficiarios import Beneficiario

class gestorbeneficiario:
    listaBene: list
    
    def __init__(self):
        self.__listaBene = []
        
    def getLista(self):
        return self.__listaBene
    
    def agregarBeneficiario(self, unBeneficiario):
        self.__listaBene.append(unBeneficiario)

    def cargaBeneficiario(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\EJERCICIO 5\beneficiarios.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarBeneficiario(Beneficiario(int(fila[0]), fila[1], fila[2], fila[3], fila[4], int(fila[5]),int(fila[6]),int(fila[7])))
        archivo.close()

    def mostrar(self, id):
        cont = 0 
        longitud = len(self.__listaBene)
        for i in range(longitud):
            if self.__listaBene[i].getIdBeca() == id:
                cont += 1
                
                print (f"Nombre:{self.__listaBene[i].getNombre()} apellido:{self.__listaBene[i].getApellido()}")
        return cont 
    
    def informarMasDeUnaBeca(self, dni):
        cont = 0
        longitud = len(self.__listaBene)
        for i in range(longitud):
            if self.__listaBene[i].getDni() == dni:
                cont += 1
                if cont > 1:
                    print(f"El beneficiario {self.__listaBene[i].getNombre()} {self.__listaBene[i].getApellido()} tiene mas de una beca")        
                
    def ordenarBeneficiario(self):
        self.__listaBene.sort()
        for Beneficiario in self.__listaBene:
            print(Beneficiario)
            
    def noposeenbeca(self):
        longitud = len(self.__listaBene)
        for i in range(longitud):
            if self.__listaBene[i].getPromedio()>=8 and self.__listaBene[i].getIdBeca != 4: 
               print(f"Nombre:{self.__listaBene[i].getNombre()} Apellido:{self.__listaBene[i].getApellido()} Promedio:{self.__listaBene[i].getPromedio()}") 
            else:
                i += 1
                