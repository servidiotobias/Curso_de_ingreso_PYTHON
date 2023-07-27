'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        maximo_votos = 0
        nombre_maximo_votos = ""
        minimo_votos = 0
        nombre_minimo_votos = ""
        edad_menos_votos = 0
        acumulador_edad = 0
        edad_promedio = 0
        cantidad_candidato = 0
        total_votos = 0
        
        while True:
            nombre = prompt("tp10", "ingrese nombre")
            while nombre == None and nombre == "" or not nombre.isalpha():
                nombre = prompt("tp10", "ingrese nombre nuevamente")
                
            edad = prompt("tp10", "ingresa edad")
            while edad == None or not edad.isdigit() or int(edad) < 25 or int(edad) > 90:
                edad = prompt("tp10", "ingresa edad nuevamente")
            edad = int(edad)
            acumulador_edad += edad

            cantidad_votos = prompt("votos", "ingresar cantidad de votos")
            while cantidad_votos == None or not cantidad_votos.isdigit() or int(cantidad_votos) <=0 : 
                cantidad_votos = prompt("votos", "volver a ingresar cantidad de votos")
            cantidad_votos = int(cantidad_votos)    

            total_votos = total_votos + cantidad_votos

            if maximo_votos == None and minimo_votos == None:
                maximo_votos = cantidad_votos
                minimo_votos = cantidad_votos
                
            if cantidad_votos > maximo_votos:
                maximo_votos = cantidad_votos    
                nombre_maximo_votos = nombre

            elif cantidad_votos < maximo_votos:
                minimo_votos = cantidad_votos
                edad_menos_votos = edad
                nombre_minimo_votos = nombre

            respuesta = question("ej 5", "desea continuar? (si/no)")    
            if respuesta == False:
               break   

            cantidad_candidato += 1

            edad_promedio = acumulador_edad / cantidad_candidato
        print(f"el cantidato con mas votos es {nombre_maximo_votos} con {maximo_votos} votos")    
        print(f"el cantidato con menos votos es {nombre_minimo_votos} con {minimo_votos} votos y edad de {edad_menos_votos}")   
        print(f"el promedio de edades es de {edad_promedio}")
        print(f"el total de votos emitidos son {total_votos}")

        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
 
