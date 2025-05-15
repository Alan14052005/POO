from claseAtenciones import Atencion
import csv 
import numpy as np

class gestorAtencion:
    __incremento: int 
    __cantidad: int 
    __dimension : int 
    __listaAten: np.ndarray
    
    def __init__(self):
        self.__incremento = 8 #iDefine cuánto va a crecer el arreglo si se queda sin espacio,,,,,,opcional ya que sabemos el tamaño del arreglo osea q podria ser 49
        self.__cantidad = 0 #Lleva la cuenta de cuántas atenciones están realmente cargadas SIEMPRE 0
        self.__dimension = 8 #Es el tamaño actual del arreglo (la cantidad de espacios disponibles) MULTIPLO DEL CSV
        self.__listaAten = np.empty(self.__dimension, dtype= Atencion) 
        
    def cargarAtencion(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\EJERCICIO 6\atenciones.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarAtencion(Atencion(int(fila[0]), fila[1], float(fila[2])))
        archivo.close()    
    
    def agregarAtencion(self, unaAtencion):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listaAten.resize(self.__dimension)
        self.__listaAten[self.__cantidad] = unaAtencion
        self.__cantidad += 1
#0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

#para recorrer un numpy se utiliza el self.__canitdad q es el tamaño del arreglo /EJ/ for i in range(self.__cantidad)
# para recorrer una lista se utiliza self.__lista /EJ/ for paciente in self.__listaPaciente

    def buscarFecha(self, fecha):
        cont = 0 
        cant = 0
        for i in range(self.__cantidad):
            if self.__listaAten[i].getFechaAte()==fecha:
                cont += self.__listaAten[i].getImporte()
                cant += 1
        print(f"Hubieron {cant} atenciones. Importe total requerido: ${cont}")
        
    def contarAtenciones(self, dni):
        cont = 0 
        for i in range(self.__cantidad):
            if self.__listaAten[i].getDni() == dni:
                cont += 1
        return cont 
    
    def buscarDni(self, xdni):
        encontrado = False
        i=0
        while i < self.__cantidad and encontrado == False:
            if xdni == self.__listaAten[i].getDni():
                encontrado = True
            else:
                i +=1
        return encontrado