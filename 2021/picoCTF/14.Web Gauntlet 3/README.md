Web Gauntlet 3
===
**Category:** Web

**Author:** MADSTACKS
### Description
Last time, I promise! Only 25 characters this time. Log in as admin

### Overview
- Ở chall này thì form và tất cả đều giống như chall v2 chỉ khác là tổng length của username và pass không được > 25

### Solution
- Do ở bài v2 mình sử dụng payload ngắn hơn 25 rồi nên ở bài này mình sử dụng lại payload của bài v2 để giải quyết bài này luôn

##### Payload
- `user=adm'||'in'%00&pass=a`