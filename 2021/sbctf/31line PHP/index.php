<?php
session_start();
if (!isset($_POST["data"])) {
    highlight_file(__FILE__);
    die();
}
if (!isset($_SESSION["id"])) {
    $_SESSION["id"] = md5(random_bytes(16));
}
$id = $_SESSION["id"];
echo "Welcome, $id\r\n";

if (!file_exists("/var/www/html/upload/" . $id)) {
    mkdir("/var/www/html/upload/" . $id, 0755, true);
}
$name = $_FILES["data"]["name"];
var_dump($name);
move_uploaded_file($_FILES["data"]["tmp_name"],"/var/www/html/upload/$id/$name");
if (PHP_VERSION_ID < 80000) {
    // This function has been deprecated in PHP 8.0 because in libxml 2.9.0, external entity loading is
    // disabled by default, so this function is no longer needed to protect against XXE attacks.
    $loader = libxml_disable_entity_loader(true);
}
$xmlfile = file_get_contents("/var/www/html/upload/$id/$name");
$dom = new DOMDocument();
$dom->loadXML($xmlfile, LIBXML_NOENT);
$creds = simplexml_import_dom($dom);
$user = $creds->user;
$pass = $creds->pass;
echo "You have logged in as user $user";
unlink("/var/www/html/upload/$id/$name");
?>