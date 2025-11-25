class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self.__saldo = saldo_inicial
        self.__deposito = 0
    
    @property
    def saldo(self):
        """Obtiene el saldo actual"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, cantidad):
        self.__saldo = cantidad
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, valor):
        self._titular = valor
    
    @property
    def deposito(self):
        return self.__deposito

    @deposito.setter
    def deposito(self, deposito):
        self.__deposito = self.__deposito + deposito
# Uso
cuenta = CuentaBancaria("María García", 1000)
print(cuenta.saldo)     # 1000
cuenta.deposito = 1500     # OK
print(cuenta.saldo)
# cuenta.titular = "Otro"  # AttributeError: no se puede modificar