from clase_sube import Tarjetasube

class gestor_sube:
    __tarjetas: list
    
    def __init__(self):
        self.__tarjetas= []
    
    def agregar_tarjetas(self, tarjeta_sube):#INCISO 1
        self.__tarjetas.append(tarjeta_sube)
        
    def mostrar(self): #INCISO 2 
        aux=-1
        for tarjeta in self.__tarjetas:
            if tarjeta.consultar_Saldo()<0:
                print(f"Tarjeta número {tarjeta.getNumero()} con saldo ${tarjeta.consultar_Saldo()}")
                aux=1
        return aux 
            
            
    def buscar_tarjeta(self,nro):#INCISO 3
        encontrado = False
        indice = 0 
        aux = 1
        aux2=None
        while not encontrado and indice < len(self.__tarjetas):
            tarjeta = self.__tarjetas[indice]
            if nro == tarjeta.getNumero():
                encontrado = True
                aux2 = tarjeta.consultar_Saldo()
            else:
                indice+=1
        return aux2