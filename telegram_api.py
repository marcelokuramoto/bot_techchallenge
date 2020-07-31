from telegram.ext import Updater
from dialogflow import detect_intent_text
from menubanco import opcao

#Mensagem a ser enviada ao receber o comando /start no Telegram
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, sou a Tuca! Sou a robo que irá te ajudar com suas dúvidas sobre o Banco Carrefour! Me diga como posso te ajudar")

#Mensagem a ser enviada com qualquer mensagem que não seja comando
def echo(update, context):
    #Recebe a mensagem e envia para análise de Intent do DialogFlow
    #O Identificador da sessão do DialogFlow será o mesmo do Chat.ID do Telegram
    response = detect_intent_text(update.effective_chat.id,update.message.text)
    print(response)

    #Relacionamento de função a ser chamada com base na resposta da Intent identificada
    result = opcao.get(int(response))()
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)
