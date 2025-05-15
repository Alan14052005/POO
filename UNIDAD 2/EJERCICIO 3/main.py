from GestorDepartamento import GestorDepa
def opciones():
    return """\n---MENU DE OPCIONES---
1. Dado un numero de mes, mostrar para cada uno de los Departamentosnombre 
del departamento y el total de accidentes ocurridos en el mes dado. 
2. Dado un mes, mostrar nombre de departamento y cantidad de accidentes, para 
el departamento que tuvo la mayor cantidad de accidentes. 
3. Dado el nombre de un departamento indicar la cantidad total de accidentes 
ocurridos el año anterior. 
4. Mostrar los datos registrados con el siguiente formato. La fila “TOTAL” se debe 
mostrar el total de accidentes del mes. 
""" 
 
def menu ():
    entrar = True
    nrodepa = int(input("Ingrese el numero de departamento"))
    gd.agregarDatos(nrodepa)
    while entrar: 
        eleccion = int(input(opciones()))
        match (eleccion):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                print("opcion no valida")
                
if __name__ == "__main__":
    gd = GestorDepa()
    GestorDepa.cargarDepto
    menu()