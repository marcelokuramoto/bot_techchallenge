from telegram_config import Telegram_TOKEN
from telegram.ext import Updater


#Inclusão de objeto da Classe Updater linkado ao TOKEN do Bot do Telegram

updater = Updater(token=Telegram_TOKEN, use_context=True) 
dispatcher = updater.dispatcher

#Definição do processo de logs
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#Manipular resposta para mensagem /start com o bot
from telegram.ext import CommandHandler
from telegram_api import start


#CommandHandler - Manipulador de comandos do telegram (começam com /)
start_handler = CommandHandler('start', start) 
dispatcher.add_handler(start_handler)


#Manipular resposta para mensagem not command com o bot
from telegram.ext import MessageHandler, Filters
from telegram_api import echo
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()