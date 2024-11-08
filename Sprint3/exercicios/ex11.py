import json 

# abrindo e lendo o arquivo
with open('person.json', 'r') as arquivo:
    
    dados = json.load(arquivo) # fazendo o parsing
    print(dados)