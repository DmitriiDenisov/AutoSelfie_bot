import PIL
import PIL.Image
import numpy as np
from keras.models import load_model
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from scripts.metrics import dice_coef_K, my_dice_metric
from scripts.predict import predict

model = load_model('../models/resnet_weights.17--0.95.hdf5.model',
                   custom_objects={'dice_coef_K': dice_coef_K, 'my_dice_metric': my_dice_metric})
print('Model read!')


def resize_image(image, target_shape):
    img = image.resize(target_shape, PIL.Image.ANTIALIAS)
    return img


def get_closest(photos, desired_size):
    def diff(p): return p.width - desired_size[0], p.height - desired_size[1]
    def norm(t): return abs(t[0] + t[1] * 1j)
    return min(photos, key=lambda p:  norm(diff(p)))

def start(bot, update):
    update.message.reply_text('Приветсвутю тебя!')

def send_photo(update, chat_id):
    photo = open('photo.png', 'rb')
    send = update.message.reply_photo(photo=photo)
    return send

def send_photo_2(update, predicted_image):
    send = update.message.reply_photo(photo=predicted_image)
    return send


def read_photo(bot, update):
    files = update.message.photo
    if len(files) > 0:
        file = get_closest(files, desired_size=(320, 240))
        # file = files[-1] # лучшее качество:
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


#@send_action(ChatAction.TYPING)
def bop(bot, update): # пример для менюшки = customKeyboard
    custom_keyboard = [['top-left', 'top-right'],
                       ['bottom-left', 'bottom-right']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    q = bot.send_message(chat_id=update.message.chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup)
    print(q)



def docs(bot, update):
    chat_id = update.message.chat_id

    bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING) # добавляем эффект typing

    read_doct(bot, update)
    send = send_photo(update, chat_id)
    print(send)

def photos(bot, update):
    chat_id = update.message.chat_id
    read_photo(bot, update)
    image = PIL.Image.open('try.jpg')
    resized_img = np.array(resize_image(image, (240, 320)))
    prediction = predict(model, resized_img)
    predicted_image = PIL.Image.fromarray(prediction, 'RGB')
    send = send_photo_2(update, predicted_image)
    print(send)

def text(bot, update):
    chat_id = update.message.chat_id
    reply_markup = ReplyKeyboardRemove() # удаляем custom Keyboard
    bot.send_message(chat_id=chat_id, text="I'm back.", reply_markup=reply_markup)
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