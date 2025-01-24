import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as func
from pyspark.sql.functions import dense_rank
from pyspark.sql.window import Window

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

destino = 's3://datalake-beatriz/Refined/parquet'

df1 = spark.read.parquet('s3://datalake-beatriz/Refined/parquet/dados_csv/')
df2 = spark.read.parquet('s3://datalake-beatriz/Refined/parquet/dados_tmdb/')

dados = df1.join(df2,df1.titulooriginal == df2.titulo)

dados = dados.withColumnRenamed('id','id_filme')
dados = dados.withColumnRenamed('anolancamento','ano')

window_spec = Window.orderBy('diretores')
dados = dados.withColumn('id_diretor',dense_rank().over(window_spec))

tabela_fato = dados.select(
    func.col('data_lancamento'),
    func.col('orcamento'),
    func.col('receita'),
    func.col('popularidade'),
    func.col('id_diretor'),
    func.col('id_filme')
).distinct()

caminho = f'{destino}/tabela_fato'
tabela_fato.write.mode('append').format('parquet').save(caminho)

filme_dim = dados.select(
    func.col('id_filme'),
    func.col('titulo'),
    func.col('tema')
).distinct()

caminho2 = f'{destino}/dim_filme'
filme_dim.write.mode('append').format('parquet').save(caminho2)

diretores_dim = dados.select(
    func.col('id_diretor'),
    func.col('diretores')
).distinct()

caminho3 = f'{destino}/dim_diretores'
diretores_dim.write.mode('append').format('parquet').save(caminho3)

dim_data = dados.select(
    func.col('data_lancamento'),
    func.col('ano'),
    func.col('mes'),
    func.col('dia'),
    func.col('estacao')
).distinct()

caminho4 = f'{destino}/dim_data'
dim_data.write.mode('append').format('parquet').save(caminho4)

job.commit()