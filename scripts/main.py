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

AutoSelfieBot(token=token, request_kwargs=REQUEST_KWARGS, model_name='resnet_weights.17--0.95.hdf5.model')

# dp.add_handler(RegexHandler("English", send_cat, pass_user_data=True))
