####
**Localização**: C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint3\README.md

## Informações
* Na parte **exercícios** encontrará minhas resoluções dos exercícios.
* Indo em evidências você consegue entender como desenvolvi o desafio do sprint.
* Em **certificados** irá encontrar quais cursos participei e conclui.

## Anotações

Nessa sprint pude aprender os principais fundamentos de Python e como utilizá-los em tratamento de dados e análises. 

## Exercícios

#### Tivemos vários exercícios para praticar os fundamentos de Python antes de colocá-los em prática no desafio. Principalmente o exercício de ETL, na qual praticamos a extração, a transformação e o carregamento de dados sem o uso de bibliotecas. Mostrarei como utilizei os fundamentos nesse exercício. 

#### A partir de um dataset precisávamos extrair e limpar para depois conseguirmos fazer as análises. Nessa parte quero mostrar como fiz para trabalhar em cima desse dataset na extração e limpeza. Antes de começar, eu observei meu dataset e vi as principais limpezas que eu deveria trabalhar em cima, como no nome de certos autores que estavam fora do padrão, do tipo de valores de algumas colunas, que deveriam estar no tipo *float* e que estavam no tipo *str*.

![](/Sprint3/evidencias/exETL1.png)

#### Comecei armazenando o local onde encontraria o csv do dataset na variável *path_arquivo*. Após isso, eu li o arquivo csv com o *with open()*, onde posso ler o arquivo e ele fecha após terminar de ler meu arquivo de linha em linha com a função *readlines*, armazenando na variável *conteudo*. Criei minha primeira função *limpar_numero* onde eu armazenaria um valor no parâmetro e me retornaria o valor com o tipo *float*. Fiz também a limpeza no cabeçalho, retirando espaços vazios na extremidades dos nomes das colunas com a função *strip*, mudando espaços vazios entre os nomes com o *replace*, deixando todos os nomes em letra minúscula com o *lower* e, por fim, separando-os de vírgula em vírgula com o *split*.

#### Para que não misturasse dados não tratados com os tratados, como o cabeçalho, eu criei duas listas, somente *dados* e *dados_tratados*.

#### Agora sim eu irei começar a trabalhar em cima dos dados, para isso eu utilizei o for para tratar de linha em linha, removendo espaços nas extremidades, retirando aspas duplas e separando linha por linha de cada autor e suas informações pela aspas simples. Eu escolhi separar pelas aspas simples, porque se eu separasse por vírgula como no cabeçalho eu separaria o nome de um autor em duas colunas, pois seu nome apresenta vírgula no meio. No final, adicionei os dados parcialmente tratados na lista de *dados*.

#### Na parte de cima, eu ainda deixei os dados dos autores todos juntos em apenas uma string, ainda preciso separá-los por colunas. Para podermos fazer isso, precisamos tratar o nome do autor com a vírgula no meio. 

#### De linha por linha, vou acessar a linha e a string dentro dela, sabemos que strings também podem ser percorridas, assim quando acesso o índice 0 da string, estou acessando a primeira informação do autor, ou seja, o nome dele, o que queremos tratar. Após acessar, vou pegar o item acessado e modificá-lo com o *replace* retirando as vírgulas e os espaços vazios. Em seguida eu já separo a string contendo todas as informações com o *split* separando de vírgula em vírgula. Após todo esse tratamento, precisamos atualizar nossa linha agora com suas colunas. Para isso *[elementos[0].strip()]* pega o primeiro elemento de elementos e remove espaços extras usando *strip*, *[elem.strip() for elem in elementos[1:]]* pega os elementos restantes em *elementos* e remove os espaços vazios também e, finalmente atribuido à dados[i] ele renova a linha. 

#### Outra coisa que precisamos tratar são nossas colunas que deveriam estar no tipo *float*. Vamos fazer isso utilizando a função já criada, *limpar_numero*. Vamos aproveitar o for que acessa nossas linhas. Como são apenas as colunas 1,2,3 e 5 iremos especificá-las. Criaremos outro for dentro desse for para percorrer os elementos dentro das linhas. Caso o índice bata com os números de colunas que especificamos, nossos dados serão convertidos. Utilizei o *try* e *except* para tratar caso dê algum erro, colocando None. 

#### Após finalizar todo o tratamento dentro da lista de *dados* eu utilizei a função *extend* para adicionar os elementos da lista de *dados* à lista de *dados_tratados.* Agora sim meu dataset ficou pronto para serem feitas as análises.

![](/Sprint3/evidencias/exETL2.png)


## Evidências

#### Uso do *with* para abertura e leitura de arquivos, criação de funções com o *def*, criação de listas com *[]*, tratamento de dados com funções *strip*, *replace*, *lower*  e *split*.

