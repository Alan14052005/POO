from clase_sube import Tarjetasube

def test():
    for i in range (3):
        saldo = float(input("Ingrese el saldo: "))
        numero = int(input("Ingrese el numero: "))
        tarjeta = Tarjetasube(saldo, numero)
        
        print(tarjeta)
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
        
        

                
                
