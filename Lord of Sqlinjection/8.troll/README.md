troll
===
### Description
- Source:
```
<?php  
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  if(preg_match("/admin/", $_GET[id])) exit("HeHe");
  $query = "select id from prob_troll where id='{$_GET[id]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id'] == 'admin') solve("troll");
  highlight_file(__FILE__);
?>
```

### Solution
- Phân tích code: Chương trình có một tham số để input vào là `id` và filter `', admin`. Để giải quyết bài này thì kết quả trả về của id phải là `admin`.
- Ở đây có một điều nó là ở if thứ 2 preg_match filter `admin` nhưng không có modifier kèm theo vì vậy để bypass đoạn này thì chỉ cần một trong các kí tự trong admin là hoa thì có thể giải quyết

#### Payload
- `?id=Admin`