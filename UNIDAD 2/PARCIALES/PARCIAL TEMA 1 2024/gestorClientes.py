from claseClientes import Cliente
import csv 

class gestorCliente:
    __listaCliente: list
    
    def __init__(self):
        self.__listaCliente = []
        
    def getLista(self):
        return self.__listaCliente   
 
    def agregarCliente(self, unCliente):
        self.__listaCliente.append(unCliente)

    def cargaCliente(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL TEMA 1 2024\ClientesAbril2024.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarCliente(Cliente(fila[0], fila[1],int(fila[2]),int(fila[3]), int(fila[4])))
        archivo.close()
        
    def incisoA(self, dni, gM):
        bandera = False
        longitud = len(self.__listaCliente)
        i = 0 
        while i < longitud and not bandera:
            if self.__listaCliente[i].getDni() == dni:
                bandera = True
                print(f"Cliente:{self.__listaCliente[i].getNombre()} {self.__listaCliente[i].getApellido()}                  Numero de Tarjeta:{self.__listaCliente[i].getNumTarjeta()}")
                print(f"Saldo Anterior:{self.__listaCliente[i].getSaldoAnterior()}")
                print("Movimientos")
                gM.mostrarDatos(self.__listaCliente[i].getNumTarjeta(), self.__listaCliente[i].getSaldoAnterior())
               
            else:
                i += 1
                
    def incisoB(self, numTarjeta, gM):
        longitud = len(self.__listaCliente)
        i = 0 
        bandera = False
        while i < longitud and not bandera:
            movimientos = gM.buscarMovimientos(numTarjeta)
            if self.__listaCliente[i].getNumTarjeta() == numTarjeta and not movimientos:
                bandera = True
                print (f"Apellido:{self.__listaCliente[i].getApellido()}  Nombre:{self.__listaCliente[i].getNombre()}")
            else:
                i += 1
        