![](/Sprint3/evidencias/exETL1.png)

#### Tratamento dos dados percorrendo linhas e elementos com o uso do *for*, utilização das funções como na primeira evidência. 

![](/Sprint3/evidencias/exETL2.png)

#### Importação de bibliotecas e suas utilizações, como leitura de arquivos com *read_csv* e remoção de dados duplicados com *drop_duplicates*.

![](/Sprint3/evidencias/parte1.png)

#### Criação de funções para ajudar nos tratamentos utilizando métodos como *isinstance* e funções para tratar os dados. Aqui eu fiz essa função para modificar strings em float. Retirando elementos dessas strings para não dar erro na transformação.

![](/Sprint3/evidencias/limpar_converter.png)

#### Nessa evidência pode se visualizar o uso da função *limpar_converter* com o *apply*. Além disso, utilizei funções como *sort_values* para ordenação em decrescente em certa coluna e a utilização do *head* que pega as n primeiras linhas, como  aqui pegando as 5 primeiras. 

#### Criação do gráfico com o *plot*. *Kind* recebe o tipo de gráfico que quero. Espefico qual coluna irá no eixo x e y. *figsize* o tamanho da figura do meu gráfico. *color* cor do gráfico. *Title* título do meu gráfico.

![](/Sprint3/evidencias/parte2.png)

#### Visualização do gráfico acima 

![](/Sprint3/evidencias/grafico2.png)

#### Utilização da função *value_counts* que mostra a quantidade de certos valores dentro de um dataset, utilizei o *head* para pegar as primeiras 15 linhas. Na crição do gráfico o tipo foi de pizza - *pie*, cor verde e como gráficos de pizzas usam porcentagem, utilizei o *autopct* para mostrar em porcentagem as quantidades com uma casa decimal

![](/Sprint3/evidencias/parte3.png)

#### Visualização do gráfico acima

![](/Sprint3/evidencias/grafico3.png)

#### Utilização da função *limpar_converter* para tratar a coluna, *sort_values* para ordenar os valores em decrescente e mostrar o primeiro resultado apenas. 

![](/Sprint3/evidencias/parte4.png)

#### Seleção das linhas que correspondiam *Mature 17+* da coluna *Content Rating*. Após isso, peguei da seleção apenas os apps que batiam com a seleção e utilizei a função *unique* para devolver como resultado apenas valores únicos, ou seja, não duplicados. Para finalizar, fiz uma contagem com a função *len*.

![](/Sprint3/evidencias/parte5.png)

#### Tratamento de dados com a função *limpar_converter*, ordenação da coluna *Reviews* em ordem decrescente e, para não pegar apps repetidos, fiz *drop_duplicates* na coluna *App* e peguei os 10 primeiros resultados apenas. 

![](/Sprint3/evidencias/parte6.png)

#### Ordenação da coluna *Last updated* em ordem crescente, pois aqui seriam os menores valores, resultado mostrando apenas as 10 primeiras linhas das colunas *App* e *Last Updated*. Criação do gráfico com a função *plot*, especificando *kind* para gráfico de linha, x e y para suas respectivas colunas, *figsize* para o tamanho do gráfico, *color* para cor do gráfico e *title* para o nome do gráfico. 

![](/Sprint3/evidencias/parte7-8.png)

#### Visualização do gráfico acima

![](/Sprint3/evidencias/grafico1-7-8.png)

#### Pegando o valor máximo da coluna *Reviews* com função *describe* que devolve a média, valor mínimo, máximo e muito mais de uma certa coluna. 

![](/Sprint3/evidencias/parte2-7-8.png)

#### Guardando o valor máximo na variável *max*, coluna *Reviews* ordenado de forma decrescente na variável *reviews* e a coluna *App* em *apps*. Após isso, criei um dataframe com essas variáveis para facilitar na criação do gráfico de dispersão. A criação do gráfico foi com a função plot e seus parâmetros utilizados da mesma forma que nas demais criações, utilizei *xticks* para remover os nomes dos apps no eixo x, pois eram muitos. Para criação da linha horizontal que marca o valor máximo, utilizei a função *axhline* e especifiquei o estilo dela com *linestyle*. Assim, o valor máximo fica evidente e conseguimos analisar a disparidade dos valores com o valor máximo.

![](/Sprint3/evidencias/parte3-7-8.png)

#### Visualização do gráfico acima

![](/Sprint3/evidencias/garfico2-7-8.png)

## Certificados
#### Pude participar do curso da AWS  e aprender mais sobre seus príncipios,como trabalham e suas ideias de negócios. Uma base para poder um dia trabalhar com eles.

![](/Sprint3/certificados/certificadoAWS.png)