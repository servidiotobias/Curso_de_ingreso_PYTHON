import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero_ingresado = ""
        suma_negativos = 0
        suma_positivos = 0
        numeros_positivos = 0
        numeros_negativos = 0
        cantidad_0 = 0
        diferencia_positivos_negativos = 0

        while numero_ingresado != None:
            numero_ingresado = prompt(title="ej10", prompt="ingrese un numero")

            if numero_ingresado != None:
                numero_ingresado = int(numero_ingresado)

                if numero_ingresado < 0:
                    suma_negativos = suma_negativos + numero_ingresado    
                    numeros_negativos = numeros_negativos + 1
                elif numero_ingresado > 0:
                    suma_positivos = suma_positivos + numero_ingresado
                    numeros_positivos = numeros_positivos + 1
                else: 
                    cantidad_0 += 1
        diferencia_positivos_negativos = numeros_positivos - numeros_negativos

        mensaje = "la suma acumulada de los negativos es {0}".format(suma_negativos)
        mensaje = mensaje + "la suma acumulada de los positivos es {0}".format(suma_positivos)                
        mensaje = mensaje + " cantidad de numeros positivos ingresados {0}".format(numeros_positivos)
        mensaje = mensaje + " cantidad de numeros negativos ingresados {0}".format(numeros_negativos)
        mensaje = mensaje + " cantidad de ceros {0}".format(cantidad_0)
        mensaje = mensaje + " diferencia entre la cantidad de los numeros positivos ingresados y negativos {0}".format(diferencia_positivos_negativos)

        alert("datos", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
