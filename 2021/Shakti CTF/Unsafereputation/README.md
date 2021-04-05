Unsafereputation
===
**Category:** Web

### Description
- Source : `main.js`

### Overview
- Trang web chỉ cho chúng ta nhận được một thống báo `Hey aren't you missing something??` và ngoài ra không có bất cứ thứ gì.

### Solution
- Vì chúng ta không nhận được hay thấy chỗ nào để input vào ở site nhưng author cũng cấp cho chúng ta một source code `main.js` và bây giờ chúng ta sẽ phân tích nó.
- Đọc code thì chúng ta thấy chương trình được viết bằng nodejs và sử dụng express. Chỉ có một path là `/` và đâu vào của chúng ta là `text` được lưu vào biến `inp`. Chúng ta có blacklist bao gồm `['system', 'child_process', 'exec', 'spawn', 'eval']` để check input của chúng ta.
- Input của chúng ta được đưa vào function `eval` và được in ra màn hình với nội dung `Welcome to the world ' + eval(inp)`.
- Nguy hiểm ở đây là input của chúng ta được đưa vào function `eval` và có thể thực thi code. Vậy bây giờ chúng ta chỉ cần tìm những function có thể RCE mà không nằm trong bộ filter.

##### Payload
- Vì mình thấy require và fs không bị filter nên mình quyết định sử dụng class `fs` này để solved bài này
`require('fs').readdirSync('.').toString()` -> scandir ở thư mục hiện tại
Author giấu flag khá kĩ nên sau một time khá lâu thì mình đã tìm được flag ở trong `/app/hosts`
`require('fs').readFileSync('/app/hosts').toString()` -> đọc file hosts và có flag trong đó.