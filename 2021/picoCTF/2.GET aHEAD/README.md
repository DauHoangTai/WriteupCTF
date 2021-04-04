GET aHEAD
===
**Category:** Web

**Author:** MADSTACKS

### Description
Find the flag being held on this server to get ahead of the competition

### Overview
- Đầu tiên vào trang web thì chúng ta thấy được trang web có chức năng chuyển màu của background thành đỏ và xanh. Kiểm tra cookie và mã nguồn thì không có gì đặc biệt để chúng ta focus vào.
- Chú ý đến tên của challange thì mình thấy được là `GET aHEAD` vì vậy mình nghĩ đến việc thay đổi method của request gửi lên

### Solution
- Chúng ta có một số method hay dùng như PUT,POST,GET,HEAD,DELETE,... mà như tên challange thì có đề cập đến HEAD vì vậy mình dùng burp để thay đổi method request gửi lên thành HEAD và nhận được flag
