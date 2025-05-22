import csv 
from claseReservas import Reserva

class gestorReserva:
    __listaReserva: list
    
    def __init__(self):
        self.__listaReserva = []
        
    def getLista(self):
        return self.__listaReserva   
 
    def agregarReserva(self, unaReserva):
        self.__listaReserva.append(unaReserva)

    def cargaReserva(self):
        archivo = open(r'C:\Users\alanm\OneDrive\Desktop\FACU\POO\PRACTICAS\UNIDAD 2\PARCIALES\PARCIAL REC TEMA 1 2024\Reservas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
                self.agregarReserva(Reserva(int(fila[0]), fila[1],int(fila[2]), fila[3], int(fila[4]), int(fila[5]), int(fila[6])))
        archivo.close()
        
    def verificarReserva(self, numero):
        encontrado = False
        i = 0 
        longitud = len(self.__listaReserva)
        while i < longitud and not encontrado:
            if self.__listaReserva[i].getNumCabaña() == numero:
                encontrado = True 
            else:
                i+=1
        return encontrado
    
    def incisob(self, fecha, gC):
        longitud = len(self.__listaReserva)
        print(f"\nReservas para la fecha{fecha}")
        for i in range(longitud):
            if self.__listaReserva[i].getFechaIni() == fecha:
                importediario = gC.buscarImporte(self.__listaReserva[i].getNumCabaña())
                impacobrar= self.__listaReserva[i].getCantDias() * importediario - self.__listaReserva[i].getImporte()
                print("\nN° de cabaña    importe diario     cantidad de dias         seña       importe a cobrar")
                print(f"   {self.__listaReserva[i].getNumCabaña()}                {importediario}                 {self.__listaReserva[i].getCantDias()}                {self.__listaReserva[i].getImporte()}            {impacobrar}           ")