<?php
error_reporting(0);
include "config.php";

if (isset($_POST['VietNam'])) {
	$VN = $_POST['VietNam'];
	if (filter($VN)) {
		die("nope!!");
	}
	if (!is_string($VN) || strlen($VN) > 110) {
		die("18cm30p ??? =)))");
	}
	else {
		$VN = "echo ".$VN.";";
		eval($VN);
	}
} else {
	if (isset($_GET['check'])) {
		echo phpinfo();
	}
	else {
		highlight_file(__FILE__);
	}
}
?>
