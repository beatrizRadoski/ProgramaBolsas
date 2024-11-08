numeros = list(range(1,101))

numeros = list(range(2,101))

# um numero primo é quando ele é divido apenas por 1 e por ele mesmo

for numero in numeros:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            break
    else:
            print(numero)