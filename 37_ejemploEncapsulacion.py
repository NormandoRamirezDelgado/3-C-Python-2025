class Persona:
    def __init__(self) -> None:
        self.__nombre: str = ''
        self.__apellidos: str = ''
        self.__direccion: str = ''

    
    
    # Propiedad Getter
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter  
    def nombre(self, nombre):
        self.__nombre = nombre

     # Propiedad Getter
    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

     # Propiedad Getter
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    
# Instancia de la Clase
persona = Persona()

# Imprimo el valor Inicial de cada Atributo
print(persona.nombre)
print(persona.apellidos)
print(persona.direccion)

# Asignar valores al atributo mediante el Setter
persona.nombre = 'Pedro'
persona.apellidos = 'Juárez'
persona.direccion = 'Domicilio Conocido'

# Imprimo el valor de cada Atributo
print(persona.nombre + ' ' + persona.apellidos )
print(persona.direccion)




    


    