def conta_vogais(string):
    
    somente_vogais = filter(lambda v: v in ['a','e','i','o','u'], string.lower())
    quantidade_vogais = len(list(somente_vogais))
    return quantidade_vogais
    
string = 'Olá, meu nome é Beatriz'   

contagem = conta_vogais(string)
print(contagem)

