import requests

contents = requests.get('https://random.dog/woof.json').json()
url = contents['url']
a = 2