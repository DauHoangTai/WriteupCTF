<?php
$l = @$_GET['l'];
if ($l) include $l;
?>

<h1>Try rce me!</h1>
<h2>
  <a href="?l=/etc/passwd">?l=/etc/passwd</a>
</h2>
