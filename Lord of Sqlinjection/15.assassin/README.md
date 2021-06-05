assassin
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_assassin where pw like '{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("assassin"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Chương trình có một tham số đầu vào là `pw` và chỉ filter một kí tự `'`. Nhưng ở câu query của bài này có điều đặc biệt là sử dụng `like` thay vì `=`. Function `like` ở sql chúng ta có thể sử dụng để tìm kiếm một mẫu chỉ định trong cột và nó có 2 kí tự đại diện là `%` và `_`. Ở đây mình sử dụng `%` để brute pw của admin
- VD: `select * from demo where id like 'a%'` ở query này nếu id có các từ bắt đầu bằng `a` nó sẽ được hiện thị ra.

#### Payload
- Ở đây mình sử dụng intruder ở burp `?pw=$$%`