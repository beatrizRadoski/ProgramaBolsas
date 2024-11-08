from functools import reduce

produtos = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

def maiores_que_media(produtos):
    soma = reduce(lambda x,y: x + y, produtos.values())
    quantidade_itens = len(produtos)
    media = soma/quantidade_itens
    
    # verificando produtos maiores que a média
    filtro = [(produto,valor) for produto,valor in produtos.items() if valor > media]
    return sorted(filtro,key=lambda x: x[1])

resultado = maiores_que_media(produtos)
print(resultado)