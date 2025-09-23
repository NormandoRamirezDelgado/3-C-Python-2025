# Esto generará números del 0 al 4
rango = 10
for i in range(5):
    print(f"Este es el ciclo número i: {i}") 
    for j in range(5):
        print(f"Este es el ciclo número j: {j}") 

variable = 1
for i in range(5):
    print(f'Número de Variable {variable}')
    variable = variable + 1
variable = 10
for i in range(5):
    print(f'Número de Variable {variable}')
    variable = variable + 1
print(variable)

# Genera números del 2 al 6
for i in range(1, 6):
    print(i)

# Genera números del 1 al 10, de dos en dos
for i in range(1000, 1050, 3):
    print(i)

# Cuenta regresiva desde 5 hasta 1
for i in range(5, 0, -1):
    print(i)

for i in range(5, -5, -1):
    print('Negativos: ', i)