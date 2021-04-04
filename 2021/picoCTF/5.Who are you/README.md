Who are you?
===
**Category:** Web

**Author:** MADSTACKS

### Description
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn

### Overview
- Đầu tiên vào site thì chúng ta thấy được có một image kèm theo một dòng mô tả.

### Solution
Sử dụng Burp Suite để giải quyết bài này
- Step 1: Ở bức hình đầu tiên có kèm theo mô tả có thể hiểu đại loại là chỉ cho user là `PicoBrowser` có thể truy cập vì vậy chúng ta chỉ cần sửa trong Burp phần header `User-Agent: PicoBrowser`
- Step 2: Nhận được mô tả `I don't trust users visiting from another site.` Vì vậy chúng ta thêm header `Referer:mercury.picoctf.net:38322`
- Step 3: Chúng ta thấy `I dont trust users who can be tracked.` vì vậy sử dụng header `DNT:1`
- Step 4: Nhận được thông báo `This website is only for people from Sweden.` -> sử dụng `X-Forwarded-For:2.71.2.7`
- Step 5: Nhận được `You're in Sweden but you don't speak Swedish?` vì vậy thay đổi `Accept-Language:sv-SE`
Đó là tất cả để nhận được flag