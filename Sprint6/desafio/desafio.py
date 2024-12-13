import boto3
import os
from datetime import datetime 

base_dir = '/data'

# Fazendo a leitura dos arquivos
url_filme = os.path.join(base_dir,'movies.csv')
url_serie = os.path.join(base_dir,'series.csv')

data = datetime.now().strftime('%Y/%m/%d')

# Acessando minha conta AWS

session = boto3.Session(profile_name='default')
s3_client = session.client('s3',region_name='us-east-1')

# Configurando o bucket e o arquivo 

bucket_name = 'datalake-beatriz'
path_filme = f'Raw/Local/CSV/Movies/{data}/movies.csv'
path_serie = f'Raw/Local/CSV/Series/{data}/series.csv'

def criar_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} criado com sucesso")
    except s3_client.exceptions.BucketAlreadyOwnedByYou:
        print(f"Bucket '{bucket_name}' já existe e pertence a você.")
    except Exception as e:
        print(f"Erro ao criar o bucket: {e}")

def upload_arquivos(arquivo_local,bucket_name,caminho_s3):
    try:
        s3_client.upload_file(arquivo_local,bucket_name,caminho_s3)
        print(f"Arquivo {arquivo_local} enviado para s3://{bucket_name}/{caminho_s3} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o arquivo: {e}")

criar_bucket(bucket_name)
upload_arquivos(url_filme,bucket_name,path_filme)
upload_arquivos(url_serie,bucket_name,path_serie)