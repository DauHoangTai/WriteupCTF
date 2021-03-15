AgentTester
===
**Category:** Web

**Author:** @jorgectf#3896

**Point:**

### Description
```
We've recently hired an entry-level web developer to build an internal system to test User Agents, let us know if you find any errors!
```
- Source: `src.zip`

### Overview
- Đầu tiên vào chúng ta thấy một form đăng nhập và có form đăng kí. Khi mình đăng kí với username là admin thì có thông báo là username này đã được sử dụng vì vậy mình đã nghĩ access admin sẽ có gì hay ho trong đó. Sau đó mình đăng kí một tài khoản bất kì và đăng nhập vô thì thấy một form cho chúng ta input vào. 
- Bây giờ mở source lên đọc (`app.py`) thì thấy 2 đoạn code cần focus vào.
```py
@app.route("/debug", methods=["POST"])
def debug():
    sessionID = session.get("id", None)
    if sessionID == 1:
        code = request.form.get("code", "<h1>Safe Debug</h1>")
        return render_template_string(code)
    else:
        return "Not allowed."
```
Ở đoạn code này thì chương trình sẽ check `sessionID` nếu là admin thì sẽ render ra đoạn code đó nếu không sẽ in ra `Not allowed`. Vì vậy ở đoạn này sau khi chúng ta đăng nhập vô được admin thì chúng ta có thể ssti vì nó sẽ render ra input của chúng ta.
```py
try:
    query = db.session.execute(
        "SELECT userAgent, url FROM uAgents WHERE userAgent = '%s'" % uAgent
    ).fetchone()

    uAgent = query["userAgent"]
    url = query["url"]
except Exception as e:
    ws.send(str(e))
    return
```
Đoạn code này thì chúng ta có thể sql injection ở `uAgent` vì đầu vào không được làm sạch sau khi được đưa vào chương trình chạy. Mà `uAgent` chính là đầu vào của chúng ta khi đăng nhập vào tài khoản của mình.

### Solution
- Sau khi phân tích code như trên thì bây giờ chúng ta chỉ cần làm từng bước đó là `sql injection -> ssti`
- SQl injection để lấy account của admin và sau đó đã được check session là admin thì ssti để rce lấy flag
- Ở trong thư mục backend của author đã cho thì thấy cấu trúc database: Table là `user` và có 2 cột là `username,password`

##### Payload
- Query sqlinjection: `' UNION SELECT username,password FROM user where id=1; -- -`
Kết quả nhận được: ```username:admin pasword:*)(@skdnaj238374834**__**=```
- Đã có pass của admin thì chúng ta đăng nhập vô sau đó ssti và kiểm tra ở file `run.sh` thì thấy flag ở biến mỗi trường là `CHALLENGE_FLAG`
- Final payload : ![image](https://user-images.githubusercontent.com/54855855/111076379-afcea280-851e-11eb-832f-0debdd197b87.png)