with open('number.txt','r') as arquivo:
    conteudo = arquivo.readlines()

# essa função é necessária para fazer a filtragem de apenas números pares e ordenar eles em ordem decrescente  
def filtro(arquivo):
    
    numeros = list(map(int,arquivo))
    
    numeros_pares = filter(lambda num: num%2 ==0, numeros)
    
    numeros_pares_ordenados = sorted(numeros_pares,reverse=True)
    
    return numeros_pares_ordenados
    
def soma_5(arquivo, funcao):
    lista = funcao(arquivo)
    
    lista_com5 = lista[:5]
    
    soma = sum(lista_com5)
    
    print(lista_com5)
    return soma
    
soma = soma_5(conteudo,filtro)
print(soma)
