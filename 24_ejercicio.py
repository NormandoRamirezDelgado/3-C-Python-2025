# Hacer un programa que capture 10 elementos enteros y calcule el promedio e imprima cuántos números son menores, mayores e iguales al promedio.
numeros = []
for i in range(10):
    numeros.append(int(input('Número: ')))
promedio = sum(numeros) / 10
mayores = 0
menores = 0
iguales = 0
for numero in numeros:
    if numero > promedio:
        mayores += 1
    if numero < promedio:
        menores += 1
    if numero == promedio:
        iguales += 1
print(f'{mayores} números son Mayores que el promedio')
print(f'{menores} números son Menores que el promedio')
print(f'{iguales} números son Iguales que el promedio')
