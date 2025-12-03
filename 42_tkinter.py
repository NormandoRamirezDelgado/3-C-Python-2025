# Importamos la Bibkioteca Tkinter
import tkinter as tk

# Creamos una ventana
ventana = tk.Tk()

# Rrdimensionar la ventana
ventana.geometry("600x400")

# Modificar el título
ventana.title('Título de la Ventana')

# Evitar que se redimensione la ventana
ventana.resizable(0, 0)

# Color del fondo de la ventana
ventana.configure(background='#D1968C')

# Hacemos visible la ventana
ventana.mainloop()