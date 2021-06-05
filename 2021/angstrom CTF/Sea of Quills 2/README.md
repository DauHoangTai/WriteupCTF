Sea of Quills 2
===
**Category:** Web

**Author:** JoshDaBosh

**Point:**
### Description
- A little bird told me my original quills store was vulnerable to illegal hacking! I've fixed my store now though, and now it should be impossible to hack!
- Site: `https://seaofquills-two.2021.chall.actf.co/`
- Source: `app.rb`

### Overview
Chall này ở bài trước đều không khác gì về site và folow của chương trình cũng giống như bài v1.

### Solution
- Phân tích code: Ở bài này thì các tham số và các câu query đều như bài v1. Chỉ khác ở một chỗ là blacklist sẽ có thêm cả chữ `flag` -> `blacklist = ["-", "/", ";", "'", "\"", "flag"]`
Ở phần check `lim` và `off` có phải là number hay không thì ở đây có thêm check length của `cols` > 24 cũng false.
Còn câu query execute thì vẫn như bài v1.
Do nó lọc đầu vào của chúng ta bằng `include` và `include` thì sẽ phân biệt là chữ hoa hay chữ thường nên vì vậy chúng ta có thể bypass được blacklist trên.
VD: Nếu là `flag` => true nhưng nếu là `Flag` => false

##### Payload
Vì payload bài 1 của mình sử dụng < 24 kí tự nên bài này mình quyết định sử dụng bài payload đó để solved
`limit=1&offset=1&cols=sql+from+sqlite_master%00` -> lấy comlumn có trong DB
Vẫn là có cột là `flag` trong tablename là `flagtable`
`limit=1&offset=1&cols=Flag+from+Flagtable%00` -> lấy flag