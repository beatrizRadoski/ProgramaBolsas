import json
import requests
from datetime import datetime
import boto3

API_KEY = 'd2b1d228172efb3c60d79433dcf8c1a6'
BASE_URL = 'https://api.themoviedb.org/3'
bucket_name = 'datalake-beatriz'
data = datetime.now().strftime('%Y/%m/%d')
base_path = f'Raw/TMDB/JSON/{data}/infos_filme'  

imdb_ids = [
    'tt0082971', 'tt0087469', 'tt0091344', 'tt0096895', 'tt0097576', 'tt0098180', 'tt0112462',
    'tt0277773', 'tt0367882', 'tt1464335', 'tt1512888', 'tt1686784', 'tt1787753', 'tt2025526',
    'tt2088003', 'tt5125414', 'tt5970844'
]

def get_movie_details(imdb_id):
    print(f'Buscando detalhes para o IMDb ID {imdb_id}')
    url = f"{BASE_URL}/find/{imdb_id}?api_key={API_KEY}&external_source=imdb_id"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro na requisição para o IMDb ID {imdb_id}: {response.status_code}")
        return None
    data = response.json()
    if 'movie_results' in data and data['movie_results']:
        movie_id = data['movie_results'][0]['id']
        detalhes_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
        detalhes_response = requests.get(detalhes_url)
        return detalhes_response.json()
    print(f'Nenhum detalhe encontrado para o IMDb ID {imdb_id}')
    return None

def get_movie_keywords(movie_id):
    print(f'Buscando palavras-chave para o filme {movie_id}')
    url = f"{BASE_URL}/movie/{movie_id}/keywords?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get('keywords', [])

def get_similar_movies(movie_id):
    print(f'Buscando filmes similares para o filme {movie_id}')
    url = f"{BASE_URL}/movie/{movie_id}/similar?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    similares = data.get('results', [])
    return [sim['title'] for sim in similares[:5]]

def get_movie_credits(movie_id):
    print(f'Buscando créditos para o filme {movie_id}')
    url = f"{BASE_URL}/movie/{movie_id}/credits?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    elenco = [membro['name'] for membro in data.get('cast', [])[:10]]  # Limitar aos 10 primeiros
    equipe = [membro['name'] for membro in data.get('crew', []) if membro.get('job') == 'Director']
    return elenco, equipe

def salvar_no_s3(registros, path_arquivo):
    s3_client = boto3.client('s3')
    body = json.dumps(registros, ensure_ascii=False, indent=4)

    s3_client.put_object(
        Bucket=bucket_name,
        Key=path_arquivo,
        Body=body,
        ContentType='application/json'
    )
    print(f'Arquivo {path_arquivo} carregado com sucesso no bucket {bucket_name}')

def lambda_handler(event, context):
    registros = []
    file_index = 1  
    for imdb_id in imdb_ids:
        detalhes = get_movie_details(imdb_id)
        if detalhes is None:
            continue
        
        keywords = get_movie_keywords(detalhes['id'])
        similares = get_similar_movies(detalhes['id'])
        elenco, equipe = get_movie_credits(detalhes['id'])
        
        if detalhes.get('budget', 0) > 0 and detalhes.get('revenue', 0) > 0:
            filme_info = {
                'titulo': detalhes.get('title', 'N/A'),
                'data_lancamento': detalhes.get('release_date', 'N/A'),
                'orçamento': detalhes.get('budget', 'N/A'),
                'receita': detalhes.get('revenue', 'N/A'),
                'popularidade': detalhes.get('popularity', 'N/A'),
                'produtoras': [produtora['name'] for produtora in detalhes.get('production_companies', [])],
                'pais_origem': [pais['name'] for pais in detalhes.get('production_countries', [])],
                'palavras_chave': [kw['name'] for kw in keywords],
                'filmes_similares': similares,
                'elenco': elenco,
                'diretores': equipe
            }
            registros.append(filme_info)
            print(f"Filme processado: {filme_info['titulo']}")

            if len(registros) >= 100:
                path_arquivo = f"{base_path}_{file_index}.json"  
                salvar_no_s3(registros, path_arquivo)
                registros = []  
                file_index += 1  

    if registros:
        path_arquivo = f"{base_path}_{file_index}.json"  
        salvar_no_s3(registros, path_arquivo)
    else:
        print("Nenhum filme com orçamento e receita encontrados.")



