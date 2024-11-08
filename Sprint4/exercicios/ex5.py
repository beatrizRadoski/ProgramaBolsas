from functools import reduce

with open('estudantes.csv','r') as arquivo:
    conteudo = arquivo.readlines()
  
lista_nova = [] 
for linha in conteudo:
    linha = linha.strip().split(',')
    
    linha[1:] = list(map(int,linha[1:]))
            
    lista_ordenada = sorted(linha[1:],reverse=True)
    nome = linha[0]
    lista_por_aluno = [nome]
    lista_por_aluno.extend(lista_ordenada)
    
    lista_nova.append(lista_por_aluno)

lista_nova.sort(key=lambda x: x[0])

for aluno in lista_nova:
    maiores_notas = aluno[1:4]
    soma = sum(maiores_notas)
    media = round(soma/3, 2)
    
    print(f'Nome: {aluno[0]} Notas: {maiores_notas} Média: {media}')
        
        