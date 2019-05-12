from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id

    photo = open('photo.png', 'rb')
    bot.send_photo(chat_id=chat_id, photo=photo)



updater = Updater('690091700:AAFEPFkipSkqkGtOnOouBc5lEYskqQiTiaU')
dp = updater.dispatcher
dp.add_handler(CommandHandler('bop', bop))
updater.start_polling()
updater.idle()