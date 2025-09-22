# Hacer un programa que imprima si un valor es par o impar.
# Tambien si es par imprimir el resultado de la multiplicación por 5. 
# Pero si es impar imprimir la división por 3

numero = 18734658346

if numero % 2 == 0:
    print(f'El número {numero} es par ')
    resultado = True
else:
    print(f'El número {numero} es impar')
    resultado = False


if resultado == True:
    print(f'Multiplicación por 5: {numero * 5}')

if resultado == False:
    print(f'Multiplicación por 5: {numero / 3}')







