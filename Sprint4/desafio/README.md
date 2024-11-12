## Desafio
Aqui você encontrará o passo a passo de como solucionei o desafio do Sprint 4.

**Localização**: C:\Users\beatr\OneDrive\Área de Trabalho\ProgramaBolsas\Sprint4\desafio\README.md

### O desafio tem como objetivo a prática de Docker com scripts de Python. O docker é uma ferramenta que quebra muito o galho dos desenvolvedores, visto que já tem todo o ambiente preparado para podermos rodar nossas aplicações mesmo que com diferentes tipos de linguagens, ou seja, não precisamos ficar instalando diferentes linguagens em nossa máquina, sobrecarregando ela. 

#### No docker temos os containers e as imagens. Os containers servem como ambientes isolados preparados para receber nossa aplicação. As imagens são nossos scripts, comandos que irão rodar dentro dos containers. 

#### O desafio forneceu um script de python de onde era preciso criar um container propício para rodar essa aplicação. 

#### Primeiro é preciso criar o documento *Dockerfile*, onde vamos informar a imagem que será rodada no *FROM*, o diretório em que será trabalhado a aplicação no *WORKDIR*, *COPY . .* para copiar tudo que se encontra no meu workdir e, por final, o *CMD* onde iremos dizer o que será rodado.

#### No *FROM* eu especifiquei a imagem de python para ajudar a rodar meu script do desafio, especifiquei meu workdir, copiei tudo de lá e rodei o *CMD ["python", "carguru.py"]*. Após a criação do arquivo Dockerfile, podemos seguir com as etapas.

![](/Sprint4/evidencias/docker_carguru.png)

### Construção da imagem

![](/Sprint4/evidencias/criando_imagem.png)

#### Para construir uma imagem, utilizamos o comando *docker build* o uso do *-t* é para nomear uma imagem enquanto ela está sendo criada, por isso *docker build -t carguru_image .* e, no final, o (.) que foi para referencia ao diretório atual.

![](/Sprint4/evidencias/imagem_carguru_criada.png)

### Rodando imagem no container

![](/Sprint4/evidencias/rodando_nocontainer.png)

#### Depois que criamos a imagem, precisamos rodar ela em um container, para isso utilizaremos o comando *docker run* ele cria o container e roda a imagem. Pela imagem é possível observar que utilizei a linha de código *docker run -it --name carguru_cont carguru_image*. A flag -it é para que eu possa visualizar a imagem rodando, o --name foi para nomear meu container para *carguru_cont*. Após rodar essa linha de código é possível ver a saída do script que pedimos no dockerfile para ser rodado, o carguru.py.

## Etapa 2 - Nessa etapa surgiu a pergunta sobre reutilização de containers, se era possível. 

#### No docker é possível sim a reutilização de containers com o comando *start*. Vamos verificar isso na imagem abaixo. Pude reiniciar o container usando *docker start -i <nome_container>*, a flag -i foi para que nosso container não rodasse no modo background.

![](/Sprint4/evidencias/reiniciando_cont.png)

## Etapa 3 - Criação do script e rodar a imagem em um container. 

#### Nessa etapa foi pedido a criação de um script que gerasse um hash a partir de uma string recebida pelo input.

![](/Sprint4/evidencias/script_hash.png)

#### Para criar uma hash a partir de uma string recebida por um input, precisei primeiro importar a biblioteca *hashlib*. Após isso, coloquei a variável *string* para guardar o que recebesse do input. Para gerar o hash, eu utilizei o algoritmo *sha1*, para encriptar utilizei o *encode()* na variável string. Para finalizar, eu utilizei o *hexdigest* para imprimir o resultado. Como o desafio pedia que retornasse ao passo 1 - começo do código - utilizei a estrutura While para sair somente quando o usuário quisesse. Para saber do desejo do usuário criei outro input onde pergunto se ele deseja sair ou continuar. Com a estrutura if e else eu controlo a saída ou não utilizando *break* caso ele indique que queira sair e *continue* caso ele queira continuar.

#### Após criar o script, era preciso criar o arquivo *Dockerfile*, igual fiz na etapa 1.

![](/Sprint4/evidencias/dockerHash.png)

#### Com o arquivo Dockerfile criado, é preciso dar o build e rodar a imagem criada no container com o run.

![](/Sprint4/evidencias/mascarar-dados_image.png)

![](/Sprint4/evidencias/rodando_imagemhash.png)



