import os, sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
import time
from scripts.main import main

server = {}
with open(os.path.join(PROJECT_PATH, 'server_parameters.txt')) as f:
    host_name = f.read()

response = os.system("ping -c 1 " + host_name)
print('Trying to connect...')

while True:
    if response == 0:
      time.sleep(5)
      response = os.system("ping -c 1 " + host_name)
    else:
      print(host_name, 'Server is down!')
      break

main()
