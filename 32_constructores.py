#Definición de clase
class Persona:

    #Constructor __init__ (dunder - doble underscore)
    def __init__(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrarContacto(self):
        print(f'''      Persona:
              Nombre: {self.nombre}
              Apellido: {self.apellido}''')
        

#Creación de Objetos

# Creación de un primer Objeto
personaUno = Persona('Layla', 'Acosta') 
#Se llama de manera automática el constructor
personaUno.mostrarContacto()

# Creamos otro objeto
print()
personaDos = Persona('Juan', 'Rodríguez')
personaDos.mostrarContacto()




