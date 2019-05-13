import PIL
import PIL.Image
import numpy as np
from keras.models import load_model
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatAction, InlineKeyboardMarkup
from io import BytesIO
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from scripts.metrics import dice_coef_K, my_dice_metric
# from scripts.predict import predict
# import tensorflow as tf

# model = load_model('../models/resnet_weights.17--0.95.hdf5.model',
#                   custom_objects={'dice_coef_K': dice_coef_K, 'my_dice_metric': my_dice_metric})
# model._make_predict_function()
# graph = tf.get_default_graph()
print('Model read!')

all_users = {}

def write_log(update):
    with open('../data/logs.txt', 'a') as text_file:
        try:
            if update.message.text:
                text_file.write('{chat_id},{username},{first_name},{second_name},{text},,,{date}\n'.format(chat_id=update.message.chat.id,
                username=update._effective_user.username, first_name=update._effective_user.first_name,
                second_name=update._effective_user.last_name, text=update.message.text, date=update.message.date))
            elif update.message.photo:
                text_file.write('{chat_id},{username},{first_name},{second_name},,{photo},,{date}\n'.format(chat_id=update.message.chat.id,
                username=update.message.chat.username, first_name=update.message.chat.first_name,
                second_name=update.message.chat.last_name, photo=1, date=update.message.date))
            elif update.message.document:
                text_file.write('{chat_id},{username},{first_name},{second_name},,,{doc},{date}\n'.format(chat_id=update.message.chat.id,
                username=update.message.chat.username, first_name=update.message.chat.first_name,
                second_name=update.message.chat.last_name, doc=update.message.document.file_name, date=update.message.date))
        except:
            print('Error in logging')

def button(bot, update):
    query = update.callback_query
    all_users[update.effective_chat.id]['language'] = query.data
    if query.data == 'English':
        query.edit_message_text(text="Selected English language")
    else:
        query.edit_message_text(text="Выбран Русский язык")


def resize_image(image, target_shape):
    img = image.resize(target_shape, PIL.Image.ANTIALIAS)
    return img


def get_closest(photos, desired_size):
    def diff(p): return p.width - desired_size[0], p.height - desired_size[1]
    def norm(t): return abs(t[0] + t[1] * 1j)
    return min(photos, key=lambda p:  norm(diff(p)))


def start(bot, update):
    first_name = update.effective_user.first_name
    update.message.reply_text('Hi {}!'.format(first_name))
    all_users[update.message.chat_id] = {'first_name': first_name}

    custom_keyboard = [['English'], ['Russian']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    q = bot.send_message(chat_id=update.message.chat_id,
                     text="Choose language:",
                     reply_markup=reply_markup)

    write_log(update)
    a = 2
    # return LANG
    #q = bot.send_message(chat_id=update.message.chat_id,
    #                 text="Please choose language:",
    #                 reply_markup=reply_markup,
    #                resize_keyboard=True)
    #print(q)


def read_photo_doc(bot, update):
    files = update.message.photo
    if len(files) > 0:
        file = get_closest(files, desired_size=(320, 240))
        # file = files[-1] # лучшее качество:
        # Note: For downloading photos, keep in mind that update.message.photo is an array
        # of different photo sizes. Use update.message.photo[-1] to get the biggest size.
        photo_file = bot.getFile(file)
        photo_file.download('../data/try.jpg')
        return True
    doc = update.message.document
    if doc:
        doc_file = bot.getFile(doc)
        doc_file.download('../data/try.jpg')
        return True
    return False


def photos(bot, update):
    write_log(update)
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id=chat_id, action=ChatAction.UPLOAD_PHOTO)  # добавляем эффект загрузки фото
    read_photo_doc(bot, update)
    try:
        image = PIL.Image.open('../data/try.jpg')
    except:
        if all_users[update.message.chat_id]['language'] == 'English':
            update.message.reply_text('I can not read you doc')
        else:
            update.message.reply_text('Не могу прочитать ваш документ')
        return False
    resized_img = np.array(resize_image(image, (240, 320))) / 255
    prediction = predict(model, resized_img, graph)
    predicted_image = PIL.Image.fromarray(prediction)

    bio = BytesIO()
    bio.name = 'image.jpeg'
    predicted_image.save(bio, 'JPEG')
    bio.seek(0)
    update.message.reply_photo(photo=bio)
    # send = send_photo(update, bio)
    # print(send)
    return True


def text(bot, update):
    chat_id = update.message.chat_id
    if update.message.text == 'English':
        all_users[chat_id]['language'] = 'English'
        update.message.reply_text('You chosed English language')
        default_state(bot, update)
        return True
    elif update.message.text == 'Russian':
        all_users[chat_id]['language'] = 'Russian'
        update.message.reply_text('Ты выбрал Русский язык')
        default_state(bot, update)
        return True
    elif update.message.text == 'Описание':
        update.message.reply_text('Пришли в чат своё селфи, а бот вырежет тебя на фотографии')
        return True
    elif update.message.text == 'Github проекта':
        update.message.reply_text('Ссылка: https://github.com/DmitriiDenisov/AutoSelfie_bot')
        return True
    elif update.message.text == 'Автор':
        update.message.reply_text('Автор: @DmitriiDenisov')
        return True
    elif update.message.text == 'Description':
        update.message.reply_text('Send to chat your selfie, and the bot will cut you on the photo')
        return True
    elif update.message.text == 'Github project':
        update.message.reply_text('Link: https://github.com/DmitriiDenisov/AutoSelfie_bot')
        return True
    elif update.message.text == 'Author':
        update.message.reply_text('Author: @DmitriiDenisov')
        return True
    else:
        if all_users[update.message.chat_id]['language'] == 'English':
            update.message.reply_text('I am waiting for a photo')
        else:
            update.message.reply_text('Я жду фотографию')


def default_state(bot, update):
    if all_users[update.message.chat_id]['language'] == 'Russian':
        custom_keyboard = [['Описание'], ['Github проекта', 'Автор']]
        text = "Можешь выбрать действие или прислать фото"
    else:
        custom_keyboard = [['Description'], ['Github project', 'Author']]
        text = "You can choose an action or send a photo"

    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    bot.send_message(chat_id=update.message.chat_id,
                         text=text,
                         reply_markup=reply_markup)


REQUEST_KWARGS={
    'proxy_url': 'socks5://80.211.195.141:1488',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': 'kurwaproxy',
        'password': 'x555abr',
    }
}


f = open('../token.txt', 'r')
token = f.read(100)
updater = Updater(token, request_kwargs=REQUEST_KWARGS)
dp = updater.dispatcher


#dp.add_handler(conv_handler)
dp.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
dp.add_handler(MessageHandler(Filters.document, photos))
dp.add_handler(MessageHandler(Filters.photo, photos))
dp.add_handler(MessageHandler(Filters.text, text))

# dp.add_handler(RegexHandler("English", send_cat, pass_user_data=True))
updater.start_polling()
updater.idle()

# df = pd.read_csv('../data/logs.txt', sep=",", header=0)
