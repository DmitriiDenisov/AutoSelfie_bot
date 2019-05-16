import os, sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)

from scripts.AutoSelfie_bot import AutoSelfieBot

REQUEST_KWARGS = {
    'proxy_url': 'socks5://80.211.195.141:1488',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': 'kurwaproxy',
        'password': 'x555abr',
    }
}

f = open('../token.txt', 'r')
token = f.read(100)

AutoSelfieBot(token=token, request_kwargs=REQUEST_KWARGS, model_name='unet_weights.49-val_loss0.12--0.96.hdf5.model')

# dp.add_handler(RegexHandler("English", send_cat, pass_user_data=True))
