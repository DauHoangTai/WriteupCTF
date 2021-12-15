<?php
include __DIR__."/lib2.php";
if (isset($_GET['url'][15]))
{
    header("location: {$_GET['url']}");
    echo "Your url is interesting, here is prize {$flag} <br>";
}
else
{
    echo "Plz make me interest with your url <br>";
}
show_source(__FILE__);
?>