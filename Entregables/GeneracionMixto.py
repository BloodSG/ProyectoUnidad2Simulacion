import numpy as np
class GeneraMixto():
    def __init__(self):
        while True:
        #Xo=10
        #m=16
        #a=5
        #c=13
            X0=int(input("Ingrese el valor de Xo: "))
            m=int(input("Ingrese el valor de m: "))
            a=int(input("Ingrese el valor de a: "))
            c=int(input("Ingrese el valor de c: "))
            # Dentro de tu bloque de inicialización o método de captura
            errores = []

            if self.SeleccionXo(X0)==False:
                errores.append("Error en la selección de Xo")

            if self.SeleccionA(a)==False:
                errores.append("Error en la selección de a")

            if self.SeleccionC(c)==False:
                errores.append("Error en la selección de c")

            if self.SeleccionM(m, X0, a, c)==False:
                errores.append("Error en la seleccion de m")

            if errores!=[]:
                for error in errores:
                    print(error) 
            else:
                print("Todos los valores son correctos. Generando...")
                numeros_aleatorios=[]
                i=0
                Xi=X0
                while i<m:
                    Xi=(a*Xi+c)%m
                    print("X",i,": ",Xi/m," Resulatado",Xi)
                    numeros_aleatorios.append(Xi/m)
                    i+=1
                print(numeros_aleatorios)
    
    
    
    def SeleccionXo(self,X0):
        # semilla
        # cualquier valor entero preferiblemente que sea primo
        # mayor que cero
        if X0>0:
            return True
        else:
            return False
    
    def SeleccionM(self,m,X0,a,c):
        # modulo 
        # m= p^d, p es la base de la numeracion binaria y d cualquier numero entero
        # m> Xo, m>a, m>c
        if m>X0 and m>a and m>c:
            pot=0
            i=1
            while pot<=m:
                pot=2**i
                if pot==m:
                    return True
                else:
                    i+=1
            return False
        else:
            return False


    def SeleccionA(self,a):
        # multiplicador
        # (a-1)mod4 == 0
        # mayor a cero
        if a>0:
            if (a-1)%4==0:
                return True
            else:
                return False
        else:
            return False
    
    def SeleccionC(self,c):
        # constante aditiva
        # (c)mod8 == 5
        # mayor a cero
        if c%8==5:
            return True
        else:
            return False

GeneraMixto()