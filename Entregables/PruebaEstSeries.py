import numpy as np
from scipy.stats import chi2

class Prueba_Series():
    def __init__(self):
        aleatorios=[]
        i=0
        l=40
        porc=5
        while i<l:
            num=np.random.rand()
            if num not in aleatorios:
                aleatorios.append(num)
                i+=1
        print(aleatorios)
        n=self.SeleccionN(l)
        print(n)
        Matriz=np.zeros((n,n))
        Fe=((l-1)/(n**2))
        print(Fe)
    
        i=1
        while i<l:
            x=aleatorios[i-1]
            y=aleatorios[i]
            print(x,y)
            
            r1=0
            r2=0
            posx=0
            posy=0
            for e in range(1,n+1):
                if x>r1 and x<e/n:
                    posx=e-1
                    break
                else:
                    r1=e/n

            for e in range(1,n+1):
                if y>r2 and y<e/n:
                    posy=e-1
                    break
                else:
                    r2=e/n
            print(posx,posy)
            Matriz[posx][posy]+=1
            i+=1
        print(Matriz)
        Fo=self.Conteo(Matriz)
        print(Fo)
        X0=self.Sumatoria(Fo,Fe)
        print("X0: ",X0)
        self.Aceptacion(X0,n,porc)

    def SeleccionN(self,l):
        n1=1
        n2=0
        while n2==0:
            Fe=(l-1)/(n1**2)
            print("Fe: ",Fe)
            print("n1: ",n1)
            if Fe<=5:
                n2=n1-1
            else:
                n1+=1
        if ((l-1)/(n1**2)-5)>=(5-(l-1)/(n2**2)):
            return n1
        else:
            return n2
    def Conteo(self,Matriz):
        Fo={}
        for f in range(len(Matriz)):
            for c in range(len(Matriz)):
                n=str(Matriz[f][c])
                if n in Fo:
                    Fo[n]+=1
                else:
                    Fo[n]=1
        return Fo
    
    def Sumatoria(self,Fo,Fe):
        print("Fe: ",Fe)
        if Fo=={}:
            print("Ocurrio un error en la sumatoria")
            return 0
        else:
            X0=0
            for k in Fo:
                print(k)
                s=((Fo[k]*(float(k)-Fe))**2)
                print("s: ",s)
                X0+=s
            X0=X0/Fe
            return X0

    def Aceptacion(self,X0,n,porc):
        alfa=porc/100
        print(n)
        gl=(n**2)-1
        # En estadística, ppf es 'Percent Point Function' (la inversa de la CDF)
        # Se usa (1 - alfa) porque queremos el valor del límite derecho
        ji2=chi2.ppf(1-alfa,gl)
        print("ji2: ",ji2, " X0: ",X0)
        if X0<ji2:
            print("Se acepta los numeros aleatorios")
        else:
            print("Se rechazan los numeros aleatorios")

obj=Prueba_Series()