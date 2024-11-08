import random

random_list = random.sample(range(500), 50)
lista_ordenada = sorted(random_list)
n = len(random_list)

if n % 2 == 0:
    mediana = (lista_ordenada[n//2 - 1] + lista_ordenada[n//2])/2
else:
    mediana = lista_ordenada[n//2]


media = sum(random_list)/len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')