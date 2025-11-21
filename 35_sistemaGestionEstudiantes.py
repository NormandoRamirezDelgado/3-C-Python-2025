'''Sistema de Gestión de Esrtudiantes
Ejemplo de uso de clases con constructores, atributos y métodos en Python.'''

class Estudiante:
    def __init__(self, matricula, nombre, edad, carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    
    def agregar_calificacion(self, materia, calificacion):
        '''Agrega una calificación de una materia'''
        self.calificaciones.append({
            'materia': materia,
            'calificacion': calificacion
        })
    
    def calcular_promedio(self):
        # Calcula el promedio de todas las calificaciones
        if not self.calificaciones:
            return 0

        suma = sum(cal['calificacion'] for cal in self.calificaciones)
        return suma / len(self.calificaciones)
    
    def mostrar_informacion(self):
        '''Muestra la información del estudiante'''
        print(f'\n\nINFORMACIÓN DEL ESTUDIANTE')
        print(f'{'='*50}')
        print(f'Matrícula: {self.matricula}')
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Carrera: {self.carrera}')
        print('\nCALIFICACIONES:')
        
        if self.calificaciones:
            for cal in self.calificaciones:
                print(f"  Materia: {cal['materia']}, Calificación: {cal['calificacion']}")
            print(f'Promedio: {self.calcular_promedio():.2f}')
        else:
            print('  No hay calificaciones registradas.')
            print(f'{"="*50}\n')

# Programa Principal
# Crear varios estudiantes usando el constructor
estudianteUno = Estudiante('A001', 'Ana Pérez', 20, 'Ingeniería')
estudianteDos = Estudiante('2025', 'Carlos Méndez', 18, 'Programación')
estudianteTres = Estudiante('2024', 'Luisa Gómez', 17, 'Puericultura')

# Agregar calificaciones a el alumno 1
estudianteUno.agregar_calificacion('Python', 90)
estudianteUno.agregar_calificacion('Dart', 100)
estudianteUno.agregar_calificacion('Java', 95)

# Agregar calificaciones a el alumno 2
estudianteDos.agregar_calificacion('Python', 60)
estudianteDos.agregar_calificacion('Dart', 95)
estudianteDos.agregar_calificacion('Java', 70)

# Agregar calificaciones a el alumno 3
estudianteTres.agregar_calificacion('Python', 60)
estudianteTres.agregar_calificacion('Dart', 95)
estudianteTres.agregar_calificacion('Java', 70)

# Vamos a mostrar la información de cada estudiante
estudianteUno.mostrar_informacion()
estudianteDos.mostrar_informacion()
estudianteTres.mostrar_informacion()

# Comparar los promedios de los estudiantes
print('\nCOMPARACIÓN DE PROMEDIOS:')
print(f'{estudianteUno.nombre}: {estudianteUno.calcular_promedio():.2f}')
print(f'{estudianteDos.nombre}: {estudianteDos.calcular_promedio():.2f}')
print(f'{estudianteTres.nombre}: {estudianteTres.calcular_promedio():.2f}')







    

