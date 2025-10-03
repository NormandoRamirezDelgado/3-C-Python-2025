mi_lista = [1, 2, 3, 4, 5]
mi_lista.clear()
print(mi_lista)
# Salida: []

print('')
mixto = ["hola", 2, True, "hola", 654]
indice = mixto.index("hola", 3)
print(indice)
# Salida: 0

print('')
calificaciones = [10, 8, 9, 7, 9, 10, 9]
num_nueves = calificaciones.count(9)
print(num_nueves)
# Salida: 3

print('')
numeros = [4, 1, 8, 3, 6]
numeros.sort()
print(numeros)
# Salida: [1, 3, 4, 6, 8]

numeros.sort(reverse=True)
print(numeros)
# Salida: [8, 6, 4, 3, 1]

print('')
vocales = ['a', 'e', 'i', 'o', 'u']
vocales.reverse()
print(vocales)
# Salida: ['u', 'o', 'i', 'e', 'a']

numeros = [4, 1, 8, 3, 6]
numeros.reverse()
print(numeros)

print('')
dias = ["Lunes", "Martes", "Miércoles"]
print(len(dias))
# Salida: 3

print('')
edades = [22, 45, 19, 32]
edades_ordenadas = sorted(edades)
print(f"Lista original: {edades}")
# Salida: Lista original: [22, 45, 19, 32]
print(f"Nueva lista ordenada: {edades_ordenadas}")
# Salida: Nueva lista ordenada: [19, 22, 32, 45]

print('')
precios = [12.5, 40.0, 9.99, 150.25]
print(f"Total: {sum(precios)}")     # Salida: Total: 212.74
print(f"Mínimo: {min(precios)}")    # Salida: Mínimo: 9.99
print(f"Máximo: {max(precios)}")    # Salida: Máximo: 150.25

print('')
original = [1, 2, 3]
copia = original.copy()
copia.append(4)

print(f"Original: {original}") # Salida: Original: [1, 2, 3]
print(f"Copia: {copia}")     # Salida: Copia: [1, 2, 3, 4]

print('')
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

valores = [10, 15, 17, 89]
suma = 0
for numero in valores:
    suma += numero
print(suma)
print(suma/len(valores))

print('')
mi_lista = ["manzana", "banana", "cereza"]

for indice, fruta in enumerate(mi_lista):
    print(f"La fruta en el índice {indice} es: {fruta}")
