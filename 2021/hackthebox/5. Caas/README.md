Caas
===
### Description
cURL As A Service or CAAS is a brand new Alien application, built so that humans can test the status of their websites. However, it seems that the Aliens have not quite got the hang of Human programming and the application is riddled with issues.

### Overview
Trang web đang hiện thị giống như 1 cái terminal và đang chạy lệnh curl
Chúng ta được cung cấp source code của chương trình nên chúng ta sẽ phân tích nó.

### Solution
- Phân tích code: Chương trình được viết bằng php và deploy theo mô hình MVC. Vậy nên chúng ta hãy focus vào controller và models.
Ở file `CurlController.php` ![image](https://user-images.githubusercontent.com/54855855/115953823-e9300000-a517-11eb-986f-33ab93d4ddfb.png) nhận đầu vào là tham số `ip` sau đó gán cho biến `url` và tiếp tục được chuyển vào class `CommandModel` ở models để xử lí. Cuối cùng ở trong class này có hàm exec để thực thi cái input của mình
Ở file `CommandModel.php` ![image](https://user-images.githubusercontent.com/54855855/115953894-5e9bd080-a518-11eb-96d4-90a3aad594d1.png)
Nó có một magic function là `__construct` khi chạy chương trình thì nó sẽ được khởi tạo và lệnh này `curl -sL " . escapeshellcmd($url)` sẽ được gán vào biến command sau đó hàm exec bên dưới sẽ thực hiện và trả về output cho chúng ta.
- Vì chương trình này đang sài curl chạy ở localhost chính là server của chall và không kiểm tra đầu vào của chúng ta nên vì vậy chúng ta chỉ cần đọc trực tiếp file ở server bằng tham số `--data` và gửi về server của mình 

### Payload
Ở đây mình sử dụng burp để thực hiện.
![image](https://user-images.githubusercontent.com/54855855/115954725-bc321c00-a51c-11eb-8566-3c696d0632d9.png)

### Flag
`CHTB{f1le_r3trieval_4s_a_s3rv1ce}`