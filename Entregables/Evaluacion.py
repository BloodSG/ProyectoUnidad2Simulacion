import customtkinter as ctk
import numpy as np

class GUI_Principal():
    def __init__(self):
        self.Ventana_main=ctk.CTk()
        self.Ventana_main.geometry("700x600")
        self.Ventana_main.title("Metodos de simulación")
        
        lblTitulo1=ctk.CTkLabel(self.Ventana_main,text="Metodos de generación de numeros aleatorios")
        lblTitulo1.place(relx=.5, rely=.1,anchor=ctk.CENTER)

        btn1=ctk.CTkButton(self.Ventana_main, text="Congruncial mixto",command= self.Genera)
        btn1.place(relx=.5,rely=.15,anchor=ctk.CENTER)


        lblTitulo2=ctk.CTkLabel(self.Ventana_main,text="Metodos de prueba de aleatoriedad")
        lblTitulo2.place(relx=.5, rely=.3,anchor=ctk.CENTER)

        btn2=ctk.CTkButton(self.Ventana_main, text="Corridas arriba y abajo",command= self.Arriba_Abajo)
        btn2.place(relx=.5,rely=.35,anchor=ctk.CENTER)

        btn3=ctk.CTkButton(self.Ventana_main, text="Corridas arriba y abajo del promedio",command= self.Arriba_Abajo_Promedio)
        btn3.place(relx=.5,rely=.4,anchor=ctk.CENTER)

        btn4=ctk.CTkButton(self.Ventana_main, text="Prueba de Series",command= self.Prueba_Series)
        btn4.place(relx=.5,rely=.45,anchor=ctk.CENTER)

        btn5=ctk.CTkButton(self.Ventana_main, text="Prueba de Poker",command= self.Prueba_Poker)
        btn5.place(relx=.5,rely=.5,anchor=ctk.CENTER)

        self.Ventana_main.mainloop()

    def Genera(self):
        self.Ventana1=ctk.CTkToplevel()
        self.Ventana1.geometry("800x700")
        self.Ventana1.title("Generación de numeros aleatorios")

        lblTitulo1=ctk.CTkLabel(self.Ventana1,text="METODO CONGRUENCIAL MIXTO",font=("Arial",20,"bold"))
        lblTitulo1.place(relx=.5, rely=.1,anchor=ctk.CENTER)

        self.entry1=ctk.CTkEntry(self.Ventana1, placeholder_text="X0",justify="center")
        self.entry1.place(relx=.5, rely=.2,anchor=ctk.CENTER)

        self.entry2=ctk.CTkEntry(self.Ventana1, placeholder_text="m",justify="center")
        self.entry2.place(relx=.5, rely=.3,anchor=ctk.CENTER)

        self.entry3=ctk.CTkEntry(self.Ventana1, placeholder_text="a",justify="center")
        self.entry3.place(relx=.5, rely=.4,anchor=ctk.CENTER)

        self.entry4=ctk.CTkEntry(self.Ventana1, placeholder_text="c",justify="center")
        self.entry4.place(relx=.5, rely=.5,anchor=ctk.CENTER)


        btn1=ctk.CTkButton(self.Ventana1, text="Iniciar")
        btn1.place(relx=.5,rely=.6,anchor=ctk.CENTER)

    def Arriba_Abajo(self):
        self.Ventana2=ctk.CTkToplevel()
        self.Ventana2.geometry("800x700")
        self.Ventana2.title("Prueba de aleatoriedad")

        lblTitulo1=ctk.CTkLabel(self.Ventana2,text="PRUEBA ARRIBA Y ABAJO",font=("Arial",20,"bold"))
        lblTitulo1.place(relx=.5, rely=.1,anchor=ctk.CENTER)

        self.txt_AA_1=ctk.CTkTextbox(self.Ventana2, width=100, height=300)
        self.txt_AA_1.place(relx=1/3, rely=.5,anchor=ctk.CENTER)

        self.txt_AA_2=ctk.CTkTextbox(self.Ventana2, width=100, height=300)
        self.txt_AA_2.place(relx=2/3, rely=.5,anchor=ctk.CENTER)

        btn1=ctk.CTkButton(self.Ventana2, text="Iniciar")
        btn1.place(relx=.5,rely=.8,anchor=ctk.CENTER)

    def Arriba_Abajo_Promedio(self):
        self.Ventana3=ctk.CTkToplevel()
        self.Ventana3.geometry("800x700")
        self.Ventana3.title("Prueba de aleatoriedad")

        
        lblTitulo1=ctk.CTkLabel(self.Ventana3,text="PRUEBA ARRIBA Y ABAJO DEL PROMEDIO",font=("Arial",20,"bold"))
        lblTitulo1.place(relx=.5, rely=.1,anchor=ctk.CENTER)


        self.txt_AAP_1=ctk.CTkTextbox(self.Ventana3, width=100, height=300)
        self.txt_AAP_1.place(relx=1/3, rely=.5,anchor=ctk.CENTER)

        self.txt_AAP_2=ctk.CTkTextbox(self.Ventana3, width=100, height=300)
        self.txt_AAP_2.place(relx=2/3, rely=.5,anchor=ctk.CENTER)

        btn1=ctk.CTkButton(self.Ventana3, text="Iniciar")
        btn1.place(relx=.5,rely=.8,anchor=ctk.CENTER)

    def Prueba_Poker(self):
        self.Ventana4=ctk.CTkToplevel()
        self.Ventana4.geometry("800x700")
        self.Ventana4.title("Prueba de aleatoriedad")


        lblTitulo1=ctk.CTkLabel(self.Ventana4,text="PRUEBA DEL POKER",font=("Arial",20,"bold"))
        lblTitulo1.place(relx=.5, rely=.1,anchor=ctk.CENTER)


        self.txt_PP_1=ctk.CTkTextbox(self.Ventana4, width=100, height=300)
        self.txt_PP_1.place(relx=1/3, rely=.5,anchor=ctk.CENTER)

        self.txt_PP_2=ctk.CTkTextbox(self.Ventana4, width=100, height=300)
        self.txt_PP_2.place(relx=2/3, rely=.5,anchor=ctk.CENTER)

        btn1=ctk.CTkButton(self.Ventana4, text="Iniciar")
        btn1.place(relx=.5,rely=.8,anchor=ctk.CENTER)

    def Prueba_Series(self):
        self.Ventana5=ctk.CTkToplevel()
        self.Ventana5.geometry("800x700")
        self.Ventana5.title("Prueba de aleatoriedad")


        lblTitulo1=ctk.CTkLabel(self.Ventana5,text="PRUEBA DE SERIES",font=("Arial",20,"bold"))
        lblTitulo1.place(relx=.5, rely=.1,anchor=ctk.CENTER)

        self.txt_PS_1=ctk.CTkTextbox(self.Ventana5, width=100, height=300)
        self.txt_PS_1.place(relx=1/3, rely=.5,anchor=ctk.CENTER)

        self.txt_PS_2=ctk.CTkTextbox(self.Ventana5, width=100, height=300)
        self.txt_PS_2.place(relx=2/3, rely=.5,anchor=ctk.CENTER)

        btn1=ctk.CTkButton(self.Ventana5, text="Iniciar")
        btn1.place(relx=.5,rely=.8,anchor=ctk.CENTER)

objeto=GUI_Principal()
