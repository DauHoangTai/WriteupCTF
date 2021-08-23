<?php
error_reporting(0);
chdir("/");
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    if (preg_match("/[3-9`~!@#\$%^&*\-=+,;?'\"\[\]\{\}\\\\]|0|pcntl|highlight_file|var|root|func|contents|eval|count|cmp/i",$cmd) || substr_count($cmd,'.') > 2 || strlen($cmd) > 64) {
        die("ấu nâu !");
    } else {
        eval($cmd.";");
    }
} else {
    highlight_file(__FILE__);
}

?>