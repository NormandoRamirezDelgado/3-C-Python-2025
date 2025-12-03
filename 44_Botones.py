import tkinter as tk
from tkinter import ttk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Botones')
ventana.configure(background='#1D2D44')

def saludar(nombre):
    print(f'Saludos {nombre}')

# Botones 
botonUno = ttk.Button(ventana, text=' Enviar ', command=lambda: saludar('Juan'))
botonUno.pack(pady=50)

ventana.mainloop()