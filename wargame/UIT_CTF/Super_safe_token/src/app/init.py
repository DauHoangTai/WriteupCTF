import mysql.connector


def init_database():
    config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql8',
            'port': '3306',
            'database': 'websec'
        }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE flags (flag VARCHAR(50));""")
    cursor.execute("""INSERT INTO flags VALUE('Wanna.One{just_a_fake_flag}');""")
    cursor.execute("""DROP TABLE flags;""")
    cursor.close()
    connection.close()

