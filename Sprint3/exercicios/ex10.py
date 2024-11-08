lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def lista_sem_elem_duplicados(lista):
   return  list(set(lista))
   
nova_lista = lista_sem_elem_duplicados(lista)
print(nova_lista)