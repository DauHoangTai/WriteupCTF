<!DOCTYPE html>
<html>
<head>
	<title>cu rờ lờ service</title>
</head>
<body>
<h1>Welcome to my free service</h1>
<form action="/ssrf.php" >
	<input type="text" name="host">
	
</form>
</body>
</html>
<?php

function filter($args){
	$blacklists = ["127.0.0.1","0.0.0.0", "127.0.1","127.1","0","localhost","2130706433","0x7f000001","0177.0.0.1"];
	$whitelists = ["http" , "https"];
	if(!in_array($args["scheme"],$whitelists))
		{echo $args["scheme"];
		return 0;}
	else{
		if(in_array($args["host"],$blacklists) ){
			echo $args["host"];
			return 0;
		}
		if(strpos($args["query"],"dir_name")){
			return 0;
		}
	}
	return 1;
}
if(isset($_GET["host"])){
	if(filter_var($_GET["host"], FILTER_VALIDATE_URL)) {
		$r = parse_url($_GET["host"]);
	    if(filter($r)){
	    	$ch = curl_init();
	    	curl_setopt($ch, CURLOPT_URL,$_GET["host"] );

	    	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	    	
	    	$output = curl_exec($ch);
	    	curl_close($ch); 
	    	echo($output);
	    }
	    else
	    	die("dont hack me pls");
	}
}