vampire
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  $_GET[id] = strtolower($_GET[id]);
  $_GET[id] = str_replace("admin","",$_GET[id]); 
  $query = "select id from prob_vampire where id='{$_GET[id]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("vampire"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Ở bài này chúng ta có đầu vào là `id` và chương trình filter `'` và sau đó chuyển tất cả các kí tự đầu vào thành in thường tiếp tục kiểm tra trong đầu vào mà có admin thì sẽ thay thế bằng `""`. Để giải quyết bài này kết quả trả về của id phải là admin
- Nếu như không có `strtolower` thì chúng ta có thể bypass `str_replace` bằng cách ở đầu vào ta chỉ cần nhập đó là chuỗi hoa hoặc bất kì kí tự nào trong chuỗi là kí tự hoa.
- Ở đây do có strtolower nên vì vậy chúng ta phải tìm một chuỗi sau khi bị replace nhưng sau đó kết quả vẫn là admin

#### Payload
- `?id=adadminmin`