# Extração de dados
path_arquivo = r'\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint3\exercicios\exETL\actors.csv'

# arrumar itens númericos de string para float 
def limpar_numero(valor):
    return float(valor) 

with open(path_arquivo,'r') as arquivo:
    conteudo = arquivo.readlines()

dados_tratados = []
dados = []
## Tratamento de dados no cabeçalho
cabecalho = conteudo[0].strip().replace(' ','_').lower().split(',')
dados_tratados.append(cabecalho)

for linha in conteudo[1:]:
    linha = linha.strip().replace('"','') #remover espaços vazios e aspas duplas
    colunas = linha.split("'")
    dados.append(colunas)

## agora preciso tirar a virgula no meio do nome de robert
for i in range(len(dados)):
    linha = dados[i][0]  # Acessa a string
    linha = linha.replace(', Jr.', ' Jr.').replace(', ', ' ')  # Remove a vírgula e os espaços extras 
    elementos = linha.split(',')
    # Atualiza a linha com os elementos limpos
    dados[i] = [elementos[0].strip()] + [elem.strip() for elem in elementos[1:]]

    for j in range(len(dados[i])):  # Use o índice para percorrer os elementos da lista
        if j in [1, 2,3, 5]:  # Verifique se o índice é um dos que queremos converter
            try:
                dados[i][j] = limpar_numero(dados[i][j])  # Converte a string para float
            except (ValueError, IndexError):
                dados[i][j] = None  # Define como None se não for possível converter

dados_tratados.extend(dados)    
#print(dados_tratados)

# ETAPA 1
path_arq1 = r'Sprint3/exercicios/exETL/etapa-1.txt'
max_filmes = -1
ator_mais_filme = ''

for linha in dados_tratados[1:]:
    ator = linha[0]
    numero_filme = linha[2]

    if numero_filme > max_filmes:
        max_filmes = numero_filme
        ator_mais_filme = ator

with open(path_arq1,'w') as arquivo:
    texto = f'O {ator_mais_filme} tem o maior número de filmes, sendo {max_filmes}'
    arquivo.write(texto)



# ETAPA 2 
path_arq2 = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint3\exercicios\exETL\etapa-2.txt'
valor_total = 0
quantidade_gross = 0

for lista in dados_tratados[1:]:
    if len(lista) > 5:
        gross = lista[5]
        valor_total = valor_total + gross
        quantidade_gross = quantidade_gross + 1

media_gross = round(valor_total/quantidade_gross,2)

with open(path_arq2,'w') as arquivo:
    texto = f'A média de receita de bilheteria bruta dos filmes é {media_gross}'
    arquivo.write(texto)

# ETAPA 3
path_arq3 = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint3\exercicios\exETL\etapa-3.txt'
maior_avg_filmes = -1
ator_maior_avg = ''

for linha in dados_tratados[1:]:
    ator = linha[0]
    avg_filme = linha[3]

    if avg_filme > maior_avg_filmes:
        maior_avg_filmes = avg_filme
        ator_maior_avg = ator

with open(path_arq3,'w') as arquivo:
    texto = f'O {ator_maior_avg} tem a maior média de faturamento, sendo {maior_avg_filmes}'
    arquivo.write(texto)

# ETAPA 4
path_arq4 = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint3\exercicios\exETL\etapa-4.txt'
quantidade_por_filme = {}

for linha in dados_tratados[1:]:
    filme = linha[4]
    if filme in quantidade_por_filme:
        quantidade_por_filme[filme]+=1
    else:
        quantidade_por_filme[filme] = 1

filmes_ordenados = sorted(quantidade_por_filme.items(), key=lambda x: (-x[1], x[0]), reverse=True)

for i in range(len(quantidade_por_filme.keys())):
    with open(path_arq4,'w') as arquivo:
        incremento = 0
        for chave, valor in filmes_ordenados:
            texto = f'{incremento} - O filme {chave} aparece {valor} vez(es) no dataset\n'
            arquivo.write(texto)
            incremento = incremento + 1

# ETAPA 5
path_arq5 = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint3\exercicios\exETL\etapa-5.txt'
lista_TotalGross = {}

for lista in dados_tratados[1:]:
    ator = lista[0]
    total_gross = lista[1]
    
    lista_TotalGross[ator] = total_gross

lista_ordenada = sorted(lista_TotalGross.items(), key=lambda x: (-x[1], x[0]), reverse=True)

for chave, valor in lista_ordenada:
    print(f'{chave}: {valor}')

for i in range(len(lista_TotalGross.keys())):
    with open(path_arq5,'w') as arquivo:
        for chave, valor in lista_ordenada:
            texto = f'{chave} - {valor}\n'
            arquivo.write(texto)
