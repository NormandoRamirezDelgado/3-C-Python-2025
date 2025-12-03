import tkinter as tk

# Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Etiquetas')
ventana.configure(background='#1D2D44')

# Creamos un aetiqueta (Label)
etiqueta = tk.Label(ventana, text='Saludos!')
etiquetaDos = tk.Label(ventana, text='Bienvenidos!')

# Cambiar el texto usando el método configure
etiqueta.configure(text='Hasta Luego!!!!')

# Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'Adios!!!!'

# Publicar o Mostrar el Widget
etiqueta.pack(pady=50)
etiquetaDos.pack(pady=100)

ventana.mainloop()