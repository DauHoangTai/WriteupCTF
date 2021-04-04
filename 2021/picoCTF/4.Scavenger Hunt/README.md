Scavenger Hunt
===
**Category:** Web

**Author:** MADSTACKS

### Description
There is some interesting information hidden around this site

### Overview
- Đầu tiên vào kiểm tra site thì ta thấy được một site khá bình thường và kiểm tra mã nguồn thì thấy được part 1 của flag là `picoCTF{t`

### Solution
- Step 1: Kiểm tra mã nguồn ta thấy được part 1 flag: `picoCTF{t`
- Step 2: Trong mã nguồn kiểm tra file `mycss.css` thì thấy được part 2 của flag: `h4ts_4_l0`
- Step 3: Truy cập path `robots.txt` thì nhận được part 3 của flag : `t_0f_pl4c`
- Step 4: Ở robots.txt ta nhận được đoạn văn bản `I think this is an apache server... can you Access the next flag?` và nghĩ đến file `.htaccess`. Truy cập vào `.htaccess` ta nhận được part 5 của flag: `3s_2_lO0k`
- Step5: Truy cập `.DS_store` ta nhận được part cuối của flag
