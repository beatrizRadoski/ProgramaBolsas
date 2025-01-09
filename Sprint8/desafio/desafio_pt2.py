import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as func
from pyspark.sql.functions import explode, when
from datetime import datetime

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

arquivo = args['S3_INPUT_PATH']
destino = args['S3_TARGET_PATH']
data = datetime.now().strftime('%Y/%m/%d')

dados = spark.read.option('multiline', 'true').json(arquivo)

df = dados.withColumn('pais_origem', explode(func.col('pais_origem')))
df = df.withColumn('produtoras', explode(func.col('produtoras')))

df = df.drop('filmes_similares','elenco')

df = df.withColumn('diretores', func.col('diretores').getItem(0))
df = df.withColumn('data_lancamento',func.col('data_lancamento').cast('date'))

df = df.withColumn('mes', func.month(df['data_lancamento']))
df = df.withColumn('dia', func.dayofmonth(df['data_lancamento']))

df = df.withColumn('Estacao',
    when(
        ((func.col('mes') == 9) & (func.col('dia') >= 23)) | 
        ((func.col('mes') > 9) & (func.col('mes') < 12)) | 
        ((func.col('mes') == 12) & (func.col('dia') <= 20)), 'Primavera'
    )
    .when(
        ((func.col('mes') == 12) & (func.col('dia') >= 21)) | 
        ((func.col('mes') >= 1) & (func.col('mes') <= 2)) | 
        ((func.col('mes') == 3) & (func.col('dia') <= 20)), 'Verao'
    )
    .when(
        ((func.col('mes') == 3) & (func.col('dia') >= 21)) | 
        ((func.col('mes') >= 4) & (func.col('mes') <= 5)) | 
        ((func.col('mes') == 6) & (func.col('dia') <= 20)), 'Outono'
    )
    .when(
        ((func.col('mes') == 6) & (func.col('dia') >= 21)) | 
        ((func.col('mes') >= 7) & (func.col('mes') <= 8)) | 
        ((func.col('mes') == 9) & (func.col('dia') <= 22)), 'Inverno'
    )
)

df = df.drop('mes','dia')

resultado = f'{destino}/Trusted/TMDB/parquet/{data}/dados_tmdb'
df.write.mode('overwrite').format('parquet').save(resultado)

job.commit()