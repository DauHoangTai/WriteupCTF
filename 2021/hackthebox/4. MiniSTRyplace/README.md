 MiniSTRyplace
 ===
 ### Description
 Let's read this website in the language of Alines. Or maybe not?

 ### Overview
 - Trang web khá bình thường và chỉ có phần thay đổi ngôn ngữ cho trang web. Ở phần mã nguồn cũng không cung cấp bất kì thứ gì cho chúng ta.
- Chúng ta được cung cấp source code của chall này nên chúng ta sẽ phân tích nó.

### Solution
- Phân tích code: Chương trình được viết bằng php và sử dụng nginx. 
- File `index.php` ở folder `/challenge/static`: 
![image](https://user-images.githubusercontent.com/54855855/115953313-e97acc00-a514-11eb-9f91-7953068c7b54.png)
Focus vào đoạn code này thì chúng ta có thấy được tham số `lang` khi truyền vào thì nó sẽ được thực hiện ở trong `include` và nếu như `lang` chứa ../ thì chúng sẽ bị triệt tiêu đi. Vậy chúng ta chỉ cần bypass ../ làm sao cho khi ../ bị filter nhưng nó vẫn còn lại chuỗi ../ -> khai thác theo kiểu LFI

### Payload
`?lang=....//....//flag`
Khi chúng ta nhập payload như trên thì replace sẽ thực hiện filter đi `../` và sẽ trở thành `../../flag`