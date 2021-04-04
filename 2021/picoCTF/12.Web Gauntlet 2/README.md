Web Gauntlet 2
===
**Category:** Web

**Author:** MADSTACKS
### Description
This website looks familiar...

### Overview
- Chúng ta được cấp từ author 2 url. 1 url là form đăng nhập, khi đăng nhập bằng bất kì username và password nào thì đều nhận được câu query của sql. Query hiện thị ra như sau: `SELECT username, password FROM users WHERE username='a' AND password='a'`. Vậy để truy cập được admin thì chúng ta cần cho username='admin' và comment câu query nằm sau đó.
- Url còn lại cho chúng ta biết được các kí tự sau bị filter `or and true false union like = > < ; -- /* */ admin`. Qua các filter này thì mình không thể sài `admin` và sử dụng các kí tự để comment câu query phía sau.
- Tổng length của username và password không được lớn hơn 35

### Solution
- Chương trình không filter kí tự `'` vì vậy chúng ta có thể escape nó nhưng `or and union admin` và các kí tự để comment trong sql bị filter vì vậy chúng ta không thể nối thêm câu query để chọn `' or username=admin -- -`.
- Ở hint 4 của author cung cấp cho chúng ta biết được chương trình sử dụng sqlite
- Vậy bây giờ chúng ta có thể sử dụng `'` -> escape, `||` -> nối chuỗi,`%00` -> ngắt dòng.

##### Payload
- `user=adm'||'in'%00&pass=a` và ở đây mình sử dụng burp để gửi lên chứ không gửi thẳng lên từ trang web thì khi gửi như vậy %00 sẽ được encode thêm 1 lần nữa là thành %2500 => false
- vì ở chall này giới hạn length cũng khá lớn nên có thể sử dụng làm substring
- payload sử dụng substring -> `user=adm'||'in'||substr(&pass=,0,0)||'`. Câu query khi nó run thì nó sẽ như này ![image](https://user-images.githubusercontent.com/54855855/112949168-209ecd00-9163-11eb-9264-b86d3967e6eb.png)