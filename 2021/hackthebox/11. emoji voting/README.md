emoji voting
===
Bài này sau khi ctf end nên mình có server nên chỉ phân tích code. Các bạn thông cảm
### Solution
- Phân tích code: Kiểm tra qua source thì chúng ta thấy được chương trình được viết bằng nodejs. Chúng ta có 2 router cần chú ý là `/api/vote` và `/api/list`. Vậy chúng ta cùng đi phân tích từng router.
+ Router `/api/vote`
![image](https://user-images.githubusercontent.com/54855855/116198895-b7f64080-a760-11eb-8426-0e10d640b466.png)
Chúng ta có một tham số có thể control đó là `id` và được gửi theo POST method