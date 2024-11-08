####
**Localização**: C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint2\README.md

## Informações
* Na parte **exercícios** encontrará minhas resoluções dos exercícios.
* Indo em evidências você consegue entender como desenvolvi o desafio do sprint.
* Em **certificados** irá encontrar quais cursos participei e conclui.

## Anotações

Nessa sprint pude aprender mais sobre banco de dados e como fazer query's dentro deles. 
Além disso, aprendi que é preciso de um banco de dados normalizado e muito bem dimensionado para que nossas consultas sejam mais rápidas e tenhamos mais facilidade em analisar sobre determinado contexto

## Exercícios

Tivemos 18 exercícios onde pude praticar os principais comandos para se fazer consultas.
Aqui no exercício 7 eu precisava criar uma query que devolvesse como resultado os nomes dos autores com nenhuma publicação.

![](/Sprint2/evidencias/exercício7.png)

Para isso eu utilizei o comando with para criar uma subquerie onde tivesse uma nova tabela que me devolvesse a quantidade de livros publicados dos autores. Mas vamos dar um passo atrás. Para que eu conseguisse criar essa subquerie foi preciso de outros comandos bem mais simples, como o SELECT, FROM,JOIN'S,GROUP BY...

**Exemplificando cada um:** 
O select tem como funcionalidade selecionar determinadas colunas de uma certa tabela. Mas que tabela? Ai que entra o FROM, o from significa origem, de qual tabela vamos pegar essas colunas. 
Agora o join é uma estrutura um pouco mais complicada, mas de forma bem simplicada, ele serve para juntar tabelas e conseguirmos pegar informações de ambas. Temos o group by, ajuda a gente na hora de agrupar dados quando utilizamos funções agregadas ou o count, que conta os registros de nossa tabela. Já o order by, que ordena nossos dados apartir de uma coluna de forma ascendente ou descendente.
Bom, depois de explicar um pouco cada um, agora posso dizer como que em conjunto eles me ajudaram a resolver essa questão.

**O exercício**

Com o select eu peguei as colunas nome e fiz um count na coluna publicacação, para me devolver a quantidade de linhas nessa coluna. Mas você percebeu que essas colunas são de tabelas diferentes e por isso usei o Left Join. E por fim, como usei o count, utilizei o group by para agrupar por nome de autor.
Depois era só usar a tabela que criei e fazer uma consulta dentro devolvendo apenas autores que tem 0 publicações ordenados por ordem alfabética.

Tivemos vários exercícios que nos ajudaram a desenvolver essa qualidade analista e o exercício 7 pode mostrar um pouco como.

## Evidências

Aqui eu utilizei o comando *Create table* e *Primary key* para criação das novas tabelas e início da normalização.
![](/Sprint2/evidencias/createTable1.png)

Aqui utilizei o comando *Foreign key*, essencial para criar as relações entre as tabelas.
![](/Sprint2/evidencias/createTable3.png)

Alocação de dados foi feito utilizando os comandos *Insert into* e *Select*  para evitar inserções um por um de dados e o *Distinct* para evitar dados duplicados.
![](/Sprint2/evidencias/alocandoDados.png)

Diagrama do modelo relacional.
![](/Sprint2/evidencias/modeloRelacional.png)

Criação do modelo dimensional através de *Views*, utilizei o comando *Create View* e *From*.
![](/Sprint2/evidencias/view1.png)

Diagrama do modelo dimensional.
![](/Sprint2/evidencias/modeloDimensional.png)

## Certificados
Pude participar do curso da AWS  e aprender mais sobre seus príncipios,como trabalham e suas ideias de negócios.
Uma base para poder um dia trabalhar com eles.
![](/Sprint2/evidencias/certificadoAWS.png)
