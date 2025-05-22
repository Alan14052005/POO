from gestorClientes import gestorCliente
from gestorMovimientos import gestorMovimiento

def menu():
    op = input('''
        Menu de opciones:
    a) inciso A
    b) inciso B
    c) Inciso C
----> ''')
    while op != 'z':
        if op == 'a':
            dni= int(input("Ingrese DNI: "))
            gC.incisoA(dni, gM)
        elif op == 'b':
            numTarjeta = int(input("Ingrese Numero de tarjeta: "))
            gC.incisoB(numTarjeta, gM)
        elif op == 'c':
            gM.ordenar()
        else:
            print("opcion no encontrada")
        menu()


if __name__=="__main__":
    gM = gestorMovimiento()
    gC = gestorCliente()
    gM.cargarMovimiento()
    gC.cargaCliente()
    menu()