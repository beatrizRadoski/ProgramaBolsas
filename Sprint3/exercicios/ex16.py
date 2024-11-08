string = '1,3,4,6,10,76'

def armazenar_strings(string):
    numeros = [int(i) for i in string.split(',')]
    return sum(numeros)

resultado = armazenar_strings(string)
print(resultado)


