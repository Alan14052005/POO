from gestorClientes import gestorCliente
from gestorMovimientos import gestorMovimiento


def menu():
    op = input('''
        Menu de opciones:
    a) LISTADO
    b) MOVIMIENTOS ABRIL
    c) ORDENAR MOVIMIENTOS POR NUMERO DE CUENTA 
----> ''')
    while op != 'z':
        if op == 'a':
            dni= int(input("Ingrese el DNI: "))
            gC.actualizarSaldo(dni, gM)
        elif op == 'b':
            DNI = input("Ingrese DNI: ")
            gC.informar(DNI, gM)
        elif op == 'c':
            gM.ordenar()
        else:
            print("opcion no encontrada")
        menu()





if __name__=='__main__':
    gM=gestorMovimiento()
    gC=gestorCliente()
    gM.cargarMovimiento()
    gC.cargaCliente()
    menu()