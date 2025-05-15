class Accidente:
    __tabla:list
    
    def __init__ (self):
        self.__tabla =[]
    
    def inicializar(self, filas, columnas):
        for i in range(filas):
            for j in range (columnas):
                self.__tabla[i][j]=0
        
    def cargaTabla(self, mes, depto,cant):
        self.__tabla [depto-1][mes-1]+= cant 
        