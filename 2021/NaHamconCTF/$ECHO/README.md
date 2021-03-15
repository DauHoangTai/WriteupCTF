$ECHO
===
**Category:** Web

**Author:** @Blacknote#1337

**Point:**

### Description
- ```So I just made a hardcoded bot that basically tells you what you wanna hear. Now usually it's a $ for each thing you want it to say but I'll waive the fee for you if you beta test it for me.```

### Overview
- Đầu tiên chúng ta vào trang web thì có có một chỗ cho chúng ta input đầu vào và khi nhập bất kì thứ gì thì nó sẽ trả về cho chúng ta kết quả như chúng ta nhập vào. Như vậy có thể thấy được nó là một `echo` trong bash như tên của đề bài.

### Solution
- Bây giờ chúng ta đã biết được cấu trúc của chương trình là đầu vào của chúng ta sẽ nằm phía sau echo vì vậy nó sẽ in ra màn hình cho chúng ta kết quả của chúng ta nhập vào. 
- Chương trình có thể như : `echo {input của chúng ta}` và nó nằm trong sanbox
- Vậy bây giờ chúng ta cần kiếm command nào đó để có thể bypass được echo và get flag.
- Đầu tiên mình sử dụng backticks và list được toàn bộ file của chương trình ![image](https://user-images.githubusercontent.com/54855855/111065275-716bc000-84eb-11eb-99b1-75a3e2ab8d63.png)
và kiểm tra như này thì chúng ta thấy được file flag.txt
![image](https://user-images.githubusercontent.com/54855855/111065312-97916000-84eb-11eb-9ca7-cfe267fe0f65.png).
- Đọc file index.php bằng cách `cat index.php` nó chứa gì thì ta nhận được đoạn source sau
```php
<?php $to_echo = $_REQUEST['echo'];
$cmd = "bash -c 'echo " . $to_echo . "'";
if (isset($to_echo))
{
    if ($to_echo == "")
    {
        print "Please don't be lame, I can't just say nothing.";
    }
    elseif (preg_match('/[#!@%^&*()$_+=\-\[\]\';,{}|":>?~\\\\]/', $to_echo))
    {
        print "Hey mate, you seem to be using some characters that makes me wanna throw it back in your face >:(";
    }
    elseif ($to_echo == "cat")
    {
        print "Meowwww... Well you asked for a cat didn't you? That's the best impression you're gonna get :/";
    }
    elseif (strlen($to_echo) > 15)
    {
        print "Man that's a mouthful to echo, what even?";
    }
    else
    {
        system($cmd);
    }
}
else
{
    print "Alright, what would you have me say?";
} ?>

``` 
- Đọc qua source code chúng ta có thì thấy được nếu chúng ta nhập vào `cat ../flag.txt` thì chuỗi đã dài hơn 15 kí tự và không thể đọc được. Ở đây mình đã từng làm một bài và cũng bị filter các kí tự tương tự như trên thì mình đã quyết định sử dụng lại đó là dấu `<`

##### Payload
- `<..flag.txt` nằm trong backticks
Giải thích về dấu `<` thì chúng ta có thể hiểu rằng là chương trình sẽ nhận đầu vào là nội dung của tệp thay vì nhập từ bàn phím và sau đó echo ra thì sẽ show tất cả nội dung trong file flag đó ra 