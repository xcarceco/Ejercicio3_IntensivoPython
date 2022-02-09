# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.
# Objetivo:
# - Uso de bucles anidados
# - El uso de colecciones

import math

def N():
    for numero in range(2,10):
        if ((math.factorial(numero-1)) + 1) % numero == 0:
            print(numero, 'es primo')
        else:
            print(numero, 'no es primo')
N()

