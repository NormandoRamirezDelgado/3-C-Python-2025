class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        """Getter para nombre"""
        return self.__nombre
    
    @property
    def edad(self):
        """Getter para edad"""
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        """Setter"""
        self.__edad = nueva_edad


# Uso
persona = Persona("Ana", 20)

persona.__edad = 15
persona.__nombre = '0adfkjhadf'

print(persona.edad)  # Usa el getter
persona.edad = 21    # Usa el setter
print(persona.edad)  # Usa el getter
