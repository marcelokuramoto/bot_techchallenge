#Dictionary de funções de opções de atuação do banco em resposta a identificação de intent do dialogflow
def default_error():
    texto = "Desculpe, não entendi o que voce deseja. Peço para que nos acione pelas nossas outras vias de contato \nSão Paulo e Regiões Metropolitanas\n3004 2222 \nDemais Localidades \n0800 718 2222"
    return texto

def saudacoes():
    texto = "Olá, sou a Tuca! Sou a robo que irá te ajudar com suas dúvidas sobre o Banco Carrefour! Me diga como posso te ajudar"
    return texto

def fatura():
    texto = "Opa! Estou te reedirecionado para voce acessar sua fatura do cartão de crédito \n "
    #Chamar interface para fatura no app do Carrefour
    return texto

def solicitar_cartao():
    texto = "Entendi! Clique no link abaixo para ir a nossa página para criação de novo cartão \n https://aquisicao.carrefoursolucoes.com.br/"
    return texto
    #Chamar interface para cadastrar cliente com input de CPF e nome do usuario

def aumentar_credito():
    texto = "Ok, entendi! Irei te redirecionar para o nosso serviço de análise de crédito"
    return texto
     #Chamar interface para análise de credito no app do Carrefour

def detalhes():
    texto = "Legal! Para conhecer melhor os serviços e soluções do banco Carrefour, clique no link abaixo: \n https://www.carrefoursolucoes.com.br/cartao/beneficios"
    return texto

opcao = {
    0 : default_error,
    1 : saudacoes,
    2 : fatura,
    3 : solicitar_cartao,
    4 : aumentar_credito,
    5 : detalhes
}

