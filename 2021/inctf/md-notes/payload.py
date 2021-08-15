from Crypto.Util.number import *
import requests
modul=99999999999
a=245
c=143
post_id=90462233978
for i in range(10000):
    tmp=post_id-c
    seed=tmp*inverse(a,modul)%modul
    print(seed)
    post_id=seed
    url="http://web.challenge.bi0s.in:5432/b5cd7ae0-7b50-7ae0-7ae0-47a03b473015"
    r=requests.get(url+f"/{post_id}")
    if "not found" not in r.text: #and "name" not in r.text and "<script>fetch(" not in r.text
        print(r.text)
        break
