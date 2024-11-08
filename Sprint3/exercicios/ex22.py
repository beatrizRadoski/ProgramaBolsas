class Pessoa:
    #inicializei o nome com none para definir seu valor somente depois
    def __init__(self, id, nome=None):
        self.nome = nome
        self.id = id
    
    @property 
    def nome(self):
        return self.__nome
        
    
    @nome.setter
    def nome(self,valor):
        self.__nome = valor
        
    
    
pessoa = Pessoa(0)
pessoa.nome = 'Fulano de Tal'
print(pessoa.nome)