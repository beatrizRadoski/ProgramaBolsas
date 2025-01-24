import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as func

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

arquivo = args['S3_INPUT_PATH']
destino = args['S3_TARGET_PATH']

dados = spark.read.parquet(arquivo)

ids_selecionados = (
    dados
    .select(func.col('id'),func.col('titulooriginal'),func.col('anolancamento'))
    .where(func.col('id')
    .isin('tt0082971','tt0091344','tt0096895','tt0098180','tt0112462','tt1464335'))
    .distinct()
)

resultado = f'{destino}/Refined/parquet/dados_csv'
ids_selecionados.write.mode('overwrite').format('parquet').save(resultado)

job.commit()