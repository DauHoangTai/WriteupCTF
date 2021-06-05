wolfman
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); 
  $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("wolfman"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Chúng ta có một tham số để input vào đó là `pw` nếu có khoảng trắng trong đầu vào thì sẽ thoát và in ra `No whitespace ~_~`.
- Chúng ta có thể bypass khoảng trắng bằng nhiều cách. Sử dụng `/**/, %0a, %09, %0d, (), +`.
- Ở đây mình sử dụng `%09`

#### Payload
- `?pw=1'%09or%09id='admin'--%09-`