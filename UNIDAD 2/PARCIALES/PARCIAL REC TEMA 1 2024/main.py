from gestorCabañas import gestorCabaña
from gestorReservas import gestorReserva

def menu():
    op = input('''
        Menu de opciones:
    a) inciso a
    b) inciso b 

----> ''')
    while op != 'z':
        if op == 'a':
            cant = int(input("Ingrese la cantidad de huespedes: "))
            gC.incisoa(cant, gR)
        elif op == 'b':
            fecha= input("Ingrese la fecha: ")
            gR.incisob(fecha, gC)
        elif op == 'c':
            pass
        else:
            print("opcion no encontrada")
        menu()

if __name__=="__main__":
    gC = gestorCabaña()
    gR = gestorReserva()
    gC.cargarCabaña()
    gR.cargaReserva()
    menu()