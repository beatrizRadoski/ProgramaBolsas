import pandas as pd 
import os

diretorio = r'C:\Users\beatr\OneDrive\Área de Trabalho\arquivos_csv'


arquivos_csv = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith('.csv')]

# juntando arquivos csv
df = pd.concat([pd.read_csv(arquivo,sep=';') for arquivo in arquivos_csv], ignore_index=True)

df.to_csv('bilheteria-diaria-obra-por-exibidora.csv',index=False)