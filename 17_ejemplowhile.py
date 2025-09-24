# Hacer un programa que calcule el promedio de N números de tipo entero e imprima como resultado el promedio obtenido.
contador = 0
suma = 0
respuesta = 's'
while respuesta == 's':
    numero = int(input('Introducir un valor entero: '))
    suma = suma + numero
    contador = contador + 1
    respuesta = input('Hay más números? ')
promedio = suma / contador
print(f'El Promedio obtenido es: {promedio}')
