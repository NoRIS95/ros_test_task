import requests
import json
import os
import yaml

CURRENT_DIR = os.path.dirname(__file__)

with open(os.path.join(CURRENT_DIR, '../src/config.yml'), "r") as yamlfile:
    CONFIG = yaml.load(yamlfile, Loader=yaml.FullLoader)

LISTENER_HOST = CONFIG['LISTENER_HOST']
LISTENER_PORT = CONFIG['LISTENER_PORT']


LISTENER_URL = f'http://{LISTENER_HOST}:{LISTENER_PORT}'

if __name__ == '__main__':
	requests.post(LISTENER_URL+'/info', json.dumps({'data': 'Hello, World!'}))