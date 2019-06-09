from download_utils import download_models
import os

download_models('models')
os.system("unzip models/model_unet_resnet.zip -d models")
os.system("rm -r models/model_unet_resnet.zip")
os.system("rm -r models/__MACOSX")
