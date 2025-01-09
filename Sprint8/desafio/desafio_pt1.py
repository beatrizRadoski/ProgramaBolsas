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

dados = spark.read.csv(arquivo, sep='|', header=True, inferSchema=True)

dados = dados.replace('\\N', None).fillna({
    'notaMedia': 0,
    'genero': 'Desconhecido'
})

acao_aventura = dados.filter(func.lower(func.col('genero')) == 'action,adventure')

dados = dados.withColumn(
    'anoNascimento', func.when(func.col('anoNascimento').rlike('^\\d+$'), func.col('anoNascimento').cast('int')).otherwise(None)
)
dados = acao_aventura.withColumn(
    'anoFalecimento', func.when(func.col('anoFalecimento').rlike('^\\d+$'), func.col('anoFalecimento').cast('int')).otherwise(None)
)

resultado = f'{destino}/movies_acao_aventura'
acao_aventura.write.mode('overwrite').format('parquet').save(resultado)

job.commit()