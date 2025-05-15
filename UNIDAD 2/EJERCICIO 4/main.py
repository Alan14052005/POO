from gestor_carrera import GestorCarrera
from gestor_facu import gestorFacu

def opciones():
    return """\n---MENU DE OPCIONES---
1. insiso A
2. insiso B
3. insiso C
4. insiso D
"""

def menu():
    entrar=True
    while entrar:
        eleccion=int(input(opciones()))
        match(eleccion):
            case 1:
                nombre = input("Ingrese el Nombre de la Carrera que quiere buscar")
                id = gc.buscarCarrera(nombre)
                if id!= -1:
                    nomFacu=gf.mostrarNombreCarre(id)
                    print (f"El nombre de la facultad de la carrera ingresada es: {nomFacu}")  
                else:
                    print("No encontrada") 
            case 2:      
                gf.mostrarFacu(gc)

            case 3:
                Facu= input("Ingrese el nombre de la facultad")
                aux = gf.buscarFacultad(Facu)#se consigue el nombre de la facu y se guarda en aux
                if aux != -1:
                    gc.listarOrdenado(aux)# se ordena la lista 
                else:
                    print("\nNo se encontro")                       
            case _:
                print("opcion no valida")             
                
if __name__ =='__main__':
  gf= gestorFacu() #crea instancias de objetos y las asigna a gf y gc
  gc= GestorCarrera() # //
  gf.cargarFacu()# carga los datos 
  gc.cargarCarrera()# //
 # gc.ordenar() #sirve para ordenar una lista (o arreglo) en su lugar
  menu()