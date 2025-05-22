from gestorColectivos import gestorColectivo
from gestorTramos import gestorTramo

def menu():
    op = input('''
        Menu de opciones:
    a) LISTADO CON DATOS 
    b) MOSTRAR GASTO ESTIMADO
    c) LISTAR DATOS DE TRAMOS SUPERIORES A UNA DISTANCIA

----> ''')
    while op != 'z':
        if op == 'a':
            DNI = int(input("Ingrese el DNI a buscar: "))
            gC.buscarPatente(DNI, gT)
        elif op == 'b':
            gT.mostrarDatos()
        elif op == 'c':
            distancia= int(input("Ingrese la distancia: "))
            gT.listar(distancia)
        else:
            print("opcion no encontrada")
        menu()

if __name__=="__main__":
    gC = gestorColectivo()
    gT = gestorTramo()
    gC.cargarColectivo()
    gT.cargaTramo()
    menu()    