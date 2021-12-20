import mysql.connector

#mydb = mysql.connector.connect(host="localhost", user="root",password="password",auth_plugin='mysql_native_password',database='chall_web')


def query(payload):
  config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql8',
        'port': '3306',
        'database': 'websec'
    }
  connection = mysql.connector.connect(**config)
  cursor = connection.cursor()
  if (waf(payload)):
    print('start query')
    cursor.execute("select * from users where uname = '{0}'".format(payload))
    result = cursor.fetchall()
  cursor.close()
  connection.close()
  return ''.join(str(s) for s in result)
  
def waf(payload):
  blacklists = ['mysql', 'history','set','general_log',';', ' ', '#','-']
  for i in blacklists:
    if i in payload:
      return False
  return True
