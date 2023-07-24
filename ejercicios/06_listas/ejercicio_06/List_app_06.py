import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'PROMEDIO' se analizará el vector lista_datos a efectos de calcular 
el promedio el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        suma = 0
        for numero in self.lista_datos:
            suma += numero
            # sumatoria = sum(self.lista_datos) este no usar aun
        cantidad_elementos_en_lista = len(self.lista_datos) 
        if cantidad_elementos_en_lista != 0:
                promedio = suma / len(self.lista_datos)
                alert("ej6", f"el promedio es de {promedio}")   
        else:        
            alert("ej6", "la lista esta vacia")    
        # sacar promedio de lista_datos
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()