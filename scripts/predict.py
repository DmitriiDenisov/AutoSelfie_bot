import cv2
from keras.engine.saving import load_model
import numpy as np


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
