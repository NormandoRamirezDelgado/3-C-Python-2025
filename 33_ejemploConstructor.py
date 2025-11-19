class Aritmetica:
    def __init__(self, operandoUno, operandoDos):
        self.operandoUno = operandoUno
        self.operandoDos = operandoDos

    def sumar(self):
        resultado = self.operandoUno + self.operandoDos
        print(f'Resultado suma: {resultado}')
    
    def restar(self):
        resultado = self.operandoUno - self.operandoDos
        print(f'Resultado resta: {resultado}')
    
    def multiplicar(self):
        resultado = self.operandoUno * self.operandoDos
        print(f'Resultado multiplicación: {resultado}')
    
    def dividir(self):
        resultado = self.operandoUno / self.operandoDos
        print(f'Resultado división: {resultado}')

print('*** Ejemplo Clase Aritmética ***')
aritmeticaUno = Aritmetica(5, 7)
aritmeticaUno.sumar()
aritmeticaUno.restar()
aritmeticaUno.multiplicar()
aritmeticaUno.dividir()

print()
operandoUno = int(input('Escribe un valor entero: '))
operandoDos = int(input('Escribe un valor entero: '))
aritmeticaDos = Aritmetica(operandoUno, operandoDos)
aritmeticaDos.sumar()
aritmeticaDos.multiplicar()
aritmeticaDos.dividir()
aritmeticaDos.restar()


    

