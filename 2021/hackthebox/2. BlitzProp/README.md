BlitzProp
===
### Description
A tribute page for the legendary alien band called BlitzProp!
This challenge will raise 33 euros for a good cause.

### Overview
- Trang web chỉ có một nơi chúng ta input vào là `name`.
- Chúng ta được cung cấp source của chall nên chúng ta cùng phân thích nó.
### Solution
Phân tích code: Chall này được viết bằng node js và sử dụng json. Focus vào file `index.js` ở thư mục `routes`.
Chúng ta có thể nhìn thấy được có một routes là `/api/submit` là nơi làm nhiệm vụ submit cái input của mình gửi lên.
Ở đoạn code này
![image](https://user-images.githubusercontent.com/54855855/115949691-f42b6600-a500-11eb-9eb7-40de2bcbb53f.png)
thì thấy được có một object được khởi tạo là `song` và input của chúng ta được gán thẳng vào `song` => `song[name] = input`
song.name phải là một trong những cái mà includes đó thì chúng ta mới có reponse là `pug.compile('span Hello #{user}, thank you for letting us know!')({ user:'guest' })`. Điều quan trọng ở đây là input của chúng ta được đưa thẳng vào object song và chúng ta có thể control nó => chúng ta có thể tấn công theo cách prototype pollution.
- Đầu tiên là đưa một tên bài hát hợp lệ để để đáp ứng các yêu cầu của lệnh if vì nếu không thì pug sẽ không được kích hoạt. Sau đó chúng ta modify payload và cho cat flag vào file main.js để không làm hỏng chương trình.

### Payload
```
{"song.name":"ASTa la vista baby",
     "__proto__.block": {
        "type": "Text", 
        "line": "process.mainModule.require('child_process').execSync('cat fl* > static/js/main.js')"
    }
}
```

### Flag
`CHTB{p0llute_with_styl3}`