from flask import Flask, request
import jwt, time, os
import query, init


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

private_key = open('priv.pem').read()
public_key = open('pub.pem').read()

@app.route("/get_token")
def get_token():
  return jwt.encode({'username': 'admin', 'now': time.time()}, private_key, algorithm='RS256')


@app.route("/admin", methods=['POST'])
def get_flag():
  try:
    payload = jwt.decode(request.form['jwt'], public_key, algorithms='RS256')
    if 'admin' in payload['username']:
      return query.query(payload['username'])
    else: return "You're not admin !!!"
  except:
    return "0ops, it's wrong way"
  #except Exception as e: print(e)

@app.route("/")
def home():
  return "I think RS256 is safe. Do you agree with me?"
if __name__ == "__main__":
  init.init_database()
  app.run(host="0.0.0.0")