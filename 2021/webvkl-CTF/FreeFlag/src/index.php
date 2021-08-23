<?php
session_start();
include_once("config.php");
if (isset($_SESSION['username'])) {
	if (isset($_GET['id'])) {
		$id = $_GET['id'];
		if (preg_match("/insert|substr|mid|left|right|ord|pi|chr|sys|0x|version|concat|ascii|convert|and|or|procedure|xml|extract|by|create|like|sleep|if|case|db|load|to|count|where|column|rand|in|[1-9`~.^\-\/\\\=<>|$]/i",$id)) {
			die("nope !");
		} else {
			$query1 = "SELECT * FROM numbers where id = {$id};";
			$result = $conn->query($query1);
			while ($row = $result->fetch_assoc()) { //db 2 column
				$number = $row['number'];
				// echo $number;
				if ((int)$number === 2050 || (int)$number === 2051) {
					$_SESSION["admin"] = true;
					header("Location: flag.php");
				}
				else {
					die("Try harder :) ");
				}
			}
		}
	} else {
		highlight_file(__FILE__);
	}
} else {
	header("Location: login.php");
}
?>
