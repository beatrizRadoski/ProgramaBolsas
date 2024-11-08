# criando a função que será aplicada a cada elemento da lista
def funcao_para_lista(lista):
    return  [i **2 for i in lista]

def my_map(lista, funcao):
    return funcao(lista) 
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(lista, funcao_para_lista)
print(resultado)
