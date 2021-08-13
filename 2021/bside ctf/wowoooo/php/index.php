<?php
include 'flag.php';
function filter($string){
    $filter = '/flag/i';
    return preg_replace($filter,'flagcc',$string);
}
$username=$_GET['name'];
$pass="V13tN4m_number_one";
$pass="Fl4g_in_V13tN4m";
$ser='a:2:{i:0;s:'.strlen($username).":\"$username\";i:1;s:".strlen($pass).":\"$pass\";}";

$authen = unserialize(filter($ser));

if($authen[1]==="V13tN4m_number_one "){
    echo $flag;
}
if (!isset($_GET['debug'])) {
    echo("PLSSS DONT HACK ME!!!!!!").PHP_EOL;
} else {
    highlight_file( __FILE__);
}
?>
<!-- debug -->