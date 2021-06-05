Cobolt
===
### Description
- Source
```
<?php
  include "./config.php"; 
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("cobolt");
  elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Chúng ta có 2 tham số để nhập vào đó là `id` và `pw`, cả hai đều được filter như bài trước không có gì mới. Nếu như `id` trả về là `admin` chúng ta có thể solves. Nếu không sẽ in ra `Hello {kết quả của id} You are not admin`. Điều đặc biệt ở đây là `pw` sau khi được nhập vô được md5 vì vậy chúng ta không thể cho `id = admin` và `pw = true` được.
- Chúng ta có thể id = admin và comment đoạn query sau để câu query chỉ select id chỉ có một điều kiện là tại `id = admin`

#### Payload
- `?id=admin'-- -`