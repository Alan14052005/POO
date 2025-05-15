from clase_cajadeahorro import Caja_de_ahorro


def test(cajas):  
    entrar = True        
    while entrar:
        eleccion = int (input(opciones()))
        match(eleccion):
            case 1:
                caja_solisi = int(input("Ingrese el numero de cuenta que desea saber infromacion:"))
                encontrado = False
                for caja in cajas:
                    if caja_solisi == caja._nroCuenta:
                            print(caja.mostrar_info())
                            encontrado = True
                            break 
                if not encontrado:
                        print("No encontrado")

            case 2:
                caja_depo = int(input("Ingrese el numero de cuenta a la que desea depositar:"))
                deposito = float(input("Ingrese le monto que desea ingresar"))
                for caja in cajas:
                    if caja_depo == caja._nroCuenta:
                         caja.depositar(deposito)
                         
                    
            case 3:
                caja_ext = int(input("Ingrese el numero de cuenta de la que desea extraer:"))
                extraccion = float(input("Ingrese el monto que desea extraer"))
                for caja in cajas:
                     if caja_ext == caja._nroCuenta:
                          caja.extraer(extraccion)
            case 4:
                entrar = False
            case _:
                print("esa opcion no es valida")

def carga(cajas):
        for i in range (1):
            nroCuenta = int(input("Ingrese el numero de cuenta:"))
            cuil = input("Inglrese el cuil:")
            apellido = input("Ingrese apellido:") 
            nombre = input("Ingrese nombre:")
            saldo = input("Ingrese saldo:")
            caja = Caja_de_ahorro(nroCuenta, cuil, apellido, nombre, saldo)
            cajas.append(caja)
    
            



def opciones():
    return """\n--- MENÚ DE OPCIONES ---
1. MOSTRAR INFORMACIÓN
2. DEPOSITAR DINERO
3. EXTRAER DINERO
4. SALIR
"""



