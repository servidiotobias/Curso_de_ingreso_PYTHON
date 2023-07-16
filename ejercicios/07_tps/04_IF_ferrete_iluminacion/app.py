import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad_numero = self.combobox_cantidad.get()
        cantidad_numero = int(cantidad_numero)
        precio = 800
#forma match
        match cantidad_numero:
            case 6:
                descuento = 0.50
            case 5:
                if marca == "ArgentinaLuz":
                    descuento = 0.40
                else:
                    descuento = 0.30
            case 4:
                if marca == "ArgentinaLuz" or "FelipeLamparas":
                    descuento = 0.25
                else:
                    descuento = 0.20
            case 3: 
                if marca == "ArgentinaLuz":
                    descuento = 0.15
                    if marca == "FelipeLamparas":
                        descuento = 0.10
                    else:
                        descuento = 0.05
            case 2 | 1:
                descuento = 0  
            case _:
                descuento = 0.50                   
        importe_final = (precio * cantidad_numero) - (precio * cantidad_numero * descuento)               
        if importe_final >= 4000:
            importe_final  * 0.95           
        mensaje = "el importe final es de {0}".format(importe_final) 
        alert("precio", mensaje)  

'''             
#forma 2
        if cantidad_numero >=6:
            descuento = 0.5
        elif cantidad_numero ==5:
            if marca == "ArgentinaLuz":
                 descuento = 0.40
            else:
                descuento = 0.30
        elif cantidad_numero ==4:
            if marca == "ArgentinaLuz" or "FelipeLamparas":
                 descuento = 0.25
            else:
                descuento = 0.20
        elif cantidad_numero ==3:
            if marca == "ArgentinaLuz":
                 descuento = 0.15
                 if marca == "FelipeLamparas":
                    descuento = 0.10
            else:
                descuento = 0.05
        importe_final = (precio * cantidad_numero) - (precio * cantidad_numero *descuento)        
        if importe_final >= 4000:
             importe_final * 0.95   
        mensaje = "el importe final es de {0}".format(importe_final) 
        alert("precio", mensaje)                  
'''
'''
#forma 1
        if(Cantidad_numero >= 6):
            total = (precio*Cantidad_numero)/2
            mensaje = "el precio total es de {0}".format(total)
            if(Cantidad_numero == 5 and "ArgentinaLuz"):
                 total = (precio*Cantidad_numero)*0.60
                 mensaje = "el precio total es de {0}".format(total)
        else:
             total = (precio*Cantidad_numero)*0.70
             mensaje = "el precio total es de {0}".format(total)    
             if(Cantidad_numero == 4):
                 if(Marca == "ArgentinaLuz" or "FelipeLamparas"):
                     total = (precio*Cantidad_numero)*0.75
                     mensaje = "el precio total es de {0}".format(total)
             else:
                total = (precio*Cantidad_numero)*0.80
                mensaje = "el precio total es de {0}".format(total)
                if(Cantidad_numero == 3 and "ArgentinaLuz"):
                     total = (precio*Cantidad_numero)*0.85
                     mensaje = "el precio total es de {0}".format(total)
                     if(Cantidad_numero == 3 and "FelipeLamparas"):
                         total = (precio * Cantidad_numero)*0.90
                         mensaje = "el precio total es de {0}".format(total)
                else:
                     total = (precio*Cantidad_numero)*0.95
                     mensaje = "el precio total es de {0}".format(total)     
 
        if(total >= 4000):
            total = (Cantidad_numero*precio)*0.95
        alert("precio", mensaje)  
'''        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()