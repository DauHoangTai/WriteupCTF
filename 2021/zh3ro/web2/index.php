<?php
ini_set('display_errors',0);
include("flag.php");
if(!isset($_GET['user'])) highlight_file(__FILE__);
else{
      $a=$_GET['user'];    
      if(strlen($a)>24 || gettype($a)!=="string" ){
  die("oh nâu!!");
}
if(preg_match("/\;|\^|\~|\&|\||\[|n|\]|\\$|\.|\`|\"|\||\+|\-|\>|\?|c|\>/i",$a)){
  $a=md5($a);
}
//',pi  (),system(ls),'
if((strpos(substr($a,4,strlen($a)),"(")>1||strpos(substr($a,6,strlen($a)),")")>1)&&
  (preg_match("/[A-Za-z0-9_]/i",substr($a,2+strpos(substr($a,4,strlen($a)),"("),2))||
   preg_match("/[A-Za-z0-9_']/i",substr(substr(substr($a,4,strlen($a)),strpos(substr($a,4,strlen($a)),"("),12),strpos(substr(substr($a,4,strlen($a)),strpos(substr($a,4,strlen($a)),"("),12),")")-1,1))))
{
  $a=md5($a);
}

eval("echo 'Hello ".$a."abc';");
}

