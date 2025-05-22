from gestorAlquileres import gestorAlquiler
from gestorCanchas import gestorCancha

def menu():
    op = input('''
        Menu de opciones:
    a) listado
    b) Iinciso b 

----> ''')
    while op != 'z':
        if op == 'a':
            gA.ordenar(gC)
        elif op == 'b':
            id = input("Ingrese el identificador de la cancha: ")
            gA.incisob(id)
        elif op == 'c':
           pass
        else:
            print("opcion no encontrada")
        menu()





if __name__=="__main__":
    gC = gestorCancha()
    gA = gestorAlquiler()
    gC.cargarCancha()
    gA.cargaAlquiler()
    menu()