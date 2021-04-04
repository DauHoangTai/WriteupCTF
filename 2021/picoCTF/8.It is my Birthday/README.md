It is my Birthday
===
**Category:** Web

**Author:** MADSTACKS
### Description
I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website

### Overview
- Truy cập site thì chúng ta thấy được chương trình cho ta upload file lên và được input 2 file cùng một lần. Mình thử upload file bất kì lên thì nhận được thông báo `Not a PDF!` vì vậy chương trình bắt buộc chúng ta phải upload file `.pdf`. Vì vậy mình đã tạo một file `a.pdf` với content là `abc` và cùng chọn ở file1 và file2 đều là `a.pfd` thì nhận được thông báo `Files are not different!`.
- Tiếp tục mình thử tạo thêm 1 file khác là `b.pdf` với content là `bcd` thì khi upload file `a.pdf` và file `b.pdf` lên thì nhận được thông báo `MD5 hashes do not match!`. 
- Mình thử tiếp để file `a.pdf` và file `b.pdf` cùng content là `abc` thì lại nhận được thông báo `Files are not different!` -> chương trình kiểm tra content của 2 file và md5 content đó xong so sánh với nhau.

### Solution
- Tới đây mình nghĩ rằng có thể là chương trình chỉ sử dụng 2 dấu == để so sánh vì vậy chúng ta có thể bypass được đoạn so sánh ở 2 chuỗi sau khi md5 với nhau.
File `a.pdf`
```
240610708
```
File `b.pdf`
```
QNKCDZO
```
- Sau khi upload lên thì đã thành công và chương trình hiện luôn source code và flag. Đọc qua source thì nhận thấy được idea mình nghĩ đã đúng, chương trình chỉ sử dụng `==` để so sánh content của file sau khi md5 vì vậy chúng ta có thể bypass nó.
```php
<?php

if (isset($_POST["submit"])) {
    $type1 = $_FILES["file1"]["type"];
    $type2 = $_FILES["file2"]["type"];
    $size1 = $_FILES["file1"]["size"];
    $size2 = $_FILES["file2"]["size"];
    $SIZE_LIMIT = 18 * 1024;

    if (($size1 < $SIZE_LIMIT) && ($size2 < $SIZE_LIMIT)) {
        if (($type1 == "application/pdf") && ($type2 == "application/pdf")) {
            $contents1 = file_get_contents($_FILES["file1"]["tmp_name"]);
            $contents2 = file_get_contents($_FILES["file2"]["tmp_name"]);

            if ($contents1 != $contents2) {
                if (md5_file($_FILES["file1"]["tmp_name"]) == md5_file($_FILES["file2"]["tmp_name"])) {
                    highlight_file("index.php");
                    die();
                } else {
                    echo "MD5 hashes do not match!";
                    die();
                }
            } else {
                echo "Files are not different!";
                die();
            }
        } else {
            echo "Not a PDF!";
            die();
        }
    } else {
        echo "File too large!";
        die();
    }
}

?>
```