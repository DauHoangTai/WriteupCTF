giant
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
  if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 
  $query = "select 1234 from{$_GET[shit]}prob_giant where 1"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result[1234]) solve("giant"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Chương trình có một tham số để chúng ta input vào đó là `shit`. Đầu vào được check nếu length > 1 thì thoát chương trình. `shit` được filter các kí tự `%20, \n, \r, \t`. Câu query của chương trình bị dính nhau vì vậy ở đầu vào `shit` chúng ta cần một khoảng trắng để chạy được câu query này. Nếu query trả về kết quả ở 1234 thì sẽ giải quyết được bài này.
- Chúng ta có một số kí tự để thay thế khoảng trắng như: `%20`->` `, `%0a`->`\n`, `%0d`->`\r`, `%09`->`\t` nhưng hầu hết mấy kí tự này đều bị filter nhưng chúng ta có thể sử dụng `%0b` hoặc `%0c` để thay thế khoảng trắng

#### Payload
- `?shit=%0b`