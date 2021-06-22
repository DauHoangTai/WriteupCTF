<?php
$a = "',pi  ()system(ls),'";
echo (strpos(substr($a,4,strlen($a)),"(")).PHP_EOL;
echo (substr($a,2+strpos(substr($a,4,strlen($a)),"("),2)).PHP_EOL;
?>