# Hacer un programa que calcule el promedio de 10 números enteros e imprima el resultado
def sumar():
    global suma
    numero = int(input('Introduce un Número Entero: '))
    suma = suma + numero

suma = 0
for i in range(10):
    sumar()
promedio = suma / 10
print('El Promedio es: ',promedio)
