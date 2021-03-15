Fastfox
===

**Category:** Web

**Author:**  mattyp

**Point:**

### Description
- Help me show Bob how slow his browser is!
- Site: http://web1.utctf.live:8124/

### Overview
- Truy cập trang web thì ta thấy được một chỗ input đầu vào của chúng ta. Và chúng ta có thể nhập bất kì đoạn code nào của js nếu như đoạn code đó đúng và thực thi được.

### Solution
- Ở đây mình thử nhập `console.log("Hello")` thì đầu ra của chương trình trả về cho mình là Hello. Chương trình là một sanbox ban đầu mình nghĩ là phải bypass sanbox nhưng sau khi thử 1 loạt idea thì không được. Tiếp tục mình thử gõ `help()` thì kết quả khá bất ngờ vì nó show cho mình một loạt các function.
- Điều mình chú ý ở đây là có hàm `run()` và `load()` đều dùng để chạy một file nào trả về kết quả là nội dung của file. Ở mô tả của thử thách author đã show là flag ở `/flag.txt` vì vậy bây giờ mình chỉ cần đọc nó bằng 1 trong 2 hàm ở trên.

##### Payload
- Ở đây mình sử dụng `run()` và đây cũng là giải pháp unintended vì ở hint của author đã cho libc và jsshell nhưng mình không dùng đến nó, sau khi mình giải quyết bài này thì đã pm author và nhận được intended và một CVE của firefox có thể rce
![image](https://user-images.githubusercontent.com/54855855/111030497-1e373600-8435-11eb-809a-202ef4b99eb1.png)
- `run('/flag.txt')`