
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for posicao, Primeironome in enumerate(primeirosNomes):
    print(f'{posicao} - {Primeironome} {sobreNomes[posicao]} está com {idades[posicao]} anos')