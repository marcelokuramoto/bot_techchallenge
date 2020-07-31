@Author: Marcelo Kuramoto
Data: 29/07/2020

Projeto realizado em resposta ao Tech Challenge fornecido pela Digital One Innovation em parceria
com o Carrefour. Segue abaixo enunciado do desafio:

"Crie uma solução (use a sua criatividade) para resolver o desafio abaixo:

Criar uma solução técnica que otimize a comunicação entre clientes e Banco Carrefour com os seguintes critérios:

Utilizar .NET ou Python
Utilizar Angular (opcional), caso tenha front-end
Utilizar a API do Telegram"

-----------### Preparando o Ambiente ###--------------

1.PIP - Gerenciador de Pacotes de Python - https://pypi.org/

2.Telegram BOT API em Python - https://github.com/python-telegram-bot/python-telegram-bot
    2.1 - Comando $ pip install python-telegram-bot

3. API do DialogFlow com Python - https://github.com/googleapis/dialogflow-python-client-v2 
    3.1 - Comando pip install dialogflow
    3.2 - TUtorial: https://cloud.google.com/dialogflow/docs/quick/api#detect-intent-text-python 

-----------### Fluxograma do Projeto ###---------------
1. Foi utilizado a linguagem Python para o desenvolvimento da solução e buscou-se a seguinte estratégia para
atendimento do problema proposto:

2.A Interface de comunicação será realizada pelo própria estrutura do Telegram através de um Bot. 
O Bot é chamado DIO_CarrefourTechChallenge.

3.As informações/mensagens transmitidas ao Bot serão analisadas pela ferramenta DialogFlow da google. 
Partindo da ferramenta, será avaliado qual a intenção desejada pelo cliente a partir da Inteligencia
Artifical existente na ferramenta. 

4.Com a intenção identificada, será devolvido pelo DialogFlow uma resposta padronizada que utilizaremos
com o Dictionary "opcao" existente no arquivo menubanco.py para definir qual ação será chamada pelo programa.

5.Com base na função chamada, será retornado uma mensagem ao Telegram para o cliente e algumas páginas de 
referencia para continuação do serviço. Nota: É possível aprimorar essa conexão com as continuações do serviço
comunicando diretamente com o Aplicativo ou ao site do Carrefour.

*Obs: O menu de opcoes definido no Dictionary "opcao" em menubanco.py pode ser aumentado , bem como a quantidade 
de Intent do DialogFlow possibilitando maiores alteranativas de serviço para o cliente.
