import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #numero = 1

       # while numero < 6:
         #   numero += 1
       # alert ("datos", f"{numero}")    
      # lista_numero = list(range(1,6))
       #lista_nimbre = ["Franco", "Alejo", "Ale"]

       for numero in range(5):
        alert("numeros", f"{numeros + 1}")
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()