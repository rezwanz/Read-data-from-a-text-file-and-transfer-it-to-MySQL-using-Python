import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    port = '3306',
    database = 'test_python'
)

# cursor = conn.cursor()
# conn.commit()

if conn.is_connected():
    print('Connection successful!')
else:
    print('Connection failed!')
    
conn.close()