Cutest Cookie Clicker Rip-Off!
===

**Category:** Web

**Author:**  Aya Abdelgawad

**Point:**

### Description
- I built this awesome game based off of cookie clicker! Bet you'll never beat my high score. Hehehe!
- Site: http://web1.utctf.live:4270/

### Overview
- Đầu tiên vào site ta thấy một nút botton nếu click vào thì sẽ được tăng điểm của bạn. Điểm sẽ được hiện thị ở Your Score và chúng ta chỉ có thời gian là 30s để thực hiện. Nếu vượt qua điểm cao nhất thì sẽ có flag. Điểm cao nhất là 1,000,000

### Solution
- Chúng ta không thể click thủ công mà trong 30 mà số điểm của chúng ta lại lớn hơn 1,000,000 được vì vậy chúng ta phải tìm cách nào đó vượt qua.
- Kiểm tra cookie thì ta thấy được có một cookie tên highScore, chúng ta thử thay đổi nó lớn hơn 1,000,000 và đợi sau 30s kết thúc thì có flag trả về

##### Payload
- Ở đây mình sử dụng edit this cookie 
- ```highScore=2000000```