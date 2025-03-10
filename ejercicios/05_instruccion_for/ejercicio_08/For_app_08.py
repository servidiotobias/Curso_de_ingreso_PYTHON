import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_pedidio = prompt("ej8", "ingresar un numero")
        while numero_pedido == None or not numero_pedido.isdigit():
            numero_pedido= prompt("IMPORTANTE", "Reingrese su numero")

        numero_pedidio = int(numero_pedidio)    
        numero_pedidio = numero_pedidio / 2

        for _ in range(1, numero_pedido + 1):
            if numero_pedido % _ == 0:
                contador = contador + 1  
                print(_)

        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()