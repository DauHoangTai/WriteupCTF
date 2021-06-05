Gremlin
===
### Desscription
- Source 
```
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); // do not try to attack another table, database!
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']) solve("gremlin");
  highlight_file(__FILE__);
?>
```

### Solution
- Phân tích code thì ta thấy , chúng ta có tham số để nhập vào là `id` và `pw`, cả 2 đều được filter giống nhau để tránh chúng ta attack vào các table khác như author comment. vì `id` và `pw` được truyền thẳng vào câu query nên chúng ta có thể injection vô cả 2. Sau đó in ra câu query của mình nhập vào. Chỉ cần có kết quả của id được trả về thì có thể solves.
- Chúng ta chỉ cần cho select tại `id = 1` và `pw thành true`.

#### Payload: `?id=1&pw='or 1=1-- -`