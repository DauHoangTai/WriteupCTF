Bithug
===
**Category:** Web

**Author:** ZWAD3
### Description
Code management software is way too bloated. Try our new lightweight solution, BitHug.

### Overview
- Access site ta thấy được có login và register. Minh tạo một account với username:test và password:test sau khi đăng nhập vô thì thấy có phần tạo repo giống như kiểu github bình thường hay sài.
- Thử tạo một repo kèm theo README thì chúng ta thấy hiện thị ra nội dung của README của repo mình tạo, có phần setting hiện thị tên repo, url của repo và phần webhooks. Phân user là phần add user nào đó vào chung để quản lí repo của mình khá giống github.

### Solution
- Đầu tiên phân tích code mà author cung cấp cho chúng ta. Ở folder server là một số file mà chạy ở server nên vì vậy chúng ta cần focus vào nó. Đoạn code này được viết bằng typescript
- Ở file `auth-api.ts` chúng ta thấy được đoạn code làm nhiệm vụ xác thực user
![image](https://user-images.githubusercontent.com/54855855/113099981-fca3c000-9224-11eb-9dd4-15122a5ed561.png)
Nhìn vào đoạn code, chương trình xác thực admin bằng cách check ip nên vì vậy chúng ta có thể ssrf đoạn này, điều quan trọng là cần tìm chỗ để input vào.
- File `auth.ts` có nhiệm vụ quản lí user như register, login, createToken. Mình đọc qua đoạn code này nhưng chưa thấy gì có thể khai thác ở đây
- File `git-api.ts` thì tương tác với repo của chúng ta tạo bao gồm cả webhooks. 
![image](https://user-images.githubusercontent.com/54855855/113100622-d6325480-9225-11eb-8f1e-61eba08b7efe.png)
Đoạn code lấy input của chúng ta gồm url,content type,POST data và sau đó check url của chúng ta nhập vào, bắt buộc phải là port 80 và không được nhập localhost hay 127.0.0.1 và phải là string. Có vẻ như đoạn này chúng ta có thể là filter để cho chúng ta khó ssrf
- File `git.ts` thì tạo một số function có chức năng giống như quản lí git của chúng ta và mình không thấy gì đặc biệt trong file này
- File `web-api.ts` có các router tương tác với chúng ta về phần git và cả account hay nói cách khác là ở đây xử lí trao đổi các chức năng với các file khác. 
![image](https://user-images.githubusercontent.com/54855855/113101942-83f23300-9227-11eb-85ac-2d8a5a158dcf.png)
Đoạn code này cho chúng ta biết được flag nằm trong README của repo admin => vậy chúng ta cần xác thực mình là admin hoặc một cách nào đó leo quyền cho account của mình thành admin.
- IDEA: Add user của mình vô access.conf của repo admin thông qua git push
![image](https://user-images.githubusercontent.com/54855855/113102275-024ed500-9228-11eb-9706-4878f0a175ca.png)
Ở đoạn code này(trong file git-api.ts) có fetch nên chúng ta dùng nó để có thể ssrf và fetch thì chúng ta có thể control được `URL, Content Type, POST data`
Để có payload add user thì ta sử dụng chức năng add user trong repo của chúng ta
![image](https://user-images.githubusercontent.com/54855855/113102852-c2d4b880-9228-11eb-83a1-fe955d4e522e.png)
Capture packet bằng wireshark để xem git push hoạt động gửi lên data như nào sau đó craft lại và gửi cho admin

##### Payload
- Step 1: 
Như ban đầu chúng ta đã tạo một username và password là `test`. Một repo kèm theo README là `abc`. Bây giờ chúng ta tự add user chúng ta vào chính repo của mình. Ở đây user của mình là `test`.
Đầu tiên git clone repo của mình về máy. URL nằm trong phần setting
Sau đó thực hiện tất cả các bước nằm trong ![image](https://user-images.githubusercontent.com/54855855/113104055-4511ac80-922a-11eb-9caf-b0393eb56133.png) thay `some-user-here` bằng tên user của chúng ta, ở đây của mình là `test`. Nhưng trước khi git push thì hãy bật wireshark lên để capture packet.
![image](https://user-images.githubusercontent.com/54855855/113104483-ccf7b680-922a-11eb-9562-1d42b3800af6.png)
Trong wireshark tìm http sau đó chú ý method là POST
![image](https://user-images.githubusercontent.com/54855855/113105169-7dfe5100-922b-11eb-8781-65cecbc9578d.png)
Phần 