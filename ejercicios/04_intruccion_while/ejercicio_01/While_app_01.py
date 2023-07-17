import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        flag_continuar = True
        contador = 0
        lista_numeros = [1,2,3,4,5,6,7,8,9,10]
        cantidad_numeros = len(lista_numeros)
        while contador < cantidad_numeros:
            alert("numeros", lista_numeros[contador])
            contador = contador + 1
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()