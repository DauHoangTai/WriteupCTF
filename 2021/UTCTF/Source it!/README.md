Source it!
===

**Category:** Web

**Author:**  Rob H

**Point:**

### Description
- Can you see how this page handles authentication?
- Site: http://web1.utctf.live:8778/

### Overview
- Đầu tiên ta vào trang web thì chúng thấy form login, kiểm tra source bằng F12 thì ta thấy được có 1 đoạn code bằng js và chỉ cần đăng nhập vào admin thì có flag

### Solution
```js
 function checkPassword(form) { 
                password1 = form.password1.value; 
                name = form.name.value;
                var username = "admin";
                var hash = "1bea3a3d4bc3be1149a75b33fb8d82bc"; 
                var hashedPasswd = CryptoJS.MD5(password1);
   
                if (password1 == '') 
                    alert ("Please enter Password"); 
              
                else if (username != name) { 
                    alert ("\nYou lack access privlages...") 
                    return false; 
                }
                     
                else if (hash != hashedPasswd) { 
                    alert ("\nIncorrect password...") 
                    return false; 
                } 
  
                else{ 
                    alert("Access Granted\n" + text) 
                    return true; 
                } 
            } 
```
- Ở đoạn code trên ta thấy username bằng `admin` và password thì bằng md5 của `1bea3a3d4bc3be1149a75b33fb8d82bc`
- Crack đoạn mã của password thì ta được `password:sherlock`
- Vậy chúng ta chỉ đăng nhập bằng `username:admin` và `password:sherlock` và chúng ta có flag