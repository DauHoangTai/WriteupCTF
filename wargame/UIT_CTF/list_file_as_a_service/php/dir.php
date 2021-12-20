<?php

echo 'User IP - '.$_SERVER['REMOTE_ADDR'];
if($_SERVER['REMOTE_ADDR']=== "127.0.0.1"){
	if(isset($_GET['dir_name'])){
		$dir = new DirectoryIterator($_GET['dir_name']);
		foreach ($dir as $key) {
			echo $key->getType();
		}
	}
	if(isset($_GET['file'])){
		var_dump(file_get_contents($_GET['file']));
	}
}
else{
	highlight_file(__FILE__);
}