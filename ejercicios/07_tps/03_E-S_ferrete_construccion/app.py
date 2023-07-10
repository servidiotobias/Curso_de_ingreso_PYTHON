import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        txt_largo = self.txt_largo.get()
        txt_ancho = self.txt_ancho.get()
        txt_largo_numero = float(txt_largo)
        txt_ancho_numero = float(txt_ancho)
        metros_cuadrados = txt_largo_numero * txt_ancho_numero
        metros_lineales = txt_largo_numero * 4
        mensaje = ("los metros cuadrados son {0} y los metros lineales son {1}").format(metros_cuadrados, metros_lineales)
        alert("metros", mensaje)
        Poste_de_quebracho_grueso = txt_largo_numero // 250 * 4 + 4
        Poste_de_quebracho_fino = txt_largo_numero // 12 * 4
        mensaje_2 = ("la cantidad de postes de quebracho grueso es de {0} y de postes de quebracho fino es de {1}").format(Poste_de_quebracho_grueso, Poste_de_quebracho_fino)
        alert("calculos", mensaje_2)
        varillas = txt_largo_numero // 2 * 4
        mensaje_3 = ("la cantidad de varillas es de {0}").format(varillas)
        alert("varillas", mensaje_3)
        alambre_alta_resistencia = metros_lineales * 7
        mensaje_4 = ("la cantidad de alambre de alta resistencia es de {0}").format(alambre_alta_resistencia)
        alert("almbre de alta resistencia", mensaje_4)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
