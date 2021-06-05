zombie assassin
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect();
  $_GET['id'] = strrev(addslashes($_GET['id']));
  $_GET['pw'] = strrev(addslashes($_GET['pw']));
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_zombie_assassin where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) solve("zombie_assassin"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: chương trình có 2 tham số để chúng ta input vào là `id` và `pw`. Hàm `strrev` có tác dụng đảo ngược các kí tự trong đầu vào của chúng ta còn hàm `addslashes` để filter các kí tự `', ", \, NUll` nếu có các kí tự đó trong đầu vào thì sẽ thêm kí tự `\` vào phía trước.
- Ở bài này giống như bài trước chúng ta có thể sử dụng `chuỗi trích dẫn đơn` để thêm query vào query gốc nhưng ở bài này nếu ở id nhập vào là `\` thì id tự động chuyển thành `\\` vì có hàm `addslashes`. Nhưng nếu chúng ta nhập vào null là `%00` thì id sẽ thành `0\`
như vậy nó đã thành chuỗi trích dẫn đơn và chúng ta có thể thêm query mới vào.

#### Payload
- `?id=%00&pw=- --1=1 ro`
`- --1=1 ro` vì sau khi chương trình đảo kí tự thì sẽ thành `or 1=1-- -`