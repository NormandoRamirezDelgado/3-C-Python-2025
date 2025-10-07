asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia','Lengua']
calificaciones = []
for asignatura in asignaturas:
    calificaciones.append(input('Introducir Calificación: ')))
for indice, asignatura in enumerate(asignaturas):
    print(f'En {asignatura} has sacado {calificaciones[indice]}')
