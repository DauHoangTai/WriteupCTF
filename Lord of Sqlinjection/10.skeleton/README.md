skeleton
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("skeleton"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tich code: Chương trình có đầu vào để chúng ta nhập là `pw`. Để giải quyết được bài này thì kêt quả trả về của id phải là admin. Nếu nhập bình thường câu query sẽ không bao giờ trả về được `admin` hoặc thậm chí là `guest` vì điều kiện ở where cần phải đúng pw và 1=0 mà 1=0 thì luôn sai vì vậy câu query này luôn sai
- Để câu query này có thể đúng thì chúng ta phải ngắt câu query phía sau bằng cách là các dâu comment tróng sql

#### Payload
- `?pw=' or 1=1 and id='admin'-- -`