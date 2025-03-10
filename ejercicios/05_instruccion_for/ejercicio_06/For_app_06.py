import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_numeros_pares = 0
        numero_pedidio = prompt("ej 4", "ingresar numeros")
        while numero_pedidio == None and not numero_pedidio.isdigit():
            numero_pedidio = prompt("ej 4", "ingresar numeros")
        numero_pedidio = int(numero_pedidio)  

        rango_a_recorrer = range(1, numero_pedidio + 1)
        rango_a_recorrer2 = range(1, numero_pedidio + 1,2)

        for numero in rango_a_recorrer2:
            print(numero)
        

        for numero in rango_a_recorrer:
            if numero % 2 == 0:
                contador_numeros_pares += 1  
                print (numero)

        alert("numeros pares", f"se encontraron {contador_numeros_pares} numeros pares")

        alert("numeros pares2", f"se encontraron  {len(rango_a_recorrer2)}numeros pares")        



        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()