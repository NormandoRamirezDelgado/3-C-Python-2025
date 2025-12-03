import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Cajas de Texto')
ventana.configure(background='#1D2D44')

# Definimos el Método Mostrar
def mostrar():
    # Leemos el valor de la caja de texto
    texto = cajaTexto.get()
    print(f'Texto proporcionado: {texto}')
    etiqueta['text'] = texto

# Caja de Texto
cajaTexto = ttk.Entry(ventana, font=('NovaMono for Powerline', 14))
cajaTexto.pack(pady=50)

# Agregar un botón
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack(pady=10)

# Agregamos una etiqueta
etiqueta = ttk.Label(ventana, text='Valor Inicial')
etiqueta.pack(pady=20)


ventana.mainloop()