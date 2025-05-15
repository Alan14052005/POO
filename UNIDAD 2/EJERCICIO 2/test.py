from clase_sube import Tarjetasube
from Gestor_Sube import gestor_sube


def test(tarjetas):
    lista=gestor_sube()
    entrar=True
    while entrar:
        eleccion=int(input(opciones()))
        match(eleccion):
            case 1:
                for i in range (2):
                    saldo = float(input("Ingrese el saldo: "))
                    numero = int(input("Ingrese el numero: "))
                    tarjeta = Tarjetasube(saldo, numero)
                    lista.agregar_tarjetas(tarjeta)
                lista.mostrar()
                
            case 2:
                no=lista.mostrar()
                if no <0:
                    print("No hay tarjetas negativas")
                
            case 3:
                nro = int(input("Ingrese el numero de la tarjeta que desea buscar: "))
                aux2=lista.buscar_tarjeta(nro)
                if aux2 == None:
                    print("Tarjeta no encontrada")
                else:
                    print(aux2)
            case 4:
                entrar=False
            case _:
                print("opcion no valida")
                
    """print(tarjeta)
        print("El saldo de la tarjeta acutualmente es: {}". format (tarjeta.consultar_Saldo()))
        
        impor_carga=float(input("Ingrese el importe que desea cargar: "))
        tarjeta.cargarSaldo(impor_carga)
        print("El saldo de la tarjeta acutualmente es: {}". format (tarjeta.consultar_Saldo()))
        
        imp_psg=float(input("Ingrese el valor del pasaje: "))
        aux=tarjeta.pagar_pasaje(imp_psg)
        if aux < 0:
            print("No hay saldo suficiente")
        else:
            print("La opracion se realizo con exito,El saldo de la tarjeta acutualmente es: {}". format (tarjeta.consultar_Saldo()))
        """
        
def opciones():
    return """\n---MENU DE OPCIONES---
1. AGREGAR TARJETAS
2. MOSTRAR TARJETAS NEGATIVAS
3. BUSCAR TARJETA
4. SALIR
"""
                
                
