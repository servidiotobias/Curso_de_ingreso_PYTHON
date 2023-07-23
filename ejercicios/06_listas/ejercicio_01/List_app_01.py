import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en el vector lista_datos utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        for nombre in self.lista_datos:
            print (nombre)

"""
list.append(x): Agrega un elemento x al final de la lista.
list.remove(x): Elimina la primera aparición del elemento x de la lista.
list.pop([i]): Elimina y devuelve el elemento en la posición i de la lista. Si no se especifica i, se eliminará y devolverá el último elemento.
list.clear(): Elimina todos los elementos de la lista, dejándola vacía.
list.index(x[, start[, end]]): Devuelve el índice de la primera aparición del elemento x. Puedes proporcionar un rango opcional start y end para buscar
list.index(x[, start[, end]]): Devuelve el índice de la primera aparición del elemento x. Puedes proporcionar un rango opcional start y end para buscar dentro de una subsección de la lista.
list.count(x): Devuelve el número de apariciones del elemento x en la lista.
list.reverse(): Invierte el orden de los elementos en la lista.
len(list): Devuelve la longitud (número de elementos) de la lista.
"""
"""
      lista_numero = list(1,2,3,4,5,6)
      lista_numero.
"""        
     
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()