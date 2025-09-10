'''Hacer un programa que calcule el 10% de descuento de la venta realizada.
Imprimir como resultado el valor original de la venta, el descuento obtenido y 
el valor final ya con el descuento.'''
# Valor de la venta realizada

venta = 1000.00
descuento = venta * 0.10  # Calculo del descuento del 10%

# Total general ya copn descuento
total = venta - descuento

# Imprimir los resultados
print('Venta Inicial: $', venta)
print('Descuento: $', descuento)
print('Total a Pagar: $', total)
