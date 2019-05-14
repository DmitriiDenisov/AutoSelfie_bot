import PIL.Image
import cv2
import numpy as np


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


def resize_image(image, target_shape):
    img = image.resize(target_shape, PIL.Image.ANTIALIAS)
    return img


def get_closest(photos, desired_size):
    def diff(p): return p.width - desired_size[0], p.height - desired_size[1]

    def norm(t): return abs(t[0] + t[1] * 1j)
    return min(photos, key=lambda p:  norm(diff(p)))


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


def predict(model, val_image, graph):
    if len(val_image.shape) == 3:
        val_image = np.expand_dims(val_image, axis=0)

    with graph.as_default():
        pred_mask = model.predict(val_image, verbose=1)
    pred_mask = np.round(pred_mask[0] * 255, 0).astype(np.uint8)
    val_image = np.round(val_image[0] * 255, 0).astype(np.uint8)
    # val_image = np.concatenate([val_image[:, :, 2].reshape(val_image.shape[:2] + (1,)),
    #                             val_image[:, :, 1].reshape(val_image.shape[:2] + (1,)),
    #                             val_image[:, :, 0].reshape(val_image.shape[:2] + (1,))], axis=2)

    pred_mask = np.squeeze(pred_mask)
    pred_mask_red = np.zeros(pred_mask.shape + (3,), np.uint8)
    pred_mask_red[:, :, 0] = pred_mask.copy()
    blended_image = cv2.addWeighted(pred_mask_red, 1, val_image, 1, 0)
    return blended_image
