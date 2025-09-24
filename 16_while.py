contador = 1
while contador < 5:
    print(contador)
    contador = contador + 1 # contador += 1

print('')
while contador > 0:
    print(contador)
    contador = contador - 1 # contador -= 1

respuesta = 's'
while respuesta.lower() == 's':
    valor = int(input('Dar un número: '))
    respuesta = input('Desesas continuar s/n? ')
