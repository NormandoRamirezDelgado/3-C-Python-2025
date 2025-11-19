#Definición de una Clase
class Persona:
    def inicializarPersona(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrarPersona(self):
        print('Datos de la Persona')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
    

#Creación de Objetos por medio de la Instancia
persona = Persona() #Crea un Objeto Vacio en Memoria
nombre = input('Nombre: ')
apellido = input('Apellido: ')
persona.inicializarPersona(nombre, apellido)
persona.mostrarPersona()
personaDos = Persona()
personaDos.inicializarPersona('Pedro', 'Juárez')
personaDos.mostrarPersona()



