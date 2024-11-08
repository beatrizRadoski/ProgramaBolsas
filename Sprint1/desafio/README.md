## Desafio
Aqui você encontrará o passo a passo de como solucionei o desafio do Sprint 1.

**Localização**:C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint1\desafio

### Preparação
Para começar o desafio era necessário primeiro a criação do diretório *ecommerce* e para dentro dele copiar o arquivo *dados_de_vendas.csv*.

![Imagem da preparação](/Sprint1/evidencias/preparacao.png)

### Script
Comecei o script detalhando o caminho para dentro de *ecommerce*, assim pude criar o diretório *vendas* e, para dentro dele,\
copiar *dados_de_vendas* como *arquivo_dados_de_vendas*.

![](/Sprint1/evidencias/parte1.png)
  
Após isso, era preciso criar um subdiretório dentro de *vendas* chamado *backup* e copiar *dados_de_vendas* como *dados-**data**.csv*
Ainda na pasta *backup*, renomeei o arquivo *dados-**data**.csv* para *backup-dados-**data**.csv*.

![](/Sprint1/evidencias/parte2.png)

#### Trabalhando dentro do diretório *backup*
Nessa etapa, precisei criar um relatório que tivesse a data do dia e a hora que o programa foi rodado,
a data da primeira e útima venda registrada no arquivo, a quantidade distinta de produtos vendidas e,
por fim, as 10 primeiras linhas do arquivo.


#### O relatório
Antes de iniciar o a criação do relatório, eu criei dois arquivos. O arquivo0.txt para ir sobrescrevendo as informações e o relatório oficial onde ficará armazenado a informação quando tudo completo.

1- Data: utilizei o comando *date* e o formatei como queria apresentar no script, sendo %F para pegar data em yyyy/mm/dd\
o %l para pegar a hora e %m o minuto.

2- Para conseguir pegar a primeira data registrada, utilizei o comando *head* para pegar as primeiras 2 linhas do arquivo e o comando *tail* para pegar a última linha das 2 que selecionei com o comando *head*. Em seguida,utilizei o comando *cut* para pegar apenas a parte que eu queria da linha, a coluna data. Foi preciso especificar cut -d"," -aqui eu especifiquei como minhas colunas estavam sendo separadas- e -f5 para mostrar qual coluna eu queria, a 5. Assim obtive o resultado que era pedido.

3- Essa etapa era preciso apenas utilizar o comando *tail* pegando a última linha e o cut igual acima para pegar
somente a data.

4- Para conseguir pegar a quantidade de produtos diferentes vendidos eu utilizei o comando *tail +2* para que ele pegasse até a penúltima linha lá de cima do arquivo, deixando o cabeçalho. Depois, eu utilizei o comando *wc-l* para que contasse as linhas que especifiquei com o comando *tail*, devolvendo-me a quantidade 66.

5- Para pegar as primeiras 10 linhas foi apenas preciso utilizar o comando *head* e especificar a quantidade que eu queria que era 10.

![](/Sprint1/evidencias/parte3.png)

No final de todas essas linhas eu utilizei o sinal >> para mandar o resultado para o *arquivo0.txt*, para só depois de tudo pronto, enviar para o arquivo oficial utilizando o *cat*. Como o arquivo0.txt não teria mais utilidade, removi-o para não ficar ocupando espaço.

![](/Sprint1/evidencias/parte4.png)


####

Para finalizar, eu peguei o arquivo *backup-dados-**data**.csv* e transformei em zip com o comando *zip*.
Apaguei o csv dele, permanecendo apenas o arquivo zip. Além disso, também era necessário apagar o *arquivo_dados_de_vendas* dentro do diretório *vendas*. Então eu sai do diretório *backup* e apaguei o arquivo.

![](/Sprint1/evidencias/parte5.png)

#### Agendamento 
Além de criar o script, era preciso agendar ele para rodar por 4 dias num determinado horário. Dessa forma,
utilizei o crontab para fazer essa tarefa.
O crontab apresenta 5 asteriscos -* * * * *- sendo, em sequência, minuto, hora,dia, mês e dia da semana e sua estrutura de implementação

Como precisei rodar meu scrip de terça a sexta às 15h27, deixei especificado da seguinte forma:
![](/Sprint1/evidencias/crontab.png)
Especifiquei o caminho para chegar até meu scrip e utilizei um outro caminho que chegasse até o caminho do
arquivo log.txt para deixar registrado quando rodasse

#### Relatório final
Após rodar por 4 dias, eu criei um script que juntasse todos os relatórios gerados em um só, o relatório-final.txt.
O script cria o arquivo relatório-final e utiliza o comando cat para juntar todos os arquivos em um único, o relatório-final.
![](/Sprint1/evidencias/script-consolidador.png)
![](/Sprint1/evidencias/executando-consolidador.png)

Entregando como resultado:
![](/Sprint1/evidencias/resultado1.png)
![](/Sprint1/evidencias/resultado2.png)
