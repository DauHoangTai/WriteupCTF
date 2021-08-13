<?php
// Flag is inside ./flag.php :)
($x=str_replace("`","",strval($_REQUEST["x"])))&&strlen(count_chars($x,3))<=5?print(eval("return $x;")):show_source(__FILE__)&&phpinfo();
