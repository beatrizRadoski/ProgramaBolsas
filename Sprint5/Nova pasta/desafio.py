import pandas as pd 
import boto3

url = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint5\desafio\bilheteria-diaria-obra-por-exibidora.csv'
df = pd.read_csv(url)

# TRATAMENTO DE DADOS

def conversao(valor):
    if isinstance(valor,(float,int)):
        valor = str(valor).strip()
        return valor
    
df['DATA_EXIBICAO'] = pd.to_datetime(df['DATA_EXIBICAO'],dayfirst=True)

df['REGISTRO_COMPLEXO'] = df['REGISTRO_COMPLEXO'].apply(conversao)
df['REGISTRO_SALA'] = df['REGISTRO_SALA'].apply(conversao)
df['REGISTRO_GRUPO_EXIBIDOR'] = df['REGISTRO_GRUPO_EXIBIDOR'].apply(conversao)
df['REGISTRO_EXIBIDOR'] = df['REGISTRO_EXIBIDOR'].apply(conversao)

# CRIANDO COLUNAS NOVAS


df['CATEGORIA'] = df['PAIS_OBRA'].apply(lambda x: 'NACIONAL' if x == 'BRASIL' else 'INTERNACIONAL')

df['PUBLICO_TOTAL_FILME_CIDADE'] = df.groupby(['TITULO_ORIGINAL','MUNICIPIO_SALA_COMPLEXO'])['PUBLICO'].transform('sum')

dados = pd.Series(df['DATA_EXIBICAO'])
df['ANO_MES'] = dados.dt.to_period('M')

selecao = (df['PUBLICO_TOTAL_FILME_CIDADE'] >= 500) | (df['UF_SALA_COMPLEXO'] == 'PR')
df = df[selecao]

# Para poder analisar qual ano e mes as pessoas foram mais ao cinema
df['PUBLICO_POR_ANO_MES'] = df.groupby(['ANO_MES'])['PUBLICO'].transform('sum')

df.to_csv('dataframe.csv',index=False)

# ENVIANDO PARA BUCKET

session = boto3.Session(profile_name='default')

s3_client = session.client('s3')

bucket_name = 'mybucket-desafio'
arquivo_csv = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint5\desafio\dataframe.csv'
nome_no_bucket = 'dataframe.csv'  

try:
    s3_client.upload_file(arquivo_csv, bucket_name, nome_no_bucket)
    print(f"Arquivo '{arquivo_csv}' enviado para '{bucket_name}/{nome_no_bucket}' com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")