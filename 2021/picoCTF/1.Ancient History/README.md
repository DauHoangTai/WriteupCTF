Ancient History
===
**Category:** Web

**Author:** MADSTACKS

### Description
I must have been sleep hacking or something, I don't remember visiting all of these sites...

### Overview
- Đầu tiên ta vào trang web thì thấy được trang web khá đơn giản chỉ có `Hello word` và kiểm tra cookie thì cũng không có gì đặc biệt. Ctrl+U để kiểm tra mã nguồn thì ta thấy được một đoạn code js khá dài và lộn xộn. Sau đó mình mang đi sài tool online để beatiful nó.

### Solution
- Sau khi beatiful nó thì ta đọc và phân tích code thì ta thấy code làm một thứ gì đó khá lằng nhằng và mình chỉ thấy nó là đoạn code rất là dài nhưng chỉ là nhiều funcion hi() lặp lại. Đọc để xem các fuction có gì khác nhau hay không thì thấy ở `urlpath` có tham số phía sau `index.html?` khác nhau.
- Ta tìm kiếm ở những cái còn lại thì thấy các tham số đó ghép lại sẽ thanh chuỗi `picoCTF`
- Và bước cuối cùng là chỉ cần ghép lại các tham số đó là chúng ta có flag