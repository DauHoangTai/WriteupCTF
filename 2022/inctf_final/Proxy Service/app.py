from flask import Flask, request, render_template, Response
from urllib.parse import urlparse
import ipaddress
import os
import requests
import time
import socket

app = Flask(__name__)

# Original flag in env variable
str_flag = os.getenv('FLAG', "inctf{this_is_fake_flag}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/proxy", methods=["POST"])
def do_request():
    try:
        url = request.form["url"]
        domain = urlparse(url).netloc
        
        if ":" in domain:
            domain = domain.split(":")[0]

        ip = socket.gethostbyname(domain)

        # block access to internal IPs
        if ipaddress.ip_address(ip).is_private or url.startswith("http") == False:
            return render_template("index.html", message="Access denied !") 
        else:
            # Prevent Denial-of-Service attack
            time.sleep(3)
            print ("Requesting: ", ip)
            r = requests.get(url)
            body = r.text
            return body

    except:
        return render_template("index.html", message="Some error occured")

@app.route("/viewsource")
def source():
    resp = Response(open("app.py").read())
    resp.headers['Content-Type'] = 'text/plain'
    return resp


@app.route("/gimme_tha_fleg")
def flag():
    # Allow flag access to internal IPs only
    if request.access_route[-1] == "127.0.0.1":
        return f"Welcome, {request.access_route[-1]}. Your flag is <code>{str_flag}</code>"
    else:
        return "Get outta here!", 403
    
if __name__ == "__main__":
    app.run(debug=False)