from gestorAtenciones import gestorAtencion
from gestorPacientes import gestorPaciente

def menu():
    op = input('''
        Menu de opciones:
    a) Infomrar atenciones en una fecha indicada.
    b) Indicar cantidad de atenciones que tuvo un paciente.
    c) Listar pacientes que no tuvieron ninguna atención.
    d) Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad.
----> ''')
    while op != 'z':
        if op == 'a':
            fecha= input("Ingrese la fecha: ")
            gA.buscarFecha(fecha)
        elif op == 'b':
            dni= int(input("Ingrese DNI: "))
            NyA=gP.buscarNombre(dni)
            cantAtenciones = gA.contarAtenciones(dni)
            print(f"El DNI {dni} a nombre de {NyA} tuvo {cantAtenciones} atenciones")
        elif op == 'c':
            gP.listarSinAtencion(gA)
            
        elif op == 'd':
            gP.ordenarPaciente()
        else:
            print("opcion no encontrada")
        menu()


if __name__=='__main__':
    gA = gestorAtencion()
    gP = gestorPaciente()
    gP.cargaPaciente()
    gA.cargarAtencion()
    menu()