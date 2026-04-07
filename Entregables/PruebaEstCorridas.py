import numpy as np
from scipy.stats import chi2

class Prueba_corridas():
    def __init__(self):
        aleatorios=[]
        l=40
        porc=5
        i=0
        self.tope=3
        while i<l:
            num=np.random.rand()
            if num not in aleatorios:
                aleatorios.append(num)
                i+=1
        print(aleatorios)
        
        i=0
        delimitacion=[]
        while i<l-1:
            if aleatorios[i]<aleatorios[i+1]:
                delimitacion.append(0)
            else:
                delimitacion.append(1)
            i+=1
        print(delimitacion)
        corridas=self.Conteo(delimitacion)
        print(corridas)
        Fe=self.FrecuenciaEsperada(corridas,l)
        print(Fe)
        X0=self.CalcularEstadistico(Fe,corridas)
        print(X0)
        self.Aceptacion(X0,porc)
        

    def Conteo(self,delimitacion):
        corrida={}
        ceros=0
        unos=1
        c=1
        for i in range(len(delimitacion)-1):
            simbol=delimitacion[i]
            print(simbol)
            if simbol==delimitacion[i+1]:
                c+=1
            else:
                if c>=self.tope:
                    c=self.tope
                if c in corrida:
                    corrida[c]+=1
                else:
                    corrida[c]=1
                c=1
            
        return corrida                    

    def FrecuenciaEsperada(self,corridas,l):
        Fe=[]
        m=(((2*l)-1)/self.tope)
        print(m)
        a1=0
        a2=0
        d=1
        for k in corridas:
            if k!=self.tope:
                a1= ((k**2) + (3*k) + 1)*l
                a2= ((k**3) + (3*(k**2)) - k - 4)
                d=1
                for i in range(k+3):
                    d+=i*d
                print(d)
                Fe.append(2*((a1-a2)/d))
        if self.tope in corridas:
            Fe.append(m-sum(Fe))
        return Fe
        

    def CalcularEstadistico(self,Fe,corridas):
        X0=0
        i=0
        for k in corridas:
            if k!=self.tope:
                X0+=    (   (corridas[k] - Fe[i]  )**2  ) /   Fe[i]
                print(X0)
                i+=1
        if self.tope in corridas:
            X0+=(   (   corridas[self.tope] - Fe[-1]   )**2    )   /   Fe[-1]
        print(X0)
        return X0

    def Aceptacion(self,X0,porc):
        alfa=porc/100
        gl=self.tope-1
        # En estadística, ppf es 'Percent Point Function' (la inversa de la CDF)
        # Se usa (1 - alfa) porque queremos el valor del límite derecho
        ji2=chi2.ppf(1-alfa,gl)
        print("ji2: ",ji2, " X0: ",X0)
        if X0<ji2:
            print("Se acepta los numeros aleatorios")
        else:
            print("Se rechazan los numeros aleatorios")


        
        
        
Prueba_corridas()