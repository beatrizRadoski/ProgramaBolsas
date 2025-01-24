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

df = (
    dados.select('*')
    .where(func.col('titulo').isin(
    'Raiders of the Lost Ark',
    'King Kong Lives',
    'Batman',
    'Red Scorpion',
    'Batman Forever',
    'Uncharted'
    ))
)

df = df.withColumn(
    'tema',
    func.expr(
        """
        element_at(
            filter(
                transform(palavras_chave, x -> lower(trim(x))),
                x -> array_contains(array('treasure hunt','giant animal','superhero','cold war'),x)
            ),
            1
        )
        """
    )
)

df = df.withColumnRenamed('orçamento','orcamento')

df = df.drop('palavras_chave','produtoras','pais_origem')

df = df.dropDuplicates()

resultado = f'{destino}/Refined/parquet/dados_tmdb'
df.write.mode('append').format('parquet').save(resultado)

job.commit()