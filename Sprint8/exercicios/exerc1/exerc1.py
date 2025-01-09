import random

numeros_aleatorios = [random.randint(0,250) for elemento in range(250)]

numeros_aleatorios.reverse()

for numero in numeros_aleatorios:
    print(numero)

