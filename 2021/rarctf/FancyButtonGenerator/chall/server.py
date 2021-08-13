from flask import Flask, render_template, request
import requests

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button')
def button():
    title = request.args.get('title')
    link = request.args.get('link')
    return render_template('button.html', title=title, link=link)

@app.route('/admin')
def admin():
    title = request.args.get('title')
    link = request.args.get('link')
    r = requests.post("http://admin/xss/add", json={"title": title, "link": link}, headers={"Authorization": os.getenv("XSSBOT_SECRET")})
    print(r.text, flush=True)
    return 'Nice button! The admin has taken a look.'

app.run(host='0.0.0.0', port=5000)
