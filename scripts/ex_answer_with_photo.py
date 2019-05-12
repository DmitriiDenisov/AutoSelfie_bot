import datetime
import requests
from scripts.BotHandler import BotHandler
from telegram.bot import Bot

token = '690091700:AAFEPFkipSkqkGtOnOouBc5lEYskqQiTiaU'


# chat_id = get_chat_id(last_update(get_updates_json(url)))
# send_mess(chat_id, 'Your message goes here')

from numpy import random




greet_bot = BotHandler(token=token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()

bot = Bot(token=token)

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        photo = open('photo.png', 'rb')
        bot.send_photo(chat_id=last_chat_id, photo=photo)


        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()