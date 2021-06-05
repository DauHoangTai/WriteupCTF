succubus
===
### Description
- Source:
```
<?php
  include "./config.php"; 
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/\'/',$_GET[id])) exit("HeHe");
  if(preg_match('/\'/',$_GET[pw])) exit("HeHe");
  $query = "select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) solve("succubus"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Chương trình có 2 tham số để chúng ta input vào đó là `id` và `pw` và đều được filter kí tự `'`. Nếu có `id` có kết quả trả về thì sẽ giải quyết được bài này. Quan trọng ở đây là chương trình đã filter kí tự `'` vì vậy chúng ta không thể thoát id hoặc pw nhưng có một cách để biến query từ id tới and pw thành một chuỗi đó là cách `chuỗi trích dẫn đơn` bằng cách sử dụng kí tự `\`
- Debug : ![image](https://user-images.githubusercontent.com/54855855/109967044-85613600-7d23-11eb-8b17-8ccc324e4b12.png)

#### Payload
- `?id=\&pw=or 1=1-- -`