<?php
session_start();
include_once("config.php");
$stmt = $conn->prepare('select * from users where username=?');
if (!$stmt)
	throw new Exception("prepare query error:" . $conn->error);
$stmt->bind_param('s', $_SESSION['username']);
$stmt->execute();
$result = $stmt->get_result();
while ($row = $result->fetch_assoc()) {
	$checkStar = $row['star'];
}
if ($checkStar >= 100) {
	if (isset($_GET['pass'])) {
		$pass = $_GET['pass'];
		if (preg_match("/user|insert|ord|chr|version|len|mid|like|right|substr|exp|cur|ascii|=|and|or|0x|between|rand|convert|sleep|xml|extract|concat|info|sys|[0-9~\/\"<>!^;\\\]/i",$pass)) {
			die("no hack");
		} else {
			// $query = "SELECT flag_ne_hihi FROM flag_here;";
			$query = "SELECT pass FROM users1 where user = 'guest' and pass = '{$pass}';";
			$result = @mysqli_fetch_array(mysqli_query($conn,$query));
			if($result['pass']) {
				// echo "wtf ?";
			}
		}
	} else {
		highlight_file(__FILE__);
	}
} else {
	die ("<script>alert('Not enough stars :( min 100 stars')</script>");
}
?>