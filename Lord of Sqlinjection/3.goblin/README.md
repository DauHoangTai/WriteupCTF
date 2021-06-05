goblin
===
### Description
- Source
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Bài này chúng ta chỉ có một tham số để nhập vào đó là `no`, ở preg_match đầu tiền nó được filter với mục đích như các bài ban đầu, ở preg_match thứ 2 nó được filter các dấu `',"`. Nó mặc định sẽ lấy id ở guest nhưng muốn solves chall này thì kết quả của id trả vể phải là admin
- Chúng ta có thể thêm một điều kiện ở `no` để câu query nó vừa select id tại guest và tại id ở admin nhưng nó đã filter dấu `' và "` vì vậy không thể id = "admin" hoặc id = 'admin'. Nhưng ta có thể hex `admin` vì vậy có thể không cần sử dụng `' và "` ở `no`

#### Payload
- `2 or id = 0x61646d696e`