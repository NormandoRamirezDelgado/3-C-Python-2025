class ClasePadre:
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo_padre(self):
        print("Método de la clase padre")


class ClaseHija(ClasePadre):
    def __init__(self, atributo, nuevo_atributo):
        super().__init__(atributo)  # Llama al constructor del padre
        self.nuevo_atributo = nuevo_atributo
    
    def metodo_hija(self):
        print("Método de la clase hija")

class ClaseHijo(ClasePadre):
    def __init__(self, atributo, otro_atributo):
        super().__init__(atributo)
        self.otro_atributo = otro_atributo
    
    def metodo_hijo(self):
        print("Método de la clase hijo")


hija = ClaseHija('María', 'Perez')
hijo = ClaseHijo('PEdro', 'Martínez')

# Clase Hija Heredada de ClasePadre
print('')
print(hija.atributo)
print(hija.nuevo_atributo)

print('')
hija.metodo_padre()
hija.metodo_hija()

# Clase Hijo Heredada de ClasePadre
print('')
print(hijo.atributo)
print(hijo.otro_atributo)

print('')
hijo.metodo_padre()
hijo.metodo_hijo()