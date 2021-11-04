import flask
import requests
import os
import urllib
import subprocess
from waitress import serve
from requests_file import FileAdapter

app = flask.Flask(__name__, static_url_path='')
home = os.path.dirname(os.path.realpath(__file__)) # /src

@app.route('/', methods=['GET'])
def index():
	return flask.render_template('index.html')

@app.route('/runScript', methods=['POST'])
def runScript():
	dir = flask.request.form.get('script_dir')
	name = flask.request.form.get('script_name')
	url = flask.request.form.get('script_url')
	command_log = flask.request.form.get('command_log_file')
	msg = start(dir, name, url, command_log)
	return ({'status': msg},200)

def check_script_dup(scripts, command_log, dir, name, url):
	try:
		script_parent_dir = scripts + '/' + dir
		script_path = script_parent_dir + '/' + name
	except:
		return "missing dir and name"
	if os.path.exists(script_path):
		return "duplicate script"
	else:
		if not os.path.exists(script_parent_dir):
			os.makedirs(script_parent_dir)
		return download_script(script_path, command_log, url)

def download_script(script_path, command_log, url):
	try:
		script_link = url
	except:
		return "missing url"
	r = requests.Session()
	r.mount('file://', FileAdapter())
	try:
		result = r.get(script_link)
	except:
		return "Oh no! Lost internet"
	with open(script_path, 'wb') as f:
		f.write(result.content)
		run_script(script_path, command_log)

def run_script(script_path, command_log):
	lf = open(command_log, 'wb+')
	command = subprocess.Popen(['bash', script_path], stderr=lf, stdout=lf, universal_newlines=True)
	return "Run successfully"

def start(dir, name, url, command_log):
	scripts = home + '/scripts'
	log = home + '/logs'
	if not os.path.exists(scripts):
		os.makedirs(scripts)
	if not os.path.exists(log):
		os.makedirs(log)
	try:
		command_log = log + '/' + command_log + '.txt'
	except:
		return "missing command_log"
	msg = check_script_dup(scripts, command_log, dir, name, url)
	return msg

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=8017)
