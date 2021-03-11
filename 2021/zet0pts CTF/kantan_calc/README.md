kanta_calc
===
**Category:** Web

**Author:** st98

**Point:** 100 (50 solves)

### Description
- Source : `app.js`

### Solution
- Phân tích code:
```js
app.get('/', function (req, res, next) {
  let output = '';
  const code = req.query.code + '';

  if (code && code.length < 30) {
    try { 
      const result = vm.runInNewContext(`'use strict'; (function () { return ${code}; /* ${FLAG} */ })()`, Object.create(null), { timeout: 100 });
      output = result + '';
      if (output.includes('zer0pts')) {
        output = 'Error: please do not exfiltrate the flag';
      }
    } catch (e) {
      output = 'Error: error occurred';
    }
  } else {
    output = 'Error: invalid code';
  }

  res.render('index', { title: 'Kantan Calc', output });
});
```
Ở đoạn code này đầu vào của người dùng và flag sẽ được đưa vào và được thực thì trong sandbox. Ở trong vm author đã thêm mode `use strict` và đầu ngoài của người dùng tối đã 29 kí tự, đầu ra của chương trình nếu có `zer0pts` thì sẽ in ra `Error: please do not exfiltrate the flag`
Chúng ta không thể call trực tiếp `FlAG` vì nó ở nằm trong vm và không thể escape bằng `contructor.constructor()` vì không đủ len.
Nếu như author không sử dụng mode strict thì chúng ta có thể dump hết câu lệnh chứa flag đó bằng cách sử dụng `arguments.callee`. Đó mục đích của author sử dụng mode strict.
Vậy ở đây chúng ta sử dụng dấu `,` để phân cách các expression (như dấu `;`) sau đó ta tạo một function mới với một tên bất kì càng ngắn càng tốt vì đỡ tốn len (tốt nhất là 1 kí tự) để return về một mảng và tiếp tục ép kiểu từ function về string bằng cách nối chuỗi là sử dụng dấu `+`. Cuối cùng sử dụng `...` để tách chuỗi ra từ string qua mảng để bypass includes

###### Payload
```js
},function a(){return [...+'abc']
```