import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, count, desc, sum

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# 1 parte
df = spark.read.csv(source_file, header=True, inferSchema=True)
df.printSchema()

# 2 parte
df = df.withColumn("nome", upper(col("nome")))

# parte 3 
total_linhas = df.count()
print(f'Total de linhas do dataframe: {total_linhas}')

# parte 4 
agrupamento = (
    df.groupBy("ano", "sexo")
    .agg(count("nome").alias("contagem_nomes"))
    .orderBy(desc("ano"))
)
print("Contagem de nomes agrupando por ano e sexo, ordenado pelo mais recente:")
agrupamento.show()

# parte 5 
ranking_nomeFem = (
    df.filter(col("sexo") == "F")
    .groupBy("nome", "ano")
    .agg(count("nome").alias("total"))
    .orderBy(desc("total"))
    .first()
)
if ranking_nomeFem:
    print(
        f'Nome feminino com mais registros: {ranking_nomeFem["nome"]} em {ranking_nomeFem["ano"]} com {ranking_nomeFem["total"]} registros.'
    )
else:
    print("Nenhum registro encontrado para sexo feminino.")

ranking_nomeMasc = (
    df.filter(col("sexo") == "M")
    .groupBy("nome", "ano")
    .agg(count("nome").alias("total"))
    .orderBy(desc("total"))
    .first()
)
if ranking_nomeMasc:
    print(
        f'Nome masculino com mais registros: {ranking_nomeMasc["nome"]} em {ranking_nomeMasc["ano"]} com {ranking_nomeMasc["total"]} registros.'
    )
else:
    print("Nenhum registro encontrado para sexo masculino.")

# parte 6 
total_por_ano = (
    df.groupBy("ano")
    .agg(count("nome").alias("total"))
    .orderBy("ano")
    .limit(10)
)
print("Total de registros por ano:")
total_por_ano.show()

# Salvando o resultado
output = f"{target_path}/frequencia_registro_nomes_eua"
df.write.mode("overwrite").partitionBy("sexo", "ano").json(output)

job.commit()
