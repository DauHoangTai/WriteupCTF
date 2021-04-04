from re import findall, sub
import requests
import base64
import json

def decode_base64(data, altchars=b'+/'):
    data = sub(r'[^a-zA-Z0-9%s]+' % altchars, '', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += '='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

url="http://104.197.195.221:8084/"
ses = requests.Session()

while True:
	r = ses.get(url)
	data=(r.cookies["session"]).split(".")[0]
	decode_data = decode_base64(data)
	payload = json.loads(decode_data)['answer']
	data_format = " ".join(str(i) for i in payload)
	r1 = ses.post(url = url, data = {"guess":data_format})
	print(r1.text)


