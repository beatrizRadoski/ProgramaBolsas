def funcao_em_3pts(lista):
    n = len(lista)
    tamanho_ideal = n//3
   
    lista1 = lista[:tamanho_ideal]
    lista2 =  lista[tamanho_ideal:2 * tamanho_ideal]
    lista3 =  lista[2 * tamanho_ideal:]

    return lista1,lista2,lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = funcao_em_3pts(lista)
print(parte1,parte2,parte3)