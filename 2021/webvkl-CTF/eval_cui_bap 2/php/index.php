<?php
error_reporting(0);
chdir("/");
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    if (preg_match("/[3-9`~!@#\$%^&*\-=+.,;?'\"\[\]\{\}\\\\]|\([2]|\_[a-q]|0|1|pcntl|highlight_file|var|root|len|func|contents|eval|count|cmp/i",$cmd) || substr_count($cmd,'ext') > 1 || substr_count($cmd,'scan') > 1) {
        die("ấu nâu !");
    } else {
        eval($cmd.";");
    }
} else {
    highlight_file(__FILE__);
}

?>