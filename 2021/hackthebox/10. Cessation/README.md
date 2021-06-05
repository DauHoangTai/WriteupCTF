Cessation
===
### Description
Enemy forces are using a stealthy device to penetrate into our country. We've identified its origin and its time cessate their strength and defend our country from the attack.

### Solution
Ở bài này chúng ta chỉ được cung cấp một file 
- Phân tích code: `regex_map` lọc nếu có path là 403 hoặc shutdown thì sẽ bị access denine. Vì vậy mình đã tìm hiểu xem regex_map có thể bypass nó không thì phát hiện được bài viết này https://github.com/apache/trafficserver/issues/3259. Chỉ cần sử dụng nhiều dấu `/` thì có thể bypass nó và access thành công.

### Payload
`//////shutdown`
![image](https://user-images.githubusercontent.com/54855855/115968321-8a8f7400-a561-11eb-8cb0-45e373fb1caf.png)