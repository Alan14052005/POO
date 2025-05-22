import csv
from claseCliente import Cliente

class gestorCliente:
    __listaCliente: list
      
    def __init__(self):
        self.__listaCliente = []
        
    def getLista(self):
        return self.__listaCliente
    
     
    def agregarCliente(self, unCliente):
        self.__listaCliente.append(unCliente)

    def cargaCliente(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL\ClientesFarmaCiudad.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarCliente(Cliente(fila[0], fila[1], int(fila[2]),int(fila[3]),int(fila[4])))
        archivo.close()

    def actualizarSaldo(self, dni, gM):
        i = 0 
        encontrado = False
        cuenta = 0
        longitud = len(self.__listaCliente)
        while i < longitud and not encontrado:
            if self.__listaCliente[i].getDni()== dni:
                encontrado = True
                cuenta = gM.calcular(self.__listaCliente[i].getNumeroDeCuenta()) + self.__listaCliente[i].getSaldoAnterior()
            else:
                i +=1
        if encontrado:
            print(f"Cliente:{self.__listaCliente[i].getApellido()} {self.__listaCliente[i].getNombre()}          numero de cuenta:{self.__listaCliente[i].getNumeroDeCuenta()} ")
            print (f"Saldo Anteriro:{self.__listaCliente[i].getSaldoAnterior()}")      
            print("Movimientos")
            print("Fecha                       descripcion                          importe                       Tipo de Movimiento")
            gM.mostrarDatos(self.__listaCliente[i].getNumeroDeCuenta())
            print(f"saldo actualizado: {cuenta}")
        else:
            print("DNI no encontrado")
            
    def informar(self, dni, gM):
        i = 0 
        encontrado = False
        longitud = len(self.__listaCliente)
        while i < longitud and not encontrado:
            bandera = gM.abril(self.__listaCliente[i].getNumeroDeCuenta)
            if self.__listaCliente[i].getDni() == dni and not bandera:
                print(f"Nombre:{self.__listaCliente[i].getNombre()} Apellido:{self.__listaCliente[i].getApellido()}")
                encontrado = True 
            else:
                i+=1