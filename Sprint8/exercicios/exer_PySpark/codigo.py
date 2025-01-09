from pyspark.sql import SparkSession
from pyspark import SparkContext,SQLContext
from pyspark.sql.functions import floor,rand, when
from pyspark.sql import functions as func

spark = SparkSession \
        .builder \
        .master ("local[*]") \
        .appName ("Exercicio Intro") \
        .getOrCreate()

arquivo = r'C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint8\exercicios\exer_PySpark\nomes_aleatorios.txt'
df = spark.read.csv(arquivo,header=False,inferSchema=True)

df = df.withColumnRenamed('_c0','Nomes')

valores = ['Fundamental','Médio', 'Superior']
df = df.withColumn('Escolaridade',
                    when(floor(rand() * 3) == 0, 'Fundamental')
                    .when(floor(rand() * 3) == 1, 'Médio')
                    .otherwise('Superior'))


paises = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 
        'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 
        'Uruguai', 'Venezuela', 'Guiana Francesa'
        ]

df = df.withColumn('Pais',
                   when(floor(rand()* 13) == 0, 'Argentina')
                   .when(floor(rand()* 13) == 1, 'Bolívia')
                   .when(floor(rand()* 13) == 2, 'Brasil')
                   .when(floor(rand()* 13) == 3, 'Chile')
                   .when(floor(rand()* 13) == 4, 'Colômbia')
                   .when(floor(rand()* 13) == 5, 'Equador')
                   .when(floor(rand()* 13) == 6, 'Guiana')
                   .when(floor(rand()* 13) == 7, 'Paraguai')
                   .when(floor(rand()* 13) == 8, 'Peru')
                   .when(floor(rand()* 13) == 9, 'Suriname')
                   .when(floor(rand()* 13) == 10, 'Uruguai')
                   .when(floor(rand()* 13) == 11, 'Venezuela')
                   .otherwise('Guiana Francesa')
                   )

anos = ['1964', '1997', '1971', '1994', '1958',
        '1977', '1987', '1978', '1973', '1956',
        '1953', '1954', '1980', '2001', '1970',
        '1949', '1990', '1966', '1959', '1989',
        '2002','2003','2005','2010','2006','2008'
]

df = df.withColumn('AnoNascimento',
                   when(floor(rand()* 26) == 0, anos[0])
                   .when(floor(rand()* 26) == 1, anos[1])
                   .when(floor(rand()* 26) == 2, anos[2])
                   .when(floor(rand()* 26) == 3, anos[3])
                   .when(floor(rand()* 26) == 4, anos[4])
                   .when(floor(rand()* 26) == 5, anos[5])
                   .when(floor(rand()* 26) == 6, anos[6])
                   .when(floor(rand()* 26) == 7, anos[7])
                   .when(floor(rand()* 26) == 8, anos[8])
                   .when(floor(rand()* 26) == 9, anos[9])
                   .when(floor(rand()* 26) == 10, anos[10])
                   .when(floor(rand()* 26) == 11, anos[11])
                   .when(floor(rand()* 26) == 12, anos[12])
                   .when(floor(rand()* 26) == 13, anos[13])
                   .when(floor(rand()* 26) == 14, anos[14])
                   .when(floor(rand()* 26) == 15, anos[15])
                   .when(floor(rand()* 26) == 16, anos[16])
                   .when(floor(rand()* 26) == 17, anos[17])
                   .when(floor(rand()* 26) == 18, anos[18])
                   .when(floor(rand()* 26) == 19, anos[19])
                   .when(floor(rand()* 26) == 20, anos[20])
                   .when(floor(rand()* 26) == 21, anos[21])
                   .when(floor(rand()* 26) == 22, anos[22])
                   .when(floor(rand()* 26) == 23, anos[23])
                   .when(floor(rand()* 26) == 24, anos[24])
                   .otherwise(anos[25])
                   )


df_select = df.select('Nomes').where(func.col('AnoNascimento').isin('2001','2002','2003','2004','2005',
                                                                        '2006','2007','2008','2009','2010'))

df.createOrReplaceTempView('pessoas')

df_select2 = spark.sql("select Nomes from pessoas where AnoNascimento in ('2001','2002','2003','2004','2005','2006','2007','2008','2009','2010')")

filtro = df.filter(func.col('AnoNascimento').isin('1980', '1981', '1982', '1983', '1984', '1985',
                                                  '1986', '1987', '1988', '1989', '1990', '1991',
                                                  '1992', '1993', '1994')) \
            .count()


filtro2 = spark.sql("""
                    select count(*) 
                    from pessoas 
                    where AnoNascimento in 
                    ('1980', '1981', '1982', '1983', '1984', '1985', 
                    '1986', '1987', '1988', '1989', '1990', '1991','1992', '1993', '1994')
                    
                   """ )

baby_b = ['1944', '1945', '1946', '1947', '1948',
          '1949', '1950', '1951', '1952', '1953',
          '1954', '1955', '1956', '1957', '1958',
          '1959', '1960', '1961', '1962', '1963', '1964']
ger_x = ['1965', '1966', '1967', '1968', '1969',
         '1970', '1971', '1972', '1973', '1974',
         '1975', '1976', '1977', '1978', '1979']
millennials = ['1980', '1981', '1982', '1983', '1984', '1985', 
                '1986', '1987', '1988', '1989', '1990', '1991',
                '1992', '1993', '1994']
ger_z = ['1995', '1996', '1997', '1998', '1999', '2000',
         '2001', '2002', '2003', '2004', '2005', '2006',
         '2007', '2008', '2009', '2010', '2011', '2012',
         '2013', '2014', '2015']

df = df.withColumn('Geracao',
                   when(df['AnoNascimento'].isin(baby_b), 'BabyBoomers')
                   .when(df['AnoNascimento'].isin(ger_x), 'GeracaoX')
                   .when(df['AnoNascimento'].isin(millennials),'Millennials')
                   .otherwise('GeracaoZ')
)

df.createOrReplaceTempView('pessoas')

filtro_geracao = spark.sql("""
                   select count(Nomes) as Quantidade,Pais,Geracao
                   from pessoas
                   group by Pais,Geracao
                   order by Pais,Geracao, Quantidade
                   """)
filtro_geracao.show()