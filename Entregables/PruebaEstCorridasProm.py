import numpy as np
from scipy.stats import chi2,norm

class Prueba_corridas_Promedio():
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
        
        suma=0
        for num in aleatorios:
            suma+=num
        
        prom=suma/l
        print(prom)

        Z0= (   (   prom - (1/2) ) * (   l**(1/2)  )   )   /   ((1/12)**(1/2))
        
        if Z0<0:
            Z0=Z0*-1
        print(Z0)
        
        self.Aceptacion(Z0,porc)
        

    
    def Aceptacion(self,Z0,porc):
        alfa=(porc/100)/2
        z_tabla=norm.ppf(1 - 0.05/2)
        print(z_tabla)

        if Z0<z_tabla:
            print("Se acepta los numeros aleatorios")
        else:
            print("Se rechazan los numeros aleatorios")


        
        
        
Prueba_corridas_Promedio()