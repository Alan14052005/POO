from gestorBecas import gestorBeca
from gestorBeneficiarios import gestorbeneficiario

def menu():
    op = input('''
        Menu de opciones:
    a) Infomrar beneficiarios e importe total a pagar por la secretaria
    b) Informar si el beneficiario tiene mas de una beca
    c) Listar los beneficiarios, ordenados de mayor a menor por Facultad. 
    d) Listar estudiantes con promedio mayor a 8 fuera de la beca.
----> ''')
    while op != 'z':
        if op == 'a':
            tipobeca = input("Ingrese el tipo de beca: ")
            gBeca.informarBene(tipobeca, gBene)
        elif op == 'b':
            dni= int(input("Ingrese el dni: "))
            gBene.informarMasDeUnaBeca(dni)
        elif op == 'c':
            gBene.ordenarBeneficiario()
        elif op == 'd':
            gBene.noposeenbeca()
        else:
            print("opcion no encontrada")
        menu()


if __name__=='__main__':
    gBeca = gestorBeca()
    gBene = gestorbeneficiario()
    gBeca.cargaBeca()
    gBene.cargaBeneficiario()
    menu()