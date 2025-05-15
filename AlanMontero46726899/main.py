#Montero Alan 46726899
from gestorMovilidades import gestorMovilidad
from gestorGastos import gestorGasto



def menu():
    op = input('''
        Menu de opciones:
    a) listado
    b) Indicar gastos producidos en una fecha
    c) ordenar
----> ''')
    while op != 'z':
        if op == 'a':
            patente=input("Ingrese patente")
            gM.incisoA(patente, gG)
        elif op == 'b':
            fecha = input("Ingrese la fecha: ")
            gG.gastos(fecha)
        elif op == 'c':
            gG.ordenar()
            fecha2 = input("Ingrese la fecha: ")
            gG.mostrarDato(fecha2, gM)

        else:
            print("opcion no encontrada")
        menu()



if __name__=='__main__':
    gM = gestorMovilidad()
    gG = gestorGasto()
    gM.cargarMovilidad()
    gG.cargaGasto()
    menu()