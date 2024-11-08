## Desafio
Aqui você encontrará o passo a passo de como solucionei o desafio do Sprint 2.

**Localização**: C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint2\desafio\README.md

O desafio propos que criássemos um modelo relacional e outro dimensional a partir de uma base de dados. Mas antes de tudo isso, foi preciso começar normalizando essa base de dados, já que continha apenas uma única tabela para todas as informações, sendo nada prático para se fazer consultas. 

## Normalização e modelo relacional

A normalização de um banco de dados consiste em organizar dados de forma lógica e eficaz, eliminando redundâncias e inconsistências.

**Formas normais**

1° Forma normal: não pode conter dados repetidos.

2° Forma normal:  Para estar na 2° forma normal é preciso que o banco de dados esteja na 1° forma normal. Além disso, nessa etapa, todos os campos que não são chaves primárias devem depender diretamente da chave primária, não podendo existir dependências parciais.

3° forma normal: O banco de dados deve estar na 1° e 2° forma normal e os atributos não chave primária devem depender apenas da chave primária, não podendo depender de outros atributos não chaves, ou seja, sem dependências transitivas.

Para fazer a normalização eu iniciei separando as colunas para suas respectivas tabelas de forma coerente, por exemplo, o que fazia sentido estar na tabela cliente. Com as chaves primárias definidas pude observar se havia dependências parciais ou transitivas, sendo mais fácil de visualizar e entender. Além disso, criei as chaves estrangeiras entre as tabelas, já criando o modelo relacional.

![](/Sprint2/evidencias/createTable1.png)
![](/Sprint2/evidencias/createTable2.png)
![](/Sprint2/evidencias/createTable3.png)

Como visto nas imagens acima, eu utilizei o comando *Create table* para criar as tabelas e *Primary key* para criar a chave primária.
Nas últimas criações das tabelas, é possível ver a estrutura da *Foreign Key*, onde criei a relação das tabelas carro-combustivel e demaisTabelas-locacao.

É preciso se atentar a uma coisa, a tabela *combustivel* não é ligada diretamente com a tabela *locação*, mas sim indiretamente. Eu liguei a tabela *combustivel* com a do *carro*, para depois ligar *carro* com *locação*.
Para isso, utilizei o comando *Update* na tabela locação e  pude fazer uma cópia do conteúdo do *idCombustivel* na tabela *carro* para tabela *locação*.

Mas por que foi feito isso? Pense que o combustível é uma parte de carro, certo? Só que se colocarmos idCombustivel como *Primary key* também, teríamos dependências parciais, ferindo a 2° forma normal. Então foi preciso criar uma tabela a parte e puxar *Idcombustivel* como *foreign key* na tabela *carro*. E para evitar dados duplicados e deixar o modelo mais limpo, eu puxei o *idCombustivel* da tabela *carros* para a tabela *locação*.

**Alocação de dados**

Após isso, eu comecei a alocar os dados sem duplicação, utilizando o comando *Distinct*. Para alocar os dados sem precisar digitar um por um, eu utilizei uma estrutura  com comandos *Insert into* e *select* para pegar os dados da base de dados que o desafio disponibilizou.

![](/Sprint2/evidencias/alocandoDados.png)
![](/Sprint2/evidencias/alocandoDados2.png)

Conforme acima, eu acabei fazendo as etapas meio que em conjunto, criando as tabelas já as normalizando e criando o modelo relacional. Ficando desta forma:

![](/Sprint2/evidencias/modeloRelacional.png)

## Modelo dimensional

Para finalizar o desafio, era preciso criar um modelo dimensional, importante para se fazer boas análises.
Um modelo dimensional contém tabelas fatos e tabelas de dimensões. Nas tabelas de fatos, encontramos dados de métricas e valores quantitativos. Já nas tabelas de dimensões, estão dados descritivos, que irão fornecer contexto e descrever melhor nossos dados quantitativos.

![](/Sprint2/evidencias/modeloDimensional.png)

Para criar o modelo dimensional, eu utilizei a dica de criar *Views*, assim criei as visualizações a partir das tabelas que criei no modelo relacional. Para isso eu utilizei o comando *Create view*, especifiquei o nome das colunas e como queria que elas ficassem e, por fim, para dizer de onde pegar essas colunas, eu utilizei o *from*.

![](/Sprint2/evidencias/view1.png)
![](/Sprint2/evidencias/view2.png)




