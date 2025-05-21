from gestorGastos import gestorGasto
from gestorMovilidades import gestorMovilidad

def menu():
    op = input('''
        Menu de opciones:
    a) listado
    b) Indicar gastos producidos en una fecha
    c) ordenar
----> ''')
    while op != 'z':
        if op == 'a':
            patente = input("Ingtrese la patente ")
            gM.inciso1(patente, gG)
        elif op == 'b':
            fecha = input("Ingrese la fecha: ")
            gG.inciso2(fecha)
        elif op == 'c':
            gG.ordenar()
            fecha2 = input("Ingrese fecha: ")
            gM.inciso3(fecha2, gG)
        else:
            print("opcion no encontrada")
        menu()





if __name__=="__main__":
    gG = gestorGasto()
    gM = gestorMovilidad()
    gG.cargaGasto()
    gM.cargarMovilidad()
    menu()