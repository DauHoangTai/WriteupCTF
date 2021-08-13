<?php

include "config.php";
function filter($str) {
    if(preg_match("/system|exec|passthru|shell_exec|pcntl_exec|bin2hex|popen|scandir|hex2bin|[~$.^_`]|\'[a-z]|\"[a-z0-9]/i",$str)) {
        return false;
    } else {
        return true;
    }
}
class BSides {
    protected $option;
    protected $name;
    protected $note;

    function __construct() {
        $option = "no flag";
        $name = "guest";
        $note = "flag{flag_phake}";
        $this->load();
    }

    public function load()
    {
        if ($this->option === "no flag") {
            die("flag here ! :)");
        } else if ($this->option === "getFlag"){
            $this->loadFlag();
        } else {
            die("You don't need flag ?");
        }
    }
    private function loadFlag() {
        if (isset($this->note) && isset($this->name)) {
            if ($this->name === "admin") {
                if (filter($this->note) == 1) {
                    eval($this->note.";");
                } else {
                    die("18cm30p !! :< ");
                }
            }
        }
    }

    function __destruct() {
        $this->load();
    }
}

if (isset($_GET['ctf'])) {
    $ctf = (string)$_GET['ctf'];
    if (check($ctf)) { //check nullbyte
        unserialize($ctf);
    }
} else {
    highlight_file(__FILE__);
}
?>