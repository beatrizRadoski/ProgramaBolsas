import boto3

session = boto3.Session(profile_name='default')

s3_client = session.client('s3')

bucket_name = 'mybucket-desafio'
arquivo_csv = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint5\desafio\bilheteria-diaria-obra-por-exibidora.csv'
nome_no_bucket = 'bilheteria-diaria-obra-por-exibidora.csv'  


try:
    s3_client.upload_file(arquivo_csv, bucket_name, nome_no_bucket)
    print(f"Arquivo '{arquivo_csv}' enviado para '{bucket_name}/{nome_no_bucket}' com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o arquivo: {e}")