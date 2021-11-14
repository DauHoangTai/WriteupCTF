import random
import os
from xlib import utils as xutils
from flask import Flask, render_template, render_template_string, url_for, redirect, session, request
from flask_socketio import SocketIO, emit, send
from xml.etree import ElementTree, ElementInclude

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('KEY')
socketio = SocketIO(app)

@app.route('/')
def index():
	if 'username' in session:
		return redirect(url_for('dashboard'))
	return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
	if 'username' in session:
		return render_template('dashboard.html', name=session['username'])
	return redirect(url_for('login'))


@app.route('/login', methods = ['GET', 'POST'])
def login():
	if 'username' in session:
		redirect(url_for('/dashboard'))
	else:
		if request.method == 'POST':
			username, password, guest = '', '', ''
			try:
				username = request.form["username"]
				password = request.form["password"]
			except:
				pass

			try:
				guest = request.form["guest"]
			except:
				pass

			if len(username)>0 and len(password) > 0:
				res = xutils.login_check(username, password)
				if len(res)>0:
					session['is_admin'] = 0
					session['username'] = username
			elif guest != None and guest == "true":
				session['is_admin'] = 0
				session['username'] = 'guest%s'%(random.randrange(1000000, 9999999))
			return redirect(url_for('dashboard'))
		return render_template('login.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('login'))

@app.route('/manage')
def manage():
	try:
		if session['is_admin'] == 1:
			if xutils.check_user(session['username']) == True:
				return render_template_string('Hello ' + session['username'] + ', under development!')
			else:
				return render_template_string(session['username'].replace("{{","") + "Not available")
		else:
			return redirect(url_for('dashboard'))
	except:
		return redirect(url_for('login'))

@socketio.on('message')
def handle_message(xpath, xml):
	if 'username' in session:
		if len(xpath) != 0 and len(xml) != 0 and "&" not in xml:
			try:
				res = ''
				root = ElementTree.fromstring(xml.strip())
				ElementInclude.include(root)
				for elem in root.findall(xpath):
					if elem.text != "":
						res += elem.text + ", "
				emit('result', res[:-2])
			except Exception as e:
				emit('result', 'Nani?')
		else:
			emit('result', 'Nani?')


@socketio.on('my event')
def handle_my_custom_event(json):
	print('received json: ' + str(json))

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=8003)

