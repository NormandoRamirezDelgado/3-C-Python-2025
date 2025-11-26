class Persona:
    def __init__(self, nombre, edad, email):
        self.__nombre = None
        self.__edad = None
        self.__email = None
    
        # Inicializamos usando los Setters para validar
        self.__nombre = nombre
        self.__edad = edad
        self.__email = email

    # Propiedad Nombre
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    # Propiedad Edad
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    # Propiedad Email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    # Mostrar Datos
    def mostrar(self):
        print(f'\n\nEl Nombre es: {self.__nombre} con {self.__edad} años y su correo es: {self.__email}')

    
persona = Persona('Juan', 16, 'juan@gmail.com')

print(f'\nNombre: {persona.nombre}')
print(f'Edad: {persona.edad}')
print(f'Email: {persona.email}')

persona.nombre = input('\nIntroduce el Nombre: ')
persona.edad = input('Introduce el Edad: ')
persona.email = input('Introduce el Correo: ')

print(f'\nNombre: {persona.nombre}')
print(f'Edad: {persona.edad}')
print(f'Email: {persona.email}')

persona.mostrar()