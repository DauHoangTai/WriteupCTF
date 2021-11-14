import sqlite3
import hashlib

def login_check(username, password):
	conn = sqlite3.connect('db/xservice_users.db')
	row = conn.execute("SELECT * from users where username = ? and password = ?", (username, hashlib.md5(password.encode()).hexdigest(), )).fetchall()
	return row

def check_user(username):
	conn = sqlite3.connect('db/xservice_users.db')	
	row = conn.execute("SELECT * from users where username = ?", (username,)).fetchall()
	if len(row) > 1:
		return True
	return False
