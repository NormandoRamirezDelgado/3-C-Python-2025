# Comprobar si es primo o no en el rango 50 al 60
for i in range(50, 61):
    numero = int(input('Mensaje al usuario'))
    contador = 0
    for j in range(2, i):
        if i % j == 0:
            contador += 1
    if contador == 0:
        print(f'El número {i} es Primo')
    else:
        print(f'El número {i} es No es Primo')




