Sea of Quills
===
**Category:** Web

**Author:** JoshDaBosh

**Point:**
### Description
- Come check out our finest selection of quills! 
- Site: `https://seaofquills.2021.chall.actf.co/`
- Source: `app.rb`

### Overview
Site khá là đơn giản có chức năng show ra các bút lông và ở phần `/quills` thì có chức năng tìm kiếm bút lông theo số lượng (Amount) mình nhập vào và bắt đầu từ cái thứ bao nhiêu (Starting from).

### Solution
- Phân tích code: Chúng ta có một file `app.rb` do author cung cấp cho chúng ta. File này được viết bằng ruby.
![image](https://user-images.githubusercontent.com/54855855/113993444-af57cc00-987e-11eb-94ab-0557bb0a7d25.png)
Ở đoạn code này nó sử dụng DB là `quills.db` và câu query là `select * from quills` -> lấy tất cả các item có trong table quills.
![image](https://user-images.githubusercontent.com/54855855/114018416-695b3200-9897-11eb-9f4a-e7f1cffafd8d.png)
Ở đoạn code này thì chương trình vẫn sử dụng DB là `quills.db`. Ở đây có 3 tham số để chúng ta nhập vào là `cols, lim, off` và đầu vào được lọc bởi blacklist `["-", "/", ";", "'", "\""]` bằng cách sử dụng hàm include. Tham số `lim` và `off` mặc định là phải là number nếu không phải là number thì chương trình sẽ in ra `bad, no quills for you!` và kết thúc chương trình
Câu query của chương trình là `select %s from quills limit %s offset %s" % [cols, lim, off]`. Ở đây chúng ta thì có thể sử dụng tham số `cols` để control query này vì đã nói như trên lim và off phải bắt buộc là number
Ở ngoài trang web thì chỉ có 2 chỗ chúng ta input vào nhưng trong code thì chúng ta thấy được là có 3 tham số vì vậy chúng ta sử dụng burpsuite để có thể gửi 3 tham số.
nếu chúng ta gửi với `limit=1&offset=1&cols=sqlite_version()%00` thì câu query sẽ thành
```sql 
select sqlite_version()%00 from quills limit 1 offset 1
```
%00 (null byte) nó sẽ hiểu là đến đây đã là hết câu query và phần query phía sau sẽ không được thực hiện (giống như các dấu comment).
Kết quả hiện thị ra version của sqlite
![image](https://user-images.githubusercontent.com/54855855/114020012-4d589000-9899-11eb-9147-f2f73244f7af.png)

##### Payload
- Lấy comlumn name có trong DB -> `limit=1&offset=1&cols=sql+FROM+sqlite_master%00`
![image](https://user-images.githubusercontent.com/54855855/114020661-0919bf80-989a-11eb-89d5-0a560d3dbb97.png)
Có một table name là `flagtable` và một cột là `flag`
Vậy bây giờ đọc flag
`limit=1&offset=1&cols=flag+from+flagtable%00`