#1. Solicitar al usuario el radio del circulo

from math import pi


radio = float(input('Ingrese el radio del circulo: '))

#2. Calcular el area del circulo usando la formula del area

area = pi*radio**2

#3. Mostrar el area calculada

print('El area del circulo con radio ', radio, ' es ', area)
