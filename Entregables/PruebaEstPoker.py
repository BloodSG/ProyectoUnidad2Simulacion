import numpy as np
from scipy.stats import chi2

class Prueba_Del_Poker():
    def __init__(self):
        aleatorios=[]
        i=0
        l=40
        porc=5
        while i<l:
            num=round(np.random.rand(),5)
            if num not in aleatorios:
                lng=len(str(num))
                if lng!=7:
                    aux=7-lng
                    num=str(num)
                    num=num+str("0"*aux)
                aleatorios.append(str(num))
                i+=1
        self.TodosDif=.30240
        self.Par=.50400
        self.DosPares=.10800
        self.Tercia=.07200
        self.Full=.00900
        self.Pocker=.00450
        self.Quintilla=.00010

        self.Fe=[self.TodosDif,
                 self.Par,
                 self.DosPares,
                 self.Tercia,
                 self.Full,
                 self.Pocker,
                 self.Quintilla]

        #print(aleatorios)
        N=len(aleatorios)
        print("N numeros aleatorios: ",N)
        
        Frecuencias=self.Clasifica(aleatorios)
        Fo=self.FrecuenciaObserbada(Frecuencias,l)
        print(Fo)
        self.Aceptacion(Fo,porc)
    




    def Clasifica(self,aleatorios):
        TD=0
        Pr=0
        DPr=0
        Tcia=0
        Fll=0
        Pkr=0
        Qta=0
        for num in aleatorios:
            mano=num[2:7]
            Full=False
            DosPases=False
            Todos=0
            comparados=""
            for c in mano:
                if c in comparados:
                    continue
                
                else:
                    comparados+=c
                    if mano.count(c)==5:
                        Qta+=1
                    elif mano.count(c)==4:
                        Pkr+=1
                    elif mano.count(c)==3:
                        Tcia+=1
                        Full=True
                    elif mano.count(c)==2:
                        if Full==True:
                            Fll+=1
                            Full=False
                        else:
                            if DosPases==True:
                                DPr+=1
                                Pr-=1
                            else:
                                Pr+=1
                                DosPases=True
                    elif mano.count(c)==1:
                        Todos+=1
            if Todos==5:
                TD+=1
        print("TD: ",TD)
        print("Pr: ",Pr)
        print("DPr: ",DPr)
        print("Tcia: ",Tcia)
        print("Fll: ",Fll)
        print("Pkr: ",Pkr)
        print("Qta: ",Qta)
        return [TD,Pr,DPr,Tcia,Fll,Pkr,Qta]
    

    def FrecuenciaObserbada(self,Frecuencias,l):
        Fo=0
        print("frecuencias de obtenidas: ",Frecuencias)
        for f in range(len(Frecuencias)):
           Fo+=((Frecuencias[f] -    (self.Fe[f]*l)   )**2)    /   (self.Fe[f]*l)
        return Fo
    

    def Aceptacion(self,X0,porc):
        alfa=porc/100
        gl=6
        # En estadística, ppf es 'Percent Point Function' (la inversa de la CDF)
        # Se usa (1 - alfa) porque queremos el valor del límite derecho
        ji2=chi2.ppf(1-alfa,gl)
        print("ji2: ",ji2, " X0: ",X0)
        if X0<ji2:
            print("Se acepta los numeros aleatorios")
        else:
            print("Se rechazan los numeros aleatorios")

obj=Prueba_Del_Poker()