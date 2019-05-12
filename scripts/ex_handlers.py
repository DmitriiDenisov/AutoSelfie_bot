from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    update.message.reply_text('Приветсвутю тебя!')

def send_photo(update, chat_id):
    photo = open('photo.png', 'rb')
    send = update.message.reply_photo(photo=photo)
    return send


def read_photo(bot, update):
    files = update.message.photo
    if len(files) > 0:
        file = files[-1] # лучшее качество:
        # Note: For downloading photos, keep in mind that update.message.photo is an array
        # of different photo sizes. Use update.message.photo[-1] to get the biggest size.
        photo_file = bot.getFile(file)
        photo_file.download('try.jpg')
    else:
        return False


def read_doct(bot, update):
    doc = update.message.document
    if doc:
        doc_file = bot.getFile(doc)
        doc_file.download('try_doc.jpg')


def bop(bot, update): # пример для менюшки
    # url = get_url()
    custom_keyboard = [['top-left', 'top-right'],
                       ['bottom-left', 'bottom-right']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    q = bot.send_message(chat_id=update.message.chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup)
    print(q)



def docs(bot, update):
    chat_id = update.message.chat_id
    read_doct(bot, update)
    send = send_photo(update, chat_id)
    print(send)

def photos(bot, update):
    chat_id = update.message.chat_id
    read_photo(bot, update)
    send = send_photo(update, chat_id)
    print(send)

def text(bot, update):
    update.message.reply_text('Я жду фотографию')

updater = Updater('690091700:AAFEPFkipSkqkGtOnOouBc5lEYskqQiTiaU')
dp = updater.dispatcher
dp.add_handler(CommandHandler('bop', bop))
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.document, docs))
dp.add_handler(MessageHandler(Filters.photo, photos))
dp.add_handler(MessageHandler(Filters.text, text))
updater.start_polling()
updater.idle()